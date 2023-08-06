"""Implementation of the SystemC class

This class inherits from the SIT base class and implements its own methods of parsing,
modifying and generating boilerplate code for its specific paradigms.
"""
from ..sit import SIT


class SystemC(SIT):
    def __init__(
        self,
        module_name,
        lib,
        ipc="sock",
        module_dir="",
        lib_dir="",
        desc="",
        width_macros=None,
    ):
        """Constructor for SystemC SIT

        Parameters:
        -----------
        ipc : str (options: "sock", "zmq")
            method of IPC
        module : str
            SST element component and HDL module name
        lib : str
            SST element library name
        module_dir : str (default: "")
            directory of HDL module
        lib_dir : str (default: "")
            directory of SIT library
        desc : str (default: "")
            description of the SST model
        driver_template_path : str (default: "")
            path to the black box-driver boilerplate
        component_template_path : str (default: "")
            path to the black box-model boilerplate
        """
        super().__init__(
            module_name=module_name,
            lib=lib,
            ipc=ipc,
            module_dir=module_dir,
            lib_dir=lib_dir,
            desc=desc,
            width_macros=width_macros,
        )

        if self.ipc == "sock":

            # driver attributes
            self.sig_type = "SITSocketBuffer"

        elif self.ipc == "zmq":

            # driver attributes
            self.sig_type = "SITZMQBuffer"

        self.paths.set_driver_path(f"{self.module_name}_driver.cpp")
        self.paths.set_comp_path(f"{self.module_name}_comp.cpp")

    def _parse_signal_type(self, signal):
        """Parse the type and computes its size from the signal

        Parameters:
        -----------
        signal : str
            signal definition

        Returns:
        --------
        int
            signal width
        """

        def __get_ints():
            """Extract integers from signal string
            This is a closure method to keep scope local

            Returns:
            --------
            int
                integers found in signal string
            """
            try:
                return self._get_ints(signal)
            except ValueError:
                return int(self._get_signal_width_from_macro(signal))

        # SystemC member data types
        if "sc" in signal:

            if any(x in signal for x in ("bv", "lv", "int")):
                return self._get_num_digits(__get_ints())

            elif any(x in signal for x in ("bit", "logic")):
                return __get_ints()

        # boolean signals
        elif signal == "<bool>":
            return 1

        # arbitrary precision for float signals
        elif signal == "<float>":
            return 12

        # default C++ data types
        else:
            return __get_ints()

    def _get_driver_outputs(self):
        """Generate output bindings for both the components in the black box

        Returns:
        --------
        str
            snippet of code representing output bindings
        """
        return self._sig_fmt(
            "_data_out << {precision}{sig}",
            lambda x: {
                "sig": x["name"],
                "precision": f"std::fixed << std::setprecision({self.precision}) << "
                if self.precision
                else "",
            },
            self.ports["output"],
            ";\n" + " " * 8,
        )

    def _get_driver_inputs(self):
        """Generate input bindings for the driver.

        Returns:
        --------
        str
            snippet of code representing input bindings
        """
        fmt = "{sig} = std::sto{type}(_data_in.substr({sp}, {sl}));"
        start_pos = 1
        clock_fmt = "{sig} = std::stoi(_data_in.substr({sp}, {sl})) % 2;"
        driver_inputs = []

        # input_port = (INPUT NAME, INPUT TYPE)
        for input_port in self.ports["input"]:
            driver_inputs.append(
                fmt.format(
                    type="f" if input_port["type"] == "<float>" else "i",
                    sp=start_pos,
                    sl=str(input_port["len"]),
                    sig=input_port["name"],
                )
            )
            start_pos += input_port["len"]

        if self.ports["clock"]:
            for clock_port in self.ports["clock"]:
                driver_inputs.append(
                    clock_fmt.format(
                        sp=start_pos,
                        sl=clock_port["len"],
                        sig=clock_port["name"],
                    )
                )
                start_pos += int(clock_port["len"])

        self.driver_buf_size = start_pos
        return ("\n" + " " * 8).join(driver_inputs)

    def __get_driver_port_defs(self):
        """Generate port definitions for the black box-driver

        Returns:
        --------
        str
           string format of driver port definitions
        """
        return "sc_signal" + ";\n    sc_signal".join(
            i["type"] + " " + i["name"] for i in self._get_all_ports()
        )

    def __get_driver_bindings(self):
        """Generate port bindings for the black box-driver

        Returns:
        --------
        str
            snippet of code representing port bindings
        """
        return self._sig_fmt(
            fmt="DUT.{sig}({sig})",
            split_func=lambda x: {"sig": x["name"]},
            array=self._get_all_ports(),
            delim=";\n    ",
        )

    def _get_driver_defs(self):
        """Map definitions for the SystemC driver format string

        Returns:
        --------
        dict(str:str)
            format mapping of template SystemC driver string
        """
        return {
            "extra_libs": self.extra_libs,
            "module_dir": self.paths.get_module_dir().resolve(),
            "lib_dir": self.lib_dir,
            "module_name": self.module_name,
            "disable_warning": self.disable_warning,
            "port_defs": self.__get_driver_port_defs(),
            "bindings": self.__get_driver_bindings(),
            "sender": self.sender,
            "receiver": self.receiver,
            "buf_size": self.driver_buf_size,
            "sig_type": self.sig_type,
        }

    def _fixed_width_float_output(self):
        """Add <iomanip> library to handle ports with float signals"""
        self.extra_libs += "#include <iomanip>"

    def _disable_runtime_warnings(self, warning):
        """Add sc_report_handler to disable driver runtime warnings

        Parameters:
        -----------
        warning : str
            runtime warning to ignore
        """
        self.disable_warning += (
            f"sc_report_handler::set_actions({warning}, SC_DO_NOTHING);"
        )

"""Implementation of the PyRTL class

This class inherits from the SIT base class and implements its own methods of parsing,
modifying and generating boilerplate code for its specific paradigms.
"""
from typing import Literal

from ..sit import SIT

class PyRTL(SIT):
    def __init__(
        self,
        module: str,
        lib: str,
        ipc: Literal["sock", "zmq"] = ...,
        module_dir: str = ...,
        lib_dir: str = ...,
        desc: str = ...,
    ) -> None: ...
    def _parse_signal_type(self, signal: str) -> int: ...
    def _get_driver_outputs(self) -> str: ...
    def _get_driver_inputs(self) -> str: ...
    def _get_driver_defs(self) -> dict[str, str]: ...

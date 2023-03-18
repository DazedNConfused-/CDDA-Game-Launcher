from cddagl.platform_api import PosixNotImplementedError


class PyWinError(Exception):
    def __int__(self):
        raise PosixNotImplementedError()

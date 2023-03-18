from .utils import is_windows

if is_windows():
    from .win32 import *
    from pywintypes import error as PyWinError
else:
    from .posix import *
    from cddagl.posix_polyfill.pywintypes import PyWinError


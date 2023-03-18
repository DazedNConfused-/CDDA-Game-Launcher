# SPDX-FileCopyrightText: 2015-2021 Rémy Roy
#
# SPDX-License-Identifier: MIT

from cddagl.platform_api import is_windows
def fix_pywin32_loading():
    try:
        import pywintypes
    except ImportError:
        import sys
        sys.path.append(r'win32')
        sys.path.append(r'win32\lib')
        import pywin32_bootstrap

if is_windows():
    fix_pywin32_loading()

import cddagl.launcher
cddagl.launcher.run_cddagl()

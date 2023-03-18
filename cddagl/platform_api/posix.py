import os

import psutil

from cddagl.platform_api.PosixNotImplementedError import PosixNotImplementedError


def get_ui_locale():
    return None


def process_id_from_path(processName):
    '''
    Get a list of all the PIDs of all the running processes whose name contains
    the given string processName
    '''
    pids = []
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.exe().lower():
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if len(pids):
        return pids[0]
    else:
        return None


def get_downloads_directory():
    raise PosixNotImplementedError()


def find_process_with_file_handle(path):
    raise PosixNotImplementedError()


def activate_window():
    raise PosixNotImplementedError()


def wait_for_pid():
    raise PosixNotImplementedError()


def get_documents_directory():
    return os.path.join(os.path.expanduser('~'))


def write_named_pipe():
    raise PosixNotImplementedError()


class SimpleNamedPipe:
    def __int__(self, name):
        raise PosixNotImplementedError()


class SingleInstance:
    def __int__(self):
        raise PosixNotImplementedError()

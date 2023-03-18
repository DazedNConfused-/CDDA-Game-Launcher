class PosixNotImplementedError(NotImplementedError):
    def __init__(self):
        default_message = 'Not implemented for posix!'
        super().__init__(default_message)

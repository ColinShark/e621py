from e621py import __version__


class BaseClient:

    APP_VERSION = "e621.py {}".format(__version__)

    def __init__(self):
        pass

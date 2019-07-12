from e621py import __version__


class EsixClient:

    APP_VERSION = "e621.py v{}".format(__version__)

    HEADER = {
    'User-Agent': "{} by Colin - colinshark.de".format(
        APP_VERSION)}

    def __init__(self):
        pass

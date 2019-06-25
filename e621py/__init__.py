__version__ = "0.0.1-develop"
__copyright__ = "Copyright (C) 2019 Colin <https://colinshark.de>"

HEADER = {
    'User-Agent': "e621py v{} by Colin - colinshark.de".format(
        __version__)}

from .client import *

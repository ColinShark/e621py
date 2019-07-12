# Module to rate-limit queries to the e621.net API
# Copied from https://gist.github.com/gregburek/1441055
# Adapted to work with Python 3.6 (time.clock() deprecation in 3.8)

import time

import requests

from e621py.esix.ext import EsixClient


def RateLimited(maxPerSecond):
    """Limit the requests to `x` per second
    """
    minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.perf_counter() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.perf_counter()
            return ret
        return rateLimitedFunction
    return decorate


@RateLimited(2)
def api_get(url: str, data: list) -> requests.Response:
    print(url)
    print(data[0])
    """Get the response from the e621 API

    Parameters
    ----------
    `url` (`str`):
        The URL to query

    `data` (`list`):
        List containing the data and Header

    Returns
    -------
    `requests.Response`
    """
    return requests.get(
        url=url,
        data=data[0],
        headers=data[1]
    ).json()

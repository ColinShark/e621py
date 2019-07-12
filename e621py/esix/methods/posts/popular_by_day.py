from typing import Generator

import requests

from e621py.esix.ext import EsixClient


class PopularByDay(EsixClient):
    def popular_by_day(self) -> Generator:
        """Get popular posts of the recent day.

        Parameters
        ----------
        No Parameters required.

        Returns
        -------
        `generator` - A generator containing the most popular posts of the
        recent day.
        """
        data = {}
        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/popular_by_day.json',
            params=data,
            headers=self.HEADER
        )
        for item in r.json():
            yield item

from typing import Generator

import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class PopularByDay(BaseClient):
    def popular_by_day(self) -> Generator:
        """Get popular posts of the recent day.

        Parameters
        ----------
        No Parameters required.

        Returns
        -------
        `generator` - A generator containing the most popular posts of the recent day.
        """
        data = {}
        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/popular_by_day.json',
            params=data,
            headers=HEADER
        )
        print(r.url)
        for item in r.json():
            yield item

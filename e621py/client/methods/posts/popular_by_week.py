from typing import Generator

import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class PopularByWeek(BaseClient):
    def popular_by_week(self):
        """Get popular posts of the recent week.

        Parameters
        ----------
        No parameters required.

        Returns
        -------
        `generator` - A generator containing the most popular posts of the
        recent week.
        """
        data = {}
        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/popular_by_week.json',
            params=data,
            headers=HEADER
        )
        print(r.url)
        for item in r.json():
            yield item

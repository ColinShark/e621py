from typing import Generator

import requests

from e621py.esix.ext import EsixClient


class PopularByMonth(EsixClient):
    def popular_by_month(self):
        """Get popular posts of the recent month.

        Parameters
        ----------
        No parameters required.

        Returns
        -------
        `generator` - A generator containing the most popular posts of the
        recent month.
        """
        data = {}
        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/popular_by_month.json',
            params=data,
            headers=self.HEADER
        )
        for item in r.json():
            yield item

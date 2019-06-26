from typing import Generator

import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class DeletedIndex(BaseClient):
    def deleted_index(
        self,
        user_id: int = None,
        page: int = None
    ) -> Generator:
        """Get the index of deleted posts.

        Parameters
        ----------
        `user_id` : `int`
            ID of the user to filter post uploads by

        `page` : `int`
            The page number to return

        Returns
        -------
        `generator` containing JSON objects
        """
        data = {
            'user_id': user_id,
            'page': page
        }
        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/deleted_index.json',
            params=data,
            headers=HEADER
        )
        for item in r.json():
            yield item

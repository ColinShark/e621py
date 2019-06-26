from types import SimpleNamespace
import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class DeletedIndex(BaseClient):
    def deleted_index(
        self,
        user_id: int = None,
        page: int = None
    ):
        """Get the index of deleted posts.

        Parameters
        ==========
        user_id : int
            ID of the user to filter post uploads by

        page : int
            The page number to return

        Returns
        =======
        generator
            A generator object.
        """
        data = {
            'user_id': user_id,
            'page': page
        }
        data['login'] = self.USERNAME
        data['password_hash'] = self.PASSWORD_HASH

        r = requests.get(
            url=self.url + '/post/deleted_index.json',
            params=data,
            headers=HEADER
        )
        print(r.url)
        for item in r.json():
            yield SimpleNamespace(**item)
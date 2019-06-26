import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class Show(BaseClient):
    def show(
        self,
        post_id: int = None,
        md5: str = None
    ) -> object:
        """Show a single post's information by ID or MD5 hash.

        Parameters
        ----------
        `id` (``int``):
            ID of the post to retrieve

        `md5` (``str``):
            MD5 of the post to retrieve

        Returns
        -------
        `JSON` Object
        """
        data = {
            'id': post_id,
            'md5': md5
        }
        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/show.json',
            params=data,
            headers=HEADER
        )
        return r.json()

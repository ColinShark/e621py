import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class CheckMD5(BaseClient):
    def check_md5(
        self,
        md5: str
    ) -> dict:
        """Check the md5 hash of a post

        Parameters
        ==========
        `md5` :`str`
            The md5 hash of a file to match

        Returns
        =======
        `generator`
            A generator that gives back the md5, whether a post exists and
            the post_id
        """
        data = {
            'md5': md5
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/check_md5.json',
            params=data,
            headers=HEADER
        )
        print(r.url)
        return r.json()

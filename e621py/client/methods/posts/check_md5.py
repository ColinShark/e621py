from types import SimpleNamespace
import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class CheckMD5(BaseClient):
    def check_md5(
        self,
        md5: str
    ) -> list:
        """Check the md5 hash of a post

        Parameters
        ==========
        md5 :str
            The md5 hash of a file to match

        Returns
        =======
        generator
            A generator that gives back the md5, whether a post exists and
            the post_id
        """
        data = {
            'md5': md5
        }

        data['login'] = self.USERNAME
        data['password_hash'] = self.PASSWORD_HASH

        r = requests.get(
            url=self.url + '/post/check_md5.json',
            params=data,
            headers=HEADER
        )
        print(r.url)
        return SimpleNamespace(**r.json())

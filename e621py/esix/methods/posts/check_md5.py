import requests

from e621py.esix.ext import EsixClient
from e621py.esix.ext.utils import api_get


class CheckMD5(EsixClient):
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
        JSON `object`
        """
        data = {
            'md5': md5
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        return api_get(
            url=self.url + '/post/check_md5.json',
            data=[data, self.HEADER]
        ).json()

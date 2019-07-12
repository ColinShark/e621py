import requests

from e621py.esix.ext import EsixClient


class Tags(EsixClient):
    def tags(
        self,
        post_id: int = None,
        md5: str = None
    ) -> object:
        """Get the tags of a post by ID or MD5 hash

        Parameters
        ----------
        `id` (`int`):
            ID of the post to retrieve the tags of.

        `md5` (`str`):
            MD5 of the post to retrieve tge tags of.

        Returns
        -------
        JSON `object`
        """
        data = {
            'id': post_id,
            'md5': md5
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.get(
            url=self.url + '/post/tags.json',
            params=data,
            headers=self.HEADER
        )
        return r.json()

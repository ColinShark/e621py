import requests

from e621py.esix.ext import EsixClient


class Flag(EsixClient):
    def flag(
        self,
        post_id: int,
        flag_option: int,
        inferior_parent: int = None
    ) -> object:
        """Flag a post for deletion.

        Parameters
        ----------
        `post_id` (`id`):
            ID of the post that is to be flagged.

        `flag_option` (`int`):
            The Reason why a post should be deleted.

        `inferior_parent` (`int`):
            Optional. The ID of the post that the flagged post is inferior to.

        Returns
        -------
        JSON `object`
        """
        data = {
            'id': post_id,
            'flag_option': flag_option,
            'inferior_parent': inferior_parent
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.post(
            url=self.url + '/post/flag.json',
            params=data,
            headers=self.HEADER
        )
        return r.json()

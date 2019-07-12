import requests

from e621py.esix.ext import EsixClient


class RevertTags(EsixClient):
    def revert_tags(
        self,
        post_id: int,
        history_id: int
    ) -> object:
        """Revert a post's tags to previous version

        Parameters
        ----------
        `post_id` (`int`):
            ID of the post.

        `history_id` (`int`):
            Version number to revert the tags to.

        Returns
        -------
        JSON `object`
        """
        data = {
            'id': post_id,
            'history_id': history_id
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.post(
            url=self.url + '/post/revert_tags.json',
            params=data,
            headers=self.HEADER
        )
        return r.json()

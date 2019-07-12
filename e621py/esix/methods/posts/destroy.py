import requests

from e621py.esix.ext import EsixClient


class Destroy(EsixClient):
    def destroy(
        self,
        post_id: int,
        reason: str,
        mode: int = None
    ) -> object:
        """Delete a post by ID. You must either own the post or be a moderator
        **Note:** The mode parameter is only required (to be 1) if you're
        attempting to permanently destroy a post. This method must be called a
        second time, after the post has been removed normally. You must be
        logged in and be ranked Janitor or higher.

        Parameters
        ----------
        `post_id` (`int`):
            ID of the post that is to be deleted.

        `reason` (`str`):
            The reason for deletion.

        `mode` (`int`):
            Set to 1 to permanently destroy the post. This only works on posts
            that have been removed previously.

        Returns
        -------
        JSON `object`
        """
        data = {
            'id': post_id,
            'reason': reason,
            'mode': mode
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.post(
            url=self.url + '/post/destroy.json',
            params=data,
            headers=self.HEADER
        )
        return r.json()

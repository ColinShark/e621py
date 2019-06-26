import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class Vote(BaseClient):
    def vote(
        self,
        post_id: int,
        score: int
    ) -> object:
        """Vote for a post. You can vote once per post per IP address.

        Parameters
        ----------
        `post_id` (`int`):
            ID of the post that is voted on.

        `score` (`int`):
            Upvote with `1`, downvote with `-1`.

        Returns
        -------
        JSON `object`
        """
        data = {
            'id': post_id,
            'score': score
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.post(
            url=self.url + '/post/vote.json',
            params=data,
            headers=HEADER
        )
        return r.json()

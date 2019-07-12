from typing import Union

import requests

from e621py.esix.ext import EsixClient


class Update(EsixClient):
    def update(
        self,
        post_id: int,
        tags: Union[str, list] = None,
        old_tags: Union[str, list] = None,
        rating: str = None,
        source: Union[str, list] = None,
        description: str = None,
        is_rating_locked: bool = None,
        is_note_locked: bool = None,
        parent_id: int = None,
        reason: str = None
    ) -> object:
        """Update the information of a post.

        Parameters
        ----------
        post_id (int):
            ID of the post that is to be updated.

        `tags` (`str` | `list`):
            The new tags.
            Either a space delimited list as string or a list of strings.

        `old_tags` (`str` | `list`):
            The old tags. This helps e621 handling simultaneous edits from
            multiple users. Either space delimited list as string of list of
            strings.

        `rating` (`str`):
            The rating. Can be `s`, `q` or `e` for safe, questionable and
            explicit, respectively.

        `source` (`str` | `list`):
            The source of the post. Either supply a string with HTML-encoded
            newlines (`%0A`) or a list of strings. Maximum of 5 allowed.

        `description` (`str`):
            The Description for the post.

        `is_rating_locked` (`bool`):
            Whether or not to prevent others from changing the rating.

        `is_note_locked` (`bool`):
            Whether or not to prevent others from changing the notes.

        `parent_id` (`int`):
            The ID of the parent post.

        `reason` (`str`):
            The reason for the edit.

        Returns
        -------
        JSON `object`
        """
        data = {
            'id': post_id,
            'post[tags]': tags,
            'post[old_tags]': old_tags,
            'post[rating]': rating,
            'post[source]': source,
            'post[description]': description,
            'post[is_rating_locked]': is_rating_locked,
            'post[is_note_locked]': is_note_locked,
            'post[parent_id]': parent_id,
            'reason': reason
        }

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        r = requests.post(
            url=self.url + '/post/update.json',
            params=data,
            headers=self.HEADER
        )
        return r.json()

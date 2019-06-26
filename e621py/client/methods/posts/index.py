from types import SimpleNamespace
import requests

from e621py import HEADER
from e621py.client.ext import BaseClient


class Index(BaseClient):
    def index(
        self,
        tags: str,
        limit: int = None,
        before_id: int = None,
        page: int = None,
        typed_tags: bool = False
    ) -> list:
        """The base URL is /post/index.json. Deleted posts are not returned.
        The most efficient method to iterate a large number of posts is to
        use before_id starting at the highest ID, and then successively
        request the lowest ID returned each time. When iterating using page,
        posts will shift between pages if posts meeting the tags search
        criteria are deleted or added to the site between requests. Page
        numbers greater than 750 will return an error.

        Parameters
        ==========
            tags : str
                The tag search query. Any tag combination that works on the
                website will work here.

            limit : int, optional
                How many posts you want to retrieve. There is a hard limit of
                320 posts per request. Defaults to the value set in user
                preferences.

            before_id : int, optional
                Returns the next [limit] posts with IDs lower than the given
                ID.

            page : int, optional
                Paginates the search query into pages of length [limit] and
                returns the given page. If before_id is supplied, this does
                nothing.

            typed_tags : bool, optional
                Set to true to return typed tag information. The tags value
                returned is a dictionary with each tag type as a key and then
                a list of tags of that type.

        Returns
        =======
        list
            A list of results.
        """
        data = {
            'tags': tags,
            'limit': limit,
            'before_id': before_id,
            'page': page
        }

        data['login'] = self.USERNAME
        data['password_hash'] = self.PASSWORD_HASH

        if typed_tags is True:
            data['typed_tags'] = True

        r = requests.get(
            url=self.url + '/post/index.json',
            params=data,
            headers=HEADER
        )
        print(r.url)
        for item in r.json():
            yield SimpleNamespace(**item)

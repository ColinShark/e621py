from .check_md5 import CheckMD5
from .create import Create
from .deleted_index import DeletedIndex
from .destroy import Destroy
from .flag import Flag
from .index import Index
from .popular_by_day import PopularByDay
from .popular_by_month import PopularByMonth
from .popular_by_week import PopularByWeek
from .show import Show
from .tags import Tags
from .update import Update
from .vote import Vote


class Posts(
    CheckMD5,
    Create,
    DeletedIndex,
    Destroy,
    Flag,
    Index,
    PopularByDay,
    PopularByMonth,
    PopularByWeek,
    Show,
    Tags,
    Update,
    Vote
):
    pass

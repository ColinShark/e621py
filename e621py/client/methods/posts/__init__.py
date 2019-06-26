from .index import Index
from .check_md5 import CheckMD5
from .deleted_index import DeletedIndex
from .popular_by_day import PopularByDay
from .popular_by_week import PopularByWeek
from .popular_by_month import PopularByMonth
from .show import Show


class Posts(
    Index,
    CheckMD5,
    DeletedIndex,
    PopularByDay,
    PopularByWeek,
    PopularByMonth,
    Show
):
    pass

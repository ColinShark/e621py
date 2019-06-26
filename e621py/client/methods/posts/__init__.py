from .index import Index
from .check_md5 import CheckMD5
from .deleted_index import DeletedIndex
from .popular_by_day import PopularByDay


class Posts(
    Index,
    CheckMD5,
    DeletedIndex,
    PopularByDay
):
    pass

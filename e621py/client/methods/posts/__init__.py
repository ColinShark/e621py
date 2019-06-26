from .index import Index
from .check_md5 import CheckMD5
from .deleted_index import DeletedIndex


class Posts(
    Index,
    CheckMD5,
    DeletedIndex
):
    pass

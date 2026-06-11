"""User store: a JSON-backed store of user records."""

from raglab_bak.util import StoreAccess
from raglab_bak.stores import stores_util


class UserStore(StoreAccess):
    def __init__(self):
        self.store = stores_util.mk_json_store()

from typing import Any, Optional, Tuple, Type, TypeVar, overload

from sqlalchemy import Column
from sqlalchemy.orm.query import Query

class _SessionClassMethods(object):
    @classmethod
    def close_all(cls): ...
    @classmethod
    def identity_key(cls, *args, **kwargs): ...
    @classmethod
    def object_session(cls, instance) -> Session: ...

class SessionTransaction(object):
    session: Any = ...
    nested: Any = ...
    def __init__(self, session, parent: Optional[Any] = ..., nested: bool = ...) -> None: ...
    @property
    def parent(self): ...
    @property
    def is_active(self): ...
    def connection(self, bindkey, execution_options: Optional[Any] = ..., **kwargs): ...
    def prepare(self): ...
    def commit(self): ...
    def rollback(self, _capture_exception: bool = ...): ...
    def close(self, invalidate: bool = ...): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...

_T = TypeVar("_T")

class Session(_SessionClassMethods):
    public_methods: Any = ...
    identity_map: Any = ...
    bind: Any = ...
    transaction: Any = ...
    hash_key: Any = ...
    autoflush: Any = ...
    autocommit: Any = ...
    expire_on_commit: Any = ...
    twophase: Any = ...
    def __init__(self, bind: Optional[Any] = ..., autoflush: bool = ..., expire_on_commit: bool = ...,
                 _enable_transaction_accounting: bool = ..., autocommit: bool = ...,
                 twophase: bool = ..., weak_identity_map: bool = ...,
                 binds: Optional[Any] = ..., extension: Optional[Any] = ...,
                 info: Optional[Any] = ..., query_cls: Any = ...) -> None: ...
    connection_callable: Any = ...
    @property
    def info(self): ...
    def begin(self, subtransactions: bool = ..., nested: bool = ...) -> SessionTransaction: ...
    def begin_nested(self) -> SessionTransaction: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def prepare(self): ...
    def connection(self, mapper: Optional[Any] = ..., clause: Optional[Any] = ...,
                   bind: Optional[Any] = ..., close_with_result: bool = ...,
                   execution_options: Optional[Any] = ..., **kw): ...
    def execute(self, clause, params: Optional[Any] = ...,
                mapper: Optional[Any] = ..., bind: Optional[Any] = ..., **kw): ...
    def scalar(self, clause, params: Optional[Any] = ...,
               mapper: Optional[Any] = ..., bind: Optional[Any] = ..., **kw): ...
    def close(self) -> None: ...
    def invalidate(self) -> None: ...
    def expunge_all(self): ...
    def bind_mapper(self, mapper, bind): ...
    def bind_table(self, table, bind): ...
    def get_bind(self, mapper: Optional[Any] = ..., clause: Optional[Any] = ...): ...
    @overload
    def query(self, entity: Type[_T], **kwargs) -> Query[_T]: ...
    @overload
    def query(self, entity: Column[_T], **kwargs) -> Query[Tuple[_T]]: ...
    @overload
    def query(self, *entities, **kwargs) -> Query[Any]: ...  # plugin is needed for precise type
    @property
    def no_autoflush(self): ...
    def refresh(self, instance, attribute_names: Optional[Any] = ..., lockmode: Optional[Any] = ...): ...
    def expire_all(self) -> None: ...
    def expire(self, instance, attribute_names: Optional[Any] = ...) -> None: ...
    def prune(self): ...
    def expunge(self, instance): ...
    def add(self, instance, _warn: bool = ...) -> None: ...
    def add_all(self, instances) -> None: ...
    def delete(self, instance): ...
    def merge(self, instance: _T, load: bool = ...) -> _T: ...
    def enable_relationship_loading(self, obj): ...
    def __contains__(self, instance): ...
    def __iter__(self): ...
    def flush(self, objects: Optional[Any] = ...) -> None: ...
    def bulk_save_objects(self, objects, return_defaults: bool = ..., update_changed_only: bool = ...): ...
    def bulk_insert_mappings(self, mapper, mappings, return_defaults: bool = ..., render_nulls: bool = ...): ...
    def bulk_update_mappings(self, mapper, mappings): ...
    def is_modified(self, instance, include_collections: bool = ..., passive: bool = ...): ...
    @property
    def is_active(self) -> bool: ...
    @property
    def dirty(self): ...
    @property
    def deleted(self): ...
    @property
    def new(self): ...

class sessionmaker(_SessionClassMethods):
    kw: Any = ...
    class_: Any = ...
    def __init__(self, bind: Optional[Any] = ..., class_: Any = ..., autoflush: bool = ...,
                 autocommit: bool = ..., expire_on_commit: bool = ...,
                 info: Optional[Any] = ..., **kw) -> None: ...
    def __call__(self, **local_kw): ...
    def configure(self, **new_kw): ...

def make_transient(instance) -> None: ...
def make_transient_to_detached(instance) -> None: ...
def object_session(instance) -> Session: ...
def close_all_sessions() -> None: ...

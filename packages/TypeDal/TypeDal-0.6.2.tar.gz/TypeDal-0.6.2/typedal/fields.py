import typing
from .core import TypedFieldType, TypedTable, TypeDAL

import decimal
import datetime as dt
from pydal.objects import Table

T = typing.TypeVar("T")


## general


def TypedField(
    _type: T,
    **kwargs,
) -> T:
    # sneaky: het is een functie en geen class opdat er een return type is :)
    # en de return type (T) is de input type in _type
    return TypedFieldType(_type, **kwargs)


TYPE_STR = typing.Type[str]
TYPE_INT = typing.Type[int]
TYPE_LIST_OF_INT = typing.Type[list[int]]


## specific
def StringField(**kw) -> TYPE_STR:
    kw["type"] = "string"
    return TypedField(str, **kw)


String = StringField


def TextField(**kw) -> TYPE_STR:
    kw["type"] = "text"
    return TypedField(str, **kw)


Text = TextField


def BlobField(**kw) -> typing.Type[bytes]:
    kw["type"] = "blob"
    return TypedField(bytes, **kw)


Blob = BlobField


def BooleanField(**kw) -> typing.Type[bool]:
    kw["type"] = "boolean"
    return TypedField(bool, **kw)


Boolean = BooleanField


def IntegerField(**kw) -> typing.Type[int]:
    kw["type"] = "integer"
    return TypedField(int, **kw)


Integer = IntegerField


def DoubleField(**kw) -> typing.Type[float]:
    kw["type"] = "double"
    return TypedField(float, **kw)


Double = DoubleField


def DecimalField(n, m, **kw) -> typing.Type[decimal.Decimal]:
    kw["type"] = f"decimal({n}, {m})"
    return TypedField(decimal.Decimal, **kw)


Decimal = DecimalField


def DateField(**kw) -> typing.Type[dt.date]:
    kw["type"] = "date"
    return TypedField(dt.date, **kw)


Date = DateField


def TimeField(**kw) -> typing.Type[dt.time]:
    kw["type"] = "time"
    return TypedField(dt.time, **kw)


Time = TimeField


def DatetimeField(**kw) -> typing.Type[dt.datetime]:
    kw["type"] = "datetime"
    return TypedField(dt.datetime, **kw)


Datetime = DatetimeField


def PasswordField(**kw) -> TYPE_STR:
    kw["type"] = "password"
    return TypedField(str, **kw)


Password = PasswordField


def UploadField(**kw) -> TYPE_STR:
    kw["type"] = "upload"
    return TypedField(str, **kw)


Upload = UploadField


def ReferenceField(other_table, **kw) -> TYPE_INT:
    if isinstance(other_table, str):
        kw["type"] = "reference " + other_table

    elif isinstance(other_table, Table):
        # db.table
        kw["type"] = f"reference {other_table._tablename}"
    elif issubclass(type(other_table), type) and issubclass(other_table, TypedTable):
        # SomeTable
        snakename = TypeDAL._to_snake(other_table.__name__)
        kw["type"] = f"reference {snakename}"
    else:
        raise ValueError(f"Don't know what to do with {type(other_table)}")

    return TypedField(int, **kw)


Reference = ReferenceField


def ListStringField(**kw) -> typing.Type[list[str]]:
    kw["type"] = "list:string"
    return TypedField(list[str], **kw)


ListString = ListStringField


def ListIntegerField(**kw) -> TYPE_LIST_OF_INT:
    kw["type"] = "list:integer"
    return TypedField(list, **kw)


ListInteger = ListIntegerField


def ListReferenceField(other_table, **kw) -> TYPE_LIST_OF_INT:
    kw["type"] = f"list:reference {other_table}"
    return TypedField(list, **kw)


ListReference = ListReferenceField


def JSONField(**kw) -> typing.Type[object]:
    kw["type"] = "json"
    return TypedField(object, **kw)


def BigintField(**kw) -> TYPE_INT:
    kw["type"] = "bigint"
    return TypedField(int, **kw)


Bigint = BigintField

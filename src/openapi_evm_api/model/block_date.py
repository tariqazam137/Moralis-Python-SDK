# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_evm_api import schemas  # noqa: F401


class BlockDate(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date",
            "block",
            "timestamp",
        }
        
        class properties:
            date = schemas.StrSchema
            block = schemas.NumberSchema
            timestamp = schemas.NumberSchema
            block_timestamp = schemas.NumberSchema
            block_hash = schemas.StrSchema
            parent_hash = schemas.StrSchema
            __annotations__ = {
                "date": date,
                "block": block,
                "timestamp": timestamp,
                "block_timestamp": block_timestamp,
                "block_hash": block_hash,
                "parent_hash": parent_hash,
            }

    
    date: MetaOapg.properties.date
    block: MetaOapg.properties.block
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block"]) -> MetaOapg.properties.block: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_hash"]) -> MetaOapg.properties.parent_hash: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "block", "timestamp", "block_timestamp", "block_hash", "parent_hash", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block"]) -> MetaOapg.properties.block: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> typing.Union[MetaOapg.properties.block_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> typing.Union[MetaOapg.properties.block_hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_hash"]) -> typing.Union[MetaOapg.properties.parent_hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "block", "timestamp", "block_timestamp", "block_hash", "parent_hash", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        date: typing.Union[MetaOapg.properties.date, str, ],
        block: typing.Union[MetaOapg.properties.block, decimal.Decimal, int, float, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, float, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, schemas.Unset] = schemas.unset,
        parent_hash: typing.Union[MetaOapg.properties.parent_hash, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BlockDate':
        return super().__new__(
            cls,
            *_args,
            date=date,
            block=block,
            timestamp=timestamp,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            parent_hash=parent_hash,
            _configuration=_configuration,
            **kwargs,
        )

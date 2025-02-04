# coding: utf-8

"""
    Solana API

    Moralis Solana API  # noqa: E501

    The version of the OpenAPI document: 1.0
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

from openapi_sol_api import schemas  # noqa: F401


class SPLNFT(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "mint",
            "associatedTokenAddress",
        }
        
        class properties:
            associatedTokenAddress = schemas.StrSchema
            mint = schemas.StrSchema
            __annotations__ = {
                "associatedTokenAddress": associatedTokenAddress,
                "mint": mint,
            }
    
    mint: MetaOapg.properties.mint
    associatedTokenAddress: MetaOapg.properties.associatedTokenAddress
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedTokenAddress"]) -> MetaOapg.properties.associatedTokenAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mint"]) -> MetaOapg.properties.mint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["associatedTokenAddress", "mint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedTokenAddress"]) -> MetaOapg.properties.associatedTokenAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mint"]) -> MetaOapg.properties.mint: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["associatedTokenAddress", "mint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mint: typing.Union[MetaOapg.properties.mint, str, ],
        associatedTokenAddress: typing.Union[MetaOapg.properties.associatedTokenAddress, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SPLNFT':
        return super().__new__(
            cls,
            *_args,
            mint=mint,
            associatedTokenAddress=associatedTokenAddress,
            _configuration=_configuration,
            **kwargs,
        )

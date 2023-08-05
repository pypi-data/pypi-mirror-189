# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/epochs/v1/genesis.proto, evmos/epochs/v1/query.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ....cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class EpochInfo(betterproto.Message):
    identifier: str = betterproto.string_field(1)
    start_time: datetime = betterproto.message_field(2)
    duration: timedelta = betterproto.message_field(3)
    current_epoch: int = betterproto.int64_field(4)
    current_epoch_start_time: datetime = betterproto.message_field(5)
    epoch_counting_started: bool = betterproto.bool_field(6)
    current_epoch_start_height: int = betterproto.int64_field(7)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the epochs module's genesis state."""

    epochs: List['EpochInfo'] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryEpochsInfoRequest(betterproto.Message):
    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class QueryEpochsInfoResponse(betterproto.Message):
    epochs: List['EpochInfo'] = betterproto.message_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class QueryCurrentEpochRequest(betterproto.Message):
    identifier: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryCurrentEpochResponse(betterproto.Message):
    current_epoch: int = betterproto.int64_field(1)


class QueryStub(betterproto.ServiceStub):
    async def epoch_infos(
        self,
        query_epochs_info_request: 'QueryEpochsInfoRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryEpochsInfoResponse':
        return await self._unary_unary(
            '/evmos.epochs.v1.Query/EpochInfos',
            query_epochs_info_request,
            QueryEpochsInfoResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def current_epoch(
        self,
        query_current_epoch_request: 'QueryCurrentEpochRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryCurrentEpochResponse':
        return await self._unary_unary(
            '/evmos.epochs.v1.Query/CurrentEpoch',
            query_current_epoch_request,
            QueryCurrentEpochResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def epoch_infos(
        self, query_epochs_info_request: 'QueryEpochsInfoRequest'
    ) -> 'QueryEpochsInfoResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def current_epoch(
        self, query_current_epoch_request: 'QueryCurrentEpochRequest'
    ) -> 'QueryCurrentEpochResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_epoch_infos(
        self,
        stream: 'grpclib.server.Stream[QueryEpochsInfoRequest, QueryEpochsInfoResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.epoch_infos(request)
        await stream.send_message(response)

    async def __rpc_current_epoch(
        self,
        stream: 'grpclib.server.Stream[QueryCurrentEpochRequest, QueryCurrentEpochResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.current_epoch(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.epochs.v1.Query/EpochInfos': grpclib.const.Handler(
                self.__rpc_epoch_infos,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryEpochsInfoRequest,
                QueryEpochsInfoResponse,
            ),
            '/evmos.epochs.v1.Query/CurrentEpoch': grpclib.const.Handler(
                self.__rpc_current_epoch,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCurrentEpochRequest,
                QueryCurrentEpochResponse,
            ),
        }

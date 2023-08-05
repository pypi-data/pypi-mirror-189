# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/claims/v1/claims.proto, evmos/claims/v1/genesis.proto, evmos/claims/v1/query.proto
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

from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from ....cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class Action(betterproto.Enum):
    """Action defines the list of available actions to claim the airdrop tokens."""

    ACTION_UNSPECIFIED = 0
    """UNSPECIFIED defines an invalid action."""

    ACTION_VOTE = 1
    """VOTE defines a proposal vote."""

    ACTION_DELEGATE = 2
    """DELEGATE defines an staking delegation."""

    ACTION_EVM = 3
    """EVM defines an EVM transaction."""

    ACTION_IBC_TRANSFER = 4
    """IBC Transfer defines a fungible token transfer transaction via IBC."""


@dataclass(eq=False, repr=False)
class Claim(betterproto.Message):
    """
    Claim defines the action, completed flag and the remaining claimable amount
    for a given user. This is only used during client queries.
    """

    action: 'Action' = betterproto.enum_field(1)
    """action enum"""

    completed: bool = betterproto.bool_field(2)
    """true if the action has been completed"""

    claimable_amount: str = betterproto.string_field(3)
    """claimable token amount for the action. Zero if completed"""


@dataclass(eq=False, repr=False)
class ClaimsRecordAddress(betterproto.Message):
    """
    ClaimsRecordAddress is the claims metadata per address that is used at
    Genesis.
    """

    address: str = betterproto.string_field(1)
    """bech32 or hex address of claim user"""

    initial_claimable_amount: str = betterproto.string_field(2)
    """total initial claimable amount for the user"""

    actions_completed: List[bool] = betterproto.bool_field(3)
    """slice of the available actions completed"""


@dataclass(eq=False, repr=False)
class ClaimsRecord(betterproto.Message):
    """
    ClaimsRecord defines the initial claimable airdrop amount and the list of
    completed actions to claim the tokens.
    """

    initial_claimable_amount: str = betterproto.string_field(1)
    """total initial claimable amount for the user"""

    actions_completed: List[bool] = betterproto.bool_field(2)
    """slice of the available actions completed"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState define the claims module's genesis state."""

    params: 'Params' = betterproto.message_field(1)
    """params defines all the parameters of the module."""

    claims_records: List['ClaimsRecordAddress'] = betterproto.message_field(2)
    """list of claim records with the corresponding airdrop recipient"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the claims module's parameters."""

    enable_claims: bool = betterproto.bool_field(1)
    """enable claiming process"""

    airdrop_start_time: datetime = betterproto.message_field(2)
    """timestamp of the airdrop start"""

    duration_until_decay: timedelta = betterproto.message_field(3)
    """duration until decay of claimable tokens begin"""

    duration_of_decay: timedelta = betterproto.message_field(4)
    """duration of the token claim decay period"""

    claims_denom: str = betterproto.string_field(5)
    """denom of claimable coin"""

    authorized_channels: List[str] = betterproto.string_field(6)
    """
    list of authorized channel identifiers that can perform address
    attestations via IBC.
    """

    evm_channels: List[str] = betterproto.string_field(7)
    """list of channel identifiers from EVM compatible chains"""


@dataclass(eq=False, repr=False)
class QueryTotalUnclaimedRequest(betterproto.Message):
    """
    QueryTotalUnclaimedRequest is the request type for the Query/TotalUnclaimed
    RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryTotalUnclaimedResponse(betterproto.Message):
    """
    QueryTotalUnclaimedResponse is the response type for the Query/TotalUnclaimed
    RPC method.
    """

    coins: List['___cosmos_base_v1_beta1__.Coin'] = betterproto.message_field(1)
    """coins defines the unclaimed coins"""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    params: 'Params' = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class QueryClaimsRecordsRequest(betterproto.Message):
    """
    QueryClaimsRecordsRequest is the request type for the Query/ClaimsRecords RPC
    method.
    """

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryClaimsRecordsResponse(betterproto.Message):
    """
    QueryClaimsRecordsResponse is the response type for the Query/ClaimsRecords
    RPC method.
    """

    claims: List['ClaimsRecordAddress'] = betterproto.message_field(1)
    """claims defines all claims records"""

    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryClaimsRecordRequest(betterproto.Message):
    """
    QueryClaimsRecordRequest is the request type for the Query/ClaimsRecord RPC
    method.
    """

    address: str = betterproto.string_field(1)
    """address defines the user to query claims record for"""


@dataclass(eq=False, repr=False)
class QueryClaimsRecordResponse(betterproto.Message):
    """
    QueryClaimsRecordResponse is the response type for the Query/ClaimsRecord RPC
    method.
    """

    initial_claimable_amount: str = betterproto.string_field(1)
    """total initial claimable amount for the user"""

    claims: List['Claim'] = betterproto.message_field(2)
    """the claims of the user"""


class QueryStub(betterproto.ServiceStub):
    async def total_unclaimed(
        self,
        query_total_unclaimed_request: 'QueryTotalUnclaimedRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryTotalUnclaimedResponse':
        return await self._unary_unary(
            '/evmos.claims.v1.Query/TotalUnclaimed',
            query_total_unclaimed_request,
            QueryTotalUnclaimedResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: 'QueryParamsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryParamsResponse':
        return await self._unary_unary(
            '/evmos.claims.v1.Query/Params',
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def claims_records(
        self,
        query_claims_records_request: 'QueryClaimsRecordsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryClaimsRecordsResponse':
        return await self._unary_unary(
            '/evmos.claims.v1.Query/ClaimsRecords',
            query_claims_records_request,
            QueryClaimsRecordsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def claims_record(
        self,
        query_claims_record_request: 'QueryClaimsRecordRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryClaimsRecordResponse':
        return await self._unary_unary(
            '/evmos.claims.v1.Query/ClaimsRecord',
            query_claims_record_request,
            QueryClaimsRecordResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def total_unclaimed(
        self, query_total_unclaimed_request: 'QueryTotalUnclaimedRequest'
    ) -> 'QueryTotalUnclaimedResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: 'QueryParamsRequest'
    ) -> 'QueryParamsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def claims_records(
        self, query_claims_records_request: 'QueryClaimsRecordsRequest'
    ) -> 'QueryClaimsRecordsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def claims_record(
        self, query_claims_record_request: 'QueryClaimsRecordRequest'
    ) -> 'QueryClaimsRecordResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_total_unclaimed(
        self,
        stream: 'grpclib.server.Stream[QueryTotalUnclaimedRequest, QueryTotalUnclaimedResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_unclaimed(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: 'grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_claims_records(
        self,
        stream: 'grpclib.server.Stream[QueryClaimsRecordsRequest, QueryClaimsRecordsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.claims_records(request)
        await stream.send_message(response)

    async def __rpc_claims_record(
        self,
        stream: 'grpclib.server.Stream[QueryClaimsRecordRequest, QueryClaimsRecordResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.claims_record(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.claims.v1.Query/TotalUnclaimed': grpclib.const.Handler(
                self.__rpc_total_unclaimed,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalUnclaimedRequest,
                QueryTotalUnclaimedResponse,
            ),
            '/evmos.claims.v1.Query/Params': grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            '/evmos.claims.v1.Query/ClaimsRecords': grpclib.const.Handler(
                self.__rpc_claims_records,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClaimsRecordsRequest,
                QueryClaimsRecordsResponse,
            ),
            '/evmos.claims.v1.Query/ClaimsRecord': grpclib.const.Handler(
                self.__rpc_claims_record,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClaimsRecordRequest,
                QueryClaimsRecordResponse,
            ),
        }

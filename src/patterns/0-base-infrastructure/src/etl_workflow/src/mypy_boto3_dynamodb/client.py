"""
Type annotations for dynamodb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dynamodb.client import DynamoDBClient

    session = Session()
    client: DynamoDBClient = session.client("dynamodb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from .type_defs import (
    BatchExecuteStatementInputTypeDef,
    BatchExecuteStatementOutputTypeDef,
    BatchGetItemInputTypeDef,
    BatchGetItemOutputTypeDef,
    BatchWriteItemInputTypeDef,
    BatchWriteItemOutputTypeDef,
    CreateBackupInputTypeDef,
    CreateBackupOutputTypeDef,
    CreateGlobalTableInputTypeDef,
    CreateGlobalTableOutputTypeDef,
    CreateTableInputTypeDef,
    CreateTableOutputTypeDef,
    DeleteBackupInputTypeDef,
    DeleteBackupOutputTypeDef,
    DeleteItemInputTypeDef,
    DeleteItemOutputTypeDef,
    DeleteResourcePolicyInputTypeDef,
    DeleteResourcePolicyOutputTypeDef,
    DeleteTableInputTypeDef,
    DeleteTableOutputTypeDef,
    DescribeBackupInputTypeDef,
    DescribeBackupOutputTypeDef,
    DescribeContinuousBackupsInputTypeDef,
    DescribeContinuousBackupsOutputTypeDef,
    DescribeContributorInsightsInputTypeDef,
    DescribeContributorInsightsOutputTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeExportInputTypeDef,
    DescribeExportOutputTypeDef,
    DescribeGlobalTableInputTypeDef,
    DescribeGlobalTableOutputTypeDef,
    DescribeGlobalTableSettingsInputTypeDef,
    DescribeGlobalTableSettingsOutputTypeDef,
    DescribeImportInputTypeDef,
    DescribeImportOutputTypeDef,
    DescribeKinesisStreamingDestinationInputTypeDef,
    DescribeKinesisStreamingDestinationOutputTypeDef,
    DescribeLimitsOutputTypeDef,
    DescribeTableInputTypeDef,
    DescribeTableOutputTypeDef,
    DescribeTableReplicaAutoScalingInputTypeDef,
    DescribeTableReplicaAutoScalingOutputTypeDef,
    DescribeTimeToLiveInputTypeDef,
    DescribeTimeToLiveOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExecuteStatementInputTypeDef,
    ExecuteStatementOutputTypeDef,
    ExecuteTransactionInputTypeDef,
    ExecuteTransactionOutputTypeDef,
    ExportTableToPointInTimeInputTypeDef,
    ExportTableToPointInTimeOutputTypeDef,
    GetItemInputTypeDef,
    GetItemOutputTypeDef,
    GetResourcePolicyInputTypeDef,
    GetResourcePolicyOutputTypeDef,
    ImportTableInputTypeDef,
    ImportTableOutputTypeDef,
    KinesisStreamingDestinationInputRequestTypeDef,
    KinesisStreamingDestinationInputTypeDef,
    KinesisStreamingDestinationOutputTypeDef,
    ListBackupsInputTypeDef,
    ListBackupsOutputTypeDef,
    ListContributorInsightsInputTypeDef,
    ListContributorInsightsOutputTypeDef,
    ListExportsInputTypeDef,
    ListExportsOutputTypeDef,
    ListGlobalTablesInputTypeDef,
    ListGlobalTablesOutputTypeDef,
    ListImportsInputTypeDef,
    ListImportsOutputTypeDef,
    ListTablesInputTypeDef,
    ListTablesOutputTypeDef,
    ListTagsOfResourceInputTypeDef,
    ListTagsOfResourceOutputTypeDef,
    PutItemInputTypeDef,
    PutItemOutputTypeDef,
    PutResourcePolicyInputTypeDef,
    PutResourcePolicyOutputTypeDef,
    QueryInputTypeDef,
    QueryOutputTypeDef,
    RestoreTableFromBackupInputTypeDef,
    RestoreTableFromBackupOutputTypeDef,
    RestoreTableToPointInTimeInputTypeDef,
    RestoreTableToPointInTimeOutputTypeDef,
    ScanInputTypeDef,
    ScanOutputTypeDef,
    TagResourceInputTypeDef,
    TransactGetItemsInputTypeDef,
    TransactGetItemsOutputTypeDef,
    TransactWriteItemsInputTypeDef,
    TransactWriteItemsOutputTypeDef,
    UntagResourceInputTypeDef,
    UpdateContinuousBackupsInputTypeDef,
    UpdateContinuousBackupsOutputTypeDef,
    UpdateContributorInsightsInputTypeDef,
    UpdateContributorInsightsOutputTypeDef,
    UpdateGlobalTableInputTypeDef,
    UpdateGlobalTableOutputTypeDef,
    UpdateGlobalTableSettingsInputTypeDef,
    UpdateGlobalTableSettingsOutputTypeDef,
    UpdateItemInputTypeDef,
    UpdateItemOutputTypeDef,
    UpdateKinesisStreamingDestinationInputTypeDef,
    UpdateKinesisStreamingDestinationOutputTypeDef,
    UpdateTableInputTypeDef,
    UpdateTableOutputTypeDef,
    UpdateTableReplicaAutoScalingInputTypeDef,
    UpdateTableReplicaAutoScalingOutputTypeDef,
    UpdateTimeToLiveInputTypeDef,
    UpdateTimeToLiveOutputTypeDef,
)
from .waiter import TableExistsWaiter, TableNotExistsWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("DynamoDBClient",)


class Exceptions(BaseClientExceptions):
    BackupInUseException: Type[BotocoreClientError]
    BackupNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConditionalCheckFailedException: Type[BotocoreClientError]
    ContinuousBackupsUnavailableException: Type[BotocoreClientError]
    DuplicateItemException: Type[BotocoreClientError]
    ExportConflictException: Type[BotocoreClientError]
    ExportNotFoundException: Type[BotocoreClientError]
    GlobalTableAlreadyExistsException: Type[BotocoreClientError]
    GlobalTableNotFoundException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    ImportConflictException: Type[BotocoreClientError]
    ImportNotFoundException: Type[BotocoreClientError]
    IndexNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidExportTimeException: Type[BotocoreClientError]
    InvalidRestoreTimeException: Type[BotocoreClientError]
    ItemCollectionSizeLimitExceededException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PointInTimeRecoveryUnavailableException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ReplicaAlreadyExistsException: Type[BotocoreClientError]
    ReplicaNotFoundException: Type[BotocoreClientError]
    ReplicatedWriteConflictException: Type[BotocoreClientError]
    RequestLimitExceeded: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TableAlreadyExistsException: Type[BotocoreClientError]
    TableInUseException: Type[BotocoreClientError]
    TableNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TransactionCanceledException: Type[BotocoreClientError]
    TransactionConflictException: Type[BotocoreClientError]
    TransactionInProgressException: Type[BotocoreClientError]


class DynamoDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DynamoDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#generate_presigned_url)
        """

    def batch_execute_statement(
        self, **kwargs: Unpack[BatchExecuteStatementInputTypeDef]
    ) -> BatchExecuteStatementOutputTypeDef:
        """
        This operation allows you to perform batch reads or writes on data stored in
        DynamoDB, using PartiQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/batch_execute_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#batch_execute_statement)
        """

    def batch_get_item(
        self, **kwargs: Unpack[BatchGetItemInputTypeDef]
    ) -> BatchGetItemOutputTypeDef:
        """
        The <code>BatchGetItem</code> operation returns the attributes of one or more
        items from one or more tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/batch_get_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#batch_get_item)
        """

    def batch_write_item(
        self, **kwargs: Unpack[BatchWriteItemInputTypeDef]
    ) -> BatchWriteItemOutputTypeDef:
        """
        The <code>BatchWriteItem</code> operation puts or deletes multiple items in one
        or more tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/batch_write_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#batch_write_item)
        """

    def create_backup(
        self, **kwargs: Unpack[CreateBackupInputTypeDef]
    ) -> CreateBackupOutputTypeDef:
        """
        Creates a backup for an existing table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/create_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#create_backup)
        """

    def create_global_table(
        self, **kwargs: Unpack[CreateGlobalTableInputTypeDef]
    ) -> CreateGlobalTableOutputTypeDef:
        """
        Creates a global table from an existing table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/create_global_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#create_global_table)
        """

    def create_table(self, **kwargs: Unpack[CreateTableInputTypeDef]) -> CreateTableOutputTypeDef:
        """
        The <code>CreateTable</code> operation adds a new table to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/create_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#create_table)
        """

    def delete_backup(
        self, **kwargs: Unpack[DeleteBackupInputTypeDef]
    ) -> DeleteBackupOutputTypeDef:
        """
        Deletes an existing backup of a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/delete_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#delete_backup)
        """

    def delete_item(self, **kwargs: Unpack[DeleteItemInputTypeDef]) -> DeleteItemOutputTypeDef:
        """
        Deletes a single item in a table by primary key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/delete_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#delete_item)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyInputTypeDef]
    ) -> DeleteResourcePolicyOutputTypeDef:
        """
        Deletes the resource-based policy attached to the resource, which can be a
        table or stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#delete_resource_policy)
        """

    def delete_table(self, **kwargs: Unpack[DeleteTableInputTypeDef]) -> DeleteTableOutputTypeDef:
        """
        The <code>DeleteTable</code> operation deletes a table and all of its items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/delete_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#delete_table)
        """

    def describe_backup(
        self, **kwargs: Unpack[DescribeBackupInputTypeDef]
    ) -> DescribeBackupOutputTypeDef:
        """
        Describes an existing backup of a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_backup)
        """

    def describe_continuous_backups(
        self, **kwargs: Unpack[DescribeContinuousBackupsInputTypeDef]
    ) -> DescribeContinuousBackupsOutputTypeDef:
        """
        Checks the status of continuous backups and point in time recovery on the
        specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_continuous_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_continuous_backups)
        """

    def describe_contributor_insights(
        self, **kwargs: Unpack[DescribeContributorInsightsInputTypeDef]
    ) -> DescribeContributorInsightsOutputTypeDef:
        """
        Returns information about contributor insights for a given table or global
        secondary index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_contributor_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_contributor_insights)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        Returns the regional endpoint information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_endpoints)
        """

    def describe_export(
        self, **kwargs: Unpack[DescribeExportInputTypeDef]
    ) -> DescribeExportOutputTypeDef:
        """
        Describes an existing table export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_export)
        """

    def describe_global_table(
        self, **kwargs: Unpack[DescribeGlobalTableInputTypeDef]
    ) -> DescribeGlobalTableOutputTypeDef:
        """
        Returns information about the specified global table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_global_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_global_table)
        """

    def describe_global_table_settings(
        self, **kwargs: Unpack[DescribeGlobalTableSettingsInputTypeDef]
    ) -> DescribeGlobalTableSettingsOutputTypeDef:
        """
        Describes Region-specific settings for a global table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_global_table_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_global_table_settings)
        """

    def describe_import(
        self, **kwargs: Unpack[DescribeImportInputTypeDef]
    ) -> DescribeImportOutputTypeDef:
        """
        Represents the properties of the import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_import)
        """

    def describe_kinesis_streaming_destination(
        self, **kwargs: Unpack[DescribeKinesisStreamingDestinationInputTypeDef]
    ) -> DescribeKinesisStreamingDestinationOutputTypeDef:
        """
        Returns information about the status of Kinesis streaming.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_kinesis_streaming_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_kinesis_streaming_destination)
        """

    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        Returns the current provisioned-capacity quotas for your Amazon Web Services
        account in a Region, both for the Region as a whole and for any one DynamoDB
        table that you create there.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_limits)
        """

    def describe_table(
        self, **kwargs: Unpack[DescribeTableInputTypeDef]
    ) -> DescribeTableOutputTypeDef:
        """
        Returns information about the table, including the current status of the table,
        when it was created, the primary key schema, and any indexes on the table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_table)
        """

    def describe_table_replica_auto_scaling(
        self, **kwargs: Unpack[DescribeTableReplicaAutoScalingInputTypeDef]
    ) -> DescribeTableReplicaAutoScalingOutputTypeDef:
        """
        Describes auto scaling settings across replicas of the global table at once.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_table_replica_auto_scaling.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_table_replica_auto_scaling)
        """

    def describe_time_to_live(
        self, **kwargs: Unpack[DescribeTimeToLiveInputTypeDef]
    ) -> DescribeTimeToLiveOutputTypeDef:
        """
        Gives a description of the Time to Live (TTL) status on the specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_time_to_live.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#describe_time_to_live)
        """

    def disable_kinesis_streaming_destination(
        self, **kwargs: Unpack[KinesisStreamingDestinationInputTypeDef]
    ) -> KinesisStreamingDestinationOutputTypeDef:
        """
        Stops replication from the DynamoDB table to the Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/disable_kinesis_streaming_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#disable_kinesis_streaming_destination)
        """

    def enable_kinesis_streaming_destination(
        self, **kwargs: Unpack[KinesisStreamingDestinationInputRequestTypeDef]
    ) -> KinesisStreamingDestinationOutputTypeDef:
        """
        Starts table data replication to the specified Kinesis data stream at a
        timestamp chosen during the enable workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/enable_kinesis_streaming_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#enable_kinesis_streaming_destination)
        """

    def execute_statement(
        self, **kwargs: Unpack[ExecuteStatementInputTypeDef]
    ) -> ExecuteStatementOutputTypeDef:
        """
        This operation allows you to perform reads and singleton writes on data stored
        in DynamoDB, using PartiQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/execute_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#execute_statement)
        """

    def execute_transaction(
        self, **kwargs: Unpack[ExecuteTransactionInputTypeDef]
    ) -> ExecuteTransactionOutputTypeDef:
        """
        This operation allows you to perform transactional reads or writes on data
        stored in DynamoDB, using PartiQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/execute_transaction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#execute_transaction)
        """

    def export_table_to_point_in_time(
        self, **kwargs: Unpack[ExportTableToPointInTimeInputTypeDef]
    ) -> ExportTableToPointInTimeOutputTypeDef:
        """
        Exports table data to an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/export_table_to_point_in_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#export_table_to_point_in_time)
        """

    def get_item(self, **kwargs: Unpack[GetItemInputTypeDef]) -> GetItemOutputTypeDef:
        """
        The <code>GetItem</code> operation returns a set of attributes for the item
        with the given primary key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_item)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyInputTypeDef]
    ) -> GetResourcePolicyOutputTypeDef:
        """
        Returns the resource-based policy document attached to the resource, which can
        be a table or stream, in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_resource_policy)
        """

    def import_table(self, **kwargs: Unpack[ImportTableInputTypeDef]) -> ImportTableOutputTypeDef:
        """
        Imports table data from an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/import_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#import_table)
        """

    def list_backups(self, **kwargs: Unpack[ListBackupsInputTypeDef]) -> ListBackupsOutputTypeDef:
        """
        List DynamoDB backups that are associated with an Amazon Web Services account
        and weren't made with Amazon Web Services Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_backups)
        """

    def list_contributor_insights(
        self, **kwargs: Unpack[ListContributorInsightsInputTypeDef]
    ) -> ListContributorInsightsOutputTypeDef:
        """
        Returns a list of ContributorInsightsSummary for a table and all its global
        secondary indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_contributor_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_contributor_insights)
        """

    def list_exports(self, **kwargs: Unpack[ListExportsInputTypeDef]) -> ListExportsOutputTypeDef:
        """
        Lists completed exports within the past 90 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_exports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_exports)
        """

    def list_global_tables(
        self, **kwargs: Unpack[ListGlobalTablesInputTypeDef]
    ) -> ListGlobalTablesOutputTypeDef:
        """
        Lists all global tables that have a replica in the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_global_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_global_tables)
        """

    def list_imports(self, **kwargs: Unpack[ListImportsInputTypeDef]) -> ListImportsOutputTypeDef:
        """
        Lists completed imports within the past 90 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_imports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_imports)
        """

    def list_tables(self, **kwargs: Unpack[ListTablesInputTypeDef]) -> ListTablesOutputTypeDef:
        """
        Returns an array of table names associated with the current account and
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_tables)
        """

    def list_tags_of_resource(
        self, **kwargs: Unpack[ListTagsOfResourceInputTypeDef]
    ) -> ListTagsOfResourceOutputTypeDef:
        """
        List all tags on an Amazon DynamoDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_tags_of_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#list_tags_of_resource)
        """

    def put_item(self, **kwargs: Unpack[PutItemInputTypeDef]) -> PutItemOutputTypeDef:
        """
        Creates a new item, or replaces an old item with a new item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#put_item)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyInputTypeDef]
    ) -> PutResourcePolicyOutputTypeDef:
        """
        Attaches a resource-based policy document to the resource, which can be a table
        or stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#put_resource_policy)
        """

    def query(self, **kwargs: Unpack[QueryInputTypeDef]) -> QueryOutputTypeDef:
        """
        You must provide the name of the partition key attribute and a single value for
        that attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#query)
        """

    def restore_table_from_backup(
        self, **kwargs: Unpack[RestoreTableFromBackupInputTypeDef]
    ) -> RestoreTableFromBackupOutputTypeDef:
        """
        Creates a new table from an existing backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/restore_table_from_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#restore_table_from_backup)
        """

    def restore_table_to_point_in_time(
        self, **kwargs: Unpack[RestoreTableToPointInTimeInputTypeDef]
    ) -> RestoreTableToPointInTimeOutputTypeDef:
        """
        Restores the specified table to the specified point in time within
        <code>EarliestRestorableDateTime</code> and
        <code>LatestRestorableDateTime</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/restore_table_to_point_in_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#restore_table_to_point_in_time)
        """

    def scan(self, **kwargs: Unpack[ScanInputTypeDef]) -> ScanOutputTypeDef:
        """
        The <code>Scan</code> operation returns one or more items and item attributes
        by accessing every item in a table or a secondary index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/scan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#scan)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associate a set of tags with an Amazon DynamoDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#tag_resource)
        """

    def transact_get_items(
        self, **kwargs: Unpack[TransactGetItemsInputTypeDef]
    ) -> TransactGetItemsOutputTypeDef:
        """
        <code>TransactGetItems</code> is a synchronous operation that atomically
        retrieves multiple items from one or more tables (but not from indexes) in a
        single account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/transact_get_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#transact_get_items)
        """

    def transact_write_items(
        self, **kwargs: Unpack[TransactWriteItemsInputTypeDef]
    ) -> TransactWriteItemsOutputTypeDef:
        """
        <code>TransactWriteItems</code> is a synchronous write operation that groups up
        to 100 action requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/transact_write_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#transact_write_items)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the association of tags from an Amazon DynamoDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#untag_resource)
        """

    def update_continuous_backups(
        self, **kwargs: Unpack[UpdateContinuousBackupsInputTypeDef]
    ) -> UpdateContinuousBackupsOutputTypeDef:
        """
        <code>UpdateContinuousBackups</code> enables or disables point in time recovery
        for the specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_continuous_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_continuous_backups)
        """

    def update_contributor_insights(
        self, **kwargs: Unpack[UpdateContributorInsightsInputTypeDef]
    ) -> UpdateContributorInsightsOutputTypeDef:
        """
        Updates the status for contributor insights for a specific table or index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_contributor_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_contributor_insights)
        """

    def update_global_table(
        self, **kwargs: Unpack[UpdateGlobalTableInputTypeDef]
    ) -> UpdateGlobalTableOutputTypeDef:
        """
        Adds or removes replicas in the specified global table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_global_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_global_table)
        """

    def update_global_table_settings(
        self, **kwargs: Unpack[UpdateGlobalTableSettingsInputTypeDef]
    ) -> UpdateGlobalTableSettingsOutputTypeDef:
        """
        Updates settings for a global table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_global_table_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_global_table_settings)
        """

    def update_item(self, **kwargs: Unpack[UpdateItemInputTypeDef]) -> UpdateItemOutputTypeDef:
        """
        Edits an existing item's attributes, or adds a new item to the table if it does
        not already exist.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_item)
        """

    def update_kinesis_streaming_destination(
        self, **kwargs: Unpack[UpdateKinesisStreamingDestinationInputTypeDef]
    ) -> UpdateKinesisStreamingDestinationOutputTypeDef:
        """
        The command to update the Kinesis stream destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_kinesis_streaming_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_kinesis_streaming_destination)
        """

    def update_table(self, **kwargs: Unpack[UpdateTableInputTypeDef]) -> UpdateTableOutputTypeDef:
        """
        Modifies the provisioned throughput settings, global secondary indexes, or
        DynamoDB Streams settings for a given table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_table)
        """

    def update_table_replica_auto_scaling(
        self, **kwargs: Unpack[UpdateTableReplicaAutoScalingInputTypeDef]
    ) -> UpdateTableReplicaAutoScalingOutputTypeDef:
        """
        Updates auto scaling settings on your global tables at once.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_table_replica_auto_scaling.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_table_replica_auto_scaling)
        """

    def update_time_to_live(
        self, **kwargs: Unpack[UpdateTimeToLiveInputTypeDef]
    ) -> UpdateTimeToLiveOutputTypeDef:
        """
        The <code>UpdateTimeToLive</code> method enables or disables Time to Live (TTL)
        for the specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_time_to_live.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#update_time_to_live)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backups"]
    ) -> ListBackupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tables"]
    ) -> ListTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_of_resource"]
    ) -> ListTagsOfResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["query"]
    ) -> QueryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["scan"]
    ) -> ScanPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["table_exists"]
    ) -> TableExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["table_not_exists"]
    ) -> TableNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client/#get_waiter)
        """

"""
Type annotations for dynamodb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dynamodb.client import DynamoDBClient
    from mypy_boto3_dynamodb.paginator import (
        ListBackupsPaginator,
        ListTablesPaginator,
        ListTagsOfResourcePaginator,
        QueryPaginator,
        ScanPaginator,
    )

    session = Session()
    client: DynamoDBClient = session.client("dynamodb")

    list_backups_paginator: ListBackupsPaginator = client.get_paginator("list_backups")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    list_tags_of_resource_paginator: ListTagsOfResourcePaginator = client.get_paginator("list_tags_of_resource")
    query_paginator: QueryPaginator = client.get_paginator("query")
    scan_paginator: ScanPaginator = client.get_paginator("scan")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBackupsInputPaginateTypeDef,
    ListBackupsOutputTypeDef,
    ListTablesInputPaginateTypeDef,
    ListTablesOutputTypeDef,
    ListTagsOfResourceInputPaginateTypeDef,
    ListTagsOfResourceOutputTypeDef,
    QueryInputPaginateTypeDef,
    QueryOutputTypeDef,
    ScanInputPaginateTypeDef,
    ScanOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
)

if TYPE_CHECKING:
    _ListBackupsPaginatorBase = Paginator[ListBackupsOutputTypeDef]
else:
    _ListBackupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupsPaginator(_ListBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/ListBackups.html#DynamoDB.Paginator.ListBackups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#listbackupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupsInputPaginateTypeDef]
    ) -> PageIterator[ListBackupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/ListBackups.html#DynamoDB.Paginator.ListBackups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#listbackupspaginator)
        """

if TYPE_CHECKING:
    _ListTablesPaginatorBase = Paginator[ListTablesOutputTypeDef]
else:
    _ListTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTablesPaginator(_ListTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/ListTables.html#DynamoDB.Paginator.ListTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#listtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTablesInputPaginateTypeDef]
    ) -> PageIterator[ListTablesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/ListTables.html#DynamoDB.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#listtablespaginator)
        """

if TYPE_CHECKING:
    _ListTagsOfResourcePaginatorBase = Paginator[ListTagsOfResourceOutputTypeDef]
else:
    _ListTagsOfResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsOfResourcePaginator(_ListTagsOfResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/ListTagsOfResource.html#DynamoDB.Paginator.ListTagsOfResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#listtagsofresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsOfResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsOfResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/ListTagsOfResource.html#DynamoDB.Paginator.ListTagsOfResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#listtagsofresourcepaginator)
        """

if TYPE_CHECKING:
    _QueryPaginatorBase = Paginator[QueryOutputTypeDef]
else:
    _QueryPaginatorBase = Paginator  # type: ignore[assignment]

class QueryPaginator(_QueryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/Query.html#DynamoDB.Paginator.Query)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#querypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[QueryInputPaginateTypeDef]
    ) -> PageIterator[QueryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/Query.html#DynamoDB.Paginator.Query.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#querypaginator)
        """

if TYPE_CHECKING:
    _ScanPaginatorBase = Paginator[ScanOutputTypeDef]
else:
    _ScanPaginatorBase = Paginator  # type: ignore[assignment]

class ScanPaginator(_ScanPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/Scan.html#DynamoDB.Paginator.Scan)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#scanpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ScanInputPaginateTypeDef]
    ) -> PageIterator[ScanOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/Scan.html#DynamoDB.Paginator.Scan.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators/#scanpaginator)
        """

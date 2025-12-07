"""
Type annotations for dynamodb service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dynamodb.client import DynamoDBClient
    from mypy_boto3_dynamodb.waiter import (
        TableExistsWaiter,
        TableNotExistsWaiter,
    )

    session = Session()
    client: DynamoDBClient = session.client("dynamodb")

    table_exists_waiter: TableExistsWaiter = client.get_waiter("table_exists")
    table_not_exists_waiter: TableNotExistsWaiter = client.get_waiter("table_not_exists")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeTableInputWaitExtraTypeDef, DescribeTableInputWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("TableExistsWaiter", "TableNotExistsWaiter")


class TableExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/waiter/TableExists.html#DynamoDB.Waiter.TableExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters/#tableexistswaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTableInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/waiter/TableExists.html#DynamoDB.Waiter.TableExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters/#tableexistswaiter)
        """


class TableNotExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/waiter/TableNotExists.html#DynamoDB.Waiter.TableNotExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters/#tablenotexistswaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTableInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/waiter/TableNotExists.html#DynamoDB.Waiter.TableNotExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters/#tablenotexistswaiter)
        """

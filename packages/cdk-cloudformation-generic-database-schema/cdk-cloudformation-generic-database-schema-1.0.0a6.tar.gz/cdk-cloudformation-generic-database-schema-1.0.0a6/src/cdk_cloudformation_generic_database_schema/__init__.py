'''
# generic-database-schema

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Generic::Database::Schema` v1.0.0.

## Description

Uses the Aurora Data API to execute SQL and enforce a schema within a database cluster. Currently only supports Aurora Postgres.

## References

* [Source](https://github.com/iann0036/cfn-types/tree/master/generic-database-schema)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Generic::Database::Schema \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/Generic-Database-Schema \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Generic::Database::Schema`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fgeneric-database-schema+v1.0.0).
* Issues related to `Generic::Database::Schema` should be reported to the [publisher](https://github.com/iann0036/cfn-types/tree/master/generic-database-schema).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnSchema(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/generic-database-schema.CfnSchema",
):
    '''A CloudFormation ``Generic::Database::Schema``.

    :cloudformationResource: Generic::Database::Schema
    :link: https://github.com/iann0036/cfn-types/tree/master/generic-database-schema
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_arn: builtins.str,
        secret_arn: builtins.str,
        databases: typing.Optional[typing.Sequence[typing.Union["Database", typing.Dict[builtins.str, typing.Any]]]] = None,
        sql: typing.Optional[typing.Sequence[builtins.str]] = None,
        sql_idempotency: typing.Optional["CfnSchemaPropsSqlIdempotency"] = None,
        users: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``Generic::Database::Schema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_arn: The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
        :param secret_arn: The name or ARN of the secret that enables access to the DB cluster.
        :param databases: An array of databases to manage within the cluster.
        :param sql: An array of SQL statements to execute within the postgres database.
        :param sql_idempotency: Whether arbitrary SQL statements are executed once (IDEMPOTENT), or on every update (RUN_ONCE).
        :param users: An array of users within the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__180a033c840c0245ca1207021c7e6346cdfb169a6b28d49b9d3d3ec6a8f5c962)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaProps(
            cluster_arn=cluster_arn,
            secret_arn=secret_arn,
            databases=databases,
            sql=sql,
            sql_idempotency=sql_idempotency,
            users=users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrExecutionId")
    def attr_execution_id(self) -> builtins.str:
        '''Attribute ``Generic::Database::Schema.ExecutionId``.

        :link: https://github.com/iann0036/cfn-types/tree/master/generic-database-schema
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExecutionId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSchemaProps":
        '''Resource props.'''
        return typing.cast("CfnSchemaProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.CfnSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_arn": "clusterArn",
        "secret_arn": "secretArn",
        "databases": "databases",
        "sql": "sql",
        "sql_idempotency": "sqlIdempotency",
        "users": "users",
    },
)
class CfnSchemaProps:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        secret_arn: builtins.str,
        databases: typing.Optional[typing.Sequence[typing.Union["Database", typing.Dict[builtins.str, typing.Any]]]] = None,
        sql: typing.Optional[typing.Sequence[builtins.str]] = None,
        sql_idempotency: typing.Optional["CfnSchemaPropsSqlIdempotency"] = None,
        users: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Uses the Aurora Data API to execute SQL and enforce a schema within a database cluster.

        Currently only supports Aurora Postgres.

        :param cluster_arn: The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
        :param secret_arn: The name or ARN of the secret that enables access to the DB cluster.
        :param databases: An array of databases to manage within the cluster.
        :param sql: An array of SQL statements to execute within the postgres database.
        :param sql_idempotency: Whether arbitrary SQL statements are executed once (IDEMPOTENT), or on every update (RUN_ONCE).
        :param users: An array of users within the cluster.

        :schema: CfnSchemaProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f8c10ab2aaf85e11863d60acff682a4d804f5511dc6c79a6916d43eb74783e)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            check_type(argname="argument databases", value=databases, expected_type=type_hints["databases"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument sql_idempotency", value=sql_idempotency, expected_type=type_hints["sql_idempotency"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "secret_arn": secret_arn,
        }
        if databases is not None:
            self._values["databases"] = databases
        if sql is not None:
            self._values["sql"] = sql
        if sql_idempotency is not None:
            self._values["sql_idempotency"] = sql_idempotency
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

        :schema: CfnSchemaProps#ClusterArn
        '''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_arn(self) -> builtins.str:
        '''The name or ARN of the secret that enables access to the DB cluster.

        :schema: CfnSchemaProps#SecretArn
        '''
        result = self._values.get("secret_arn")
        assert result is not None, "Required property 'secret_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def databases(self) -> typing.Optional[typing.List["Database"]]:
        '''An array of databases to manage within the cluster.

        :schema: CfnSchemaProps#Databases
        '''
        result = self._values.get("databases")
        return typing.cast(typing.Optional[typing.List["Database"]], result)

    @builtins.property
    def sql(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of SQL statements to execute within the postgres database.

        :schema: CfnSchemaProps#SQL
        '''
        result = self._values.get("sql")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sql_idempotency(self) -> typing.Optional["CfnSchemaPropsSqlIdempotency"]:
        '''Whether arbitrary SQL statements are executed once (IDEMPOTENT), or on every update (RUN_ONCE).

        :schema: CfnSchemaProps#SQLIdempotency
        '''
        result = self._values.get("sql_idempotency")
        return typing.cast(typing.Optional["CfnSchemaPropsSqlIdempotency"], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List["User"]]:
        '''An array of users within the cluster.

        :schema: CfnSchemaProps#Users
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/generic-database-schema.CfnSchemaPropsSqlIdempotency"
)
class CfnSchemaPropsSqlIdempotency(enum.Enum):
    '''Whether arbitrary SQL statements are executed once (IDEMPOTENT), or on every update (RUN_ONCE).

    :schema: CfnSchemaPropsSqlIdempotency
    '''

    IDEMPOTENT = "IDEMPOTENT"
    '''IDEMPOTENT.'''
    RUN_ONCE = "RUN_ONCE"
    '''RUN_ONCE.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.Column",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "default": "default",
        "nullable": "nullable",
    },
)
class Column:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        default: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param name: The name of the column. Creates the column if it doesn't exist. Cannot be updated after creation.
        :param type: The type of the column. Cannot be updated after creation.
        :param default: The default value of the column. Cannot be updated after creation.
        :param nullable: Whether the column is nullable. Cannot be updated after creation.

        :schema: Column
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc4fb29a919b275da6802f1a22aaec7407f5a67c0ecc19dfa463b879db3d72fe)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if default is not None:
            self._values["default"] = default
        if nullable is not None:
            self._values["nullable"] = nullable

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the column.

        Creates the column if it doesn't exist. Cannot be updated after creation.

        :schema: Column#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the column.

        Cannot be updated after creation.

        :schema: Column#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''The default value of the column.

        Cannot be updated after creation.

        :schema: Column#Default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(self) -> typing.Optional[builtins.bool]:
        '''Whether the column is nullable.

        Cannot be updated after creation.

        :schema: Column#Nullable
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Column(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.Database",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "extensions": "extensions",
        "sql": "sql",
        "tables": "tables",
    },
)
class Database:
    def __init__(
        self,
        *,
        name: builtins.str,
        extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        sql: typing.Optional[typing.Sequence[builtins.str]] = None,
        tables: typing.Optional[typing.Sequence[typing.Union["Table", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param name: The name of the database. Creates the database if it doesn't exist.
        :param extensions: An array of extensions to enable within the database.
        :param sql: An array of SQL statements to execute within the database.
        :param tables: An array of tables to manage within the database.

        :schema: Database
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f34472ba6cbc9c6f646e83fbfa30b020f2001aa441b42913c39d590b773e7b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument extensions", value=extensions, expected_type=type_hints["extensions"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument tables", value=tables, expected_type=type_hints["tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if extensions is not None:
            self._values["extensions"] = extensions
        if sql is not None:
            self._values["sql"] = sql
        if tables is not None:
            self._values["tables"] = tables

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the database.

        Creates the database if it doesn't exist.

        :schema: Database#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of extensions to enable within the database.

        :schema: Database#Extensions
        '''
        result = self._values.get("extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sql(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of SQL statements to execute within the database.

        :schema: Database#SQL
        '''
        result = self._values.get("sql")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tables(self) -> typing.Optional[typing.List["Table"]]:
        '''An array of tables to manage within the database.

        :schema: Database#Tables
        '''
        result = self._values.get("tables")
        return typing.cast(typing.Optional[typing.List["Table"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Database(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.Grant",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "privileges": "privileges",
        "table": "table",
    },
)
class Grant:
    def __init__(
        self,
        *,
        database: builtins.str,
        privileges: typing.Sequence[builtins.str],
        table: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database: The name of the database. If the grant Table field is omitted, this represents a database grant, otherwise represents a table grant.
        :param privileges: An array of privileges to grant (CONNECT, SELECT, etc.).
        :param table: The name of the table. The grant Database field must specify the containing database and the database must be specified in the Databases section of the base of the type.

        :schema: Grant
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baaea3df5ee82c58883b8c1db74523e4679b45947044e2a1089d9e6a42aaac31)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument privileges", value=privileges, expected_type=type_hints["privileges"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "privileges": privileges,
        }
        if table is not None:
            self._values["table"] = table

    @builtins.property
    def database(self) -> builtins.str:
        '''The name of the database.

        If the grant Table field is omitted, this represents a database grant, otherwise represents a table grant.

        :schema: Grant#Database
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def privileges(self) -> typing.List[builtins.str]:
        '''An array of privileges to grant (CONNECT, SELECT, etc.).

        :schema: Grant#Privileges
        '''
        result = self._values.get("privileges")
        assert result is not None, "Required property 'privileges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def table(self) -> typing.Optional[builtins.str]:
        '''The name of the table.

        The grant Database field must specify the containing database and the database must be specified in the Databases section of the base of the type.

        :schema: Grant#Table
        '''
        result = self._values.get("table")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Grant(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.PrimaryKey",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "default": "default"},
)
class PrimaryKey:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        default: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the primary key. Cannot be updated after creation.
        :param type: The type of the primary key. Cannot be updated after creation.
        :param default: The default value of the primary key. Cannot be updated after creation.

        :schema: PrimaryKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acd3dfb3c0c1be88e54748a0e86e31c29c4e1cd4e31d09e4e56bd3902f033569)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the primary key.

        Cannot be updated after creation.

        :schema: PrimaryKey#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the primary key.

        Cannot be updated after creation.

        :schema: PrimaryKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''The default value of the primary key.

        Cannot be updated after creation.

        :schema: PrimaryKey#Default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrimaryKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.Table",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "columns": "columns", "primary_key": "primaryKey"},
)
class Table:
    def __init__(
        self,
        *,
        name: builtins.str,
        columns: typing.Optional[typing.Sequence[typing.Union[Column, typing.Dict[builtins.str, typing.Any]]]] = None,
        primary_key: typing.Optional[typing.Union[PrimaryKey, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: The name of the table. Creates the table if it doesn't exist.
        :param columns: An array of columns to manage within the database.
        :param primary_key: 

        :schema: Table
        '''
        if isinstance(primary_key, dict):
            primary_key = PrimaryKey(**primary_key)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a6d52a2796eb7e20ef58a580551024e9300544837f48df7bc364ee7b13a6bcc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if columns is not None:
            self._values["columns"] = columns
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the table.

        Creates the table if it doesn't exist.

        :schema: Table#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def columns(self) -> typing.Optional[typing.List[Column]]:
        '''An array of columns to manage within the database.

        :schema: Table#Columns
        '''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.List[Column]], result)

    @builtins.property
    def primary_key(self) -> typing.Optional[PrimaryKey]:
        '''
        :schema: Table#PrimaryKey
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[PrimaryKey], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Table(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/generic-database-schema.User",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "grants": "grants",
        "secret_id": "secretId",
        "super_user": "superUser",
    },
)
class User:
    def __init__(
        self,
        *,
        name: builtins.str,
        grants: typing.Optional[typing.Sequence[typing.Union[Grant, typing.Dict[builtins.str, typing.Any]]]] = None,
        secret_id: typing.Optional[builtins.str] = None,
        super_user: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param name: The username of the user. Creates the user/role.
        :param grants: An array of grants to assign to the user.
        :param secret_id: The Secrets Manager secret ID or ARN of the credentials to set for the user ('password' field of the JSON secret value).
        :param super_user: Whether to give the user rds_superuser privileges.

        :schema: User
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98137549c078debc099111add4e51a51eb0409d68eca45770d0a148487b994c6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument grants", value=grants, expected_type=type_hints["grants"])
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            check_type(argname="argument super_user", value=super_user, expected_type=type_hints["super_user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if grants is not None:
            self._values["grants"] = grants
        if secret_id is not None:
            self._values["secret_id"] = secret_id
        if super_user is not None:
            self._values["super_user"] = super_user

    @builtins.property
    def name(self) -> builtins.str:
        '''The username of the user.

        Creates the user/role.

        :schema: User#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grants(self) -> typing.Optional[typing.List[Grant]]:
        '''An array of grants to assign to the user.

        :schema: User#Grants
        '''
        result = self._values.get("grants")
        return typing.cast(typing.Optional[typing.List[Grant]], result)

    @builtins.property
    def secret_id(self) -> typing.Optional[builtins.str]:
        '''The Secrets Manager secret ID or ARN of the credentials to set for the user ('password' field of the JSON secret value).

        :schema: User#SecretId
        '''
        result = self._values.get("secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def super_user(self) -> typing.Optional[builtins.bool]:
        '''Whether to give the user rds_superuser privileges.

        :schema: User#SuperUser
        '''
        result = self._values.get("super_user")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "User(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSchema",
    "CfnSchemaProps",
    "CfnSchemaPropsSqlIdempotency",
    "Column",
    "Database",
    "Grant",
    "PrimaryKey",
    "Table",
    "User",
]

publication.publish()

def _typecheckingstub__180a033c840c0245ca1207021c7e6346cdfb169a6b28d49b9d3d3ec6a8f5c962(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_arn: builtins.str,
    secret_arn: builtins.str,
    databases: typing.Optional[typing.Sequence[typing.Union[Database, typing.Dict[builtins.str, typing.Any]]]] = None,
    sql: typing.Optional[typing.Sequence[builtins.str]] = None,
    sql_idempotency: typing.Optional[CfnSchemaPropsSqlIdempotency] = None,
    users: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f8c10ab2aaf85e11863d60acff682a4d804f5511dc6c79a6916d43eb74783e(
    *,
    cluster_arn: builtins.str,
    secret_arn: builtins.str,
    databases: typing.Optional[typing.Sequence[typing.Union[Database, typing.Dict[builtins.str, typing.Any]]]] = None,
    sql: typing.Optional[typing.Sequence[builtins.str]] = None,
    sql_idempotency: typing.Optional[CfnSchemaPropsSqlIdempotency] = None,
    users: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc4fb29a919b275da6802f1a22aaec7407f5a67c0ecc19dfa463b879db3d72fe(
    *,
    name: builtins.str,
    type: builtins.str,
    default: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f34472ba6cbc9c6f646e83fbfa30b020f2001aa441b42913c39d590b773e7b(
    *,
    name: builtins.str,
    extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    sql: typing.Optional[typing.Sequence[builtins.str]] = None,
    tables: typing.Optional[typing.Sequence[typing.Union[Table, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baaea3df5ee82c58883b8c1db74523e4679b45947044e2a1089d9e6a42aaac31(
    *,
    database: builtins.str,
    privileges: typing.Sequence[builtins.str],
    table: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd3dfb3c0c1be88e54748a0e86e31c29c4e1cd4e31d09e4e56bd3902f033569(
    *,
    name: builtins.str,
    type: builtins.str,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a6d52a2796eb7e20ef58a580551024e9300544837f48df7bc364ee7b13a6bcc(
    *,
    name: builtins.str,
    columns: typing.Optional[typing.Sequence[typing.Union[Column, typing.Dict[builtins.str, typing.Any]]]] = None,
    primary_key: typing.Optional[typing.Union[PrimaryKey, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98137549c078debc099111add4e51a51eb0409d68eca45770d0a148487b994c6(
    *,
    name: builtins.str,
    grants: typing.Optional[typing.Sequence[typing.Union[Grant, typing.Dict[builtins.str, typing.Any]]]] = None,
    secret_id: typing.Optional[builtins.str] = None,
    super_user: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

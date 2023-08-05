'''
# Amazon Neptune Construct Library

Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine. This engine is optimized for storing billions of relationships and querying the graph with milliseconds latency. Neptune supports the popular graph query languages Apache TinkerPop Gremlin and W3C’s SPARQL, enabling you to build queries that efficiently navigate highly connected datasets.

The `@aws-cdk/aws-neptune` package contains primitives for setting up Neptune database clusters and instances.

```python
import monocdk as neptune
```

## Starting a Neptune Database

To set up a Neptune database, define a `DatabaseCluster`. You must always launch a database in a VPC.

```python
cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE
)
```

By default only writer instance is provisioned with this construct.

## Connecting

To control who can access the cluster, use the `.connections` attribute. Neptune databases have a default port, so
you don't need to specify the port:

```python
cluster.connections.allow_default_port_from_any_ipv4("Open to the world")
```

The endpoints to access your database cluster will be available as the `.clusterEndpoint` and `.clusterReadEndpoint`
attributes:

```python
write_address = cluster.cluster_endpoint.socket_address
```

## IAM Authentication

You can also authenticate to a database cluster using AWS Identity and Access Management (IAM) database authentication;
See [https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html) for more information and a list of supported
versions and limitations.

The following example shows enabling IAM authentication for a database cluster and granting connection access to an IAM role.

```python
cluster = neptune.DatabaseCluster(self, "Cluster",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    iam_authentication=True
)
role = iam.Role(self, "DBRole", assumed_by=iam.AccountPrincipal(self.account))
cluster.grant_connect(role)
```

## Customizing parameters

Neptune allows configuring database behavior by supplying custom parameter groups.  For more details, refer to the
following link: [https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html)

```python
cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
    description="Cluster parameter group",
    parameters={
        "neptune_enable_audit_log": "1"
    }
)

db_params = neptune.ParameterGroup(self, "DbParams",
    description="Db parameter group",
    parameters={
        "neptune_query_timeout": "120000"
    }
)

cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    cluster_parameter_group=cluster_params,
    parameter_group=db_params
)
```

## Adding replicas

`DatabaseCluster` allows launching replicas along with the writer instance. This can be specified using the `instanceCount`
attribute.

```python
cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    instances=2
)
```

Additionally it is also possible to add replicas using `DatabaseInstance` for an existing cluster.

```python
replica1 = neptune.DatabaseInstance(self, "Instance",
    cluster=cluster,
    instance_type=neptune.InstanceType.R5_LARGE
)
```

## Automatic minor version upgrades

By setting `autoMinorVersionUpgrade` to true, Neptune will automatically update
the engine of the entire cluster to the latest minor version after a stabilization
window of 2 to 3 weeks.

```python
neptune.DatabaseCluster(self, "Cluster",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    auto_minor_version_upgrade=True
)
```
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    RemovalPolicy as _RemovalPolicy_c97e7a20,
    Resource as _Resource_abff4495,
    ResourceProps as _ResourceProps_9b554c0f,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_ec2 import (
    Connections as _Connections_57ccbda9,
    IConnectable as _IConnectable_c1c0e72c,
    ISecurityGroup as _ISecurityGroup_cdbba9d3,
    IVpc as _IVpc_6d1f76c4,
    SubnetSelection as _SubnetSelection_1284e62c,
)
from ..aws_iam import (
    Grant as _Grant_bcb5eae7,
    IGrantable as _IGrantable_4c5a91d1,
    IRole as _IRole_59af6f50,
)
from ..aws_kms import IKey as _IKey_36930160


@jsii.implements(_IInspectable_82c04a63)
class CfnDBCluster(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.CfnDBCluster",
):
    '''A CloudFormation ``AWS::Neptune::DBCluster``.

    The ``AWS::Neptune::DBCluster`` resource creates an Amazon Neptune DB cluster. Neptune is a fully managed graph database.
    .. epigraph::

       Currently, you can create this resource only in AWS Regions in which Amazon Neptune is supported.

    If no ``DeletionPolicy`` is set for ``AWS::Neptune::DBCluster`` resources, the default deletion behavior is that the entire volume will be deleted without a snapshot. To retain a backup of the volume, the ``DeletionPolicy`` should be set to ``Snapshot`` . For more information about how AWS CloudFormation deletes resources, see `DeletionPolicy Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .

    You can use ``AWS::Neptune::DBCluster.DeletionProtection`` to help guard against unintended deletion of your DB cluster.

    :cloudformationResource: AWS::Neptune::DBCluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        cfn_dBCluster = neptune.CfnDBCluster(self, "MyCfnDBCluster",
            associated_roles=[neptune.CfnDBCluster.DBClusterRoleProperty(
                role_arn="roleArn",
        
                # the properties below are optional
                feature_name="featureName"
            )],
            availability_zones=["availabilityZones"],
            backup_retention_period=123,
            db_cluster_identifier="dbClusterIdentifier",
            db_cluster_parameter_group_name="dbClusterParameterGroupName",
            db_subnet_group_name="dbSubnetGroupName",
            deletion_protection=False,
            enable_cloudwatch_logs_exports=["enableCloudwatchLogsExports"],
            engine_version="engineVersion",
            iam_auth_enabled=False,
            kms_key_id="kmsKeyId",
            port=123,
            preferred_backup_window="preferredBackupWindow",
            preferred_maintenance_window="preferredMaintenanceWindow",
            restore_to_time="restoreToTime",
            restore_type="restoreType",
            snapshot_identifier="snapshotIdentifier",
            source_db_cluster_identifier="sourceDbClusterIdentifier",
            storage_encrypted=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            use_latest_restorable_time=False,
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        associated_roles: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnDBCluster.DBClusterRoleProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        restore_to_time: typing.Optional[builtins.str] = None,
        restore_type: typing.Optional[builtins.str] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        source_db_cluster_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Neptune::DBCluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param associated_roles: Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.
        :param availability_zones: Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.
        :param backup_retention_period: Specifies the number of days for which automatic DB snapshots are retained. An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.
        :param db_cluster_identifier: Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
        :param db_cluster_parameter_group_name: Provides the name of the DB cluster parameter group. An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.
        :param db_subnet_group_name: Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.
        :param deletion_protection: Indicates whether or not the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.
        :param enable_cloudwatch_logs_exports: Specifies a list of log types that are enabled for export to CloudWatch Logs.
        :param engine_version: Indicates the database engine version.
        :param iam_auth_enabled: True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
        :param kms_key_id: If ``StorageEncrypted`` is true, the Amazon KMS key identifier for the encrypted DB cluster.
        :param port: Specifies the port that the database engine is listening on.
        :param preferred_backup_window: Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` . An update may require some interruption.
        :param preferred_maintenance_window: Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        :param restore_to_time: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param restore_type: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param snapshot_identifier: Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot. After you restore a DB cluster using a ``SnapshotIdentifier`` , you must specify the same ``SnapshotIdentifier`` for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the ``SnapshotIdentifier`` , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the ``SnapshotIdentifier`` , and the original DB cluster is deleted.
        :param source_db_cluster_identifier: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param storage_encrypted: Indicates whether the DB cluster is encrypted. If you specify the ``DBClusterIdentifier`` , ``DBSnapshotIdentifier`` , or ``SourceDBInstanceIdentifier`` property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance. If you specify the ``KmsKeyId`` property, you must enable encryption. If you specify the ``KmsKeyId`` , you must enable encryption by setting ``StorageEncrypted`` to true.
        :param tags: The tags assigned to this cluster.
        :param use_latest_restorable_time: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param vpc_security_group_ids: Provides a list of VPC security groups that the DB cluster belongs to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110f0a0ca6029ca303ccae8c4b1962c65ff0b45e7d0966eade290eeae5ee729a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBClusterProps(
            associated_roles=associated_roles,
            availability_zones=availability_zones,
            backup_retention_period=backup_retention_period,
            db_cluster_identifier=db_cluster_identifier,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            db_subnet_group_name=db_subnet_group_name,
            deletion_protection=deletion_protection,
            enable_cloudwatch_logs_exports=enable_cloudwatch_logs_exports,
            engine_version=engine_version,
            iam_auth_enabled=iam_auth_enabled,
            kms_key_id=kms_key_id,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            restore_to_time=restore_to_time,
            restore_type=restore_type,
            snapshot_identifier=snapshot_identifier,
            source_db_cluster_identifier=source_db_cluster_identifier,
            storage_encrypted=storage_encrypted,
            tags=tags,
            use_latest_restorable_time=use_latest_restorable_time,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2a6ce322c50bc9084e6133094cb4401fe1adbb5965953fd21b500b0992834c2)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28e1e64cc5275c80c6f47ed013c54071cf7d21bc625fd6f689e01d1a3a860237)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterResourceId")
    def attr_cluster_resource_id(self) -> builtins.str:
        '''The resource id for the DB cluster.

        For example: ``cluster-ABCD1234EFGH5678IJKL90MNOP`` . The cluster ID uniquely identifies the cluster and is used in things like IAM authentication policies.

        :cloudformationAttribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterResourceId"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connection endpoint for the DB cluster.

        For example: ``mystack-mydbcluster-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com``

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> builtins.str:
        '''The port number on which the DB cluster accepts connections.

        For example: ``8182`` .

        :cloudformationAttribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPort"))

    @builtins.property
    @jsii.member(jsii_name="attrReadEndpoint")
    def attr_read_endpoint(self) -> builtins.str:
        '''The reader endpoint for the DB cluster.

        For example: ``mystack-mydbcluster-ro-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com``

        :cloudformationAttribute: ReadEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''The tags assigned to this cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="associatedRoles")
    def associated_roles(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDBCluster.DBClusterRoleProperty", _IResolvable_a771d0ef]]]]:
        '''Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster.

        IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-associatedroles
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDBCluster.DBClusterRoleProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "associatedRoles"))

    @associated_roles.setter
    def associated_roles(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDBCluster.DBClusterRoleProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a64529c1a353c08398998e015ac02cd1e4ba99312328b957222a78c98a7173df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-availabilityzones
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7fcabe49cb63a4d591f30468f5bcabdcc3ba177fa37c0d49c7f76419600ff68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriod")
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days for which automatic DB snapshots are retained.

        An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-backupretentionperiod
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionPeriod"))

    @backup_retention_period.setter
    def backup_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e551bfda1f5fe7597511b098f86d55bd4377c666f04adaae0d4566c704cb9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Contains a user-supplied DB cluster identifier.

        This identifier is the unique key that identifies a DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbclusteridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5273f369a2c6fae3a41345bb5c4f22d00808ac38cdd38073159005b2cf5e0cf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Provides the name of the DB cluster parameter group.

        An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbclusterparametergroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterParameterGroupName"))

    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dffc607e9308142bb1eb7d94565e22e808b21cdcecd6887da47f711a17c82b75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbsubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663e5f807524c3c37f38e6de1f265ea06d8c8d2c419e68012accfe0251211790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether or not the DB cluster has deletion protection enabled.

        The database can't be deleted when deletion protection is enabled.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-deletionprotection
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a183fe00ab2c4744d66b20fddca2e608a9128e7251e4da38dd6513018f9a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of log types that are enabled for export to CloudWatch Logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-enablecloudwatchlogsexports
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enableCloudwatchLogsExports"))

    @enable_cloudwatch_logs_exports.setter
    def enable_cloudwatch_logs_exports(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eecea3cea363cb4b46c8508826f18df296230035a032d74740dae7e3a708e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCloudwatchLogsExports", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Indicates the database engine version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-engineversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd71208085eb7cb069b63cc80e28fa9ff883a10c66815a41e4f2654cbeeccdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="iamAuthEnabled")
    def iam_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-iamauthenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "iamAuthEnabled"))

    @iam_auth_enabled.setter
    def iam_auth_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bf49b70503842f6979907eb55b623a1780c8ce9cea9b7d10c3a118762501d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamAuthEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''If ``StorageEncrypted`` is true, the Amazon KMS key identifier for the encrypted DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b9f060f88336d4561d525fa60e65cfc81d48d5ea7f5a5af76be5476388ce41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port that the database engine is listening on.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-port
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c63efeb9a3573de6cd786e4e1e379b11fe9942b90dd66138be2c380055c484e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        An update may require some interruption.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-preferredbackupwindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aefa7f4de3b606275bc08b0ae8c4d3a34930ac79c7df59f06bb3a0afec80cfcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8d8d53155fce9af8c7d4d1ab0d95c46a5e33281cd00804bafd32bad2589bf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="restoreToTime")
    def restore_to_time(self) -> typing.Optional[builtins.str]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-restoretotime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreToTime"))

    @restore_to_time.setter
    def restore_to_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb390a4d8cb25abb23e1ba947f838d339e9797b24a34a333f1d0102c98beb76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreToTime", value)

    @builtins.property
    @jsii.member(jsii_name="restoreType")
    def restore_type(self) -> typing.Optional[builtins.str]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-restoretype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreType"))

    @restore_type.setter
    def restore_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5aaa7fc2573157105d2532204b5b9dfdeb492219e79e88e017d1ab35fd9477a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreType", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.

        After you restore a DB cluster using a ``SnapshotIdentifier`` , you must specify the same ``SnapshotIdentifier`` for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.

        However, if you don't specify the ``SnapshotIdentifier`` , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the ``SnapshotIdentifier`` , and the original DB cluster is deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-snapshotidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdentifier"))

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e498d9d1b7d0268549e83a61ade1fb2845fa1ceb7ee70400a8c02bc79a056248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-sourcedbclusteridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDbClusterIdentifier"))

    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3bb98fb744b7a6099224397a2de663be76b9c1289b3bf8a1457f80cb1c3ec3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="storageEncrypted")
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether the DB cluster is encrypted.

        If you specify the ``DBClusterIdentifier`` , ``DBSnapshotIdentifier`` , or ``SourceDBInstanceIdentifier`` property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance. If you specify the ``KmsKeyId`` property, you must enable encryption.

        If you specify the ``KmsKeyId`` , you must enable encryption by setting ``StorageEncrypted`` to true.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-storageencrypted
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "storageEncrypted"))

    @storage_encrypted.setter
    def storage_encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d34deaa79c19af406cfeca0c8e222afa333b40bb15e1ed80a54a993dfbe74d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="useLatestRestorableTime")
    def use_latest_restorable_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-uselatestrestorabletime
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "useLatestRestorableTime"))

    @use_latest_restorable_time.setter
    def use_latest_restorable_time(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41994621c4a717d04de5812413cc948b8afd12bf89d14e57ebb745f2f75f76c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLatestRestorableTime", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Provides a list of VPC security groups that the DB cluster belongs to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-vpcsecuritygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f430a7be49051a74c6c91d951d71aeccb6c9e1db3d6322a2e5d8ea5c03576992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_neptune.CfnDBCluster.DBClusterRoleProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "feature_name": "featureName"},
    )
    class DBClusterRoleProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            feature_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an Amazon Identity and Access Management (IAM) role that is associated with a DB cluster.

            :param role_arn: The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.
            :param feature_name: The name of the feature associated with the Amazon Identity and Access Management (IAM) role. For the list of supported feature names, see `DescribeDBEngineVersions <https://docs.aws.amazon.com/neptune/latest/userguide/api-other-apis.html#DescribeDBEngineVersions>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_neptune as neptune
                
                d_bCluster_role_property = neptune.CfnDBCluster.DBClusterRoleProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    feature_name="featureName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51377912c1292d83ddc74442be10cbd438049e46d7b0787cd6186a792152fba1)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument feature_name", value=feature_name, expected_type=type_hints["feature_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if feature_name is not None:
                self._values["feature_name"] = feature_name

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html#cfn-neptune-dbcluster-dbclusterrole-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def feature_name(self) -> typing.Optional[builtins.str]:
            '''The name of the feature associated with the Amazon Identity and Access Management (IAM) role.

            For the list of supported feature names, see `DescribeDBEngineVersions <https://docs.aws.amazon.com/neptune/latest/userguide/api-other-apis.html#DescribeDBEngineVersions>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html#cfn-neptune-dbcluster-dbclusterrole-featurename
            '''
            result = self._values.get("feature_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DBClusterRoleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnDBClusterParameterGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.CfnDBClusterParameterGroup",
):
    '''A CloudFormation ``AWS::Neptune::DBClusterParameterGroup``.

    The ``AWS::Neptune::DBClusterParameterGroup`` resource creates a new Amazon Neptune DB cluster parameter group.
    .. epigraph::

       Applying a parameter group to a DB cluster might require instances to reboot, resulting in a database outage while the instances reboot.

    :cloudformationResource: AWS::Neptune::DBClusterParameterGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        # parameters: Any
        
        cfn_dBCluster_parameter_group = neptune.CfnDBClusterParameterGroup(self, "MyCfnDBClusterParameterGroup",
            description="description",
            family="family",
            parameters=parameters,
        
            # the properties below are optional
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Neptune::DBClusterParameterGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: Provides the customer-specified description for this DB cluster parameter group.
        :param family: Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.
        :param parameters: The parameters to set for this DB cluster parameter group. The parameters are expressed as a JSON object consisting of key-value pairs. If you update the parameters, some interruption may occur depending on which parameters you update.
        :param name: Provides the name of the DB cluster parameter group.
        :param tags: The tags that you want to attach to this parameter group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05b2c3ccfadd7f38535855c44c75fdd9632e222bf34afaaff70fae41d14b5d9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBClusterParameterGroupProps(
            description=description,
            family=family,
            parameters=parameters,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e821e5ea7bf8e93698cdea04b1b9e020502edefb0185ecdf214322b63d87061)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21c3ee8920c840687d9044b6daff47800dc77106fa6ddf95c4176c79e24f8804)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''The tags that you want to attach to this parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''Provides the customer-specified description for this DB cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6d2bebeea5db75e1ea8f1c2321b92ad7f980de3e3712e9bd4e248dd61ace46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        '''Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-family
        '''
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b640487ba2001e72f58363685c5bd1951e2efbc641915491dd99e6807e2f0fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''The parameters to set for this DB cluster parameter group.

        The parameters are expressed as a JSON object consisting of key-value pairs.

        If you update the parameters, some interruption may occur depending on which parameters you update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-parameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a9e4da527cfb52dbf0ee09d3f1c4aada153c5cd19b759b2accbfca834604446)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Provides the name of the DB cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e4bd16626f0dfa51387a3ab9ff70abb0ab9800634eb91fc906ba16ce25c1dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.CfnDBClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "family": "family",
        "parameters": "parameters",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDBClusterParameterGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBClusterParameterGroup``.

        :param description: Provides the customer-specified description for this DB cluster parameter group.
        :param family: Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.
        :param parameters: The parameters to set for this DB cluster parameter group. The parameters are expressed as a JSON object consisting of key-value pairs. If you update the parameters, some interruption may occur depending on which parameters you update.
        :param name: Provides the name of the DB cluster parameter group.
        :param tags: The tags that you want to attach to this parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_neptune as neptune
            
            # parameters: Any
            
            cfn_dBCluster_parameter_group_props = neptune.CfnDBClusterParameterGroupProps(
                description="description",
                family="family",
                parameters=parameters,
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfd09d54313fb179052cb8c2cbb7a17ee0718a06172bc7e4604f57cb1bdf280f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "family": family,
            "parameters": parameters,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''Provides the customer-specified description for this DB cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def family(self) -> builtins.str:
        '''Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-family
        '''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters to set for this DB cluster parameter group.

        The parameters are expressed as a JSON object consisting of key-value pairs.

        If you update the parameters, some interruption may occur depending on which parameters you update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-parameters
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Provides the name of the DB cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''The tags that you want to attach to this parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.CfnDBClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "associated_roles": "associatedRoles",
        "availability_zones": "availabilityZones",
        "backup_retention_period": "backupRetentionPeriod",
        "db_cluster_identifier": "dbClusterIdentifier",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "deletion_protection": "deletionProtection",
        "enable_cloudwatch_logs_exports": "enableCloudwatchLogsExports",
        "engine_version": "engineVersion",
        "iam_auth_enabled": "iamAuthEnabled",
        "kms_key_id": "kmsKeyId",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "restore_to_time": "restoreToTime",
        "restore_type": "restoreType",
        "snapshot_identifier": "snapshotIdentifier",
        "source_db_cluster_identifier": "sourceDbClusterIdentifier",
        "storage_encrypted": "storageEncrypted",
        "tags": "tags",
        "use_latest_restorable_time": "useLatestRestorableTime",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnDBClusterProps:
    def __init__(
        self,
        *,
        associated_roles: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnDBCluster.DBClusterRoleProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        restore_to_time: typing.Optional[builtins.str] = None,
        restore_type: typing.Optional[builtins.str] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        source_db_cluster_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBCluster``.

        :param associated_roles: Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.
        :param availability_zones: Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.
        :param backup_retention_period: Specifies the number of days for which automatic DB snapshots are retained. An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.
        :param db_cluster_identifier: Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
        :param db_cluster_parameter_group_name: Provides the name of the DB cluster parameter group. An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.
        :param db_subnet_group_name: Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.
        :param deletion_protection: Indicates whether or not the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.
        :param enable_cloudwatch_logs_exports: Specifies a list of log types that are enabled for export to CloudWatch Logs.
        :param engine_version: Indicates the database engine version.
        :param iam_auth_enabled: True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
        :param kms_key_id: If ``StorageEncrypted`` is true, the Amazon KMS key identifier for the encrypted DB cluster.
        :param port: Specifies the port that the database engine is listening on.
        :param preferred_backup_window: Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` . An update may require some interruption.
        :param preferred_maintenance_window: Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        :param restore_to_time: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param restore_type: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param snapshot_identifier: Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot. After you restore a DB cluster using a ``SnapshotIdentifier`` , you must specify the same ``SnapshotIdentifier`` for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the ``SnapshotIdentifier`` , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the ``SnapshotIdentifier`` , and the original DB cluster is deleted.
        :param source_db_cluster_identifier: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param storage_encrypted: Indicates whether the DB cluster is encrypted. If you specify the ``DBClusterIdentifier`` , ``DBSnapshotIdentifier`` , or ``SourceDBInstanceIdentifier`` property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance. If you specify the ``KmsKeyId`` property, you must enable encryption. If you specify the ``KmsKeyId`` , you must enable encryption by setting ``StorageEncrypted`` to true.
        :param tags: The tags assigned to this cluster.
        :param use_latest_restorable_time: Creates a new DB cluster from a DB snapshot or DB cluster snapshot. If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group. If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        :param vpc_security_group_ids: Provides a list of VPC security groups that the DB cluster belongs to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_neptune as neptune
            
            cfn_dBCluster_props = neptune.CfnDBClusterProps(
                associated_roles=[neptune.CfnDBCluster.DBClusterRoleProperty(
                    role_arn="roleArn",
            
                    # the properties below are optional
                    feature_name="featureName"
                )],
                availability_zones=["availabilityZones"],
                backup_retention_period=123,
                db_cluster_identifier="dbClusterIdentifier",
                db_cluster_parameter_group_name="dbClusterParameterGroupName",
                db_subnet_group_name="dbSubnetGroupName",
                deletion_protection=False,
                enable_cloudwatch_logs_exports=["enableCloudwatchLogsExports"],
                engine_version="engineVersion",
                iam_auth_enabled=False,
                kms_key_id="kmsKeyId",
                port=123,
                preferred_backup_window="preferredBackupWindow",
                preferred_maintenance_window="preferredMaintenanceWindow",
                restore_to_time="restoreToTime",
                restore_type="restoreType",
                snapshot_identifier="snapshotIdentifier",
                source_db_cluster_identifier="sourceDbClusterIdentifier",
                storage_encrypted=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                use_latest_restorable_time=False,
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5eaf46b1e8f8ecfa044c04fea9a8d313e373a0556ecbaeadf92b15e633e0880)
            check_type(argname="argument associated_roles", value=associated_roles, expected_type=type_hints["associated_roles"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument backup_retention_period", value=backup_retention_period, expected_type=type_hints["backup_retention_period"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument enable_cloudwatch_logs_exports", value=enable_cloudwatch_logs_exports, expected_type=type_hints["enable_cloudwatch_logs_exports"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument iam_auth_enabled", value=iam_auth_enabled, expected_type=type_hints["iam_auth_enabled"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument restore_to_time", value=restore_to_time, expected_type=type_hints["restore_to_time"])
            check_type(argname="argument restore_type", value=restore_type, expected_type=type_hints["restore_type"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument source_db_cluster_identifier", value=source_db_cluster_identifier, expected_type=type_hints["source_db_cluster_identifier"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_latest_restorable_time", value=use_latest_restorable_time, expected_type=type_hints["use_latest_restorable_time"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if associated_roles is not None:
            self._values["associated_roles"] = associated_roles
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if db_cluster_identifier is not None:
            self._values["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if enable_cloudwatch_logs_exports is not None:
            self._values["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if iam_auth_enabled is not None:
            self._values["iam_auth_enabled"] = iam_auth_enabled
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if restore_to_time is not None:
            self._values["restore_to_time"] = restore_to_time
        if restore_type is not None:
            self._values["restore_type"] = restore_type
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if source_db_cluster_identifier is not None:
            self._values["source_db_cluster_identifier"] = source_db_cluster_identifier
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if tags is not None:
            self._values["tags"] = tags
        if use_latest_restorable_time is not None:
            self._values["use_latest_restorable_time"] = use_latest_restorable_time
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def associated_roles(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDBCluster.DBClusterRoleProperty, _IResolvable_a771d0ef]]]]:
        '''Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster.

        IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-associatedroles
        '''
        result = self._values.get("associated_roles")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDBCluster.DBClusterRoleProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-availabilityzones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days for which automatic DB snapshots are retained.

        An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-backupretentionperiod
        '''
        result = self._values.get("backup_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Contains a user-supplied DB cluster identifier.

        This identifier is the unique key that identifies a DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbclusteridentifier
        '''
        result = self._values.get("db_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Provides the name of the DB cluster parameter group.

        An update may require some interruption. See `ModifyDBInstance <https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#ModifyDBInstance>`_ in the Amazon Neptune User Guide for more information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbclusterparametergroupname
        '''
        result = self._values.get("db_cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbsubnetgroupname
        '''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether or not the DB cluster has deletion protection enabled.

        The database can't be deleted when deletion protection is enabled.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-deletionprotection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def enable_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of log types that are enabled for export to CloudWatch Logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-enablecloudwatchlogsexports
        '''
        result = self._values.get("enable_cloudwatch_logs_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Indicates the database engine version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-iamauthenabled
        '''
        result = self._values.get("iam_auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''If ``StorageEncrypted`` is true, the Amazon KMS key identifier for the encrypted DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port that the database engine is listening on.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        An update may require some interruption.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_to_time(self) -> typing.Optional[builtins.str]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-restoretotime
        '''
        result = self._values.get("restore_to_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_type(self) -> typing.Optional[builtins.str]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-restoretype
        '''
        result = self._values.get("restore_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.

        After you restore a DB cluster using a ``SnapshotIdentifier`` , you must specify the same ``SnapshotIdentifier`` for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.

        However, if you don't specify the ``SnapshotIdentifier`` , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the ``SnapshotIdentifier`` , and the original DB cluster is deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-snapshotidentifier
        '''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-sourcedbclusteridentifier
        '''
        result = self._values.get("source_db_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether the DB cluster is encrypted.

        If you specify the ``DBClusterIdentifier`` , ``DBSnapshotIdentifier`` , or ``SourceDBInstanceIdentifier`` property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance. If you specify the ``KmsKeyId`` property, you must enable encryption.

        If you specify the ``KmsKeyId`` , you must enable encryption by setting ``StorageEncrypted`` to true.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-storageencrypted
        '''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''The tags assigned to this cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def use_latest_restorable_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-uselatestrestorabletime
        '''
        result = self._values.get("use_latest_restorable_time")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Provides a list of VPC security groups that the DB cluster belongs to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDBInstance(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.CfnDBInstance",
):
    '''A CloudFormation ``AWS::Neptune::DBInstance``.

    The ``AWS::Neptune::DBInstance`` type creates an Amazon Neptune DB instance.

    *Updating DB Instances*

    You can set a deletion policy for your DB instance to control how AWS CloudFormation handles the instance when the stack is deleted. For Neptune DB instances, you can choose to *retain* the instance, to *delete* the instance, or to *create a snapshot* of the instance. The default AWS CloudFormation behavior depends on the ``DBClusterIdentifier`` property:

    - For ``AWS::Neptune::DBInstance`` resources that don't specify the ``DBClusterIdentifier`` property, AWS CloudFormation saves a snapshot of the DB instance.
    - For ``AWS::Neptune::DBInstance`` resources that do specify the ``DBClusterIdentifier`` property, AWS CloudFormation deletes the DB instance.

    *Deleting DB Instances*
    .. epigraph::

       If a DB instance is deleted or replaced during an update, AWS CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an update that requires replacement, you can apply a stack policy to prevent DB instances from being replaced.

    When properties labeled *Update requires: Replacement* are updated, AWS CloudFormation first creates a replacement DB instance, changes references from other dependent resources to point to the replacement DB instance, and finally deletes the old DB instance.
    .. epigraph::

       We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when AWS CloudFormation replaces your DB instance. To preserve your data, perform the following procedure:

       - Deactivate any applications that are using the DB instance so that there's no activity on the DB instance.
       - Create a snapshot of the DB instance.
       - If you want to restore your instance using a DB snapshot, modify the updated template with your DB instance changes and add the ``DBSnapshotIdentifier`` property with the ID of the DB snapshot that you want to use.
       - Update the stack.

    :cloudformationResource: AWS::Neptune::DBInstance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        cfn_dBInstance = neptune.CfnDBInstance(self, "MyCfnDBInstance",
            db_instance_class="dbInstanceClass",
        
            # the properties below are optional
            allow_major_version_upgrade=False,
            auto_minor_version_upgrade=False,
            availability_zone="availabilityZone",
            db_cluster_identifier="dbClusterIdentifier",
            db_instance_identifier="dbInstanceIdentifier",
            db_parameter_group_name="dbParameterGroupName",
            db_snapshot_identifier="dbSnapshotIdentifier",
            db_subnet_group_name="dbSubnetGroupName",
            preferred_maintenance_window="preferredMaintenanceWindow",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        db_instance_class: builtins.str,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_instance_identifier: typing.Optional[builtins.str] = None,
        db_parameter_group_name: typing.Optional[builtins.str] = None,
        db_snapshot_identifier: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Neptune::DBInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param db_instance_class: Contains the name of the compute and memory capacity class of the DB instance. If you update this property, some interruptions may occur.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.
        :param auto_minor_version_upgrade: Indicates that minor version patches are applied automatically. When updating this property, some interruptions may occur.
        :param availability_zone: Specifies the name of the Availability Zone the DB instance is located in.
        :param db_cluster_identifier: If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
        :param db_instance_identifier: Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.
        :param db_parameter_group_name: The name of an existing DB parameter group or a reference to an AWS::Neptune::DBParameterGroup resource created in the template. If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.
        :param db_snapshot_identifier: This parameter is not supported. ``AWS::Neptune::DBInstance`` does not support restoring from snapshots. ``AWS::Neptune::DBCluster`` does support restoring from snapshots.
        :param db_subnet_group_name: A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new virtual private cloud (VPC).
        :param preferred_maintenance_window: Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        :param tags: An arbitrary set of tags (key-value pairs) for this DB instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a8a367809652871a1143ad207bbfa8c53f3ba49c49826ae7ef6f70d6a9067a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBInstanceProps(
            db_instance_class=db_instance_class,
            allow_major_version_upgrade=allow_major_version_upgrade,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            db_cluster_identifier=db_cluster_identifier,
            db_instance_identifier=db_instance_identifier,
            db_parameter_group_name=db_parameter_group_name,
            db_snapshot_identifier=db_snapshot_identifier,
            db_subnet_group_name=db_subnet_group_name,
            preferred_maintenance_window=preferred_maintenance_window,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1696b63951b7a18ec83e9b7a3738becddb501794dd5a54f9b5bfd1ec0a0312)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76df152bae97b41623f22250ac3287417f139c383492103f40d356bcb5585b5c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connection endpoint for the database.

        For example: ``mystack-mydb-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com`` .

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> builtins.str:
        '''The port number on which the database accepts connections.

        For example: ``8182`` .

        :cloudformationAttribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPort"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''An arbitrary set of tags (key-value pairs) for this DB instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceClass")
    def db_instance_class(self) -> builtins.str:
        '''Contains the name of the compute and memory capacity class of the DB instance.

        If you update this property, some interruptions may occur.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbinstanceclass
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceClass"))

    @db_instance_class.setter
    def db_instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93e6eb318f9a5098b4f80fc5a2f201be470d29cfd55ba22d730859884dd26dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbInstanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates that major version upgrades are allowed.

        Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-allowmajorversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "allowMajorVersionUpgrade"))

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__372eae02d88f94c7cf93c12041d0608b7b720ddbf1ed30a73c2ff00d60cd9b47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMajorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates that minor version patches are applied automatically.

        When updating this property, some interruptions may occur.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-autominorversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa184cdde7a3d69b2e71d3b36ee4668cbd4400184febfc17bb6e0f7eb74d6829)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Availability Zone the DB instance is located in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d45cbcec0f761ea665aef83df2bae58fb8939a8ea563c95ecdfa7539a78010e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbclusteridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5fdb5582539d5602cc0f9e7fc9c1e50f203345b7c40942d6f44983a83af132a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''Contains a user-supplied database identifier.

        This identifier is the unique key that identifies a DB instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbinstanceidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbInstanceIdentifier"))

    @db_instance_identifier.setter
    def db_instance_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__448207c47601fe3197b6125466abb081d69dbdaa94516e357765abbd3bd17a20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbInstanceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dbParameterGroupName")
    def db_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of an existing DB parameter group or a reference to an AWS::Neptune::DBParameterGroup resource created in the template.

        If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbparametergroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbParameterGroupName"))

    @db_parameter_group_name.setter
    def db_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a30308fe6702ce7e9fe957a0ad8803384554b3924cf2dac003d936c632a057a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''This parameter is not supported.

        ``AWS::Neptune::DBInstance`` does not support restoring from snapshots.

        ``AWS::Neptune::DBCluster`` does support restoring from snapshots.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbsnapshotidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSnapshotIdentifier"))

    @db_snapshot_identifier.setter
    def db_snapshot_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3979221f94740b369c3a98b9a887625a0dbac9db7a19d17b4276edbd506069)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSnapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''A DB subnet group to associate with the DB instance.

        If you update this value, the new subnet group must be a subnet group in a new virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbsubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a365ff19ad84890a2275929b79b7b04a7f2f12e72af21fec2b666fbbbe9908e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665f2f2b46768c6a2543146a65b04aa837dbf013090ec30a9cbea7c29f2f8ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.CfnDBInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "db_instance_class": "dbInstanceClass",
        "allow_major_version_upgrade": "allowMajorVersionUpgrade",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "db_cluster_identifier": "dbClusterIdentifier",
        "db_instance_identifier": "dbInstanceIdentifier",
        "db_parameter_group_name": "dbParameterGroupName",
        "db_snapshot_identifier": "dbSnapshotIdentifier",
        "db_subnet_group_name": "dbSubnetGroupName",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "tags": "tags",
    },
)
class CfnDBInstanceProps:
    def __init__(
        self,
        *,
        db_instance_class: builtins.str,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_instance_identifier: typing.Optional[builtins.str] = None,
        db_parameter_group_name: typing.Optional[builtins.str] = None,
        db_snapshot_identifier: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBInstance``.

        :param db_instance_class: Contains the name of the compute and memory capacity class of the DB instance. If you update this property, some interruptions may occur.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.
        :param auto_minor_version_upgrade: Indicates that minor version patches are applied automatically. When updating this property, some interruptions may occur.
        :param availability_zone: Specifies the name of the Availability Zone the DB instance is located in.
        :param db_cluster_identifier: If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
        :param db_instance_identifier: Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.
        :param db_parameter_group_name: The name of an existing DB parameter group or a reference to an AWS::Neptune::DBParameterGroup resource created in the template. If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.
        :param db_snapshot_identifier: This parameter is not supported. ``AWS::Neptune::DBInstance`` does not support restoring from snapshots. ``AWS::Neptune::DBCluster`` does support restoring from snapshots.
        :param db_subnet_group_name: A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new virtual private cloud (VPC).
        :param preferred_maintenance_window: Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        :param tags: An arbitrary set of tags (key-value pairs) for this DB instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_neptune as neptune
            
            cfn_dBInstance_props = neptune.CfnDBInstanceProps(
                db_instance_class="dbInstanceClass",
            
                # the properties below are optional
                allow_major_version_upgrade=False,
                auto_minor_version_upgrade=False,
                availability_zone="availabilityZone",
                db_cluster_identifier="dbClusterIdentifier",
                db_instance_identifier="dbInstanceIdentifier",
                db_parameter_group_name="dbParameterGroupName",
                db_snapshot_identifier="dbSnapshotIdentifier",
                db_subnet_group_name="dbSubnetGroupName",
                preferred_maintenance_window="preferredMaintenanceWindow",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1fb6d71eaeb543bc7cb3b9aa840bdbded401c75e10dac9b2a21126ce57fb87)
            check_type(argname="argument db_instance_class", value=db_instance_class, expected_type=type_hints["db_instance_class"])
            check_type(argname="argument allow_major_version_upgrade", value=allow_major_version_upgrade, expected_type=type_hints["allow_major_version_upgrade"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument db_instance_identifier", value=db_instance_identifier, expected_type=type_hints["db_instance_identifier"])
            check_type(argname="argument db_parameter_group_name", value=db_parameter_group_name, expected_type=type_hints["db_parameter_group_name"])
            check_type(argname="argument db_snapshot_identifier", value=db_snapshot_identifier, expected_type=type_hints["db_snapshot_identifier"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_instance_class": db_instance_class,
        }
        if allow_major_version_upgrade is not None:
            self._values["allow_major_version_upgrade"] = allow_major_version_upgrade
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_cluster_identifier is not None:
            self._values["db_cluster_identifier"] = db_cluster_identifier
        if db_instance_identifier is not None:
            self._values["db_instance_identifier"] = db_instance_identifier
        if db_parameter_group_name is not None:
            self._values["db_parameter_group_name"] = db_parameter_group_name
        if db_snapshot_identifier is not None:
            self._values["db_snapshot_identifier"] = db_snapshot_identifier
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def db_instance_class(self) -> builtins.str:
        '''Contains the name of the compute and memory capacity class of the DB instance.

        If you update this property, some interruptions may occur.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbinstanceclass
        '''
        result = self._values.get("db_instance_class")
        assert result is not None, "Required property 'db_instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates that major version upgrades are allowed.

        Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-allowmajorversionupgrade
        '''
        result = self._values.get("allow_major_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates that minor version patches are applied automatically.

        When updating this property, some interruptions may occur.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Availability Zone the DB instance is located in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbclusteridentifier
        '''
        result = self._values.get("db_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''Contains a user-supplied database identifier.

        This identifier is the unique key that identifies a DB instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbinstanceidentifier
        '''
        result = self._values.get("db_instance_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of an existing DB parameter group or a reference to an AWS::Neptune::DBParameterGroup resource created in the template.

        If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbparametergroupname
        '''
        result = self._values.get("db_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''This parameter is not supported.

        ``AWS::Neptune::DBInstance`` does not support restoring from snapshots.

        ``AWS::Neptune::DBCluster`` does support restoring from snapshots.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbsnapshotidentifier
        '''
        result = self._values.get("db_snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''A DB subnet group to associate with the DB instance.

        If you update this value, the new subnet group must be a subnet group in a new virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbsubnetgroupname
        '''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''An arbitrary set of tags (key-value pairs) for this DB instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDBParameterGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.CfnDBParameterGroup",
):
    '''A CloudFormation ``AWS::Neptune::DBParameterGroup``.

    ``AWS::Neptune::DBParameterGroup`` creates a new DB parameter group. This type can be declared in a template and referenced in the ``DBParameterGroupName`` parameter of ``AWS::Neptune::DBInstance`` .
    .. epigraph::

       Applying a parameter group to a DB instance might require the instance to reboot, resulting in a database outage for the duration of the reboot.

    A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using *ModifyDBParameterGroup* . Once you've created a DB parameter group, you need to associate it with your DB instance using *ModifyDBInstance* . When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.
    .. epigraph::

       After you create a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the ``character_set_database`` parameter. You can use the *Parameter Groups* option of the Amazon Neptune console or the *DescribeDBParameters* command to verify that your DB parameter group has been created or modified.

    :cloudformationResource: AWS::Neptune::DBParameterGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        # parameters: Any
        
        cfn_dBParameter_group = neptune.CfnDBParameterGroup(self, "MyCfnDBParameterGroup",
            description="description",
            family="family",
            parameters=parameters,
        
            # the properties below are optional
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Neptune::DBParameterGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: Provides the customer-specified description for this DB parameter group.
        :param family: Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.
        :param parameters: The parameters to set for this DB parameter group. The parameters are expressed as a JSON object consisting of key-value pairs. Changes to dynamic parameters are applied immediately. During an update, if you have static parameters (whether they were changed or not), it triggers AWS CloudFormation to reboot the associated DB instance without failover.
        :param name: Provides the name of the DB parameter group.
        :param tags: The tags that you want to attach to this parameter group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9531a12535e3dcc492841cafda57b477d641a45735206232b2cd6075573ce0b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBParameterGroupProps(
            description=description,
            family=family,
            parameters=parameters,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57f66b17c6a6e12dc93955c4934ddd681191171a1337bb0ebc8759a2a3f8e01d)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a586917b31ba82752540b0cdbeed4c44d439fc74221ac808486099911ceade15)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''The tags that you want to attach to this parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''Provides the customer-specified description for this DB parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9173da35b8da6ba1998acd81ff38951946a3e42564de4a226e6a20befc42ffbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        '''Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-family
        '''
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7677475fa98cc1ea9c8bfeefc803d5dbc0968050f8b4982847facd5bf236fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''The parameters to set for this DB parameter group.

        The parameters are expressed as a JSON object consisting of key-value pairs.

        Changes to dynamic parameters are applied immediately. During an update, if you have static parameters (whether they were changed or not), it triggers AWS CloudFormation to reboot the associated DB instance without failover.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-parameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242b7b7736ae59cc5383ae4aa595144a76e1d8d2eb761e37c376223fca5a4494)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Provides the name of the DB parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__988f5b78f66356e17f3013a33bb18c09a626c177cea9d2a26e909077197ca242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.CfnDBParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "family": "family",
        "parameters": "parameters",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDBParameterGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBParameterGroup``.

        :param description: Provides the customer-specified description for this DB parameter group.
        :param family: Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.
        :param parameters: The parameters to set for this DB parameter group. The parameters are expressed as a JSON object consisting of key-value pairs. Changes to dynamic parameters are applied immediately. During an update, if you have static parameters (whether they were changed or not), it triggers AWS CloudFormation to reboot the associated DB instance without failover.
        :param name: Provides the name of the DB parameter group.
        :param tags: The tags that you want to attach to this parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_neptune as neptune
            
            # parameters: Any
            
            cfn_dBParameter_group_props = neptune.CfnDBParameterGroupProps(
                description="description",
                family="family",
                parameters=parameters,
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f64e963b89f92f33d3bc9e8f24968777ab6d46e116cfdabe98f548686b43f56)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "family": family,
            "parameters": parameters,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''Provides the customer-specified description for this DB parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def family(self) -> builtins.str:
        '''Must be ``neptune1`` for engine versions prior to `1.2.0.0 <https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html>`_ , or ``neptune1.2`` for engine version ``1.2.0.0`` and higher.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-family
        '''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters to set for this DB parameter group.

        The parameters are expressed as a JSON object consisting of key-value pairs.

        Changes to dynamic parameters are applied immediately. During an update, if you have static parameters (whether they were changed or not), it triggers AWS CloudFormation to reboot the associated DB instance without failover.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-parameters
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Provides the name of the DB parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''The tags that you want to attach to this parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDBSubnetGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.CfnDBSubnetGroup",
):
    '''A CloudFormation ``AWS::Neptune::DBSubnetGroup``.

    The ``AWS::Neptune::DBSubnetGroup`` type creates an Amazon Neptune DB subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same AWS Region.

    :cloudformationResource: AWS::Neptune::DBSubnetGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        cfn_dBSubnet_group = neptune.CfnDBSubnetGroup(self, "MyCfnDBSubnetGroup",
            db_subnet_group_description="dbSubnetGroupDescription",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            db_subnet_group_name="dbSubnetGroupName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        db_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Neptune::DBSubnetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param db_subnet_group_description: Provides the description of the DB subnet group.
        :param subnet_ids: The Amazon EC2 subnet IDs for the DB subnet group.
        :param db_subnet_group_name: The name of the DB subnet group.
        :param tags: The tags that you want to attach to the DB subnet group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2262e2507b407657ba24a3ec51f766ba5e3d31f79c0c021e1b04ab4188e9dace)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBSubnetGroupProps(
            db_subnet_group_description=db_subnet_group_description,
            subnet_ids=subnet_ids,
            db_subnet_group_name=db_subnet_group_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df01555392876c797e5ffc30b112beaf54529a025b86b12a40f5497d1b8326e2)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f064c02d1de01be33001989ba9512c25bafa8f7869c2eee2d85b92df3ffa1ab)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''The tags that you want to attach to the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupDescription")
    def db_subnet_group_description(self) -> builtins.str:
        '''Provides the description of the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-dbsubnetgroupdescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbSubnetGroupDescription"))

    @db_subnet_group_description.setter
    def db_subnet_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a06736421152d2c958705ab802e2d3761236b6870df3e2ecc4b8e90c9a7610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The Amazon EC2 subnet IDs for the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39bbcb98e7e57c92236b37b495688ec832ee067f13cba815bae889584fd7b48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-dbsubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__810885be1ab82e6fdc39774db0790a05e9370f5c81a162e9f20ca5020ae22f79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.CfnDBSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "db_subnet_group_description": "dbSubnetGroupDescription",
        "subnet_ids": "subnetIds",
        "db_subnet_group_name": "dbSubnetGroupName",
        "tags": "tags",
    },
)
class CfnDBSubnetGroupProps:
    def __init__(
        self,
        *,
        db_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBSubnetGroup``.

        :param db_subnet_group_description: Provides the description of the DB subnet group.
        :param subnet_ids: The Amazon EC2 subnet IDs for the DB subnet group.
        :param db_subnet_group_name: The name of the DB subnet group.
        :param tags: The tags that you want to attach to the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_neptune as neptune
            
            cfn_dBSubnet_group_props = neptune.CfnDBSubnetGroupProps(
                db_subnet_group_description="dbSubnetGroupDescription",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                db_subnet_group_name="dbSubnetGroupName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6441a59239f7248ab62d741db23f65df2a2bf55cc216e9dee34b8696d10b448)
            check_type(argname="argument db_subnet_group_description", value=db_subnet_group_description, expected_type=type_hints["db_subnet_group_description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_subnet_group_description": db_subnet_group_description,
            "subnet_ids": subnet_ids,
        }
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def db_subnet_group_description(self) -> builtins.str:
        '''Provides the description of the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-dbsubnetgroupdescription
        '''
        result = self._values.get("db_subnet_group_description")
        assert result is not None, "Required property 'db_subnet_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The Amazon EC2 subnet IDs for the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-dbsubnetgroupname
        '''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''The tags that you want to attach to the DB subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.ClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameters": "parameters",
        "cluster_parameter_group_name": "clusterParameterGroupName",
        "description": "description",
    },
)
class ClusterParameterGroupProps:
    def __init__(
        self,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Marker class for cluster parameter group.

        :param parameters: (experimental) The parameters in this parameter group.
        :param cluster_parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description

        :stability: experimental
        :exampleMetadata: infused

        Example::

            cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
                description="Cluster parameter group",
                parameters={
                    "neptune_enable_audit_log": "1"
                }
            )
            
            db_params = neptune.ParameterGroup(self, "DbParams",
                description="Db parameter group",
                parameters={
                    "neptune_query_timeout": "120000"
                }
            )
            
            cluster = neptune.DatabaseCluster(self, "Database",
                vpc=vpc,
                instance_type=neptune.InstanceType.R5_LARGE,
                cluster_parameter_group=cluster_params,
                parameter_group=db_params
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__636f8b3fa2e201078e81259990468340f395b80d51f5a57b2f31f039079a5271)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument cluster_parameter_group_name", value=cluster_parameter_group_name, expected_type=type_hints["cluster_parameter_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameters": parameters,
        }
        if cluster_parameter_group_name is not None:
            self._values["cluster_parameter_group_name"] = cluster_parameter_group_name
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The parameters in this parameter group.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter group.

        :default: A CDK generated name for the parameter group

        :stability: experimental
        '''
        result = self._values.get("cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for this parameter group.

        :default: a CDK generated description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.DatabaseClusterAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_endpoint_address": "clusterEndpointAddress",
        "cluster_identifier": "clusterIdentifier",
        "cluster_resource_identifier": "clusterResourceIdentifier",
        "port": "port",
        "reader_endpoint_address": "readerEndpointAddress",
        "security_group": "securityGroup",
    },
)
class DatabaseClusterAttributes:
    def __init__(
        self,
        *,
        cluster_endpoint_address: builtins.str,
        cluster_identifier: builtins.str,
        cluster_resource_identifier: builtins.str,
        port: jsii.Number,
        reader_endpoint_address: builtins.str,
        security_group: _ISecurityGroup_cdbba9d3,
    ) -> None:
        '''(experimental) Properties that describe an existing cluster instance.

        :param cluster_endpoint_address: (experimental) Cluster endpoint address.
        :param cluster_identifier: (experimental) Identifier for the cluster.
        :param cluster_resource_identifier: (experimental) Resource Identifier for the cluster.
        :param port: (experimental) The database port.
        :param reader_endpoint_address: (experimental) Reader endpoint address.
        :param security_group: (experimental) The security group of the database cluster.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_ec2 as ec2
            from monocdk import aws_neptune as neptune
            
            # security_group: ec2.SecurityGroup
            
            database_cluster_attributes = neptune.DatabaseClusterAttributes(
                cluster_endpoint_address="clusterEndpointAddress",
                cluster_identifier="clusterIdentifier",
                cluster_resource_identifier="clusterResourceIdentifier",
                port=123,
                reader_endpoint_address="readerEndpointAddress",
                security_group=security_group
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a86ee433e52a4025ce1b1121ea90a74a035465c69a7956b2cfcfa1fbb936bd)
            check_type(argname="argument cluster_endpoint_address", value=cluster_endpoint_address, expected_type=type_hints["cluster_endpoint_address"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_resource_identifier", value=cluster_resource_identifier, expected_type=type_hints["cluster_resource_identifier"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument reader_endpoint_address", value=reader_endpoint_address, expected_type=type_hints["reader_endpoint_address"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_endpoint_address": cluster_endpoint_address,
            "cluster_identifier": cluster_identifier,
            "cluster_resource_identifier": cluster_resource_identifier,
            "port": port,
            "reader_endpoint_address": reader_endpoint_address,
            "security_group": security_group,
        }

    @builtins.property
    def cluster_endpoint_address(self) -> builtins.str:
        '''(experimental) Cluster endpoint address.

        :stability: experimental
        '''
        result = self._values.get("cluster_endpoint_address")
        assert result is not None, "Required property 'cluster_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier for the cluster.

        :stability: experimental
        '''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource Identifier for the cluster.

        :stability: experimental
        '''
        result = self._values.get("cluster_resource_identifier")
        assert result is not None, "Required property 'cluster_resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''(experimental) The database port.

        :stability: experimental
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def reader_endpoint_address(self) -> builtins.str:
        '''(experimental) Reader endpoint address.

        :stability: experimental
        '''
        result = self._values.get("reader_endpoint_address")
        assert result is not None, "Required property 'reader_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group(self) -> _ISecurityGroup_cdbba9d3:
        '''(experimental) The security group of the database cluster.

        :stability: experimental
        '''
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return typing.cast(_ISecurityGroup_cdbba9d3, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.DatabaseClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "vpc": "vpc",
        "associated_roles": "associatedRoles",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "backup_retention": "backupRetention",
        "cluster_parameter_group": "clusterParameterGroup",
        "db_cluster_name": "dbClusterName",
        "deletion_protection": "deletionProtection",
        "engine_version": "engineVersion",
        "iam_authentication": "iamAuthentication",
        "instance_identifier_base": "instanceIdentifierBase",
        "instances": "instances",
        "kms_key": "kmsKey",
        "parameter_group": "parameterGroup",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "removal_policy": "removalPolicy",
        "security_groups": "securityGroups",
        "storage_encrypted": "storageEncrypted",
        "subnet_group": "subnetGroup",
        "vpc_subnets": "vpcSubnets",
    },
)
class DatabaseClusterProps:
    def __init__(
        self,
        *,
        instance_type: "InstanceType",
        vpc: _IVpc_6d1f76c4,
        associated_roles: typing.Optional[typing.Sequence[_IRole_59af6f50]] = None,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        backup_retention: typing.Optional[_Duration_070aa057] = None,
        cluster_parameter_group: typing.Optional["IClusterParameterGroup"] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        engine_version: typing.Optional["EngineVersion"] = None,
        iam_authentication: typing.Optional[builtins.bool] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[_IKey_36930160] = None,
        parameter_group: typing.Optional["IParameterGroup"] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_cdbba9d3]] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
        subnet_group: typing.Optional["ISubnetGroup"] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for a new database cluster.

        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param vpc: (experimental) What subnets to run the Neptune instances in. Must be at least 2 subnets in two different AZs.
        :param associated_roles: (experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services. Default: - No role is attached to the cluster.
        :param auto_minor_version_upgrade: (experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks. Default: - false
        :param backup_retention: (experimental) How many days to retain the backup. Default: - cdk.Duration.days(1)
        :param cluster_parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
        :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
        :param deletion_protection: (experimental) Indicates whether the DB cluster should have deletion protection enabled. Default: - true if ``removalPolicy`` is RETAIN, false otherwise
        :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
        :param iam_authentication: (experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts. Default: - ``false``
        :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: (experimental) Number of Neptune compute instances. Default: 1
        :param kms_key: (experimental) The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param port: (experimental) The port the Neptune cluster will listen on. Default: - The default engine port
        :param preferred_backup_window: (experimental) A daily time range in 24-hours UTC format in which backups preferably execute. Must be at least 30 minutes long. Example: '01:00-02:00' Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see
        :param preferred_maintenance_window: (experimental) A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: (experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param security_groups: (experimental) Security group. Default: a new security group is created.
        :param storage_encrypted: (experimental) Whether to enable storage encryption. Default: true
        :param subnet_group: (experimental) Existing subnet group for the cluster. Default: - a new subnet group will be created.
        :param vpc_subnets: (experimental) Where to place the instances within the VPC. Default: private subnets

        :stability: experimental
        :exampleMetadata: infused

        Example::

            cluster = neptune.DatabaseCluster(self, "Database",
                vpc=vpc,
                instance_type=neptune.InstanceType.R5_LARGE,
                instances=2
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d622d32457ed8a245ceb3abcb570e97abaccbaece38ced991b9b2ee4fc0965ac)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument associated_roles", value=associated_roles, expected_type=type_hints["associated_roles"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument backup_retention", value=backup_retention, expected_type=type_hints["backup_retention"])
            check_type(argname="argument cluster_parameter_group", value=cluster_parameter_group, expected_type=type_hints["cluster_parameter_group"])
            check_type(argname="argument db_cluster_name", value=db_cluster_name, expected_type=type_hints["db_cluster_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument iam_authentication", value=iam_authentication, expected_type=type_hints["iam_authentication"])
            check_type(argname="argument instance_identifier_base", value=instance_identifier_base, expected_type=type_hints["instance_identifier_base"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument parameter_group", value=parameter_group, expected_type=type_hints["parameter_group"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument subnet_group", value=subnet_group, expected_type=type_hints["subnet_group"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "vpc": vpc,
        }
        if associated_roles is not None:
            self._values["associated_roles"] = associated_roles
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if backup_retention is not None:
            self._values["backup_retention"] = backup_retention
        if cluster_parameter_group is not None:
            self._values["cluster_parameter_group"] = cluster_parameter_group
        if db_cluster_name is not None:
            self._values["db_cluster_name"] = db_cluster_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if iam_authentication is not None:
            self._values["iam_authentication"] = iam_authentication
        if instance_identifier_base is not None:
            self._values["instance_identifier_base"] = instance_identifier_base
        if instances is not None:
            self._values["instances"] = instances
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if subnet_group is not None:
            self._values["subnet_group"] = subnet_group
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def instance_type(self) -> "InstanceType":
        '''(experimental) What type of instance to start for the replicas.

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast("InstanceType", result)

    @builtins.property
    def vpc(self) -> _IVpc_6d1f76c4:
        '''(experimental) What subnets to run the Neptune instances in.

        Must be at least 2 subnets in two different AZs.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_6d1f76c4, result)

    @builtins.property
    def associated_roles(self) -> typing.Optional[typing.List[_IRole_59af6f50]]:
        '''(experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services.

        :default: - No role is attached to the cluster.

        :stability: experimental
        '''
        result = self._values.get("associated_roles")
        return typing.cast(typing.Optional[typing.List[_IRole_59af6f50]], result)

    @builtins.property
    def auto_minor_version_upgrade(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks.

        :default: - false

        :stability: experimental
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def backup_retention(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) How many days to retain the backup.

        :default: - cdk.Duration.days(1)

        :stability: experimental
        '''
        result = self._values.get("backup_retention")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def cluster_parameter_group(self) -> typing.Optional["IClusterParameterGroup"]:
        '''(experimental) Additional parameters to pass to the database engine.

        :default: - No parameter group.

        :stability: experimental
        '''
        result = self._values.get("cluster_parameter_group")
        return typing.cast(typing.Optional["IClusterParameterGroup"], result)

    @builtins.property
    def db_cluster_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional identifier for the cluster.

        :default: - A name is automatically generated.

        :stability: experimental
        '''
        result = self._values.get("db_cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether the DB cluster should have deletion protection enabled.

        :default: - true if ``removalPolicy`` is RETAIN, false otherwise

        :stability: experimental
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def engine_version(self) -> typing.Optional["EngineVersion"]:
        '''(experimental) What version of the database to start.

        :default: - The default engine version.

        :stability: experimental
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional["EngineVersion"], result)

    @builtins.property
    def iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts.

        :default: - ``false``

        :stability: experimental
        '''
        result = self._values.get("iam_authentication")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_identifier_base(self) -> typing.Optional[builtins.str]:
        '''(experimental) Base identifier for instances.

        Every replica is named by appending the replica number to this string, 1-based.

        :default:

        - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the
        identifier is automatically generated.

        :stability: experimental
        '''
        result = self._values.get("instance_identifier_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instances(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Number of Neptune compute instances.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) The KMS key for storage encryption.

        :default: - default master key.

        :stability: experimental
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_36930160], result)

    @builtins.property
    def parameter_group(self) -> typing.Optional["IParameterGroup"]:
        '''(experimental) The DB parameter group to associate with the instance.

        :default: no parameter group

        :stability: experimental
        '''
        result = self._values.get("parameter_group")
        return typing.cast(typing.Optional["IParameterGroup"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The port the Neptune cluster will listen on.

        :default: - The default engine port

        :stability: experimental
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''(experimental) A daily time range in 24-hours UTC format in which backups preferably execute.

        Must be at least 30 minutes long.

        Example: '01:00-02:00'

        :default:

        - a 30-minute window selected at random from an 8-hour block of
        time for each AWS Region. To see the time blocks available, see

        :stability: experimental
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''(experimental) A weekly time range in which maintenance should preferably execute.

        Must be at least 30 minutes long.

        Example: 'tue:04:17-tue:04:47'

        :default:

        - 30-minute window selected at random from an 8-hour block of time for
        each AWS Region, occurring on a random day of the week.

        :stability: experimental
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        '''(experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted.

        This
        removal policy also applies to the implicit security group created for the
        cluster if one is not supplied as a parameter.

        :default: - Retain cluster.

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_c97e7a20], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]]:
        '''(experimental) Security group.

        :default: a new security group is created.

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]], result)

    @builtins.property
    def storage_encrypted(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to enable storage encryption.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_group(self) -> typing.Optional["ISubnetGroup"]:
        '''(experimental) Existing subnet group for the cluster.

        :default: - a new subnet group will be created.

        :stability: experimental
        '''
        result = self._values.get("subnet_group")
        return typing.cast(typing.Optional["ISubnetGroup"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        '''(experimental) Where to place the instances within the VPC.

        :default: private subnets

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_1284e62c], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.DatabaseInstanceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "instance_endpoint_address": "instanceEndpointAddress",
        "instance_identifier": "instanceIdentifier",
        "port": "port",
    },
)
class DatabaseInstanceAttributes:
    def __init__(
        self,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''(experimental) Properties that describe an existing instance.

        :param instance_endpoint_address: (experimental) The endpoint address.
        :param instance_identifier: (experimental) The instance identifier.
        :param port: (experimental) The database port.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_neptune as neptune
            
            database_instance_attributes = neptune.DatabaseInstanceAttributes(
                instance_endpoint_address="instanceEndpointAddress",
                instance_identifier="instanceIdentifier",
                port=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f45f6be7fc2aa9a2e6781e13c030a8ca93edcebffbe8bc10e177446e70b1de44)
            check_type(argname="argument instance_endpoint_address", value=instance_endpoint_address, expected_type=type_hints["instance_endpoint_address"])
            check_type(argname="argument instance_identifier", value=instance_identifier, expected_type=type_hints["instance_identifier"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_endpoint_address": instance_endpoint_address,
            "instance_identifier": instance_identifier,
            "port": port,
        }

    @builtins.property
    def instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The endpoint address.

        :stability: experimental
        '''
        result = self._values.get("instance_endpoint_address")
        assert result is not None, "Required property 'instance_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        '''
        result = self._values.get("instance_identifier")
        assert result is not None, "Required property 'instance_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''(experimental) The database port.

        :stability: experimental
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.DatabaseInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "instance_type": "instanceType",
        "availability_zone": "availabilityZone",
        "db_instance_name": "dbInstanceName",
        "parameter_group": "parameterGroup",
        "removal_policy": "removalPolicy",
    },
)
class DatabaseInstanceProps:
    def __init__(
        self,
        *,
        cluster: "IDatabaseCluster",
        instance_type: "InstanceType",
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        parameter_group: typing.Optional["IParameterGroup"] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    ) -> None:
        '''(experimental) Construction properties for a DatabaseInstanceNew.

        :param cluster: (experimental) The Neptune database cluster the instance should launch into.
        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param availability_zone: (experimental) The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: (experimental) A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param removal_policy: (experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :stability: experimental
        :exampleMetadata: fixture=with-cluster infused

        Example::

            replica1 = neptune.DatabaseInstance(self, "Instance",
                cluster=cluster,
                instance_type=neptune.InstanceType.R5_LARGE
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0136f7e070e22b1427432a4a1167a40c63db91692ee432b4de2b8b11cc7da36f)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument db_instance_name", value=db_instance_name, expected_type=type_hints["db_instance_name"])
            check_type(argname="argument parameter_group", value=parameter_group, expected_type=type_hints["parameter_group"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "instance_type": instance_type,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_instance_name is not None:
            self._values["db_instance_name"] = db_instance_name
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def cluster(self) -> "IDatabaseCluster":
        '''(experimental) The Neptune database cluster the instance should launch into.

        :stability: experimental
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("IDatabaseCluster", result)

    @builtins.property
    def instance_type(self) -> "InstanceType":
        '''(experimental) What type of instance to start for the replicas.

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast("InstanceType", result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the Availability Zone where the DB instance will be located.

        :default: - no preference

        :stability: experimental
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_instance_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the DB instance.

        If you specify a name, AWS CloudFormation
        converts it to lowercase.

        :default: - a CloudFormation generated name

        :stability: experimental
        '''
        result = self._values.get("db_instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group(self) -> typing.Optional["IParameterGroup"]:
        '''(experimental) The DB parameter group to associate with the instance.

        :default: no parameter group

        :stability: experimental
        '''
        result = self._values.get("parameter_group")
        return typing.cast(typing.Optional["IParameterGroup"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        '''(experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update.

        :default: RemovalPolicy.Retain

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_c97e7a20], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Endpoint(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_neptune.Endpoint"):
    '''(experimental) Connection endpoint of a neptune cluster or instance.

    Consists of a combination of hostname and port.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        endpoint = neptune.Endpoint("address", 123)
    '''

    def __init__(self, address: builtins.str, port: jsii.Number) -> None:
        '''
        :param address: -
        :param port: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b984e3cfe600b7c5ba0025f0211180de4756a4a88d72f67e877b85362b6ad4e)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [address, port])

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        '''(experimental) The hostname of the endpoint.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        '''(experimental) The port of the endpoint.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="socketAddress")
    def socket_address(self) -> builtins.str:
        '''(experimental) The combination of "HOSTNAME:PORT" for this endpoint.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "socketAddress"))


class EngineVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.EngineVersion",
):
    '''(experimental) Possible Instances Types to use in Neptune cluster used for defining {@link DatabaseClusterProps.engineVersion}.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_neptune as neptune
        
        engine_version = neptune.EngineVersion.V1_0_1_0
    '''

    def __init__(self, version: builtins.str) -> None:
        '''(experimental) Constructor for specifying a custom engine version.

        :param version: the engine version of Neptune.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5591e1f415b918c8c0b35a5b36e40cfaab54030fb1f2474ce69fc1d6ae8a20)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        jsii.create(self.__class__, self, [version])

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_1_0")
    def V1_0_1_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.1.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_1_1")
    def V1_0_1_1(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.1.1.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_1_2")
    def V1_0_1_2(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.1.2.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_1_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_2_1")
    def V1_0_2_1(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.2.1.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_2_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_2_2")
    def V1_0_2_2(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.2.2.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_2_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_3_0")
    def V1_0_3_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.3.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_3_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_4_0")
    def V1_0_4_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.4.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_4_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_4_1")
    def V1_0_4_1(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.4.1.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_4_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_5_0")
    def V1_0_5_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.5.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_5_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_1_0_0")
    def V1_1_0_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.1.0.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_1_0_0"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) the engine version of Neptune.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.interface(jsii_type="monocdk.aws_neptune.IClusterParameterGroup")
class IClusterParameterGroup(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        ...


class _IClusterParameterGroupProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_neptune.IClusterParameterGroup"

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterParameterGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterParameterGroup).__jsii_proxy_class__ = lambda : _IClusterParameterGroupProxy


@jsii.interface(jsii_type="monocdk.aws_neptune.IDatabaseCluster")
class IDatabaseCluster(
    _IResource_8c1dbbbd,
    _IConnectable_c1c0e72c,
    typing_extensions.Protocol,
):
    '''(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        :attribute: Endpoint,Port
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        :attribute: ReadEndpoint
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        :attribute: ClusterResourceId
        '''
        ...

    @jsii.member(jsii_name="grantConnect")
    def grant_connect(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Grant the given identity connection access to the database.

        :param grantee: -

        :stability: experimental
        '''
        ...


class _IDatabaseClusterProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
    jsii.proxy_for(_IConnectable_c1c0e72c), # type: ignore[misc]
):
    '''(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_neptune.IDatabaseCluster"

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        :attribute: Endpoint,Port
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        :attribute: ReadEndpoint
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        :attribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @jsii.member(jsii_name="grantConnect")
    def grant_connect(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Grant the given identity connection access to the database.

        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__530716cb2e0ea65597123d14208d7bddd9ee1dbe4721494374285325befac8d3)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantConnect", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseCluster).__jsii_proxy_class__ = lambda : _IDatabaseClusterProxy


@jsii.interface(jsii_type="monocdk.aws_neptune.IDatabaseInstance")
class IDatabaseInstance(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) A database instance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :attribute: Endpoint
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :attribute: Port
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        '''
        ...


class _IDatabaseInstanceProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
):
    '''(experimental) A database instance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_neptune.IDatabaseInstance"

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :attribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :attribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseInstance).__jsii_proxy_class__ = lambda : _IDatabaseInstanceProxy


@jsii.interface(jsii_type="monocdk.aws_neptune.IParameterGroup")
class IParameterGroup(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        ...


class _IParameterGroupProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_neptune.IParameterGroup"

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterGroup).__jsii_proxy_class__ = lambda : _IParameterGroupProxy


@jsii.interface(jsii_type="monocdk.aws_neptune.ISubnetGroup")
class ISubnetGroup(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) Interface for a subnet group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''(experimental) The name of the subnet group.

        :stability: experimental
        :attribute: true
        '''
        ...


class _ISubnetGroupProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
):
    '''(experimental) Interface for a subnet group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_neptune.ISubnetGroup"

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''(experimental) The name of the subnet group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetGroup).__jsii_proxy_class__ = lambda : _ISubnetGroupProxy


class InstanceType(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.InstanceType",
):
    '''(experimental) Possible Instances Types to use in Neptune cluster used for defining {@link DatabaseInstanceProps.instanceType}.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            instances=2
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, instance_type: builtins.str) -> "InstanceType":
        '''(experimental) Build an InstanceType from given string or token, such as CfnParameter.

        :param instance_type: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85d80fd2872d659c8fdfd814ef7c8d67286b0810419cb964e85a1e72d57a9928)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        return typing.cast("InstanceType", jsii.sinvoke(cls, "of", [instance_type]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_2XLARGE")
    def R4_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_4XLARGE")
    def R4_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_8XLARGE")
    def R4_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_LARGE")
    def R4_LARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_XLARGE")
    def R4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_12XLARGE")
    def R5_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_24XLARGE")
    def R5_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_2XLARGE")
    def R5_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_4XLARGE")
    def R5_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_8XLARGE")
    def R5_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_LARGE")
    def R5_LARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_XLARGE")
    def R5_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_12XLARGE")
    def R6_G_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_16XLARGE")
    def R6_G_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_2XLARGE")
    def R6_G_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_4XLARGE")
    def R6_G_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_8XLARGE")
    def R6_G_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_LARGE")
    def R6_G_LARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_XLARGE")
    def R6_G_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T3_MEDIUM")
    def T3_MEDIUM(cls) -> "InstanceType":
        '''(experimental) db.t3.medium.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T3_MEDIUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T4G_MEDIUM")
    def T4_G_MEDIUM(cls) -> "InstanceType":
        '''(experimental) db.t4g.medium.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T4G_MEDIUM"))


@jsii.implements(IParameterGroup)
class ParameterGroup(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.ParameterGroup",
):
    '''(experimental) DB parameter group.

    :stability: experimental
    :resource: AWS::Neptune::DBParameterGroup
    :exampleMetadata: infused

    Example::

        cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
            description="Cluster parameter group",
            parameters={
                "neptune_enable_audit_log": "1"
            }
        )
        
        db_params = neptune.ParameterGroup(self, "DbParams",
            description="Db parameter group",
            parameters={
                "neptune_query_timeout": "120000"
            }
        )
        
        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            cluster_parameter_group=cluster_params,
            parameter_group=db_params
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        description: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param parameters: (experimental) The parameters in this parameter group.
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description
        :param parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bcd246ad45691c628c1cfeaccac8f4476d466efdf28ebd13893227b61f644c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ParameterGroupProps(
            parameters=parameters,
            description=description,
            parameter_group_name=parameter_group_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromParameterGroupName")
    @builtins.classmethod
    def from_parameter_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        parameter_group_name: builtins.str,
    ) -> IParameterGroup:
        '''(experimental) Imports a parameter group.

        :param scope: -
        :param id: -
        :param parameter_group_name: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b31611094db72fd1c8de60994b5c7c6900c61c8a87630fc39c885999cc745356)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        return typing.cast(IParameterGroup, jsii.sinvoke(cls, "fromParameterGroupName", [scope, id, parameter_group_name]))

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of the parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.ParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameters": "parameters",
        "description": "description",
        "parameter_group_name": "parameterGroupName",
    },
)
class ParameterGroupProps:
    def __init__(
        self,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        description: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Marker class for cluster parameter group.

        :param parameters: (experimental) The parameters in this parameter group.
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description
        :param parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group

        :stability: experimental
        :exampleMetadata: infused

        Example::

            cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
                description="Cluster parameter group",
                parameters={
                    "neptune_enable_audit_log": "1"
                }
            )
            
            db_params = neptune.ParameterGroup(self, "DbParams",
                description="Db parameter group",
                parameters={
                    "neptune_query_timeout": "120000"
                }
            )
            
            cluster = neptune.DatabaseCluster(self, "Database",
                vpc=vpc,
                instance_type=neptune.InstanceType.R5_LARGE,
                cluster_parameter_group=cluster_params,
                parameter_group=db_params
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af31de91a8c93e485d793322d9f8f6d3272df36de18179eba26da914822469f6)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameters": parameters,
        }
        if description is not None:
            self._values["description"] = description
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name

    @builtins.property
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The parameters in this parameter group.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for this parameter group.

        :default: a CDK generated description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter group.

        :default: A CDK generated name for the parameter group

        :stability: experimental
        '''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISubnetGroup)
class SubnetGroup(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.SubnetGroup",
):
    '''(experimental) Class for creating a RDS DB subnet group.

    :stability: experimental
    :resource: AWS::Neptune::DBSubnetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import monocdk as monocdk
        from monocdk import aws_ec2 as ec2
        from monocdk import aws_neptune as neptune
        
        # subnet: ec2.Subnet
        # subnet_filter: ec2.SubnetFilter
        # vpc: ec2.Vpc
        
        subnet_group = neptune.SubnetGroup(self, "MySubnetGroup",
            vpc=vpc,
        
            # the properties below are optional
            description="description",
            removal_policy=monocdk.RemovalPolicy.DESTROY,
            subnet_group_name="subnetGroupName",
            vpc_subnets=ec2.SubnetSelection(
                availability_zones=["availabilityZones"],
                one_per_az=False,
                subnet_filters=[subnet_filter],
                subnet_group_name="subnetGroupName",
                subnet_name="subnetName",
                subnets=[subnet],
                subnet_type=ec2.SubnetType.ISOLATED
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        vpc: _IVpc_6d1f76c4,
        description: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: (experimental) The VPC to place the subnet group in.
        :param description: (experimental) Description of the subnet group. Default: - a name is generated
        :param removal_policy: (experimental) The removal policy to apply when the subnet group are removed from the stack or replaced during an update. Default: RemovalPolicy.DESTROY
        :param subnet_group_name: (experimental) The name of the subnet group. Default: - a name is generated
        :param vpc_subnets: (experimental) Which subnets within the VPC to associate with this group. Default: - private subnets

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09542191ecaf0819bd839a2e9ddebcc40070d5fbff23bcab52ed70eefc7b3277)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubnetGroupProps(
            vpc=vpc,
            description=description,
            removal_policy=removal_policy,
            subnet_group_name=subnet_group_name,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSubnetGroupName")
    @builtins.classmethod
    def from_subnet_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        subnet_group_name: builtins.str,
    ) -> ISubnetGroup:
        '''(experimental) Imports an existing subnet group by name.

        :param scope: -
        :param id: -
        :param subnet_group_name: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be9bb82eba36dd47eb521d7889b00213cb90ae48805388734e289eb3734ebbc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
        return typing.cast(ISubnetGroup, jsii.sinvoke(cls, "fromSubnetGroupName", [scope, id, subnet_group_name]))

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''(experimental) The name of the subnet group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))


@jsii.data_type(
    jsii_type="monocdk.aws_neptune.SubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "vpc": "vpc",
        "description": "description",
        "removal_policy": "removalPolicy",
        "subnet_group_name": "subnetGroupName",
        "vpc_subnets": "vpcSubnets",
    },
)
class SubnetGroupProps:
    def __init__(
        self,
        *,
        vpc: _IVpc_6d1f76c4,
        description: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for creating a SubnetGroup.

        :param vpc: (experimental) The VPC to place the subnet group in.
        :param description: (experimental) Description of the subnet group. Default: - a name is generated
        :param removal_policy: (experimental) The removal policy to apply when the subnet group are removed from the stack or replaced during an update. Default: RemovalPolicy.DESTROY
        :param subnet_group_name: (experimental) The name of the subnet group. Default: - a name is generated
        :param vpc_subnets: (experimental) Which subnets within the VPC to associate with this group. Default: - private subnets

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_ec2 as ec2
            from monocdk import aws_neptune as neptune
            
            # subnet: ec2.Subnet
            # subnet_filter: ec2.SubnetFilter
            # vpc: ec2.Vpc
            
            subnet_group_props = neptune.SubnetGroupProps(
                vpc=vpc,
            
                # the properties below are optional
                description="description",
                removal_policy=monocdk.RemovalPolicy.DESTROY,
                subnet_group_name="subnetGroupName",
                vpc_subnets=ec2.SubnetSelection(
                    availability_zones=["availabilityZones"],
                    one_per_az=False,
                    subnet_filters=[subnet_filter],
                    subnet_group_name="subnetGroupName",
                    subnet_name="subnetName",
                    subnets=[subnet],
                    subnet_type=ec2.SubnetType.ISOLATED
                )
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da38dbe97fed5704c6f6f37e7651709d3248a023e83546bdf05023e408d0c426)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
        }
        if description is not None:
            self._values["description"] = description
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def vpc(self) -> _IVpc_6d1f76c4:
        '''(experimental) The VPC to place the subnet group in.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_6d1f76c4, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description of the subnet group.

        :default: - a name is generated

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        '''(experimental) The removal policy to apply when the subnet group are removed from the stack or replaced during an update.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_c97e7a20], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the subnet group.

        :default: - a name is generated

        :stability: experimental
        '''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        '''(experimental) Which subnets within the VPC to associate with this group.

        :default: - private subnets

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_1284e62c], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IClusterParameterGroup)
class ClusterParameterGroup(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.ClusterParameterGroup",
):
    '''(experimental) A cluster parameter group.

    :stability: experimental
    :resource: AWS::Neptune::DBClusterParameterGroup
    :exampleMetadata: infused

    Example::

        cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
            description="Cluster parameter group",
            parameters={
                "neptune_enable_audit_log": "1"
            }
        )
        
        db_params = neptune.ParameterGroup(self, "DbParams",
            description="Db parameter group",
            parameters={
                "neptune_query_timeout": "120000"
            }
        )
        
        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            cluster_parameter_group=cluster_params,
            parameter_group=db_params
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param parameters: (experimental) The parameters in this parameter group.
        :param cluster_parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4245d85118c5239ed4321bc3b3eadbeb7f9c5ffdce76de6ddf598f8a6ca9376)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterParameterGroupProps(
            parameters=parameters,
            cluster_parameter_group_name=cluster_parameter_group_name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClusterParameterGroupName")
    @builtins.classmethod
    def from_cluster_parameter_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        cluster_parameter_group_name: builtins.str,
    ) -> IClusterParameterGroup:
        '''(experimental) Imports a parameter group.

        :param scope: -
        :param id: -
        :param cluster_parameter_group_name: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f12c73ccf22e9f10f7392856df2d09be4fcf95daafbea180558625bdf5edc50e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument cluster_parameter_group_name", value=cluster_parameter_group_name, expected_type=type_hints["cluster_parameter_group_name"])
        return typing.cast(IClusterParameterGroup, jsii.sinvoke(cls, "fromClusterParameterGroupName", [scope, id, cluster_parameter_group_name]))

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of the parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterParameterGroupName"))


@jsii.implements(IDatabaseCluster)
class DatabaseClusterBase(
    _Resource_abff4495,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_neptune.DatabaseClusterBase",
):
    '''(experimental) A new or imported database cluster.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_ec2 as ec2
        from monocdk import aws_neptune as neptune
        
        # security_group: ec2.SecurityGroup
        
        database_cluster_base = neptune.DatabaseClusterBase.from_database_cluster_attributes(self, "MyDatabaseClusterBase",
            cluster_endpoint_address="clusterEndpointAddress",
            cluster_identifier="clusterIdentifier",
            cluster_resource_identifier="clusterResourceIdentifier",
            port=123,
            reader_endpoint_address="readerEndpointAddress",
            security_group=security_group
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: (experimental) The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: (experimental) ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: (experimental) The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: (experimental) The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3120823d77ade184eafab00cd223ffe7c5e0fece54f5ef9a301ee9f529111cf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_9b554c0f(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseClusterAttributes")
    @builtins.classmethod
    def from_database_cluster_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_endpoint_address: builtins.str,
        cluster_identifier: builtins.str,
        cluster_resource_identifier: builtins.str,
        port: jsii.Number,
        reader_endpoint_address: builtins.str,
        security_group: _ISecurityGroup_cdbba9d3,
    ) -> IDatabaseCluster:
        '''(experimental) Import an existing DatabaseCluster from properties.

        :param scope: -
        :param id: -
        :param cluster_endpoint_address: (experimental) Cluster endpoint address.
        :param cluster_identifier: (experimental) Identifier for the cluster.
        :param cluster_resource_identifier: (experimental) Resource Identifier for the cluster.
        :param port: (experimental) The database port.
        :param reader_endpoint_address: (experimental) Reader endpoint address.
        :param security_group: (experimental) The security group of the database cluster.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4023667e5a5d9bdd8d55b859cdeef5eaefa8697aec7c1cea543dc73ab23b842)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DatabaseClusterAttributes(
            cluster_endpoint_address=cluster_endpoint_address,
            cluster_identifier=cluster_identifier,
            cluster_resource_identifier=cluster_resource_identifier,
            port=port,
            reader_endpoint_address=reader_endpoint_address,
            security_group=security_group,
        )

        return typing.cast(IDatabaseCluster, jsii.sinvoke(cls, "fromDatabaseClusterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="grantConnect")
    def grant_connect(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Grant the given identity connection access to the database.

        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb06be137eeaadb7fd6a4acc3d2ae7fdfb831abbf77934920cdf24d22c18178)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantConnect", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    @abc.abstractmethod
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    @abc.abstractmethod
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    @abc.abstractmethod
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    @abc.abstractmethod
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="connections")
    @abc.abstractmethod
    def connections(self) -> _Connections_57ccbda9:
        '''(experimental) The connections object to implement IConnectable.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="enableIamAuthentication")
    @abc.abstractmethod
    def _enable_iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        ...

    @_enable_iam_authentication.setter
    @abc.abstractmethod
    def _enable_iam_authentication(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _DatabaseClusterBaseProxy(
    DatabaseClusterBase,
    jsii.proxy_for(_Resource_abff4495), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_57ccbda9:
        '''(experimental) The connections object to implement IConnectable.

        :stability: experimental
        '''
        return typing.cast(_Connections_57ccbda9, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="enableIamAuthentication")
    def _enable_iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableIamAuthentication"))

    @_enable_iam_authentication.setter
    def _enable_iam_authentication(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96d996e19aa9e4339bdb05d1a98453cb02f62a6c59ea1ff5279eac8db1f020ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIamAuthentication", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DatabaseClusterBase).__jsii_proxy_class__ = lambda : _DatabaseClusterBaseProxy


@jsii.implements(IDatabaseInstance)
class DatabaseInstance(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.DatabaseInstance",
):
    '''(experimental) A database instance.

    :stability: experimental
    :resource: AWS::Neptune::DBInstance
    :exampleMetadata: fixture=with-cluster infused

    Example::

        replica1 = neptune.DatabaseInstance(self, "Instance",
            cluster=cluster,
            instance_type=neptune.InstanceType.R5_LARGE
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster: IDatabaseCluster,
        instance_type: InstanceType,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        parameter_group: typing.Optional[IParameterGroup] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: (experimental) The Neptune database cluster the instance should launch into.
        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param availability_zone: (experimental) The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: (experimental) A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param removal_policy: (experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1468d9fb32aa4aa8320dfa1ef6eb4ccaae12d03d49154499dead4cc03649afa3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseInstanceProps(
            cluster=cluster,
            instance_type=instance_type,
            availability_zone=availability_zone,
            db_instance_name=db_instance_name,
            parameter_group=parameter_group,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseInstanceAttributes")
    @builtins.classmethod
    def from_database_instance_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> IDatabaseInstance:
        '''(experimental) Import an existing database instance.

        :param scope: -
        :param id: -
        :param instance_endpoint_address: (experimental) The endpoint address.
        :param instance_identifier: (experimental) The instance identifier.
        :param port: (experimental) The database port.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a6cc6eb64b3208bf5d57d52d5774d4096dbbf4ac28fa42505918b896f92af3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DatabaseInstanceAttributes(
            instance_endpoint_address=instance_endpoint_address,
            instance_identifier=instance_identifier,
            port=port,
        )

        return typing.cast(IDatabaseInstance, jsii.sinvoke(cls, "fromDatabaseInstanceAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> IDatabaseCluster:
        '''(experimental) The instance's database cluster.

        :stability: experimental
        '''
        return typing.cast(IDatabaseCluster, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))


@jsii.implements(IDatabaseCluster)
class DatabaseCluster(
    DatabaseClusterBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_neptune.DatabaseCluster",
):
    '''(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    :resource: AWS::Neptune::DBCluster
    :exampleMetadata: infused

    Example::

        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            instances=2
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_type: InstanceType,
        vpc: _IVpc_6d1f76c4,
        associated_roles: typing.Optional[typing.Sequence[_IRole_59af6f50]] = None,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        backup_retention: typing.Optional[_Duration_070aa057] = None,
        cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        engine_version: typing.Optional[EngineVersion] = None,
        iam_authentication: typing.Optional[builtins.bool] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[_IKey_36930160] = None,
        parameter_group: typing.Optional[IParameterGroup] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_cdbba9d3]] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
        subnet_group: typing.Optional[ISubnetGroup] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param vpc: (experimental) What subnets to run the Neptune instances in. Must be at least 2 subnets in two different AZs.
        :param associated_roles: (experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services. Default: - No role is attached to the cluster.
        :param auto_minor_version_upgrade: (experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks. Default: - false
        :param backup_retention: (experimental) How many days to retain the backup. Default: - cdk.Duration.days(1)
        :param cluster_parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
        :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
        :param deletion_protection: (experimental) Indicates whether the DB cluster should have deletion protection enabled. Default: - true if ``removalPolicy`` is RETAIN, false otherwise
        :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
        :param iam_authentication: (experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts. Default: - ``false``
        :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: (experimental) Number of Neptune compute instances. Default: 1
        :param kms_key: (experimental) The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param port: (experimental) The port the Neptune cluster will listen on. Default: - The default engine port
        :param preferred_backup_window: (experimental) A daily time range in 24-hours UTC format in which backups preferably execute. Must be at least 30 minutes long. Example: '01:00-02:00' Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see
        :param preferred_maintenance_window: (experimental) A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: (experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param security_groups: (experimental) Security group. Default: a new security group is created.
        :param storage_encrypted: (experimental) Whether to enable storage encryption. Default: true
        :param subnet_group: (experimental) Existing subnet group for the cluster. Default: - a new subnet group will be created.
        :param vpc_subnets: (experimental) Where to place the instances within the VPC. Default: private subnets

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3635e07f45ca913ca4f3ae977143679943f25d21c049fe9e9cd539270ad791a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseClusterProps(
            instance_type=instance_type,
            vpc=vpc,
            associated_roles=associated_roles,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            backup_retention=backup_retention,
            cluster_parameter_group=cluster_parameter_group,
            db_cluster_name=db_cluster_name,
            deletion_protection=deletion_protection,
            engine_version=engine_version,
            iam_authentication=iam_authentication,
            instance_identifier_base=instance_identifier_base,
            instances=instances,
            kms_key=kms_key,
            parameter_group=parameter_group,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            removal_policy=removal_policy,
            security_groups=security_groups,
            storage_encrypted=storage_encrypted,
            subnet_group=subnet_group,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_NUM_INSTANCES")
    def DEFAULT_NUM_INSTANCES(cls) -> jsii.Number:
        '''(experimental) The default number of instances in the Neptune cluster if none are specified.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_NUM_INSTANCES"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) The resource id for the cluster;

        for example: cluster-ABCD1234EFGH5678IJKL90MNOP. The cluster ID uniquely
        identifies the cluster and is used in things like IAM authentication policies.

        :stability: experimental
        :attribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_57ccbda9:
        '''(experimental) The connections object to implement IConnectable.

        :stability: experimental
        '''
        return typing.cast(_Connections_57ccbda9, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        '''(experimental) Endpoints which address each individual instance.

        :stability: experimental
        '''
        return typing.cast(typing.List[Endpoint], jsii.get(self, "instanceEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        '''(experimental) Identifiers of the instance.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceIdentifiers"))

    @builtins.property
    @jsii.member(jsii_name="subnetGroup")
    def subnet_group(self) -> ISubnetGroup:
        '''(experimental) Subnet group used by the DB.

        :stability: experimental
        '''
        return typing.cast(ISubnetGroup, jsii.get(self, "subnetGroup"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> _IVpc_6d1f76c4:
        '''(experimental) The VPC where the DB subnet group is created.

        :stability: experimental
        '''
        return typing.cast(_IVpc_6d1f76c4, jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="vpcSubnets")
    def vpc_subnets(self) -> _SubnetSelection_1284e62c:
        '''(experimental) The subnets used by the DB subnet group.

        :stability: experimental
        '''
        return typing.cast(_SubnetSelection_1284e62c, jsii.get(self, "vpcSubnets"))

    @builtins.property
    @jsii.member(jsii_name="enableIamAuthentication")
    def _enable_iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableIamAuthentication"))

    @_enable_iam_authentication.setter
    def _enable_iam_authentication(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc55348b18daae72a916f4446a6207a851e8b1e4b996734b3ddcf22b572e65bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIamAuthentication", value)


__all__ = [
    "CfnDBCluster",
    "CfnDBClusterParameterGroup",
    "CfnDBClusterParameterGroupProps",
    "CfnDBClusterProps",
    "CfnDBInstance",
    "CfnDBInstanceProps",
    "CfnDBParameterGroup",
    "CfnDBParameterGroupProps",
    "CfnDBSubnetGroup",
    "CfnDBSubnetGroupProps",
    "ClusterParameterGroup",
    "ClusterParameterGroupProps",
    "DatabaseCluster",
    "DatabaseClusterAttributes",
    "DatabaseClusterBase",
    "DatabaseClusterProps",
    "DatabaseInstance",
    "DatabaseInstanceAttributes",
    "DatabaseInstanceProps",
    "Endpoint",
    "EngineVersion",
    "IClusterParameterGroup",
    "IDatabaseCluster",
    "IDatabaseInstance",
    "IParameterGroup",
    "ISubnetGroup",
    "InstanceType",
    "ParameterGroup",
    "ParameterGroupProps",
    "SubnetGroup",
    "SubnetGroupProps",
]

publication.publish()

def _typecheckingstub__110f0a0ca6029ca303ccae8c4b1962c65ff0b45e7d0966eade290eeae5ee729a(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    associated_roles: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnDBCluster.DBClusterRoleProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    db_cluster_identifier: typing.Optional[builtins.str] = None,
    db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    restore_to_time: typing.Optional[builtins.str] = None,
    restore_type: typing.Optional[builtins.str] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    source_db_cluster_identifier: typing.Optional[builtins.str] = None,
    storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a6ce322c50bc9084e6133094cb4401fe1adbb5965953fd21b500b0992834c2(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28e1e64cc5275c80c6f47ed013c54071cf7d21bc625fd6f689e01d1a3a860237(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a64529c1a353c08398998e015ac02cd1e4ba99312328b957222a78c98a7173df(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDBCluster.DBClusterRoleProperty, _IResolvable_a771d0ef]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7fcabe49cb63a4d591f30468f5bcabdcc3ba177fa37c0d49c7f76419600ff68(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e551bfda1f5fe7597511b098f86d55bd4377c666f04adaae0d4566c704cb9e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5273f369a2c6fae3a41345bb5c4f22d00808ac38cdd38073159005b2cf5e0cf5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dffc607e9308142bb1eb7d94565e22e808b21cdcecd6887da47f711a17c82b75(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663e5f807524c3c37f38e6de1f265ea06d8c8d2c419e68012accfe0251211790(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a183fe00ab2c4744d66b20fddca2e608a9128e7251e4da38dd6513018f9a8b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eecea3cea363cb4b46c8508826f18df296230035a032d74740dae7e3a708e00(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd71208085eb7cb069b63cc80e28fa9ff883a10c66815a41e4f2654cbeeccdb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bf49b70503842f6979907eb55b623a1780c8ce9cea9b7d10c3a118762501d0(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b9f060f88336d4561d525fa60e65cfc81d48d5ea7f5a5af76be5476388ce41(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c63efeb9a3573de6cd786e4e1e379b11fe9942b90dd66138be2c380055c484e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aefa7f4de3b606275bc08b0ae8c4d3a34930ac79c7df59f06bb3a0afec80cfcb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8d8d53155fce9af8c7d4d1ab0d95c46a5e33281cd00804bafd32bad2589bf6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb390a4d8cb25abb23e1ba947f838d339e9797b24a34a333f1d0102c98beb76(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5aaa7fc2573157105d2532204b5b9dfdeb492219e79e88e017d1ab35fd9477a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e498d9d1b7d0268549e83a61ade1fb2845fa1ceb7ee70400a8c02bc79a056248(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3bb98fb744b7a6099224397a2de663be76b9c1289b3bf8a1457f80cb1c3ec3c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d34deaa79c19af406cfeca0c8e222afa333b40bb15e1ed80a54a993dfbe74d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41994621c4a717d04de5812413cc948b8afd12bf89d14e57ebb745f2f75f76c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f430a7be49051a74c6c91d951d71aeccb6c9e1db3d6322a2e5d8ea5c03576992(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51377912c1292d83ddc74442be10cbd438049e46d7b0787cd6186a792152fba1(
    *,
    role_arn: builtins.str,
    feature_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05b2c3ccfadd7f38535855c44c75fdd9632e222bf34afaaff70fae41d14b5d9(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    description: builtins.str,
    family: builtins.str,
    parameters: typing.Any,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e821e5ea7bf8e93698cdea04b1b9e020502edefb0185ecdf214322b63d87061(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21c3ee8920c840687d9044b6daff47800dc77106fa6ddf95c4176c79e24f8804(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6d2bebeea5db75e1ea8f1c2321b92ad7f980de3e3712e9bd4e248dd61ace46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b640487ba2001e72f58363685c5bd1951e2efbc641915491dd99e6807e2f0fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9e4da527cfb52dbf0ee09d3f1c4aada153c5cd19b759b2accbfca834604446(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e4bd16626f0dfa51387a3ab9ff70abb0ab9800634eb91fc906ba16ce25c1dcb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfd09d54313fb179052cb8c2cbb7a17ee0718a06172bc7e4604f57cb1bdf280f(
    *,
    description: builtins.str,
    family: builtins.str,
    parameters: typing.Any,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5eaf46b1e8f8ecfa044c04fea9a8d313e373a0556ecbaeadf92b15e633e0880(
    *,
    associated_roles: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnDBCluster.DBClusterRoleProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    db_cluster_identifier: typing.Optional[builtins.str] = None,
    db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    restore_to_time: typing.Optional[builtins.str] = None,
    restore_type: typing.Optional[builtins.str] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    source_db_cluster_identifier: typing.Optional[builtins.str] = None,
    storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8a367809652871a1143ad207bbfa8c53f3ba49c49826ae7ef6f70d6a9067a5(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    db_instance_class: builtins.str,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    db_cluster_identifier: typing.Optional[builtins.str] = None,
    db_instance_identifier: typing.Optional[builtins.str] = None,
    db_parameter_group_name: typing.Optional[builtins.str] = None,
    db_snapshot_identifier: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1696b63951b7a18ec83e9b7a3738becddb501794dd5a54f9b5bfd1ec0a0312(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76df152bae97b41623f22250ac3287417f139c383492103f40d356bcb5585b5c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93e6eb318f9a5098b4f80fc5a2f201be470d29cfd55ba22d730859884dd26dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__372eae02d88f94c7cf93c12041d0608b7b720ddbf1ed30a73c2ff00d60cd9b47(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa184cdde7a3d69b2e71d3b36ee4668cbd4400184febfc17bb6e0f7eb74d6829(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d45cbcec0f761ea665aef83df2bae58fb8939a8ea563c95ecdfa7539a78010e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5fdb5582539d5602cc0f9e7fc9c1e50f203345b7c40942d6f44983a83af132a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__448207c47601fe3197b6125466abb081d69dbdaa94516e357765abbd3bd17a20(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30308fe6702ce7e9fe957a0ad8803384554b3924cf2dac003d936c632a057a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3979221f94740b369c3a98b9a887625a0dbac9db7a19d17b4276edbd506069(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a365ff19ad84890a2275929b79b7b04a7f2f12e72af21fec2b666fbbbe9908e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665f2f2b46768c6a2543146a65b04aa837dbf013090ec30a9cbea7c29f2f8ee4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1fb6d71eaeb543bc7cb3b9aa840bdbded401c75e10dac9b2a21126ce57fb87(
    *,
    db_instance_class: builtins.str,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    db_cluster_identifier: typing.Optional[builtins.str] = None,
    db_instance_identifier: typing.Optional[builtins.str] = None,
    db_parameter_group_name: typing.Optional[builtins.str] = None,
    db_snapshot_identifier: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9531a12535e3dcc492841cafda57b477d641a45735206232b2cd6075573ce0b4(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    description: builtins.str,
    family: builtins.str,
    parameters: typing.Any,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f66b17c6a6e12dc93955c4934ddd681191171a1337bb0ebc8759a2a3f8e01d(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a586917b31ba82752540b0cdbeed4c44d439fc74221ac808486099911ceade15(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9173da35b8da6ba1998acd81ff38951946a3e42564de4a226e6a20befc42ffbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7677475fa98cc1ea9c8bfeefc803d5dbc0968050f8b4982847facd5bf236fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242b7b7736ae59cc5383ae4aa595144a76e1d8d2eb761e37c376223fca5a4494(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988f5b78f66356e17f3013a33bb18c09a626c177cea9d2a26e909077197ca242(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f64e963b89f92f33d3bc9e8f24968777ab6d46e116cfdabe98f548686b43f56(
    *,
    description: builtins.str,
    family: builtins.str,
    parameters: typing.Any,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2262e2507b407657ba24a3ec51f766ba5e3d31f79c0c021e1b04ab4188e9dace(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    db_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df01555392876c797e5ffc30b112beaf54529a025b86b12a40f5497d1b8326e2(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f064c02d1de01be33001989ba9512c25bafa8f7869c2eee2d85b92df3ffa1ab(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a06736421152d2c958705ab802e2d3761236b6870df3e2ecc4b8e90c9a7610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39bbcb98e7e57c92236b37b495688ec832ee067f13cba815bae889584fd7b48(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__810885be1ab82e6fdc39774db0790a05e9370f5c81a162e9f20ca5020ae22f79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6441a59239f7248ab62d741db23f65df2a2bf55cc216e9dee34b8696d10b448(
    *,
    db_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__636f8b3fa2e201078e81259990468340f395b80d51f5a57b2f31f039079a5271(
    *,
    parameters: typing.Mapping[builtins.str, builtins.str],
    cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a86ee433e52a4025ce1b1121ea90a74a035465c69a7956b2cfcfa1fbb936bd(
    *,
    cluster_endpoint_address: builtins.str,
    cluster_identifier: builtins.str,
    cluster_resource_identifier: builtins.str,
    port: jsii.Number,
    reader_endpoint_address: builtins.str,
    security_group: _ISecurityGroup_cdbba9d3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d622d32457ed8a245ceb3abcb570e97abaccbaece38ced991b9b2ee4fc0965ac(
    *,
    instance_type: InstanceType,
    vpc: _IVpc_6d1f76c4,
    associated_roles: typing.Optional[typing.Sequence[_IRole_59af6f50]] = None,
    auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
    backup_retention: typing.Optional[_Duration_070aa057] = None,
    cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
    db_cluster_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    engine_version: typing.Optional[EngineVersion] = None,
    iam_authentication: typing.Optional[builtins.bool] = None,
    instance_identifier_base: typing.Optional[builtins.str] = None,
    instances: typing.Optional[jsii.Number] = None,
    kms_key: typing.Optional[_IKey_36930160] = None,
    parameter_group: typing.Optional[IParameterGroup] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_cdbba9d3]] = None,
    storage_encrypted: typing.Optional[builtins.bool] = None,
    subnet_group: typing.Optional[ISubnetGroup] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45f6be7fc2aa9a2e6781e13c030a8ca93edcebffbe8bc10e177446e70b1de44(
    *,
    instance_endpoint_address: builtins.str,
    instance_identifier: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0136f7e070e22b1427432a4a1167a40c63db91692ee432b4de2b8b11cc7da36f(
    *,
    cluster: IDatabaseCluster,
    instance_type: InstanceType,
    availability_zone: typing.Optional[builtins.str] = None,
    db_instance_name: typing.Optional[builtins.str] = None,
    parameter_group: typing.Optional[IParameterGroup] = None,
    removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b984e3cfe600b7c5ba0025f0211180de4756a4a88d72f67e877b85362b6ad4e(
    address: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5591e1f415b918c8c0b35a5b36e40cfaab54030fb1f2474ce69fc1d6ae8a20(
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__530716cb2e0ea65597123d14208d7bddd9ee1dbe4721494374285325befac8d3(
    grantee: _IGrantable_4c5a91d1,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85d80fd2872d659c8fdfd814ef7c8d67286b0810419cb964e85a1e72d57a9928(
    instance_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bcd246ad45691c628c1cfeaccac8f4476d466efdf28ebd13893227b61f644c4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Mapping[builtins.str, builtins.str],
    description: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b31611094db72fd1c8de60994b5c7c6900c61c8a87630fc39c885999cc745356(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af31de91a8c93e485d793322d9f8f6d3272df36de18179eba26da914822469f6(
    *,
    parameters: typing.Mapping[builtins.str, builtins.str],
    description: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09542191ecaf0819bd839a2e9ddebcc40070d5fbff23bcab52ed70eefc7b3277(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    vpc: _IVpc_6d1f76c4,
    description: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be9bb82eba36dd47eb521d7889b00213cb90ae48805388734e289eb3734ebbc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da38dbe97fed5704c6f6f37e7651709d3248a023e83546bdf05023e408d0c426(
    *,
    vpc: _IVpc_6d1f76c4,
    description: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4245d85118c5239ed4321bc3b3eadbeb7f9c5ffdce76de6ddf598f8a6ca9376(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Mapping[builtins.str, builtins.str],
    cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f12c73ccf22e9f10f7392856df2d09be4fcf95daafbea180558625bdf5edc50e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    cluster_parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3120823d77ade184eafab00cd223ffe7c5e0fece54f5ef9a301ee9f529111cf6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4023667e5a5d9bdd8d55b859cdeef5eaefa8697aec7c1cea543dc73ab23b842(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_endpoint_address: builtins.str,
    cluster_identifier: builtins.str,
    cluster_resource_identifier: builtins.str,
    port: jsii.Number,
    reader_endpoint_address: builtins.str,
    security_group: _ISecurityGroup_cdbba9d3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb06be137eeaadb7fd6a4acc3d2ae7fdfb831abbf77934920cdf24d22c18178(
    grantee: _IGrantable_4c5a91d1,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d996e19aa9e4339bdb05d1a98453cb02f62a6c59ea1ff5279eac8db1f020ce(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1468d9fb32aa4aa8320dfa1ef6eb4ccaae12d03d49154499dead4cc03649afa3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: IDatabaseCluster,
    instance_type: InstanceType,
    availability_zone: typing.Optional[builtins.str] = None,
    db_instance_name: typing.Optional[builtins.str] = None,
    parameter_group: typing.Optional[IParameterGroup] = None,
    removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a6cc6eb64b3208bf5d57d52d5774d4096dbbf4ac28fa42505918b896f92af3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_endpoint_address: builtins.str,
    instance_identifier: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3635e07f45ca913ca4f3ae977143679943f25d21c049fe9e9cd539270ad791a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: InstanceType,
    vpc: _IVpc_6d1f76c4,
    associated_roles: typing.Optional[typing.Sequence[_IRole_59af6f50]] = None,
    auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
    backup_retention: typing.Optional[_Duration_070aa057] = None,
    cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
    db_cluster_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    engine_version: typing.Optional[EngineVersion] = None,
    iam_authentication: typing.Optional[builtins.bool] = None,
    instance_identifier_base: typing.Optional[builtins.str] = None,
    instances: typing.Optional[jsii.Number] = None,
    kms_key: typing.Optional[_IKey_36930160] = None,
    parameter_group: typing.Optional[IParameterGroup] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_cdbba9d3]] = None,
    storage_encrypted: typing.Optional[builtins.bool] = None,
    subnet_group: typing.Optional[ISubnetGroup] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_1284e62c, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc55348b18daae72a916f4446a6207a851e8b1e4b996734b3ddcf22b572e65bb(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

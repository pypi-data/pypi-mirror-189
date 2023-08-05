'''
# AWS::KinesisAnalyticsV2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as kinesisanalytics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KinesisAnalyticsV2 construct libraries](https://constructs.dev/search?q=kinesisanalyticsv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KinesisAnalyticsV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KinesisAnalyticsV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnApplication(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::Application``.

    Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see `Creating an Application <https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html>`_ .

    :cloudformationResource: AWS::KinesisAnalyticsV2::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
        
        cfn_application = kinesisanalyticsv2.CfnApplication(self, "MyCfnApplication",
            runtime_environment="runtimeEnvironment",
            service_execution_role="serviceExecutionRole",
        
            # the properties below are optional
            application_configuration=kinesisanalyticsv2.CfnApplication.ApplicationConfigurationProperty(
                application_code_configuration=kinesisanalyticsv2.CfnApplication.ApplicationCodeConfigurationProperty(
                    code_content=kinesisanalyticsv2.CfnApplication.CodeContentProperty(
                        s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
        
                            # the properties below are optional
                            object_version="objectVersion"
                        ),
                        text_content="textContent",
                        zip_file_content="zipFileContent"
                    ),
                    code_content_type="codeContentType"
                ),
                application_snapshot_configuration=kinesisanalyticsv2.CfnApplication.ApplicationSnapshotConfigurationProperty(
                    snapshots_enabled=False
                ),
                environment_properties=kinesisanalyticsv2.CfnApplication.EnvironmentPropertiesProperty(
                    property_groups=[kinesisanalyticsv2.CfnApplication.PropertyGroupProperty(
                        property_group_id="propertyGroupId",
                        property_map={
                            "property_map_key": "propertyMap"
                        }
                    )]
                ),
                flink_application_configuration=kinesisanalyticsv2.CfnApplication.FlinkApplicationConfigurationProperty(
                    checkpoint_configuration=kinesisanalyticsv2.CfnApplication.CheckpointConfigurationProperty(
                        configuration_type="configurationType",
        
                        # the properties below are optional
                        checkpointing_enabled=False,
                        checkpoint_interval=123,
                        min_pause_between_checkpoints=123
                    ),
                    monitoring_configuration=kinesisanalyticsv2.CfnApplication.MonitoringConfigurationProperty(
                        configuration_type="configurationType",
        
                        # the properties below are optional
                        log_level="logLevel",
                        metrics_level="metricsLevel"
                    ),
                    parallelism_configuration=kinesisanalyticsv2.CfnApplication.ParallelismConfigurationProperty(
                        configuration_type="configurationType",
        
                        # the properties below are optional
                        auto_scaling_enabled=False,
                        parallelism=123,
                        parallelism_per_kpu=123
                    )
                ),
                sql_application_configuration=kinesisanalyticsv2.CfnApplication.SqlApplicationConfigurationProperty(
                    inputs=[kinesisanalyticsv2.CfnApplication.InputProperty(
                        input_schema=kinesisanalyticsv2.CfnApplication.InputSchemaProperty(
                            record_columns=[kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                                name="name",
                                sql_type="sqlType",
        
                                # the properties below are optional
                                mapping="mapping"
                            )],
                            record_format=kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                                record_format_type="recordFormatType",
        
                                # the properties below are optional
                                mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                                    csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                                        record_column_delimiter="recordColumnDelimiter",
                                        record_row_delimiter="recordRowDelimiter"
                                    ),
                                    json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                                        record_row_path="recordRowPath"
                                    )
                                )
                            ),
        
                            # the properties below are optional
                            record_encoding="recordEncoding"
                        ),
                        name_prefix="namePrefix",
        
                        # the properties below are optional
                        input_parallelism=kinesisanalyticsv2.CfnApplication.InputParallelismProperty(
                            count=123
                        ),
                        input_processing_configuration=kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty(
                            input_lambda_processor=kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                                resource_arn="resourceArn"
                            )
                        ),
                        kinesis_firehose_input=kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty(
                            resource_arn="resourceArn"
                        ),
                        kinesis_streams_input=kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty(
                            resource_arn="resourceArn"
                        )
                    )]
                ),
                vpc_configurations=[kinesisanalyticsv2.CfnApplication.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )],
                zeppelin_application_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinApplicationConfigurationProperty(
                    catalog_configuration=kinesisanalyticsv2.CfnApplication.CatalogConfigurationProperty(
                        glue_data_catalog_configuration=kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty(
                            database_arn="databaseArn"
                        )
                    ),
                    custom_artifacts_configuration=[kinesisanalyticsv2.CfnApplication.CustomArtifactConfigurationProperty(
                        artifact_type="artifactType",
        
                        # the properties below are optional
                        maven_reference=kinesisanalyticsv2.CfnApplication.MavenReferenceProperty(
                            artifact_id="artifactId",
                            group_id="groupId",
                            version="version"
                        ),
                        s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
        
                            # the properties below are optional
                            object_version="objectVersion"
                        )
                    )],
                    deploy_as_application_configuration=kinesisanalyticsv2.CfnApplication.DeployAsApplicationConfigurationProperty(
                        s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty(
                            bucket_arn="bucketArn",
        
                            # the properties below are optional
                            base_path="basePath"
                        )
                    ),
                    monitoring_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinMonitoringConfigurationProperty(
                        log_level="logLevel"
                    )
                )
            ),
            application_description="applicationDescription",
            application_maintenance_configuration=kinesisanalyticsv2.CfnApplication.ApplicationMaintenanceConfigurationProperty(
                application_maintenance_window_start_time="applicationMaintenanceWindowStartTime"
            ),
            application_mode="applicationMode",
            application_name="applicationName",
            run_configuration=kinesisanalyticsv2.CfnApplication.RunConfigurationProperty(
                application_restore_configuration=kinesisanalyticsv2.CfnApplication.ApplicationRestoreConfigurationProperty(
                    application_restore_type="applicationRestoreType",
        
                    # the properties below are optional
                    snapshot_name="snapshotName"
                ),
                flink_run_configuration=kinesisanalyticsv2.CfnApplication.FlinkRunConfigurationProperty(
                    allow_non_restored_state=False
                )
            ),
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
        runtime_environment: builtins.str,
        service_execution_role: builtins.str,
        application_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        application_description: typing.Optional[builtins.str] = None,
        application_maintenance_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ApplicationMaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        application_mode: typing.Optional[builtins.str] = None,
        application_name: typing.Optional[builtins.str] = None,
        run_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.RunConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param runtime_environment: The runtime environment for the application.
        :param service_execution_role: Specifies the IAM role that the application uses to access external resources.
        :param application_configuration: Use this parameter to configure the application.
        :param application_description: The description of the application.
        :param application_maintenance_configuration: ``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.
        :param application_mode: To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` . However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.
        :param application_name: The name of the application.
        :param run_configuration: ``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.
        :param tags: A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12e67892a82c6d1808b5d6c741fa71363db5f6826592dea9906e4acd4726c71b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            runtime_environment=runtime_environment,
            service_execution_role=service_execution_role,
            application_configuration=application_configuration,
            application_description=application_description,
            application_maintenance_configuration=application_maintenance_configuration,
            application_mode=application_mode,
            application_name=application_name,
            run_configuration=run_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b072b5b9c049860c2761003244200c7bfc5b54664a33d619d25b598d43a1443)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e100f6d8c189b6599865437dacff274cc5f6d10779f4a1ac0bad3a6e74e72fb0)
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
        '''A list of one or more tags to assign to the application.

        A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEnvironment")
    def runtime_environment(self) -> builtins.str:
        '''The runtime environment for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
        '''
        return typing.cast(builtins.str, jsii.get(self, "runtimeEnvironment"))

    @runtime_environment.setter
    def runtime_environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1dd55ad95914803e10f8c8eaeb87515063322bc9a9c814946c8166395fa4035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRole")
    def service_execution_role(self) -> builtins.str:
        '''Specifies the IAM role that the application uses to access external resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRole"))

    @service_execution_role.setter
    def service_execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a10b6ff7459cf5fe1f1266f7aef330cfd09792a0c3bb052627c00ece64faa425)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRole", value)

    @builtins.property
    @jsii.member(jsii_name="applicationConfiguration")
    def application_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.ApplicationConfigurationProperty", _IResolvable_a771d0ef]]:
        '''Use this parameter to configure the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.ApplicationConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "applicationConfiguration"))

    @application_configuration.setter
    def application_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.ApplicationConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b235931470408a9cb299904e2942364a0b27e4565b900c557b297bf8205a397c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="applicationDescription")
    def application_description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationDescription"))

    @application_description.setter
    def application_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1aa2e851a1c297bdc7e6dad9869dfe704d5f6003bfa580d283074ae041adadf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationDescription", value)

    @builtins.property
    @jsii.member(jsii_name="applicationMaintenanceConfiguration")
    def application_maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.ApplicationMaintenanceConfigurationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.ApplicationMaintenanceConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "applicationMaintenanceConfiguration"))

    @application_maintenance_configuration.setter
    def application_maintenance_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.ApplicationMaintenanceConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__743c8a381911e16447a8636deacd67efd6da8dca4f27b3eaf23b97b03627071b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationMaintenanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="applicationMode")
    def application_mode(self) -> typing.Optional[builtins.str]:
        '''To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` .

        However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationMode"))

    @application_mode.setter
    def application_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bd09b1de1838881420cce52ab783d77852e5c8f550939f1fc3563f1a7e2b4fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationMode", value)

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fbec8560868a34badcbc4885de17d083836da83abfe5ba02a394aec0f9704d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="runConfiguration")
    def run_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.RunConfigurationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.RunConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "runConfiguration"))

    @run_configuration.setter
    def run_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.RunConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699b043527d0eab8bc137440c2366270bb1cf87b18f80da555845fd0e200414e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runConfiguration", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ApplicationCodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_content": "codeContent",
            "code_content_type": "codeContentType",
        },
    )
    class ApplicationCodeConfigurationProperty:
        def __init__(
            self,
            *,
            code_content: typing.Union[typing.Union["CfnApplication.CodeContentProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            code_content_type: builtins.str,
        ) -> None:
            '''Describes code configuration for an application.

            :param code_content: The location and type of the application code.
            :param code_content_type: Specifies whether the code content is in text or zip format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                application_code_configuration_property = kinesisanalyticsv2.CfnApplication.ApplicationCodeConfigurationProperty(
                    code_content=kinesisanalyticsv2.CfnApplication.CodeContentProperty(
                        s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
                
                            # the properties below are optional
                            object_version="objectVersion"
                        ),
                        text_content="textContent",
                        zip_file_content="zipFileContent"
                    ),
                    code_content_type="codeContentType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13eeab7bbd807eedcde281c9bdc70fd1558cf16e894d7621aeae5ef23b21000e)
                check_type(argname="argument code_content", value=code_content, expected_type=type_hints["code_content"])
                check_type(argname="argument code_content_type", value=code_content_type, expected_type=type_hints["code_content_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code_content": code_content,
                "code_content_type": code_content_type,
            }

        @builtins.property
        def code_content(
            self,
        ) -> typing.Union["CfnApplication.CodeContentProperty", _IResolvable_a771d0ef]:
            '''The location and type of the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent
            '''
            result = self._values.get("code_content")
            assert result is not None, "Required property 'code_content' is missing"
            return typing.cast(typing.Union["CfnApplication.CodeContentProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def code_content_type(self) -> builtins.str:
            '''Specifies whether the code content is in text or zip format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype
            '''
            result = self._values.get("code_content_type")
            assert result is not None, "Required property 'code_content_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationCodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_code_configuration": "applicationCodeConfiguration",
            "application_snapshot_configuration": "applicationSnapshotConfiguration",
            "environment_properties": "environmentProperties",
            "flink_application_configuration": "flinkApplicationConfiguration",
            "sql_application_configuration": "sqlApplicationConfiguration",
            "vpc_configurations": "vpcConfigurations",
            "zeppelin_application_configuration": "zeppelinApplicationConfiguration",
        },
    )
    class ApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            application_code_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ApplicationCodeConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            application_snapshot_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ApplicationSnapshotConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            environment_properties: typing.Optional[typing.Union[typing.Union["CfnApplication.EnvironmentPropertiesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            flink_application_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.FlinkApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            sql_application_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.SqlApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            vpc_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplication.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
            zeppelin_application_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ZeppelinApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Specifies the creation parameters for a Kinesis Data Analytics application.

            :param application_code_configuration: The code location and type parameters for a Flink-based Kinesis Data Analytics application.
            :param application_snapshot_configuration: Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.
            :param environment_properties: Describes execution properties for a Flink-based Kinesis Data Analytics application.
            :param flink_application_configuration: The creation and update parameters for a Flink-based Kinesis Data Analytics application.
            :param sql_application_configuration: The creation and update parameters for a SQL-based Kinesis Data Analytics application.
            :param vpc_configurations: The array of descriptions of VPC configurations available to the application.
            :param zeppelin_application_configuration: The configuration parameters for a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                application_configuration_property = kinesisanalyticsv2.CfnApplication.ApplicationConfigurationProperty(
                    application_code_configuration=kinesisanalyticsv2.CfnApplication.ApplicationCodeConfigurationProperty(
                        code_content=kinesisanalyticsv2.CfnApplication.CodeContentProperty(
                            s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
                
                                # the properties below are optional
                                object_version="objectVersion"
                            ),
                            text_content="textContent",
                            zip_file_content="zipFileContent"
                        ),
                        code_content_type="codeContentType"
                    ),
                    application_snapshot_configuration=kinesisanalyticsv2.CfnApplication.ApplicationSnapshotConfigurationProperty(
                        snapshots_enabled=False
                    ),
                    environment_properties=kinesisanalyticsv2.CfnApplication.EnvironmentPropertiesProperty(
                        property_groups=[kinesisanalyticsv2.CfnApplication.PropertyGroupProperty(
                            property_group_id="propertyGroupId",
                            property_map={
                                "property_map_key": "propertyMap"
                            }
                        )]
                    ),
                    flink_application_configuration=kinesisanalyticsv2.CfnApplication.FlinkApplicationConfigurationProperty(
                        checkpoint_configuration=kinesisanalyticsv2.CfnApplication.CheckpointConfigurationProperty(
                            configuration_type="configurationType",
                
                            # the properties below are optional
                            checkpointing_enabled=False,
                            checkpoint_interval=123,
                            min_pause_between_checkpoints=123
                        ),
                        monitoring_configuration=kinesisanalyticsv2.CfnApplication.MonitoringConfigurationProperty(
                            configuration_type="configurationType",
                
                            # the properties below are optional
                            log_level="logLevel",
                            metrics_level="metricsLevel"
                        ),
                        parallelism_configuration=kinesisanalyticsv2.CfnApplication.ParallelismConfigurationProperty(
                            configuration_type="configurationType",
                
                            # the properties below are optional
                            auto_scaling_enabled=False,
                            parallelism=123,
                            parallelism_per_kpu=123
                        )
                    ),
                    sql_application_configuration=kinesisanalyticsv2.CfnApplication.SqlApplicationConfigurationProperty(
                        inputs=[kinesisanalyticsv2.CfnApplication.InputProperty(
                            input_schema=kinesisanalyticsv2.CfnApplication.InputSchemaProperty(
                                record_columns=[kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                                    name="name",
                                    sql_type="sqlType",
                
                                    # the properties below are optional
                                    mapping="mapping"
                                )],
                                record_format=kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                                    record_format_type="recordFormatType",
                
                                    # the properties below are optional
                                    mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                                        csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                                            record_column_delimiter="recordColumnDelimiter",
                                            record_row_delimiter="recordRowDelimiter"
                                        ),
                                        json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                                            record_row_path="recordRowPath"
                                        )
                                    )
                                ),
                
                                # the properties below are optional
                                record_encoding="recordEncoding"
                            ),
                            name_prefix="namePrefix",
                
                            # the properties below are optional
                            input_parallelism=kinesisanalyticsv2.CfnApplication.InputParallelismProperty(
                                count=123
                            ),
                            input_processing_configuration=kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty(
                                input_lambda_processor=kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                                    resource_arn="resourceArn"
                                )
                            ),
                            kinesis_firehose_input=kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty(
                                resource_arn="resourceArn"
                            ),
                            kinesis_streams_input=kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty(
                                resource_arn="resourceArn"
                            )
                        )]
                    ),
                    vpc_configurations=[kinesisanalyticsv2.CfnApplication.VpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )],
                    zeppelin_application_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinApplicationConfigurationProperty(
                        catalog_configuration=kinesisanalyticsv2.CfnApplication.CatalogConfigurationProperty(
                            glue_data_catalog_configuration=kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty(
                                database_arn="databaseArn"
                            )
                        ),
                        custom_artifacts_configuration=[kinesisanalyticsv2.CfnApplication.CustomArtifactConfigurationProperty(
                            artifact_type="artifactType",
                
                            # the properties below are optional
                            maven_reference=kinesisanalyticsv2.CfnApplication.MavenReferenceProperty(
                                artifact_id="artifactId",
                                group_id="groupId",
                                version="version"
                            ),
                            s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
                
                                # the properties below are optional
                                object_version="objectVersion"
                            )
                        )],
                        deploy_as_application_configuration=kinesisanalyticsv2.CfnApplication.DeployAsApplicationConfigurationProperty(
                            s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty(
                                bucket_arn="bucketArn",
                
                                # the properties below are optional
                                base_path="basePath"
                            )
                        ),
                        monitoring_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinMonitoringConfigurationProperty(
                            log_level="logLevel"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__daf609d2989df28525010c375f134f6321667a16467ea4466f5d4e0726803488)
                check_type(argname="argument application_code_configuration", value=application_code_configuration, expected_type=type_hints["application_code_configuration"])
                check_type(argname="argument application_snapshot_configuration", value=application_snapshot_configuration, expected_type=type_hints["application_snapshot_configuration"])
                check_type(argname="argument environment_properties", value=environment_properties, expected_type=type_hints["environment_properties"])
                check_type(argname="argument flink_application_configuration", value=flink_application_configuration, expected_type=type_hints["flink_application_configuration"])
                check_type(argname="argument sql_application_configuration", value=sql_application_configuration, expected_type=type_hints["sql_application_configuration"])
                check_type(argname="argument vpc_configurations", value=vpc_configurations, expected_type=type_hints["vpc_configurations"])
                check_type(argname="argument zeppelin_application_configuration", value=zeppelin_application_configuration, expected_type=type_hints["zeppelin_application_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_code_configuration is not None:
                self._values["application_code_configuration"] = application_code_configuration
            if application_snapshot_configuration is not None:
                self._values["application_snapshot_configuration"] = application_snapshot_configuration
            if environment_properties is not None:
                self._values["environment_properties"] = environment_properties
            if flink_application_configuration is not None:
                self._values["flink_application_configuration"] = flink_application_configuration
            if sql_application_configuration is not None:
                self._values["sql_application_configuration"] = sql_application_configuration
            if vpc_configurations is not None:
                self._values["vpc_configurations"] = vpc_configurations
            if zeppelin_application_configuration is not None:
                self._values["zeppelin_application_configuration"] = zeppelin_application_configuration

        @builtins.property
        def application_code_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ApplicationCodeConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The code location and type parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration
            '''
            result = self._values.get("application_code_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ApplicationCodeConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def application_snapshot_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ApplicationSnapshotConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration
            '''
            result = self._values.get("application_snapshot_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ApplicationSnapshotConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def environment_properties(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.EnvironmentPropertiesProperty", _IResolvable_a771d0ef]]:
            '''Describes execution properties for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties
            '''
            result = self._values.get("environment_properties")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.EnvironmentPropertiesProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def flink_application_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.FlinkApplicationConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The creation and update parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration
            '''
            result = self._values.get("flink_application_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.FlinkApplicationConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def sql_application_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.SqlApplicationConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The creation and update parameters for a SQL-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration
            '''
            result = self._values.get("sql_application_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.SqlApplicationConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def vpc_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.VpcConfigurationProperty", _IResolvable_a771d0ef]]]]:
            '''The array of descriptions of VPC configurations available to the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-vpcconfigurations
            '''
            result = self._values.get("vpc_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.VpcConfigurationProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def zeppelin_application_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ZeppelinApplicationConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The configuration parameters for a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration
            '''
            result = self._values.get("zeppelin_application_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ZeppelinApplicationConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ApplicationMaintenanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_maintenance_window_start_time": "applicationMaintenanceWindowStartTime",
        },
    )
    class ApplicationMaintenanceConfigurationProperty:
        def __init__(
            self,
            *,
            application_maintenance_window_start_time: builtins.str,
        ) -> None:
            '''Specifies the maintence window parameters for a Kinesis Data Analytics application.

            :param application_maintenance_window_start_time: Specifies the start time of the maintence window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                application_maintenance_configuration_property = kinesisanalyticsv2.CfnApplication.ApplicationMaintenanceConfigurationProperty(
                    application_maintenance_window_start_time="applicationMaintenanceWindowStartTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7462f8d09fdb8ff887317583b98a199e471b98e4a50f44f1f8a2644c21f6639d)
                check_type(argname="argument application_maintenance_window_start_time", value=application_maintenance_window_start_time, expected_type=type_hints["application_maintenance_window_start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_maintenance_window_start_time": application_maintenance_window_start_time,
            }

        @builtins.property
        def application_maintenance_window_start_time(self) -> builtins.str:
            '''Specifies the start time of the maintence window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-applicationmaintenancewindowstarttime
            '''
            result = self._values.get("application_maintenance_window_start_time")
            assert result is not None, "Required property 'application_maintenance_window_start_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationMaintenanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ApplicationRestoreConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_restore_type": "applicationRestoreType",
            "snapshot_name": "snapshotName",
        },
    )
    class ApplicationRestoreConfigurationProperty:
        def __init__(
            self,
            *,
            application_restore_type: builtins.str,
            snapshot_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the method and snapshot to use when restarting an application using previously saved application state.

            :param application_restore_type: Specifies how the application should be restored.
            :param snapshot_name: The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                application_restore_configuration_property = kinesisanalyticsv2.CfnApplication.ApplicationRestoreConfigurationProperty(
                    application_restore_type="applicationRestoreType",
                
                    # the properties below are optional
                    snapshot_name="snapshotName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6aa7fb84287e4033b4cb56097667a9b3357e1e5b751480d08cfe91262ef33589)
                check_type(argname="argument application_restore_type", value=application_restore_type, expected_type=type_hints["application_restore_type"])
                check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_restore_type": application_restore_type,
            }
            if snapshot_name is not None:
                self._values["snapshot_name"] = snapshot_name

        @builtins.property
        def application_restore_type(self) -> builtins.str:
            '''Specifies how the application should be restored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html#cfn-kinesisanalyticsv2-application-applicationrestoreconfiguration-applicationrestoretype
            '''
            result = self._values.get("application_restore_type")
            assert result is not None, "Required property 'application_restore_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def snapshot_name(self) -> typing.Optional[builtins.str]:
            '''The identifier of an existing snapshot of application state to use to restart an application.

            The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html#cfn-kinesisanalyticsv2-application-applicationrestoreconfiguration-snapshotname
            '''
            result = self._values.get("snapshot_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationRestoreConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ApplicationSnapshotConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshots_enabled": "snapshotsEnabled"},
    )
    class ApplicationSnapshotConfigurationProperty:
        def __init__(
            self,
            *,
            snapshots_enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        ) -> None:
            '''Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :param snapshots_enabled: Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                application_snapshot_configuration_property = kinesisanalyticsv2.CfnApplication.ApplicationSnapshotConfigurationProperty(
                    snapshots_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dc52c2ce7cc5186b3dff29ff0057aecc56120b03cf3d81011bc77552df12ce09)
                check_type(argname="argument snapshots_enabled", value=snapshots_enabled, expected_type=type_hints["snapshots_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "snapshots_enabled": snapshots_enabled,
            }

        @builtins.property
        def snapshots_enabled(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled
            '''
            result = self._values.get("snapshots_enabled")
            assert result is not None, "Required property 'snapshots_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationSnapshotConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_column_delimiter": "recordColumnDelimiter",
            "record_row_delimiter": "recordRowDelimiter",
        },
    )
    class CSVMappingParametersProperty:
        def __init__(
            self,
            *,
            record_column_delimiter: builtins.str,
            record_row_delimiter: builtins.str,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV.

            For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

            ``"name1", "address1"``

            ``"name2", "address2"``

            :param record_column_delimiter: The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
            :param record_row_delimiter: The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                c_sVMapping_parameters_property = kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                    record_column_delimiter="recordColumnDelimiter",
                    record_row_delimiter="recordRowDelimiter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f14e6d57cccce8fda1518d7421e571116034a17fcfe62756d1e8b612e5faf4c9)
                check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
                check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_column_delimiter": record_column_delimiter,
                "record_row_delimiter": record_row_delimiter,
            }

        @builtins.property
        def record_column_delimiter(self) -> builtins.str:
            '''The column delimiter.

            For example, in a CSV format, a comma (",") is the typical column delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordcolumndelimiter
            '''
            result = self._values.get("record_column_delimiter")
            assert result is not None, "Required property 'record_column_delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_row_delimiter(self) -> builtins.str:
            '''The row delimiter.

            For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordrowdelimiter
            '''
            result = self._values.get("record_row_delimiter")
            assert result is not None, "Required property 'record_row_delimiter' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CSVMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.CatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "glue_data_catalog_configuration": "glueDataCatalogConfiguration",
        },
    )
    class CatalogConfigurationProperty:
        def __init__(
            self,
            *,
            glue_data_catalog_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.GlueDataCatalogConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The configuration parameters for the default Amazon Glue database.

            You use this database for SQL queries that you write in a Kinesis Data Analytics Studio notebook.

            :param glue_data_catalog_configuration: The configuration parameters for the default Amazon Glue database. You use this database for Apache Flink SQL queries and table API transforms that you write in a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                catalog_configuration_property = kinesisanalyticsv2.CfnApplication.CatalogConfigurationProperty(
                    glue_data_catalog_configuration=kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty(
                        database_arn="databaseArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f220f09714a28332714008ca1cbd47bc4805aeb1ef275e127b85c1f08bc7f494)
                check_type(argname="argument glue_data_catalog_configuration", value=glue_data_catalog_configuration, expected_type=type_hints["glue_data_catalog_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_data_catalog_configuration is not None:
                self._values["glue_data_catalog_configuration"] = glue_data_catalog_configuration

        @builtins.property
        def glue_data_catalog_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.GlueDataCatalogConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The configuration parameters for the default Amazon Glue database.

            You use this database for Apache Flink SQL queries and table API transforms that you write in a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration
            '''
            result = self._values.get("glue_data_catalog_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.GlueDataCatalogConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.CheckpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_type": "configurationType",
            "checkpointing_enabled": "checkpointingEnabled",
            "checkpoint_interval": "checkpointInterval",
            "min_pause_between_checkpoints": "minPauseBetweenCheckpoints",
        },
    )
    class CheckpointConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_type: builtins.str,
            checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            checkpoint_interval: typing.Optional[jsii.Number] = None,
            min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes an application's checkpointing configuration.

            Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .

            :param configuration_type: Describes whether the application uses Kinesis Data Analytics' default checkpointing behavior. You must set this property to ``CUSTOM`` in order to set the ``CheckpointingEnabled`` , ``CheckpointInterval`` , or ``MinPauseBetweenCheckpoints`` parameters. .. epigraph:: If this value is set to ``DEFAULT`` , the application will use the following values, even if they are set to other values using APIs or application code: - *CheckpointingEnabled:* true - *CheckpointInterval:* 60000 - *MinPauseBetweenCheckpoints:* 5000
            :param checkpointing_enabled: Describes whether checkpointing is enabled for a Flink-based Kinesis Data Analytics application. .. epigraph:: If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointingEnabled`` value of ``true`` , even if this value is set to another value using this API or in application code.
            :param checkpoint_interval: Describes the interval in milliseconds between checkpoint operations. .. epigraph:: If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointInterval`` value of 60000, even if this value is set to another value using this API or in application code.
            :param min_pause_between_checkpoints: Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the ``CheckpointInterval`` , the application otherwise performs continual checkpoint operations. For more information, see `Tuning Checkpointing <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/large_state_tuning.html#tuning-checkpointing>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ . .. epigraph:: If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``MinPauseBetweenCheckpoints`` value of 5000, even if this value is set using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                checkpoint_configuration_property = kinesisanalyticsv2.CfnApplication.CheckpointConfigurationProperty(
                    configuration_type="configurationType",
                
                    # the properties below are optional
                    checkpointing_enabled=False,
                    checkpoint_interval=123,
                    min_pause_between_checkpoints=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be8c4bd6829e531df3cbac9d8bb68bb24a5d7c9d978d05e21da8c79156cf88cf)
                check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
                check_type(argname="argument checkpointing_enabled", value=checkpointing_enabled, expected_type=type_hints["checkpointing_enabled"])
                check_type(argname="argument checkpoint_interval", value=checkpoint_interval, expected_type=type_hints["checkpoint_interval"])
                check_type(argname="argument min_pause_between_checkpoints", value=min_pause_between_checkpoints, expected_type=type_hints["min_pause_between_checkpoints"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_type": configuration_type,
            }
            if checkpointing_enabled is not None:
                self._values["checkpointing_enabled"] = checkpointing_enabled
            if checkpoint_interval is not None:
                self._values["checkpoint_interval"] = checkpoint_interval
            if min_pause_between_checkpoints is not None:
                self._values["min_pause_between_checkpoints"] = min_pause_between_checkpoints

        @builtins.property
        def configuration_type(self) -> builtins.str:
            '''Describes whether the application uses Kinesis Data Analytics' default checkpointing behavior.

            You must set this property to ``CUSTOM`` in order to set the ``CheckpointingEnabled`` , ``CheckpointInterval`` , or ``MinPauseBetweenCheckpoints`` parameters.
            .. epigraph::

               If this value is set to ``DEFAULT`` , the application will use the following values, even if they are set to other values using APIs or application code:

               - *CheckpointingEnabled:* true
               - *CheckpointInterval:* 60000
               - *MinPauseBetweenCheckpoints:* 5000

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype
            '''
            result = self._values.get("configuration_type")
            assert result is not None, "Required property 'configuration_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def checkpointing_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Describes whether checkpointing is enabled for a Flink-based Kinesis Data Analytics application.

            .. epigraph::

               If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointingEnabled`` value of ``true`` , even if this value is set to another value using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled
            '''
            result = self._values.get("checkpointing_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def checkpoint_interval(self) -> typing.Optional[jsii.Number]:
            '''Describes the interval in milliseconds between checkpoint operations.

            .. epigraph::

               If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointInterval`` value of 60000, even if this value is set to another value using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval
            '''
            result = self._values.get("checkpoint_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_pause_between_checkpoints(self) -> typing.Optional[jsii.Number]:
            '''Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

            If a checkpoint operation takes longer than the ``CheckpointInterval`` , the application otherwise performs continual checkpoint operations. For more information, see `Tuning Checkpointing <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/large_state_tuning.html#tuning-checkpointing>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .
            .. epigraph::

               If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``MinPauseBetweenCheckpoints`` value of 5000, even if this value is set using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints
            '''
            result = self._values.get("min_pause_between_checkpoints")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CheckpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.CodeContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_content_location": "s3ContentLocation",
            "text_content": "textContent",
            "zip_file_content": "zipFileContent",
        },
    )
    class CodeContentProperty:
        def __init__(
            self,
            *,
            s3_content_location: typing.Optional[typing.Union[typing.Union["CfnApplication.S3ContentLocationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            text_content: typing.Optional[builtins.str] = None,
            zip_file_content: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies either the application code, or the location of the application code, for a Flink-based Kinesis Data Analytics application.

            :param s3_content_location: Information about the Amazon S3 bucket that contains the application code.
            :param text_content: The text-format code for a Flink-based Kinesis Data Analytics application.
            :param zip_file_content: The zip-format code for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                code_content_property = kinesisanalyticsv2.CfnApplication.CodeContentProperty(
                    s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                
                        # the properties below are optional
                        object_version="objectVersion"
                    ),
                    text_content="textContent",
                    zip_file_content="zipFileContent"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5da6df32ce408303384d90949a674ab8c057c88fd28d42887434699d64aaaff)
                check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
                check_type(argname="argument text_content", value=text_content, expected_type=type_hints["text_content"])
                check_type(argname="argument zip_file_content", value=zip_file_content, expected_type=type_hints["zip_file_content"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_content_location is not None:
                self._values["s3_content_location"] = s3_content_location
            if text_content is not None:
                self._values["text_content"] = text_content
            if zip_file_content is not None:
                self._values["zip_file_content"] = zip_file_content

        @builtins.property
        def s3_content_location(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.S3ContentLocationProperty", _IResolvable_a771d0ef]]:
            '''Information about the Amazon S3 bucket that contains the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation
            '''
            result = self._values.get("s3_content_location")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.S3ContentLocationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def text_content(self) -> typing.Optional[builtins.str]:
            '''The text-format code for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent
            '''
            result = self._values.get("text_content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zip_file_content(self) -> typing.Optional[builtins.str]:
            '''The zip-format code for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent
            '''
            result = self._values.get("zip_file_content")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.CustomArtifactConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "artifact_type": "artifactType",
            "maven_reference": "mavenReference",
            "s3_content_location": "s3ContentLocation",
        },
    )
    class CustomArtifactConfigurationProperty:
        def __init__(
            self,
            *,
            artifact_type: builtins.str,
            maven_reference: typing.Optional[typing.Union[typing.Union["CfnApplication.MavenReferenceProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            s3_content_location: typing.Optional[typing.Union[typing.Union["CfnApplication.S3ContentLocationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The configuration of connectors and user-defined functions.

            :param artifact_type: Set this to either ``UDF`` or ``DEPENDENCY_JAR`` . ``UDF`` stands for user-defined functions. This type of artifact must be in an S3 bucket. A ``DEPENDENCY_JAR`` can be in either Maven or an S3 bucket.
            :param maven_reference: The parameters required to fully specify a Maven reference.
            :param s3_content_location: The location of the custom artifacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                custom_artifact_configuration_property = kinesisanalyticsv2.CfnApplication.CustomArtifactConfigurationProperty(
                    artifact_type="artifactType",
                
                    # the properties below are optional
                    maven_reference=kinesisanalyticsv2.CfnApplication.MavenReferenceProperty(
                        artifact_id="artifactId",
                        group_id="groupId",
                        version="version"
                    ),
                    s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                
                        # the properties below are optional
                        object_version="objectVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ac8ebe88f7cd9056ef1e8530d1f385c787f7bcc14f35dd6085fdd081c7c6344)
                check_type(argname="argument artifact_type", value=artifact_type, expected_type=type_hints["artifact_type"])
                check_type(argname="argument maven_reference", value=maven_reference, expected_type=type_hints["maven_reference"])
                check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "artifact_type": artifact_type,
            }
            if maven_reference is not None:
                self._values["maven_reference"] = maven_reference
            if s3_content_location is not None:
                self._values["s3_content_location"] = s3_content_location

        @builtins.property
        def artifact_type(self) -> builtins.str:
            '''Set this to either ``UDF`` or ``DEPENDENCY_JAR`` .

            ``UDF`` stands for user-defined functions. This type of artifact must be in an S3 bucket. A ``DEPENDENCY_JAR`` can be in either Maven or an S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype
            '''
            result = self._values.get("artifact_type")
            assert result is not None, "Required property 'artifact_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maven_reference(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.MavenReferenceProperty", _IResolvable_a771d0ef]]:
            '''The parameters required to fully specify a Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference
            '''
            result = self._values.get("maven_reference")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.MavenReferenceProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def s3_content_location(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.S3ContentLocationProperty", _IResolvable_a771d0ef]]:
            '''The location of the custom artifacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation
            '''
            result = self._values.get("s3_content_location")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.S3ContentLocationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomArtifactConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.DeployAsApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_content_location": "s3ContentLocation"},
    )
    class DeployAsApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            s3_content_location: typing.Union[typing.Union["CfnApplication.S3ContentBaseLocationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        ) -> None:
            '''The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.

            :param s3_content_location: The description of an Amazon S3 object that contains the Amazon Data Analytics application, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                deploy_as_application_configuration_property = kinesisanalyticsv2.CfnApplication.DeployAsApplicationConfigurationProperty(
                    s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty(
                        bucket_arn="bucketArn",
                
                        # the properties below are optional
                        base_path="basePath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf70e5813fb387690981a05abe1b3349f24f89b7f5f7552d25470e14d324df06)
                check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_content_location": s3_content_location,
            }

        @builtins.property
        def s3_content_location(
            self,
        ) -> typing.Union["CfnApplication.S3ContentBaseLocationProperty", _IResolvable_a771d0ef]:
            '''The description of an Amazon S3 object that contains the Amazon Data Analytics application, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation
            '''
            result = self._values.get("s3_content_location")
            assert result is not None, "Required property 's3_content_location' is missing"
            return typing.cast(typing.Union["CfnApplication.S3ContentBaseLocationProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeployAsApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.EnvironmentPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"property_groups": "propertyGroups"},
    )
    class EnvironmentPropertiesProperty:
        def __init__(
            self,
            *,
            property_groups: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplication.PropertyGroupProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''Describes execution properties for a Flink-based Kinesis Data Analytics application.

            :param property_groups: Describes the execution property groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                environment_properties_property = kinesisanalyticsv2.CfnApplication.EnvironmentPropertiesProperty(
                    property_groups=[kinesisanalyticsv2.CfnApplication.PropertyGroupProperty(
                        property_group_id="propertyGroupId",
                        property_map={
                            "property_map_key": "propertyMap"
                        }
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e2149252f1fba3853f4547ab1e4a59f90dbb1440c859dd59819f6a15f8eb1f7)
                check_type(argname="argument property_groups", value=property_groups, expected_type=type_hints["property_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if property_groups is not None:
                self._values["property_groups"] = property_groups

        @builtins.property
        def property_groups(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.PropertyGroupProperty", _IResolvable_a771d0ef]]]]:
            '''Describes the execution property groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups
            '''
            result = self._values.get("property_groups")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.PropertyGroupProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.FlinkApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "checkpoint_configuration": "checkpointConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
            "parallelism_configuration": "parallelismConfiguration",
        },
    )
    class FlinkApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            checkpoint_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.CheckpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            monitoring_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            parallelism_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ParallelismConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes configuration parameters for a Flink-based Kinesis Data Analytics application or a Studio notebook.

            :param checkpoint_configuration: Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .
            :param monitoring_configuration: Describes configuration parameters for Amazon CloudWatch logging for an application.
            :param parallelism_configuration: Describes parameters for how an application executes multiple tasks simultaneously.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                flink_application_configuration_property = kinesisanalyticsv2.CfnApplication.FlinkApplicationConfigurationProperty(
                    checkpoint_configuration=kinesisanalyticsv2.CfnApplication.CheckpointConfigurationProperty(
                        configuration_type="configurationType",
                
                        # the properties below are optional
                        checkpointing_enabled=False,
                        checkpoint_interval=123,
                        min_pause_between_checkpoints=123
                    ),
                    monitoring_configuration=kinesisanalyticsv2.CfnApplication.MonitoringConfigurationProperty(
                        configuration_type="configurationType",
                
                        # the properties below are optional
                        log_level="logLevel",
                        metrics_level="metricsLevel"
                    ),
                    parallelism_configuration=kinesisanalyticsv2.CfnApplication.ParallelismConfigurationProperty(
                        configuration_type="configurationType",
                
                        # the properties below are optional
                        auto_scaling_enabled=False,
                        parallelism=123,
                        parallelism_per_kpu=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b605308ceb4be4709633e97f0a389cdd488993b82d8d56b81c0550ab8617b1ba)
                check_type(argname="argument checkpoint_configuration", value=checkpoint_configuration, expected_type=type_hints["checkpoint_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
                check_type(argname="argument parallelism_configuration", value=parallelism_configuration, expected_type=type_hints["parallelism_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if checkpoint_configuration is not None:
                self._values["checkpoint_configuration"] = checkpoint_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration
            if parallelism_configuration is not None:
                self._values["parallelism_configuration"] = parallelism_configuration

        @builtins.property
        def checkpoint_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.CheckpointConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Describes an application's checkpointing configuration.

            Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration
            '''
            result = self._values.get("checkpoint_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.CheckpointConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.MonitoringConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Describes configuration parameters for Amazon CloudWatch logging for an application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.MonitoringConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def parallelism_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ParallelismConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Describes parameters for how an application executes multiple tasks simultaneously.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration
            '''
            result = self._values.get("parallelism_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ParallelismConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlinkApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.FlinkRunConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allow_non_restored_state": "allowNonRestoredState"},
    )
    class FlinkRunConfigurationProperty:
        def __init__(
            self,
            *,
            allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes the starting parameters for a Flink-based Kinesis Data Analytics application.

            :param allow_non_restored_state: When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see `Allowing Non-Restored State <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/savepoints.html#allowing-non-restored-state>`_ in the `Apache Flink documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ . .. epigraph:: This value defaults to ``false`` . If you update your application without specifying this parameter, ``AllowNonRestoredState`` will be set to ``false`` , even if it was previously set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                flink_run_configuration_property = kinesisanalyticsv2.CfnApplication.FlinkRunConfigurationProperty(
                    allow_non_restored_state=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4da069b82e76ab0194e91430281f179c3d6668b09bca4be4fa71c5a61c93ca8)
                check_type(argname="argument allow_non_restored_state", value=allow_non_restored_state, expected_type=type_hints["allow_non_restored_state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_non_restored_state is not None:
                self._values["allow_non_restored_state"] = allow_non_restored_state

        @builtins.property
        def allow_non_restored_state(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program.

            This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see `Allowing Non-Restored State <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/savepoints.html#allowing-non-restored-state>`_ in the `Apache Flink documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .
            .. epigraph::

               This value defaults to ``false`` . If you update your application without specifying this parameter, ``AllowNonRestoredState`` will be set to ``false`` , even if it was previously set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html#cfn-kinesisanalyticsv2-application-flinkrunconfiguration-allownonrestoredstate
            '''
            result = self._values.get("allow_non_restored_state")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlinkRunConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"database_arn": "databaseArn"},
    )
    class GlueDataCatalogConfigurationProperty:
        def __init__(
            self,
            *,
            database_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of the Glue Data Catalog that you use for Apache Flink SQL queries and table API transforms that you write in an application.

            :param database_arn: The Amazon Resource Name (ARN) of the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                glue_data_catalog_configuration_property = kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty(
                    database_arn="databaseArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f97bbd7472996325553db625cc32496a2ee6e5ec82ceffb1176cf9629827a5d0)
                check_type(argname="argument database_arn", value=database_arn, expected_type=type_hints["database_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if database_arn is not None:
                self._values["database_arn"] = database_arn

        @builtins.property
        def database_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn
            '''
            result = self._values.get("database_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueDataCatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class InputLambdaProcessorProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''An object that contains the Amazon Resource Name (ARN) of the Amazon Lambda function that is used to preprocess records in the stream in a SQL-based Kinesis Data Analytics application.

            :param resource_arn: The ARN of the Amazon Lambda function that operates on records in the stream. .. epigraph:: To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                input_lambda_processor_property = kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa0dc913c642e0d7fdb4c27e14a3116ad2ac8761071d7a245fe0ede17c91958b)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the Amazon Lambda function that operates on records in the stream.

            .. epigraph::

               To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLambdaProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.InputParallelismProperty",
        jsii_struct_bases=[],
        name_mapping={"count": "count"},
    )
    class InputParallelismProperty:
        def __init__(self, *, count: typing.Optional[jsii.Number] = None) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the number of in-application streams to create for a given streaming source.

            :param count: The number of in-application streams to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                input_parallelism_property = kinesisanalyticsv2.CfnApplication.InputParallelismProperty(
                    count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05d05df1edf43f121cb6afde5c953f3321d0e9fed1f138c7d8ccb5b38c7f228c)
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''The number of in-application streams to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html#cfn-kinesisanalyticsv2-application-inputparallelism-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputParallelismProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"input_lambda_processor": "inputLambdaProcessor"},
    )
    class InputProcessingConfigurationProperty:
        def __init__(
            self,
            *,
            input_lambda_processor: typing.Optional[typing.Union[typing.Union["CfnApplication.InputLambdaProcessorProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''For an SQL-based Amazon Kinesis Data Analytics application, describes a processor that is used to preprocess the records in the stream before being processed by your application code.

            Currently, the only input processor available is `Amazon Lambda <https://docs.aws.amazon.com/lambda/>`_ .

            :param input_lambda_processor: The `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ that is used to preprocess the records in the stream before being processed by your application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                input_processing_configuration_property = kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty(
                    input_lambda_processor=kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                        resource_arn="resourceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e27e29aedd4e30be4ff1e97d0cdd36861d3ca026f17651c891cedae66abddc5c)
                check_type(argname="argument input_lambda_processor", value=input_lambda_processor, expected_type=type_hints["input_lambda_processor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if input_lambda_processor is not None:
                self._values["input_lambda_processor"] = input_lambda_processor

        @builtins.property
        def input_lambda_processor(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.InputLambdaProcessorProperty", _IResolvable_a771d0ef]]:
            '''The `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ that is used to preprocess the records in the stream before being processed by your application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor
            '''
            result = self._values.get("input_lambda_processor")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.InputLambdaProcessorProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProcessingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.InputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_schema": "inputSchema",
            "name_prefix": "namePrefix",
            "input_parallelism": "inputParallelism",
            "input_processing_configuration": "inputProcessingConfiguration",
            "kinesis_firehose_input": "kinesisFirehoseInput",
            "kinesis_streams_input": "kinesisStreamsInput",
        },
    )
    class InputProperty:
        def __init__(
            self,
            *,
            input_schema: typing.Union[typing.Union["CfnApplication.InputSchemaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            name_prefix: builtins.str,
            input_parallelism: typing.Optional[typing.Union[typing.Union["CfnApplication.InputParallelismProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            input_processing_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.InputProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            kinesis_firehose_input: typing.Optional[typing.Union[typing.Union["CfnApplication.KinesisFirehoseInputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            kinesis_streams_input: typing.Optional[typing.Union[typing.Union["CfnApplication.KinesisStreamsInputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''When you configure the application input for a SQL-based Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.

            :param input_schema: Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. Also used to describe the format of the reference data source.
            :param name_prefix: The name prefix to use when creating an in-application stream. Suppose that you specify a prefix " ``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with the names " ``MyInApplicationStream_001`` ," " ``MyInApplicationStream_002`` ," and so on.
            :param input_parallelism: Describes the number of in-application streams to create.
            :param input_processing_configuration: The `InputProcessingConfiguration <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputProcessingConfiguration.html>`_ for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ .
            :param kinesis_firehose_input: If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream's ARN.
            :param kinesis_streams_input: If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon Resource Name (ARN).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                input_property = kinesisanalyticsv2.CfnApplication.InputProperty(
                    input_schema=kinesisanalyticsv2.CfnApplication.InputSchemaProperty(
                        record_columns=[kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
                
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                            record_format_type="recordFormatType",
                
                            # the properties below are optional
                            mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
                
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                    name_prefix="namePrefix",
                
                    # the properties below are optional
                    input_parallelism=kinesisanalyticsv2.CfnApplication.InputParallelismProperty(
                        count=123
                    ),
                    input_processing_configuration=kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty(
                        input_lambda_processor=kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                            resource_arn="resourceArn"
                        )
                    ),
                    kinesis_firehose_input=kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty(
                        resource_arn="resourceArn"
                    ),
                    kinesis_streams_input=kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty(
                        resource_arn="resourceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40d29088a61dcb4e7cb40f424bfad67cc87998380931c0245cc65e8e61af5a16)
                check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
                check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
                check_type(argname="argument input_parallelism", value=input_parallelism, expected_type=type_hints["input_parallelism"])
                check_type(argname="argument input_processing_configuration", value=input_processing_configuration, expected_type=type_hints["input_processing_configuration"])
                check_type(argname="argument kinesis_firehose_input", value=kinesis_firehose_input, expected_type=type_hints["kinesis_firehose_input"])
                check_type(argname="argument kinesis_streams_input", value=kinesis_streams_input, expected_type=type_hints["kinesis_streams_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_schema": input_schema,
                "name_prefix": name_prefix,
            }
            if input_parallelism is not None:
                self._values["input_parallelism"] = input_parallelism
            if input_processing_configuration is not None:
                self._values["input_processing_configuration"] = input_processing_configuration
            if kinesis_firehose_input is not None:
                self._values["kinesis_firehose_input"] = kinesis_firehose_input
            if kinesis_streams_input is not None:
                self._values["kinesis_streams_input"] = kinesis_streams_input

        @builtins.property
        def input_schema(
            self,
        ) -> typing.Union["CfnApplication.InputSchemaProperty", _IResolvable_a771d0ef]:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

            Also used to describe the format of the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema
            '''
            result = self._values.get("input_schema")
            assert result is not None, "Required property 'input_schema' is missing"
            return typing.cast(typing.Union["CfnApplication.InputSchemaProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def name_prefix(self) -> builtins.str:
            '''The name prefix to use when creating an in-application stream.

            Suppose that you specify a prefix " ``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with the names " ``MyInApplicationStream_001`` ," " ``MyInApplicationStream_002`` ," and so on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix
            '''
            result = self._values.get("name_prefix")
            assert result is not None, "Required property 'name_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_parallelism(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.InputParallelismProperty", _IResolvable_a771d0ef]]:
            '''Describes the number of in-application streams to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism
            '''
            result = self._values.get("input_parallelism")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.InputParallelismProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def input_processing_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.InputProcessingConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The `InputProcessingConfiguration <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputProcessingConfiguration.html>`_ for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration
            '''
            result = self._values.get("input_processing_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.InputProcessingConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def kinesis_firehose_input(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.KinesisFirehoseInputProperty", _IResolvable_a771d0ef]]:
            '''If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream's ARN.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput
            '''
            result = self._values.get("kinesis_firehose_input")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.KinesisFirehoseInputProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def kinesis_streams_input(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.KinesisStreamsInputProperty", _IResolvable_a771d0ef]]:
            '''If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon Resource Name (ARN).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput
            '''
            result = self._values.get("kinesis_streams_input")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.KinesisStreamsInputProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.InputSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_columns": "recordColumns",
            "record_format": "recordFormat",
            "record_encoding": "recordEncoding",
        },
    )
    class InputSchemaProperty:
        def __init__(
            self,
            *,
            record_columns: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplication.RecordColumnProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
            record_format: typing.Union[typing.Union["CfnApplication.RecordFormatProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            record_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :param record_columns: A list of ``RecordColumn`` objects.
            :param record_format: Specifies the format of the records on the streaming source.
            :param record_encoding: Specifies the encoding of the records in the streaming source. For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                input_schema_property = kinesisanalyticsv2.CfnApplication.InputSchemaProperty(
                    record_columns=[kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
                
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                        record_format_type="recordFormatType",
                
                        # the properties below are optional
                        mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    record_encoding="recordEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07582f09ec12cbc76de59fd2c5e05fa6218ccbff367381671d9d6d4030c68100)
                check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
                check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
                check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_columns": record_columns,
                "record_format": record_format,
            }
            if record_encoding is not None:
                self._values["record_encoding"] = record_encoding

        @builtins.property
        def record_columns(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.RecordColumnProperty", _IResolvable_a771d0ef]]]:
            '''A list of ``RecordColumn`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns
            '''
            result = self._values.get("record_columns")
            assert result is not None, "Required property 'record_columns' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.RecordColumnProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def record_format(
            self,
        ) -> typing.Union["CfnApplication.RecordFormatProperty", _IResolvable_a771d0ef]:
            '''Specifies the format of the records on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat
            '''
            result = self._values.get("record_format")
            assert result is not None, "Required property 'record_format' is missing"
            return typing.cast(typing.Union["CfnApplication.RecordFormatProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def record_encoding(self) -> typing.Optional[builtins.str]:
            '''Specifies the encoding of the records in the streaming source.

            For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding
            '''
            result = self._values.get("record_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"record_row_path": "recordRowPath"},
    )
    class JSONMappingParametersProperty:
        def __init__(self, *, record_row_path: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when JSON is the record format on the streaming source.

            :param record_row_path: The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                j_sONMapping_parameters_property = kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                    record_row_path="recordRowPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eba0a5944e215305c2f0b5a2aa0b4cd079d74257bf71e104ca00aaab430cc273)
                check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_row_path": record_row_path,
            }

        @builtins.property
        def record_row_path(self) -> builtins.str:
            '''The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html#cfn-kinesisanalyticsv2-application-jsonmappingparameters-recordrowpath
            '''
            result = self._values.get("record_row_path")
            assert result is not None, "Required property 'record_row_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JSONMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisFirehoseInputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, identifies a Kinesis Data Firehose delivery stream as the streaming source.

            You provide the delivery stream's Amazon Resource Name (ARN).

            :param resource_arn: The Amazon Resource Name (ARN) of the delivery stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                kinesis_firehose_input_property = kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b08ef2e6b733956aa0067d4eac9e0d5b985c9e12f26717621bf4fc94f7046fa)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the delivery stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisStreamsInputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''Identifies a Kinesis data stream as the streaming source.

            You provide the stream's Amazon Resource Name (ARN).

            :param resource_arn: The ARN of the input Kinesis data stream to read.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                kinesis_streams_input_property = kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ba0dd16da39f3bcc9e9740ee7a5b2339ec88e7c4f0a5a0d7b6353293af76614)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the input Kinesis data stream to read.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html#cfn-kinesisanalyticsv2-application-kinesisstreamsinput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamsInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.MappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_mapping_parameters": "csvMappingParameters",
            "json_mapping_parameters": "jsonMappingParameters",
        },
    )
    class MappingParametersProperty:
        def __init__(
            self,
            *,
            csv_mapping_parameters: typing.Optional[typing.Union[typing.Union["CfnApplication.CSVMappingParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            json_mapping_parameters: typing.Optional[typing.Union[typing.Union["CfnApplication.JSONMappingParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :param csv_mapping_parameters: Provides additional mapping information when the record format uses delimiters (for example, CSV).
            :param json_mapping_parameters: Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                mapping_parameters_property = kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                    csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                        record_column_delimiter="recordColumnDelimiter",
                        record_row_delimiter="recordRowDelimiter"
                    ),
                    json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                        record_row_path="recordRowPath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8215b5c7883e182db6518989b0d53378e85928196ffe3588da4a2e7461e8cec0)
                check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
                check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_mapping_parameters is not None:
                self._values["csv_mapping_parameters"] = csv_mapping_parameters
            if json_mapping_parameters is not None:
                self._values["json_mapping_parameters"] = json_mapping_parameters

        @builtins.property
        def csv_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.CSVMappingParametersProperty", _IResolvable_a771d0ef]]:
            '''Provides additional mapping information when the record format uses delimiters (for example, CSV).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters
            '''
            result = self._values.get("csv_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.CSVMappingParametersProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def json_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.JSONMappingParametersProperty", _IResolvable_a771d0ef]]:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters
            '''
            result = self._values.get("json_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.JSONMappingParametersProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.MavenReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "artifact_id": "artifactId",
            "group_id": "groupId",
            "version": "version",
        },
    )
    class MavenReferenceProperty:
        def __init__(
            self,
            *,
            artifact_id: builtins.str,
            group_id: builtins.str,
            version: builtins.str,
        ) -> None:
            '''The information required to specify a Maven reference.

            You can use Maven references to specify dependency JAR files.

            :param artifact_id: The artifact ID of the Maven reference.
            :param group_id: The group ID of the Maven reference.
            :param version: The version of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                maven_reference_property = kinesisanalyticsv2.CfnApplication.MavenReferenceProperty(
                    artifact_id="artifactId",
                    group_id="groupId",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b33ab3b00534d95c05dae81dd5bbc5127193db0b389d399d946d04809da919ff)
                check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
                check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "artifact_id": artifact_id,
                "group_id": group_id,
                "version": version,
            }

        @builtins.property
        def artifact_id(self) -> builtins.str:
            '''The artifact ID of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-artifactid
            '''
            result = self._values.get("artifact_id")
            assert result is not None, "Required property 'artifact_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_id(self) -> builtins.str:
            '''The group ID of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-groupid
            '''
            result = self._values.get("group_id")
            assert result is not None, "Required property 'group_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''The version of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MavenReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_type": "configurationType",
            "log_level": "logLevel",
            "metrics_level": "metricsLevel",
        },
    )
    class MonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_type: builtins.str,
            log_level: typing.Optional[builtins.str] = None,
            metrics_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes configuration parameters for Amazon CloudWatch logging for a Java-based Kinesis Data Analytics application.

            For more information about CloudWatch logging, see `Monitoring <https://docs.aws.amazon.com/kinesisanalytics/latest/java/monitoring-overview>`_ .

            :param configuration_type: Describes whether to use the default CloudWatch logging configuration for an application. You must set this property to ``CUSTOM`` in order to set the ``LogLevel`` or ``MetricsLevel`` parameters.
            :param log_level: Describes the verbosity of the CloudWatch Logs for an application.
            :param metrics_level: Describes the granularity of the CloudWatch Logs for an application. The ``Parallelism`` level is not recommended for applications with a Parallelism over 64 due to excessive costs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                monitoring_configuration_property = kinesisanalyticsv2.CfnApplication.MonitoringConfigurationProperty(
                    configuration_type="configurationType",
                
                    # the properties below are optional
                    log_level="logLevel",
                    metrics_level="metricsLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e257771a336685becd71f4c3b56cab2ca4cf42092ed173e247a1bff8949de2c5)
                check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument metrics_level", value=metrics_level, expected_type=type_hints["metrics_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_type": configuration_type,
            }
            if log_level is not None:
                self._values["log_level"] = log_level
            if metrics_level is not None:
                self._values["metrics_level"] = metrics_level

        @builtins.property
        def configuration_type(self) -> builtins.str:
            '''Describes whether to use the default CloudWatch logging configuration for an application.

            You must set this property to ``CUSTOM`` in order to set the ``LogLevel`` or ``MetricsLevel`` parameters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-configurationtype
            '''
            result = self._values.get("configuration_type")
            assert result is not None, "Required property 'configuration_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''Describes the verbosity of the CloudWatch Logs for an application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metrics_level(self) -> typing.Optional[builtins.str]:
            '''Describes the granularity of the CloudWatch Logs for an application.

            The ``Parallelism`` level is not recommended for applications with a Parallelism over 64 due to excessive costs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-metricslevel
            '''
            result = self._values.get("metrics_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ParallelismConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_type": "configurationType",
            "auto_scaling_enabled": "autoScalingEnabled",
            "parallelism": "parallelism",
            "parallelism_per_kpu": "parallelismPerKpu",
        },
    )
    class ParallelismConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_type: builtins.str,
            auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            parallelism: typing.Optional[jsii.Number] = None,
            parallelism_per_kpu: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes parameters for how a Flink-based Kinesis Data Analytics application executes multiple tasks simultaneously.

            For more information about parallelism, see `Parallel Execution <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/parallel.html>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .

            :param configuration_type: Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. You must set this property to ``CUSTOM`` in order to change your application's ``AutoScalingEnabled`` , ``Parallelism`` , or ``ParallelismPerKPU`` properties.
            :param auto_scaling_enabled: Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
            :param parallelism: Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. The Kinesis Data Analytics service can increase this number automatically if `ParallelismConfiguration:AutoScalingEnabled <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_ParallelismConfiguration.html#kinesisanalytics-Type-ParallelismConfiguration-AutoScalingEnabled.html>`_ is set to ``true`` .
            :param parallelism_per_kpu: Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application. For more information about KPUs, see `Amazon Kinesis Data Analytics Pricing <https://docs.aws.amazon.com/kinesis/data-analytics/pricing/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                parallelism_configuration_property = kinesisanalyticsv2.CfnApplication.ParallelismConfigurationProperty(
                    configuration_type="configurationType",
                
                    # the properties below are optional
                    auto_scaling_enabled=False,
                    parallelism=123,
                    parallelism_per_kpu=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3679c096e66f08dbee6d0c1adedaace74f43467f8d943c41af773860c0c3642)
                check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
                check_type(argname="argument auto_scaling_enabled", value=auto_scaling_enabled, expected_type=type_hints["auto_scaling_enabled"])
                check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
                check_type(argname="argument parallelism_per_kpu", value=parallelism_per_kpu, expected_type=type_hints["parallelism_per_kpu"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_type": configuration_type,
            }
            if auto_scaling_enabled is not None:
                self._values["auto_scaling_enabled"] = auto_scaling_enabled
            if parallelism is not None:
                self._values["parallelism"] = parallelism
            if parallelism_per_kpu is not None:
                self._values["parallelism_per_kpu"] = parallelism_per_kpu

        @builtins.property
        def configuration_type(self) -> builtins.str:
            '''Describes whether the application uses the default parallelism for the Kinesis Data Analytics service.

            You must set this property to ``CUSTOM`` in order to change your application's ``AutoScalingEnabled`` , ``Parallelism`` , or ``ParallelismPerKPU`` properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-configurationtype
            '''
            result = self._values.get("configuration_type")
            assert result is not None, "Required property 'configuration_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_scaling_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-autoscalingenabled
            '''
            result = self._values.get("auto_scaling_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def parallelism(self) -> typing.Optional[jsii.Number]:
            '''Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform.

            The Kinesis Data Analytics service can increase this number automatically if `ParallelismConfiguration:AutoScalingEnabled <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_ParallelismConfiguration.html#kinesisanalytics-Type-ParallelismConfiguration-AutoScalingEnabled.html>`_ is set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelism
            '''
            result = self._values.get("parallelism")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallelism_per_kpu(self) -> typing.Optional[jsii.Number]:
            '''Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.

            For more information about KPUs, see `Amazon Kinesis Data Analytics Pricing <https://docs.aws.amazon.com/kinesis/data-analytics/pricing/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelismperkpu
            '''
            result = self._values.get("parallelism_per_kpu")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParallelismConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.PropertyGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_group_id": "propertyGroupId",
            "property_map": "propertyMap",
        },
    )
    class PropertyGroupProperty:
        def __init__(
            self,
            *,
            property_group_id: typing.Optional[builtins.str] = None,
            property_map: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Property key-value pairs passed into an application.

            :param property_group_id: Describes the key of an application execution property key-value pair.
            :param property_map: Describes the value of an application execution property key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                property_group_property = kinesisanalyticsv2.CfnApplication.PropertyGroupProperty(
                    property_group_id="propertyGroupId",
                    property_map={
                        "property_map_key": "propertyMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a86aa6ad12be17a993ab91b0ce275ac4f361e59a29c1d54591f300fdb8859fc9)
                check_type(argname="argument property_group_id", value=property_group_id, expected_type=type_hints["property_group_id"])
                check_type(argname="argument property_map", value=property_map, expected_type=type_hints["property_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if property_group_id is not None:
                self._values["property_group_id"] = property_group_id
            if property_map is not None:
                self._values["property_map"] = property_map

        @builtins.property
        def property_group_id(self) -> typing.Optional[builtins.str]:
            '''Describes the key of an application execution property key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid
            '''
            result = self._values.get("property_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
            '''Describes the value of an application execution property key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertymap
            '''
            result = self._values.get("property_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertyGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.RecordColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
    )
    class RecordColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sql_type: builtins.str,
            mapping: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

            Also used to describe the format of the reference data source.

            :param name: The name of the column that is created in the in-application input stream or reference table.
            :param sql_type: The type of column created in the in-application input stream or reference table.
            :param mapping: A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                record_column_property = kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                    name="name",
                    sql_type="sqlType",
                
                    # the properties below are optional
                    mapping="mapping"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b22aaeaca13d8c4a421431996bf70cd18f416137fb2396c699ec0645fd7b9302)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
                check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sql_type": sql_type,
            }
            if mapping is not None:
                self._values["mapping"] = mapping

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the column that is created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_type(self) -> builtins.str:
            '''The type of column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-sqltype
            '''
            result = self._values.get("sql_type")
            assert result is not None, "Required property 'sql_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping(self) -> typing.Optional[builtins.str]:
            '''A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-mapping
            '''
            result = self._values.get("mapping")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.RecordFormatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_format_type": "recordFormatType",
            "mapping_parameters": "mappingParameters",
        },
    )
    class RecordFormatProperty:
        def __init__(
            self,
            *,
            record_format_type: builtins.str,
            mapping_parameters: typing.Optional[typing.Union[typing.Union["CfnApplication.MappingParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

            :param record_format_type: The type of record format.
            :param mapping_parameters: When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                record_format_property = kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                    record_format_type="recordFormatType",
                
                    # the properties below are optional
                    mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                        csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                            record_column_delimiter="recordColumnDelimiter",
                            record_row_delimiter="recordRowDelimiter"
                        ),
                        json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                            record_row_path="recordRowPath"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d9cad5b7cd64bae3df4be2d3dc19b7dbe08cf10e1171d9ebf12b999cc3eb27f)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
                check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_format_type": record_format_type,
            }
            if mapping_parameters is not None:
                self._values["mapping_parameters"] = mapping_parameters

        @builtins.property
        def record_format_type(self) -> builtins.str:
            '''The type of record format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-recordformattype
            '''
            result = self._values.get("record_format_type")
            assert result is not None, "Required property 'record_format_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.MappingParametersProperty", _IResolvable_a771d0ef]]:
            '''When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters
            '''
            result = self._values.get("mapping_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.MappingParametersProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.RunConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_restore_configuration": "applicationRestoreConfiguration",
            "flink_run_configuration": "flinkRunConfiguration",
        },
    )
    class RunConfigurationProperty:
        def __init__(
            self,
            *,
            application_restore_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ApplicationRestoreConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            flink_run_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.FlinkRunConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes the starting parameters for an Kinesis Data Analytics application.

            :param application_restore_configuration: Describes the restore behavior of a restarting application.
            :param flink_run_configuration: Describes the starting parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                run_configuration_property = kinesisanalyticsv2.CfnApplication.RunConfigurationProperty(
                    application_restore_configuration=kinesisanalyticsv2.CfnApplication.ApplicationRestoreConfigurationProperty(
                        application_restore_type="applicationRestoreType",
                
                        # the properties below are optional
                        snapshot_name="snapshotName"
                    ),
                    flink_run_configuration=kinesisanalyticsv2.CfnApplication.FlinkRunConfigurationProperty(
                        allow_non_restored_state=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a42e0fac5c7628128bdc30f3c35565ca083169b903f655b3a6c22062157a384)
                check_type(argname="argument application_restore_configuration", value=application_restore_configuration, expected_type=type_hints["application_restore_configuration"])
                check_type(argname="argument flink_run_configuration", value=flink_run_configuration, expected_type=type_hints["flink_run_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_restore_configuration is not None:
                self._values["application_restore_configuration"] = application_restore_configuration
            if flink_run_configuration is not None:
                self._values["flink_run_configuration"] = flink_run_configuration

        @builtins.property
        def application_restore_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ApplicationRestoreConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Describes the restore behavior of a restarting application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html#cfn-kinesisanalyticsv2-application-runconfiguration-applicationrestoreconfiguration
            '''
            result = self._values.get("application_restore_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ApplicationRestoreConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def flink_run_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.FlinkRunConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Describes the starting parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html#cfn-kinesisanalyticsv2-application-runconfiguration-flinkrunconfiguration
            '''
            result = self._values.get("flink_run_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.FlinkRunConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_arn": "bucketArn", "base_path": "basePath"},
    )
    class S3ContentBaseLocationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            base_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The base location of the Amazon Data Analytics application.

            :param bucket_arn: The Amazon Resource Name (ARN) of the S3 bucket.
            :param base_path: The base path for the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                s3_content_base_location_property = kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty(
                    bucket_arn="bucketArn",
                
                    # the properties below are optional
                    base_path="basePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2da0d51202d0f062effcca96f9892423ca35b3273f5bce36b956e5f9bb6770d)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument base_path", value=base_path, expected_type=type_hints["base_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
            }
            if base_path is not None:
                self._values["base_path"] = base_path

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_path(self) -> typing.Optional[builtins.str]:
            '''The base path for the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath
            '''
            result = self._values.get("base_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ContentBaseLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "file_key": "fileKey",
            "object_version": "objectVersion",
        },
    )
    class S3ContentLocationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            file_key: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location of an application or a custom artifact.

            :param bucket_arn: The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
            :param file_key: The file key for the object containing the application code.
            :param object_version: The version of the object containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                s3_content_location_property = kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6321dd0fc53802294669175bc8428f6bc176c78816b4da0f776098b5ca4b7c9)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "file_key": file_key,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_key(self) -> builtins.str:
            '''The file key for the object containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-filekey
            '''
            result = self._values.get("file_key")
            assert result is not None, "Required property 'file_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The version of the object containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ContentLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.SqlApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"inputs": "inputs"},
    )
    class SqlApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            inputs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplication.InputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''Describes the inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.

            :param inputs: The array of `Input <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_Input.html>`_ objects describing the input streams used by the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                sql_application_configuration_property = kinesisanalyticsv2.CfnApplication.SqlApplicationConfigurationProperty(
                    inputs=[kinesisanalyticsv2.CfnApplication.InputProperty(
                        input_schema=kinesisanalyticsv2.CfnApplication.InputSchemaProperty(
                            record_columns=[kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                                name="name",
                                sql_type="sqlType",
                
                                # the properties below are optional
                                mapping="mapping"
                            )],
                            record_format=kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                                record_format_type="recordFormatType",
                
                                # the properties below are optional
                                mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                                    csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                                        record_column_delimiter="recordColumnDelimiter",
                                        record_row_delimiter="recordRowDelimiter"
                                    ),
                                    json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                                        record_row_path="recordRowPath"
                                    )
                                )
                            ),
                
                            # the properties below are optional
                            record_encoding="recordEncoding"
                        ),
                        name_prefix="namePrefix",
                
                        # the properties below are optional
                        input_parallelism=kinesisanalyticsv2.CfnApplication.InputParallelismProperty(
                            count=123
                        ),
                        input_processing_configuration=kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty(
                            input_lambda_processor=kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                                resource_arn="resourceArn"
                            )
                        ),
                        kinesis_firehose_input=kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty(
                            resource_arn="resourceArn"
                        ),
                        kinesis_streams_input=kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty(
                            resource_arn="resourceArn"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e38bfb8546822a60c3939bf4683ce4585642fd16375fad99cff06d75f5881fd0)
                check_type(argname="argument inputs", value=inputs, expected_type=type_hints["inputs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inputs is not None:
                self._values["inputs"] = inputs

        @builtins.property
        def inputs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.InputProperty", _IResolvable_a771d0ef]]]]:
            '''The array of `Input <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_Input.html>`_ objects describing the input streams used by the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs
            '''
            result = self._values.get("inputs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.InputProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''Describes the parameters of a VPC used by the application.

            :param security_group_ids: The array of `SecurityGroup <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html>`_ IDs used by the VPC configuration.
            :param subnet_ids: The array of `Subnet <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html>`_ IDs used by the VPC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                vpc_configuration_property = kinesisanalyticsv2.CfnApplication.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0641a9df6ea02dfd3cbc91ef2e9dc4840d1d28f5f6d1d5ec9bb19d063fcfb7f7)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The array of `SecurityGroup <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html>`_ IDs used by the VPC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html#cfn-kinesisanalyticsv2-application-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The array of `Subnet <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html>`_ IDs used by the VPC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html#cfn-kinesisanalyticsv2-application-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ZeppelinApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_configuration": "catalogConfiguration",
            "custom_artifacts_configuration": "customArtifactsConfiguration",
            "deploy_as_application_configuration": "deployAsApplicationConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
        },
    )
    class ZeppelinApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.CatalogConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            custom_artifacts_configuration: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplication.CustomArtifactConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
            deploy_as_application_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.DeployAsApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            monitoring_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ZeppelinMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The configuration of a Kinesis Data Analytics Studio notebook.

            :param catalog_configuration: The Amazon Glue Data Catalog that you use in queries in a Kinesis Data Analytics Studio notebook.
            :param custom_artifacts_configuration: A list of ``CustomArtifactConfiguration`` objects.
            :param deploy_as_application_configuration: The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.
            :param monitoring_configuration: The monitoring configuration of a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                zeppelin_application_configuration_property = kinesisanalyticsv2.CfnApplication.ZeppelinApplicationConfigurationProperty(
                    catalog_configuration=kinesisanalyticsv2.CfnApplication.CatalogConfigurationProperty(
                        glue_data_catalog_configuration=kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty(
                            database_arn="databaseArn"
                        )
                    ),
                    custom_artifacts_configuration=[kinesisanalyticsv2.CfnApplication.CustomArtifactConfigurationProperty(
                        artifact_type="artifactType",
                
                        # the properties below are optional
                        maven_reference=kinesisanalyticsv2.CfnApplication.MavenReferenceProperty(
                            artifact_id="artifactId",
                            group_id="groupId",
                            version="version"
                        ),
                        s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
                
                            # the properties below are optional
                            object_version="objectVersion"
                        )
                    )],
                    deploy_as_application_configuration=kinesisanalyticsv2.CfnApplication.DeployAsApplicationConfigurationProperty(
                        s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty(
                            bucket_arn="bucketArn",
                
                            # the properties below are optional
                            base_path="basePath"
                        )
                    ),
                    monitoring_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinMonitoringConfigurationProperty(
                        log_level="logLevel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9abd85eb978e76384e96ee4e723bb54178d27f84cb56d5dfa7b180d8a9d2687c)
                check_type(argname="argument catalog_configuration", value=catalog_configuration, expected_type=type_hints["catalog_configuration"])
                check_type(argname="argument custom_artifacts_configuration", value=custom_artifacts_configuration, expected_type=type_hints["custom_artifacts_configuration"])
                check_type(argname="argument deploy_as_application_configuration", value=deploy_as_application_configuration, expected_type=type_hints["deploy_as_application_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_configuration is not None:
                self._values["catalog_configuration"] = catalog_configuration
            if custom_artifacts_configuration is not None:
                self._values["custom_artifacts_configuration"] = custom_artifacts_configuration
            if deploy_as_application_configuration is not None:
                self._values["deploy_as_application_configuration"] = deploy_as_application_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration

        @builtins.property
        def catalog_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.CatalogConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The Amazon Glue Data Catalog that you use in queries in a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration
            '''
            result = self._values.get("catalog_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.CatalogConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def custom_artifacts_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.CustomArtifactConfigurationProperty", _IResolvable_a771d0ef]]]]:
            '''A list of ``CustomArtifactConfiguration`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration
            '''
            result = self._values.get("custom_artifacts_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.CustomArtifactConfigurationProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def deploy_as_application_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.DeployAsApplicationConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration
            '''
            result = self._values.get("deploy_as_application_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.DeployAsApplicationConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ZeppelinMonitoringConfigurationProperty", _IResolvable_a771d0ef]]:
            '''The monitoring configuration of a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ZeppelinMonitoringConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZeppelinApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplication.ZeppelinMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_level": "logLevel"},
    )
    class ZeppelinMonitoringConfigurationProperty:
        def __init__(self, *, log_level: typing.Optional[builtins.str] = None) -> None:
            '''Describes configuration parameters for Amazon CloudWatch logging for a Kinesis Data Analytics Studio notebook.

            For more information about CloudWatch logging, see `Monitoring <https://docs.aws.amazon.com/kinesisanalytics/latest/java/monitoring-overview.html>`_ .

            :param log_level: The verbosity of the CloudWatch Logs for an application. You can set it to ``INFO`` , ``WARN`` , ``ERROR`` , or ``DEBUG`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                zeppelin_monitoring_configuration_property = kinesisanalyticsv2.CfnApplication.ZeppelinMonitoringConfigurationProperty(
                    log_level="logLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a921d2594e7d83ab1caf34ab022271dc283f0c4c7adbb187986ad5aa82e1092)
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_level is not None:
                self._values["log_level"] = log_level

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''The verbosity of the CloudWatch Logs for an application.

            You can set it to ``INFO`` , ``WARN`` , ``ERROR`` , or ``DEBUG`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZeppelinMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnApplicationCloudWatchLoggingOption(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

    Adds an Amazon CloudWatch log stream to monitor application configuration errors.
    .. epigraph::

       Only one *ApplicationCloudWatchLoggingOption* resource can be attached per application.

    :cloudformationResource: AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
        
        cfn_application_cloud_watch_logging_option = kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption(self, "MyCfnApplicationCloudWatchLoggingOption",
            application_name="applicationName",
            cloud_watch_logging_option=kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty(
                log_stream_arn="logStreamArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        application_name: builtins.str,
        cloud_watch_logging_option: typing.Union[typing.Union["CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: The name of the application.
        :param cloud_watch_logging_option: Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66c427154899af9803115aa7b67044500e370aa5c3d23d2fb565dfc44df56b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationCloudWatchLoggingOptionProps(
            application_name=application_name,
            cloud_watch_logging_option=cloud_watch_logging_option,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a849bf42636f2b1c8e6e98a8264331e330d259a43059e6a3bac9c3f1b4c731f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c438ebfbbd2ccbadfc14057a7b12f05f31f056fe7b3501eeb205b21e0b3a710f)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9a8e120c57ca619dd0c44757426e8a365050f5f3b801fa4790b06194ff2805c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLoggingOption")
    def cloud_watch_logging_option(
        self,
    ) -> typing.Union["CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty", _IResolvable_a771d0ef]:
        '''Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
        '''
        return typing.cast(typing.Union["CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty", _IResolvable_a771d0ef], jsii.get(self, "cloudWatchLoggingOption"))

    @cloud_watch_logging_option.setter
    def cloud_watch_logging_option(
        self,
        value: typing.Union["CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc63f6963b1507360f0f71666b5373d08899f4cf560596cdb776c8232a7a18c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLoggingOption", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"log_stream_arn": "logStreamArn"},
    )
    class CloudWatchLoggingOptionProperty:
        def __init__(self, *, log_stream_arn: builtins.str) -> None:
            '''Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

            :param log_stream_arn: The ARN of the CloudWatch log to receive application messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                cloud_watch_logging_option_property = kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty(
                    log_stream_arn="logStreamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0860029a68d5a969b1530e03eddfafe354c343e8665a07aeadd64d203729308d)
                check_type(argname="argument log_stream_arn", value=log_stream_arn, expected_type=type_hints["log_stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_stream_arn": log_stream_arn,
            }

        @builtins.property
        def log_stream_arn(self) -> builtins.str:
            '''The ARN of the CloudWatch log to receive application messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn
            '''
            result = self._values.get("log_stream_arn")
            assert result is not None, "Required property 'log_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLoggingOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "cloud_watch_logging_option": "cloudWatchLoggingOption",
    },
)
class CfnApplicationCloudWatchLoggingOptionProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        cloud_watch_logging_option: typing.Union[typing.Union[CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Properties for defining a ``CfnApplicationCloudWatchLoggingOption``.

        :param application_name: The name of the application.
        :param cloud_watch_logging_option: Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
            
            cfn_application_cloud_watch_logging_option_props = kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOptionProps(
                application_name="applicationName",
                cloud_watch_logging_option=kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty(
                    log_stream_arn="logStreamArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088a026a61075834276214d56567cb73f83ba68c0b84507b923e6fe7f2afc509)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument cloud_watch_logging_option", value=cloud_watch_logging_option, expected_type=type_hints["cloud_watch_logging_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "cloud_watch_logging_option": cloud_watch_logging_option,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_watch_logging_option(
        self,
    ) -> typing.Union[CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty, _IResolvable_a771d0ef]:
        '''Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
        '''
        result = self._values.get("cloud_watch_logging_option")
        assert result is not None, "Required property 'cloud_watch_logging_option' is missing"
        return typing.cast(typing.Union[CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty, _IResolvable_a771d0ef], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationCloudWatchLoggingOptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnApplicationOutput(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutput",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

    Adds an external destination to your SQL-based Amazon Kinesis Data Analytics application.

    If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.

    You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors.

    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the `DescribeApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_DescribeApplication.html>`_ operation to find the current application version.
    .. epigraph::

       Creation of multiple outputs should be sequential (use of DependsOn) to avoid a problem with a stale application version ( *ConcurrentModificationException* ).

    :cloudformationResource: AWS::KinesisAnalyticsV2::ApplicationOutput
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
        
        cfn_application_output = kinesisanalyticsv2.CfnApplicationOutput(self, "MyCfnApplicationOutput",
            application_name="applicationName",
            output=kinesisanalyticsv2.CfnApplicationOutput.OutputProperty(
                destination_schema=kinesisanalyticsv2.CfnApplicationOutput.DestinationSchemaProperty(
                    record_format_type="recordFormatType"
                ),
        
                # the properties below are optional
                kinesis_firehose_output=kinesisanalyticsv2.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                    resource_arn="resourceArn"
                ),
                kinesis_streams_output=kinesisanalyticsv2.CfnApplicationOutput.KinesisStreamsOutputProperty(
                    resource_arn="resourceArn"
                ),
                lambda_output=kinesisanalyticsv2.CfnApplicationOutput.LambdaOutputProperty(
                    resource_arn="resourceArn"
                ),
                name="name"
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        application_name: builtins.str,
        output: typing.Union[typing.Union["CfnApplicationOutput.OutputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: The name of the application.
        :param output: Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b349088222421e3c50e6e5c907b5849a2724995d71d433a04e0c6cf60bfb0b81)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationOutputProps(
            application_name=application_name, output=output
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b45c7707450f48e64bf550749124d935e40d67395840ea88b5871e245c581ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__67311b2235be7d3e320c535379c43d2ea791808f49da523fa7cb73b4d820815a)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f4e50f771f1193f875fdab3ceb20f8e7cde0bd1b541d63a018c3b38f5364d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(
        self,
    ) -> typing.Union["CfnApplicationOutput.OutputProperty", _IResolvable_a771d0ef]:
        '''Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

        The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
        '''
        return typing.cast(typing.Union["CfnApplicationOutput.OutputProperty", _IResolvable_a771d0ef], jsii.get(self, "output"))

    @output.setter
    def output(
        self,
        value: typing.Union["CfnApplicationOutput.OutputProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4facdb2b648238b2f495d81f71664370f6b515061c3f0e0c09e8140ba02bf99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "output", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutput.DestinationSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"record_format_type": "recordFormatType"},
    )
    class DestinationSchemaProperty:
        def __init__(
            self,
            *,
            record_format_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the data format when records are written to the destination in a SQL-based Kinesis Data Analytics application.

            :param record_format_type: Specifies the format of the records on the output stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                destination_schema_property = kinesisanalyticsv2.CfnApplicationOutput.DestinationSchemaProperty(
                    record_format_type="recordFormatType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc8785b6cda6486c803af7fba6996a2eefd9790b7ab489491d5ee93f29534f72)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if record_format_type is not None:
                self._values["record_format_type"] = record_format_type

        @builtins.property
        def record_format_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the format of the records on the output stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html#cfn-kinesisanalyticsv2-applicationoutput-destinationschema-recordformattype
            '''
            result = self._values.get("record_format_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutput.KinesisFirehoseOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisFirehoseOutputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, when configuring application output, identifies a Kinesis Data Firehose delivery stream as the destination.

            You provide the stream Amazon Resource Name (ARN) of the delivery stream.

            :param resource_arn: The ARN of the destination delivery stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                kinesis_firehose_output_property = kinesisanalyticsv2.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bc938ab4e3df1578b2a3902504b29e1c4c95f52764b5fd69b1156abdf98a0bc)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the destination delivery stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutput.KinesisStreamsOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisStreamsOutputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's output, identifies a Kinesis data stream as the destination.

            You provide the stream Amazon Resource Name (ARN).

            :param resource_arn: The ARN of the destination Kinesis data stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                kinesis_streams_output_property = kinesisanalyticsv2.CfnApplicationOutput.KinesisStreamsOutputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db0a116ad42f8729047d93a312b247dc295c41473f9de5764eeb6d38d1832765)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the destination Kinesis data stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamsOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutput.LambdaOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class LambdaOutputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's output, identifies an Amazon Lambda function as the destination.

            You provide the function Amazon Resource Name (ARN) of the Lambda function.

            :param resource_arn: The Amazon Resource Name (ARN) of the destination Lambda function to write to. .. epigraph:: To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                lambda_output_property = kinesisanalyticsv2.CfnApplicationOutput.LambdaOutputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__939acc597225a110aab8861676e18abcd08ef77273acb1daf6f4a5b60c872b77)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the destination Lambda function to write to.

            .. epigraph::

               To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html#cfn-kinesisanalyticsv2-applicationoutput-lambdaoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutput.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_schema": "destinationSchema",
            "kinesis_firehose_output": "kinesisFirehoseOutput",
            "kinesis_streams_output": "kinesisStreamsOutput",
            "lambda_output": "lambdaOutput",
            "name": "name",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            destination_schema: typing.Union[typing.Union["CfnApplicationOutput.DestinationSchemaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            kinesis_firehose_output: typing.Optional[typing.Union[typing.Union["CfnApplicationOutput.KinesisFirehoseOutputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            kinesis_streams_output: typing.Optional[typing.Union[typing.Union["CfnApplicationOutput.KinesisStreamsOutputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            lambda_output: typing.Optional[typing.Union[typing.Union["CfnApplicationOutput.LambdaOutputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

            The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

            :param destination_schema: Describes the data format when records are written to the destination.
            :param kinesis_firehose_output: Identifies a Kinesis Data Firehose delivery stream as the destination.
            :param kinesis_streams_output: Identifies a Kinesis data stream as the destination.
            :param lambda_output: Identifies an Amazon Lambda function as the destination.
            :param name: The name of the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                output_property = kinesisanalyticsv2.CfnApplicationOutput.OutputProperty(
                    destination_schema=kinesisanalyticsv2.CfnApplicationOutput.DestinationSchemaProperty(
                        record_format_type="recordFormatType"
                    ),
                
                    # the properties below are optional
                    kinesis_firehose_output=kinesisanalyticsv2.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    kinesis_streams_output=kinesisanalyticsv2.CfnApplicationOutput.KinesisStreamsOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    lambda_output=kinesisanalyticsv2.CfnApplicationOutput.LambdaOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ea6bc770388499b050e422780c4626409280ae8780c26fe7aa12bd8a36f1807)
                check_type(argname="argument destination_schema", value=destination_schema, expected_type=type_hints["destination_schema"])
                check_type(argname="argument kinesis_firehose_output", value=kinesis_firehose_output, expected_type=type_hints["kinesis_firehose_output"])
                check_type(argname="argument kinesis_streams_output", value=kinesis_streams_output, expected_type=type_hints["kinesis_streams_output"])
                check_type(argname="argument lambda_output", value=lambda_output, expected_type=type_hints["lambda_output"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_schema": destination_schema,
            }
            if kinesis_firehose_output is not None:
                self._values["kinesis_firehose_output"] = kinesis_firehose_output
            if kinesis_streams_output is not None:
                self._values["kinesis_streams_output"] = kinesis_streams_output
            if lambda_output is not None:
                self._values["lambda_output"] = lambda_output
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def destination_schema(
            self,
        ) -> typing.Union["CfnApplicationOutput.DestinationSchemaProperty", _IResolvable_a771d0ef]:
            '''Describes the data format when records are written to the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema
            '''
            result = self._values.get("destination_schema")
            assert result is not None, "Required property 'destination_schema' is missing"
            return typing.cast(typing.Union["CfnApplicationOutput.DestinationSchemaProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def kinesis_firehose_output(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationOutput.KinesisFirehoseOutputProperty", _IResolvable_a771d0ef]]:
            '''Identifies a Kinesis Data Firehose delivery stream as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput
            '''
            result = self._values.get("kinesis_firehose_output")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationOutput.KinesisFirehoseOutputProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def kinesis_streams_output(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationOutput.KinesisStreamsOutputProperty", _IResolvable_a771d0ef]]:
            '''Identifies a Kinesis data stream as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput
            '''
            result = self._values.get("kinesis_streams_output")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationOutput.KinesisStreamsOutputProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def lambda_output(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationOutput.LambdaOutputProperty", _IResolvable_a771d0ef]]:
            '''Identifies an Amazon Lambda function as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-lambdaoutput
            '''
            result = self._values.get("lambda_output")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationOutput.LambdaOutputProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationOutputProps",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName", "output": "output"},
)
class CfnApplicationOutputProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        output: typing.Union[typing.Union[CfnApplicationOutput.OutputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Properties for defining a ``CfnApplicationOutput``.

        :param application_name: The name of the application.
        :param output: Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
            
            cfn_application_output_props = kinesisanalyticsv2.CfnApplicationOutputProps(
                application_name="applicationName",
                output=kinesisanalyticsv2.CfnApplicationOutput.OutputProperty(
                    destination_schema=kinesisanalyticsv2.CfnApplicationOutput.DestinationSchemaProperty(
                        record_format_type="recordFormatType"
                    ),
            
                    # the properties below are optional
                    kinesis_firehose_output=kinesisanalyticsv2.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    kinesis_streams_output=kinesisanalyticsv2.CfnApplicationOutput.KinesisStreamsOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    lambda_output=kinesisanalyticsv2.CfnApplicationOutput.LambdaOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    name="name"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32968bd6091e478dd2b78f10321b0677a621a2ee9edceeb1ea063139b1f152d9)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "output": output,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output(
        self,
    ) -> typing.Union[CfnApplicationOutput.OutputProperty, _IResolvable_a771d0ef]:
        '''Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

        The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
        '''
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(typing.Union[CfnApplicationOutput.OutputProperty, _IResolvable_a771d0ef], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "runtime_environment": "runtimeEnvironment",
        "service_execution_role": "serviceExecutionRole",
        "application_configuration": "applicationConfiguration",
        "application_description": "applicationDescription",
        "application_maintenance_configuration": "applicationMaintenanceConfiguration",
        "application_mode": "applicationMode",
        "application_name": "applicationName",
        "run_configuration": "runConfiguration",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        runtime_environment: builtins.str,
        service_execution_role: builtins.str,
        application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        application_description: typing.Optional[builtins.str] = None,
        application_maintenance_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        application_mode: typing.Optional[builtins.str] = None,
        application_name: typing.Optional[builtins.str] = None,
        run_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.RunConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param runtime_environment: The runtime environment for the application.
        :param service_execution_role: Specifies the IAM role that the application uses to access external resources.
        :param application_configuration: Use this parameter to configure the application.
        :param application_description: The description of the application.
        :param application_maintenance_configuration: ``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.
        :param application_mode: To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` . However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.
        :param application_name: The name of the application.
        :param run_configuration: ``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.
        :param tags: A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
            
            cfn_application_props = kinesisanalyticsv2.CfnApplicationProps(
                runtime_environment="runtimeEnvironment",
                service_execution_role="serviceExecutionRole",
            
                # the properties below are optional
                application_configuration=kinesisanalyticsv2.CfnApplication.ApplicationConfigurationProperty(
                    application_code_configuration=kinesisanalyticsv2.CfnApplication.ApplicationCodeConfigurationProperty(
                        code_content=kinesisanalyticsv2.CfnApplication.CodeContentProperty(
                            s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
            
                                # the properties below are optional
                                object_version="objectVersion"
                            ),
                            text_content="textContent",
                            zip_file_content="zipFileContent"
                        ),
                        code_content_type="codeContentType"
                    ),
                    application_snapshot_configuration=kinesisanalyticsv2.CfnApplication.ApplicationSnapshotConfigurationProperty(
                        snapshots_enabled=False
                    ),
                    environment_properties=kinesisanalyticsv2.CfnApplication.EnvironmentPropertiesProperty(
                        property_groups=[kinesisanalyticsv2.CfnApplication.PropertyGroupProperty(
                            property_group_id="propertyGroupId",
                            property_map={
                                "property_map_key": "propertyMap"
                            }
                        )]
                    ),
                    flink_application_configuration=kinesisanalyticsv2.CfnApplication.FlinkApplicationConfigurationProperty(
                        checkpoint_configuration=kinesisanalyticsv2.CfnApplication.CheckpointConfigurationProperty(
                            configuration_type="configurationType",
            
                            # the properties below are optional
                            checkpointing_enabled=False,
                            checkpoint_interval=123,
                            min_pause_between_checkpoints=123
                        ),
                        monitoring_configuration=kinesisanalyticsv2.CfnApplication.MonitoringConfigurationProperty(
                            configuration_type="configurationType",
            
                            # the properties below are optional
                            log_level="logLevel",
                            metrics_level="metricsLevel"
                        ),
                        parallelism_configuration=kinesisanalyticsv2.CfnApplication.ParallelismConfigurationProperty(
                            configuration_type="configurationType",
            
                            # the properties below are optional
                            auto_scaling_enabled=False,
                            parallelism=123,
                            parallelism_per_kpu=123
                        )
                    ),
                    sql_application_configuration=kinesisanalyticsv2.CfnApplication.SqlApplicationConfigurationProperty(
                        inputs=[kinesisanalyticsv2.CfnApplication.InputProperty(
                            input_schema=kinesisanalyticsv2.CfnApplication.InputSchemaProperty(
                                record_columns=[kinesisanalyticsv2.CfnApplication.RecordColumnProperty(
                                    name="name",
                                    sql_type="sqlType",
            
                                    # the properties below are optional
                                    mapping="mapping"
                                )],
                                record_format=kinesisanalyticsv2.CfnApplication.RecordFormatProperty(
                                    record_format_type="recordFormatType",
            
                                    # the properties below are optional
                                    mapping_parameters=kinesisanalyticsv2.CfnApplication.MappingParametersProperty(
                                        csv_mapping_parameters=kinesisanalyticsv2.CfnApplication.CSVMappingParametersProperty(
                                            record_column_delimiter="recordColumnDelimiter",
                                            record_row_delimiter="recordRowDelimiter"
                                        ),
                                        json_mapping_parameters=kinesisanalyticsv2.CfnApplication.JSONMappingParametersProperty(
                                            record_row_path="recordRowPath"
                                        )
                                    )
                                ),
            
                                # the properties below are optional
                                record_encoding="recordEncoding"
                            ),
                            name_prefix="namePrefix",
            
                            # the properties below are optional
                            input_parallelism=kinesisanalyticsv2.CfnApplication.InputParallelismProperty(
                                count=123
                            ),
                            input_processing_configuration=kinesisanalyticsv2.CfnApplication.InputProcessingConfigurationProperty(
                                input_lambda_processor=kinesisanalyticsv2.CfnApplication.InputLambdaProcessorProperty(
                                    resource_arn="resourceArn"
                                )
                            ),
                            kinesis_firehose_input=kinesisanalyticsv2.CfnApplication.KinesisFirehoseInputProperty(
                                resource_arn="resourceArn"
                            ),
                            kinesis_streams_input=kinesisanalyticsv2.CfnApplication.KinesisStreamsInputProperty(
                                resource_arn="resourceArn"
                            )
                        )]
                    ),
                    vpc_configurations=[kinesisanalyticsv2.CfnApplication.VpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )],
                    zeppelin_application_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinApplicationConfigurationProperty(
                        catalog_configuration=kinesisanalyticsv2.CfnApplication.CatalogConfigurationProperty(
                            glue_data_catalog_configuration=kinesisanalyticsv2.CfnApplication.GlueDataCatalogConfigurationProperty(
                                database_arn="databaseArn"
                            )
                        ),
                        custom_artifacts_configuration=[kinesisanalyticsv2.CfnApplication.CustomArtifactConfigurationProperty(
                            artifact_type="artifactType",
            
                            # the properties below are optional
                            maven_reference=kinesisanalyticsv2.CfnApplication.MavenReferenceProperty(
                                artifact_id="artifactId",
                                group_id="groupId",
                                version="version"
                            ),
                            s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
            
                                # the properties below are optional
                                object_version="objectVersion"
                            )
                        )],
                        deploy_as_application_configuration=kinesisanalyticsv2.CfnApplication.DeployAsApplicationConfigurationProperty(
                            s3_content_location=kinesisanalyticsv2.CfnApplication.S3ContentBaseLocationProperty(
                                bucket_arn="bucketArn",
            
                                # the properties below are optional
                                base_path="basePath"
                            )
                        ),
                        monitoring_configuration=kinesisanalyticsv2.CfnApplication.ZeppelinMonitoringConfigurationProperty(
                            log_level="logLevel"
                        )
                    )
                ),
                application_description="applicationDescription",
                application_maintenance_configuration=kinesisanalyticsv2.CfnApplication.ApplicationMaintenanceConfigurationProperty(
                    application_maintenance_window_start_time="applicationMaintenanceWindowStartTime"
                ),
                application_mode="applicationMode",
                application_name="applicationName",
                run_configuration=kinesisanalyticsv2.CfnApplication.RunConfigurationProperty(
                    application_restore_configuration=kinesisanalyticsv2.CfnApplication.ApplicationRestoreConfigurationProperty(
                        application_restore_type="applicationRestoreType",
            
                        # the properties below are optional
                        snapshot_name="snapshotName"
                    ),
                    flink_run_configuration=kinesisanalyticsv2.CfnApplication.FlinkRunConfigurationProperty(
                        allow_non_restored_state=False
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39db75c89149de5863b2d649418dc3661b84e8793445aa4d71e2384c22fc6404)
            check_type(argname="argument runtime_environment", value=runtime_environment, expected_type=type_hints["runtime_environment"])
            check_type(argname="argument service_execution_role", value=service_execution_role, expected_type=type_hints["service_execution_role"])
            check_type(argname="argument application_configuration", value=application_configuration, expected_type=type_hints["application_configuration"])
            check_type(argname="argument application_description", value=application_description, expected_type=type_hints["application_description"])
            check_type(argname="argument application_maintenance_configuration", value=application_maintenance_configuration, expected_type=type_hints["application_maintenance_configuration"])
            check_type(argname="argument application_mode", value=application_mode, expected_type=type_hints["application_mode"])
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument run_configuration", value=run_configuration, expected_type=type_hints["run_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "runtime_environment": runtime_environment,
            "service_execution_role": service_execution_role,
        }
        if application_configuration is not None:
            self._values["application_configuration"] = application_configuration
        if application_description is not None:
            self._values["application_description"] = application_description
        if application_maintenance_configuration is not None:
            self._values["application_maintenance_configuration"] = application_maintenance_configuration
        if application_mode is not None:
            self._values["application_mode"] = application_mode
        if application_name is not None:
            self._values["application_name"] = application_name
        if run_configuration is not None:
            self._values["run_configuration"] = run_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def runtime_environment(self) -> builtins.str:
        '''The runtime environment for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
        '''
        result = self._values.get("runtime_environment")
        assert result is not None, "Required property 'runtime_environment' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_execution_role(self) -> builtins.str:
        '''Specifies the IAM role that the application uses to access external resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
        '''
        result = self._values.get("service_execution_role")
        assert result is not None, "Required property 'service_execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.ApplicationConfigurationProperty, _IResolvable_a771d0ef]]:
        '''Use this parameter to configure the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
        '''
        result = self._values.get("application_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.ApplicationConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def application_description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
        '''
        result = self._values.get("application_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.ApplicationMaintenanceConfigurationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration
        '''
        result = self._values.get("application_maintenance_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.ApplicationMaintenanceConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def application_mode(self) -> typing.Optional[builtins.str]:
        '''To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` .

        However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode
        '''
        result = self._values.get("application_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.RunConfigurationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runconfiguration
        '''
        result = self._values.get("run_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.RunConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''A list of one or more tags to assign to the application.

        A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnApplicationReferenceDataSource(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

    Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.

    Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.

    :cloudformationResource: AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
        
        cfn_application_reference_data_source = kinesisanalyticsv2.CfnApplicationReferenceDataSource(self, "MyCfnApplicationReferenceDataSource",
            application_name="applicationName",
            reference_data_source=kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty(
                reference_schema=kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                    record_columns=[kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
        
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordFormatProperty(
                        record_format_type="recordFormatType",
        
                        # the properties below are optional
                        mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
        
                    # the properties below are optional
                    record_encoding="recordEncoding"
                ),
        
                # the properties below are optional
                s3_reference_data_source=kinesisanalyticsv2.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey"
                ),
                table_name="tableName"
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        application_name: builtins.str,
        reference_data_source: typing.Union[typing.Union["CfnApplicationReferenceDataSource.ReferenceDataSourceProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: The name of the application.
        :param reference_data_source: For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25610c135bf208b232f6545a5c4093e4ca2c12c2871ea1a8d87e9912c41c8f53)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationReferenceDataSourceProps(
            application_name=application_name,
            reference_data_source=reference_data_source,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356a199f3a0010617f6aafe57e8451311e0ac55941fd9035c96d3c419795c96e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0539ad95d248380df273f7fa43b7b1c2da39b3c46baa2125d1f801c48f89af0b)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72732ae0525d29dd775d8095afffde56e03c0928af738b1c665a45352f6b3ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="referenceDataSource")
    def reference_data_source(
        self,
    ) -> typing.Union["CfnApplicationReferenceDataSource.ReferenceDataSourceProperty", _IResolvable_a771d0ef]:
        '''For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
        '''
        return typing.cast(typing.Union["CfnApplicationReferenceDataSource.ReferenceDataSourceProperty", _IResolvable_a771d0ef], jsii.get(self, "referenceDataSource"))

    @reference_data_source.setter
    def reference_data_source(
        self,
        value: typing.Union["CfnApplicationReferenceDataSource.ReferenceDataSourceProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7debe0e1784a621fbff07ba1518272c0c6e8d98736201fadf1b4f9094fd58515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referenceDataSource", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_column_delimiter": "recordColumnDelimiter",
            "record_row_delimiter": "recordRowDelimiter",
        },
    )
    class CSVMappingParametersProperty:
        def __init__(
            self,
            *,
            record_column_delimiter: builtins.str,
            record_row_delimiter: builtins.str,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV.

            For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

            ``"name1", "address1"``

            ``"name2", "address2"``

            :param record_column_delimiter: The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
            :param record_row_delimiter: The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                c_sVMapping_parameters_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                    record_column_delimiter="recordColumnDelimiter",
                    record_row_delimiter="recordRowDelimiter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d632f1cc043e69b3c6395c7f040b5572b52cab2830faa81bb1f9ce9b287ac5c7)
                check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
                check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_column_delimiter": record_column_delimiter,
                "record_row_delimiter": record_row_delimiter,
            }

        @builtins.property
        def record_column_delimiter(self) -> builtins.str:
            '''The column delimiter.

            For example, in a CSV format, a comma (",") is the typical column delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
            '''
            result = self._values.get("record_column_delimiter")
            assert result is not None, "Required property 'record_column_delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_row_delimiter(self) -> builtins.str:
            '''The row delimiter.

            For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
            '''
            result = self._values.get("record_row_delimiter")
            assert result is not None, "Required property 'record_row_delimiter' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CSVMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"record_row_path": "recordRowPath"},
    )
    class JSONMappingParametersProperty:
        def __init__(self, *, record_row_path: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when JSON is the record format on the streaming source.

            :param record_row_path: The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                j_sONMapping_parameters_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                    record_row_path="recordRowPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b573a01e361030c64e926fa5f1401124f594e0979e9580236bffff3be848ee9)
                check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_row_path": record_row_path,
            }

        @builtins.property
        def record_row_path(self) -> builtins.str:
            '''The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath
            '''
            result = self._values.get("record_row_path")
            assert result is not None, "Required property 'record_row_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JSONMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_mapping_parameters": "csvMappingParameters",
            "json_mapping_parameters": "jsonMappingParameters",
        },
    )
    class MappingParametersProperty:
        def __init__(
            self,
            *,
            csv_mapping_parameters: typing.Optional[typing.Union[typing.Union["CfnApplicationReferenceDataSource.CSVMappingParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            json_mapping_parameters: typing.Optional[typing.Union[typing.Union["CfnApplicationReferenceDataSource.JSONMappingParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :param csv_mapping_parameters: Provides additional mapping information when the record format uses delimiters (for example, CSV).
            :param json_mapping_parameters: Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                mapping_parameters_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty(
                    csv_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                        record_column_delimiter="recordColumnDelimiter",
                        record_row_delimiter="recordRowDelimiter"
                    ),
                    json_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                        record_row_path="recordRowPath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01c944f769f2c0a1a9f39f3fef36fa8b8871bf4782112eacda97f3779ef05828)
                check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
                check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_mapping_parameters is not None:
                self._values["csv_mapping_parameters"] = csv_mapping_parameters
            if json_mapping_parameters is not None:
                self._values["json_mapping_parameters"] = json_mapping_parameters

        @builtins.property
        def csv_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationReferenceDataSource.CSVMappingParametersProperty", _IResolvable_a771d0ef]]:
            '''Provides additional mapping information when the record format uses delimiters (for example, CSV).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters
            '''
            result = self._values.get("csv_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationReferenceDataSource.CSVMappingParametersProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def json_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationReferenceDataSource.JSONMappingParametersProperty", _IResolvable_a771d0ef]]:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters
            '''
            result = self._values.get("json_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationReferenceDataSource.JSONMappingParametersProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
    )
    class RecordColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sql_type: builtins.str,
            mapping: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

            Also used to describe the format of the reference data source.

            :param name: The name of the column that is created in the in-application input stream or reference table.
            :param sql_type: The type of column created in the in-application input stream or reference table.
            :param mapping: A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                record_column_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordColumnProperty(
                    name="name",
                    sql_type="sqlType",
                
                    # the properties below are optional
                    mapping="mapping"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__72e467e0d96c4b4d68162b27ed41290bf4d452f0fe8efd3f93b09971abfa2fc5)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
                check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sql_type": sql_type,
            }
            if mapping is not None:
                self._values["mapping"] = mapping

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the column that is created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_type(self) -> builtins.str:
            '''The type of column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype
            '''
            result = self._values.get("sql_type")
            assert result is not None, "Required property 'sql_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping(self) -> typing.Optional[builtins.str]:
            '''A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping
            '''
            result = self._values.get("mapping")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordFormatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_format_type": "recordFormatType",
            "mapping_parameters": "mappingParameters",
        },
    )
    class RecordFormatProperty:
        def __init__(
            self,
            *,
            record_format_type: builtins.str,
            mapping_parameters: typing.Optional[typing.Union[typing.Union["CfnApplicationReferenceDataSource.MappingParametersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

            :param record_format_type: The type of record format.
            :param mapping_parameters: When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                record_format_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordFormatProperty(
                    record_format_type="recordFormatType",
                
                    # the properties below are optional
                    mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty(
                        csv_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                            record_column_delimiter="recordColumnDelimiter",
                            record_row_delimiter="recordRowDelimiter"
                        ),
                        json_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                            record_row_path="recordRowPath"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb54eda137596911b754c1f0a9a9bf5242195584d0060b6a9f902bb8d3b45505)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
                check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_format_type": record_format_type,
            }
            if mapping_parameters is not None:
                self._values["mapping_parameters"] = mapping_parameters

        @builtins.property
        def record_format_type(self) -> builtins.str:
            '''The type of record format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-recordformattype
            '''
            result = self._values.get("record_format_type")
            assert result is not None, "Required property 'record_format_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationReferenceDataSource.MappingParametersProperty", _IResolvable_a771d0ef]]:
            '''When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters
            '''
            result = self._values.get("mapping_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationReferenceDataSource.MappingParametersProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "reference_schema": "referenceSchema",
            "s3_reference_data_source": "s3ReferenceDataSource",
            "table_name": "tableName",
        },
    )
    class ReferenceDataSourceProperty:
        def __init__(
            self,
            *,
            reference_schema: typing.Union[typing.Union["CfnApplicationReferenceDataSource.ReferenceSchemaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            s3_reference_data_source: typing.Optional[typing.Union[typing.Union["CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            table_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

            :param reference_schema: Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            :param s3_reference_data_source: Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.
            :param table_name: The name of the in-application table to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                reference_data_source_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty(
                    reference_schema=kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                        record_columns=[kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
                
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordFormatProperty(
                            record_format_type="recordFormatType",
                
                            # the properties below are optional
                            mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
                
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                
                    # the properties below are optional
                    s3_reference_data_source=kinesisanalyticsv2.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey"
                    ),
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8fb9355d29d0b83aeff8560e276cb13f9ff4365e1f8ff6174a40a22e4c04b36)
                check_type(argname="argument reference_schema", value=reference_schema, expected_type=type_hints["reference_schema"])
                check_type(argname="argument s3_reference_data_source", value=s3_reference_data_source, expected_type=type_hints["s3_reference_data_source"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_schema": reference_schema,
            }
            if s3_reference_data_source is not None:
                self._values["s3_reference_data_source"] = s3_reference_data_source
            if table_name is not None:
                self._values["table_name"] = table_name

        @builtins.property
        def reference_schema(
            self,
        ) -> typing.Union["CfnApplicationReferenceDataSource.ReferenceSchemaProperty", _IResolvable_a771d0ef]:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema
            '''
            result = self._values.get("reference_schema")
            assert result is not None, "Required property 'reference_schema' is missing"
            return typing.cast(typing.Union["CfnApplicationReferenceDataSource.ReferenceSchemaProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def s3_reference_data_source(
            self,
        ) -> typing.Optional[typing.Union["CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty", _IResolvable_a771d0ef]]:
            '''Identifies the S3 bucket and object that contains the reference data.

            A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource
            '''
            result = self._values.get("s3_reference_data_source")
            return typing.cast(typing.Optional[typing.Union["CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''The name of the in-application table to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_columns": "recordColumns",
            "record_format": "recordFormat",
            "record_encoding": "recordEncoding",
        },
    )
    class ReferenceSchemaProperty:
        def __init__(
            self,
            *,
            record_columns: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplicationReferenceDataSource.RecordColumnProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
            record_format: typing.Union[typing.Union["CfnApplicationReferenceDataSource.RecordFormatProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            record_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :param record_columns: A list of ``RecordColumn`` objects.
            :param record_format: Specifies the format of the records on the streaming source.
            :param record_encoding: Specifies the encoding of the records in the streaming source. For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                reference_schema_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                    record_columns=[kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
                
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordFormatProperty(
                        record_format_type="recordFormatType",
                
                        # the properties below are optional
                        mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    record_encoding="recordEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5c53d79f81a243372e59b967f40bee8dcc429bfad0e9f68e6c55e784e6548dd)
                check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
                check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
                check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_columns": record_columns,
                "record_format": record_format,
            }
            if record_encoding is not None:
                self._values["record_encoding"] = record_encoding

        @builtins.property
        def record_columns(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplicationReferenceDataSource.RecordColumnProperty", _IResolvable_a771d0ef]]]:
            '''A list of ``RecordColumn`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns
            '''
            result = self._values.get("record_columns")
            assert result is not None, "Required property 'record_columns' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplicationReferenceDataSource.RecordColumnProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def record_format(
            self,
        ) -> typing.Union["CfnApplicationReferenceDataSource.RecordFormatProperty", _IResolvable_a771d0ef]:
            '''Specifies the format of the records on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat
            '''
            result = self._values.get("record_format")
            assert result is not None, "Required property 'record_format' is missing"
            return typing.cast(typing.Union["CfnApplicationReferenceDataSource.RecordFormatProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def record_encoding(self) -> typing.Optional[builtins.str]:
            '''Specifies the encoding of the records in the streaming source.

            For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding
            '''
            result = self._values.get("record_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_arn": "bucketArn", "file_key": "fileKey"},
    )
    class S3ReferenceDataSourceProperty:
        def __init__(self, *, bucket_arn: builtins.str, file_key: builtins.str) -> None:
            '''For an SQL-based Amazon Kinesis Data Analytics application, identifies the Amazon S3 bucket and object that contains the reference data.

            A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.

            :param bucket_arn: The Amazon Resource Name (ARN) of the S3 bucket.
            :param file_key: The object key name containing the reference data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
                
                s3_reference_data_source_property = kinesisanalyticsv2.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0be2e0fc25e2a4fe79899029ad17c9c3764b6374288eea5f014bba8f3a6ce003)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "file_key": file_key,
            }

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_key(self) -> builtins.str:
            '''The object key name containing the reference data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey
            '''
            result = self._values.get("file_key")
            assert result is not None, "Required property 'file_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ReferenceDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_kinesisanalyticsv2.CfnApplicationReferenceDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "reference_data_source": "referenceDataSource",
    },
)
class CfnApplicationReferenceDataSourceProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        reference_data_source: typing.Union[typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Properties for defining a ``CfnApplicationReferenceDataSource``.

        :param application_name: The name of the application.
        :param reference_data_source: For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_kinesisanalyticsv2 as kinesisanalyticsv2
            
            cfn_application_reference_data_source_props = kinesisanalyticsv2.CfnApplicationReferenceDataSourceProps(
                application_name="applicationName",
                reference_data_source=kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty(
                    reference_schema=kinesisanalyticsv2.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                        record_columns=[kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
            
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalyticsv2.CfnApplicationReferenceDataSource.RecordFormatProperty(
                            record_format_type="recordFormatType",
            
                            # the properties below are optional
                            mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalyticsv2.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
            
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
            
                    # the properties below are optional
                    s3_reference_data_source=kinesisanalyticsv2.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey"
                    ),
                    table_name="tableName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07a003aa006e793a4fb5478bb16c17d3ad1714c053edc769e9f9b4848864991)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument reference_data_source", value=reference_data_source, expected_type=type_hints["reference_data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "reference_data_source": reference_data_source,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reference_data_source(
        self,
    ) -> typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, _IResolvable_a771d0ef]:
        '''For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
        '''
        result = self._values.get("reference_data_source")
        assert result is not None, "Required property 'reference_data_source' is missing"
        return typing.cast(typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, _IResolvable_a771d0ef], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationReferenceDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationCloudWatchLoggingOption",
    "CfnApplicationCloudWatchLoggingOptionProps",
    "CfnApplicationOutput",
    "CfnApplicationOutputProps",
    "CfnApplicationProps",
    "CfnApplicationReferenceDataSource",
    "CfnApplicationReferenceDataSourceProps",
]

publication.publish()

def _typecheckingstub__12e67892a82c6d1808b5d6c741fa71363db5f6826592dea9906e4acd4726c71b(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    runtime_environment: builtins.str,
    service_execution_role: builtins.str,
    application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_maintenance_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    application_mode: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
    run_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.RunConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b072b5b9c049860c2761003244200c7bfc5b54664a33d619d25b598d43a1443(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e100f6d8c189b6599865437dacff274cc5f6d10779f4a1ac0bad3a6e74e72fb0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1dd55ad95914803e10f8c8eaeb87515063322bc9a9c814946c8166395fa4035(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a10b6ff7459cf5fe1f1266f7aef330cfd09792a0c3bb052627c00ece64faa425(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b235931470408a9cb299904e2942364a0b27e4565b900c557b297bf8205a397c(
    value: typing.Optional[typing.Union[CfnApplication.ApplicationConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1aa2e851a1c297bdc7e6dad9869dfe704d5f6003bfa580d283074ae041adadf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743c8a381911e16447a8636deacd67efd6da8dca4f27b3eaf23b97b03627071b(
    value: typing.Optional[typing.Union[CfnApplication.ApplicationMaintenanceConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd09b1de1838881420cce52ab783d77852e5c8f550939f1fc3563f1a7e2b4fa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fbec8560868a34badcbc4885de17d083836da83abfe5ba02a394aec0f9704d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699b043527d0eab8bc137440c2366270bb1cf87b18f80da555845fd0e200414e(
    value: typing.Optional[typing.Union[CfnApplication.RunConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13eeab7bbd807eedcde281c9bdc70fd1558cf16e894d7621aeae5ef23b21000e(
    *,
    code_content: typing.Union[typing.Union[CfnApplication.CodeContentProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    code_content_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf609d2989df28525010c375f134f6321667a16467ea4466f5d4e0726803488(
    *,
    application_code_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationCodeConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    application_snapshot_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationSnapshotConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    environment_properties: typing.Optional[typing.Union[typing.Union[CfnApplication.EnvironmentPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    flink_application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.FlinkApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sql_application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.SqlApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    vpc_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    zeppelin_application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ZeppelinApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7462f8d09fdb8ff887317583b98a199e471b98e4a50f44f1f8a2644c21f6639d(
    *,
    application_maintenance_window_start_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa7fb84287e4033b4cb56097667a9b3357e1e5b751480d08cfe91262ef33589(
    *,
    application_restore_type: builtins.str,
    snapshot_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc52c2ce7cc5186b3dff29ff0057aecc56120b03cf3d81011bc77552df12ce09(
    *,
    snapshots_enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14e6d57cccce8fda1518d7421e571116034a17fcfe62756d1e8b612e5faf4c9(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f220f09714a28332714008ca1cbd47bc4805aeb1ef275e127b85c1f08bc7f494(
    *,
    glue_data_catalog_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.GlueDataCatalogConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8c4bd6829e531df3cbac9d8bb68bb24a5d7c9d978d05e21da8c79156cf88cf(
    *,
    configuration_type: builtins.str,
    checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    checkpoint_interval: typing.Optional[jsii.Number] = None,
    min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5da6df32ce408303384d90949a674ab8c057c88fd28d42887434699d64aaaff(
    *,
    s3_content_location: typing.Optional[typing.Union[typing.Union[CfnApplication.S3ContentLocationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    text_content: typing.Optional[builtins.str] = None,
    zip_file_content: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac8ebe88f7cd9056ef1e8530d1f385c787f7bcc14f35dd6085fdd081c7c6344(
    *,
    artifact_type: builtins.str,
    maven_reference: typing.Optional[typing.Union[typing.Union[CfnApplication.MavenReferenceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    s3_content_location: typing.Optional[typing.Union[typing.Union[CfnApplication.S3ContentLocationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf70e5813fb387690981a05abe1b3349f24f89b7f5f7552d25470e14d324df06(
    *,
    s3_content_location: typing.Union[typing.Union[CfnApplication.S3ContentBaseLocationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2149252f1fba3853f4547ab1e4a59f90dbb1440c859dd59819f6a15f8eb1f7(
    *,
    property_groups: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.PropertyGroupProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b605308ceb4be4709633e97f0a389cdd488993b82d8d56b81c0550ab8617b1ba(
    *,
    checkpoint_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.CheckpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    monitoring_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    parallelism_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ParallelismConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4da069b82e76ab0194e91430281f179c3d6668b09bca4be4fa71c5a61c93ca8(
    *,
    allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97bbd7472996325553db625cc32496a2ee6e5ec82ceffb1176cf9629827a5d0(
    *,
    database_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0dc913c642e0d7fdb4c27e14a3116ad2ac8761071d7a245fe0ede17c91958b(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d05df1edf43f121cb6afde5c953f3321d0e9fed1f138c7d8ccb5b38c7f228c(
    *,
    count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27e29aedd4e30be4ff1e97d0cdd36861d3ca026f17651c891cedae66abddc5c(
    *,
    input_lambda_processor: typing.Optional[typing.Union[typing.Union[CfnApplication.InputLambdaProcessorProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d29088a61dcb4e7cb40f424bfad67cc87998380931c0245cc65e8e61af5a16(
    *,
    input_schema: typing.Union[typing.Union[CfnApplication.InputSchemaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    name_prefix: builtins.str,
    input_parallelism: typing.Optional[typing.Union[typing.Union[CfnApplication.InputParallelismProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    input_processing_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.InputProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kinesis_firehose_input: typing.Optional[typing.Union[typing.Union[CfnApplication.KinesisFirehoseInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kinesis_streams_input: typing.Optional[typing.Union[typing.Union[CfnApplication.KinesisStreamsInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07582f09ec12cbc76de59fd2c5e05fa6218ccbff367381671d9d6d4030c68100(
    *,
    record_columns: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.RecordColumnProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    record_format: typing.Union[typing.Union[CfnApplication.RecordFormatProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eba0a5944e215305c2f0b5a2aa0b4cd079d74257bf71e104ca00aaab430cc273(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b08ef2e6b733956aa0067d4eac9e0d5b985c9e12f26717621bf4fc94f7046fa(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba0dd16da39f3bcc9e9740ee7a5b2339ec88e7c4f0a5a0d7b6353293af76614(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8215b5c7883e182db6518989b0d53378e85928196ffe3588da4a2e7461e8cec0(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[typing.Union[CfnApplication.CSVMappingParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[typing.Union[CfnApplication.JSONMappingParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33ab3b00534d95c05dae81dd5bbc5127193db0b389d399d946d04809da919ff(
    *,
    artifact_id: builtins.str,
    group_id: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e257771a336685becd71f4c3b56cab2ca4cf42092ed173e247a1bff8949de2c5(
    *,
    configuration_type: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
    metrics_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3679c096e66f08dbee6d0c1adedaace74f43467f8d943c41af773860c0c3642(
    *,
    configuration_type: builtins.str,
    auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    parallelism: typing.Optional[jsii.Number] = None,
    parallelism_per_kpu: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86aa6ad12be17a993ab91b0ce275ac4f361e59a29c1d54591f300fdb8859fc9(
    *,
    property_group_id: typing.Optional[builtins.str] = None,
    property_map: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b22aaeaca13d8c4a421431996bf70cd18f416137fb2396c699ec0645fd7b9302(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d9cad5b7cd64bae3df4be2d3dc19b7dbe08cf10e1171d9ebf12b999cc3eb27f(
    *,
    record_format_type: builtins.str,
    mapping_parameters: typing.Optional[typing.Union[typing.Union[CfnApplication.MappingParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a42e0fac5c7628128bdc30f3c35565ca083169b903f655b3a6c22062157a384(
    *,
    application_restore_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationRestoreConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    flink_run_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.FlinkRunConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2da0d51202d0f062effcca96f9892423ca35b3273f5bce36b956e5f9bb6770d(
    *,
    bucket_arn: builtins.str,
    base_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6321dd0fc53802294669175bc8428f6bc176c78816b4da0f776098b5ca4b7c9(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e38bfb8546822a60c3939bf4683ce4585642fd16375fad99cff06d75f5881fd0(
    *,
    inputs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.InputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0641a9df6ea02dfd3cbc91ef2e9dc4840d1d28f5f6d1d5ec9bb19d063fcfb7f7(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abd85eb978e76384e96ee4e723bb54178d27f84cb56d5dfa7b180d8a9d2687c(
    *,
    catalog_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.CatalogConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    custom_artifacts_configuration: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.CustomArtifactConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    deploy_as_application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.DeployAsApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    monitoring_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ZeppelinMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a921d2594e7d83ab1caf34ab022271dc283f0c4c7adbb187986ad5aa82e1092(
    *,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66c427154899af9803115aa7b67044500e370aa5c3d23d2fb565dfc44df56b8(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    application_name: builtins.str,
    cloud_watch_logging_option: typing.Union[typing.Union[CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a849bf42636f2b1c8e6e98a8264331e330d259a43059e6a3bac9c3f1b4c731f(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c438ebfbbd2ccbadfc14057a7b12f05f31f056fe7b3501eeb205b21e0b3a710f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a8e120c57ca619dd0c44757426e8a365050f5f3b801fa4790b06194ff2805c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc63f6963b1507360f0f71666b5373d08899f4cf560596cdb776c8232a7a18c0(
    value: typing.Union[CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0860029a68d5a969b1530e03eddfafe354c343e8665a07aeadd64d203729308d(
    *,
    log_stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088a026a61075834276214d56567cb73f83ba68c0b84507b923e6fe7f2afc509(
    *,
    application_name: builtins.str,
    cloud_watch_logging_option: typing.Union[typing.Union[CfnApplicationCloudWatchLoggingOption.CloudWatchLoggingOptionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b349088222421e3c50e6e5c907b5849a2724995d71d433a04e0c6cf60bfb0b81(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    application_name: builtins.str,
    output: typing.Union[typing.Union[CfnApplicationOutput.OutputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b45c7707450f48e64bf550749124d935e40d67395840ea88b5871e245c581ce(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67311b2235be7d3e320c535379c43d2ea791808f49da523fa7cb73b4d820815a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f4e50f771f1193f875fdab3ceb20f8e7cde0bd1b541d63a018c3b38f5364d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4facdb2b648238b2f495d81f71664370f6b515061c3f0e0c09e8140ba02bf99(
    value: typing.Union[CfnApplicationOutput.OutputProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc8785b6cda6486c803af7fba6996a2eefd9790b7ab489491d5ee93f29534f72(
    *,
    record_format_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc938ab4e3df1578b2a3902504b29e1c4c95f52764b5fd69b1156abdf98a0bc(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0a116ad42f8729047d93a312b247dc295c41473f9de5764eeb6d38d1832765(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939acc597225a110aab8861676e18abcd08ef77273acb1daf6f4a5b60c872b77(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea6bc770388499b050e422780c4626409280ae8780c26fe7aa12bd8a36f1807(
    *,
    destination_schema: typing.Union[typing.Union[CfnApplicationOutput.DestinationSchemaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    kinesis_firehose_output: typing.Optional[typing.Union[typing.Union[CfnApplicationOutput.KinesisFirehoseOutputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kinesis_streams_output: typing.Optional[typing.Union[typing.Union[CfnApplicationOutput.KinesisStreamsOutputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    lambda_output: typing.Optional[typing.Union[typing.Union[CfnApplicationOutput.LambdaOutputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32968bd6091e478dd2b78f10321b0677a621a2ee9edceeb1ea063139b1f152d9(
    *,
    application_name: builtins.str,
    output: typing.Union[typing.Union[CfnApplicationOutput.OutputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39db75c89149de5863b2d649418dc3661b84e8793445aa4d71e2384c22fc6404(
    *,
    runtime_environment: builtins.str,
    service_execution_role: builtins.str,
    application_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_maintenance_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ApplicationMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    application_mode: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
    run_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.RunConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25610c135bf208b232f6545a5c4093e4ca2c12c2871ea1a8d87e9912c41c8f53(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    application_name: builtins.str,
    reference_data_source: typing.Union[typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356a199f3a0010617f6aafe57e8451311e0ac55941fd9035c96d3c419795c96e(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0539ad95d248380df273f7fa43b7b1c2da39b3c46baa2125d1f801c48f89af0b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72732ae0525d29dd775d8095afffde56e03c0928af738b1c665a45352f6b3ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7debe0e1784a621fbff07ba1518272c0c6e8d98736201fadf1b4f9094fd58515(
    value: typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d632f1cc043e69b3c6395c7f040b5572b52cab2830faa81bb1f9ce9b287ac5c7(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b573a01e361030c64e926fa5f1401124f594e0979e9580236bffff3be848ee9(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c944f769f2c0a1a9f39f3fef36fa8b8871bf4782112eacda97f3779ef05828(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[typing.Union[CfnApplicationReferenceDataSource.CSVMappingParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[typing.Union[CfnApplicationReferenceDataSource.JSONMappingParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e467e0d96c4b4d68162b27ed41290bf4d452f0fe8efd3f93b09971abfa2fc5(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb54eda137596911b754c1f0a9a9bf5242195584d0060b6a9f902bb8d3b45505(
    *,
    record_format_type: builtins.str,
    mapping_parameters: typing.Optional[typing.Union[typing.Union[CfnApplicationReferenceDataSource.MappingParametersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fb9355d29d0b83aeff8560e276cb13f9ff4365e1f8ff6174a40a22e4c04b36(
    *,
    reference_schema: typing.Union[typing.Union[CfnApplicationReferenceDataSource.ReferenceSchemaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    s3_reference_data_source: typing.Optional[typing.Union[typing.Union[CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    table_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c53d79f81a243372e59b967f40bee8dcc429bfad0e9f68e6c55e784e6548dd(
    *,
    record_columns: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplicationReferenceDataSource.RecordColumnProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    record_format: typing.Union[typing.Union[CfnApplicationReferenceDataSource.RecordFormatProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be2e0fc25e2a4fe79899029ad17c9c3764b6374288eea5f014bba8f3a6ce003(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07a003aa006e793a4fb5478bb16c17d3ad1714c053edc769e9f9b4848864991(
    *,
    application_name: builtins.str,
    reference_data_source: typing.Union[typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

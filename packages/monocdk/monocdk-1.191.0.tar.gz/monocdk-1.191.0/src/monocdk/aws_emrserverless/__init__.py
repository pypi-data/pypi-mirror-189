'''
# AWS::EMRServerless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as emrserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMRServerless construct libraries](https://constructs.dev/search?q=emrserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMRServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMRServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRServerless.html).

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
    jsii_type="monocdk.aws_emrserverless.CfnApplication",
):
    '''A CloudFormation ``AWS::EMRServerless::Application``.

    The ``AWS::EMRServerless::Application`` resource specifies an EMR Serverless application. An application uses open source analytics frameworks to run jobs that process data. To create an application, you must specify the release version for the open source framework version you want to use and the type of application you want, such as Apache Spark or Apache Hive. After you create an application, you can submit data processing jobs or interactive requests to it.

    :cloudformationResource: AWS::EMRServerless::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_emrserverless as emrserverless
        
        cfn_application = emrserverless.CfnApplication(self, "MyCfnApplication",
            release_label="releaseLabel",
            type="type",
        
            # the properties below are optional
            architecture="architecture",
            auto_start_configuration=emrserverless.CfnApplication.AutoStartConfigurationProperty(
                enabled=False
            ),
            auto_stop_configuration=emrserverless.CfnApplication.AutoStopConfigurationProperty(
                enabled=False,
                idle_timeout_minutes=123
            ),
            image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                image_uri="imageUri"
            ),
            initial_capacity=[emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                key="key",
                value=emrserverless.CfnApplication.InitialCapacityConfigProperty(
                    worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                        cpu="cpu",
                        memory="memory",
        
                        # the properties below are optional
                        disk="disk"
                    ),
                    worker_count=123
                )
            )],
            maximum_capacity=emrserverless.CfnApplication.MaximumAllowedResourcesProperty(
                cpu="cpu",
                memory="memory",
        
                # the properties below are optional
                disk="disk"
            ),
            name="name",
            network_configuration=emrserverless.CfnApplication.NetworkConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            worker_type_specifications={
                "worker_type_specifications_key": emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty(
                    image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                        image_uri="imageUri"
                    )
                )
            }
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        release_label: builtins.str,
        type: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        auto_start_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.AutoStartConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        auto_stop_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.AutoStopConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        image_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ImageConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        initial_capacity: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnApplication.InitialCapacityConfigKeyValuePairProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        maximum_capacity: typing.Optional[typing.Union[typing.Union["CfnApplication.MaximumAllowedResourcesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_type_specifications: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnApplication.WorkerTypeSpecificationInputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRServerless::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param release_label: The EMR release version associated with the application. *Minimum* : 1 *Maximum* : 64 *Pattern* : ``^[A-Za-z0-9._/-]+$``
        :param type: The type of application, such as Spark or Hive.
        :param architecture: The CPU architecture type of the application. Allowed values: ``X86_64`` or ``ARM64``
        :param auto_start_configuration: The configuration for an application to automatically start on job submission.
        :param auto_stop_configuration: The configuration for an application to automatically stop after a certain amount of time being idle.
        :param image_configuration: The image configuration applied to all worker types.
        :param initial_capacity: The initial capacity of the application.
        :param maximum_capacity: The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.
        :param name: The name of the application. *Minimum* : 1 *Maximum* : 64 *Pattern* : ``^[A-Za-z0-9._\\\\/#-]+$``
        :param network_configuration: The network configuration for customer VPC connectivity for the application.
        :param tags: The tags assigned to the application.
        :param worker_type_specifications: The specification applied to each worker type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2def5a29819fba00d3e95c284e6b6ad99fecc63a7fa191864d3cece5270e800)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            release_label=release_label,
            type=type,
            architecture=architecture,
            auto_start_configuration=auto_start_configuration,
            auto_stop_configuration=auto_stop_configuration,
            image_configuration=image_configuration,
            initial_capacity=initial_capacity,
            maximum_capacity=maximum_capacity,
            name=name,
            network_configuration=network_configuration,
            tags=tags,
            worker_type_specifications=worker_type_specifications,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358b2208ce14da0230fad65c9cdff98cbfc9e37511a9f6904f31602bbf000c55)
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
            type_hints = typing.get_type_hints(_typecheckingstub__43f28f0192289d70abdeec853b2d1c5fd0f17ab1ab2e14ff4c40be80f7c4471c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''The ID of the application, such as ``ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the project.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''The tags assigned to the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        '''The EMR release version associated with the application.

        *Minimum* : 1

        *Maximum* : 64

        *Pattern* : ``^[A-Za-z0-9._/-]+$``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-releaselabel
        '''
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ee5b8825364e2f73465577126d4aa57ff0dc0b62bc8692295c5b886cd55544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of application, such as Spark or Hive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e55c2d5f6b1a8413abefe0e1b0b65b0e211c4f418c6dfb7bc7b48dc1a7b9150a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> typing.Optional[builtins.str]:
        '''The CPU architecture type of the application.

        Allowed values: ``X86_64`` or ``ARM64``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-architecture
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7023b9ac50f1930079b9c0f26ad577d3d42e1352f8276b857aa8e98526f2866a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value)

    @builtins.property
    @jsii.member(jsii_name="autoStartConfiguration")
    def auto_start_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.AutoStartConfigurationProperty", _IResolvable_a771d0ef]]:
        '''The configuration for an application to automatically start on job submission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostartconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.AutoStartConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "autoStartConfiguration"))

    @auto_start_configuration.setter
    def auto_start_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.AutoStartConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56ba22cebb5f28ac547ec1a2b1bf0d8c07bca7d2bb25df78f726a92c783d63b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStartConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="autoStopConfiguration")
    def auto_stop_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.AutoStopConfigurationProperty", _IResolvable_a771d0ef]]:
        '''The configuration for an application to automatically stop after a certain amount of time being idle.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostopconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.AutoStopConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "autoStopConfiguration"))

    @auto_stop_configuration.setter
    def auto_stop_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.AutoStopConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d4db05cbd99642a575bfbe31cc97d31f7ebaf881eb868427a15432e59f06ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStopConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageConfiguration")
    def image_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.ImageConfigurationInputProperty", _IResolvable_a771d0ef]]:
        '''The image configuration applied to all worker types.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-imageconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.ImageConfigurationInputProperty", _IResolvable_a771d0ef]], jsii.get(self, "imageConfiguration"))

    @image_configuration.setter
    def image_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.ImageConfigurationInputProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6694ffdf382c05463e35b8ba63b0f86166274b5b85e5529d6d070547ed65b616)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="initialCapacity")
    def initial_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.InitialCapacityConfigKeyValuePairProperty", _IResolvable_a771d0ef]]]]:
        '''The initial capacity of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-initialcapacity
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.InitialCapacityConfigKeyValuePairProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "initialCapacity"))

    @initial_capacity.setter
    def initial_capacity(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnApplication.InitialCapacityConfigKeyValuePairProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355df0b6b1e6ec3344487bea06275b90f0f9620dc3fa44bcc3576469c3ae0ddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="maximumCapacity")
    def maximum_capacity(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.MaximumAllowedResourcesProperty", _IResolvable_a771d0ef]]:
        '''The maximum capacity of the application.

        This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-maximumcapacity
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.MaximumAllowedResourcesProperty", _IResolvable_a771d0ef]], jsii.get(self, "maximumCapacity"))

    @maximum_capacity.setter
    def maximum_capacity(
        self,
        value: typing.Optional[typing.Union["CfnApplication.MaximumAllowedResourcesProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a733767df574926ee1726131c2f31033dd434daaf9d322dcc720c78a44c5867b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        *Minimum* : 1

        *Maximum* : 64

        *Pattern* : ``^[A-Za-z0-9._\\\\/#-]+$``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdc3eeea2304b53b1e450fb562e0f145a4dda373b7ac4acfaf1d2f651080107c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnApplication.NetworkConfigurationProperty", _IResolvable_a771d0ef]]:
        '''The network configuration for customer VPC connectivity for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-networkconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplication.NetworkConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union["CfnApplication.NetworkConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c7a3716b8f4cdb5ef3aa52d4256bb49cdf1467ee5f9883b21531bded468444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="workerTypeSpecifications")
    def worker_type_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnApplication.WorkerTypeSpecificationInputProperty", _IResolvable_a771d0ef]]]]:
        '''The specification applied to each worker type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-workertypespecifications
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnApplication.WorkerTypeSpecificationInputProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "workerTypeSpecifications"))

    @worker_type_specifications.setter
    def worker_type_specifications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnApplication.WorkerTypeSpecificationInputProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78eadf1d334152f8023e8a94b3cd108bd99814cedd9df8975504f451aaaa317e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerTypeSpecifications", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.AutoStartConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AutoStartConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The conﬁguration for an application to automatically start on job submission.

            :param enabled: Enables the application to automatically start on job submission. Defaults to true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                auto_start_configuration_property = emrserverless.CfnApplication.AutoStartConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__370f12f1920dd05dcd2558ce09d3685ae6c995cd855a3233c85397b47794ae91)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Enables the application to automatically start on job submission.

            Defaults to true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html#cfn-emrserverless-application-autostartconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoStartConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.AutoStopConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "idle_timeout_minutes": "idleTimeoutMinutes",
        },
    )
    class AutoStopConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            idle_timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The conﬁguration for an application to automatically stop after a certain amount of time being idle.

            :param enabled: Enables the application to automatically stop after a certain amount of time being idle. Defaults to true.
            :param idle_timeout_minutes: The amount of idle time in minutes after which your application will automatically stop. Defaults to 15 minutes. *Minimum* : 1 *Maximum* : 10080

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                auto_stop_configuration_property = emrserverless.CfnApplication.AutoStopConfigurationProperty(
                    enabled=False,
                    idle_timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4809d7a3c791d01aa8da83404630f9a7909e729e1eb68c5f32330abb4244f7b0)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument idle_timeout_minutes", value=idle_timeout_minutes, expected_type=type_hints["idle_timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if idle_timeout_minutes is not None:
                self._values["idle_timeout_minutes"] = idle_timeout_minutes

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Enables the application to automatically stop after a certain amount of time being idle.

            Defaults to true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html#cfn-emrserverless-application-autostopconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def idle_timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The amount of idle time in minutes after which your application will automatically stop. Defaults to 15 minutes.

            *Minimum* : 1

            *Maximum* : 10080

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html#cfn-emrserverless-application-autostopconfiguration-idletimeoutminutes
            '''
            result = self._values.get("idle_timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoStopConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.ImageConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"image_uri": "imageUri"},
    )
    class ImageConfigurationInputProperty:
        def __init__(self, *, image_uri: typing.Optional[builtins.str] = None) -> None:
            '''The image configuration.

            :param image_uri: The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-imageconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                image_configuration_input_property = emrserverless.CfnApplication.ImageConfigurationInputProperty(
                    image_uri="imageUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15deaeb26439772f9121d7df090fd53fd7815c226cf46a8f5b4c0f9cffb98ec9)
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_uri is not None:
                self._values["image_uri"] = image_uri

        @builtins.property
        def image_uri(self) -> typing.Optional[builtins.str]:
            '''The URI of an image in the Amazon ECR registry.

            This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-imageconfigurationinput.html#cfn-emrserverless-application-imageconfigurationinput-imageuri
            '''
            result = self._values.get("image_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class InitialCapacityConfigKeyValuePairProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[typing.Union["CfnApplication.InitialCapacityConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        ) -> None:
            '''The initial capacity configuration per worker.

            :param key: The worker type for an analytics framework. For Spark applications, the key can either be set to ``Driver`` or ``Executor`` . For Hive applications, it can be set to ``HiveDriver`` or ``TezTask`` . *Minimum* : 1 *Maximum* : 50 *Pattern* : ``^[a-zA-Z]+[-_]*[a-zA-Z]+$``
            :param value: The value for the initial capacity configuration per worker.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                initial_capacity_config_key_value_pair_property = emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                    key="key",
                    value=emrserverless.CfnApplication.InitialCapacityConfigProperty(
                        worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                            cpu="cpu",
                            memory="memory",
                
                            # the properties below are optional
                            disk="disk"
                        ),
                        worker_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1c0e5518e9aced40b236c9e7e78c240295afb3c816fbc36982bde35ad46835ba)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The worker type for an analytics framework.

            For Spark applications, the key can either be set to ``Driver`` or ``Executor`` . For Hive applications, it can be set to ``HiveDriver`` or ``TezTask`` .

            *Minimum* : 1

            *Maximum* : 50

            *Pattern* : ``^[a-zA-Z]+[-_]*[a-zA-Z]+$``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union["CfnApplication.InitialCapacityConfigProperty", _IResolvable_a771d0ef]:
            '''The value for the initial capacity configuration per worker.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union["CfnApplication.InitialCapacityConfigProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialCapacityConfigKeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.InitialCapacityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "worker_configuration": "workerConfiguration",
            "worker_count": "workerCount",
        },
    )
    class InitialCapacityConfigProperty:
        def __init__(
            self,
            *,
            worker_configuration: typing.Union[typing.Union["CfnApplication.WorkerConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            worker_count: jsii.Number,
        ) -> None:
            '''The initial capacity configuration per worker.

            :param worker_configuration: The resource configuration of the initial capacity configuration.
            :param worker_count: The number of workers in the initial capacity configuration. *Minimum* : 1 *Maximum* : 1000000

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                initial_capacity_config_property = emrserverless.CfnApplication.InitialCapacityConfigProperty(
                    worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                        cpu="cpu",
                        memory="memory",
                
                        # the properties below are optional
                        disk="disk"
                    ),
                    worker_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f529c9b5a8cf9ab7b06b913d889b6eb3e8084e9fa03445238f18eb5ff565b57)
                check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
                check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "worker_configuration": worker_configuration,
                "worker_count": worker_count,
            }

        @builtins.property
        def worker_configuration(
            self,
        ) -> typing.Union["CfnApplication.WorkerConfigurationProperty", _IResolvable_a771d0ef]:
            '''The resource configuration of the initial capacity configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html#cfn-emrserverless-application-initialcapacityconfig-workerconfiguration
            '''
            result = self._values.get("worker_configuration")
            assert result is not None, "Required property 'worker_configuration' is missing"
            return typing.cast(typing.Union["CfnApplication.WorkerConfigurationProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def worker_count(self) -> jsii.Number:
            '''The number of workers in the initial capacity configuration.

            *Minimum* : 1

            *Maximum* : 1000000

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html#cfn-emrserverless-application-initialcapacityconfig-workercount
            '''
            result = self._values.get("worker_count")
            assert result is not None, "Required property 'worker_count' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialCapacityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.MaximumAllowedResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu": "cpu", "memory": "memory", "disk": "disk"},
    )
    class MaximumAllowedResourcesProperty:
        def __init__(
            self,
            *,
            cpu: builtins.str,
            memory: builtins.str,
            disk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The maximum allowed cumulative resources for an application.

            No new resources will be created once the limit is hit.

            :param cpu: The maximum allowed CPU for an application. *Minimum* : 1 *Maximum* : 15 *Pattern* : ``^[1-9][0-9]*(\\\\s)?(vCPU|vcpu|VCPU)?$``
            :param memory: The maximum allowed resources for an application. *Minimum* : 1 *Maximum* : 15 *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)?$``
            :param disk: The maximum allowed disk for an application. *Minimum* : 1 *Maximum* : 15 *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)$"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                maximum_allowed_resources_property = emrserverless.CfnApplication.MaximumAllowedResourcesProperty(
                    cpu="cpu",
                    memory="memory",
                
                    # the properties below are optional
                    disk="disk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d7edeb0cc7cb49c07cb1db3e7cf8fd8924ff21c434570f205d6ca59a6f049f9)
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu": cpu,
                "memory": memory,
            }
            if disk is not None:
                self._values["disk"] = disk

        @builtins.property
        def cpu(self) -> builtins.str:
            '''The maximum allowed CPU for an application.

            *Minimum* : 1

            *Maximum* : 15

            *Pattern* : ``^[1-9][0-9]*(\\\\s)?(vCPU|vcpu|VCPU)?$``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-cpu
            '''
            result = self._values.get("cpu")
            assert result is not None, "Required property 'cpu' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def memory(self) -> builtins.str:
            '''The maximum allowed resources for an application.

            *Minimum* : 1

            *Maximum* : 15

            *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)?$``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-memory
            '''
            result = self._values.get("memory")
            assert result is not None, "Required property 'memory' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def disk(self) -> typing.Optional[builtins.str]:
            '''The maximum allowed disk for an application.

            *Minimum* : 1

            *Maximum* : 15

            *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)$"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-disk
            '''
            result = self._values.get("disk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaximumAllowedResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The network configuration for customer VPC connectivity.

            :param security_group_ids: The array of security group Ids for customer VPC connectivity. *Minimum* : 1 *Maximum* : 32 *Pattern* : ``^[-0-9a-zA-Z]+``
            :param subnet_ids: The array of subnet Ids for customer VPC connectivity. *Minimum* : 1 *Maximum* : 32 *Pattern* : ``^[-0-9a-zA-Z]+``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                network_configuration_property = emrserverless.CfnApplication.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10f9f815ec2c7acc701b84605938f516db5309bcb6b5745e54e29bd6de2fd422)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The array of security group Ids for customer VPC connectivity.

            *Minimum* : 1

            *Maximum* : 32

            *Pattern* : ``^[-0-9a-zA-Z]+``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html#cfn-emrserverless-application-networkconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The array of subnet Ids for customer VPC connectivity.

            *Minimum* : 1

            *Maximum* : 32

            *Pattern* : ``^[-0-9a-zA-Z]+``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html#cfn-emrserverless-application-networkconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.WorkerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu": "cpu", "memory": "memory", "disk": "disk"},
    )
    class WorkerConfigurationProperty:
        def __init__(
            self,
            *,
            cpu: builtins.str,
            memory: builtins.str,
            disk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The resource configuration of the initial capacity configuration.

            :param cpu: *Minimum* : 1. *Maximum* : 15 *Pattern* : ``^[1-9][0-9]*(\\\\s)?(vCPU|vcpu|VCPU)?$``
            :param memory: *Minimum* : 1. *Maximum* : 15 *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)?$``
            :param disk: *Minimum* : 1. *Maximum* : 15 *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)$"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                worker_configuration_property = emrserverless.CfnApplication.WorkerConfigurationProperty(
                    cpu="cpu",
                    memory="memory",
                
                    # the properties below are optional
                    disk="disk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57d98955cc118b9648503a4d0838fa75a032a4035514fdbbbfc2b8bf1a2f85a1)
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu": cpu,
                "memory": memory,
            }
            if disk is not None:
                self._values["disk"] = disk

        @builtins.property
        def cpu(self) -> builtins.str:
            '''*Minimum* : 1.

            *Maximum* : 15

            *Pattern* : ``^[1-9][0-9]*(\\\\s)?(vCPU|vcpu|VCPU)?$``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-cpu
            '''
            result = self._values.get("cpu")
            assert result is not None, "Required property 'cpu' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def memory(self) -> builtins.str:
            '''*Minimum* : 1.

            *Maximum* : 15

            *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)?$``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-memory
            '''
            result = self._values.get("memory")
            assert result is not None, "Required property 'memory' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def disk(self) -> typing.Optional[builtins.str]:
            '''*Minimum* : 1.

            *Maximum* : 15

            *Pattern* : ``^[1-9][0-9]*(\\\\s)?(GB|gb|gB|Gb)$"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-disk
            '''
            result = self._values.get("disk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"image_configuration": "imageConfiguration"},
    )
    class WorkerTypeSpecificationInputProperty:
        def __init__(
            self,
            *,
            image_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ImageConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The specifications for a worker type.

            :param image_configuration: The image configuration for a worker type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workertypespecificationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrserverless as emrserverless
                
                worker_type_specification_input_property = emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty(
                    image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                        image_uri="imageUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__380798d888d15f4423509027789672146e3161fd11743c96996b0a954206909a)
                check_type(argname="argument image_configuration", value=image_configuration, expected_type=type_hints["image_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_configuration is not None:
                self._values["image_configuration"] = image_configuration

        @builtins.property
        def image_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ImageConfigurationInputProperty", _IResolvable_a771d0ef]]:
            '''The image configuration for a worker type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workertypespecificationinput.html#cfn-emrserverless-application-workertypespecificationinput-imageconfiguration
            '''
            result = self._values.get("image_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ImageConfigurationInputProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerTypeSpecificationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_emrserverless.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "release_label": "releaseLabel",
        "type": "type",
        "architecture": "architecture",
        "auto_start_configuration": "autoStartConfiguration",
        "auto_stop_configuration": "autoStopConfiguration",
        "image_configuration": "imageConfiguration",
        "initial_capacity": "initialCapacity",
        "maximum_capacity": "maximumCapacity",
        "name": "name",
        "network_configuration": "networkConfiguration",
        "tags": "tags",
        "worker_type_specifications": "workerTypeSpecifications",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        release_label: builtins.str,
        type: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        auto_start_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.AutoStartConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        auto_stop_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.AutoStopConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        image_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        initial_capacity: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        maximum_capacity: typing.Optional[typing.Union[typing.Union[CfnApplication.MaximumAllowedResourcesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_type_specifications: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param release_label: The EMR release version associated with the application. *Minimum* : 1 *Maximum* : 64 *Pattern* : ``^[A-Za-z0-9._/-]+$``
        :param type: The type of application, such as Spark or Hive.
        :param architecture: The CPU architecture type of the application. Allowed values: ``X86_64`` or ``ARM64``
        :param auto_start_configuration: The configuration for an application to automatically start on job submission.
        :param auto_stop_configuration: The configuration for an application to automatically stop after a certain amount of time being idle.
        :param image_configuration: The image configuration applied to all worker types.
        :param initial_capacity: The initial capacity of the application.
        :param maximum_capacity: The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.
        :param name: The name of the application. *Minimum* : 1 *Maximum* : 64 *Pattern* : ``^[A-Za-z0-9._\\\\/#-]+$``
        :param network_configuration: The network configuration for customer VPC connectivity for the application.
        :param tags: The tags assigned to the application.
        :param worker_type_specifications: The specification applied to each worker type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_emrserverless as emrserverless
            
            cfn_application_props = emrserverless.CfnApplicationProps(
                release_label="releaseLabel",
                type="type",
            
                # the properties below are optional
                architecture="architecture",
                auto_start_configuration=emrserverless.CfnApplication.AutoStartConfigurationProperty(
                    enabled=False
                ),
                auto_stop_configuration=emrserverless.CfnApplication.AutoStopConfigurationProperty(
                    enabled=False,
                    idle_timeout_minutes=123
                ),
                image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                    image_uri="imageUri"
                ),
                initial_capacity=[emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                    key="key",
                    value=emrserverless.CfnApplication.InitialCapacityConfigProperty(
                        worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                            cpu="cpu",
                            memory="memory",
            
                            # the properties below are optional
                            disk="disk"
                        ),
                        worker_count=123
                    )
                )],
                maximum_capacity=emrserverless.CfnApplication.MaximumAllowedResourcesProperty(
                    cpu="cpu",
                    memory="memory",
            
                    # the properties below are optional
                    disk="disk"
                ),
                name="name",
                network_configuration=emrserverless.CfnApplication.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                worker_type_specifications={
                    "worker_type_specifications_key": emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty(
                        image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                            image_uri="imageUri"
                        )
                    )
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18932d3223f2e2289dc54cd89fb0a7a296f2ee5c21c9f9b7c7ceb64759218921)
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument auto_start_configuration", value=auto_start_configuration, expected_type=type_hints["auto_start_configuration"])
            check_type(argname="argument auto_stop_configuration", value=auto_stop_configuration, expected_type=type_hints["auto_stop_configuration"])
            check_type(argname="argument image_configuration", value=image_configuration, expected_type=type_hints["image_configuration"])
            check_type(argname="argument initial_capacity", value=initial_capacity, expected_type=type_hints["initial_capacity"])
            check_type(argname="argument maximum_capacity", value=maximum_capacity, expected_type=type_hints["maximum_capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument worker_type_specifications", value=worker_type_specifications, expected_type=type_hints["worker_type_specifications"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "release_label": release_label,
            "type": type,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if auto_start_configuration is not None:
            self._values["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            self._values["auto_stop_configuration"] = auto_stop_configuration
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration
        if initial_capacity is not None:
            self._values["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            self._values["maximum_capacity"] = maximum_capacity
        if name is not None:
            self._values["name"] = name
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if tags is not None:
            self._values["tags"] = tags
        if worker_type_specifications is not None:
            self._values["worker_type_specifications"] = worker_type_specifications

    @builtins.property
    def release_label(self) -> builtins.str:
        '''The EMR release version associated with the application.

        *Minimum* : 1

        *Maximum* : 64

        *Pattern* : ``^[A-Za-z0-9._/-]+$``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-releaselabel
        '''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of application, such as Spark or Hive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[builtins.str]:
        '''The CPU architecture type of the application.

        Allowed values: ``X86_64`` or ``ARM64``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-architecture
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_start_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.AutoStartConfigurationProperty, _IResolvable_a771d0ef]]:
        '''The configuration for an application to automatically start on job submission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostartconfiguration
        '''
        result = self._values.get("auto_start_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.AutoStartConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def auto_stop_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.AutoStopConfigurationProperty, _IResolvable_a771d0ef]]:
        '''The configuration for an application to automatically stop after a certain amount of time being idle.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostopconfiguration
        '''
        result = self._values.get("auto_stop_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.AutoStopConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def image_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.ImageConfigurationInputProperty, _IResolvable_a771d0ef]]:
        '''The image configuration applied to all worker types.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-imageconfiguration
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.ImageConfigurationInputProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def initial_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, _IResolvable_a771d0ef]]]]:
        '''The initial capacity of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-initialcapacity
        '''
        result = self._values.get("initial_capacity")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def maximum_capacity(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.MaximumAllowedResourcesProperty, _IResolvable_a771d0ef]]:
        '''The maximum capacity of the application.

        This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-maximumcapacity
        '''
        result = self._values.get("maximum_capacity")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.MaximumAllowedResourcesProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        *Minimum* : 1

        *Maximum* : 64

        *Pattern* : ``^[A-Za-z0-9._\\\\/#-]+$``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnApplication.NetworkConfigurationProperty, _IResolvable_a771d0ef]]:
        '''The network configuration for customer VPC connectivity for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnApplication.NetworkConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''The tags assigned to the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def worker_type_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, _IResolvable_a771d0ef]]]]:
        '''The specification applied to each worker type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-workertypespecifications
        '''
        result = self._values.get("worker_type_specifications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, _IResolvable_a771d0ef]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()

def _typecheckingstub__a2def5a29819fba00d3e95c284e6b6ad99fecc63a7fa191864d3cece5270e800(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    release_label: builtins.str,
    type: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
    auto_start_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.AutoStartConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    auto_stop_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.AutoStopConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    image_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    initial_capacity: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    maximum_capacity: typing.Optional[typing.Union[typing.Union[CfnApplication.MaximumAllowedResourcesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    name: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_type_specifications: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358b2208ce14da0230fad65c9cdff98cbfc9e37511a9f6904f31602bbf000c55(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43f28f0192289d70abdeec853b2d1c5fd0f17ab1ab2e14ff4c40be80f7c4471c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ee5b8825364e2f73465577126d4aa57ff0dc0b62bc8692295c5b886cd55544(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55c2d5f6b1a8413abefe0e1b0b65b0e211c4f418c6dfb7bc7b48dc1a7b9150a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7023b9ac50f1930079b9c0f26ad577d3d42e1352f8276b857aa8e98526f2866a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ba22cebb5f28ac547ec1a2b1bf0d8c07bca7d2bb25df78f726a92c783d63b4(
    value: typing.Optional[typing.Union[CfnApplication.AutoStartConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d4db05cbd99642a575bfbe31cc97d31f7ebaf881eb868427a15432e59f06ff(
    value: typing.Optional[typing.Union[CfnApplication.AutoStopConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6694ffdf382c05463e35b8ba63b0f86166274b5b85e5529d6d070547ed65b616(
    value: typing.Optional[typing.Union[CfnApplication.ImageConfigurationInputProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355df0b6b1e6ec3344487bea06275b90f0f9620dc3fa44bcc3576469c3ae0ddd(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, _IResolvable_a771d0ef]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a733767df574926ee1726131c2f31033dd434daaf9d322dcc720c78a44c5867b(
    value: typing.Optional[typing.Union[CfnApplication.MaximumAllowedResourcesProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc3eeea2304b53b1e450fb562e0f145a4dda373b7ac4acfaf1d2f651080107c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c7a3716b8f4cdb5ef3aa52d4256bb49cdf1467ee5f9883b21531bded468444(
    value: typing.Optional[typing.Union[CfnApplication.NetworkConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78eadf1d334152f8023e8a94b3cd108bd99814cedd9df8975504f451aaaa317e(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, _IResolvable_a771d0ef]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370f12f1920dd05dcd2558ce09d3685ae6c995cd855a3233c85397b47794ae91(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4809d7a3c791d01aa8da83404630f9a7909e729e1eb68c5f32330abb4244f7b0(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    idle_timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15deaeb26439772f9121d7df090fd53fd7815c226cf46a8f5b4c0f9cffb98ec9(
    *,
    image_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0e5518e9aced40b236c9e7e78c240295afb3c816fbc36982bde35ad46835ba(
    *,
    key: builtins.str,
    value: typing.Union[typing.Union[CfnApplication.InitialCapacityConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f529c9b5a8cf9ab7b06b913d889b6eb3e8084e9fa03445238f18eb5ff565b57(
    *,
    worker_configuration: typing.Union[typing.Union[CfnApplication.WorkerConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    worker_count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7edeb0cc7cb49c07cb1db3e7cf8fd8924ff21c434570f205d6ca59a6f049f9(
    *,
    cpu: builtins.str,
    memory: builtins.str,
    disk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10f9f815ec2c7acc701b84605938f516db5309bcb6b5745e54e29bd6de2fd422(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d98955cc118b9648503a4d0838fa75a032a4035514fdbbbfc2b8bf1a2f85a1(
    *,
    cpu: builtins.str,
    memory: builtins.str,
    disk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__380798d888d15f4423509027789672146e3161fd11743c96996b0a954206909a(
    *,
    image_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18932d3223f2e2289dc54cd89fb0a7a296f2ee5c21c9f9b7c7ceb64759218921(
    *,
    release_label: builtins.str,
    type: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
    auto_start_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.AutoStartConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    auto_stop_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.AutoStopConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    image_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    initial_capacity: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    maximum_capacity: typing.Optional[typing.Union[typing.Union[CfnApplication.MaximumAllowedResourcesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    name: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[typing.Union[CfnApplication.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_type_specifications: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

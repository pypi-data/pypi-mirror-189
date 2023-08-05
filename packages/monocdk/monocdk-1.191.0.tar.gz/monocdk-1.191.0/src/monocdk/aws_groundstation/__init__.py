'''
# AWS::GroundStation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as groundstation
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GroundStation construct libraries](https://constructs.dev/search?q=groundstation)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GroundStation resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GroundStation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html).

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
class CfnConfig(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_groundstation.CfnConfig",
):
    '''A CloudFormation ``AWS::GroundStation::Config``.

    Creates a ``Config`` with the specified parameters.

    Config objects provide Ground Station with the details necessary in order to schedule and execute satellite contacts.

    :cloudformationResource: AWS::GroundStation::Config
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_groundstation as groundstation
        
        cfn_config = groundstation.CfnConfig(self, "MyCfnConfig",
            config_data=groundstation.CfnConfig.ConfigDataProperty(
                antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                ),
                antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                    decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                ),
                antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    ),
                    target_eirp=groundstation.CfnConfig.EirpProperty(
                        units="units",
                        value=123
                    ),
                    transmit_disabled=False
                ),
                dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                    dataflow_endpoint_name="dataflowEndpointName",
                    dataflow_endpoint_region="dataflowEndpointRegion"
                ),
                s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                    bucket_arn="bucketArn",
                    prefix="prefix",
                    role_arn="roleArn"
                ),
                tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                    autotrack="autotrack"
                ),
                uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                    antenna_uplink_config_arn="antennaUplinkConfigArn",
                    enabled=False
                )
            ),
            name="name",
        
            # the properties below are optional
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
        config_data: typing.Union[typing.Union["CfnConfig.ConfigDataProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::GroundStation::Config``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param config_data: Object containing the parameters of a config. Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.
        :param name: The name of the config object.
        :param tags: Tags assigned to a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__657c3e97ed7d45b231a24236c1cae3dca8102fb25e9f2d958c56983bacf4369b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigProps(config_data=config_data, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8704ae026161d5f282efc7f368880887d004821ba903ffbce74f9b7622897b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5f30635d8eb8952763b80a1c069ec2123de641681a0a3f5d23078f6b27daf2f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the config, such as ``arn:aws:groundstation:us-east-2:1234567890:config/tracking/9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the config, such as ``9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the config, such as ``tracking`` .

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Tags assigned to a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="configData")
    def config_data(
        self,
    ) -> typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_a771d0ef]:
        '''Object containing the parameters of a config.

        Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-configdata
        '''
        return typing.cast(typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_a771d0ef], jsii.get(self, "configData"))

    @config_data.setter
    def config_data(
        self,
        value: typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd09d2578ff00eb8423fdb785e94cafd2362719d33d9b57c7d8ec421ed2e2318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configData", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the config object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6982bee99a38dbfa5743bcf0824d49af7adabc0595f0b95b2d6ea098691c7697)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.AntennaDownlinkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"spectrum_config": "spectrumConfig"},
    )
    class AntennaDownlinkConfigProperty:
        def __init__(
            self,
            *,
            spectrum_config: typing.Optional[typing.Union[typing.Union["CfnConfig.SpectrumConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should configure an antenna for downlink during a contact.

            Use an antenna downlink config in a mission profile to receive the downlink data in raw DigIF format.

            :param spectrum_config: Defines the spectrum configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                antenna_downlink_config_property = groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c04352481a7c34a3c688e56f8318117369261927c92158d3300cb4c2542689d)
                check_type(argname="argument spectrum_config", value=spectrum_config, expected_type=type_hints["spectrum_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_a771d0ef]]:
            '''Defines the spectrum configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html#cfn-groundstation-config-antennadownlinkconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaDownlinkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decode_config": "decodeConfig",
            "demodulation_config": "demodulationConfig",
            "spectrum_config": "spectrumConfig",
        },
    )
    class AntennaDownlinkDemodDecodeConfigProperty:
        def __init__(
            self,
            *,
            decode_config: typing.Optional[typing.Union[typing.Union["CfnConfig.DecodeConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            demodulation_config: typing.Optional[typing.Union[typing.Union["CfnConfig.DemodulationConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            spectrum_config: typing.Optional[typing.Union[typing.Union["CfnConfig.SpectrumConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should configure an antenna for downlink during a contact.

            Use an antenna downlink demod decode config in a mission profile to receive the downlink data that has been demodulated and decoded.

            :param decode_config: Defines how the RF signal will be decoded.
            :param demodulation_config: Defines how the RF signal will be demodulated.
            :param spectrum_config: Defines the spectrum configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                antenna_downlink_demod_decode_config_property = groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                    decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4faf95e28d2f8ffe9bb21eec57b5a7129d3297fb344d9dc018e75d434aee790f)
                check_type(argname="argument decode_config", value=decode_config, expected_type=type_hints["decode_config"])
                check_type(argname="argument demodulation_config", value=demodulation_config, expected_type=type_hints["demodulation_config"])
                check_type(argname="argument spectrum_config", value=spectrum_config, expected_type=type_hints["spectrum_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if decode_config is not None:
                self._values["decode_config"] = decode_config
            if demodulation_config is not None:
                self._values["demodulation_config"] = demodulation_config
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config

        @builtins.property
        def decode_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.DecodeConfigProperty", _IResolvable_a771d0ef]]:
            '''Defines how the RF signal will be decoded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-decodeconfig
            '''
            result = self._values.get("decode_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.DecodeConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def demodulation_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.DemodulationConfigProperty", _IResolvable_a771d0ef]]:
            '''Defines how the RF signal will be demodulated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-demodulationconfig
            '''
            result = self._values.get("demodulation_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.DemodulationConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_a771d0ef]]:
            '''Defines the spectrum configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaDownlinkDemodDecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.AntennaUplinkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "spectrum_config": "spectrumConfig",
            "target_eirp": "targetEirp",
            "transmit_disabled": "transmitDisabled",
        },
    )
    class AntennaUplinkConfigProperty:
        def __init__(
            self,
            *,
            spectrum_config: typing.Optional[typing.Union[typing.Union["CfnConfig.UplinkSpectrumConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            target_eirp: typing.Optional[typing.Union[typing.Union["CfnConfig.EirpProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            transmit_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should configure an antenna for uplink during a contact.

            :param spectrum_config: Defines the spectrum configuration.
            :param target_eirp: The equivalent isotropically radiated power (EIRP) to use for uplink transmissions. Valid values are between 20.0 to 50.0 dBW.
            :param transmit_disabled: Whether or not uplink transmit is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                antenna_uplink_config_property = groundstation.CfnConfig.AntennaUplinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    ),
                    target_eirp=groundstation.CfnConfig.EirpProperty(
                        units="units",
                        value=123
                    ),
                    transmit_disabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__397131565634a34a48430e2550aab56d413c7ee6bb7053746f323457c20138bb)
                check_type(argname="argument spectrum_config", value=spectrum_config, expected_type=type_hints["spectrum_config"])
                check_type(argname="argument target_eirp", value=target_eirp, expected_type=type_hints["target_eirp"])
                check_type(argname="argument transmit_disabled", value=transmit_disabled, expected_type=type_hints["transmit_disabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config
            if target_eirp is not None:
                self._values["target_eirp"] = target_eirp
            if transmit_disabled is not None:
                self._values["transmit_disabled"] = transmit_disabled

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.UplinkSpectrumConfigProperty", _IResolvable_a771d0ef]]:
            '''Defines the spectrum configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.UplinkSpectrumConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def target_eirp(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.EirpProperty", _IResolvable_a771d0ef]]:
            '''The equivalent isotropically radiated power (EIRP) to use for uplink transmissions.

            Valid values are between 20.0 to 50.0 dBW.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-targeteirp
            '''
            result = self._values.get("target_eirp")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.EirpProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def transmit_disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether or not uplink transmit is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-transmitdisabled
            '''
            result = self._values.get("transmit_disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaUplinkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.ConfigDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "antenna_downlink_config": "antennaDownlinkConfig",
            "antenna_downlink_demod_decode_config": "antennaDownlinkDemodDecodeConfig",
            "antenna_uplink_config": "antennaUplinkConfig",
            "dataflow_endpoint_config": "dataflowEndpointConfig",
            "s3_recording_config": "s3RecordingConfig",
            "tracking_config": "trackingConfig",
            "uplink_echo_config": "uplinkEchoConfig",
        },
    )
    class ConfigDataProperty:
        def __init__(
            self,
            *,
            antenna_downlink_config: typing.Optional[typing.Union[typing.Union["CfnConfig.AntennaDownlinkConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            antenna_downlink_demod_decode_config: typing.Optional[typing.Union[typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            antenna_uplink_config: typing.Optional[typing.Union[typing.Union["CfnConfig.AntennaUplinkConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            dataflow_endpoint_config: typing.Optional[typing.Union[typing.Union["CfnConfig.DataflowEndpointConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            s3_recording_config: typing.Optional[typing.Union[typing.Union["CfnConfig.S3RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            tracking_config: typing.Optional[typing.Union[typing.Union["CfnConfig.TrackingConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            uplink_echo_config: typing.Optional[typing.Union[typing.Union["CfnConfig.UplinkEchoConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Config objects provide information to Ground Station about how to configure the antenna and how data flows during a contact.

            :param antenna_downlink_config: Provides information for an antenna downlink config object. Antenna downlink config objects are used to provide parameters for downlinks where no demodulation or decoding is performed by Ground Station (RF over IP downlinks).
            :param antenna_downlink_demod_decode_config: Provides information for a downlink demod decode config object. Downlink demod decode config objects are used to provide parameters for downlinks where the Ground Station service will demodulate and decode the downlinked data.
            :param antenna_uplink_config: Provides information for an uplink config object. Uplink config objects are used to provide parameters for uplink contacts.
            :param dataflow_endpoint_config: Provides information for a dataflow endpoint config object. Dataflow endpoint config objects are used to provide parameters about which IP endpoint(s) to use during a contact. Dataflow endpoints are where Ground Station sends data during a downlink contact and where Ground Station receives data to send to the satellite during an uplink contact.
            :param s3_recording_config: Provides information for an S3 recording config object. S3 recording config objects are used to provide parameters for S3 recording during downlink contacts.
            :param tracking_config: Provides information for a tracking config object. Tracking config objects are used to provide parameters about how to track the satellite through the sky during a contact.
            :param uplink_echo_config: Provides information for an uplink echo config object. Uplink echo config objects are used to provide parameters for uplink echo during uplink contacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                config_data_property = groundstation.CfnConfig.ConfigDataProperty(
                    antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                        decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        ),
                        target_eirp=groundstation.CfnConfig.EirpProperty(
                            units="units",
                            value=123
                        ),
                        transmit_disabled=False
                    ),
                    dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                        dataflow_endpoint_name="dataflowEndpointName",
                        dataflow_endpoint_region="dataflowEndpointRegion"
                    ),
                    s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                        bucket_arn="bucketArn",
                        prefix="prefix",
                        role_arn="roleArn"
                    ),
                    tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                        autotrack="autotrack"
                    ),
                    uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                        antenna_uplink_config_arn="antennaUplinkConfigArn",
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15b22aa96006504c7fec0cf4e75d06fb8f9e7128df24bd581d183c54387f9378)
                check_type(argname="argument antenna_downlink_config", value=antenna_downlink_config, expected_type=type_hints["antenna_downlink_config"])
                check_type(argname="argument antenna_downlink_demod_decode_config", value=antenna_downlink_demod_decode_config, expected_type=type_hints["antenna_downlink_demod_decode_config"])
                check_type(argname="argument antenna_uplink_config", value=antenna_uplink_config, expected_type=type_hints["antenna_uplink_config"])
                check_type(argname="argument dataflow_endpoint_config", value=dataflow_endpoint_config, expected_type=type_hints["dataflow_endpoint_config"])
                check_type(argname="argument s3_recording_config", value=s3_recording_config, expected_type=type_hints["s3_recording_config"])
                check_type(argname="argument tracking_config", value=tracking_config, expected_type=type_hints["tracking_config"])
                check_type(argname="argument uplink_echo_config", value=uplink_echo_config, expected_type=type_hints["uplink_echo_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if antenna_downlink_config is not None:
                self._values["antenna_downlink_config"] = antenna_downlink_config
            if antenna_downlink_demod_decode_config is not None:
                self._values["antenna_downlink_demod_decode_config"] = antenna_downlink_demod_decode_config
            if antenna_uplink_config is not None:
                self._values["antenna_uplink_config"] = antenna_uplink_config
            if dataflow_endpoint_config is not None:
                self._values["dataflow_endpoint_config"] = dataflow_endpoint_config
            if s3_recording_config is not None:
                self._values["s3_recording_config"] = s3_recording_config
            if tracking_config is not None:
                self._values["tracking_config"] = tracking_config
            if uplink_echo_config is not None:
                self._values["uplink_echo_config"] = uplink_echo_config

        @builtins.property
        def antenna_downlink_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.AntennaDownlinkConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for an antenna downlink config object.

            Antenna downlink config objects are used to provide parameters for downlinks where no demodulation or decoding is performed by Ground Station (RF over IP downlinks).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkconfig
            '''
            result = self._values.get("antenna_downlink_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.AntennaDownlinkConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def antenna_downlink_demod_decode_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for a downlink demod decode config object.

            Downlink demod decode config objects are used to provide parameters for downlinks where the Ground Station service will demodulate and decode the downlinked data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkdemoddecodeconfig
            '''
            result = self._values.get("antenna_downlink_demod_decode_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def antenna_uplink_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.AntennaUplinkConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for an uplink config object.

            Uplink config objects are used to provide parameters for uplink contacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennauplinkconfig
            '''
            result = self._values.get("antenna_uplink_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.AntennaUplinkConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def dataflow_endpoint_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.DataflowEndpointConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for a dataflow endpoint config object.

            Dataflow endpoint config objects are used to provide parameters about which IP endpoint(s) to use during a contact. Dataflow endpoints are where Ground Station sends data during a downlink contact and where Ground Station receives data to send to the satellite during an uplink contact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-dataflowendpointconfig
            '''
            result = self._values.get("dataflow_endpoint_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.DataflowEndpointConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def s3_recording_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.S3RecordingConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for an S3 recording config object.

            S3 recording config objects are used to provide parameters for S3 recording during downlink contacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-s3recordingconfig
            '''
            result = self._values.get("s3_recording_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.S3RecordingConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def tracking_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.TrackingConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for a tracking config object.

            Tracking config objects are used to provide parameters about how to track the satellite through the sky during a contact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-trackingconfig
            '''
            result = self._values.get("tracking_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.TrackingConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def uplink_echo_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.UplinkEchoConfigProperty", _IResolvable_a771d0ef]]:
            '''Provides information for an uplink echo config object.

            Uplink echo config objects are used to provide parameters for uplink echo during uplink contacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-uplinkechoconfig
            '''
            result = self._values.get("uplink_echo_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.UplinkEchoConfigProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.DataflowEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dataflow_endpoint_name": "dataflowEndpointName",
            "dataflow_endpoint_region": "dataflowEndpointRegion",
        },
    )
    class DataflowEndpointConfigProperty:
        def __init__(
            self,
            *,
            dataflow_endpoint_name: typing.Optional[builtins.str] = None,
            dataflow_endpoint_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information to AWS Ground Station about which IP endpoints to use during a contact.

            :param dataflow_endpoint_name: The name of the dataflow endpoint to use during contacts.
            :param dataflow_endpoint_region: The region of the dataflow endpoint to use during contacts. When omitted, Ground Station will use the region of the contact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                dataflow_endpoint_config_property = groundstation.CfnConfig.DataflowEndpointConfigProperty(
                    dataflow_endpoint_name="dataflowEndpointName",
                    dataflow_endpoint_region="dataflowEndpointRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7d2f55bc531770d611617be39d5f269f70f39b8bee9c9389cb21ca8e3f3f821)
                check_type(argname="argument dataflow_endpoint_name", value=dataflow_endpoint_name, expected_type=type_hints["dataflow_endpoint_name"])
                check_type(argname="argument dataflow_endpoint_region", value=dataflow_endpoint_region, expected_type=type_hints["dataflow_endpoint_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dataflow_endpoint_name is not None:
                self._values["dataflow_endpoint_name"] = dataflow_endpoint_name
            if dataflow_endpoint_region is not None:
                self._values["dataflow_endpoint_region"] = dataflow_endpoint_region

        @builtins.property
        def dataflow_endpoint_name(self) -> typing.Optional[builtins.str]:
            '''The name of the dataflow endpoint to use during contacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname
            '''
            result = self._values.get("dataflow_endpoint_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dataflow_endpoint_region(self) -> typing.Optional[builtins.str]:
            '''The region of the dataflow endpoint to use during contacts.

            When omitted, Ground Station will use the region of the contact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion
            '''
            result = self._values.get("dataflow_endpoint_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.DecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"unvalidated_json": "unvalidatedJson"},
    )
    class DecodeConfigProperty:
        def __init__(
            self,
            *,
            unvalidated_json: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines decoding settings.

            :param unvalidated_json: The decoding settings are in JSON format and define a set of steps to perform to decode the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                decode_config_property = groundstation.CfnConfig.DecodeConfigProperty(
                    unvalidated_json="unvalidatedJson"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86e607cadb9fbc58a2a4f7c79b3882b1ed43311d63e92beb7b12bc5cd79a285b)
                check_type(argname="argument unvalidated_json", value=unvalidated_json, expected_type=type_hints["unvalidated_json"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if unvalidated_json is not None:
                self._values["unvalidated_json"] = unvalidated_json

        @builtins.property
        def unvalidated_json(self) -> typing.Optional[builtins.str]:
            '''The decoding settings are in JSON format and define a set of steps to perform to decode the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html#cfn-groundstation-config-decodeconfig-unvalidatedjson
            '''
            result = self._values.get("unvalidated_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.DemodulationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"unvalidated_json": "unvalidatedJson"},
    )
    class DemodulationConfigProperty:
        def __init__(
            self,
            *,
            unvalidated_json: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines demodulation settings.

            :param unvalidated_json: The demodulation settings are in JSON format and define parameters for demodulation, for example which modulation scheme (e.g. PSK, QPSK, etc.) and matched filter to use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                demodulation_config_property = groundstation.CfnConfig.DemodulationConfigProperty(
                    unvalidated_json="unvalidatedJson"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccaa56ccbd83a420e521d2cb4523d49cfa112e2fd415cfc5e19fdf0b95d45f6b)
                check_type(argname="argument unvalidated_json", value=unvalidated_json, expected_type=type_hints["unvalidated_json"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if unvalidated_json is not None:
                self._values["unvalidated_json"] = unvalidated_json

        @builtins.property
        def unvalidated_json(self) -> typing.Optional[builtins.str]:
            '''The demodulation settings are in JSON format and define parameters for demodulation, for example which modulation scheme (e.g. PSK, QPSK, etc.) and matched filter to use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html#cfn-groundstation-config-demodulationconfig-unvalidatedjson
            '''
            result = self._values.get("unvalidated_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DemodulationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.EirpProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class EirpProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines an equivalent isotropically radiated power (EIRP).

            :param units: The units of the EIRP.
            :param value: The value of the EIRP. Valid values are between 20.0 to 50.0 dBW.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                eirp_property = groundstation.CfnConfig.EirpProperty(
                    units="units",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58a98a3bde417e64e3e4b176491780cc578cd3ee8c4faaf84d7802297d8cd75f)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''The units of the EIRP.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value of the EIRP.

            Valid values are between 20.0 to 50.0 dBW.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EirpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.FrequencyBandwidthProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class FrequencyBandwidthProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines a bandwidth.

            :param units: The units of the bandwidth.
            :param value: The value of the bandwidth. AWS Ground Station currently has the following bandwidth limitations:. - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz. - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz. - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                frequency_bandwidth_property = groundstation.CfnConfig.FrequencyBandwidthProperty(
                    units="units",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__302f13976c3c3d7b6f0326f26b09f77adaa23fe64a67a999ec3f548217a3df76)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''The units of the bandwidth.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value of the bandwidth. AWS Ground Station currently has the following bandwidth limitations:.

            - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz.
            - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz.
            - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrequencyBandwidthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.FrequencyProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class FrequencyProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines a frequency.

            :param units: The units of the frequency.
            :param value: The value of the frequency. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                frequency_property = groundstation.CfnConfig.FrequencyProperty(
                    units="units",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac4c98a56bc0e5c59cc6da2fd0e58e8b7eef163bad672fffa982dcd2b5844b78)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''The units of the frequency.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value of the frequency.

            Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrequencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.S3RecordingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "prefix": "prefix",
            "role_arn": "roleArn",
        },
    )
    class S3RecordingConfigProperty:
        def __init__(
            self,
            *,
            bucket_arn: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should save downlink data to S3.

            :param bucket_arn: S3 Bucket where the data is written. The name of the S3 Bucket provided must begin with ``aws-groundstation`` .
            :param prefix: The prefix of the S3 data object. If you choose to use any optional keys for substitution, these values will be replaced with the corresponding information from your contact details. For example, a prefix of ``{satellite_id}/{year}/{month}/{day}/`` will replaced with ``fake_satellite_id/2021/01/10/`` *Optional keys for substitution* : ``{satellite_id}`` | ``{config-name}`` | ``{config-id}`` | ``{year}`` | ``{month}`` | ``{day}``
            :param role_arn: Defines the ARN of the role assumed for putting archives to S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                s3_recording_config_property = groundstation.CfnConfig.S3RecordingConfigProperty(
                    bucket_arn="bucketArn",
                    prefix="prefix",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__493cf27eca919ee7b66301aaccbfd2cc027645907a126e31271631eb96d102ea)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_arn is not None:
                self._values["bucket_arn"] = bucket_arn
            if prefix is not None:
                self._values["prefix"] = prefix
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def bucket_arn(self) -> typing.Optional[builtins.str]:
            '''S3 Bucket where the data is written.

            The name of the S3 Bucket provided must begin with ``aws-groundstation`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-bucketarn
            '''
            result = self._values.get("bucket_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix of the S3 data object.

            If you choose to use any optional keys for substitution, these values will be replaced with the corresponding information from your contact details. For example, a prefix of ``{satellite_id}/{year}/{month}/{day}/`` will replaced with ``fake_satellite_id/2021/01/10/``

            *Optional keys for substitution* : ``{satellite_id}`` | ``{config-name}`` | ``{config-id}`` | ``{year}`` | ``{month}`` | ``{day}``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Defines the ARN of the role assumed for putting archives to S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3RecordingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.SpectrumConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bandwidth": "bandwidth",
            "center_frequency": "centerFrequency",
            "polarization": "polarization",
        },
    )
    class SpectrumConfigProperty:
        def __init__(
            self,
            *,
            bandwidth: typing.Optional[typing.Union[typing.Union["CfnConfig.FrequencyBandwidthProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            center_frequency: typing.Optional[typing.Union[typing.Union["CfnConfig.FrequencyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            polarization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a spectrum.

            :param bandwidth: The bandwidth of the spectrum. AWS Ground Station currently has the following bandwidth limitations:. - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz. - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz. - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.
            :param center_frequency: The center frequency of the spectrum. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.
            :param polarization: The polarization of the spectrum. Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` . Capturing both ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` polarization requires two separate configs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                spectrum_config_property = groundstation.CfnConfig.SpectrumConfigProperty(
                    bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                        units="units",
                        value=123
                    ),
                    center_frequency=groundstation.CfnConfig.FrequencyProperty(
                        units="units",
                        value=123
                    ),
                    polarization="polarization"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9adb807c6b9574ca840386f2cd60c26bf54d2807b578363b02a6755e987ed3d2)
                check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
                check_type(argname="argument center_frequency", value=center_frequency, expected_type=type_hints["center_frequency"])
                check_type(argname="argument polarization", value=polarization, expected_type=type_hints["polarization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bandwidth is not None:
                self._values["bandwidth"] = bandwidth
            if center_frequency is not None:
                self._values["center_frequency"] = center_frequency
            if polarization is not None:
                self._values["polarization"] = polarization

        @builtins.property
        def bandwidth(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.FrequencyBandwidthProperty", _IResolvable_a771d0ef]]:
            '''The bandwidth of the spectrum. AWS Ground Station currently has the following bandwidth limitations:.

            - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz.
            - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz.
            - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-bandwidth
            '''
            result = self._values.get("bandwidth")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.FrequencyBandwidthProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def center_frequency(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_a771d0ef]]:
            '''The center frequency of the spectrum.

            Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-centerfrequency
            '''
            result = self._values.get("center_frequency")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def polarization(self) -> typing.Optional[builtins.str]:
            '''The polarization of the spectrum.

            Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` . Capturing both ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` polarization requires two separate configs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-polarization
            '''
            result = self._values.get("polarization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpectrumConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.TrackingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"autotrack": "autotrack"},
    )
    class TrackingConfigProperty:
        def __init__(self, *, autotrack: typing.Optional[builtins.str] = None) -> None:
            '''Provides information about how AWS Ground Station should track the satellite through the sky during a contact.

            :param autotrack: Specifies whether or not to use autotrack. ``REMOVED`` specifies that program track should only be used during the contact. ``PREFERRED`` specifies that autotracking is preferred during the contact but fallback to program track if the signal is lost. ``REQUIRED`` specifies that autotracking is required during the contact and not to use program track if the signal is lost.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                tracking_config_property = groundstation.CfnConfig.TrackingConfigProperty(
                    autotrack="autotrack"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a649cc24680f06b905daee3d3ae4d959095ba1de230c27c2e50aa6c9b498a949)
                check_type(argname="argument autotrack", value=autotrack, expected_type=type_hints["autotrack"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if autotrack is not None:
                self._values["autotrack"] = autotrack

        @builtins.property
        def autotrack(self) -> typing.Optional[builtins.str]:
            '''Specifies whether or not to use autotrack.

            ``REMOVED`` specifies that program track should only be used during the contact. ``PREFERRED`` specifies that autotracking is preferred during the contact but fallback to program track if the signal is lost. ``REQUIRED`` specifies that autotracking is required during the contact and not to use program track if the signal is lost.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html#cfn-groundstation-config-trackingconfig-autotrack
            '''
            result = self._values.get("autotrack")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.UplinkEchoConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "antenna_uplink_config_arn": "antennaUplinkConfigArn",
            "enabled": "enabled",
        },
    )
    class UplinkEchoConfigProperty:
        def __init__(
            self,
            *,
            antenna_uplink_config_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should echo back uplink transmissions to a dataflow endpoint.

            :param antenna_uplink_config_arn: Defines the ARN of the uplink config to echo back to a dataflow endpoint.
            :param enabled: Whether or not uplink echo is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                uplink_echo_config_property = groundstation.CfnConfig.UplinkEchoConfigProperty(
                    antenna_uplink_config_arn="antennaUplinkConfigArn",
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a5dde389e04804c15edf5b5c6d93e3ebaf320af28e1ae9dfac4ca6d52f548d9)
                check_type(argname="argument antenna_uplink_config_arn", value=antenna_uplink_config_arn, expected_type=type_hints["antenna_uplink_config_arn"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if antenna_uplink_config_arn is not None:
                self._values["antenna_uplink_config_arn"] = antenna_uplink_config_arn
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def antenna_uplink_config_arn(self) -> typing.Optional[builtins.str]:
            '''Defines the ARN of the uplink config to echo back to a dataflow endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn
            '''
            result = self._values.get("antenna_uplink_config_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether or not uplink echo is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UplinkEchoConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnConfig.UplinkSpectrumConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "center_frequency": "centerFrequency",
            "polarization": "polarization",
        },
    )
    class UplinkSpectrumConfigProperty:
        def __init__(
            self,
            *,
            center_frequency: typing.Optional[typing.Union[typing.Union["CfnConfig.FrequencyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            polarization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a uplink spectrum.

            :param center_frequency: The center frequency of the spectrum. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.
            :param polarization: The polarization of the spectrum. Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                uplink_spectrum_config_property = groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                    center_frequency=groundstation.CfnConfig.FrequencyProperty(
                        units="units",
                        value=123
                    ),
                    polarization="polarization"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a731e0bfae50c5135fc115de0242f154c9a6feb5c403997dbfbdd381c811bd0)
                check_type(argname="argument center_frequency", value=center_frequency, expected_type=type_hints["center_frequency"])
                check_type(argname="argument polarization", value=polarization, expected_type=type_hints["polarization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if center_frequency is not None:
                self._values["center_frequency"] = center_frequency
            if polarization is not None:
                self._values["polarization"] = polarization

        @builtins.property
        def center_frequency(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_a771d0ef]]:
            '''The center frequency of the spectrum.

            Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-centerfrequency
            '''
            result = self._values.get("center_frequency")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def polarization(self) -> typing.Optional[builtins.str]:
            '''The polarization of the spectrum.

            Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-polarization
            '''
            result = self._values.get("polarization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UplinkSpectrumConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_groundstation.CfnConfigProps",
    jsii_struct_bases=[],
    name_mapping={"config_data": "configData", "name": "name", "tags": "tags"},
)
class CfnConfigProps:
    def __init__(
        self,
        *,
        config_data: typing.Union[typing.Union[CfnConfig.ConfigDataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfig``.

        :param config_data: Object containing the parameters of a config. Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.
        :param name: The name of the config object.
        :param tags: Tags assigned to a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_groundstation as groundstation
            
            cfn_config_props = groundstation.CfnConfigProps(
                config_data=groundstation.CfnConfig.ConfigDataProperty(
                    antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                        decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        ),
                        target_eirp=groundstation.CfnConfig.EirpProperty(
                            units="units",
                            value=123
                        ),
                        transmit_disabled=False
                    ),
                    dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                        dataflow_endpoint_name="dataflowEndpointName",
                        dataflow_endpoint_region="dataflowEndpointRegion"
                    ),
                    s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                        bucket_arn="bucketArn",
                        prefix="prefix",
                        role_arn="roleArn"
                    ),
                    tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                        autotrack="autotrack"
                    ),
                    uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                        antenna_uplink_config_arn="antennaUplinkConfigArn",
                        enabled=False
                    )
                ),
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32beda0b8f3cd1c907abe93c5126f04185f8e2c4b04e908d717777df4aa00342)
            check_type(argname="argument config_data", value=config_data, expected_type=type_hints["config_data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_data": config_data,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def config_data(
        self,
    ) -> typing.Union[CfnConfig.ConfigDataProperty, _IResolvable_a771d0ef]:
        '''Object containing the parameters of a config.

        Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-configdata
        '''
        result = self._values.get("config_data")
        assert result is not None, "Required property 'config_data' is missing"
        return typing.cast(typing.Union[CfnConfig.ConfigDataProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the config object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Tags assigned to a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDataflowEndpointGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_groundstation.CfnDataflowEndpointGroup",
):
    '''A CloudFormation ``AWS::GroundStation::DataflowEndpointGroup``.

    Creates a Dataflow Endpoint Group request.

    Dataflow endpoint groups contain a list of endpoints. When the name of a dataflow endpoint group is specified in a mission profile, the Ground Station service will connect to the endpoints and flow data during a contact.

    For more information about dataflow endpoint groups, see `Dataflow Endpoint Groups <https://docs.aws.amazon.com/ground-station/latest/ug/dataflowendpointgroups.html>`_ .

    :cloudformationResource: AWS::GroundStation::DataflowEndpointGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_groundstation as groundstation
        
        cfn_dataflow_endpoint_group = groundstation.CfnDataflowEndpointGroup(self, "MyCfnDataflowEndpointGroup",
            endpoint_details=[groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                    address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    ),
                    mtu=123,
                    name="name"
                ),
                security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )],
        
            # the properties below are optional
            contact_post_pass_duration_seconds=123,
            contact_pre_pass_duration_seconds=123,
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
        endpoint_details: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::GroundStation::DataflowEndpointGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_details: List of Endpoint Details, containing address and port for each endpoint.
        :param contact_post_pass_duration_seconds: ``AWS::GroundStation::DataflowEndpointGroup.ContactPostPassDurationSeconds``.
        :param contact_pre_pass_duration_seconds: ``AWS::GroundStation::DataflowEndpointGroup.ContactPrePassDurationSeconds``.
        :param tags: Tags assigned to a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__006fc29ed40400465da28e607e91916cf4754a95601d4906ff2f879def4da0cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataflowEndpointGroupProps(
            endpoint_details=endpoint_details,
            contact_post_pass_duration_seconds=contact_post_pass_duration_seconds,
            contact_pre_pass_duration_seconds=contact_pre_pass_duration_seconds,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d626b2ba1439f3723650348bfaabb073f29787e7b2f674860f4a702f9210728)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb4eefd82a36eb2eea3769307c4fa3d3e7ba27a68d1a08ab235150c7a1e3b696)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the dataflow endpoint group, such as ``arn:aws:groundstation:us-east-2:1234567890:dataflow-endpoint-group/9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''UUID of a dataflow endpoint group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Tags assigned to a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_a771d0ef]]]:
        '''List of Endpoint Details, containing address and port for each endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-endpointdetails
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_a771d0ef]]], jsii.get(self, "endpointDetails"))

    @endpoint_details.setter
    def endpoint_details(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1180b67cd56c498b0a621032a3ada07d925e7da5eb565210edcbc7500a9c50d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointDetails", value)

    @builtins.property
    @jsii.member(jsii_name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::DataflowEndpointGroup.ContactPostPassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPostPassDurationSeconds"))

    @contact_post_pass_duration_seconds.setter
    def contact_post_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d9d71e3873a3732752d7b419aa97edc3cfb6c69c75ae0cd1293332d32a9eee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPostPassDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::DataflowEndpointGroup.ContactPrePassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPrePassDurationSeconds"))

    @contact_pre_pass_duration_seconds.setter
    def contact_pre_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd20705e1c88d244943b3068d0fae6005b550f99c36cde62ac7b7aebaa407503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPrePassDurationSeconds", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "mtu": "mtu", "name": "name"},
    )
    class DataflowEndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[typing.Union[typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            mtu: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information such as socket address and name that defines an endpoint.

            :param address: The address and port of an endpoint.
            :param mtu: Maximum transmission unit (MTU) size in bytes of a dataflow endpoint. Valid values are between 1400 and 1500. A default value of 1500 is used if not set.
            :param name: The endpoint name. When listing available contacts for a satellite, Ground Station searches for a dataflow endpoint whose name matches the value specified by the dataflow endpoint config of the selected mission profile. If no matching dataflow endpoints are found then Ground Station will not display any available contacts for the satellite.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                dataflow_endpoint_property = groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                    address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    ),
                    mtu=123,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3701331129f17bedee284cd2993120a37fc6e66e02af9245cfec41493ae81a1)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if mtu is not None:
                self._values["mtu"] = mtu
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def address(
            self,
        ) -> typing.Optional[typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", _IResolvable_a771d0ef]]:
            '''The address and port of an endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def mtu(self) -> typing.Optional[jsii.Number]:
            '''Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.

            Valid values are between 1400 and 1500. A default value of 1500 is used if not set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-mtu
            '''
            result = self._values.get("mtu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The endpoint name.

            When listing available contacts for a satellite, Ground Station searches for a dataflow endpoint whose name matches the value specified by the dataflow endpoint config of the selected mission profile. If no matching dataflow endpoints are found then Ground Station will not display any available contacts for the satellite.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint", "security_details": "securityDetails"},
    )
    class EndpointDetailsProperty:
        def __init__(
            self,
            *,
            endpoint: typing.Optional[typing.Union[typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            security_details: typing.Optional[typing.Union[typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The security details and endpoint information.

            :param endpoint: Information about the endpoint such as name and the endpoint address.
            :param security_details: The role ARN, and IDs for security groups and subnets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                endpoint_details_property = groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                    endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                        address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        ),
                        mtu=123,
                        name="name"
                    ),
                    security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4423867d9810d2ad9ef03d9eda98498ecb5952ecddebda47fac09848ff958bb2)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument security_details", value=security_details, expected_type=type_hints["security_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if security_details is not None:
                self._values["security_details"] = security_details

        @builtins.property
        def endpoint(
            self,
        ) -> typing.Optional[typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", _IResolvable_a771d0ef]]:
            '''Information about the endpoint such as name and the endpoint address.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def security_details(
            self,
        ) -> typing.Optional[typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", _IResolvable_a771d0ef]]:
            '''The role ARN, and IDs for security groups and subnets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails
            '''
            result = self._values.get("security_details")
            return typing.cast(typing.Optional[typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class SecurityDetailsProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Information about IAM roles, subnets, and security groups needed for this DataflowEndpointGroup.

            :param role_arn: The ARN of a role which Ground Station has permission to assume, such as ``arn:aws:iam::1234567890:role/DataDeliveryServiceRole`` . Ground Station will assume this role and create an ENI in your VPC on the specified subnet upon creation of a dataflow endpoint group. This ENI is used as the ingress/egress point for data streamed during a satellite contact.
            :param security_group_ids: The security group Ids of the security role, such as ``sg-1234567890abcdef0`` .
            :param subnet_ids: The subnet Ids of the security details, such as ``subnet-12345678`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                security_details_property = groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af1d80d40b717dc3d03e47a8c010c25af557c966752a3bfca4afd4fda080dc6e)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of a role which Ground Station has permission to assume, such as ``arn:aws:iam::1234567890:role/DataDeliveryServiceRole`` .

            Ground Station will assume this role and create an ENI in your VPC on the specified subnet upon creation of a dataflow endpoint group. This ENI is used as the ingress/egress point for data streamed during a satellite contact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security group Ids of the security role, such as ``sg-1234567890abcdef0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The subnet Ids of the security details, such as ``subnet-12345678`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnDataflowEndpointGroup.SocketAddressProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "port": "port"},
    )
    class SocketAddressProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The address of the endpoint, such as ``192.168.1.1`` .

            :param name: The name of the endpoint, such as ``Endpoint 1`` .
            :param port: The port of the endpoint, such as ``55888`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                socket_address_property = groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                    name="name",
                    port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3edbe1e795e1837558a4cc5dc6918ae06d74ee6eb6b216a7b7f1107537c1ece)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the endpoint, such as ``Endpoint 1`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port of the endpoint, such as ``55888`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SocketAddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_groundstation.CfnDataflowEndpointGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_details": "endpointDetails",
        "contact_post_pass_duration_seconds": "contactPostPassDurationSeconds",
        "contact_pre_pass_duration_seconds": "contactPrePassDurationSeconds",
        "tags": "tags",
    },
)
class CfnDataflowEndpointGroupProps:
    def __init__(
        self,
        *,
        endpoint_details: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataflowEndpointGroup``.

        :param endpoint_details: List of Endpoint Details, containing address and port for each endpoint.
        :param contact_post_pass_duration_seconds: ``AWS::GroundStation::DataflowEndpointGroup.ContactPostPassDurationSeconds``.
        :param contact_pre_pass_duration_seconds: ``AWS::GroundStation::DataflowEndpointGroup.ContactPrePassDurationSeconds``.
        :param tags: Tags assigned to a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_groundstation as groundstation
            
            cfn_dataflow_endpoint_group_props = groundstation.CfnDataflowEndpointGroupProps(
                endpoint_details=[groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                    endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                        address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        ),
                        mtu=123,
                        name="name"
                    ),
                    security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )],
            
                # the properties below are optional
                contact_post_pass_duration_seconds=123,
                contact_pre_pass_duration_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba30a4da161078026e6d76116bc97f1021d6c78718d529c9d25544e7cc607b76)
            check_type(argname="argument endpoint_details", value=endpoint_details, expected_type=type_hints["endpoint_details"])
            check_type(argname="argument contact_post_pass_duration_seconds", value=contact_post_pass_duration_seconds, expected_type=type_hints["contact_post_pass_duration_seconds"])
            check_type(argname="argument contact_pre_pass_duration_seconds", value=contact_pre_pass_duration_seconds, expected_type=type_hints["contact_pre_pass_duration_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_details": endpoint_details,
        }
        if contact_post_pass_duration_seconds is not None:
            self._values["contact_post_pass_duration_seconds"] = contact_post_pass_duration_seconds
        if contact_pre_pass_duration_seconds is not None:
            self._values["contact_pre_pass_duration_seconds"] = contact_pre_pass_duration_seconds
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_details(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, _IResolvable_a771d0ef]]]:
        '''List of Endpoint Details, containing address and port for each endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-endpointdetails
        '''
        result = self._values.get("endpoint_details")
        assert result is not None, "Required property 'endpoint_details' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::DataflowEndpointGroup.ContactPostPassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds
        '''
        result = self._values.get("contact_post_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::DataflowEndpointGroup.ContactPrePassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds
        '''
        result = self._values.get("contact_pre_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Tags assigned to a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataflowEndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnMissionProfile(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_groundstation.CfnMissionProfile",
):
    '''A CloudFormation ``AWS::GroundStation::MissionProfile``.

    Mission profiles specify parameters and provide references to config objects to define how Ground Station lists and executes contacts.

    :cloudformationResource: AWS::GroundStation::MissionProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_groundstation as groundstation
        
        cfn_mission_profile = groundstation.CfnMissionProfile(self, "MyCfnMissionProfile",
            dataflow_edges=[groundstation.CfnMissionProfile.DataflowEdgeProperty(
                destination="destination",
                source="source"
            )],
            minimum_viable_contact_duration_seconds=123,
            name="name",
            tracking_config_arn="trackingConfigArn",
        
            # the properties below are optional
            contact_post_pass_duration_seconds=123,
            contact_pre_pass_duration_seconds=123,
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
        dataflow_edges: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnMissionProfile.DataflowEdgeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
        minimum_viable_contact_duration_seconds: jsii.Number,
        name: builtins.str,
        tracking_config_arn: builtins.str,
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::GroundStation::MissionProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dataflow_edges: A list containing lists of config ARNs. Each list of config ARNs is an edge, with a "from" config and a "to" config.
        :param minimum_viable_contact_duration_seconds: Minimum length of a contact in seconds that Ground Station will return when listing contacts. Ground Station will not return contacts shorter than this duration.
        :param name: The name of the mission profile.
        :param tracking_config_arn: The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.
        :param contact_post_pass_duration_seconds: Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param contact_pre_pass_duration_seconds: Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param tags: Tags assigned to the mission profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__033b90ee689d77aa5132e8b009b9a4be1cc6de9db33b8649108eabd7064b0f2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMissionProfileProps(
            dataflow_edges=dataflow_edges,
            minimum_viable_contact_duration_seconds=minimum_viable_contact_duration_seconds,
            name=name,
            tracking_config_arn=tracking_config_arn,
            contact_post_pass_duration_seconds=contact_post_pass_duration_seconds,
            contact_pre_pass_duration_seconds=contact_pre_pass_duration_seconds,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__718eddf91282965b494b2a28d0ccd5f89daf7e71ac877b8bd2508f64dec39770)
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
            type_hints = typing.get_type_hints(_typecheckingstub__10dfc0b338ca4bd2816c4f50a88c90905f6ed88321cdcbb069bcd2dccc27e42f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the mission profile, such as ``arn:aws:groundstation:us-east-2:1234567890:mission-profile/9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the mission profile, such as ``9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRegion")
    def attr_region(self) -> builtins.str:
        '''The region of the mission profile.

        :cloudformationAttribute: Region
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Tags assigned to the mission profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dataflowEdges")
    def dataflow_edges(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_a771d0ef]]]:
        '''A list containing lists of config ARNs.

        Each list of config ARNs is an edge, with a "from" config and a "to" config.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-dataflowedges
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_a771d0ef]]], jsii.get(self, "dataflowEdges"))

    @dataflow_edges.setter
    def dataflow_edges(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43d40e2eaae9ea126000ebc198ca2dabb658a3794469f9d2205bc6214f96e814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataflowEdges", value)

    @builtins.property
    @jsii.member(jsii_name="minimumViableContactDurationSeconds")
    def minimum_viable_contact_duration_seconds(self) -> jsii.Number:
        '''Minimum length of a contact in seconds that Ground Station will return when listing contacts.

        Ground Station will not return contacts shorter than this duration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds
        '''
        return typing.cast(jsii.Number, jsii.get(self, "minimumViableContactDurationSeconds"))

    @minimum_viable_contact_duration_seconds.setter
    def minimum_viable_contact_duration_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__732a154dbd945eeedeb2e1b62ac2052ecea135cbeb02876105d6bb3574c3b4fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumViableContactDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the mission profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90173731028b0745472ef1fc90bfd514697f8875b84a1a593c2fb786e61b6c8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="trackingConfigArn")
    def tracking_config_arn(self) -> builtins.str:
        '''The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-trackingconfigarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "trackingConfigArn"))

    @tracking_config_arn.setter
    def tracking_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24cffb024ad13354281b3df894b8c5390976e4a265feb40423ae0469667253ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished.

        For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactpostpassdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPostPassDurationSeconds"))

    @contact_post_pass_duration_seconds.setter
    def contact_post_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b56f1c27068b271741503ff36e3447ebb37613d7f295b15ed8e603c73b9071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPostPassDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass.

        For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactprepassdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPrePassDurationSeconds"))

    @contact_pre_pass_duration_seconds.setter
    def contact_pre_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__834ee5a024189d41b5919c1289b90ea43f6bd3cdca2ec26d6345163b63d05afb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPrePassDurationSeconds", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_groundstation.CfnMissionProfile.DataflowEdgeProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class DataflowEdgeProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A dataflow edge defines from where and to where data will flow during a contact.

            :param destination: The ARN of the destination for this dataflow edge. For example, specify the ARN of a dataflow endpoint config for a downlink edge or an antenna uplink config for an uplink edge.
            :param source: The ARN of the source for this dataflow edge. For example, specify the ARN of an antenna downlink config for a downlink edge or a dataflow endpoint config for an uplink edge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_groundstation as groundstation
                
                dataflow_edge_property = groundstation.CfnMissionProfile.DataflowEdgeProperty(
                    destination="destination",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0dde948392439aff4872a263d6f4bd715d1f43acd63de856a2f433886c7ee99)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The ARN of the destination for this dataflow edge.

            For example, specify the ARN of a dataflow endpoint config for a downlink edge or an antenna uplink config for an uplink edge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''The ARN of the source for this dataflow edge.

            For example, specify the ARN of an antenna downlink config for a downlink edge or a dataflow endpoint config for an uplink edge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEdgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_groundstation.CfnMissionProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataflow_edges": "dataflowEdges",
        "minimum_viable_contact_duration_seconds": "minimumViableContactDurationSeconds",
        "name": "name",
        "tracking_config_arn": "trackingConfigArn",
        "contact_post_pass_duration_seconds": "contactPostPassDurationSeconds",
        "contact_pre_pass_duration_seconds": "contactPrePassDurationSeconds",
        "tags": "tags",
    },
)
class CfnMissionProfileProps:
    def __init__(
        self,
        *,
        dataflow_edges: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnMissionProfile.DataflowEdgeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
        minimum_viable_contact_duration_seconds: jsii.Number,
        name: builtins.str,
        tracking_config_arn: builtins.str,
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMissionProfile``.

        :param dataflow_edges: A list containing lists of config ARNs. Each list of config ARNs is an edge, with a "from" config and a "to" config.
        :param minimum_viable_contact_duration_seconds: Minimum length of a contact in seconds that Ground Station will return when listing contacts. Ground Station will not return contacts shorter than this duration.
        :param name: The name of the mission profile.
        :param tracking_config_arn: The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.
        :param contact_post_pass_duration_seconds: Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param contact_pre_pass_duration_seconds: Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param tags: Tags assigned to the mission profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_groundstation as groundstation
            
            cfn_mission_profile_props = groundstation.CfnMissionProfileProps(
                dataflow_edges=[groundstation.CfnMissionProfile.DataflowEdgeProperty(
                    destination="destination",
                    source="source"
                )],
                minimum_viable_contact_duration_seconds=123,
                name="name",
                tracking_config_arn="trackingConfigArn",
            
                # the properties below are optional
                contact_post_pass_duration_seconds=123,
                contact_pre_pass_duration_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffcd765f58cc3e2a73c40360cc760b172eaac48b4abed8bc5946ebc9392c169b)
            check_type(argname="argument dataflow_edges", value=dataflow_edges, expected_type=type_hints["dataflow_edges"])
            check_type(argname="argument minimum_viable_contact_duration_seconds", value=minimum_viable_contact_duration_seconds, expected_type=type_hints["minimum_viable_contact_duration_seconds"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tracking_config_arn", value=tracking_config_arn, expected_type=type_hints["tracking_config_arn"])
            check_type(argname="argument contact_post_pass_duration_seconds", value=contact_post_pass_duration_seconds, expected_type=type_hints["contact_post_pass_duration_seconds"])
            check_type(argname="argument contact_pre_pass_duration_seconds", value=contact_pre_pass_duration_seconds, expected_type=type_hints["contact_pre_pass_duration_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataflow_edges": dataflow_edges,
            "minimum_viable_contact_duration_seconds": minimum_viable_contact_duration_seconds,
            "name": name,
            "tracking_config_arn": tracking_config_arn,
        }
        if contact_post_pass_duration_seconds is not None:
            self._values["contact_post_pass_duration_seconds"] = contact_post_pass_duration_seconds
        if contact_pre_pass_duration_seconds is not None:
            self._values["contact_pre_pass_duration_seconds"] = contact_pre_pass_duration_seconds
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dataflow_edges(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMissionProfile.DataflowEdgeProperty, _IResolvable_a771d0ef]]]:
        '''A list containing lists of config ARNs.

        Each list of config ARNs is an edge, with a "from" config and a "to" config.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-dataflowedges
        '''
        result = self._values.get("dataflow_edges")
        assert result is not None, "Required property 'dataflow_edges' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMissionProfile.DataflowEdgeProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def minimum_viable_contact_duration_seconds(self) -> jsii.Number:
        '''Minimum length of a contact in seconds that Ground Station will return when listing contacts.

        Ground Station will not return contacts shorter than this duration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds
        '''
        result = self._values.get("minimum_viable_contact_duration_seconds")
        assert result is not None, "Required property 'minimum_viable_contact_duration_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the mission profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracking_config_arn(self) -> builtins.str:
        '''The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-trackingconfigarn
        '''
        result = self._values.get("tracking_config_arn")
        assert result is not None, "Required property 'tracking_config_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished.

        For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactpostpassdurationseconds
        '''
        result = self._values.get("contact_post_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass.

        For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactprepassdurationseconds
        '''
        result = self._values.get("contact_pre_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Tags assigned to the mission profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMissionProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfig",
    "CfnConfigProps",
    "CfnDataflowEndpointGroup",
    "CfnDataflowEndpointGroupProps",
    "CfnMissionProfile",
    "CfnMissionProfileProps",
]

publication.publish()

def _typecheckingstub__657c3e97ed7d45b231a24236c1cae3dca8102fb25e9f2d958c56983bacf4369b(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    config_data: typing.Union[typing.Union[CfnConfig.ConfigDataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8704ae026161d5f282efc7f368880887d004821ba903ffbce74f9b7622897b2(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5f30635d8eb8952763b80a1c069ec2123de641681a0a3f5d23078f6b27daf2f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd09d2578ff00eb8423fdb785e94cafd2362719d33d9b57c7d8ec421ed2e2318(
    value: typing.Union[CfnConfig.ConfigDataProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6982bee99a38dbfa5743bcf0824d49af7adabc0595f0b95b2d6ea098691c7697(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c04352481a7c34a3c688e56f8318117369261927c92158d3300cb4c2542689d(
    *,
    spectrum_config: typing.Optional[typing.Union[typing.Union[CfnConfig.SpectrumConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4faf95e28d2f8ffe9bb21eec57b5a7129d3297fb344d9dc018e75d434aee790f(
    *,
    decode_config: typing.Optional[typing.Union[typing.Union[CfnConfig.DecodeConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    demodulation_config: typing.Optional[typing.Union[typing.Union[CfnConfig.DemodulationConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    spectrum_config: typing.Optional[typing.Union[typing.Union[CfnConfig.SpectrumConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397131565634a34a48430e2550aab56d413c7ee6bb7053746f323457c20138bb(
    *,
    spectrum_config: typing.Optional[typing.Union[typing.Union[CfnConfig.UplinkSpectrumConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    target_eirp: typing.Optional[typing.Union[typing.Union[CfnConfig.EirpProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    transmit_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b22aa96006504c7fec0cf4e75d06fb8f9e7128df24bd581d183c54387f9378(
    *,
    antenna_downlink_config: typing.Optional[typing.Union[typing.Union[CfnConfig.AntennaDownlinkConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    antenna_downlink_demod_decode_config: typing.Optional[typing.Union[typing.Union[CfnConfig.AntennaDownlinkDemodDecodeConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    antenna_uplink_config: typing.Optional[typing.Union[typing.Union[CfnConfig.AntennaUplinkConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    dataflow_endpoint_config: typing.Optional[typing.Union[typing.Union[CfnConfig.DataflowEndpointConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    s3_recording_config: typing.Optional[typing.Union[typing.Union[CfnConfig.S3RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tracking_config: typing.Optional[typing.Union[typing.Union[CfnConfig.TrackingConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    uplink_echo_config: typing.Optional[typing.Union[typing.Union[CfnConfig.UplinkEchoConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d2f55bc531770d611617be39d5f269f70f39b8bee9c9389cb21ca8e3f3f821(
    *,
    dataflow_endpoint_name: typing.Optional[builtins.str] = None,
    dataflow_endpoint_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e607cadb9fbc58a2a4f7c79b3882b1ed43311d63e92beb7b12bc5cd79a285b(
    *,
    unvalidated_json: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccaa56ccbd83a420e521d2cb4523d49cfa112e2fd415cfc5e19fdf0b95d45f6b(
    *,
    unvalidated_json: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a98a3bde417e64e3e4b176491780cc578cd3ee8c4faaf84d7802297d8cd75f(
    *,
    units: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302f13976c3c3d7b6f0326f26b09f77adaa23fe64a67a999ec3f548217a3df76(
    *,
    units: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4c98a56bc0e5c59cc6da2fd0e58e8b7eef163bad672fffa982dcd2b5844b78(
    *,
    units: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493cf27eca919ee7b66301aaccbfd2cc027645907a126e31271631eb96d102ea(
    *,
    bucket_arn: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9adb807c6b9574ca840386f2cd60c26bf54d2807b578363b02a6755e987ed3d2(
    *,
    bandwidth: typing.Optional[typing.Union[typing.Union[CfnConfig.FrequencyBandwidthProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    center_frequency: typing.Optional[typing.Union[typing.Union[CfnConfig.FrequencyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    polarization: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a649cc24680f06b905daee3d3ae4d959095ba1de230c27c2e50aa6c9b498a949(
    *,
    autotrack: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5dde389e04804c15edf5b5c6d93e3ebaf320af28e1ae9dfac4ca6d52f548d9(
    *,
    antenna_uplink_config_arn: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a731e0bfae50c5135fc115de0242f154c9a6feb5c403997dbfbdd381c811bd0(
    *,
    center_frequency: typing.Optional[typing.Union[typing.Union[CfnConfig.FrequencyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    polarization: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32beda0b8f3cd1c907abe93c5126f04185f8e2c4b04e908d717777df4aa00342(
    *,
    config_data: typing.Union[typing.Union[CfnConfig.ConfigDataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006fc29ed40400465da28e607e91916cf4754a95601d4906ff2f879def4da0cc(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    endpoint_details: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d626b2ba1439f3723650348bfaabb073f29787e7b2f674860f4a702f9210728(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4eefd82a36eb2eea3769307c4fa3d3e7ba27a68d1a08ab235150c7a1e3b696(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1180b67cd56c498b0a621032a3ada07d925e7da5eb565210edcbc7500a9c50d3(
    value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, _IResolvable_a771d0ef]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d9d71e3873a3732752d7b419aa97edc3cfb6c69c75ae0cd1293332d32a9eee(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd20705e1c88d244943b3068d0fae6005b550f99c36cde62ac7b7aebaa407503(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3701331129f17bedee284cd2993120a37fc6e66e02af9245cfec41493ae81a1(
    *,
    address: typing.Optional[typing.Union[typing.Union[CfnDataflowEndpointGroup.SocketAddressProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    mtu: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4423867d9810d2ad9ef03d9eda98498ecb5952ecddebda47fac09848ff958bb2(
    *,
    endpoint: typing.Optional[typing.Union[typing.Union[CfnDataflowEndpointGroup.DataflowEndpointProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    security_details: typing.Optional[typing.Union[typing.Union[CfnDataflowEndpointGroup.SecurityDetailsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af1d80d40b717dc3d03e47a8c010c25af557c966752a3bfca4afd4fda080dc6e(
    *,
    role_arn: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3edbe1e795e1837558a4cc5dc6918ae06d74ee6eb6b216a7b7f1107537c1ece(
    *,
    name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba30a4da161078026e6d76116bc97f1021d6c78718d529c9d25544e7cc607b76(
    *,
    endpoint_details: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__033b90ee689d77aa5132e8b009b9a4be1cc6de9db33b8649108eabd7064b0f2f(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    dataflow_edges: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnMissionProfile.DataflowEdgeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    minimum_viable_contact_duration_seconds: jsii.Number,
    name: builtins.str,
    tracking_config_arn: builtins.str,
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__718eddf91282965b494b2a28d0ccd5f89daf7e71ac877b8bd2508f64dec39770(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10dfc0b338ca4bd2816c4f50a88c90905f6ed88321cdcbb069bcd2dccc27e42f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d40e2eaae9ea126000ebc198ca2dabb658a3794469f9d2205bc6214f96e814(
    value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMissionProfile.DataflowEdgeProperty, _IResolvable_a771d0ef]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732a154dbd945eeedeb2e1b62ac2052ecea135cbeb02876105d6bb3574c3b4fa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90173731028b0745472ef1fc90bfd514697f8875b84a1a593c2fb786e61b6c8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24cffb024ad13354281b3df894b8c5390976e4a265feb40423ae0469667253ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b56f1c27068b271741503ff36e3447ebb37613d7f295b15ed8e603c73b9071(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__834ee5a024189d41b5919c1289b90ea43f6bd3cdca2ec26d6345163b63d05afb(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0dde948392439aff4872a263d6f4bd715d1f43acd63de856a2f433886c7ee99(
    *,
    destination: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffcd765f58cc3e2a73c40360cc760b172eaac48b4abed8bc5946ebc9392c169b(
    *,
    dataflow_edges: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnMissionProfile.DataflowEdgeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    minimum_viable_contact_duration_seconds: jsii.Number,
    name: builtins.str,
    tracking_config_arn: builtins.str,
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

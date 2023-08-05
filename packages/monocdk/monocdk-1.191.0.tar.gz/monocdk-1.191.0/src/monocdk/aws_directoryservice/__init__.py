'''
# AWS Directory Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as directoryservice
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DirectoryService construct libraries](https://constructs.dev/search?q=directoryservice)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DirectoryService resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DirectoryService](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html).

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
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnMicrosoftAD(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_directoryservice.CfnMicrosoftAD",
):
    '''A CloudFormation ``AWS::DirectoryService::MicrosoftAD``.

    The ``AWS::DirectoryService::MicrosoftAD`` resource specifies a Microsoft Active Directory in AWS so that your directory users and groups can access the AWS Management Console and AWS applications using their existing credentials. For more information, see `AWS Managed Microsoft AD <https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html>`_ in the *AWS Directory Service Admin Guide* .

    :cloudformationResource: AWS::DirectoryService::MicrosoftAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_directoryservice as directoryservice
        
        cfn_microsoft_aD = directoryservice.CfnMicrosoftAD(self, "MyCfnMicrosoftAD",
            name="name",
            password="password",
            vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            edition="edition",
            enable_sso=False,
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[typing.Union["CfnMicrosoftAD.VpcSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectoryService::MicrosoftAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        :param password: The password for the default administrative user named ``Admin`` . If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param vpc_settings: Specifies the VPC settings of the Microsoft AD directory server in AWS .
        :param create_alias: Specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias. .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param edition: AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` . ``Enterprise`` is the default.
        :param enable_sso: Whether to enable single sign-on for a Microsoft Active Directory in AWS . Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param short_name: The NetBIOS name for your domain, such as ``CORP`` . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4165e3330fab5bf517c9a0850b7425b76c565a9f88b43cf1980c668fa48c8081)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMicrosoftADProps(
            name=name,
            password=password,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            edition=edition,
            enable_sso=enable_sso,
            short_name=short_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2eeeb41273a18ebb186a838901aa305e0c98b6c56c755b0695eb3db83de117)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a411fd51aa7220a98b9ec6db63c86f3fb5ff1ff9ce2902ebe1ea548c4810f8ab)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''The alias for a directory.

        For example: ``d-12373a053a`` or ``alias4-mydirectory-12345abcgmzsk`` (if you have the ``CreateAlias`` property set to true).

        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of the DNS servers for the directory, such as ``[ "192.0.2.1", "192.0.2.2" ]`` .

        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b131b94f87cdcc9a0cd74338ad88bbaef7683e7415c4bccf8e9060ee148839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''The password for the default administrative user named ``Admin`` .

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b9e96c0eb570b11098fb700bba687c995b61bbc7211edfaf0ad5180bd413b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_a771d0ef]:
        '''Specifies the VPC settings of the Microsoft AD directory server in AWS .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        return typing.cast(typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_a771d0ef], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21c61a53930ddcd2a787b50285a29e2af597273888873e90ee91f31e1d7af117)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSettings", value)

    @builtins.property
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias.
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed842d411d013832ec1a8e771ce05dbcc3f3e16489d12d59a5c94bddfd09d3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAlias", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> typing.Optional[builtins.str]:
        '''AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` .

        ``Enterprise`` is the default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f94a33703213fba8c368cacbf870f9abb873fdb6afb7cf6e18a93eb1fd8197a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Whether to enable single sign-on for a Microsoft Active Directory in AWS .

        Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70136eb5ea632d6b6dcea29a4eaefc857fc301887d5865ba5fe2456389f91f49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSso", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name for your domain, such as ``CORP`` .

        If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e77ea8614123cbaa48058f94e937e9ac7e2e2a66b0c9435945e8a3317d92f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_directoryservice.CfnMicrosoftAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''Contains VPC information for the `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ or `CreateMicrosoftAD <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html>`_ operation.

            :param subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
            :param vpc_id: The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__88ca00b71e9776e96b3b0fb0761740eac4f5e3acb3c3be2b715aa669d8da31d1)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The identifiers of the subnets for the directory servers.

            The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_directoryservice.CfnMicrosoftADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "edition": "edition",
        "enable_sso": "enableSso",
        "short_name": "shortName",
    },
)
class CfnMicrosoftADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMicrosoftAD``.

        :param name: The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        :param password: The password for the default administrative user named ``Admin`` . If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param vpc_settings: Specifies the VPC settings of the Microsoft AD directory server in AWS .
        :param create_alias: Specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias. .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param edition: AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` . ``Enterprise`` is the default.
        :param enable_sso: Whether to enable single sign-on for a Microsoft Active Directory in AWS . Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param short_name: The NetBIOS name for your domain, such as ``CORP`` . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_directoryservice as directoryservice
            
            cfn_microsoft_aDProps = directoryservice.CfnMicrosoftADProps(
                name="name",
                password="password",
                vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                edition="edition",
                enable_sso=False,
                short_name="shortName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b150f030360eefb1f15698e21016879fb65576bfa98b641e9038a82c76f6cbd4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument vpc_settings", value=vpc_settings, expected_type=type_hints["vpc_settings"])
            check_type(argname="argument create_alias", value=create_alias, expected_type=type_hints["create_alias"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument enable_sso", value=enable_sso, expected_type=type_hints["enable_sso"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "password": password,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if edition is not None:
            self._values["edition"] = edition
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password for the default administrative user named ``Admin`` .

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _IResolvable_a771d0ef]:
        '''Specifies the VPC settings of the Microsoft AD directory server in AWS .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias.
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` .

        ``Enterprise`` is the default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Whether to enable single sign-on for a Microsoft Active Directory in AWS .

        Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name for your domain, such as ``CORP`` .

        If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMicrosoftADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnSimpleAD(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_directoryservice.CfnSimpleAD",
):
    '''A CloudFormation ``AWS::DirectoryService::SimpleAD``.

    The ``AWS::DirectoryService::SimpleAD`` resource specifies an AWS Directory Service Simple Active Directory ( Simple AD ) in AWS so that your directory users and groups can access the AWS Management Console and AWS applications using their existing credentials. Simple AD is a Microsoft Active Directory–compatible directory. For more information, see `Simple Active Directory <https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html>`_ in the *AWS Directory Service Admin Guide* .

    :cloudformationResource: AWS::DirectoryService::SimpleAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_directoryservice as directoryservice
        
        cfn_simple_aD = directoryservice.CfnSimpleAD(self, "MyCfnSimpleAD",
            name="name",
            size="size",
            vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            description="description",
            enable_sso=False,
            password="password",
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[typing.Union["CfnSimpleAD.VpcSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        password: typing.Optional[builtins.str] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectoryService::SimpleAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The fully qualified name for the directory, such as ``corp.example.com`` .
        :param size: The size of the directory. For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .
        :param vpc_settings: A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.
        :param create_alias: If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` . .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param description: A description for the directory.
        :param enable_sso: Whether to enable single sign-on for a directory. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param password: The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password. If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param short_name: The NetBIOS name of the directory, such as ``CORP`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8b3f8eae353e226b95ea2d77b198e268a142fb9526b026b3cc43bf6e1287aec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimpleADProps(
            name=name,
            size=size,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            description=description,
            enable_sso=enable_sso,
            password=password,
            short_name=short_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8b60fc0022cd3b08fc1ffd39fc8ffc96917349d1b6d2c3a571782dd76c86825)
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
            type_hints = typing.get_type_hints(_typecheckingstub__27f39a75ec2ef03c476f663275e00fc466633a22612ad1ab0c0f3bbce9a8cbe6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''The alias for a directory.

        For example: ``d-12373a053a`` or ``alias4-mydirectory-12345abcgmzsk`` (if you have the ``CreateAlias`` property set to true).

        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrDirectoryId")
    def attr_directory_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DirectoryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirectoryId"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of the DNS servers for the directory, such as ``[ "172.31.3.154", "172.31.63.203" ]`` .

        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The fully qualified name for the directory, such as ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb55412a147e7e82af7b19b4d7850f3f48eed5b3af46cfbbfb0c6bbecddac67e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        '''The size of the directory.

        For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6019ce0a31717664e7137eaf7692c2f0ce5024d8a2da23aa6feb597fa8d7843c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_a771d0ef]:
        '''A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        return typing.cast(typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_a771d0ef], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e743801e79c1e6221268c28f256638192b6efb9463721b383a04ec47e57c4ec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSettings", value)

    @builtins.property
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` .
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81e2c3289518710eba295dc5a9fe1066d4ea8f398459c5229f7d2c034ec1faf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAlias", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the directory.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3834cb2f24132cc82908494ba38a722ac1182f4ce9cf5d2d2bab99832f93f6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Whether to enable single sign-on for a directory.

        If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c78c770a187c0386faeb239aa1159da92b6220318ec75662761135c2169af101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSso", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the directory administrator.

        The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password.

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34d556a8235bcce371773e694922ba972576cc3db97f0ebf21659ae8672e84d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name of the directory, such as ``CORP`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd000d3a0429b2867d5d46821713a2456733415dcc6705696f1cdc965c2d753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_directoryservice.CfnSimpleAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''Contains VPC information for the `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ or `CreateMicrosoftAD <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html>`_ operation.

            :param subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
            :param vpc_id: The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8761d510db330d913811734d5fe756d657b87b25fac444f95190ff528dd5abab)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The identifiers of the subnets for the directory servers.

            The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_directoryservice.CfnSimpleADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "size": "size",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "description": "description",
        "enable_sso": "enableSso",
        "password": "password",
        "short_name": "shortName",
    },
)
class CfnSimpleADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        password: typing.Optional[builtins.str] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimpleAD``.

        :param name: The fully qualified name for the directory, such as ``corp.example.com`` .
        :param size: The size of the directory. For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .
        :param vpc_settings: A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.
        :param create_alias: If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` . .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param description: A description for the directory.
        :param enable_sso: Whether to enable single sign-on for a directory. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param password: The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password. If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param short_name: The NetBIOS name of the directory, such as ``CORP`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_directoryservice as directoryservice
            
            cfn_simple_aDProps = directoryservice.CfnSimpleADProps(
                name="name",
                size="size",
                vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                description="description",
                enable_sso=False,
                password="password",
                short_name="shortName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0975274aa3f0aedfdde40cbc2133a3e2ff5ba89f189c89999d8a0965fb23950)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument vpc_settings", value=vpc_settings, expected_type=type_hints["vpc_settings"])
            check_type(argname="argument create_alias", value=create_alias, expected_type=type_hints["create_alias"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_sso", value=enable_sso, expected_type=type_hints["enable_sso"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "size": size,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if description is not None:
            self._values["description"] = description
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if password is not None:
            self._values["password"] = password
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''The fully qualified name for the directory, such as ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''The size of the directory.

        For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[CfnSimpleAD.VpcSettingsProperty, _IResolvable_a771d0ef]:
        '''A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[CfnSimpleAD.VpcSettingsProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` .
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the directory.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Whether to enable single sign-on for a directory.

        If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the directory administrator.

        The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password.

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name of the directory, such as ``CORP`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimpleADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMicrosoftAD",
    "CfnMicrosoftADProps",
    "CfnSimpleAD",
    "CfnSimpleADProps",
]

publication.publish()

def _typecheckingstub__4165e3330fab5bf517c9a0850b7425b76c565a9f88b43cf1980c668fa48c8081(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    name: builtins.str,
    password: builtins.str,
    vpc_settings: typing.Union[typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    edition: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2eeeb41273a18ebb186a838901aa305e0c98b6c56c755b0695eb3db83de117(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a411fd51aa7220a98b9ec6db63c86f3fb5ff1ff9ce2902ebe1ea548c4810f8ab(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b131b94f87cdcc9a0cd74338ad88bbaef7683e7415c4bccf8e9060ee148839(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b9e96c0eb570b11098fb700bba687c995b61bbc7211edfaf0ad5180bd413b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21c61a53930ddcd2a787b50285a29e2af597273888873e90ee91f31e1d7af117(
    value: typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed842d411d013832ec1a8e771ce05dbcc3f3e16489d12d59a5c94bddfd09d3d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94a33703213fba8c368cacbf870f9abb873fdb6afb7cf6e18a93eb1fd8197a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70136eb5ea632d6b6dcea29a4eaefc857fc301887d5865ba5fe2456389f91f49(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e77ea8614123cbaa48058f94e937e9ac7e2e2a66b0c9435945e8a3317d92f2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ca00b71e9776e96b3b0fb0761740eac4f5e3acb3c3be2b715aa669d8da31d1(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b150f030360eefb1f15698e21016879fb65576bfa98b641e9038a82c76f6cbd4(
    *,
    name: builtins.str,
    password: builtins.str,
    vpc_settings: typing.Union[typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    edition: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b3f8eae353e226b95ea2d77b198e268a142fb9526b026b3cc43bf6e1287aec(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    name: builtins.str,
    size: builtins.str,
    vpc_settings: typing.Union[typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    password: typing.Optional[builtins.str] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8b60fc0022cd3b08fc1ffd39fc8ffc96917349d1b6d2c3a571782dd76c86825(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f39a75ec2ef03c476f663275e00fc466633a22612ad1ab0c0f3bbce9a8cbe6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb55412a147e7e82af7b19b4d7850f3f48eed5b3af46cfbbfb0c6bbecddac67e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6019ce0a31717664e7137eaf7692c2f0ce5024d8a2da23aa6feb597fa8d7843c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e743801e79c1e6221268c28f256638192b6efb9463721b383a04ec47e57c4ec1(
    value: typing.Union[CfnSimpleAD.VpcSettingsProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81e2c3289518710eba295dc5a9fe1066d4ea8f398459c5229f7d2c034ec1faf5(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3834cb2f24132cc82908494ba38a722ac1182f4ce9cf5d2d2bab99832f93f6f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c78c770a187c0386faeb239aa1159da92b6220318ec75662761135c2169af101(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d556a8235bcce371773e694922ba972576cc3db97f0ebf21659ae8672e84d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd000d3a0429b2867d5d46821713a2456733415dcc6705696f1cdc965c2d753(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8761d510db330d913811734d5fe756d657b87b25fac444f95190ff528dd5abab(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0975274aa3f0aedfdde40cbc2133a3e2ff5ba89f189c89999d8a0965fb23950(
    *,
    name: builtins.str,
    size: builtins.str,
    vpc_settings: typing.Union[typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    password: typing.Optional[builtins.str] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

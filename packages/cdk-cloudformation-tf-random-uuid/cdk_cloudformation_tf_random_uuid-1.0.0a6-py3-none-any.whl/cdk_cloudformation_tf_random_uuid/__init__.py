'''
# tf-random-uuid

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::Random::Uuid` v1.0.0.

## Description

CloudFormation equivalent of random_uuid

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/random/TF-Random-Uuid/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::Random::Uuid \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-Random-Uuid \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::Random::Uuid`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-random-uuid+v1.0.0).
* Issues related to `TF::Random::Uuid` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/random/TF-Random-Uuid/docs/README.md).

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


class CfnUuid(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-random-uuid.CfnUuid",
):
    '''A CloudFormation ``TF::Random::Uuid``.

    :cloudformationResource: TF::Random::Uuid
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        keepers: typing.Optional[typing.Sequence[typing.Union["KeepersDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``TF::Random::Uuid``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param keepers: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8716417d1d698bf0198b5ff5afcec9d4ba4b39053860f6c541c3fa5a4f0c3070)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUuidProps(keepers=keepers)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::Random::Uuid.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResult")
    def attr_result(self) -> builtins.str:
        '''Attribute ``TF::Random::Uuid.Result``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResult"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::Random::Uuid.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUuidProps":
        '''Resource props.'''
        return typing.cast("CfnUuidProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-random-uuid.CfnUuidProps",
    jsii_struct_bases=[],
    name_mapping={"keepers": "keepers"},
)
class CfnUuidProps:
    def __init__(
        self,
        *,
        keepers: typing.Optional[typing.Sequence[typing.Union["KeepersDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''CloudFormation equivalent of random_uuid.

        :param keepers: 

        :schema: CfnUuidProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a81196f7a52b7b65a8a9a45f1692123215393d0a05559d27fe91a245dab112)
            check_type(argname="argument keepers", value=keepers, expected_type=type_hints["keepers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if keepers is not None:
            self._values["keepers"] = keepers

    @builtins.property
    def keepers(self) -> typing.Optional[typing.List["KeepersDefinition"]]:
        '''
        :schema: CfnUuidProps#Keepers
        '''
        result = self._values.get("keepers")
        return typing.cast(typing.Optional[typing.List["KeepersDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUuidProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-random-uuid.KeepersDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class KeepersDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: KeepersDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa7ab9fa613c23dc3530409d8eca279968cbc52716e886f824081227fc80729)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: KeepersDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: KeepersDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeepersDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUuid",
    "CfnUuidProps",
    "KeepersDefinition",
]

publication.publish()

def _typecheckingstub__8716417d1d698bf0198b5ff5afcec9d4ba4b39053860f6c541c3fa5a4f0c3070(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    keepers: typing.Optional[typing.Sequence[typing.Union[KeepersDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a81196f7a52b7b65a8a9a45f1692123215393d0a05559d27fe91a245dab112(
    *,
    keepers: typing.Optional[typing.Sequence[typing.Union[KeepersDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa7ab9fa613c23dc3530409d8eca279968cbc52716e886f824081227fc80729(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

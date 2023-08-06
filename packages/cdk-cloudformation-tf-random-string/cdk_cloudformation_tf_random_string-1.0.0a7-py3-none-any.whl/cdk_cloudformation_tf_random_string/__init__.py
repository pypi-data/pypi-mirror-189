'''
# tf-random-string

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::Random::String` v1.0.0.

## Description

CloudFormation equivalent of random_string

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/random/TF-Random-String/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::Random::String \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-Random-String \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::Random::String`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-random-string+v1.0.0).
* Issues related to `TF::Random::String` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/random/TF-Random-String/docs/README.md).

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


class CfnString(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-random-string.CfnString",
):
    '''A CloudFormation ``TF::Random::String``.

    :cloudformationResource: TF::Random::String
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        length: jsii.Number,
        keepers: typing.Optional[typing.Sequence[typing.Union["KeepersDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        lower: typing.Optional[builtins.bool] = None,
        min_lower: typing.Optional[jsii.Number] = None,
        min_numeric: typing.Optional[jsii.Number] = None,
        min_special: typing.Optional[jsii.Number] = None,
        min_upper: typing.Optional[jsii.Number] = None,
        number: typing.Optional[builtins.bool] = None,
        override_special: typing.Optional[builtins.str] = None,
        special: typing.Optional[builtins.bool] = None,
        upper: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``TF::Random::String``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param length: 
        :param keepers: 
        :param lower: 
        :param min_lower: 
        :param min_numeric: 
        :param min_special: 
        :param min_upper: 
        :param number: 
        :param override_special: 
        :param special: 
        :param upper: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3abbab9ca58a1eeb2ac0593c6dd03022cb03220f3fff26123c9797e80b3be6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStringProps(
            length=length,
            keepers=keepers,
            lower=lower,
            min_lower=min_lower,
            min_numeric=min_numeric,
            min_special=min_special,
            min_upper=min_upper,
            number=number,
            override_special=override_special,
            special=special,
            upper=upper,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::Random::String.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResult")
    def attr_result(self) -> builtins.str:
        '''Attribute ``TF::Random::String.Result``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResult"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::Random::String.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnStringProps":
        '''Resource props.'''
        return typing.cast("CfnStringProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-random-string.CfnStringProps",
    jsii_struct_bases=[],
    name_mapping={
        "length": "length",
        "keepers": "keepers",
        "lower": "lower",
        "min_lower": "minLower",
        "min_numeric": "minNumeric",
        "min_special": "minSpecial",
        "min_upper": "minUpper",
        "number": "number",
        "override_special": "overrideSpecial",
        "special": "special",
        "upper": "upper",
    },
)
class CfnStringProps:
    def __init__(
        self,
        *,
        length: jsii.Number,
        keepers: typing.Optional[typing.Sequence[typing.Union["KeepersDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        lower: typing.Optional[builtins.bool] = None,
        min_lower: typing.Optional[jsii.Number] = None,
        min_numeric: typing.Optional[jsii.Number] = None,
        min_special: typing.Optional[jsii.Number] = None,
        min_upper: typing.Optional[jsii.Number] = None,
        number: typing.Optional[builtins.bool] = None,
        override_special: typing.Optional[builtins.str] = None,
        special: typing.Optional[builtins.bool] = None,
        upper: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''CloudFormation equivalent of random_string.

        :param length: 
        :param keepers: 
        :param lower: 
        :param min_lower: 
        :param min_numeric: 
        :param min_special: 
        :param min_upper: 
        :param number: 
        :param override_special: 
        :param special: 
        :param upper: 

        :schema: CfnStringProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30971bac33a28b8a4f5786d543d1aa7eca1fa99f5452b2099173ae82e8cfb4e3)
            check_type(argname="argument length", value=length, expected_type=type_hints["length"])
            check_type(argname="argument keepers", value=keepers, expected_type=type_hints["keepers"])
            check_type(argname="argument lower", value=lower, expected_type=type_hints["lower"])
            check_type(argname="argument min_lower", value=min_lower, expected_type=type_hints["min_lower"])
            check_type(argname="argument min_numeric", value=min_numeric, expected_type=type_hints["min_numeric"])
            check_type(argname="argument min_special", value=min_special, expected_type=type_hints["min_special"])
            check_type(argname="argument min_upper", value=min_upper, expected_type=type_hints["min_upper"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
            check_type(argname="argument override_special", value=override_special, expected_type=type_hints["override_special"])
            check_type(argname="argument special", value=special, expected_type=type_hints["special"])
            check_type(argname="argument upper", value=upper, expected_type=type_hints["upper"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "length": length,
        }
        if keepers is not None:
            self._values["keepers"] = keepers
        if lower is not None:
            self._values["lower"] = lower
        if min_lower is not None:
            self._values["min_lower"] = min_lower
        if min_numeric is not None:
            self._values["min_numeric"] = min_numeric
        if min_special is not None:
            self._values["min_special"] = min_special
        if min_upper is not None:
            self._values["min_upper"] = min_upper
        if number is not None:
            self._values["number"] = number
        if override_special is not None:
            self._values["override_special"] = override_special
        if special is not None:
            self._values["special"] = special
        if upper is not None:
            self._values["upper"] = upper

    @builtins.property
    def length(self) -> jsii.Number:
        '''
        :schema: CfnStringProps#Length
        '''
        result = self._values.get("length")
        assert result is not None, "Required property 'length' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def keepers(self) -> typing.Optional[typing.List["KeepersDefinition"]]:
        '''
        :schema: CfnStringProps#Keepers
        '''
        result = self._values.get("keepers")
        return typing.cast(typing.Optional[typing.List["KeepersDefinition"]], result)

    @builtins.property
    def lower(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnStringProps#Lower
        '''
        result = self._values.get("lower")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_lower(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnStringProps#MinLower
        '''
        result = self._values.get("min_lower")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_numeric(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnStringProps#MinNumeric
        '''
        result = self._values.get("min_numeric")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_special(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnStringProps#MinSpecial
        '''
        result = self._values.get("min_special")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_upper(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnStringProps#MinUpper
        '''
        result = self._values.get("min_upper")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def number(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnStringProps#Number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def override_special(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnStringProps#OverrideSpecial
        '''
        result = self._values.get("override_special")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def special(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnStringProps#Special
        '''
        result = self._values.get("special")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def upper(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnStringProps#Upper
        '''
        result = self._values.get("upper")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-random-string.KeepersDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f80b70a5ebfb9f0058317ddd22c4e359874260e04530f8e90bb0730f4158b6f8)
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
    "CfnString",
    "CfnStringProps",
    "KeepersDefinition",
]

publication.publish()

def _typecheckingstub__8a3abbab9ca58a1eeb2ac0593c6dd03022cb03220f3fff26123c9797e80b3be6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    length: jsii.Number,
    keepers: typing.Optional[typing.Sequence[typing.Union[KeepersDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    lower: typing.Optional[builtins.bool] = None,
    min_lower: typing.Optional[jsii.Number] = None,
    min_numeric: typing.Optional[jsii.Number] = None,
    min_special: typing.Optional[jsii.Number] = None,
    min_upper: typing.Optional[jsii.Number] = None,
    number: typing.Optional[builtins.bool] = None,
    override_special: typing.Optional[builtins.str] = None,
    special: typing.Optional[builtins.bool] = None,
    upper: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30971bac33a28b8a4f5786d543d1aa7eca1fa99f5452b2099173ae82e8cfb4e3(
    *,
    length: jsii.Number,
    keepers: typing.Optional[typing.Sequence[typing.Union[KeepersDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    lower: typing.Optional[builtins.bool] = None,
    min_lower: typing.Optional[jsii.Number] = None,
    min_numeric: typing.Optional[jsii.Number] = None,
    min_special: typing.Optional[jsii.Number] = None,
    min_upper: typing.Optional[jsii.Number] = None,
    number: typing.Optional[builtins.bool] = None,
    override_special: typing.Optional[builtins.str] = None,
    special: typing.Optional[builtins.bool] = None,
    upper: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f80b70a5ebfb9f0058317ddd22c4e359874260e04530f8e90bb0730f4158b6f8(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

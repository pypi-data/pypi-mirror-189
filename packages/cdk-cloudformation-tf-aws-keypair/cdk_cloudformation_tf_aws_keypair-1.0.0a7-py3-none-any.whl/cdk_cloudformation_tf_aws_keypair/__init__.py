'''
# tf-aws-keypair

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::AWS::KeyPair` v1.0.0.

## Description

Provides an [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.

Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.

When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:

* OpenSSH public key format (the format in ~/.ssh/authorized_keys)
* Base64 encoded DER format
* SSH public key file format as specified in RFC4716

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-KeyPair/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::AWS::KeyPair \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-AWS-KeyPair \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::AWS::KeyPair`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-aws-keypair+v1.0.0).
* Issues related to `TF::AWS::KeyPair` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-KeyPair/docs/README.md).

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


class CfnKeyPair(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-aws-keypair.CfnKeyPair",
):
    '''A CloudFormation ``TF::AWS::KeyPair``.

    :cloudformationResource: TF::AWS::KeyPair
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        public_key: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
        key_name_prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags_all: typing.Optional[typing.Sequence[typing.Union["TagsAllDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``TF::AWS::KeyPair``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param public_key: The public key material.
        :param key_name: The name for the key pair.
        :param key_name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with ``key_name``.
        :param tags: Key-value map of resource tags. If configured with a provider ```default_tags`` configuration block <https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__964ed495f2a076f92e94b4e5b07e203b5d580e9438c550f2663015b01c18c847)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKeyPairProps(
            public_key=public_key,
            key_name=key_name,
            key_name_prefix=key_name_prefix,
            tags=tags,
            tags_all=tags_all,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.Arn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFingerprint")
    def attr_fingerprint(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.Fingerprint``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyPairId")
    def attr_key_pair_id(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.KeyPairId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyPairId"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnKeyPairProps":
        '''Resource props.'''
        return typing.cast("CfnKeyPairProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-keypair.CfnKeyPairProps",
    jsii_struct_bases=[],
    name_mapping={
        "public_key": "publicKey",
        "key_name": "keyName",
        "key_name_prefix": "keyNamePrefix",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CfnKeyPairProps:
    def __init__(
        self,
        *,
        public_key: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
        key_name_prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags_all: typing.Optional[typing.Sequence[typing.Union["TagsAllDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Provides an `EC2 key pair <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`_ resource. A key pair is used to control login access to EC2 instances.

        Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.

        When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the `AWS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws>`_) are:

        - OpenSSH public key format (the format in ~/.ssh/authorized_keys)
        - Base64 encoded DER format
        - SSH public key file format as specified in RFC4716

        :param public_key: The public key material.
        :param key_name: The name for the key pair.
        :param key_name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with ``key_name``.
        :param tags: Key-value map of resource tags. If configured with a provider ```default_tags`` configuration block <https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 

        :schema: CfnKeyPairProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65855f19f18a91b6ed1f4cb6e449d4d312f80677e12bdb308e21c6d8af9055bd)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument key_name_prefix", value=key_name_prefix, expected_type=type_hints["key_name_prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_key": public_key,
        }
        if key_name is not None:
            self._values["key_name"] = key_name
        if key_name_prefix is not None:
            self._values["key_name_prefix"] = key_name_prefix
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def public_key(self) -> builtins.str:
        '''The public key material.

        :schema: CfnKeyPairProps#PublicKey
        '''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''The name for the key pair.

        :schema: CfnKeyPairProps#KeyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique name beginning with the specified prefix.

        Conflicts with ``key_name``.

        :schema: CfnKeyPairProps#KeyNamePrefix
        '''
        result = self._values.get("key_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagsDefinition"]]:
        '''Key-value map of resource tags.

        If configured with a provider ```default_tags`` configuration block <https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.

        :schema: CfnKeyPairProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagsDefinition"]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.List["TagsAllDefinition"]]:
        '''
        :schema: CfnKeyPairProps#TagsAll
        '''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.List["TagsAllDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeyPairProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-keypair.TagsAllDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class TagsAllDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: TagsAllDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ba9caf35811058113ecab2760220e66570ae2be34df48fc04bf6a8103d79a30)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: TagsAllDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: TagsAllDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagsAllDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-keypair.TagsDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class TagsDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: TagsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3e145493a017f1fbef94d6d26b68b2f72fa8cc3a096b5418545d116377176c)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: TagsDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: TagsDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnKeyPair",
    "CfnKeyPairProps",
    "TagsAllDefinition",
    "TagsDefinition",
]

publication.publish()

def _typecheckingstub__964ed495f2a076f92e94b4e5b07e203b5d580e9438c550f2663015b01c18c847(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    public_key: builtins.str,
    key_name: typing.Optional[builtins.str] = None,
    key_name_prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags_all: typing.Optional[typing.Sequence[typing.Union[TagsAllDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65855f19f18a91b6ed1f4cb6e449d4d312f80677e12bdb308e21c6d8af9055bd(
    *,
    public_key: builtins.str,
    key_name: typing.Optional[builtins.str] = None,
    key_name_prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags_all: typing.Optional[typing.Sequence[typing.Union[TagsAllDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba9caf35811058113ecab2760220e66570ae2be34df48fc04bf6a8103d79a30(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3e145493a017f1fbef94d6d26b68b2f72fa8cc3a096b5418545d116377176c(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

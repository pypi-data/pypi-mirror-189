'''
# atlassian-opsgenie-user

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Atlassian::Opsgenie::User` v1.0.1.

## Description

Opsgenie User

## References

* [Source](https://github.com/opsgenie/opsgenie-cloudformation-resources)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Atlassian::Opsgenie::User \
  --publisher-id 4fb8713ab4ce2587ce74e0559d7661bb6e01e72b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/4fb8713ab4ce2587ce74e0559d7661bb6e01e72b/Atlassian-Opsgenie-User \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Atlassian::Opsgenie::User`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fatlassian-opsgenie-user+v1.0.1).
* Issues related to `Atlassian::Opsgenie::User` should be reported to the [publisher](https://github.com/opsgenie/opsgenie-cloudformation-resources).

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


class CfnUser(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-user.CfnUser",
):
    '''A CloudFormation ``Atlassian::Opsgenie::User``.

    :cloudformationResource: Atlassian::Opsgenie::User
    :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        full_name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        role: builtins.str,
        username: builtins.str,
    ) -> None:
        '''Create a new ``Atlassian::Opsgenie::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param full_name: User full name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param role: User role, default is User.
        :param username: Opsgenie Username the mail address of the user.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d422e41157aa40c880e96f1e2e97994b3d87ed520c32298249ba4811ba17cafe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            full_name=full_name,
            opsgenie_api_endpoint=opsgenie_api_endpoint,
            opsgenie_api_key=opsgenie_api_key,
            role=role,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrUserId")
    def attr_user_id(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::User.UserId``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUserProps":
        '''Resource props.'''
        return typing.cast("CfnUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-user.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "full_name": "fullName",
        "opsgenie_api_endpoint": "opsgenieApiEndpoint",
        "opsgenie_api_key": "opsgenieApiKey",
        "role": "role",
        "username": "username",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        full_name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        role: builtins.str,
        username: builtins.str,
    ) -> None:
        '''Opsgenie User.

        :param full_name: User full name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param role: User role, default is User.
        :param username: Opsgenie Username the mail address of the user.

        :schema: CfnUserProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04dc669f8e751f32709b8d5bee4301f6a65486fc3b976f2024d4008ae4b1c04b)
            check_type(argname="argument full_name", value=full_name, expected_type=type_hints["full_name"])
            check_type(argname="argument opsgenie_api_endpoint", value=opsgenie_api_endpoint, expected_type=type_hints["opsgenie_api_endpoint"])
            check_type(argname="argument opsgenie_api_key", value=opsgenie_api_key, expected_type=type_hints["opsgenie_api_key"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "full_name": full_name,
            "opsgenie_api_endpoint": opsgenie_api_endpoint,
            "opsgenie_api_key": opsgenie_api_key,
            "role": role,
            "username": username,
        }

    @builtins.property
    def full_name(self) -> builtins.str:
        '''User full name.

        :schema: CfnUserProps#FullName
        '''
        result = self._values.get("full_name")
        assert result is not None, "Required property 'full_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_endpoint(self) -> builtins.str:
        '''
        :schema: CfnUserProps#OpsgenieApiEndpoint
        '''
        result = self._values.get("opsgenie_api_endpoint")
        assert result is not None, "Required property 'opsgenie_api_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_key(self) -> builtins.str:
        '''
        :schema: CfnUserProps#OpsgenieApiKey
        '''
        result = self._values.get("opsgenie_api_key")
        assert result is not None, "Required property 'opsgenie_api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''User role, default is User.

        :schema: CfnUserProps#Role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Opsgenie Username the mail address of the user.

        :schema: CfnUserProps#Username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUser",
    "CfnUserProps",
]

publication.publish()

def _typecheckingstub__d422e41157aa40c880e96f1e2e97994b3d87ed520c32298249ba4811ba17cafe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    full_name: builtins.str,
    opsgenie_api_endpoint: builtins.str,
    opsgenie_api_key: builtins.str,
    role: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04dc669f8e751f32709b8d5bee4301f6a65486fc3b976f2024d4008ae4b1c04b(
    *,
    full_name: builtins.str,
    opsgenie_api_endpoint: builtins.str,
    opsgenie_api_key: builtins.str,
    role: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

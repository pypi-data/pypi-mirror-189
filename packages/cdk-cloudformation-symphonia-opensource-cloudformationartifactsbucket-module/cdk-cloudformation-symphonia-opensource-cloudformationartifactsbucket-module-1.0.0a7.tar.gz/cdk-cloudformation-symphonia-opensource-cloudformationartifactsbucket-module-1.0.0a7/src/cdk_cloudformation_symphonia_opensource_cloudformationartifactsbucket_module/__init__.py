'''
# symphonia-opensource-cloudformationartifactsbucket-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE \
  --publisher-id bf9c3875bb157d57566fdd0661e23ca05eb62a19 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/bf9c3875bb157d57566fdd0661e23ca05eb62a19/Symphonia-OpenSource-CloudFormationArtifactsBucket-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fsymphonia-opensource-cloudformationartifactsbucket-module+v1.0.0).
* Issues related to `Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE` should be reported to the [publisher](undefined).

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


class CfnCloudFormationArtifactsBucketModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnCloudFormationArtifactsBucketModule",
):
    '''A CloudFormation ``Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE``.

    :cloudformationResource: Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resources: typing.Optional[typing.Union["CfnCloudFormationArtifactsBucketModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe9aef02b6e7b0470ca245ec313c0c3414dc71f0772002c002d34cb22c1925ea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudFormationArtifactsBucketModuleProps(resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudFormationArtifactsBucketModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudFormationArtifactsBucketModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnCloudFormationArtifactsBucketModuleProps",
    jsii_struct_bases=[],
    name_mapping={"resources": "resources"},
)
class CfnCloudFormationArtifactsBucketModuleProps:
    def __init__(
        self,
        *,
        resources: typing.Optional[typing.Union["CfnCloudFormationArtifactsBucketModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE.

        :param resources: 

        :schema: CfnCloudFormationArtifactsBucketModuleProps
        '''
        if isinstance(resources, dict):
            resources = CfnCloudFormationArtifactsBucketModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab67ae4bfc96431844fa763776156a62bd1ba616d3c7829c50c58e0e61a46c1)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def resources(
        self,
    ) -> typing.Optional["CfnCloudFormationArtifactsBucketModulePropsResources"]:
        '''
        :schema: CfnCloudFormationArtifactsBucketModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCloudFormationArtifactsBucketModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationArtifactsBucketModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnCloudFormationArtifactsBucketModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class CfnCloudFormationArtifactsBucketModulePropsResources:
    def __init__(
        self,
        *,
        bucket: typing.Optional[typing.Union["CfnCloudFormationArtifactsBucketModulePropsResourcesBucket", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket: 

        :schema: CfnCloudFormationArtifactsBucketModulePropsResources
        '''
        if isinstance(bucket, dict):
            bucket = CfnCloudFormationArtifactsBucketModulePropsResourcesBucket(**bucket)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a9f464484d53547513d7aed367cfb4e97ba21166c9e3acaecc9c024b4e1205)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket

    @builtins.property
    def bucket(
        self,
    ) -> typing.Optional["CfnCloudFormationArtifactsBucketModulePropsResourcesBucket"]:
        '''
        :schema: CfnCloudFormationArtifactsBucketModulePropsResources#Bucket
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional["CfnCloudFormationArtifactsBucketModulePropsResourcesBucket"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationArtifactsBucketModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnCloudFormationArtifactsBucketModulePropsResourcesBucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudFormationArtifactsBucketModulePropsResourcesBucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudFormationArtifactsBucketModulePropsResourcesBucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7312c2210202b2d720556d26de071e5a556f14b8e5ffe3e6334eb34ac8912592)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudFormationArtifactsBucketModulePropsResourcesBucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudFormationArtifactsBucketModulePropsResourcesBucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationArtifactsBucketModulePropsResourcesBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudFormationArtifactsBucketModule",
    "CfnCloudFormationArtifactsBucketModuleProps",
    "CfnCloudFormationArtifactsBucketModulePropsResources",
    "CfnCloudFormationArtifactsBucketModulePropsResourcesBucket",
]

publication.publish()

def _typecheckingstub__fe9aef02b6e7b0470ca245ec313c0c3414dc71f0772002c002d34cb22c1925ea(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resources: typing.Optional[typing.Union[CfnCloudFormationArtifactsBucketModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab67ae4bfc96431844fa763776156a62bd1ba616d3c7829c50c58e0e61a46c1(
    *,
    resources: typing.Optional[typing.Union[CfnCloudFormationArtifactsBucketModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a9f464484d53547513d7aed367cfb4e97ba21166c9e3acaecc9c024b4e1205(
    *,
    bucket: typing.Optional[typing.Union[CfnCloudFormationArtifactsBucketModulePropsResourcesBucket, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7312c2210202b2d720556d26de071e5a556f14b8e5ffe3e6334eb34ac8912592(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

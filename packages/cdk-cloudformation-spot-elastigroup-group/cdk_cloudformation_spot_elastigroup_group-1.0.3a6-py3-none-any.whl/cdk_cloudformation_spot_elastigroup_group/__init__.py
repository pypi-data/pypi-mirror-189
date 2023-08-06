'''
# spot-elastigroup-group

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Spot::Elastigroup::Group` v1.0.3.

## Description

The Spot Elastigroup Resource allows you to create, update, manage, and delete Spot Elastigroups easily with CloudFormation

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Spot::Elastigroup::Group \
  --publisher-id 91d05981c6c0b080f2f1adcb370e1145c39b99e2 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/91d05981c6c0b080f2f1adcb370e1145c39b99e2/Spot-Elastigroup-Group \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Spot::Elastigroup::Group`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fspot-elastigroup-group+v1.0.3).
* Issues related to `Spot::Elastigroup::Group` should be reported to the [publisher](undefined).

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


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Attribute",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Attribute:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :schema: Attribute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9478cc4b27b054d3ffa8d22ecfb7e1d41ca962813698f0f602875c1fc537d688)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Attribute#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Attribute#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Attribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.BlockDeviceMapping",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "ebs": "ebs",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class BlockDeviceMapping:
    def __init__(
        self,
        *,
        device_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[typing.Union["BlockDeviceMappingEbs", typing.Dict[builtins.str, typing.Any]]] = None,
        no_device: typing.Optional[builtins.str] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: 
        :param ebs: 
        :param no_device: 
        :param virtual_name: 

        :schema: BlockDeviceMapping
        '''
        if isinstance(ebs, dict):
            ebs = BlockDeviceMappingEbs(**ebs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1dde2b7b9f057e6a4056311f29fd57ec58a1a8363155c7695fd24057b666b9f)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
            check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if device_name is not None:
            self._values["device_name"] = device_name
        if ebs is not None:
            self._values["ebs"] = ebs
        if no_device is not None:
            self._values["no_device"] = no_device
        if virtual_name is not None:
            self._values["virtual_name"] = virtual_name

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMapping#deviceName
        '''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs(self) -> typing.Optional["BlockDeviceMappingEbs"]:
        '''
        :schema: BlockDeviceMapping#ebs
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["BlockDeviceMappingEbs"], result)

    @builtins.property
    def no_device(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMapping#noDevice
        '''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMapping#virtualName
        '''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlockDeviceMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.BlockDeviceMappingEbs",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "snapshot_id": "snapshotId",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class BlockDeviceMappingEbs:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[builtins.bool] = None,
        encrypted: typing.Optional[builtins.bool] = None,
        iops: typing.Optional[jsii.Number] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional["BlockDeviceMappingEbsVolumeType"] = None,
    ) -> None:
        '''
        :param delete_on_termination: 
        :param encrypted: 
        :param iops: 
        :param snapshot_id: 
        :param volume_size: 
        :param volume_type: 

        :schema: BlockDeviceMappingEbs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c10ac981f599a2044252842b6ffbb099615349100cfb1361cd6e2bdd512022)
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def delete_on_termination(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: BlockDeviceMappingEbs#deleteOnTermination
        '''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encrypted(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: BlockDeviceMappingEbs#encrypted
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: BlockDeviceMappingEbs#iops
        '''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMappingEbs#snapshotId
        '''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: BlockDeviceMappingEbs#volumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional["BlockDeviceMappingEbsVolumeType"]:
        '''
        :schema: BlockDeviceMappingEbs#volumeType
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional["BlockDeviceMappingEbsVolumeType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlockDeviceMappingEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.BlockDeviceMappingEbsVolumeType"
)
class BlockDeviceMappingEbsVolumeType(enum.Enum):
    '''
    :schema: BlockDeviceMappingEbsVolumeType
    '''

    STANDARD = "STANDARD"
    '''standard.'''
    IO1 = "IO1"
    '''io1.'''
    GP2 = "GP2"
    '''gp2.'''


class CfnGroup(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroup",
):
    '''A CloudFormation ``Spot::Elastigroup::Group``.

    :cloudformationResource: Spot::Elastigroup::Group
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        credentials: typing.Union["CfnGroupPropsCredentials", typing.Dict[builtins.str, typing.Any]],
        group: typing.Optional[typing.Union["CfnGroupPropsGroup", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Spot::Elastigroup::Group``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param credentials: 
        :param group: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae8e0a0cd3b8949c7f43b677824dc627fa20df44be75a759d4b20a225cc4e0d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(credentials=credentials, group=group)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnGroupProps":
        '''Resource props.'''
        return typing.cast("CfnGroupProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={"credentials": "credentials", "group": "group"},
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        credentials: typing.Union["CfnGroupPropsCredentials", typing.Dict[builtins.str, typing.Any]],
        group: typing.Optional[typing.Union["CfnGroupPropsGroup", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''The Spot Elastigroup Resource allows you to create, update, manage, and delete Spot Elastigroups easily with CloudFormation.

        :param credentials: 
        :param group: 

        :schema: CfnGroupProps
        '''
        if isinstance(credentials, dict):
            credentials = CfnGroupPropsCredentials(**credentials)
        if isinstance(group, dict):
            group = CfnGroupPropsGroup(**group)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82575e10378d1e80a2be695e0a4451974db65b6b7371f3a9c5206a6ada5b6571)
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "credentials": credentials,
        }
        if group is not None:
            self._values["group"] = group

    @builtins.property
    def credentials(self) -> "CfnGroupPropsCredentials":
        '''
        :schema: CfnGroupProps#credentials
        '''
        result = self._values.get("credentials")
        assert result is not None, "Required property 'credentials' is missing"
        return typing.cast("CfnGroupPropsCredentials", result)

    @builtins.property
    def group(self) -> typing.Optional["CfnGroupPropsGroup"]:
        '''
        :schema: CfnGroupProps#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional["CfnGroupPropsGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsCredentials",
    jsii_struct_bases=[],
    name_mapping={"access_token": "accessToken", "account_id": "accountId"},
)
class CfnGroupPropsCredentials:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: 
        :param account_id: 

        :schema: CfnGroupPropsCredentials
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0c275b3c48a48d155c02caed86b6136e593b75b08a89b188a1b6de40a12bad)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsCredentials#accessToken
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsCredentials#accountId
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroup",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "compute": "compute",
        "description": "description",
        "group_id": "groupId",
        "name": "name",
        "region": "region",
        "scaling": "scaling",
        "scheduling": "scheduling",
        "strategy": "strategy",
        "third_parties_integration": "thirdPartiesIntegration",
    },
)
class CfnGroupPropsGroup:
    def __init__(
        self,
        *,
        capacity: typing.Optional[typing.Union["CfnGroupPropsGroupCapacity", typing.Dict[builtins.str, typing.Any]]] = None,
        compute: typing.Optional[typing.Union["CfnGroupPropsGroupCompute", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        scaling: typing.Optional[typing.Union["CfnGroupPropsGroupScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        scheduling: typing.Optional[typing.Union["CfnGroupPropsGroupScheduling", typing.Dict[builtins.str, typing.Any]]] = None,
        strategy: typing.Optional[typing.Union["CfnGroupPropsGroupStrategy", typing.Dict[builtins.str, typing.Any]]] = None,
        third_parties_integration: typing.Optional[typing.Union["CfnGroupPropsGroupThirdPartiesIntegration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity: 
        :param compute: 
        :param description: The description of the elastigroup.
        :param group_id: 
        :param name: The name of the elastigroup.
        :param region: 
        :param scaling: 
        :param scheduling: 
        :param strategy: 
        :param third_parties_integration: 

        :schema: CfnGroupPropsGroup
        '''
        if isinstance(capacity, dict):
            capacity = CfnGroupPropsGroupCapacity(**capacity)
        if isinstance(compute, dict):
            compute = CfnGroupPropsGroupCompute(**compute)
        if isinstance(scaling, dict):
            scaling = CfnGroupPropsGroupScaling(**scaling)
        if isinstance(scheduling, dict):
            scheduling = CfnGroupPropsGroupScheduling(**scheduling)
        if isinstance(strategy, dict):
            strategy = CfnGroupPropsGroupStrategy(**strategy)
        if isinstance(third_parties_integration, dict):
            third_parties_integration = CfnGroupPropsGroupThirdPartiesIntegration(**third_parties_integration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c2da0e1ca2dea5cefa49b31a4b41756489368be15ebc8431dd8794b542eff90)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument scaling", value=scaling, expected_type=type_hints["scaling"])
            check_type(argname="argument scheduling", value=scheduling, expected_type=type_hints["scheduling"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument third_parties_integration", value=third_parties_integration, expected_type=type_hints["third_parties_integration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity is not None:
            self._values["capacity"] = capacity
        if compute is not None:
            self._values["compute"] = compute
        if description is not None:
            self._values["description"] = description
        if group_id is not None:
            self._values["group_id"] = group_id
        if name is not None:
            self._values["name"] = name
        if region is not None:
            self._values["region"] = region
        if scaling is not None:
            self._values["scaling"] = scaling
        if scheduling is not None:
            self._values["scheduling"] = scheduling
        if strategy is not None:
            self._values["strategy"] = strategy
        if third_parties_integration is not None:
            self._values["third_parties_integration"] = third_parties_integration

    @builtins.property
    def capacity(self) -> typing.Optional["CfnGroupPropsGroupCapacity"]:
        '''
        :schema: CfnGroupPropsGroup#capacity
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional["CfnGroupPropsGroupCapacity"], result)

    @builtins.property
    def compute(self) -> typing.Optional["CfnGroupPropsGroupCompute"]:
        '''
        :schema: CfnGroupPropsGroup#compute
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional["CfnGroupPropsGroupCompute"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the elastigroup.

        :schema: CfnGroupPropsGroup#description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroup#groupId
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the elastigroup.

        :schema: CfnGroupPropsGroup#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroup#region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling(self) -> typing.Optional["CfnGroupPropsGroupScaling"]:
        '''
        :schema: CfnGroupPropsGroup#scaling
        '''
        result = self._values.get("scaling")
        return typing.cast(typing.Optional["CfnGroupPropsGroupScaling"], result)

    @builtins.property
    def scheduling(self) -> typing.Optional["CfnGroupPropsGroupScheduling"]:
        '''
        :schema: CfnGroupPropsGroup#scheduling
        '''
        result = self._values.get("scheduling")
        return typing.cast(typing.Optional["CfnGroupPropsGroupScheduling"], result)

    @builtins.property
    def strategy(self) -> typing.Optional["CfnGroupPropsGroupStrategy"]:
        '''
        :schema: CfnGroupPropsGroup#strategy
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional["CfnGroupPropsGroupStrategy"], result)

    @builtins.property
    def third_parties_integration(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupThirdPartiesIntegration"]:
        '''
        :schema: CfnGroupPropsGroup#thirdPartiesIntegration
        '''
        result = self._values.get("third_parties_integration")
        return typing.cast(typing.Optional["CfnGroupPropsGroupThirdPartiesIntegration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "maximum": "maximum",
        "minimum": "minimum",
        "target": "target",
        "unit": "unit",
    },
)
class CfnGroupPropsGroupCapacity:
    def __init__(
        self,
        *,
        maximum: typing.Optional[jsii.Number] = None,
        minimum: typing.Optional[jsii.Number] = None,
        target: typing.Optional[jsii.Number] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param maximum: 
        :param minimum: 
        :param target: 
        :param unit: 

        :schema: CfnGroupPropsGroupCapacity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894230b9753e3d68cf11052e16e651cb0d621f7121db214f2ed21c08b9080912)
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if maximum is not None:
            self._values["maximum"] = maximum
        if minimum is not None:
            self._values["minimum"] = minimum
        if target is not None:
            self._values["target"] = target
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def maximum(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupCapacity#maximum
        '''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupCapacity#minimum
        '''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupCapacity#target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupCapacity#unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupCompute",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "instance_types": "instanceTypes",
        "launch_specification": "launchSpecification",
        "product": "product",
    },
)
class CfnGroupPropsGroupCompute:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional[typing.Sequence[typing.Union["CfnGroupPropsGroupComputeAvailabilityZones", typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_types: typing.Optional[typing.Union["CfnGroupPropsGroupComputeInstanceTypes", typing.Dict[builtins.str, typing.Any]]] = None,
        launch_specification: typing.Optional[typing.Union["CfnGroupPropsGroupComputeLaunchSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        product: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability_zones: 
        :param instance_types: 
        :param launch_specification: 
        :param product: 

        :schema: CfnGroupPropsGroupCompute
        '''
        if isinstance(instance_types, dict):
            instance_types = CfnGroupPropsGroupComputeInstanceTypes(**instance_types)
        if isinstance(launch_specification, dict):
            launch_specification = CfnGroupPropsGroupComputeLaunchSpecification(**launch_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da077a38f05e3993b1b12bb0749e466d5f318dc90e57119b8d468044262f7994)
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument launch_specification", value=launch_specification, expected_type=type_hints["launch_specification"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if launch_specification is not None:
            self._values["launch_specification"] = launch_specification
        if product is not None:
            self._values["product"] = product

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional[typing.List["CfnGroupPropsGroupComputeAvailabilityZones"]]:
        '''
        :schema: CfnGroupPropsGroupCompute#availabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List["CfnGroupPropsGroupComputeAvailabilityZones"]], result)

    @builtins.property
    def instance_types(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeInstanceTypes"]:
        '''
        :schema: CfnGroupPropsGroupCompute#instanceTypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeInstanceTypes"], result)

    @builtins.property
    def launch_specification(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeLaunchSpecification"]:
        '''
        :schema: CfnGroupPropsGroupCompute#launchSpecification
        '''
        result = self._values.get("launch_specification")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeLaunchSpecification"], result)

    @builtins.property
    def product(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupCompute#product
        '''
        result = self._values.get("product")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupCompute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "subnet_ids": "subnetIds"},
)
class CfnGroupPropsGroupComputeAvailabilityZones:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: 
        :param subnet_ids: 

        :schema: CfnGroupPropsGroupComputeAvailabilityZones
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df5d0ec8dfd5c0d0d2321774c8c961748b40c0360c961e6adc738d3f4b6edff7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeAvailabilityZones#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupComputeAvailabilityZones#subnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeInstanceTypes",
    jsii_struct_bases=[],
    name_mapping={"on_demand": "onDemand", "spot": "spot"},
)
class CfnGroupPropsGroupComputeInstanceTypes:
    def __init__(
        self,
        *,
        on_demand: typing.Optional[builtins.str] = None,
        spot: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param on_demand: 
        :param spot: 

        :schema: CfnGroupPropsGroupComputeInstanceTypes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1927a0c9607121c4d10644386828ab615815e17301dd36b4b7478e6b8f2c41c5)
            check_type(argname="argument on_demand", value=on_demand, expected_type=type_hints["on_demand"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if on_demand is not None:
            self._values["on_demand"] = on_demand
        if spot is not None:
            self._values["spot"] = spot

    @builtins.property
    def on_demand(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeInstanceTypes#onDemand
        '''
        result = self._values.get("on_demand")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupComputeInstanceTypes#spot
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeInstanceTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "block_device_mappings": "blockDeviceMappings",
        "ebs_optimized": "ebsOptimized",
        "health_check_grace_period": "healthCheckGracePeriod",
        "health_check_type": "healthCheckType",
        "health_check_unhealthy_duration_before_replacement": "healthCheckUnhealthyDurationBeforeReplacement",
        "iam_role": "iamRole",
        "image_id": "imageId",
        "key_pair": "keyPair",
        "load_balancers_config": "loadBalancersConfig",
        "monitoring": "monitoring",
        "security_group_ids": "securityGroupIds",
        "shutdown_script": "shutdownScript",
        "tags": "tags",
        "tenancy": "tenancy",
        "user_data": "userData",
    },
)
class CfnGroupPropsGroupComputeLaunchSpecification:
    def __init__(
        self,
        *,
        block_device_mappings: typing.Optional[typing.Sequence[typing.Union[BlockDeviceMapping, typing.Dict[builtins.str, typing.Any]]]] = None,
        ebs_optimized: typing.Optional[builtins.bool] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        health_check_unhealthy_duration_before_replacement: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[typing.Union["CfnGroupPropsGroupComputeLaunchSpecificationIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        image_id: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional[builtins.str] = None,
        load_balancers_config: typing.Optional[typing.Union["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["Tag", typing.Dict[builtins.str, typing.Any]]]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_device_mappings: 
        :param ebs_optimized: 
        :param health_check_grace_period: 
        :param health_check_type: 
        :param health_check_unhealthy_duration_before_replacement: 
        :param iam_role: 
        :param image_id: 
        :param key_pair: 
        :param load_balancers_config: 
        :param monitoring: 
        :param security_group_ids: 
        :param shutdown_script: 
        :param tags: 
        :param tenancy: 
        :param user_data: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecification
        '''
        if isinstance(iam_role, dict):
            iam_role = CfnGroupPropsGroupComputeLaunchSpecificationIamRole(**iam_role)
        if isinstance(load_balancers_config, dict):
            load_balancers_config = CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig(**load_balancers_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eee7380e54403b9ce880f4d67b7075395a3a7149abf51a88f9e1a9e846bc266)
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument health_check_unhealthy_duration_before_replacement", value=health_check_unhealthy_duration_before_replacement, expected_type=type_hints["health_check_unhealthy_duration_before_replacement"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument load_balancers_config", value=load_balancers_config, expected_type=type_hints["load_balancers_config"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument shutdown_script", value=shutdown_script, expected_type=type_hints["shutdown_script"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if health_check_unhealthy_duration_before_replacement is not None:
            self._values["health_check_unhealthy_duration_before_replacement"] = health_check_unhealthy_duration_before_replacement
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if image_id is not None:
            self._values["image_id"] = image_id
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if load_balancers_config is not None:
            self._values["load_balancers_config"] = load_balancers_config
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if shutdown_script is not None:
            self._values["shutdown_script"] = shutdown_script
        if tags is not None:
            self._values["tags"] = tags
        if tenancy is not None:
            self._values["tenancy"] = tenancy
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def block_device_mappings(self) -> typing.Optional[typing.List[BlockDeviceMapping]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#blockDeviceMappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.List[BlockDeviceMapping]], result)

    @builtins.property
    def ebs_optimized(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#ebsOptimized
        '''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#healthCheckGracePeriod
        '''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#healthCheckType
        '''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_unhealthy_duration_before_replacement(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#healthCheckUnhealthyDurationBeforeReplacement
        '''
        result = self._values.get("health_check_unhealthy_duration_before_replacement")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_role(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationIamRole"]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#iamRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationIamRole"], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#imageId
        '''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#keyPair
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancers_config(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig"]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#loadBalancersConfig
        '''
        result = self._values.get("load_balancers_config")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig"], result)

    @builtins.property
    def monitoring(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#monitoring
        '''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#securityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shutdown_script(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#shutdownScript
        '''
        result = self._values.get("shutdown_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#tenancy
        '''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#userData
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecificationIamRole",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "name": "name"},
)
class CfnGroupPropsGroupComputeLaunchSpecificationIamRole:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param name: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecificationIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aca8cb410a3729539a4a314dbce75c50198f529ee196a1999bc9f9ca52c6be1)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationIamRole#arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationIamRole#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecificationIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig",
    jsii_struct_bases=[],
    name_mapping={"load_balancers": "loadBalancers"},
)
class CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig:
    def __init__(
        self,
        *,
        load_balancers: typing.Optional[typing.Sequence[typing.Union["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param load_balancers: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9037fd5917e1788a60ae2092aac1baa77c41116f2acc93af0c7a2752e118f0d)
            check_type(argname="argument load_balancers", value=load_balancers, expected_type=type_hints["load_balancers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers

    @builtins.property
    def load_balancers(
        self,
    ) -> typing.Optional[typing.List["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers"]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig#loadBalancers
        '''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.List["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "auto_weight": "autoWeight",
        "az_awareness": "azAwareness",
        "balancer_id": "balancerId",
        "name": "name",
        "target_set_id": "targetSetId",
        "type": "type",
    },
)
class CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        auto_weight: typing.Optional[builtins.bool] = None,
        az_awareness: typing.Optional[builtins.bool] = None,
        balancer_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        target_set_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param auto_weight: 
        :param az_awareness: 
        :param balancer_id: 
        :param name: 
        :param target_set_id: 
        :param type: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__485d7ef5c0402b31d384b20f3f872955b74075ea556dec94a114748125c2bafb)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument auto_weight", value=auto_weight, expected_type=type_hints["auto_weight"])
            check_type(argname="argument az_awareness", value=az_awareness, expected_type=type_hints["az_awareness"])
            check_type(argname="argument balancer_id", value=balancer_id, expected_type=type_hints["balancer_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_set_id", value=target_set_id, expected_type=type_hints["target_set_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if auto_weight is not None:
            self._values["auto_weight"] = auto_weight
        if az_awareness is not None:
            self._values["az_awareness"] = az_awareness
        if balancer_id is not None:
            self._values["balancer_id"] = balancer_id
        if name is not None:
            self._values["name"] = name
        if target_set_id is not None:
            self._values["target_set_id"] = target_set_id
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_weight(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#autoWeight
        '''
        result = self._values.get("auto_weight")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def az_awareness(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#azAwareness
        '''
        result = self._values.get("az_awareness")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def balancer_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#balancerId
        '''
        result = self._values.get("balancer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_set_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#targetSetId
        '''
        result = self._values.get("target_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupScaling",
    jsii_struct_bases=[],
    name_mapping={"down": "down", "up": "up"},
)
class CfnGroupPropsGroupScaling:
    def __init__(
        self,
        *,
        down: typing.Optional[typing.Sequence[typing.Union["ScalingPolicy", typing.Dict[builtins.str, typing.Any]]]] = None,
        up: typing.Optional[typing.Sequence[typing.Union["ScalingPolicy", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param down: 
        :param up: 

        :schema: CfnGroupPropsGroupScaling
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e7511661618b1dbaa7841f92e9a1536c3d91439dc5014d69abc3c56f74b20a)
            check_type(argname="argument down", value=down, expected_type=type_hints["down"])
            check_type(argname="argument up", value=up, expected_type=type_hints["up"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if down is not None:
            self._values["down"] = down
        if up is not None:
            self._values["up"] = up

    @builtins.property
    def down(self) -> typing.Optional[typing.List["ScalingPolicy"]]:
        '''
        :schema: CfnGroupPropsGroupScaling#down
        '''
        result = self._values.get("down")
        return typing.cast(typing.Optional[typing.List["ScalingPolicy"]], result)

    @builtins.property
    def up(self) -> typing.Optional[typing.List["ScalingPolicy"]]:
        '''
        :schema: CfnGroupPropsGroupScaling#up
        '''
        result = self._values.get("up")
        return typing.cast(typing.Optional[typing.List["ScalingPolicy"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupScheduling",
    jsii_struct_bases=[],
    name_mapping={"tasks": "tasks"},
)
class CfnGroupPropsGroupScheduling:
    def __init__(
        self,
        *,
        tasks: typing.Optional[typing.Sequence[typing.Union["Task", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param tasks: 

        :schema: CfnGroupPropsGroupScheduling
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33064e0dd49716025f7b3360d1ddec0a63f1d66b443a255fc6d554cf749d13a1)
            check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tasks is not None:
            self._values["tasks"] = tasks

    @builtins.property
    def tasks(self) -> typing.Optional[typing.List["Task"]]:
        '''
        :schema: CfnGroupPropsGroupScheduling#tasks
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.List["Task"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupScheduling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "availability_vs_cost": "availabilityVsCost",
        "draining_timeout": "drainingTimeout",
        "fallback_to_od": "fallbackToOd",
        "lifetime_period": "lifetimePeriod",
        "on_demand_count": "onDemandCount",
        "revert_to_spot": "revertToSpot",
        "risk": "risk",
    },
)
class CfnGroupPropsGroupStrategy:
    def __init__(
        self,
        *,
        availability_vs_cost: typing.Optional[builtins.str] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        fallback_to_od: typing.Optional[builtins.bool] = None,
        lifetime_period: typing.Optional[builtins.str] = None,
        on_demand_count: typing.Optional[jsii.Number] = None,
        revert_to_spot: typing.Optional[typing.Union["CfnGroupPropsGroupStrategyRevertToSpot", typing.Dict[builtins.str, typing.Any]]] = None,
        risk: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_vs_cost: 
        :param draining_timeout: 
        :param fallback_to_od: 
        :param lifetime_period: 
        :param on_demand_count: 
        :param revert_to_spot: 
        :param risk: 

        :schema: CfnGroupPropsGroupStrategy
        '''
        if isinstance(revert_to_spot, dict):
            revert_to_spot = CfnGroupPropsGroupStrategyRevertToSpot(**revert_to_spot)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2da4975b53bf256b867c857027268e918b39c0a7635f118b55815b2ee4f887)
            check_type(argname="argument availability_vs_cost", value=availability_vs_cost, expected_type=type_hints["availability_vs_cost"])
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument fallback_to_od", value=fallback_to_od, expected_type=type_hints["fallback_to_od"])
            check_type(argname="argument lifetime_period", value=lifetime_period, expected_type=type_hints["lifetime_period"])
            check_type(argname="argument on_demand_count", value=on_demand_count, expected_type=type_hints["on_demand_count"])
            check_type(argname="argument revert_to_spot", value=revert_to_spot, expected_type=type_hints["revert_to_spot"])
            check_type(argname="argument risk", value=risk, expected_type=type_hints["risk"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_vs_cost is not None:
            self._values["availability_vs_cost"] = availability_vs_cost
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if fallback_to_od is not None:
            self._values["fallback_to_od"] = fallback_to_od
        if lifetime_period is not None:
            self._values["lifetime_period"] = lifetime_period
        if on_demand_count is not None:
            self._values["on_demand_count"] = on_demand_count
        if revert_to_spot is not None:
            self._values["revert_to_spot"] = revert_to_spot
        if risk is not None:
            self._values["risk"] = risk

    @builtins.property
    def availability_vs_cost(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupStrategy#availabilityVsCost
        '''
        result = self._values.get("availability_vs_cost")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupStrategy#drainingTimeout
        '''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fallback_to_od(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupStrategy#fallbackToOd
        '''
        result = self._values.get("fallback_to_od")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lifetime_period(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupStrategy#lifetimePeriod
        '''
        result = self._values.get("lifetime_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_demand_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupStrategy#onDemandCount
        '''
        result = self._values.get("on_demand_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def revert_to_spot(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupStrategyRevertToSpot"]:
        '''
        :schema: CfnGroupPropsGroupStrategy#revertToSpot
        '''
        result = self._values.get("revert_to_spot")
        return typing.cast(typing.Optional["CfnGroupPropsGroupStrategyRevertToSpot"], result)

    @builtins.property
    def risk(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupStrategy#risk
        '''
        result = self._values.get("risk")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupStrategyRevertToSpot",
    jsii_struct_bases=[],
    name_mapping={"perform_at": "performAt", "time_windows": "timeWindows"},
)
class CfnGroupPropsGroupStrategyRevertToSpot:
    def __init__(
        self,
        *,
        perform_at: typing.Optional[builtins.str] = None,
        time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param perform_at: 
        :param time_windows: 

        :schema: CfnGroupPropsGroupStrategyRevertToSpot
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4038443c669504fd62a7fe192dbd44e2b8f11183a61aeabb8503bd9d99393812)
            check_type(argname="argument perform_at", value=perform_at, expected_type=type_hints["perform_at"])
            check_type(argname="argument time_windows", value=time_windows, expected_type=type_hints["time_windows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if perform_at is not None:
            self._values["perform_at"] = perform_at
        if time_windows is not None:
            self._values["time_windows"] = time_windows

    @builtins.property
    def perform_at(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupStrategyRevertToSpot#performAt
        '''
        result = self._values.get("perform_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_windows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupStrategyRevertToSpot#timeWindows
        '''
        result = self._values.get("time_windows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupStrategyRevertToSpot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupThirdPartiesIntegration",
    jsii_struct_bases=[],
    name_mapping={"code_deploy": "codeDeploy", "ecs": "ecs"},
)
class CfnGroupPropsGroupThirdPartiesIntegration:
    def __init__(
        self,
        *,
        code_deploy: typing.Optional[typing.Union["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy", typing.Dict[builtins.str, typing.Any]]] = None,
        ecs: typing.Optional[typing.Union["Ecs", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param code_deploy: 
        :param ecs: 

        :schema: CfnGroupPropsGroupThirdPartiesIntegration
        '''
        if isinstance(code_deploy, dict):
            code_deploy = CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy(**code_deploy)
        if isinstance(ecs, dict):
            ecs = Ecs(**ecs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5555d4f9d204203ac07f07c71c7c81553d8076fdf497aa0a812e17238a23a8)
            check_type(argname="argument code_deploy", value=code_deploy, expected_type=type_hints["code_deploy"])
            check_type(argname="argument ecs", value=ecs, expected_type=type_hints["ecs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if code_deploy is not None:
            self._values["code_deploy"] = code_deploy
        if ecs is not None:
            self._values["ecs"] = ecs

    @builtins.property
    def code_deploy(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy"]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegration#codeDeploy
        '''
        result = self._values.get("code_deploy")
        return typing.cast(typing.Optional["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy"], result)

    @builtins.property
    def ecs(self) -> typing.Optional["Ecs"]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegration#ecs
        '''
        result = self._values.get("ecs")
        return typing.cast(typing.Optional["Ecs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupThirdPartiesIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy",
    jsii_struct_bases=[],
    name_mapping={
        "clean_up_on_failure": "cleanUpOnFailure",
        "deployment_groups": "deploymentGroups",
        "terminate_instance_on_failure": "terminateInstanceOnFailure",
    },
)
class CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy:
    def __init__(
        self,
        *,
        clean_up_on_failure: typing.Optional[builtins.bool] = None,
        deployment_groups: typing.Optional[typing.Sequence[typing.Union["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups", typing.Dict[builtins.str, typing.Any]]]] = None,
        terminate_instance_on_failure: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param clean_up_on_failure: 
        :param deployment_groups: 
        :param terminate_instance_on_failure: 

        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdd7671b9bec15a81fe403e32e96b93775bc11f0ef34ed74ddc45c7d34bfb247)
            check_type(argname="argument clean_up_on_failure", value=clean_up_on_failure, expected_type=type_hints["clean_up_on_failure"])
            check_type(argname="argument deployment_groups", value=deployment_groups, expected_type=type_hints["deployment_groups"])
            check_type(argname="argument terminate_instance_on_failure", value=terminate_instance_on_failure, expected_type=type_hints["terminate_instance_on_failure"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if clean_up_on_failure is not None:
            self._values["clean_up_on_failure"] = clean_up_on_failure
        if deployment_groups is not None:
            self._values["deployment_groups"] = deployment_groups
        if terminate_instance_on_failure is not None:
            self._values["terminate_instance_on_failure"] = terminate_instance_on_failure

    @builtins.property
    def clean_up_on_failure(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy#cleanUpOnFailure
        '''
        result = self._values.get("clean_up_on_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deployment_groups(
        self,
    ) -> typing.Optional[typing.List["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups"]]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy#deploymentGroups
        '''
        result = self._values.get("deployment_groups")
        return typing.cast(typing.Optional[typing.List["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups"]], result)

    @builtins.property
    def terminate_instance_on_failure(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy#terminateInstanceOnFailure
        '''
        result = self._values.get("terminate_instance_on_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "deployment_group_name": "deploymentGroupName",
    },
)
class CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_name: 
        :param deployment_group_name: 

        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332a3aceba069d7e5c5c597c6e06d2938fbf30f33f38e6949539f8cbc776be68)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name
        if deployment_group_name is not None:
            self._values["deployment_group_name"] = deployment_group_name

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups#applicationName
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups#deploymentGroupName
        '''
        result = self._values.get("deployment_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Ecs",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scale": "autoScale",
        "batch": "batch",
        "cluster_name": "clusterName",
        "optimize_images": "optimizeImages",
    },
)
class Ecs:
    def __init__(
        self,
        *,
        auto_scale: typing.Optional[typing.Union["EcsAutoScale", typing.Dict[builtins.str, typing.Any]]] = None,
        batch: typing.Optional[typing.Union["EcsBatch", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        optimize_images: typing.Optional[typing.Union["EcsOptimizeImages", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_scale: 
        :param batch: 
        :param cluster_name: 
        :param optimize_images: 

        :schema: ecs
        '''
        if isinstance(auto_scale, dict):
            auto_scale = EcsAutoScale(**auto_scale)
        if isinstance(batch, dict):
            batch = EcsBatch(**batch)
        if isinstance(optimize_images, dict):
            optimize_images = EcsOptimizeImages(**optimize_images)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466b61f9eb0052a5d9d806629bab4e13e48e193ee86a917a331cf4ad3efe11b0)
            check_type(argname="argument auto_scale", value=auto_scale, expected_type=type_hints["auto_scale"])
            check_type(argname="argument batch", value=batch, expected_type=type_hints["batch"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument optimize_images", value=optimize_images, expected_type=type_hints["optimize_images"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_scale is not None:
            self._values["auto_scale"] = auto_scale
        if batch is not None:
            self._values["batch"] = batch
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if optimize_images is not None:
            self._values["optimize_images"] = optimize_images

    @builtins.property
    def auto_scale(self) -> typing.Optional["EcsAutoScale"]:
        '''
        :schema: ecs#autoScale
        '''
        result = self._values.get("auto_scale")
        return typing.cast(typing.Optional["EcsAutoScale"], result)

    @builtins.property
    def batch(self) -> typing.Optional["EcsBatch"]:
        '''
        :schema: ecs#batch
        '''
        result = self._values.get("batch")
        return typing.cast(typing.Optional["EcsBatch"], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ecs#clusterName
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optimize_images(self) -> typing.Optional["EcsOptimizeImages"]:
        '''
        :schema: ecs#optimizeImages
        '''
        result = self._values.get("optimize_images")
        return typing.cast(typing.Optional["EcsOptimizeImages"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ecs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsAutoScale",
    jsii_struct_bases=[],
    name_mapping={
        "attributes": "attributes",
        "cooldown": "cooldown",
        "down": "down",
        "headroom": "headroom",
        "is_auto_config": "isAutoConfig",
        "is_enabled": "isEnabled",
        "should_scale_down_non_service_tasks": "shouldScaleDownNonServiceTasks",
    },
)
class EcsAutoScale:
    def __init__(
        self,
        *,
        attributes: typing.Optional[typing.Sequence[typing.Union[Attribute, typing.Dict[builtins.str, typing.Any]]]] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        down: typing.Optional[typing.Union["EcsAutoScaleDown", typing.Dict[builtins.str, typing.Any]]] = None,
        headroom: typing.Optional[typing.Union["EcsAutoScaleHeadroom", typing.Dict[builtins.str, typing.Any]]] = None,
        is_auto_config: typing.Optional[builtins.bool] = None,
        is_enabled: typing.Optional[builtins.bool] = None,
        should_scale_down_non_service_tasks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param attributes: 
        :param cooldown: 
        :param down: 
        :param headroom: 
        :param is_auto_config: 
        :param is_enabled: 
        :param should_scale_down_non_service_tasks: 

        :schema: EcsAutoScale
        '''
        if isinstance(down, dict):
            down = EcsAutoScaleDown(**down)
        if isinstance(headroom, dict):
            headroom = EcsAutoScaleHeadroom(**headroom)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__960c14eaf1e43efcff09a331d7e0c8ca3f5d02188737bb2497e50d7975d15f03)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument down", value=down, expected_type=type_hints["down"])
            check_type(argname="argument headroom", value=headroom, expected_type=type_hints["headroom"])
            check_type(argname="argument is_auto_config", value=is_auto_config, expected_type=type_hints["is_auto_config"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument should_scale_down_non_service_tasks", value=should_scale_down_non_service_tasks, expected_type=type_hints["should_scale_down_non_service_tasks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if attributes is not None:
            self._values["attributes"] = attributes
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if down is not None:
            self._values["down"] = down
        if headroom is not None:
            self._values["headroom"] = headroom
        if is_auto_config is not None:
            self._values["is_auto_config"] = is_auto_config
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if should_scale_down_non_service_tasks is not None:
            self._values["should_scale_down_non_service_tasks"] = should_scale_down_non_service_tasks

    @builtins.property
    def attributes(self) -> typing.Optional[typing.List[Attribute]]:
        '''
        :schema: EcsAutoScale#attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.List[Attribute]], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScale#cooldown
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def down(self) -> typing.Optional["EcsAutoScaleDown"]:
        '''
        :schema: EcsAutoScale#down
        '''
        result = self._values.get("down")
        return typing.cast(typing.Optional["EcsAutoScaleDown"], result)

    @builtins.property
    def headroom(self) -> typing.Optional["EcsAutoScaleHeadroom"]:
        '''
        :schema: EcsAutoScale#headroom
        '''
        result = self._values.get("headroom")
        return typing.cast(typing.Optional["EcsAutoScaleHeadroom"], result)

    @builtins.property
    def is_auto_config(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsAutoScale#isAutoConfig
        '''
        result = self._values.get("is_auto_config")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsAutoScale#isEnabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def should_scale_down_non_service_tasks(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsAutoScale#shouldScaleDownNonServiceTasks
        '''
        result = self._values.get("should_scale_down_non_service_tasks")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsAutoScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsAutoScaleDown",
    jsii_struct_bases=[],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "max_scale_down_percentage": "maxScaleDownPercentage",
    },
)
class EcsAutoScaleDown:
    def __init__(
        self,
        *,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evaluation_periods: 
        :param max_scale_down_percentage: 

        :schema: EcsAutoScaleDown
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3b1648eab235dd3306474e01a2494b8b03d85953db8534f57641c96c6359983)
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument max_scale_down_percentage", value=max_scale_down_percentage, expected_type=type_hints["max_scale_down_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if max_scale_down_percentage is not None:
            self._values["max_scale_down_percentage"] = max_scale_down_percentage

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleDown#evaluationPeriods
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_scale_down_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleDown#maxScaleDownPercentage
        '''
        result = self._values.get("max_scale_down_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsAutoScaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsAutoScaleHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_per_unit": "cpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
        "num_of_units": "numOfUnits",
    },
)
class EcsAutoScaleHeadroom:
    def __init__(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: 
        :param memory_per_unit: 
        :param num_of_units: 

        :schema: EcsAutoScaleHeadroom
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__247f1ed89c8287ff7f77b60c536d99f2040ff98cf8020ca9e33e851259192721)
            check_type(argname="argument cpu_per_unit", value=cpu_per_unit, expected_type=type_hints["cpu_per_unit"])
            check_type(argname="argument memory_per_unit", value=memory_per_unit, expected_type=type_hints["memory_per_unit"])
            check_type(argname="argument num_of_units", value=num_of_units, expected_type=type_hints["num_of_units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit
        if num_of_units is not None:
            self._values["num_of_units"] = num_of_units

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleHeadroom#cpuPerUnit
        '''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleHeadroom#memoryPerUnit
        '''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_of_units(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleHeadroom#numOfUnits
        '''
        result = self._values.get("num_of_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsAutoScaleHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsBatch",
    jsii_struct_bases=[],
    name_mapping={"job_queue_names": "jobQueueNames"},
)
class EcsBatch:
    def __init__(
        self,
        *,
        job_queue_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param job_queue_names: 

        :schema: EcsBatch
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3264a75640a8edad557155e40074f9fd12451cf509ae5a20917902a0e1042b1)
            check_type(argname="argument job_queue_names", value=job_queue_names, expected_type=type_hints["job_queue_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if job_queue_names is not None:
            self._values["job_queue_names"] = job_queue_names

    @builtins.property
    def job_queue_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: EcsBatch#jobQueueNames
        '''
        result = self._values.get("job_queue_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsBatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsOptimizeImages",
    jsii_struct_bases=[],
    name_mapping={
        "perform_at": "performAt",
        "should_optimize_ecs_ami": "shouldOptimizeEcsAmi",
        "time_windows": "timeWindows",
    },
)
class EcsOptimizeImages:
    def __init__(
        self,
        *,
        perform_at: typing.Optional[builtins.str] = None,
        should_optimize_ecs_ami: typing.Optional[builtins.bool] = None,
        time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param perform_at: 
        :param should_optimize_ecs_ami: 
        :param time_windows: 

        :schema: EcsOptimizeImages
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f70955dc6486d6e50bba46be0b08edd3f15932703fda1aab9edd609df0a9e38)
            check_type(argname="argument perform_at", value=perform_at, expected_type=type_hints["perform_at"])
            check_type(argname="argument should_optimize_ecs_ami", value=should_optimize_ecs_ami, expected_type=type_hints["should_optimize_ecs_ami"])
            check_type(argname="argument time_windows", value=time_windows, expected_type=type_hints["time_windows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if perform_at is not None:
            self._values["perform_at"] = perform_at
        if should_optimize_ecs_ami is not None:
            self._values["should_optimize_ecs_ami"] = should_optimize_ecs_ami
        if time_windows is not None:
            self._values["time_windows"] = time_windows

    @builtins.property
    def perform_at(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EcsOptimizeImages#performAt
        '''
        result = self._values.get("perform_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def should_optimize_ecs_ami(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsOptimizeImages#shouldOptimizeEcsAmi
        '''
        result = self._values.get("should_optimize_ecs_ami")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def time_windows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: EcsOptimizeImages#timeWindows
        '''
        result = self._values.get("time_windows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsOptimizeImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.ScalingPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "cooldown": "cooldown",
        "dimension": "dimension",
        "evaluation_periods": "evaluationPeriods",
        "metric_name": "metricName",
        "namespace": "namespace",
        "period": "period",
        "policy_name": "policyName",
        "statistic": "statistic",
        "threshold": "threshold",
        "unit": "unit",
    },
)
class ScalingPolicy:
    def __init__(
        self,
        *,
        action: typing.Optional[typing.Union["ScalingPolicyAction", typing.Dict[builtins.str, typing.Any]]] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimension: typing.Optional[typing.Sequence[typing.Union["ScalingPolicyDimension", typing.Dict[builtins.str, typing.Any]]]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[jsii.Number] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: 
        :param cooldown: 
        :param dimension: 
        :param evaluation_periods: 
        :param metric_name: 
        :param namespace: 
        :param period: 
        :param policy_name: 
        :param statistic: 
        :param threshold: 
        :param unit: 

        :schema: ScalingPolicy
        '''
        if isinstance(action, dict):
            action = ScalingPolicyAction(**action)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ddba07a135cd470599832c6376126ef47d4578d3919ac20a70c3a6272844a64)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if dimension is not None:
            self._values["dimension"] = dimension
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if namespace is not None:
            self._values["namespace"] = namespace
        if period is not None:
            self._values["period"] = period
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if statistic is not None:
            self._values["statistic"] = statistic
        if threshold is not None:
            self._values["threshold"] = threshold
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def action(self) -> typing.Optional["ScalingPolicyAction"]:
        '''
        :schema: ScalingPolicy#action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["ScalingPolicyAction"], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#cooldown
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimension(self) -> typing.Optional[typing.List["ScalingPolicyDimension"]]:
        '''
        :schema: ScalingPolicy#dimension
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional[typing.List["ScalingPolicyDimension"]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#evaluationPeriods
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#metricName
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#period
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#policyName
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#statistic
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.ScalingPolicyAction",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "maximum": "maximum",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "target": "target",
        "type": "type",
    },
)
class ScalingPolicyAction:
    def __init__(
        self,
        *,
        adjustment: typing.Optional[builtins.str] = None,
        maximum: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param adjustment: 
        :param maximum: 
        :param minimum: 
        :param min_target_capacity: 
        :param target: 
        :param type: 

        :schema: ScalingPolicyAction
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61630ac35cd6275a396f037eecbe165d4c6d5bb6c85a6acb3e82e244b1cdd931)
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if maximum is not None:
            self._values["maximum"] = maximum
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if target is not None:
            self._values["target"] = target
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#adjustment
        '''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#maximum
        '''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#minimum
        '''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#minTargetCapacity
        '''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicyAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.ScalingPolicyDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ScalingPolicyDimension:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param value: 

        :schema: ScalingPolicyDimension
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1140ce681bfa63e917681b7b340ada35e4eb863eae03e8a9574bfaac5bd724c7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyDimension#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyDimension#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicyDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Tag",
    jsii_struct_bases=[],
    name_mapping={"tag_key": "tagKey", "tag_value": "tagValue"},
)
class Tag:
    def __init__(
        self,
        *,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param tag_key: 
        :param tag_value: 

        :schema: Tag
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba768e6ef5a62c63e7aadaf97eae5cb36a88ad2361f245b7acce6300e8b8674a)
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Tag#tagKey
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Tag#tagValue
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Task",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "batch_size_percentage": "batchSizePercentage",
        "cron_expression": "cronExpression",
        "frequency": "frequency",
        "grace_period": "gracePeriod",
        "is_enabled": "isEnabled",
        "scale_max_capacity": "scaleMaxCapacity",
        "scale_min_capacity": "scaleMinCapacity",
        "scale_target_capacity": "scaleTargetCapacity",
        "start_time": "startTime",
        "task_type": "taskType",
    },
)
class Task:
    def __init__(
        self,
        *,
        adjustment: typing.Optional[jsii.Number] = None,
        batch_size_percentage: typing.Optional[jsii.Number] = None,
        cron_expression: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        is_enabled: typing.Optional[builtins.bool] = None,
        scale_max_capacity: typing.Optional[jsii.Number] = None,
        scale_min_capacity: typing.Optional[jsii.Number] = None,
        scale_target_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[builtins.str] = None,
        task_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param adjustment: 
        :param batch_size_percentage: 
        :param cron_expression: 
        :param frequency: 
        :param grace_period: 
        :param is_enabled: 
        :param scale_max_capacity: 
        :param scale_min_capacity: 
        :param scale_target_capacity: 
        :param start_time: 
        :param task_type: 

        :schema: Task
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1b6b735b15d3de623e7f51f851353aee987008f8fdb1a3dda95a881fe0689a7)
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument scale_max_capacity", value=scale_max_capacity, expected_type=type_hints["scale_max_capacity"])
            check_type(argname="argument scale_min_capacity", value=scale_min_capacity, expected_type=type_hints["scale_min_capacity"])
            check_type(argname="argument scale_target_capacity", value=scale_target_capacity, expected_type=type_hints["scale_target_capacity"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if batch_size_percentage is not None:
            self._values["batch_size_percentage"] = batch_size_percentage
        if cron_expression is not None:
            self._values["cron_expression"] = cron_expression
        if frequency is not None:
            self._values["frequency"] = frequency
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if scale_max_capacity is not None:
            self._values["scale_max_capacity"] = scale_max_capacity
        if scale_min_capacity is not None:
            self._values["scale_min_capacity"] = scale_min_capacity
        if scale_target_capacity is not None:
            self._values["scale_target_capacity"] = scale_target_capacity
        if start_time is not None:
            self._values["start_time"] = start_time
        if task_type is not None:
            self._values["task_type"] = task_type

    @builtins.property
    def adjustment(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#adjustment
        '''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_size_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#batchSizePercentage
        '''
        result = self._values.get("batch_size_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cron_expression(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#cronExpression
        '''
        result = self._values.get("cron_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#frequency
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#gracePeriod
        '''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def is_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: Task#isEnabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def scale_max_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#scaleMaxCapacity
        '''
        result = self._values.get("scale_max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_min_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#scaleMinCapacity
        '''
        result = self._values.get("scale_min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_target_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#scaleTargetCapacity
        '''
        result = self._values.get("scale_target_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#startTime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#taskType
        '''
        result = self._values.get("task_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Task(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Attribute",
    "BlockDeviceMapping",
    "BlockDeviceMappingEbs",
    "BlockDeviceMappingEbsVolumeType",
    "CfnGroup",
    "CfnGroupProps",
    "CfnGroupPropsCredentials",
    "CfnGroupPropsGroup",
    "CfnGroupPropsGroupCapacity",
    "CfnGroupPropsGroupCompute",
    "CfnGroupPropsGroupComputeAvailabilityZones",
    "CfnGroupPropsGroupComputeInstanceTypes",
    "CfnGroupPropsGroupComputeLaunchSpecification",
    "CfnGroupPropsGroupComputeLaunchSpecificationIamRole",
    "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig",
    "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers",
    "CfnGroupPropsGroupScaling",
    "CfnGroupPropsGroupScheduling",
    "CfnGroupPropsGroupStrategy",
    "CfnGroupPropsGroupStrategyRevertToSpot",
    "CfnGroupPropsGroupThirdPartiesIntegration",
    "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy",
    "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups",
    "Ecs",
    "EcsAutoScale",
    "EcsAutoScaleDown",
    "EcsAutoScaleHeadroom",
    "EcsBatch",
    "EcsOptimizeImages",
    "ScalingPolicy",
    "ScalingPolicyAction",
    "ScalingPolicyDimension",
    "Tag",
    "Task",
]

publication.publish()

def _typecheckingstub__9478cc4b27b054d3ffa8d22ecfb7e1d41ca962813698f0f602875c1fc537d688(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1dde2b7b9f057e6a4056311f29fd57ec58a1a8363155c7695fd24057b666b9f(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[BlockDeviceMappingEbs, typing.Dict[builtins.str, typing.Any]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c10ac981f599a2044252842b6ffbb099615349100cfb1361cd6e2bdd512022(
    *,
    delete_on_termination: typing.Optional[builtins.bool] = None,
    encrypted: typing.Optional[builtins.bool] = None,
    iops: typing.Optional[jsii.Number] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[BlockDeviceMappingEbsVolumeType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8e0a0cd3b8949c7f43b677824dc627fa20df44be75a759d4b20a225cc4e0d3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    credentials: typing.Union[CfnGroupPropsCredentials, typing.Dict[builtins.str, typing.Any]],
    group: typing.Optional[typing.Union[CfnGroupPropsGroup, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82575e10378d1e80a2be695e0a4451974db65b6b7371f3a9c5206a6ada5b6571(
    *,
    credentials: typing.Union[CfnGroupPropsCredentials, typing.Dict[builtins.str, typing.Any]],
    group: typing.Optional[typing.Union[CfnGroupPropsGroup, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0c275b3c48a48d155c02caed86b6136e593b75b08a89b188a1b6de40a12bad(
    *,
    access_token: typing.Optional[builtins.str] = None,
    account_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c2da0e1ca2dea5cefa49b31a4b41756489368be15ebc8431dd8794b542eff90(
    *,
    capacity: typing.Optional[typing.Union[CfnGroupPropsGroupCapacity, typing.Dict[builtins.str, typing.Any]]] = None,
    compute: typing.Optional[typing.Union[CfnGroupPropsGroupCompute, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    group_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    scaling: typing.Optional[typing.Union[CfnGroupPropsGroupScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    scheduling: typing.Optional[typing.Union[CfnGroupPropsGroupScheduling, typing.Dict[builtins.str, typing.Any]]] = None,
    strategy: typing.Optional[typing.Union[CfnGroupPropsGroupStrategy, typing.Dict[builtins.str, typing.Any]]] = None,
    third_parties_integration: typing.Optional[typing.Union[CfnGroupPropsGroupThirdPartiesIntegration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894230b9753e3d68cf11052e16e651cb0d621f7121db214f2ed21c08b9080912(
    *,
    maximum: typing.Optional[jsii.Number] = None,
    minimum: typing.Optional[jsii.Number] = None,
    target: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da077a38f05e3993b1b12bb0749e466d5f318dc90e57119b8d468044262f7994(
    *,
    availability_zones: typing.Optional[typing.Sequence[typing.Union[CfnGroupPropsGroupComputeAvailabilityZones, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_types: typing.Optional[typing.Union[CfnGroupPropsGroupComputeInstanceTypes, typing.Dict[builtins.str, typing.Any]]] = None,
    launch_specification: typing.Optional[typing.Union[CfnGroupPropsGroupComputeLaunchSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    product: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df5d0ec8dfd5c0d0d2321774c8c961748b40c0360c961e6adc738d3f4b6edff7(
    *,
    name: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1927a0c9607121c4d10644386828ab615815e17301dd36b4b7478e6b8f2c41c5(
    *,
    on_demand: typing.Optional[builtins.str] = None,
    spot: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eee7380e54403b9ce880f4d67b7075395a3a7149abf51a88f9e1a9e846bc266(
    *,
    block_device_mappings: typing.Optional[typing.Sequence[typing.Union[BlockDeviceMapping, typing.Dict[builtins.str, typing.Any]]]] = None,
    ebs_optimized: typing.Optional[builtins.bool] = None,
    health_check_grace_period: typing.Optional[jsii.Number] = None,
    health_check_type: typing.Optional[builtins.str] = None,
    health_check_unhealthy_duration_before_replacement: typing.Optional[jsii.Number] = None,
    iam_role: typing.Optional[typing.Union[CfnGroupPropsGroupComputeLaunchSpecificationIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    image_id: typing.Optional[builtins.str] = None,
    key_pair: typing.Optional[builtins.str] = None,
    load_balancers_config: typing.Optional[typing.Union[CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[builtins.bool] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    shutdown_script: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    user_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aca8cb410a3729539a4a314dbce75c50198f529ee196a1999bc9f9ca52c6be1(
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9037fd5917e1788a60ae2092aac1baa77c41116f2acc93af0c7a2752e118f0d(
    *,
    load_balancers: typing.Optional[typing.Sequence[typing.Union[CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__485d7ef5c0402b31d384b20f3f872955b74075ea556dec94a114748125c2bafb(
    *,
    arn: typing.Optional[builtins.str] = None,
    auto_weight: typing.Optional[builtins.bool] = None,
    az_awareness: typing.Optional[builtins.bool] = None,
    balancer_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    target_set_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e7511661618b1dbaa7841f92e9a1536c3d91439dc5014d69abc3c56f74b20a(
    *,
    down: typing.Optional[typing.Sequence[typing.Union[ScalingPolicy, typing.Dict[builtins.str, typing.Any]]]] = None,
    up: typing.Optional[typing.Sequence[typing.Union[ScalingPolicy, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33064e0dd49716025f7b3360d1ddec0a63f1d66b443a255fc6d554cf749d13a1(
    *,
    tasks: typing.Optional[typing.Sequence[typing.Union[Task, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2da4975b53bf256b867c857027268e918b39c0a7635f118b55815b2ee4f887(
    *,
    availability_vs_cost: typing.Optional[builtins.str] = None,
    draining_timeout: typing.Optional[jsii.Number] = None,
    fallback_to_od: typing.Optional[builtins.bool] = None,
    lifetime_period: typing.Optional[builtins.str] = None,
    on_demand_count: typing.Optional[jsii.Number] = None,
    revert_to_spot: typing.Optional[typing.Union[CfnGroupPropsGroupStrategyRevertToSpot, typing.Dict[builtins.str, typing.Any]]] = None,
    risk: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4038443c669504fd62a7fe192dbd44e2b8f11183a61aeabb8503bd9d99393812(
    *,
    perform_at: typing.Optional[builtins.str] = None,
    time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5555d4f9d204203ac07f07c71c7c81553d8076fdf497aa0a812e17238a23a8(
    *,
    code_deploy: typing.Optional[typing.Union[CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy, typing.Dict[builtins.str, typing.Any]]] = None,
    ecs: typing.Optional[typing.Union[Ecs, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdd7671b9bec15a81fe403e32e96b93775bc11f0ef34ed74ddc45c7d34bfb247(
    *,
    clean_up_on_failure: typing.Optional[builtins.bool] = None,
    deployment_groups: typing.Optional[typing.Sequence[typing.Union[CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups, typing.Dict[builtins.str, typing.Any]]]] = None,
    terminate_instance_on_failure: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332a3aceba069d7e5c5c597c6e06d2938fbf30f33f38e6949539f8cbc776be68(
    *,
    application_name: typing.Optional[builtins.str] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466b61f9eb0052a5d9d806629bab4e13e48e193ee86a917a331cf4ad3efe11b0(
    *,
    auto_scale: typing.Optional[typing.Union[EcsAutoScale, typing.Dict[builtins.str, typing.Any]]] = None,
    batch: typing.Optional[typing.Union[EcsBatch, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    optimize_images: typing.Optional[typing.Union[EcsOptimizeImages, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960c14eaf1e43efcff09a331d7e0c8ca3f5d02188737bb2497e50d7975d15f03(
    *,
    attributes: typing.Optional[typing.Sequence[typing.Union[Attribute, typing.Dict[builtins.str, typing.Any]]]] = None,
    cooldown: typing.Optional[jsii.Number] = None,
    down: typing.Optional[typing.Union[EcsAutoScaleDown, typing.Dict[builtins.str, typing.Any]]] = None,
    headroom: typing.Optional[typing.Union[EcsAutoScaleHeadroom, typing.Dict[builtins.str, typing.Any]]] = None,
    is_auto_config: typing.Optional[builtins.bool] = None,
    is_enabled: typing.Optional[builtins.bool] = None,
    should_scale_down_non_service_tasks: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3b1648eab235dd3306474e01a2494b8b03d85953db8534f57641c96c6359983(
    *,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    max_scale_down_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__247f1ed89c8287ff7f77b60c536d99f2040ff98cf8020ca9e33e851259192721(
    *,
    cpu_per_unit: typing.Optional[jsii.Number] = None,
    memory_per_unit: typing.Optional[jsii.Number] = None,
    num_of_units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3264a75640a8edad557155e40074f9fd12451cf509ae5a20917902a0e1042b1(
    *,
    job_queue_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f70955dc6486d6e50bba46be0b08edd3f15932703fda1aab9edd609df0a9e38(
    *,
    perform_at: typing.Optional[builtins.str] = None,
    should_optimize_ecs_ami: typing.Optional[builtins.bool] = None,
    time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ddba07a135cd470599832c6376126ef47d4578d3919ac20a70c3a6272844a64(
    *,
    action: typing.Optional[typing.Union[ScalingPolicyAction, typing.Dict[builtins.str, typing.Any]]] = None,
    cooldown: typing.Optional[jsii.Number] = None,
    dimension: typing.Optional[typing.Sequence[typing.Union[ScalingPolicyDimension, typing.Dict[builtins.str, typing.Any]]]] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    period: typing.Optional[jsii.Number] = None,
    policy_name: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    threshold: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61630ac35cd6275a396f037eecbe165d4c6d5bb6c85a6acb3e82e244b1cdd931(
    *,
    adjustment: typing.Optional[builtins.str] = None,
    maximum: typing.Optional[builtins.str] = None,
    minimum: typing.Optional[builtins.str] = None,
    min_target_capacity: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1140ce681bfa63e917681b7b340ada35e4eb863eae03e8a9574bfaac5bd724c7(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba768e6ef5a62c63e7aadaf97eae5cb36a88ad2361f245b7acce6300e8b8674a(
    *,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1b6b735b15d3de623e7f51f851353aee987008f8fdb1a3dda95a881fe0689a7(
    *,
    adjustment: typing.Optional[jsii.Number] = None,
    batch_size_percentage: typing.Optional[jsii.Number] = None,
    cron_expression: typing.Optional[builtins.str] = None,
    frequency: typing.Optional[builtins.str] = None,
    grace_period: typing.Optional[jsii.Number] = None,
    is_enabled: typing.Optional[builtins.bool] = None,
    scale_max_capacity: typing.Optional[jsii.Number] = None,
    scale_min_capacity: typing.Optional[jsii.Number] = None,
    scale_target_capacity: typing.Optional[jsii.Number] = None,
    start_time: typing.Optional[builtins.str] = None,
    task_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

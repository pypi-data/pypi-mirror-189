'''
# tf-digitalocean-droplet

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::DigitalOcean::Droplet` v1.0.0.

## Description

Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
[provisioning](https://www.terraform.io/docs/language/resources/provisioners/syntax.html).

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/digitalocean/TF-DigitalOcean-Droplet/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::DigitalOcean::Droplet \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-DigitalOcean-Droplet \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::DigitalOcean::Droplet`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-digitalocean-droplet+v1.0.0).
* Issues related to `TF::DigitalOcean::Droplet` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/digitalocean/TF-DigitalOcean-Droplet/docs/README.md).

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


class CfnDroplet(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-digitalocean-droplet.CfnDroplet",
):
    '''A CloudFormation ``TF::DigitalOcean::Droplet``.

    :cloudformationResource: TF::DigitalOcean::Droplet
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        image: builtins.str,
        name: builtins.str,
        region: builtins.str,
        size: builtins.str,
        backups: typing.Optional[builtins.bool] = None,
        ipv6: typing.Optional[builtins.bool] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        private_networking: typing.Optional[builtins.bool] = None,
        resize_disk: typing.Optional[builtins.bool] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
        volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::DigitalOcean::Droplet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param image: The Droplet image ID or slug.
        :param name: The Droplet name.
        :param region: The region to start in.
        :param size: The unique slug that indentifies the type of Droplet. You can find a list of available slugs on `DigitalOcean API documentation <https://developers.digitalocean.com/documentation/v2/#list-all-sizes>`_.
        :param backups: Boolean controlling if backups are made. Defaults to false. Default: false.
        :param ipv6: Boolean controlling if IPv6 is enabled. Defaults to false. Default: false.
        :param monitoring: Boolean controlling whether monitoring agent is installed. Defaults to false. Default: false.
        :param private_networking: Boolean controlling if private networking is enabled. When VPC is enabled on an account, this will provision the Droplet inside of your account's default VPC for the region. Use the ``vpc_uuid`` attribute to specify a different VPC.
        :param resize_disk: Boolean controlling whether to increase the disk size when resizing a Droplet. It defaults to ``true``. When set to ``false``, only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk size is a permanent change**. Increasing only RAM and CPU is reversible.
        :param ssh_keys: A list of SSH key IDs or fingerprints to enable in the format ``[12345, 123456]``. To retrieve this info, use the `DigitalOcean API <https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys>`_ or CLI (``doctl compute ssh-key list``). Once a Droplet is created keys can not be added or removed via this provider. Modifying this field will prompt you to destroy and recreate the Droplet.
        :param tags: A list of the tags to be applied to this Droplet.
        :param user_data: 
        :param volume_ids: 
        :param vpc_uuid: The ID of the VPC where the Droplet will be located.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bbe18f6017cb556a777147d594fec0bd0e52f090dd4b8ee6099cb248ece27f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDropletProps(
            image=image,
            name=name,
            region=region,
            size=size,
            backups=backups,
            ipv6=ipv6,
            monitoring=monitoring,
            private_networking=private_networking,
            resize_disk=resize_disk,
            ssh_keys=ssh_keys,
            tags=tags,
            user_data=user_data,
            volume_ids=volume_ids,
            vpc_uuid=vpc_uuid,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.CreatedAt``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDisk")
    def attr_disk(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.Disk``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDisk"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrIpv4Address")
    def attr_ipv4_address(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Ipv4Address``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpv4Address"))

    @builtins.property
    @jsii.member(jsii_name="attrIpv4AddressPrivate")
    def attr_ipv4_address_private(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Ipv4AddressPrivate``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpv4AddressPrivate"))

    @builtins.property
    @jsii.member(jsii_name="attrIpv6Address")
    def attr_ipv6_address(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Ipv6Address``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpv6Address"))

    @builtins.property
    @jsii.member(jsii_name="attrLocked")
    def attr_locked(self) -> _aws_cdk_ceddda9d.IResolvable:
        '''Attribute ``TF::DigitalOcean::Droplet.Locked``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(_aws_cdk_ceddda9d.IResolvable, jsii.get(self, "attrLocked"))

    @builtins.property
    @jsii.member(jsii_name="attrMemory")
    def attr_memory(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.Memory``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMemory"))

    @builtins.property
    @jsii.member(jsii_name="attrPriceHourly")
    def attr_price_hourly(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.PriceHourly``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPriceHourly"))

    @builtins.property
    @jsii.member(jsii_name="attrPriceMonthly")
    def attr_price_monthly(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.PriceMonthly``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPriceMonthly"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Status``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="attrUrn")
    def attr_urn(self) -> builtins.str:
        '''Attribute ``TF::DigitalOcean::Droplet.Urn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrn"))

    @builtins.property
    @jsii.member(jsii_name="attrVcpus")
    def attr_vcpus(self) -> jsii.Number:
        '''Attribute ``TF::DigitalOcean::Droplet.Vcpus``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVcpus"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDropletProps":
        '''Resource props.'''
        return typing.cast("CfnDropletProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-digitalocean-droplet.CfnDropletProps",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "name": "name",
        "region": "region",
        "size": "size",
        "backups": "backups",
        "ipv6": "ipv6",
        "monitoring": "monitoring",
        "private_networking": "privateNetworking",
        "resize_disk": "resizeDisk",
        "ssh_keys": "sshKeys",
        "tags": "tags",
        "user_data": "userData",
        "volume_ids": "volumeIds",
        "vpc_uuid": "vpcUuid",
    },
)
class CfnDropletProps:
    def __init__(
        self,
        *,
        image: builtins.str,
        name: builtins.str,
        region: builtins.str,
        size: builtins.str,
        backups: typing.Optional[builtins.bool] = None,
        ipv6: typing.Optional[builtins.bool] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        private_networking: typing.Optional[builtins.bool] = None,
        resize_disk: typing.Optional[builtins.bool] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
        volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Provides a DigitalOcean Droplet resource.

        This can be used to create,
        modify, and delete Droplets. Droplets also support
        `provisioning <https://www.terraform.io/docs/language/resources/provisioners/syntax.html>`_.

        :param image: The Droplet image ID or slug.
        :param name: The Droplet name.
        :param region: The region to start in.
        :param size: The unique slug that indentifies the type of Droplet. You can find a list of available slugs on `DigitalOcean API documentation <https://developers.digitalocean.com/documentation/v2/#list-all-sizes>`_.
        :param backups: Boolean controlling if backups are made. Defaults to false. Default: false.
        :param ipv6: Boolean controlling if IPv6 is enabled. Defaults to false. Default: false.
        :param monitoring: Boolean controlling whether monitoring agent is installed. Defaults to false. Default: false.
        :param private_networking: Boolean controlling if private networking is enabled. When VPC is enabled on an account, this will provision the Droplet inside of your account's default VPC for the region. Use the ``vpc_uuid`` attribute to specify a different VPC.
        :param resize_disk: Boolean controlling whether to increase the disk size when resizing a Droplet. It defaults to ``true``. When set to ``false``, only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk size is a permanent change**. Increasing only RAM and CPU is reversible.
        :param ssh_keys: A list of SSH key IDs or fingerprints to enable in the format ``[12345, 123456]``. To retrieve this info, use the `DigitalOcean API <https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys>`_ or CLI (``doctl compute ssh-key list``). Once a Droplet is created keys can not be added or removed via this provider. Modifying this field will prompt you to destroy and recreate the Droplet.
        :param tags: A list of the tags to be applied to this Droplet.
        :param user_data: 
        :param volume_ids: 
        :param vpc_uuid: The ID of the VPC where the Droplet will be located.

        :schema: CfnDropletProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c94da30c1219e50d8de5b3f4c657de927f49c5f84dddec7f9e1e786b17e6d1)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument backups", value=backups, expected_type=type_hints["backups"])
            check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument private_networking", value=private_networking, expected_type=type_hints["private_networking"])
            check_type(argname="argument resize_disk", value=resize_disk, expected_type=type_hints["resize_disk"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument volume_ids", value=volume_ids, expected_type=type_hints["volume_ids"])
            check_type(argname="argument vpc_uuid", value=vpc_uuid, expected_type=type_hints["vpc_uuid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image": image,
            "name": name,
            "region": region,
            "size": size,
        }
        if backups is not None:
            self._values["backups"] = backups
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if private_networking is not None:
            self._values["private_networking"] = private_networking
        if resize_disk is not None:
            self._values["resize_disk"] = resize_disk
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if tags is not None:
            self._values["tags"] = tags
        if user_data is not None:
            self._values["user_data"] = user_data
        if volume_ids is not None:
            self._values["volume_ids"] = volume_ids
        if vpc_uuid is not None:
            self._values["vpc_uuid"] = vpc_uuid

    @builtins.property
    def image(self) -> builtins.str:
        '''The Droplet image ID or slug.

        :schema: CfnDropletProps#Image
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The Droplet name.

        :schema: CfnDropletProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region to start in.

        :schema: CfnDropletProps#Region
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''The unique slug that indentifies the type of Droplet.

        You can find a list of available slugs on `DigitalOcean API documentation <https://developers.digitalocean.com/documentation/v2/#list-all-sizes>`_.

        :schema: CfnDropletProps#Size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backups(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling if backups are made.

        Defaults to
        false.

        :default: false.

        :schema: CfnDropletProps#Backups
        '''
        result = self._values.get("backups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ipv6(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling if IPv6 is enabled.

        Defaults to false.

        :default: false.

        :schema: CfnDropletProps#Ipv6
        '''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def monitoring(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling whether monitoring agent is installed.

        Defaults to false.

        :default: false.

        :schema: CfnDropletProps#Monitoring
        '''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_networking(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling if private networking is enabled.

        When VPC is enabled on an account, this will provision the
        Droplet inside of your account's default VPC for the region. Use the
        ``vpc_uuid`` attribute to specify a different VPC.

        :schema: CfnDropletProps#PrivateNetworking
        '''
        result = self._values.get("private_networking")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def resize_disk(self) -> typing.Optional[builtins.bool]:
        '''Boolean controlling whether to increase the disk size when resizing a Droplet.

        It defaults to ``true``. When set to ``false``,
        only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk
        size is a permanent change**. Increasing only RAM and CPU is reversible.

        :schema: CfnDropletProps#ResizeDisk
        '''
        result = self._values.get("resize_disk")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of SSH key IDs or fingerprints to enable in the format ``[12345, 123456]``.

        To retrieve this info, use the
        `DigitalOcean API <https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys>`_
        or CLI (``doctl compute ssh-key list``). Once a Droplet is created keys can not
        be added or removed via this provider. Modifying this field will prompt you
        to destroy and recreate the Droplet.

        :schema: CfnDropletProps#SshKeys
        '''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the tags to be applied to this Droplet.

        :schema: CfnDropletProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDropletProps#UserData
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnDropletProps#VolumeIds
        '''
        result = self._values.get("volume_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_uuid(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC where the Droplet will be located.

        :schema: CfnDropletProps#VpcUuid
        '''
        result = self._values.get("vpc_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDropletProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDroplet",
    "CfnDropletProps",
]

publication.publish()

def _typecheckingstub__1bbe18f6017cb556a777147d594fec0bd0e52f090dd4b8ee6099cb248ece27f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    image: builtins.str,
    name: builtins.str,
    region: builtins.str,
    size: builtins.str,
    backups: typing.Optional[builtins.bool] = None,
    ipv6: typing.Optional[builtins.bool] = None,
    monitoring: typing.Optional[builtins.bool] = None,
    private_networking: typing.Optional[builtins.bool] = None,
    resize_disk: typing.Optional[builtins.bool] = None,
    ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_data: typing.Optional[builtins.str] = None,
    volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c94da30c1219e50d8de5b3f4c657de927f49c5f84dddec7f9e1e786b17e6d1(
    *,
    image: builtins.str,
    name: builtins.str,
    region: builtins.str,
    size: builtins.str,
    backups: typing.Optional[builtins.bool] = None,
    ipv6: typing.Optional[builtins.bool] = None,
    monitoring: typing.Optional[builtins.bool] = None,
    private_networking: typing.Optional[builtins.bool] = None,
    resize_disk: typing.Optional[builtins.bool] = None,
    ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_data: typing.Optional[builtins.str] = None,
    volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

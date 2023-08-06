'''
# mongodb-atlas-networkpeering

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MongoDB::Atlas::NetworkPeering` v1.2.0.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated. Please use the respective `@mongodbatlas-awscdk/*` scoped package instead

---


## Description

This resource allows to create, read, update and delete a network peering

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MongoDB::Atlas::NetworkPeering \
  --publisher-id bb989456c78c398a858fef18f2ca1bfc1fbba082 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/bb989456c78c398a858fef18f2ca1bfc1fbba082/MongoDB-Atlas-NetworkPeering \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MongoDB::Atlas::NetworkPeering`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmongodb-atlas-networkpeering+v1.2.0).
* Issues related to `MongoDB::Atlas::NetworkPeering` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-networkpeering.ApiKeyDefinition",
    jsii_struct_bases=[],
    name_mapping={"private_key": "privateKey", "public_key": "publicKey"},
)
class ApiKeyDefinition:
    def __init__(
        self,
        *,
        private_key: typing.Optional[builtins.str] = None,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_key: 
        :param public_key: 

        :stability: deprecated
        :schema: apiKeyDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e2540ac3da84f62990444c2a98fc6f26942672d65708339e18143a70f286bd)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if private_key is not None:
            self._values["private_key"] = private_key
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: apiKeyDefinition#PrivateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: apiKeyDefinition#PublicKey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnNetworkPeering(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-networkpeering.CfnNetworkPeering",
):
    '''A CloudFormation ``MongoDB::Atlas::NetworkPeering``.

    :cloudformationResource: MongoDB::Atlas::NetworkPeering
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
        vpc_id: builtins.str,
        accepter_region_name: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        container_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        route_table_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::NetworkPeering``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_keys: 
        :param project_id: (deprecated) The unique identifier of the project.
        :param vpc_id: (deprecated) Unique identifier of the peer VPC.
        :param accepter_region_name: (deprecated) AWS region where the peer VPC resides. Returns null if the region is the same region in which the Atlas VPC resides.
        :param aws_account_id: (deprecated) AWS account ID of the owner of the peer VPC.
        :param connection_id: (deprecated) Unique identifier for the peering connection.
        :param container_id: (deprecated) Unique identifier of the Atlas VPC container for the AWS region.
        :param provider_name: (deprecated) The name of the provider.
        :param route_table_cidr_block: (deprecated) Peer VPC CIDR block or subnet.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c8aa98d1839c0b9b5aabe0c756fce06abaf0b33b53639e8a7219b957dd9a81c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkPeeringProps(
            api_keys=api_keys,
            project_id=project_id,
            vpc_id=vpc_id,
            accepter_region_name=accepter_region_name,
            aws_account_id=aws_account_id,
            connection_id=connection_id,
            container_id=container_id,
            provider_name=provider_name,
            route_table_cidr_block=route_table_cidr_block,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrErrorStateName")
    def attr_error_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.ErrorStateName``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorStateName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusName")
    def attr_status_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.StatusName``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusName"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnNetworkPeeringProps":
        '''Resource props.'''
        return typing.cast("CfnNetworkPeeringProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-networkpeering.CfnNetworkPeeringProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_keys": "apiKeys",
        "project_id": "projectId",
        "vpc_id": "vpcId",
        "accepter_region_name": "accepterRegionName",
        "aws_account_id": "awsAccountId",
        "connection_id": "connectionId",
        "container_id": "containerId",
        "provider_name": "providerName",
        "route_table_cidr_block": "routeTableCidrBlock",
    },
)
class CfnNetworkPeeringProps:
    def __init__(
        self,
        *,
        api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
        vpc_id: builtins.str,
        accepter_region_name: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        container_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        route_table_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) This resource allows to create, read, update and delete a network peering.

        :param api_keys: 
        :param project_id: (deprecated) The unique identifier of the project.
        :param vpc_id: (deprecated) Unique identifier of the peer VPC.
        :param accepter_region_name: (deprecated) AWS region where the peer VPC resides. Returns null if the region is the same region in which the Atlas VPC resides.
        :param aws_account_id: (deprecated) AWS account ID of the owner of the peer VPC.
        :param connection_id: (deprecated) Unique identifier for the peering connection.
        :param container_id: (deprecated) Unique identifier of the Atlas VPC container for the AWS region.
        :param provider_name: (deprecated) The name of the provider.
        :param route_table_cidr_block: (deprecated) Peer VPC CIDR block or subnet.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__215051c29cb9269b5a016625f6a2114ebf78b7ad03bf98eefcfce52b2c27d496)
            check_type(argname="argument api_keys", value=api_keys, expected_type=type_hints["api_keys"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument accepter_region_name", value=accepter_region_name, expected_type=type_hints["accepter_region_name"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument container_id", value=container_id, expected_type=type_hints["container_id"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument route_table_cidr_block", value=route_table_cidr_block, expected_type=type_hints["route_table_cidr_block"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_keys": api_keys,
            "project_id": project_id,
            "vpc_id": vpc_id,
        }
        if accepter_region_name is not None:
            self._values["accepter_region_name"] = accepter_region_name
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if container_id is not None:
            self._values["container_id"] = container_id
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if route_table_cidr_block is not None:
            self._values["route_table_cidr_block"] = route_table_cidr_block

    @builtins.property
    def api_keys(self) -> ApiKeyDefinition:
        '''
        :stability: deprecated
        :schema: CfnNetworkPeeringProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        assert result is not None, "Required property 'api_keys' is missing"
        return typing.cast(ApiKeyDefinition, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''(deprecated) The unique identifier of the project.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''(deprecated) Unique identifier of the peer VPC.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#VpcId
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepter_region_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) AWS region where the peer VPC resides.

        Returns null if the region is the same region in which the Atlas VPC resides.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#AccepterRegionName
        '''
        result = self._values.get("accepter_region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''(deprecated) AWS account ID of the owner of the peer VPC.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#AwsAccountId
        '''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Unique identifier for the peering connection.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#ConnectionId
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_id(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Unique identifier of the Atlas VPC container for the AWS region.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#ContainerId
        '''
        result = self._values.get("container_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of the provider.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_table_cidr_block(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Peer VPC CIDR block or subnet.

        :stability: deprecated
        :schema: CfnNetworkPeeringProps#RouteTableCIDRBlock
        '''
        result = self._values.get("route_table_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkPeeringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiKeyDefinition",
    "CfnNetworkPeering",
    "CfnNetworkPeeringProps",
]

publication.publish()

def _typecheckingstub__52e2540ac3da84f62990444c2a98fc6f26942672d65708339e18143a70f286bd(
    *,
    private_key: typing.Optional[builtins.str] = None,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8aa98d1839c0b9b5aabe0c756fce06abaf0b33b53639e8a7219b957dd9a81c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
    vpc_id: builtins.str,
    accepter_region_name: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    connection_id: typing.Optional[builtins.str] = None,
    container_id: typing.Optional[builtins.str] = None,
    provider_name: typing.Optional[builtins.str] = None,
    route_table_cidr_block: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215051c29cb9269b5a016625f6a2114ebf78b7ad03bf98eefcfce52b2c27d496(
    *,
    api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
    vpc_id: builtins.str,
    accepter_region_name: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    connection_id: typing.Optional[builtins.str] = None,
    container_id: typing.Optional[builtins.str] = None,
    provider_name: typing.Optional[builtins.str] = None,
    route_table_cidr_block: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

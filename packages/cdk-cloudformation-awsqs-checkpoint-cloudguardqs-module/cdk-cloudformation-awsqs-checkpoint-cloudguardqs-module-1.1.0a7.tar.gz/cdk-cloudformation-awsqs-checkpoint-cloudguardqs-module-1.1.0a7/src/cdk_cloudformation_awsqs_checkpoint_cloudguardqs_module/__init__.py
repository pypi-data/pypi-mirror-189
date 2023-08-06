'''
# awsqs-checkpoint-cloudguardqs-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::CheckPoint::CloudGuardQS::MODULE` v1.1.0.

## Description

Schema for Module Fragment of type AWSQS::CheckPoint::CloudGuardQS::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::CheckPoint::CloudGuardQS::MODULE \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-CheckPoint-CloudGuardQS-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::CheckPoint::CloudGuardQS::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-checkpoint-cloudguardqs-module+v1.1.0).
* Issues related to `AWSQS::CheckPoint::CloudGuardQS::MODULE` should be reported to the [publisher](undefined).

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


class CfnCloudGuardQsModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModule",
):
    '''A CloudFormation ``AWSQS::CheckPoint::CloudGuardQS::MODULE``.

    :cloudformationResource: AWSQS::CheckPoint::CloudGuardQS::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``AWSQS::CheckPoint::CloudGuardQS::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fff8e443652c7933b6b9f6847fe30fc28ad6cc4d8ac8bf4a83150f9af8a00289)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudGuardQsModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudGuardQsModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudGuardQsModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCloudGuardQsModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type AWSQS::CheckPoint::CloudGuardQS::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCloudGuardQsModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCloudGuardQsModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCloudGuardQsModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599eea0487839a1d4761f141456cef9fc7b05751a268093d953445b6ed361137)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCloudGuardQsModulePropsParameters"]:
        '''
        :schema: CfnCloudGuardQsModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCloudGuardQsModulePropsResources"]:
        '''
        :schema: CfnCloudGuardQsModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "admin_cidr": "adminCidr",
        "admin_email": "adminEmail",
        "alb_protocol": "albProtocol",
        "allocate_public_address": "allocatePublicAddress",
        "allow_upload_download": "allowUploadDownload",
        "availability_zones": "availabilityZones",
        "certificate": "certificate",
        "cloud_watch": "cloudWatch",
        "control_gateway_over_private_or_public_address": "controlGatewayOverPrivateOrPublicAddress",
        "create_private_subnets": "createPrivateSubnets",
        "create_tgw_subnets": "createTgwSubnets",
        "elb_clients": "elbClients",
        "elb_port": "elbPort",
        "elb_type": "elbType",
        "enable_instance_connect": "enableInstanceConnect",
        "enable_volume_encryption": "enableVolumeEncryption",
        "gateway_instance_type": "gatewayInstanceType",
        "gateway_management": "gatewayManagement",
        "gateway_password_hash": "gatewayPasswordHash",
        "gateways_addresses": "gatewaysAddresses",
        "gateways_blades": "gatewaysBlades",
        "gateway_sic_key": "gatewaySicKey",
        "gateways_max_size": "gatewaysMaxSize",
        "gateways_min_size": "gatewaysMinSize",
        "gateways_policy": "gatewaysPolicy",
        "gateways_target_groups": "gatewaysTargetGroups",
        "gateway_version": "gatewayVersion",
        "key_name": "keyName",
        "load_balancers_type": "loadBalancersType",
        "management_deploy": "managementDeploy",
        "management_hostname": "managementHostname",
        "management_instance_type": "managementInstanceType",
        "management_password_hash": "managementPasswordHash",
        "management_permissions": "managementPermissions",
        "management_predefined_role": "managementPredefinedRole",
        "management_sic_key": "managementSicKey",
        "management_stack_volume_size": "managementStackVolumeSize",
        "management_version": "managementVersion",
        "nlb_protocol": "nlbProtocol",
        "ntp_primary": "ntpPrimary",
        "ntp_secondary": "ntpSecondary",
        "number_of_a_zs": "numberOfAZs",
        "permissions": "permissions",
        "primary_management": "primaryManagement",
        "private_subnet1_cidr": "privateSubnet1Cidr",
        "private_subnet2_cidr": "privateSubnet2Cidr",
        "private_subnet3_cidr": "privateSubnet3Cidr",
        "private_subnet4_cidr": "privateSubnet4Cidr",
        "provision_tag": "provisionTag",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "public_subnet3_cidr": "publicSubnet3Cidr",
        "public_subnet4_cidr": "publicSubnet4Cidr",
        "security_gateway_volume_size": "securityGatewayVolumeSize",
        "server_ami": "serverAmi",
        "server_instance_type": "serverInstanceType",
        "server_name": "serverName",
        "servers_deploy": "serversDeploy",
        "servers_max_size": "serversMaxSize",
        "servers_min_size": "serversMinSize",
        "servers_target_groups": "serversTargetGroups",
        "service_port": "servicePort",
        "shell_management_stack": "shellManagementStack",
        "shell_security_gateway_stack": "shellSecurityGatewayStack",
        "source_security_group": "sourceSecurityGroup",
        "sts_roles": "stsRoles",
        "tgw_subnet1_cidr": "tgwSubnet1Cidr",
        "tgw_subnet2_cidr": "tgwSubnet2Cidr",
        "tgw_subnet3_cidr": "tgwSubnet3Cidr",
        "tgw_subnet4_cidr": "tgwSubnet4Cidr",
        "trusted_account": "trustedAccount",
        "vpccidr": "vpccidr",
    },
)
class CfnCloudGuardQsModulePropsParameters:
    def __init__(
        self,
        *,
        admin_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersAdminCidr", typing.Dict[builtins.str, typing.Any]]] = None,
        admin_email: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersAdminEmail", typing.Dict[builtins.str, typing.Any]]] = None,
        alb_protocol: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersAlbProtocol", typing.Dict[builtins.str, typing.Any]]] = None,
        allocate_public_address: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersAllocatePublicAddress", typing.Dict[builtins.str, typing.Any]]] = None,
        allow_upload_download: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersAllowUploadDownload", typing.Dict[builtins.str, typing.Any]]] = None,
        availability_zones: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersAvailabilityZones", typing.Dict[builtins.str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_watch: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersCloudWatch", typing.Dict[builtins.str, typing.Any]]] = None,
        control_gateway_over_private_or_public_address: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress", typing.Dict[builtins.str, typing.Any]]] = None,
        create_private_subnets: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets", typing.Dict[builtins.str, typing.Any]]] = None,
        create_tgw_subnets: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersCreateTgwSubnets", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_clients: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersElbClients", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_port: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersElbPort", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_type: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersElbType", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_instance_connect: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersEnableInstanceConnect", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_volume_encryption: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_instance_type: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewayInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_management: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewayManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_password_hash: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewayPasswordHash", typing.Dict[builtins.str, typing.Any]]] = None,
        gateways_addresses: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaysAddresses", typing.Dict[builtins.str, typing.Any]]] = None,
        gateways_blades: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaysBlades", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_sic_key: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaySicKey", typing.Dict[builtins.str, typing.Any]]] = None,
        gateways_max_size: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaysMaxSize", typing.Dict[builtins.str, typing.Any]]] = None,
        gateways_min_size: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaysMinSize", typing.Dict[builtins.str, typing.Any]]] = None,
        gateways_policy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaysPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        gateways_target_groups: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_version: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersGatewayVersion", typing.Dict[builtins.str, typing.Any]]] = None,
        key_name: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersKeyName", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancers_type: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersLoadBalancersType", typing.Dict[builtins.str, typing.Any]]] = None,
        management_deploy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementDeploy", typing.Dict[builtins.str, typing.Any]]] = None,
        management_hostname: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        management_instance_type: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        management_password_hash: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementPasswordHash", typing.Dict[builtins.str, typing.Any]]] = None,
        management_permissions: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementPermissions", typing.Dict[builtins.str, typing.Any]]] = None,
        management_predefined_role: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementPredefinedRole", typing.Dict[builtins.str, typing.Any]]] = None,
        management_sic_key: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementSicKey", typing.Dict[builtins.str, typing.Any]]] = None,
        management_stack_volume_size: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        management_version: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersManagementVersion", typing.Dict[builtins.str, typing.Any]]] = None,
        nlb_protocol: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersNlbProtocol", typing.Dict[builtins.str, typing.Any]]] = None,
        ntp_primary: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersNtpPrimary", typing.Dict[builtins.str, typing.Any]]] = None,
        ntp_secondary: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersNtpSecondary", typing.Dict[builtins.str, typing.Any]]] = None,
        number_of_a_zs: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersNumberOfAZs", typing.Dict[builtins.str, typing.Any]]] = None,
        permissions: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPermissions", typing.Dict[builtins.str, typing.Any]]] = None,
        primary_management: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPrimaryManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        provision_tag: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersProvisionTag", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet3_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet4_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        security_gateway_volume_size: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        server_ami: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServerAmi", typing.Dict[builtins.str, typing.Any]]] = None,
        server_instance_type: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServerInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        server_name: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServerName", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_deploy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServersDeploy", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_max_size: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServersMaxSize", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_min_size: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServersMinSize", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_target_groups: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServersTargetGroups", typing.Dict[builtins.str, typing.Any]]] = None,
        service_port: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersServicePort", typing.Dict[builtins.str, typing.Any]]] = None,
        shell_management_stack: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersShellManagementStack", typing.Dict[builtins.str, typing.Any]]] = None,
        shell_security_gateway_stack: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack", typing.Dict[builtins.str, typing.Any]]] = None,
        source_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersSourceSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        sts_roles: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersStsRoles", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet1_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet2_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet3_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet4_cidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        trusted_account: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersTrustedAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        vpccidr: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsParametersVpccidr", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param admin_cidr: Allow web, SSH, and graphical clients only from this network to communicate with the Security Management Server.
        :param admin_email: Notifications about scaling events will be sent to this email address (optional).
        :param alb_protocol: The protocol to use on the Application Load Balancer. If Network Load Balancer was selected this section will be ignored. Default: HTTP. Allowed values: HTTP, HTTPS
        :param allocate_public_address: Allocate an elastic IP for the Management. Default: true
        :param allow_upload_download: Automatically download Blade Contracts and other important data. Improve product experience by sending data to Check Point. Default: true
        :param availability_zones: List of Availability Zones (AZs) to use for the subnets in the VPC. Select at least two
        :param certificate: Amazon Resource Name (ARN) of an HTTPS Certificate, ignored if the selected protocol is HTTP (for the ALBProtocol parameter).
        :param cloud_watch: Report Check Point specific CloudWatch metrics. Default: false
        :param control_gateway_over_private_or_public_address: Determines if the gateways are provisioned using their private or public address. Default: private. Allowed values: private, public
        :param create_private_subnets: Set to false to create only public subnets. If false, the CIDR parameters for ALL private subnets will be ignored. Default: true
        :param create_tgw_subnets: Set true for creating designated subnets for VPC TGW attachments. If false, the CIDR parameters for the TGW subnets will be ignored. Default: false
        :param elb_clients: Allow clients only from this network to communicate with the Web Servers. Default: 0.0.0.0/0
        :param elb_port: Port for the ELB. Default: 8080
        :param elb_type: The Elasitc Load Balancer Type. Default: none. Allowed values: none, internal, internet-facing
        :param enable_instance_connect: Enable SSH connection over AWS web console. Default: false
        :param enable_volume_encryption: Encrypt Environment instances volume with default AWS KMS key. Default: true
        :param gateway_instance_type: The EC2 instance type for the Security Gateways. Default: c5.xlarge. Allowed values: c5.xlarge, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.18xlarge, c5n.large, c5n.xlarge, c5n.2xlarge, c5n.4xlarge, c5n.9xlarge, c5n.18xlarge
        :param gateway_management: Select 'Over the internet' if any of the gateways you wish to manage are not directly accessed via their private IP address. Default: 'Locally managed'. Allowed values: Locally managed, Over the internet
        :param gateway_password_hash: Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).
        :param gateways_addresses: Allow gateways only from this network to communicate with the Security Management Server.
        :param gateways_blades: Turn on the Intrusion Prevention System, Application Control, Anti-Virus and Anti-Bot Blades (these and additional Blades can be manually turned on or off later). Default: true
        :param gateway_sic_key: The Secure Internal Communication key creates trusted connections between Check Point components. Choose a random string consisting of at least 8 alphanumeric characters.
        :param gateways_max_size: The maximal number of Security Gateways.
        :param gateways_min_size: The minimal number of Security Gateways.
        :param gateways_policy: The name of the Security Policy package to be installed on the gateways in the Security Gateways Auto Scaling group. Default: Standard
        :param gateways_target_groups: A list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces) (optional).
        :param gateway_version: The version and license to install on the Security Gateways. Default: R80.40-PAYG-NGTP-GW. Allowed values: R80.40-BYOL-GW, R80.40-PAYG-NGTP-GW, R80.40-PAYG-NGTX-GW, R81-BYOL-GW, R81-PAYG-NGTP-GW, R81-PAYG-NGTX-GW
        :param key_name: The EC2 Key Pair to allow SSH access to the instances. For more detail visit: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
        :param load_balancers_type: Use Network Load Balancer if you wish to preserve the source IP address and Application Load Balancer if you wish to perform SSL Offloading. Default: Network Load Balancer. Allowed values: Network Load Balancer, Application Load Balancer
        :param management_deploy: Select false to use an existing Security Management Server or to deploy one later and to ignore the other parameters of this section. Default: true
        :param management_hostname: (optional). Default: mgmt-aws
        :param management_instance_type: The EC2 instance type of the Security Management Server. Default: m5.xlarge. Allowed values: m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.12xlarge, m5.24xlarge
        :param management_password_hash: Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).
        :param management_permissions: IAM role to attach to the instance profile of the Management Server. Default: Create with read permissions. Allowed values: None (configure later), Use existing (specify an existing IAM role name), Create with assume role permissions (specify an STS role ARN), Create with read permissions, Create with read-write permissions
        :param management_predefined_role: A predefined IAM role to attach to the instance profile. Ignored if IAM role is not set to 'Use existing'
        :param management_sic_key: Mandatory only if deploying a secondary Management Server, the Secure Internal Communication key creates trusted connections between Check Point components. Choose a random string consisting of at least 8 alphanumeric characters
        :param management_stack_volume_size: EBS Volume size of the management server.
        :param management_version: The version and license to install on the Security Management Server. Default: R80.40-PAYG-MGMT. Allowed values: R80.40-BYOL-MGMT, R80.40-PAYG-MGMT, R81-BYOL-MGMT, R81-PAYG-MGMT
        :param nlb_protocol: The protocol to use on the Network Load Balancer. If Application Load Balancer was selected this section will be ignored. Default: TCP. Allowed values: TCP, TLS, UDP, TCP_UDP
        :param ntp_primary: (optional). Default: 169.254.169.123
        :param ntp_secondary: (optional). Default: 0.pool.ntp.org
        :param number_of_a_zs: Number of Availability Zones to use in the VPC. This must match your selections in the list of Availability Zones parameter. Default: 2
        :param permissions: IAM Permissions for the management server. Default: Create with read permissions. Allowed values: Create with read permissions Create with read-write permissions Create with assume role permissions (specify an STS role ARN)
        :param primary_management: Determines if this is the primary Management Server or not. Default: true
        :param private_subnet1_cidr: CIDR block for private subnet 1 located in the 1st Availability Zone. Default: 10.0.11.0/24
        :param private_subnet2_cidr: CIDR block for private subnet 2 located in the 2nd Availability Zone. Default: 10.0.21.0/24
        :param private_subnet3_cidr: CIDR block for private subnet 3 located in the 3rd Availability Zone. Default: 10.0.31.0/24
        :param private_subnet4_cidr: CIDR block for private subnet 4 located in the 4th Availability Zone. Default: 10.0.41.0/24
        :param provision_tag: The tag is used by the Security Management Server to automatically provision the Security Gateways. Must be up to 12 alphanumeric characters and unique for each Quick Start deployment. Default: quickstart
        :param public_subnet1_cidr: CIDR block for public subnet 1 located in the 1st Availability Zone. If you choose to deploy a Security Management Server it will be deployed in this subnet. Default: 10.0.10.0/24
        :param public_subnet2_cidr: CIDR block for public subnet 2 located in the 2nd Availability Zone. Default: 10.0.20.0/24
        :param public_subnet3_cidr: CIDR block for public subnet 3 located in the 3rd Availability Zone. Default: 10.0.30.0/24
        :param public_subnet4_cidr: CIDR block for public subnet 4 located in the 4th Availability Zone. Default: 10.0.40.0/24
        :param security_gateway_volume_size: EBS Volume size of the security gateway server.
        :param server_ami: The Amazon Machine Image ID of a preconfigured web server (e.g. ami-0dc7dc63).
        :param server_instance_type: The EC2 instance type for the web servers. Default: t3.micro. Allowed values: t3.nano, t3.micro, t3.small, t3.medium, t3.large, t3.xlarge, t3.2xlarge
        :param server_name: The servers name tag. Default: Server
        :param servers_deploy: Select true to deploy web servers and an internal Application Load Balancer. If you select false the other parameters of this section will be ignored. Default: false
        :param servers_max_size: The maximal number of servers in the Auto Scaling group. Default: 10
        :param servers_min_size: The minimal number of servers in the Auto Scaling group. Default: 2
        :param servers_target_groups: An optional list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces).
        :param service_port: The external Load Balancer listens to this port. Leave this field blank to use default ports: 80 for HTTP and 443 for HTTPS
        :param shell_management_stack: Change the admin shell to enable advanced command line configuration. Default: /etc/cli.sh. Allowed values: /etc/cli.sh, /bin/bash, /bin/csh, /bin/tcsh
        :param shell_security_gateway_stack: Change the admin shell to enable advanced command line configuration. Default: /etc/cli.sh. Allowed Values: /etc/cli.sh /bin/bash /bin/csh /bin/tcsh
        :param source_security_group: The ID of Security Group from which access will be allowed to the instances in this Auto Scaling group.
        :param sts_roles: The IAM role will be able to assume these STS Roles (comma separated list of ARNs, without spaces).
        :param tgw_subnet1_cidr: CIDR block for TGW subnet 1 located in Availability Zone 1. Default: 10.0.12.0/24
        :param tgw_subnet2_cidr: CIDR block for TGW subnet 2 located in Availability Zone 2. Default: 10.0.22.0/24
        :param tgw_subnet3_cidr: CIDR block for TGW subnet 3 located in Availability Zone 3. Default: 10.0.32.0/24
        :param tgw_subnet4_cidr: CIDR block for TGW subnet 4 located in Availability Zone 4. Default: 10.0.42.0/24
        :param trusted_account: A 12 digits number that represents the ID of a trusted account. IAM users in this account will be able assume the IAM role and receive the permissions attached to it.
        :param vpccidr: CIDR block for the VPC. Default: 10.0.0.0/16

        :schema: CfnCloudGuardQsModulePropsParameters
        '''
        if isinstance(admin_cidr, dict):
            admin_cidr = CfnCloudGuardQsModulePropsParametersAdminCidr(**admin_cidr)
        if isinstance(admin_email, dict):
            admin_email = CfnCloudGuardQsModulePropsParametersAdminEmail(**admin_email)
        if isinstance(alb_protocol, dict):
            alb_protocol = CfnCloudGuardQsModulePropsParametersAlbProtocol(**alb_protocol)
        if isinstance(allocate_public_address, dict):
            allocate_public_address = CfnCloudGuardQsModulePropsParametersAllocatePublicAddress(**allocate_public_address)
        if isinstance(allow_upload_download, dict):
            allow_upload_download = CfnCloudGuardQsModulePropsParametersAllowUploadDownload(**allow_upload_download)
        if isinstance(availability_zones, dict):
            availability_zones = CfnCloudGuardQsModulePropsParametersAvailabilityZones(**availability_zones)
        if isinstance(certificate, dict):
            certificate = CfnCloudGuardQsModulePropsParametersCertificate(**certificate)
        if isinstance(cloud_watch, dict):
            cloud_watch = CfnCloudGuardQsModulePropsParametersCloudWatch(**cloud_watch)
        if isinstance(control_gateway_over_private_or_public_address, dict):
            control_gateway_over_private_or_public_address = CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress(**control_gateway_over_private_or_public_address)
        if isinstance(create_private_subnets, dict):
            create_private_subnets = CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets(**create_private_subnets)
        if isinstance(create_tgw_subnets, dict):
            create_tgw_subnets = CfnCloudGuardQsModulePropsParametersCreateTgwSubnets(**create_tgw_subnets)
        if isinstance(elb_clients, dict):
            elb_clients = CfnCloudGuardQsModulePropsParametersElbClients(**elb_clients)
        if isinstance(elb_port, dict):
            elb_port = CfnCloudGuardQsModulePropsParametersElbPort(**elb_port)
        if isinstance(elb_type, dict):
            elb_type = CfnCloudGuardQsModulePropsParametersElbType(**elb_type)
        if isinstance(enable_instance_connect, dict):
            enable_instance_connect = CfnCloudGuardQsModulePropsParametersEnableInstanceConnect(**enable_instance_connect)
        if isinstance(enable_volume_encryption, dict):
            enable_volume_encryption = CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption(**enable_volume_encryption)
        if isinstance(gateway_instance_type, dict):
            gateway_instance_type = CfnCloudGuardQsModulePropsParametersGatewayInstanceType(**gateway_instance_type)
        if isinstance(gateway_management, dict):
            gateway_management = CfnCloudGuardQsModulePropsParametersGatewayManagement(**gateway_management)
        if isinstance(gateway_password_hash, dict):
            gateway_password_hash = CfnCloudGuardQsModulePropsParametersGatewayPasswordHash(**gateway_password_hash)
        if isinstance(gateways_addresses, dict):
            gateways_addresses = CfnCloudGuardQsModulePropsParametersGatewaysAddresses(**gateways_addresses)
        if isinstance(gateways_blades, dict):
            gateways_blades = CfnCloudGuardQsModulePropsParametersGatewaysBlades(**gateways_blades)
        if isinstance(gateway_sic_key, dict):
            gateway_sic_key = CfnCloudGuardQsModulePropsParametersGatewaySicKey(**gateway_sic_key)
        if isinstance(gateways_max_size, dict):
            gateways_max_size = CfnCloudGuardQsModulePropsParametersGatewaysMaxSize(**gateways_max_size)
        if isinstance(gateways_min_size, dict):
            gateways_min_size = CfnCloudGuardQsModulePropsParametersGatewaysMinSize(**gateways_min_size)
        if isinstance(gateways_policy, dict):
            gateways_policy = CfnCloudGuardQsModulePropsParametersGatewaysPolicy(**gateways_policy)
        if isinstance(gateways_target_groups, dict):
            gateways_target_groups = CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups(**gateways_target_groups)
        if isinstance(gateway_version, dict):
            gateway_version = CfnCloudGuardQsModulePropsParametersGatewayVersion(**gateway_version)
        if isinstance(key_name, dict):
            key_name = CfnCloudGuardQsModulePropsParametersKeyName(**key_name)
        if isinstance(load_balancers_type, dict):
            load_balancers_type = CfnCloudGuardQsModulePropsParametersLoadBalancersType(**load_balancers_type)
        if isinstance(management_deploy, dict):
            management_deploy = CfnCloudGuardQsModulePropsParametersManagementDeploy(**management_deploy)
        if isinstance(management_hostname, dict):
            management_hostname = CfnCloudGuardQsModulePropsParametersManagementHostname(**management_hostname)
        if isinstance(management_instance_type, dict):
            management_instance_type = CfnCloudGuardQsModulePropsParametersManagementInstanceType(**management_instance_type)
        if isinstance(management_password_hash, dict):
            management_password_hash = CfnCloudGuardQsModulePropsParametersManagementPasswordHash(**management_password_hash)
        if isinstance(management_permissions, dict):
            management_permissions = CfnCloudGuardQsModulePropsParametersManagementPermissions(**management_permissions)
        if isinstance(management_predefined_role, dict):
            management_predefined_role = CfnCloudGuardQsModulePropsParametersManagementPredefinedRole(**management_predefined_role)
        if isinstance(management_sic_key, dict):
            management_sic_key = CfnCloudGuardQsModulePropsParametersManagementSicKey(**management_sic_key)
        if isinstance(management_stack_volume_size, dict):
            management_stack_volume_size = CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize(**management_stack_volume_size)
        if isinstance(management_version, dict):
            management_version = CfnCloudGuardQsModulePropsParametersManagementVersion(**management_version)
        if isinstance(nlb_protocol, dict):
            nlb_protocol = CfnCloudGuardQsModulePropsParametersNlbProtocol(**nlb_protocol)
        if isinstance(ntp_primary, dict):
            ntp_primary = CfnCloudGuardQsModulePropsParametersNtpPrimary(**ntp_primary)
        if isinstance(ntp_secondary, dict):
            ntp_secondary = CfnCloudGuardQsModulePropsParametersNtpSecondary(**ntp_secondary)
        if isinstance(number_of_a_zs, dict):
            number_of_a_zs = CfnCloudGuardQsModulePropsParametersNumberOfAZs(**number_of_a_zs)
        if isinstance(permissions, dict):
            permissions = CfnCloudGuardQsModulePropsParametersPermissions(**permissions)
        if isinstance(primary_management, dict):
            primary_management = CfnCloudGuardQsModulePropsParametersPrimaryManagement(**primary_management)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(private_subnet3_cidr, dict):
            private_subnet3_cidr = CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr(**private_subnet3_cidr)
        if isinstance(private_subnet4_cidr, dict):
            private_subnet4_cidr = CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr(**private_subnet4_cidr)
        if isinstance(provision_tag, dict):
            provision_tag = CfnCloudGuardQsModulePropsParametersProvisionTag(**provision_tag)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet3_cidr, dict):
            public_subnet3_cidr = CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr(**public_subnet3_cidr)
        if isinstance(public_subnet4_cidr, dict):
            public_subnet4_cidr = CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr(**public_subnet4_cidr)
        if isinstance(security_gateway_volume_size, dict):
            security_gateway_volume_size = CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize(**security_gateway_volume_size)
        if isinstance(server_ami, dict):
            server_ami = CfnCloudGuardQsModulePropsParametersServerAmi(**server_ami)
        if isinstance(server_instance_type, dict):
            server_instance_type = CfnCloudGuardQsModulePropsParametersServerInstanceType(**server_instance_type)
        if isinstance(server_name, dict):
            server_name = CfnCloudGuardQsModulePropsParametersServerName(**server_name)
        if isinstance(servers_deploy, dict):
            servers_deploy = CfnCloudGuardQsModulePropsParametersServersDeploy(**servers_deploy)
        if isinstance(servers_max_size, dict):
            servers_max_size = CfnCloudGuardQsModulePropsParametersServersMaxSize(**servers_max_size)
        if isinstance(servers_min_size, dict):
            servers_min_size = CfnCloudGuardQsModulePropsParametersServersMinSize(**servers_min_size)
        if isinstance(servers_target_groups, dict):
            servers_target_groups = CfnCloudGuardQsModulePropsParametersServersTargetGroups(**servers_target_groups)
        if isinstance(service_port, dict):
            service_port = CfnCloudGuardQsModulePropsParametersServicePort(**service_port)
        if isinstance(shell_management_stack, dict):
            shell_management_stack = CfnCloudGuardQsModulePropsParametersShellManagementStack(**shell_management_stack)
        if isinstance(shell_security_gateway_stack, dict):
            shell_security_gateway_stack = CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack(**shell_security_gateway_stack)
        if isinstance(source_security_group, dict):
            source_security_group = CfnCloudGuardQsModulePropsParametersSourceSecurityGroup(**source_security_group)
        if isinstance(sts_roles, dict):
            sts_roles = CfnCloudGuardQsModulePropsParametersStsRoles(**sts_roles)
        if isinstance(tgw_subnet1_cidr, dict):
            tgw_subnet1_cidr = CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr(**tgw_subnet1_cidr)
        if isinstance(tgw_subnet2_cidr, dict):
            tgw_subnet2_cidr = CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr(**tgw_subnet2_cidr)
        if isinstance(tgw_subnet3_cidr, dict):
            tgw_subnet3_cidr = CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr(**tgw_subnet3_cidr)
        if isinstance(tgw_subnet4_cidr, dict):
            tgw_subnet4_cidr = CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr(**tgw_subnet4_cidr)
        if isinstance(trusted_account, dict):
            trusted_account = CfnCloudGuardQsModulePropsParametersTrustedAccount(**trusted_account)
        if isinstance(vpccidr, dict):
            vpccidr = CfnCloudGuardQsModulePropsParametersVpccidr(**vpccidr)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4328a53d809df0331a47e7d45f875ff1f877db04d78578ff28b70dddf67c9c4a)
            check_type(argname="argument admin_cidr", value=admin_cidr, expected_type=type_hints["admin_cidr"])
            check_type(argname="argument admin_email", value=admin_email, expected_type=type_hints["admin_email"])
            check_type(argname="argument alb_protocol", value=alb_protocol, expected_type=type_hints["alb_protocol"])
            check_type(argname="argument allocate_public_address", value=allocate_public_address, expected_type=type_hints["allocate_public_address"])
            check_type(argname="argument allow_upload_download", value=allow_upload_download, expected_type=type_hints["allow_upload_download"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument cloud_watch", value=cloud_watch, expected_type=type_hints["cloud_watch"])
            check_type(argname="argument control_gateway_over_private_or_public_address", value=control_gateway_over_private_or_public_address, expected_type=type_hints["control_gateway_over_private_or_public_address"])
            check_type(argname="argument create_private_subnets", value=create_private_subnets, expected_type=type_hints["create_private_subnets"])
            check_type(argname="argument create_tgw_subnets", value=create_tgw_subnets, expected_type=type_hints["create_tgw_subnets"])
            check_type(argname="argument elb_clients", value=elb_clients, expected_type=type_hints["elb_clients"])
            check_type(argname="argument elb_port", value=elb_port, expected_type=type_hints["elb_port"])
            check_type(argname="argument elb_type", value=elb_type, expected_type=type_hints["elb_type"])
            check_type(argname="argument enable_instance_connect", value=enable_instance_connect, expected_type=type_hints["enable_instance_connect"])
            check_type(argname="argument enable_volume_encryption", value=enable_volume_encryption, expected_type=type_hints["enable_volume_encryption"])
            check_type(argname="argument gateway_instance_type", value=gateway_instance_type, expected_type=type_hints["gateway_instance_type"])
            check_type(argname="argument gateway_management", value=gateway_management, expected_type=type_hints["gateway_management"])
            check_type(argname="argument gateway_password_hash", value=gateway_password_hash, expected_type=type_hints["gateway_password_hash"])
            check_type(argname="argument gateways_addresses", value=gateways_addresses, expected_type=type_hints["gateways_addresses"])
            check_type(argname="argument gateways_blades", value=gateways_blades, expected_type=type_hints["gateways_blades"])
            check_type(argname="argument gateway_sic_key", value=gateway_sic_key, expected_type=type_hints["gateway_sic_key"])
            check_type(argname="argument gateways_max_size", value=gateways_max_size, expected_type=type_hints["gateways_max_size"])
            check_type(argname="argument gateways_min_size", value=gateways_min_size, expected_type=type_hints["gateways_min_size"])
            check_type(argname="argument gateways_policy", value=gateways_policy, expected_type=type_hints["gateways_policy"])
            check_type(argname="argument gateways_target_groups", value=gateways_target_groups, expected_type=type_hints["gateways_target_groups"])
            check_type(argname="argument gateway_version", value=gateway_version, expected_type=type_hints["gateway_version"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument load_balancers_type", value=load_balancers_type, expected_type=type_hints["load_balancers_type"])
            check_type(argname="argument management_deploy", value=management_deploy, expected_type=type_hints["management_deploy"])
            check_type(argname="argument management_hostname", value=management_hostname, expected_type=type_hints["management_hostname"])
            check_type(argname="argument management_instance_type", value=management_instance_type, expected_type=type_hints["management_instance_type"])
            check_type(argname="argument management_password_hash", value=management_password_hash, expected_type=type_hints["management_password_hash"])
            check_type(argname="argument management_permissions", value=management_permissions, expected_type=type_hints["management_permissions"])
            check_type(argname="argument management_predefined_role", value=management_predefined_role, expected_type=type_hints["management_predefined_role"])
            check_type(argname="argument management_sic_key", value=management_sic_key, expected_type=type_hints["management_sic_key"])
            check_type(argname="argument management_stack_volume_size", value=management_stack_volume_size, expected_type=type_hints["management_stack_volume_size"])
            check_type(argname="argument management_version", value=management_version, expected_type=type_hints["management_version"])
            check_type(argname="argument nlb_protocol", value=nlb_protocol, expected_type=type_hints["nlb_protocol"])
            check_type(argname="argument ntp_primary", value=ntp_primary, expected_type=type_hints["ntp_primary"])
            check_type(argname="argument ntp_secondary", value=ntp_secondary, expected_type=type_hints["ntp_secondary"])
            check_type(argname="argument number_of_a_zs", value=number_of_a_zs, expected_type=type_hints["number_of_a_zs"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument primary_management", value=primary_management, expected_type=type_hints["primary_management"])
            check_type(argname="argument private_subnet1_cidr", value=private_subnet1_cidr, expected_type=type_hints["private_subnet1_cidr"])
            check_type(argname="argument private_subnet2_cidr", value=private_subnet2_cidr, expected_type=type_hints["private_subnet2_cidr"])
            check_type(argname="argument private_subnet3_cidr", value=private_subnet3_cidr, expected_type=type_hints["private_subnet3_cidr"])
            check_type(argname="argument private_subnet4_cidr", value=private_subnet4_cidr, expected_type=type_hints["private_subnet4_cidr"])
            check_type(argname="argument provision_tag", value=provision_tag, expected_type=type_hints["provision_tag"])
            check_type(argname="argument public_subnet1_cidr", value=public_subnet1_cidr, expected_type=type_hints["public_subnet1_cidr"])
            check_type(argname="argument public_subnet2_cidr", value=public_subnet2_cidr, expected_type=type_hints["public_subnet2_cidr"])
            check_type(argname="argument public_subnet3_cidr", value=public_subnet3_cidr, expected_type=type_hints["public_subnet3_cidr"])
            check_type(argname="argument public_subnet4_cidr", value=public_subnet4_cidr, expected_type=type_hints["public_subnet4_cidr"])
            check_type(argname="argument security_gateway_volume_size", value=security_gateway_volume_size, expected_type=type_hints["security_gateway_volume_size"])
            check_type(argname="argument server_ami", value=server_ami, expected_type=type_hints["server_ami"])
            check_type(argname="argument server_instance_type", value=server_instance_type, expected_type=type_hints["server_instance_type"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument servers_deploy", value=servers_deploy, expected_type=type_hints["servers_deploy"])
            check_type(argname="argument servers_max_size", value=servers_max_size, expected_type=type_hints["servers_max_size"])
            check_type(argname="argument servers_min_size", value=servers_min_size, expected_type=type_hints["servers_min_size"])
            check_type(argname="argument servers_target_groups", value=servers_target_groups, expected_type=type_hints["servers_target_groups"])
            check_type(argname="argument service_port", value=service_port, expected_type=type_hints["service_port"])
            check_type(argname="argument shell_management_stack", value=shell_management_stack, expected_type=type_hints["shell_management_stack"])
            check_type(argname="argument shell_security_gateway_stack", value=shell_security_gateway_stack, expected_type=type_hints["shell_security_gateway_stack"])
            check_type(argname="argument source_security_group", value=source_security_group, expected_type=type_hints["source_security_group"])
            check_type(argname="argument sts_roles", value=sts_roles, expected_type=type_hints["sts_roles"])
            check_type(argname="argument tgw_subnet1_cidr", value=tgw_subnet1_cidr, expected_type=type_hints["tgw_subnet1_cidr"])
            check_type(argname="argument tgw_subnet2_cidr", value=tgw_subnet2_cidr, expected_type=type_hints["tgw_subnet2_cidr"])
            check_type(argname="argument tgw_subnet3_cidr", value=tgw_subnet3_cidr, expected_type=type_hints["tgw_subnet3_cidr"])
            check_type(argname="argument tgw_subnet4_cidr", value=tgw_subnet4_cidr, expected_type=type_hints["tgw_subnet4_cidr"])
            check_type(argname="argument trusted_account", value=trusted_account, expected_type=type_hints["trusted_account"])
            check_type(argname="argument vpccidr", value=vpccidr, expected_type=type_hints["vpccidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if admin_cidr is not None:
            self._values["admin_cidr"] = admin_cidr
        if admin_email is not None:
            self._values["admin_email"] = admin_email
        if alb_protocol is not None:
            self._values["alb_protocol"] = alb_protocol
        if allocate_public_address is not None:
            self._values["allocate_public_address"] = allocate_public_address
        if allow_upload_download is not None:
            self._values["allow_upload_download"] = allow_upload_download
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if certificate is not None:
            self._values["certificate"] = certificate
        if cloud_watch is not None:
            self._values["cloud_watch"] = cloud_watch
        if control_gateway_over_private_or_public_address is not None:
            self._values["control_gateway_over_private_or_public_address"] = control_gateway_over_private_or_public_address
        if create_private_subnets is not None:
            self._values["create_private_subnets"] = create_private_subnets
        if create_tgw_subnets is not None:
            self._values["create_tgw_subnets"] = create_tgw_subnets
        if elb_clients is not None:
            self._values["elb_clients"] = elb_clients
        if elb_port is not None:
            self._values["elb_port"] = elb_port
        if elb_type is not None:
            self._values["elb_type"] = elb_type
        if enable_instance_connect is not None:
            self._values["enable_instance_connect"] = enable_instance_connect
        if enable_volume_encryption is not None:
            self._values["enable_volume_encryption"] = enable_volume_encryption
        if gateway_instance_type is not None:
            self._values["gateway_instance_type"] = gateway_instance_type
        if gateway_management is not None:
            self._values["gateway_management"] = gateway_management
        if gateway_password_hash is not None:
            self._values["gateway_password_hash"] = gateway_password_hash
        if gateways_addresses is not None:
            self._values["gateways_addresses"] = gateways_addresses
        if gateways_blades is not None:
            self._values["gateways_blades"] = gateways_blades
        if gateway_sic_key is not None:
            self._values["gateway_sic_key"] = gateway_sic_key
        if gateways_max_size is not None:
            self._values["gateways_max_size"] = gateways_max_size
        if gateways_min_size is not None:
            self._values["gateways_min_size"] = gateways_min_size
        if gateways_policy is not None:
            self._values["gateways_policy"] = gateways_policy
        if gateways_target_groups is not None:
            self._values["gateways_target_groups"] = gateways_target_groups
        if gateway_version is not None:
            self._values["gateway_version"] = gateway_version
        if key_name is not None:
            self._values["key_name"] = key_name
        if load_balancers_type is not None:
            self._values["load_balancers_type"] = load_balancers_type
        if management_deploy is not None:
            self._values["management_deploy"] = management_deploy
        if management_hostname is not None:
            self._values["management_hostname"] = management_hostname
        if management_instance_type is not None:
            self._values["management_instance_type"] = management_instance_type
        if management_password_hash is not None:
            self._values["management_password_hash"] = management_password_hash
        if management_permissions is not None:
            self._values["management_permissions"] = management_permissions
        if management_predefined_role is not None:
            self._values["management_predefined_role"] = management_predefined_role
        if management_sic_key is not None:
            self._values["management_sic_key"] = management_sic_key
        if management_stack_volume_size is not None:
            self._values["management_stack_volume_size"] = management_stack_volume_size
        if management_version is not None:
            self._values["management_version"] = management_version
        if nlb_protocol is not None:
            self._values["nlb_protocol"] = nlb_protocol
        if ntp_primary is not None:
            self._values["ntp_primary"] = ntp_primary
        if ntp_secondary is not None:
            self._values["ntp_secondary"] = ntp_secondary
        if number_of_a_zs is not None:
            self._values["number_of_a_zs"] = number_of_a_zs
        if permissions is not None:
            self._values["permissions"] = permissions
        if primary_management is not None:
            self._values["primary_management"] = primary_management
        if private_subnet1_cidr is not None:
            self._values["private_subnet1_cidr"] = private_subnet1_cidr
        if private_subnet2_cidr is not None:
            self._values["private_subnet2_cidr"] = private_subnet2_cidr
        if private_subnet3_cidr is not None:
            self._values["private_subnet3_cidr"] = private_subnet3_cidr
        if private_subnet4_cidr is not None:
            self._values["private_subnet4_cidr"] = private_subnet4_cidr
        if provision_tag is not None:
            self._values["provision_tag"] = provision_tag
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if public_subnet3_cidr is not None:
            self._values["public_subnet3_cidr"] = public_subnet3_cidr
        if public_subnet4_cidr is not None:
            self._values["public_subnet4_cidr"] = public_subnet4_cidr
        if security_gateway_volume_size is not None:
            self._values["security_gateway_volume_size"] = security_gateway_volume_size
        if server_ami is not None:
            self._values["server_ami"] = server_ami
        if server_instance_type is not None:
            self._values["server_instance_type"] = server_instance_type
        if server_name is not None:
            self._values["server_name"] = server_name
        if servers_deploy is not None:
            self._values["servers_deploy"] = servers_deploy
        if servers_max_size is not None:
            self._values["servers_max_size"] = servers_max_size
        if servers_min_size is not None:
            self._values["servers_min_size"] = servers_min_size
        if servers_target_groups is not None:
            self._values["servers_target_groups"] = servers_target_groups
        if service_port is not None:
            self._values["service_port"] = service_port
        if shell_management_stack is not None:
            self._values["shell_management_stack"] = shell_management_stack
        if shell_security_gateway_stack is not None:
            self._values["shell_security_gateway_stack"] = shell_security_gateway_stack
        if source_security_group is not None:
            self._values["source_security_group"] = source_security_group
        if sts_roles is not None:
            self._values["sts_roles"] = sts_roles
        if tgw_subnet1_cidr is not None:
            self._values["tgw_subnet1_cidr"] = tgw_subnet1_cidr
        if tgw_subnet2_cidr is not None:
            self._values["tgw_subnet2_cidr"] = tgw_subnet2_cidr
        if tgw_subnet3_cidr is not None:
            self._values["tgw_subnet3_cidr"] = tgw_subnet3_cidr
        if tgw_subnet4_cidr is not None:
            self._values["tgw_subnet4_cidr"] = tgw_subnet4_cidr
        if trusted_account is not None:
            self._values["trusted_account"] = trusted_account
        if vpccidr is not None:
            self._values["vpccidr"] = vpccidr

    @builtins.property
    def admin_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersAdminCidr"]:
        '''Allow web, SSH, and graphical clients only from this network to communicate with the Security Management Server.

        :schema: CfnCloudGuardQsModulePropsParameters#AdminCIDR
        '''
        result = self._values.get("admin_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersAdminCidr"], result)

    @builtins.property
    def admin_email(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersAdminEmail"]:
        '''Notifications about scaling events will be sent to this email address (optional).

        :schema: CfnCloudGuardQsModulePropsParameters#AdminEmail
        '''
        result = self._values.get("admin_email")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersAdminEmail"], result)

    @builtins.property
    def alb_protocol(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersAlbProtocol"]:
        '''The protocol to use on the Application Load Balancer.

        If Network Load Balancer was selected this section will be ignored. Default: HTTP. Allowed values: HTTP, HTTPS

        :schema: CfnCloudGuardQsModulePropsParameters#ALBProtocol
        '''
        result = self._values.get("alb_protocol")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersAlbProtocol"], result)

    @builtins.property
    def allocate_public_address(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersAllocatePublicAddress"]:
        '''Allocate an elastic IP for the Management.

        Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#AllocatePublicAddress
        '''
        result = self._values.get("allocate_public_address")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersAllocatePublicAddress"], result)

    @builtins.property
    def allow_upload_download(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersAllowUploadDownload"]:
        '''Automatically download Blade Contracts and other important data.

        Improve product experience by sending data to Check Point. Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#AllowUploadDownload
        '''
        result = self._values.get("allow_upload_download")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersAllowUploadDownload"], result)

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersAvailabilityZones"]:
        '''List of Availability Zones (AZs) to use for the subnets in the VPC.

        Select at least two

        :schema: CfnCloudGuardQsModulePropsParameters#AvailabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersAvailabilityZones"], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersCertificate"]:
        '''Amazon Resource Name (ARN) of an HTTPS Certificate, ignored if the selected protocol is HTTP (for the ALBProtocol parameter).

        :schema: CfnCloudGuardQsModulePropsParameters#Certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersCertificate"], result)

    @builtins.property
    def cloud_watch(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersCloudWatch"]:
        '''Report Check Point specific CloudWatch metrics.

        Default: false

        :schema: CfnCloudGuardQsModulePropsParameters#CloudWatch
        '''
        result = self._values.get("cloud_watch")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersCloudWatch"], result)

    @builtins.property
    def control_gateway_over_private_or_public_address(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress"]:
        '''Determines if the gateways are provisioned using their private or public address.

        Default: private. Allowed values: private, public

        :schema: CfnCloudGuardQsModulePropsParameters#ControlGatewayOverPrivateOrPublicAddress
        '''
        result = self._values.get("control_gateway_over_private_or_public_address")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress"], result)

    @builtins.property
    def create_private_subnets(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets"]:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored. Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#CreatePrivateSubnets
        '''
        result = self._values.get("create_private_subnets")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets"], result)

    @builtins.property
    def create_tgw_subnets(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersCreateTgwSubnets"]:
        '''Set true for creating designated subnets for VPC TGW attachments.

        If false, the CIDR parameters for the TGW subnets will be ignored. Default: false

        :schema: CfnCloudGuardQsModulePropsParameters#CreateTgwSubnets
        '''
        result = self._values.get("create_tgw_subnets")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersCreateTgwSubnets"], result)

    @builtins.property
    def elb_clients(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersElbClients"]:
        '''Allow clients only from this network to communicate with the Web Servers.

        Default: 0.0.0.0/0

        :schema: CfnCloudGuardQsModulePropsParameters#ELBClients
        '''
        result = self._values.get("elb_clients")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersElbClients"], result)

    @builtins.property
    def elb_port(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersElbPort"]:
        '''Port for the ELB.

        Default: 8080

        :schema: CfnCloudGuardQsModulePropsParameters#ELBPort
        '''
        result = self._values.get("elb_port")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersElbPort"], result)

    @builtins.property
    def elb_type(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersElbType"]:
        '''The Elasitc Load Balancer Type.

        Default: none. Allowed values: none, internal, internet-facing

        :schema: CfnCloudGuardQsModulePropsParameters#ELBType
        '''
        result = self._values.get("elb_type")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersElbType"], result)

    @builtins.property
    def enable_instance_connect(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersEnableInstanceConnect"]:
        '''Enable SSH connection over AWS web console.

        Default: false

        :schema: CfnCloudGuardQsModulePropsParameters#EnableInstanceConnect
        '''
        result = self._values.get("enable_instance_connect")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersEnableInstanceConnect"], result)

    @builtins.property
    def enable_volume_encryption(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption"]:
        '''Encrypt Environment instances volume with default AWS KMS key.

        Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#EnableVolumeEncryption
        '''
        result = self._values.get("enable_volume_encryption")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption"], result)

    @builtins.property
    def gateway_instance_type(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayInstanceType"]:
        '''The EC2 instance type for the Security Gateways.

        Default: c5.xlarge. Allowed values: c5.xlarge, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.18xlarge, c5n.large, c5n.xlarge, c5n.2xlarge, c5n.4xlarge, c5n.9xlarge, c5n.18xlarge

        :schema: CfnCloudGuardQsModulePropsParameters#GatewayInstanceType
        '''
        result = self._values.get("gateway_instance_type")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayInstanceType"], result)

    @builtins.property
    def gateway_management(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayManagement"]:
        '''Select 'Over the internet' if any of the gateways you wish to manage are not directly accessed via their private IP address.

        Default: 'Locally managed'. Allowed values: Locally managed, Over the internet

        :schema: CfnCloudGuardQsModulePropsParameters#GatewayManagement
        '''
        result = self._values.get("gateway_management")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayManagement"], result)

    @builtins.property
    def gateway_password_hash(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayPasswordHash"]:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :schema: CfnCloudGuardQsModulePropsParameters#GatewayPasswordHash
        '''
        result = self._values.get("gateway_password_hash")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayPasswordHash"], result)

    @builtins.property
    def gateways_addresses(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysAddresses"]:
        '''Allow gateways only from this network to communicate with the Security Management Server.

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaysAddresses
        '''
        result = self._values.get("gateways_addresses")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysAddresses"], result)

    @builtins.property
    def gateways_blades(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysBlades"]:
        '''Turn on the Intrusion Prevention System, Application Control, Anti-Virus and Anti-Bot Blades (these and additional Blades can be manually turned on or off later).

        Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaysBlades
        '''
        result = self._values.get("gateways_blades")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysBlades"], result)

    @builtins.property
    def gateway_sic_key(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaySicKey"]:
        '''The Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters.

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaySICKey
        '''
        result = self._values.get("gateway_sic_key")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaySicKey"], result)

    @builtins.property
    def gateways_max_size(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysMaxSize"]:
        '''The maximal number of Security Gateways.

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaysMaxSize
        '''
        result = self._values.get("gateways_max_size")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysMaxSize"], result)

    @builtins.property
    def gateways_min_size(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysMinSize"]:
        '''The minimal number of Security Gateways.

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaysMinSize
        '''
        result = self._values.get("gateways_min_size")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysMinSize"], result)

    @builtins.property
    def gateways_policy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysPolicy"]:
        '''The name of the Security Policy package to be installed on the gateways in the Security Gateways Auto Scaling group.

        Default: Standard

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaysPolicy
        '''
        result = self._values.get("gateways_policy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysPolicy"], result)

    @builtins.property
    def gateways_target_groups(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups"]:
        '''A list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces) (optional).

        :schema: CfnCloudGuardQsModulePropsParameters#GatewaysTargetGroups
        '''
        result = self._values.get("gateways_target_groups")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups"], result)

    @builtins.property
    def gateway_version(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayVersion"]:
        '''The version and license to install on the Security Gateways.

        Default: R80.40-PAYG-NGTP-GW. Allowed values: R80.40-BYOL-GW, R80.40-PAYG-NGTP-GW, R80.40-PAYG-NGTX-GW, R81-BYOL-GW, R81-PAYG-NGTP-GW, R81-PAYG-NGTX-GW

        :schema: CfnCloudGuardQsModulePropsParameters#GatewayVersion
        '''
        result = self._values.get("gateway_version")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersGatewayVersion"], result)

    @builtins.property
    def key_name(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersKeyName"]:
        '''The EC2 Key Pair to allow SSH access to the instances.

        For more detail visit: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

        :schema: CfnCloudGuardQsModulePropsParameters#KeyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersKeyName"], result)

    @builtins.property
    def load_balancers_type(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersLoadBalancersType"]:
        '''Use Network Load Balancer if you wish to preserve the source IP address and Application Load Balancer if you wish to perform SSL Offloading.

        Default: Network Load Balancer. Allowed values: Network Load Balancer, Application Load Balancer

        :schema: CfnCloudGuardQsModulePropsParameters#LoadBalancersType
        '''
        result = self._values.get("load_balancers_type")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersLoadBalancersType"], result)

    @builtins.property
    def management_deploy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementDeploy"]:
        '''Select false to use an existing Security Management Server or to deploy one later and to ignore the other parameters of this section.

        Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementDeploy
        '''
        result = self._values.get("management_deploy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementDeploy"], result)

    @builtins.property
    def management_hostname(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementHostname"]:
        '''(optional).

        Default: mgmt-aws

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementHostname
        '''
        result = self._values.get("management_hostname")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementHostname"], result)

    @builtins.property
    def management_instance_type(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementInstanceType"]:
        '''The EC2 instance type of the Security Management Server.

        Default: m5.xlarge. Allowed values: m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.12xlarge, m5.24xlarge

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementInstanceType
        '''
        result = self._values.get("management_instance_type")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementInstanceType"], result)

    @builtins.property
    def management_password_hash(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementPasswordHash"]:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementPasswordHash
        '''
        result = self._values.get("management_password_hash")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementPasswordHash"], result)

    @builtins.property
    def management_permissions(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementPermissions"]:
        '''IAM role to attach to the instance profile of the Management Server.

        Default: Create with read permissions. Allowed values: None (configure later), Use existing (specify an existing IAM role name), Create with assume role permissions (specify an STS role ARN), Create with read permissions, Create with read-write permissions

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementPermissions
        '''
        result = self._values.get("management_permissions")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementPermissions"], result)

    @builtins.property
    def management_predefined_role(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementPredefinedRole"]:
        '''A predefined IAM role to attach to the instance profile.

        Ignored if IAM role is not set to 'Use existing'

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementPredefinedRole
        '''
        result = self._values.get("management_predefined_role")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementPredefinedRole"], result)

    @builtins.property
    def management_sic_key(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementSicKey"]:
        '''Mandatory only if deploying a secondary Management Server, the Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementSICKey
        '''
        result = self._values.get("management_sic_key")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementSicKey"], result)

    @builtins.property
    def management_stack_volume_size(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize"]:
        '''EBS Volume size of the management server.

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementStackVolumeSize
        '''
        result = self._values.get("management_stack_volume_size")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize"], result)

    @builtins.property
    def management_version(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersManagementVersion"]:
        '''The version and license to install on the Security Management Server.

        Default: R80.40-PAYG-MGMT. Allowed values: R80.40-BYOL-MGMT, R80.40-PAYG-MGMT, R81-BYOL-MGMT, R81-PAYG-MGMT

        :schema: CfnCloudGuardQsModulePropsParameters#ManagementVersion
        '''
        result = self._values.get("management_version")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersManagementVersion"], result)

    @builtins.property
    def nlb_protocol(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersNlbProtocol"]:
        '''The protocol to use on the Network Load Balancer.

        If Application Load Balancer was selected this section will be ignored. Default: TCP. Allowed values: TCP, TLS, UDP, TCP_UDP

        :schema: CfnCloudGuardQsModulePropsParameters#NLBProtocol
        '''
        result = self._values.get("nlb_protocol")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersNlbProtocol"], result)

    @builtins.property
    def ntp_primary(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersNtpPrimary"]:
        '''(optional).

        Default: 169.254.169.123

        :schema: CfnCloudGuardQsModulePropsParameters#NTPPrimary
        '''
        result = self._values.get("ntp_primary")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersNtpPrimary"], result)

    @builtins.property
    def ntp_secondary(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersNtpSecondary"]:
        '''(optional).

        Default: 0.pool.ntp.org

        :schema: CfnCloudGuardQsModulePropsParameters#NTPSecondary
        '''
        result = self._values.get("ntp_secondary")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersNtpSecondary"], result)

    @builtins.property
    def number_of_a_zs(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersNumberOfAZs"]:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.  Default: 2

        :schema: CfnCloudGuardQsModulePropsParameters#NumberOfAZs
        '''
        result = self._values.get("number_of_a_zs")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersNumberOfAZs"], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPermissions"]:
        '''IAM Permissions for the management server.

        Default: Create with read permissions. Allowed values: Create with read permissions Create with read-write permissions Create with assume role permissions (specify an STS role ARN)

        :schema: CfnCloudGuardQsModulePropsParameters#Permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPermissions"], result)

    @builtins.property
    def primary_management(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPrimaryManagement"]:
        '''Determines if this is the primary Management Server or not.

        Default: true

        :schema: CfnCloudGuardQsModulePropsParameters#PrimaryManagement
        '''
        result = self._values.get("primary_management")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPrimaryManagement"], result)

    @builtins.property
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr"]:
        '''CIDR block for private subnet 1 located in the 1st Availability Zone.

        Default: 10.0.11.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PrivateSubnet1CIDR
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr"], result)

    @builtins.property
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr"]:
        '''CIDR block for private subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.21.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PrivateSubnet2CIDR
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def private_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr"]:
        '''CIDR block for private subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.31.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PrivateSubnet3CIDR
        '''
        result = self._values.get("private_subnet3_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr"], result)

    @builtins.property
    def private_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr"]:
        '''CIDR block for private subnet 4 located in the 4th Availability Zone.

        Default: 10.0.41.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PrivateSubnet4CIDR
        '''
        result = self._values.get("private_subnet4_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr"], result)

    @builtins.property
    def provision_tag(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersProvisionTag"]:
        '''The tag is used by the Security Management Server to automatically provision the Security Gateways.

        Must be up to 12 alphanumeric characters and unique for each Quick Start deployment. Default: quickstart

        :schema: CfnCloudGuardQsModulePropsParameters#ProvisionTag
        '''
        result = self._values.get("provision_tag")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersProvisionTag"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for public subnet 1 located in the 1st Availability Zone.

        If you choose to deploy a Security Management Server it will be deployed in this subnet. Default: 10.0.10.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for public subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.20.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr"]:
        '''CIDR block for public subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.30.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PublicSubnet3CIDR
        '''
        result = self._values.get("public_subnet3_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr"], result)

    @builtins.property
    def public_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr"]:
        '''CIDR block for public subnet 4 located in the 4th Availability Zone.

        Default: 10.0.40.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#PublicSubnet4CIDR
        '''
        result = self._values.get("public_subnet4_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr"], result)

    @builtins.property
    def security_gateway_volume_size(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize"]:
        '''EBS Volume size of the security gateway server.

        :schema: CfnCloudGuardQsModulePropsParameters#SecurityGatewayVolumeSize
        '''
        result = self._values.get("security_gateway_volume_size")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize"], result)

    @builtins.property
    def server_ami(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServerAmi"]:
        '''The Amazon Machine Image ID of a preconfigured web server (e.g. ami-0dc7dc63).

        :schema: CfnCloudGuardQsModulePropsParameters#ServerAMI
        '''
        result = self._values.get("server_ami")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServerAmi"], result)

    @builtins.property
    def server_instance_type(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServerInstanceType"]:
        '''The EC2 instance type for the web servers.

        Default: t3.micro. Allowed values: t3.nano, t3.micro, t3.small, t3.medium, t3.large, t3.xlarge, t3.2xlarge

        :schema: CfnCloudGuardQsModulePropsParameters#ServerInstanceType
        '''
        result = self._values.get("server_instance_type")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServerInstanceType"], result)

    @builtins.property
    def server_name(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServerName"]:
        '''The servers name tag.

        Default: Server

        :schema: CfnCloudGuardQsModulePropsParameters#ServerName
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServerName"], result)

    @builtins.property
    def servers_deploy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServersDeploy"]:
        '''Select true to deploy web servers and an internal Application Load Balancer.

        If you select false the other parameters of this section will be ignored. Default: false

        :schema: CfnCloudGuardQsModulePropsParameters#ServersDeploy
        '''
        result = self._values.get("servers_deploy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServersDeploy"], result)

    @builtins.property
    def servers_max_size(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServersMaxSize"]:
        '''The maximal number of servers in the Auto Scaling group.

        Default: 10

        :schema: CfnCloudGuardQsModulePropsParameters#ServersMaxSize
        '''
        result = self._values.get("servers_max_size")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServersMaxSize"], result)

    @builtins.property
    def servers_min_size(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServersMinSize"]:
        '''The minimal number of servers in the Auto Scaling group.

        Default: 2

        :schema: CfnCloudGuardQsModulePropsParameters#ServersMinSize
        '''
        result = self._values.get("servers_min_size")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServersMinSize"], result)

    @builtins.property
    def servers_target_groups(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServersTargetGroups"]:
        '''An optional list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces).

        :schema: CfnCloudGuardQsModulePropsParameters#ServersTargetGroups
        '''
        result = self._values.get("servers_target_groups")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServersTargetGroups"], result)

    @builtins.property
    def service_port(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersServicePort"]:
        '''The external Load Balancer listens to this port.

        Leave this field blank to use default ports: 80 for HTTP and 443 for HTTPS

        :schema: CfnCloudGuardQsModulePropsParameters#ServicePort
        '''
        result = self._values.get("service_port")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersServicePort"], result)

    @builtins.property
    def shell_management_stack(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersShellManagementStack"]:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed values: /etc/cli.sh, /bin/bash, /bin/csh, /bin/tcsh

        :schema: CfnCloudGuardQsModulePropsParameters#ShellManagementStack
        '''
        result = self._values.get("shell_management_stack")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersShellManagementStack"], result)

    @builtins.property
    def shell_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack"]:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed Values: /etc/cli.sh /bin/bash /bin/csh /bin/tcsh

        :schema: CfnCloudGuardQsModulePropsParameters#ShellSecurityGatewayStack
        '''
        result = self._values.get("shell_security_gateway_stack")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack"], result)

    @builtins.property
    def source_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersSourceSecurityGroup"]:
        '''The ID of Security Group from which access will be allowed to the instances in this Auto Scaling group.

        :schema: CfnCloudGuardQsModulePropsParameters#SourceSecurityGroup
        '''
        result = self._values.get("source_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersSourceSecurityGroup"], result)

    @builtins.property
    def sts_roles(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersStsRoles"]:
        '''The IAM role will be able to assume these STS Roles (comma separated list of ARNs, without spaces).

        :schema: CfnCloudGuardQsModulePropsParameters#STSRoles
        '''
        result = self._values.get("sts_roles")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersStsRoles"], result)

    @builtins.property
    def tgw_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr"]:
        '''CIDR block for TGW subnet 1 located in Availability Zone 1.

        Default: 10.0.12.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#TgwSubnet1CIDR
        '''
        result = self._values.get("tgw_subnet1_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr"], result)

    @builtins.property
    def tgw_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr"]:
        '''CIDR block for TGW subnet 2 located in Availability Zone 2.

        Default: 10.0.22.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#TgwSubnet2CIDR
        '''
        result = self._values.get("tgw_subnet2_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr"], result)

    @builtins.property
    def tgw_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr"]:
        '''CIDR block for TGW subnet 3 located in Availability Zone 3.

        Default: 10.0.32.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#TgwSubnet3CIDR
        '''
        result = self._values.get("tgw_subnet3_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr"], result)

    @builtins.property
    def tgw_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr"]:
        '''CIDR block for TGW subnet 4 located in Availability Zone 4.

        Default: 10.0.42.0/24

        :schema: CfnCloudGuardQsModulePropsParameters#TgwSubnet4CIDR
        '''
        result = self._values.get("tgw_subnet4_cidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr"], result)

    @builtins.property
    def trusted_account(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsParametersTrustedAccount"]:
        '''A 12 digits number that represents the ID of a trusted account.

        IAM users in this account will be able assume the IAM role and receive the permissions attached to it.

        :schema: CfnCloudGuardQsModulePropsParameters#TrustedAccount
        '''
        result = self._values.get("trusted_account")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersTrustedAccount"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnCloudGuardQsModulePropsParametersVpccidr"]:
        '''CIDR block for the VPC.

        Default: 10.0.0.0/16

        :schema: CfnCloudGuardQsModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsParametersVpccidr"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersAdminCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersAdminCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allow web, SSH, and graphical clients only from this network to communicate with the Security Management Server.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersAdminCidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb7db9b3fa37e254ff81e31253caee6ba2db66a9b2ca252e8439bd873b165b0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAdminCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAdminCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersAdminCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersAdminEmail",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersAdminEmail:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Notifications about scaling events will be sent to this email address (optional).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersAdminEmail
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9971e1bacc76211dc6fe1d9cb133d90c2fb0a8dab87b8b7301b5d1b456717e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAdminEmail#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAdminEmail#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersAdminEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersAlbProtocol",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersAlbProtocol:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The protocol to use on the Application Load Balancer.

        If Network Load Balancer was selected this section will be ignored. Default: HTTP. Allowed values: HTTP, HTTPS

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersAlbProtocol
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7da7c9f79cf613725f598459cf114b398af73597f454d3fe4c387beb279f34a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAlbProtocol#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAlbProtocol#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersAlbProtocol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersAllocatePublicAddress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersAllocatePublicAddress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allocate an elastic IP for the Management.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersAllocatePublicAddress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca370f55f9b60908c9d43b182eea4e0ed983695bc50066340484e0430517a7b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAllocatePublicAddress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAllocatePublicAddress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersAllocatePublicAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersAllowUploadDownload",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersAllowUploadDownload:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Automatically download Blade Contracts and other important data.

        Improve product experience by sending data to Check Point. Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersAllowUploadDownload
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4fe51216a493fd425344504f49e8eff6d13f17cd8bffb56bcab57c15cb34ad7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAllowUploadDownload#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAllowUploadDownload#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersAllowUploadDownload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersAvailabilityZones:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''List of Availability Zones (AZs) to use for the subnets in the VPC.

        Select at least two

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersAvailabilityZones
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955f9e7b492417d86422274972d39c846b6477bc82317015d4b1ec627c912ae0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAvailabilityZones#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersAvailabilityZones#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersCertificate",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersCertificate:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon Resource Name (ARN) of an HTTPS Certificate, ignored if the selected protocol is HTTP (for the ALBProtocol parameter).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersCertificate
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce36a4886065f86921b904f2570a23d249df67c619f78cfe6ec3ca9efe829a00)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCertificate#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCertificate#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersCloudWatch",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersCloudWatch:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Report Check Point specific CloudWatch metrics.

        Default: false

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersCloudWatch
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b26af9b98285712eee5c438b33b6f6eeb80a741c606e1862f28ffbba4cb5b07a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCloudWatch#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCloudWatch#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersCloudWatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Determines if the gateways are provisioned using their private or public address.

        Default: private. Allowed values: private, public

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ac0e193822bc243f0a78999075165c89dca3cc2982534fc85519e1f22de36e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored. Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33abb2b26622038bcf65ac573a9f33cbb04bc725a156f048bb5ed266cd78a2c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersCreateTgwSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersCreateTgwSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set true for creating designated subnets for VPC TGW attachments.

        If false, the CIDR parameters for the TGW subnets will be ignored. Default: false

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersCreateTgwSubnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16654ffe240541f090f56fa68b9c3d37cb39195a833f5d99735ea0306b4639fb)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCreateTgwSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersCreateTgwSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersCreateTgwSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersElbClients",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersElbClients:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allow clients only from this network to communicate with the Web Servers.

        Default: 0.0.0.0/0

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersElbClients
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5990dd2c27957b9b8de505411b5699185c7a630edb58baf2145392f4ff2729aa)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersElbClients#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersElbClients#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersElbClients(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersElbPort",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersElbPort:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Port for the ELB.

        Default: 8080

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersElbPort
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf2835392ad1c3181ab5a13a4a9746c7488cde8745ca0f8e7eaa78fdf6d278f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersElbPort#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersElbPort#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersElbPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersElbType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersElbType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Elasitc Load Balancer Type.

        Default: none. Allowed values: none, internal, internet-facing

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersElbType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8b3a27c3dbddbc16b321f94f9578a2d86d215ee6ccd8f14ce019523e249801c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersElbType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersElbType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersElbType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersEnableInstanceConnect",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersEnableInstanceConnect:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enable SSH connection over AWS web console.

        Default: false

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersEnableInstanceConnect
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__232e57cc80211385d6a639061ad22153d24ff4ad78d8a929b80df2ad2273ceb3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersEnableInstanceConnect#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersEnableInstanceConnect#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersEnableInstanceConnect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Encrypt Environment instances volume with default AWS KMS key.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d05607e4e68034f0935231a8bb50f36a4faceee9e0b177951e8806261c80cd6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewayInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the Security Gateways.

        Default: c5.xlarge. Allowed values: c5.xlarge, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.18xlarge, c5n.large, c5n.xlarge, c5n.2xlarge, c5n.4xlarge, c5n.9xlarge, c5n.18xlarge

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewayInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7196bc9d7b9d34fc10aebe0728e101b384171c35a3a08e9cb71e8725c886b28)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewayInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewayManagement",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewayManagement:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Select 'Over the internet' if any of the gateways you wish to manage are not directly accessed via their private IP address.

        Default: 'Locally managed'. Allowed values: Locally managed, Over the internet

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewayManagement
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6cca0be6211d5b73dfb3b21d4494db437678cbf12a0f3724203ed8e92be1c9f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayManagement#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayManagement#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewayManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewayPasswordHash",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewayPasswordHash:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewayPasswordHash
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43706457692e4b1e97e6051b3beb05d21bd3add49fb183736f31f57f7d65b648)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayPasswordHash#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayPasswordHash#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewayPasswordHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaySicKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaySicKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaySicKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a15d7058f15881b5d42cdc436d6f182ca71d18ea15952dff80b2205aed5d3f89)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaySicKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaySicKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaySicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewayVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewayVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version and license to install on the Security Gateways.

        Default: R80.40-PAYG-NGTP-GW. Allowed values: R80.40-BYOL-GW, R80.40-PAYG-NGTP-GW, R80.40-PAYG-NGTX-GW, R81-BYOL-GW, R81-PAYG-NGTP-GW, R81-PAYG-NGTX-GW

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewayVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ac830e922f6df56a1ff671f19948c443fccfe044abfdc08ec0fff861fd2e4c2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewayVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewayVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaysAddresses",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaysAddresses:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allow gateways only from this network to communicate with the Security Management Server.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaysAddresses
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c7156c890f157d1dfcd16b5c9d76d53fb15fdcac62ad1357f194adc8fd2b4e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysAddresses#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysAddresses#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaysAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaysBlades",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaysBlades:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Turn on the Intrusion Prevention System, Application Control, Anti-Virus and Anti-Bot Blades (these and additional Blades can be manually turned on or off later).

        Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaysBlades
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b738ae064c628d7aa26000521c0ea96e66043577b80c4f3d7a1305a60da56609)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysBlades#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysBlades#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaysBlades(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaysMaxSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaysMaxSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The maximal number of Security Gateways.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaysMaxSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ce16da5f41bddd19f747435d7e8d27826cd792108e401f6e871190283ce77a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysMaxSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysMaxSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaysMaxSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaysMinSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaysMinSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The minimal number of Security Gateways.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaysMinSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__798e1ced99ede998b8eb24cbd83da0ed642d547e376813dd854603438dc00151)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysMinSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysMinSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaysMinSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaysPolicy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaysPolicy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name of the Security Policy package to be installed on the gateways in the Security Gateways Auto Scaling group.

        Default: Standard

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaysPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53dfa8a9bc23f31e938682f11ad238b7fca940e19b0ed0b5447aa6a06a2f957c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysPolicy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysPolicy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaysPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces) (optional).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d068a2ac936586044d1c6183b064ceb5ff3f9d42f713471d26dacaca046998f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersKeyName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersKeyName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 Key Pair to allow SSH access to the instances.

        For more detail visit: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersKeyName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__589ef24df1010c37a0b9b9e0d38e60d666b6f394447f0cce7e5fb4c7dcffc22a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersKeyName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersKeyName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersKeyName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersLoadBalancersType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersLoadBalancersType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Use Network Load Balancer if you wish to preserve the source IP address and Application Load Balancer if you wish to perform SSL Offloading.

        Default: Network Load Balancer. Allowed values: Network Load Balancer, Application Load Balancer

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersLoadBalancersType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d3e6157e7d263193525fcaa60d8c70ef1c78fd059ea19118a5f9c4a98aaf117)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersLoadBalancersType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersLoadBalancersType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersLoadBalancersType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementDeploy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementDeploy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Select false to use an existing Security Management Server or to deploy one later and to ignore the other parameters of this section.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementDeploy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__371e7d2fcb02d88f8e287e31090e91d9879dc8b22e17b916f5f89c30a2f032c0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementDeploy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementDeploy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementDeploy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementHostname",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementHostname:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(optional).

        Default: mgmt-aws

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementHostname
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e954e6587d2ef206390d38c5d823620dd90e8f6e08db6e23c740a777edd26dc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementHostname#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementHostname#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type of the Security Management Server.

        Default: m5.xlarge. Allowed values: m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.12xlarge, m5.24xlarge

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0cca8396d332e8c716c4f2b4dda922c7b6136a387609f3a8127010b62f17f2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementPasswordHash",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementPasswordHash:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementPasswordHash
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bab924efe4ec2a6f40909cc79b745b2108942e840199474a8e3c17406dfaf03)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementPasswordHash#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementPasswordHash#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementPasswordHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementPermissions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementPermissions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''IAM role to attach to the instance profile of the Management Server.

        Default: Create with read permissions. Allowed values: None (configure later), Use existing (specify an existing IAM role name), Create with assume role permissions (specify an STS role ARN), Create with read permissions, Create with read-write permissions

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementPermissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992d85bf47e48f8bd1145209bdc30d23b8777f0203af71db046d33294cce054d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementPermissions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementPermissions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementPredefinedRole",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementPredefinedRole:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A predefined IAM role to attach to the instance profile.

        Ignored if IAM role is not set to 'Use existing'

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementPredefinedRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8912689afe8756723f1fa4c4ade6302ac38c1bb996c20ed08286c4f1b11286ae)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementPredefinedRole#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementPredefinedRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementPredefinedRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementSicKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementSicKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Mandatory only if deploying a secondary Management Server, the Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementSicKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf2bea786d1c72a87724b54d5b53c081e67193fdd739f2284ad4f4991132abca)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementSicKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementSicKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementSicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EBS Volume size of the management server.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba5871ed379783bc84bcbfde956ea42c33bc94ec84953a6e427cd818e55655b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersManagementVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersManagementVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version and license to install on the Security Management Server.

        Default: R80.40-PAYG-MGMT. Allowed values: R80.40-BYOL-MGMT, R80.40-PAYG-MGMT, R81-BYOL-MGMT, R81-PAYG-MGMT

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersManagementVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba6d0f01c650ecf0e362512a2653f9eafec713d0afcc2510950983175cfa726f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersManagementVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersManagementVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersNlbProtocol",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersNlbProtocol:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The protocol to use on the Network Load Balancer.

        If Application Load Balancer was selected this section will be ignored. Default: TCP. Allowed values: TCP, TLS, UDP, TCP_UDP

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersNlbProtocol
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9c6efaaa36b479f698f581a73747b9df13114d9181c73223cf82e2f57196b7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNlbProtocol#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNlbProtocol#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersNlbProtocol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersNtpPrimary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersNtpPrimary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(optional).

        Default: 169.254.169.123

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersNtpPrimary
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cd3835895cecde5a38417f7a8bfbab8b0d4c1f5b692030d9e17747d3f8bbd3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNtpPrimary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNtpPrimary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersNtpPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersNtpSecondary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersNtpSecondary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(optional).

        Default: 0.pool.ntp.org

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersNtpSecondary
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24dfd7f25930cb8021c923aa9f497d82b08f082b0eb0930d4ce4c711b0ccc7d9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNtpSecondary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNtpSecondary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersNtpSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersNumberOfAZs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersNumberOfAZs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.  Default: 2

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersNumberOfAZs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__764a7b5c4cf23095a088d04f4205b2e5636bd140af8e116e792706b102fd1d8b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNumberOfAZs#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersNumberOfAZs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersNumberOfAZs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPermissions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPermissions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''IAM Permissions for the management server.

        Default: Create with read permissions. Allowed values: Create with read permissions Create with read-write permissions Create with assume role permissions (specify an STS role ARN)

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPermissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__428825e5971d9a728079b37ad0a9a0d63f253182153a1a0254374c205f995baf)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPermissions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPermissions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPrimaryManagement",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPrimaryManagement:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Determines if this is the primary Management Server or not.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPrimaryManagement
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c5cd014614433c7b5cfaba3f72fb1e09aaf95239e78ea55c6fbabeb41bdcce9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrimaryManagement#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrimaryManagement#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPrimaryManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1 located in the 1st Availability Zone.

        Default: 10.0.11.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b15f560e53f6792179ff6b3797c01bed979559b4d5f05e3a1a1357ca7124ca)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.21.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4299402fc52a56427f18c9928e554a1c2bc69f6683b102ddf2b2aa2602759d9e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.31.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75fe73e699be1ab381507982fb1957c9095cf999fed90b921f08db657916d754)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 4 located in the 4th Availability Zone.

        Default: 10.0.41.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96bce719059e14ff3a26def2a109ddc090497fd358e76e4c5fca4e5dda2e420)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersProvisionTag",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersProvisionTag:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The tag is used by the Security Management Server to automatically provision the Security Gateways.

        Must be up to 12 alphanumeric characters and unique for each Quick Start deployment. Default: quickstart

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersProvisionTag
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a188641f5b9b74324d74e164029a36d236996843bafca20e8e351d9ca4233313)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersProvisionTag#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersProvisionTag#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersProvisionTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 1 located in the 1st Availability Zone.

        If you choose to deploy a Security Management Server it will be deployed in this subnet. Default: 10.0.10.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2c240d4625f31af97833c35871088f447471baeb5da0824e8ab0e3475c7b08e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.20.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f292bcfb0a9a43f817dcac91bae8df0a5b5a4936d6491bc1b00488992910f8f0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.30.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b6df933b1dd80e681bc6d7d337171da44fb8ebab76eb799c1edf343bc301a13)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 4 located in the 4th Availability Zone.

        Default: 10.0.40.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f3aeb7a6464009648a96f2d7cc39b96b33a541fc91d50a0289152ae24654d27)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EBS Volume size of the security gateway server.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__919a0214ed436b2313cbf25b472ebdbba59dd19d7ea679020721887b7c6e9694)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServerAmi",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServerAmi:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Amazon Machine Image ID of a preconfigured web server (e.g. ami-0dc7dc63).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServerAmi
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fcd4edbe3ce10480789b5b1a5fb528e728860f4bf9af8584fba4a24705aeb60)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServerAmi#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServerAmi#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServerAmi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServerInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServerInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the web servers.

        Default: t3.micro. Allowed values: t3.nano, t3.micro, t3.small, t3.medium, t3.large, t3.xlarge, t3.2xlarge

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServerInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606083edcf98e0af0b6a2b928492d34257939a488e9cc9ba9a045ed8c1df34f1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServerInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServerInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServerInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServerName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServerName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The servers name tag.

        Default: Server

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServerName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910117380e221fd385a335199a65a25bb94f4f0584f6e0fa8fae91d30dfec6e9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServerName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServersDeploy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServersDeploy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Select true to deploy web servers and an internal Application Load Balancer.

        If you select false the other parameters of this section will be ignored. Default: false

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServersDeploy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0e0a937f6dc8d3c992750079294e147e77c0d9b91a165258d550c0e77957e1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersDeploy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersDeploy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServersDeploy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServersMaxSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServersMaxSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The maximal number of servers in the Auto Scaling group.

        Default: 10

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServersMaxSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__136d9194374305cc93959e80bdb588b3479c6f46448dd4ef260b08941c2cab68)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersMaxSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersMaxSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServersMaxSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServersMinSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServersMinSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The minimal number of servers in the Auto Scaling group.

        Default: 2

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServersMinSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9db38b1ae200859ac23a25dfc52a19007243906a10b755595f28c46de658c1a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersMinSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersMinSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServersMinSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServersTargetGroups",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServersTargetGroups:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''An optional list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServersTargetGroups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c2c962741c7f0ee93ff93d8a602078bc5e3c2b12bcf13900f482da9586109a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersTargetGroups#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServersTargetGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServersTargetGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersServicePort",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersServicePort:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The external Load Balancer listens to this port.

        Leave this field blank to use default ports: 80 for HTTP and 443 for HTTPS

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersServicePort
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923183299703584f359587bc024687a77cdce8ee9e481b99f9637c62e9264674)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServicePort#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersServicePort#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersShellManagementStack",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersShellManagementStack:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed values: /etc/cli.sh, /bin/bash, /bin/csh, /bin/tcsh

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersShellManagementStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4344843f4e5ab56fbcd4fdf3338de39e174ad7c6012515def9ec33bad9ba0a52)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersShellManagementStack#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersShellManagementStack#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersShellManagementStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed Values: /etc/cli.sh /bin/bash /bin/csh /bin/tcsh

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5402e79db2083ed4c3bfd7c63a957e94c140343357cb7a8963de5e426be3f1c4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersSourceSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersSourceSecurityGroup:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The ID of Security Group from which access will be allowed to the instances in this Auto Scaling group.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersSourceSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bd54a85105e991d846d75c9b5928b612f43322f49d8054271302df92dc98c0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersSourceSecurityGroup#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersSourceSecurityGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersSourceSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersStsRoles",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersStsRoles:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The IAM role will be able to assume these STS Roles (comma separated list of ARNs, without spaces).

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersStsRoles
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67422c6845f595119262d78a12a863f79b7c73cd4ce58fb9503f396c960d9c36)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersStsRoles#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersStsRoles#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersStsRoles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 1 located in Availability Zone 1.

        Default: 10.0.12.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95fc8dd08d29177b2c27c6475963cba197a994ebc454935cdfa2051bd2fd4a45)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 2 located in Availability Zone 2.

        Default: 10.0.22.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96edeb1b7b98c137c36ee3e4a938625cad569fcc6774cc85f5ac23c2d7512b55)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 3 located in Availability Zone 3.

        Default: 10.0.32.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9414f5166ddc59b8a0073803e22b0f72f04fe36bd5d9805a9bf9fdfb3ebaa274)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 4 located in Availability Zone 4.

        Default: 10.0.42.0/24

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158289b86782a76f4dd8b4dd13ac4dc368a69a93c34b7c23641bee17ea88b35c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersTrustedAccount",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersTrustedAccount:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A 12 digits number that represents the ID of a trusted account.

        IAM users in this account will be able assume the IAM role and receive the permissions attached to it.

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersTrustedAccount
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__261183f64f5963780cf487a2a948949a21e29b119b748c02d7b6302e314edfac)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTrustedAccount#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersTrustedAccount#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersTrustedAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudGuardQsModulePropsParametersVpccidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        Default: 10.0.0.0/16

        :param description: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsParametersVpccidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b1a13ab59c6e031a966f4764621ebabd74f417dc216b4dd5bdc591c11bdfff)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersVpccidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudGuardQsModulePropsParametersVpccidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsParametersVpccidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "address_assoc": "addressAssoc",
        "chkp_gateway_role": "chkpGatewayRole",
        "cmeiam_role": "cmeiamRole",
        "cpu_alarm_high": "cpuAlarmHigh",
        "cpu_alarm_high_security_gateway_stack": "cpuAlarmHighSecurityGatewayStack",
        "cpu_alarm_low": "cpuAlarmLow",
        "cpu_alarm_low_security_gateway_stack": "cpuAlarmLowSecurityGatewayStack",
        "elastic_load_balancer": "elasticLoadBalancer",
        "elb_security_group": "elbSecurityGroup",
        "external_alb_security_group": "externalAlbSecurityGroup",
        "external_lb_listener": "externalLbListener",
        "external_lb_target_group": "externalLbTargetGroup",
        "external_load_balancer": "externalLoadBalancer",
        "gateway_group": "gatewayGroup",
        "gateway_launch_config": "gatewayLaunchConfig",
        "gateway_scale_down_policy": "gatewayScaleDownPolicy",
        "gateway_scale_up_policy": "gatewayScaleUpPolicy",
        "instance_profile": "instanceProfile",
        "instance_profile_security_gateway_stack": "instanceProfileSecurityGatewayStack",
        "internal_lb_listener": "internalLbListener",
        "internal_lb_target_group": "internalLbTargetGroup",
        "internal_load_balancer": "internalLoadBalancer",
        "internal_security_group": "internalSecurityGroup",
        "internet_gateway": "internetGateway",
        "management_instance": "managementInstance",
        "management_ready_condition": "managementReadyCondition",
        "management_ready_handle": "managementReadyHandle",
        "management_security_group": "managementSecurityGroup",
        "notification_topic": "notificationTopic",
        "notification_topic_security_gateway_stack": "notificationTopicSecurityGatewayStack",
        "permissive_security_group": "permissiveSecurityGroup",
        "private_subnet1": "privateSubnet1",
        "private_subnet2": "privateSubnet2",
        "private_subnet3": "privateSubnet3",
        "private_subnet4": "privateSubnet4",
        "public_address": "publicAddress",
        "public_subnet1": "publicSubnet1",
        "public_subnet1_route_table_association": "publicSubnet1RouteTableAssociation",
        "public_subnet2": "publicSubnet2",
        "public_subnet2_route_table_association": "publicSubnet2RouteTableAssociation",
        "public_subnet3": "publicSubnet3",
        "public_subnet3_route_table_association": "publicSubnet3RouteTableAssociation",
        "public_subnet4": "publicSubnet4",
        "public_subnet4_route_table_association": "publicSubnet4RouteTableAssociation",
        "public_subnet_route": "publicSubnetRoute",
        "public_subnet_route_table": "publicSubnetRouteTable",
        "scale_down_policy": "scaleDownPolicy",
        "scale_up_policy": "scaleUpPolicy",
        "servers_group": "serversGroup",
        "servers_launch_configuration": "serversLaunchConfiguration",
        "servers_security_group": "serversSecurityGroup",
        "tgw_subnet1": "tgwSubnet1",
        "tgw_subnet2": "tgwSubnet2",
        "tgw_subnet3": "tgwSubnet3",
        "tgw_subnet4": "tgwSubnet4",
        "vpc": "vpc",
        "vpc_gateway_attachment": "vpcGatewayAttachment",
    },
)
class CfnCloudGuardQsModulePropsResources:
    def __init__(
        self,
        *,
        address_assoc: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesAddressAssoc", typing.Dict[builtins.str, typing.Any]]] = None,
        chkp_gateway_role: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesChkpGatewayRole", typing.Dict[builtins.str, typing.Any]]] = None,
        cmeiam_role: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesCmeiamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_alarm_high: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_alarm_high_security_gateway_stack: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_alarm_low: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesCpuAlarmLow", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_alarm_low_security_gateway_stack: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack", typing.Dict[builtins.str, typing.Any]]] = None,
        elastic_load_balancer: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesElbSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        external_alb_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        external_lb_listener: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesExternalLbListener", typing.Dict[builtins.str, typing.Any]]] = None,
        external_lb_target_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        external_load_balancer: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesGatewayGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_launch_config: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_scale_down_policy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        gateway_scale_up_policy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_profile: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInstanceProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_profile_security_gateway_stack: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack", typing.Dict[builtins.str, typing.Any]]] = None,
        internal_lb_listener: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInternalLbListener", typing.Dict[builtins.str, typing.Any]]] = None,
        internal_lb_target_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        internal_load_balancer: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer", typing.Dict[builtins.str, typing.Any]]] = None,
        internal_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        internet_gateway: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesInternetGateway", typing.Dict[builtins.str, typing.Any]]] = None,
        management_instance: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesManagementInstance", typing.Dict[builtins.str, typing.Any]]] = None,
        management_ready_condition: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesManagementReadyCondition", typing.Dict[builtins.str, typing.Any]]] = None,
        management_ready_handle: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesManagementReadyHandle", typing.Dict[builtins.str, typing.Any]]] = None,
        management_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_topic: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesNotificationTopic", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_topic_security_gateway_stack: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack", typing.Dict[builtins.str, typing.Any]]] = None,
        permissive_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPrivateSubnet1", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPrivateSubnet2", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPrivateSubnet3", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPrivateSubnet4", typing.Dict[builtins.str, typing.Any]]] = None,
        public_address: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicAddress", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet1", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_route_table_association: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet2", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_route_table_association: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet3: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet3", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet3_route_table_association: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet4: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet4", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet4_route_table_association: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_route: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_route_table: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_down_policy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesScaleDownPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_up_policy: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesScaleUpPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesServersGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_launch_configuration: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        servers_security_group: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesServersSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet1: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesTgwSubnet1", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet2: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesTgwSubnet2", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet3: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesTgwSubnet3", typing.Dict[builtins.str, typing.Any]]] = None,
        tgw_subnet4: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesTgwSubnet4", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesVpc", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_gateway_attachment: typing.Optional[typing.Union["CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param address_assoc: 
        :param chkp_gateway_role: 
        :param cmeiam_role: 
        :param cpu_alarm_high: 
        :param cpu_alarm_high_security_gateway_stack: 
        :param cpu_alarm_low: 
        :param cpu_alarm_low_security_gateway_stack: 
        :param elastic_load_balancer: 
        :param elb_security_group: 
        :param external_alb_security_group: 
        :param external_lb_listener: 
        :param external_lb_target_group: 
        :param external_load_balancer: 
        :param gateway_group: 
        :param gateway_launch_config: 
        :param gateway_scale_down_policy: 
        :param gateway_scale_up_policy: 
        :param instance_profile: 
        :param instance_profile_security_gateway_stack: 
        :param internal_lb_listener: 
        :param internal_lb_target_group: 
        :param internal_load_balancer: 
        :param internal_security_group: 
        :param internet_gateway: 
        :param management_instance: 
        :param management_ready_condition: 
        :param management_ready_handle: 
        :param management_security_group: 
        :param notification_topic: 
        :param notification_topic_security_gateway_stack: 
        :param permissive_security_group: 
        :param private_subnet1: 
        :param private_subnet2: 
        :param private_subnet3: 
        :param private_subnet4: 
        :param public_address: 
        :param public_subnet1: 
        :param public_subnet1_route_table_association: 
        :param public_subnet2: 
        :param public_subnet2_route_table_association: 
        :param public_subnet3: 
        :param public_subnet3_route_table_association: 
        :param public_subnet4: 
        :param public_subnet4_route_table_association: 
        :param public_subnet_route: 
        :param public_subnet_route_table: 
        :param scale_down_policy: 
        :param scale_up_policy: 
        :param servers_group: 
        :param servers_launch_configuration: 
        :param servers_security_group: 
        :param tgw_subnet1: 
        :param tgw_subnet2: 
        :param tgw_subnet3: 
        :param tgw_subnet4: 
        :param vpc: 
        :param vpc_gateway_attachment: 

        :schema: CfnCloudGuardQsModulePropsResources
        '''
        if isinstance(address_assoc, dict):
            address_assoc = CfnCloudGuardQsModulePropsResourcesAddressAssoc(**address_assoc)
        if isinstance(chkp_gateway_role, dict):
            chkp_gateway_role = CfnCloudGuardQsModulePropsResourcesChkpGatewayRole(**chkp_gateway_role)
        if isinstance(cmeiam_role, dict):
            cmeiam_role = CfnCloudGuardQsModulePropsResourcesCmeiamRole(**cmeiam_role)
        if isinstance(cpu_alarm_high, dict):
            cpu_alarm_high = CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh(**cpu_alarm_high)
        if isinstance(cpu_alarm_high_security_gateway_stack, dict):
            cpu_alarm_high_security_gateway_stack = CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack(**cpu_alarm_high_security_gateway_stack)
        if isinstance(cpu_alarm_low, dict):
            cpu_alarm_low = CfnCloudGuardQsModulePropsResourcesCpuAlarmLow(**cpu_alarm_low)
        if isinstance(cpu_alarm_low_security_gateway_stack, dict):
            cpu_alarm_low_security_gateway_stack = CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack(**cpu_alarm_low_security_gateway_stack)
        if isinstance(elastic_load_balancer, dict):
            elastic_load_balancer = CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer(**elastic_load_balancer)
        if isinstance(elb_security_group, dict):
            elb_security_group = CfnCloudGuardQsModulePropsResourcesElbSecurityGroup(**elb_security_group)
        if isinstance(external_alb_security_group, dict):
            external_alb_security_group = CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup(**external_alb_security_group)
        if isinstance(external_lb_listener, dict):
            external_lb_listener = CfnCloudGuardQsModulePropsResourcesExternalLbListener(**external_lb_listener)
        if isinstance(external_lb_target_group, dict):
            external_lb_target_group = CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup(**external_lb_target_group)
        if isinstance(external_load_balancer, dict):
            external_load_balancer = CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer(**external_load_balancer)
        if isinstance(gateway_group, dict):
            gateway_group = CfnCloudGuardQsModulePropsResourcesGatewayGroup(**gateway_group)
        if isinstance(gateway_launch_config, dict):
            gateway_launch_config = CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig(**gateway_launch_config)
        if isinstance(gateway_scale_down_policy, dict):
            gateway_scale_down_policy = CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy(**gateway_scale_down_policy)
        if isinstance(gateway_scale_up_policy, dict):
            gateway_scale_up_policy = CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy(**gateway_scale_up_policy)
        if isinstance(instance_profile, dict):
            instance_profile = CfnCloudGuardQsModulePropsResourcesInstanceProfile(**instance_profile)
        if isinstance(instance_profile_security_gateway_stack, dict):
            instance_profile_security_gateway_stack = CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack(**instance_profile_security_gateway_stack)
        if isinstance(internal_lb_listener, dict):
            internal_lb_listener = CfnCloudGuardQsModulePropsResourcesInternalLbListener(**internal_lb_listener)
        if isinstance(internal_lb_target_group, dict):
            internal_lb_target_group = CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup(**internal_lb_target_group)
        if isinstance(internal_load_balancer, dict):
            internal_load_balancer = CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer(**internal_load_balancer)
        if isinstance(internal_security_group, dict):
            internal_security_group = CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup(**internal_security_group)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnCloudGuardQsModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(management_instance, dict):
            management_instance = CfnCloudGuardQsModulePropsResourcesManagementInstance(**management_instance)
        if isinstance(management_ready_condition, dict):
            management_ready_condition = CfnCloudGuardQsModulePropsResourcesManagementReadyCondition(**management_ready_condition)
        if isinstance(management_ready_handle, dict):
            management_ready_handle = CfnCloudGuardQsModulePropsResourcesManagementReadyHandle(**management_ready_handle)
        if isinstance(management_security_group, dict):
            management_security_group = CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup(**management_security_group)
        if isinstance(notification_topic, dict):
            notification_topic = CfnCloudGuardQsModulePropsResourcesNotificationTopic(**notification_topic)
        if isinstance(notification_topic_security_gateway_stack, dict):
            notification_topic_security_gateway_stack = CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack(**notification_topic_security_gateway_stack)
        if isinstance(permissive_security_group, dict):
            permissive_security_group = CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup(**permissive_security_group)
        if isinstance(private_subnet1, dict):
            private_subnet1 = CfnCloudGuardQsModulePropsResourcesPrivateSubnet1(**private_subnet1)
        if isinstance(private_subnet2, dict):
            private_subnet2 = CfnCloudGuardQsModulePropsResourcesPrivateSubnet2(**private_subnet2)
        if isinstance(private_subnet3, dict):
            private_subnet3 = CfnCloudGuardQsModulePropsResourcesPrivateSubnet3(**private_subnet3)
        if isinstance(private_subnet4, dict):
            private_subnet4 = CfnCloudGuardQsModulePropsResourcesPrivateSubnet4(**private_subnet4)
        if isinstance(public_address, dict):
            public_address = CfnCloudGuardQsModulePropsResourcesPublicAddress(**public_address)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnCloudGuardQsModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnCloudGuardQsModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet3, dict):
            public_subnet3 = CfnCloudGuardQsModulePropsResourcesPublicSubnet3(**public_subnet3)
        if isinstance(public_subnet3_route_table_association, dict):
            public_subnet3_route_table_association = CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation(**public_subnet3_route_table_association)
        if isinstance(public_subnet4, dict):
            public_subnet4 = CfnCloudGuardQsModulePropsResourcesPublicSubnet4(**public_subnet4)
        if isinstance(public_subnet4_route_table_association, dict):
            public_subnet4_route_table_association = CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation(**public_subnet4_route_table_association)
        if isinstance(public_subnet_route, dict):
            public_subnet_route = CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute(**public_subnet_route)
        if isinstance(public_subnet_route_table, dict):
            public_subnet_route_table = CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable(**public_subnet_route_table)
        if isinstance(scale_down_policy, dict):
            scale_down_policy = CfnCloudGuardQsModulePropsResourcesScaleDownPolicy(**scale_down_policy)
        if isinstance(scale_up_policy, dict):
            scale_up_policy = CfnCloudGuardQsModulePropsResourcesScaleUpPolicy(**scale_up_policy)
        if isinstance(servers_group, dict):
            servers_group = CfnCloudGuardQsModulePropsResourcesServersGroup(**servers_group)
        if isinstance(servers_launch_configuration, dict):
            servers_launch_configuration = CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration(**servers_launch_configuration)
        if isinstance(servers_security_group, dict):
            servers_security_group = CfnCloudGuardQsModulePropsResourcesServersSecurityGroup(**servers_security_group)
        if isinstance(tgw_subnet1, dict):
            tgw_subnet1 = CfnCloudGuardQsModulePropsResourcesTgwSubnet1(**tgw_subnet1)
        if isinstance(tgw_subnet2, dict):
            tgw_subnet2 = CfnCloudGuardQsModulePropsResourcesTgwSubnet2(**tgw_subnet2)
        if isinstance(tgw_subnet3, dict):
            tgw_subnet3 = CfnCloudGuardQsModulePropsResourcesTgwSubnet3(**tgw_subnet3)
        if isinstance(tgw_subnet4, dict):
            tgw_subnet4 = CfnCloudGuardQsModulePropsResourcesTgwSubnet4(**tgw_subnet4)
        if isinstance(vpc, dict):
            vpc = CfnCloudGuardQsModulePropsResourcesVpc(**vpc)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee95227a37dee0c2c796fd9bf5426b567fb13eefe7c40e09de4c434331a27b6c)
            check_type(argname="argument address_assoc", value=address_assoc, expected_type=type_hints["address_assoc"])
            check_type(argname="argument chkp_gateway_role", value=chkp_gateway_role, expected_type=type_hints["chkp_gateway_role"])
            check_type(argname="argument cmeiam_role", value=cmeiam_role, expected_type=type_hints["cmeiam_role"])
            check_type(argname="argument cpu_alarm_high", value=cpu_alarm_high, expected_type=type_hints["cpu_alarm_high"])
            check_type(argname="argument cpu_alarm_high_security_gateway_stack", value=cpu_alarm_high_security_gateway_stack, expected_type=type_hints["cpu_alarm_high_security_gateway_stack"])
            check_type(argname="argument cpu_alarm_low", value=cpu_alarm_low, expected_type=type_hints["cpu_alarm_low"])
            check_type(argname="argument cpu_alarm_low_security_gateway_stack", value=cpu_alarm_low_security_gateway_stack, expected_type=type_hints["cpu_alarm_low_security_gateway_stack"])
            check_type(argname="argument elastic_load_balancer", value=elastic_load_balancer, expected_type=type_hints["elastic_load_balancer"])
            check_type(argname="argument elb_security_group", value=elb_security_group, expected_type=type_hints["elb_security_group"])
            check_type(argname="argument external_alb_security_group", value=external_alb_security_group, expected_type=type_hints["external_alb_security_group"])
            check_type(argname="argument external_lb_listener", value=external_lb_listener, expected_type=type_hints["external_lb_listener"])
            check_type(argname="argument external_lb_target_group", value=external_lb_target_group, expected_type=type_hints["external_lb_target_group"])
            check_type(argname="argument external_load_balancer", value=external_load_balancer, expected_type=type_hints["external_load_balancer"])
            check_type(argname="argument gateway_group", value=gateway_group, expected_type=type_hints["gateway_group"])
            check_type(argname="argument gateway_launch_config", value=gateway_launch_config, expected_type=type_hints["gateway_launch_config"])
            check_type(argname="argument gateway_scale_down_policy", value=gateway_scale_down_policy, expected_type=type_hints["gateway_scale_down_policy"])
            check_type(argname="argument gateway_scale_up_policy", value=gateway_scale_up_policy, expected_type=type_hints["gateway_scale_up_policy"])
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
            check_type(argname="argument instance_profile_security_gateway_stack", value=instance_profile_security_gateway_stack, expected_type=type_hints["instance_profile_security_gateway_stack"])
            check_type(argname="argument internal_lb_listener", value=internal_lb_listener, expected_type=type_hints["internal_lb_listener"])
            check_type(argname="argument internal_lb_target_group", value=internal_lb_target_group, expected_type=type_hints["internal_lb_target_group"])
            check_type(argname="argument internal_load_balancer", value=internal_load_balancer, expected_type=type_hints["internal_load_balancer"])
            check_type(argname="argument internal_security_group", value=internal_security_group, expected_type=type_hints["internal_security_group"])
            check_type(argname="argument internet_gateway", value=internet_gateway, expected_type=type_hints["internet_gateway"])
            check_type(argname="argument management_instance", value=management_instance, expected_type=type_hints["management_instance"])
            check_type(argname="argument management_ready_condition", value=management_ready_condition, expected_type=type_hints["management_ready_condition"])
            check_type(argname="argument management_ready_handle", value=management_ready_handle, expected_type=type_hints["management_ready_handle"])
            check_type(argname="argument management_security_group", value=management_security_group, expected_type=type_hints["management_security_group"])
            check_type(argname="argument notification_topic", value=notification_topic, expected_type=type_hints["notification_topic"])
            check_type(argname="argument notification_topic_security_gateway_stack", value=notification_topic_security_gateway_stack, expected_type=type_hints["notification_topic_security_gateway_stack"])
            check_type(argname="argument permissive_security_group", value=permissive_security_group, expected_type=type_hints["permissive_security_group"])
            check_type(argname="argument private_subnet1", value=private_subnet1, expected_type=type_hints["private_subnet1"])
            check_type(argname="argument private_subnet2", value=private_subnet2, expected_type=type_hints["private_subnet2"])
            check_type(argname="argument private_subnet3", value=private_subnet3, expected_type=type_hints["private_subnet3"])
            check_type(argname="argument private_subnet4", value=private_subnet4, expected_type=type_hints["private_subnet4"])
            check_type(argname="argument public_address", value=public_address, expected_type=type_hints["public_address"])
            check_type(argname="argument public_subnet1", value=public_subnet1, expected_type=type_hints["public_subnet1"])
            check_type(argname="argument public_subnet1_route_table_association", value=public_subnet1_route_table_association, expected_type=type_hints["public_subnet1_route_table_association"])
            check_type(argname="argument public_subnet2", value=public_subnet2, expected_type=type_hints["public_subnet2"])
            check_type(argname="argument public_subnet2_route_table_association", value=public_subnet2_route_table_association, expected_type=type_hints["public_subnet2_route_table_association"])
            check_type(argname="argument public_subnet3", value=public_subnet3, expected_type=type_hints["public_subnet3"])
            check_type(argname="argument public_subnet3_route_table_association", value=public_subnet3_route_table_association, expected_type=type_hints["public_subnet3_route_table_association"])
            check_type(argname="argument public_subnet4", value=public_subnet4, expected_type=type_hints["public_subnet4"])
            check_type(argname="argument public_subnet4_route_table_association", value=public_subnet4_route_table_association, expected_type=type_hints["public_subnet4_route_table_association"])
            check_type(argname="argument public_subnet_route", value=public_subnet_route, expected_type=type_hints["public_subnet_route"])
            check_type(argname="argument public_subnet_route_table", value=public_subnet_route_table, expected_type=type_hints["public_subnet_route_table"])
            check_type(argname="argument scale_down_policy", value=scale_down_policy, expected_type=type_hints["scale_down_policy"])
            check_type(argname="argument scale_up_policy", value=scale_up_policy, expected_type=type_hints["scale_up_policy"])
            check_type(argname="argument servers_group", value=servers_group, expected_type=type_hints["servers_group"])
            check_type(argname="argument servers_launch_configuration", value=servers_launch_configuration, expected_type=type_hints["servers_launch_configuration"])
            check_type(argname="argument servers_security_group", value=servers_security_group, expected_type=type_hints["servers_security_group"])
            check_type(argname="argument tgw_subnet1", value=tgw_subnet1, expected_type=type_hints["tgw_subnet1"])
            check_type(argname="argument tgw_subnet2", value=tgw_subnet2, expected_type=type_hints["tgw_subnet2"])
            check_type(argname="argument tgw_subnet3", value=tgw_subnet3, expected_type=type_hints["tgw_subnet3"])
            check_type(argname="argument tgw_subnet4", value=tgw_subnet4, expected_type=type_hints["tgw_subnet4"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_gateway_attachment", value=vpc_gateway_attachment, expected_type=type_hints["vpc_gateway_attachment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if address_assoc is not None:
            self._values["address_assoc"] = address_assoc
        if chkp_gateway_role is not None:
            self._values["chkp_gateway_role"] = chkp_gateway_role
        if cmeiam_role is not None:
            self._values["cmeiam_role"] = cmeiam_role
        if cpu_alarm_high is not None:
            self._values["cpu_alarm_high"] = cpu_alarm_high
        if cpu_alarm_high_security_gateway_stack is not None:
            self._values["cpu_alarm_high_security_gateway_stack"] = cpu_alarm_high_security_gateway_stack
        if cpu_alarm_low is not None:
            self._values["cpu_alarm_low"] = cpu_alarm_low
        if cpu_alarm_low_security_gateway_stack is not None:
            self._values["cpu_alarm_low_security_gateway_stack"] = cpu_alarm_low_security_gateway_stack
        if elastic_load_balancer is not None:
            self._values["elastic_load_balancer"] = elastic_load_balancer
        if elb_security_group is not None:
            self._values["elb_security_group"] = elb_security_group
        if external_alb_security_group is not None:
            self._values["external_alb_security_group"] = external_alb_security_group
        if external_lb_listener is not None:
            self._values["external_lb_listener"] = external_lb_listener
        if external_lb_target_group is not None:
            self._values["external_lb_target_group"] = external_lb_target_group
        if external_load_balancer is not None:
            self._values["external_load_balancer"] = external_load_balancer
        if gateway_group is not None:
            self._values["gateway_group"] = gateway_group
        if gateway_launch_config is not None:
            self._values["gateway_launch_config"] = gateway_launch_config
        if gateway_scale_down_policy is not None:
            self._values["gateway_scale_down_policy"] = gateway_scale_down_policy
        if gateway_scale_up_policy is not None:
            self._values["gateway_scale_up_policy"] = gateway_scale_up_policy
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile
        if instance_profile_security_gateway_stack is not None:
            self._values["instance_profile_security_gateway_stack"] = instance_profile_security_gateway_stack
        if internal_lb_listener is not None:
            self._values["internal_lb_listener"] = internal_lb_listener
        if internal_lb_target_group is not None:
            self._values["internal_lb_target_group"] = internal_lb_target_group
        if internal_load_balancer is not None:
            self._values["internal_load_balancer"] = internal_load_balancer
        if internal_security_group is not None:
            self._values["internal_security_group"] = internal_security_group
        if internet_gateway is not None:
            self._values["internet_gateway"] = internet_gateway
        if management_instance is not None:
            self._values["management_instance"] = management_instance
        if management_ready_condition is not None:
            self._values["management_ready_condition"] = management_ready_condition
        if management_ready_handle is not None:
            self._values["management_ready_handle"] = management_ready_handle
        if management_security_group is not None:
            self._values["management_security_group"] = management_security_group
        if notification_topic is not None:
            self._values["notification_topic"] = notification_topic
        if notification_topic_security_gateway_stack is not None:
            self._values["notification_topic_security_gateway_stack"] = notification_topic_security_gateway_stack
        if permissive_security_group is not None:
            self._values["permissive_security_group"] = permissive_security_group
        if private_subnet1 is not None:
            self._values["private_subnet1"] = private_subnet1
        if private_subnet2 is not None:
            self._values["private_subnet2"] = private_subnet2
        if private_subnet3 is not None:
            self._values["private_subnet3"] = private_subnet3
        if private_subnet4 is not None:
            self._values["private_subnet4"] = private_subnet4
        if public_address is not None:
            self._values["public_address"] = public_address
        if public_subnet1 is not None:
            self._values["public_subnet1"] = public_subnet1
        if public_subnet1_route_table_association is not None:
            self._values["public_subnet1_route_table_association"] = public_subnet1_route_table_association
        if public_subnet2 is not None:
            self._values["public_subnet2"] = public_subnet2
        if public_subnet2_route_table_association is not None:
            self._values["public_subnet2_route_table_association"] = public_subnet2_route_table_association
        if public_subnet3 is not None:
            self._values["public_subnet3"] = public_subnet3
        if public_subnet3_route_table_association is not None:
            self._values["public_subnet3_route_table_association"] = public_subnet3_route_table_association
        if public_subnet4 is not None:
            self._values["public_subnet4"] = public_subnet4
        if public_subnet4_route_table_association is not None:
            self._values["public_subnet4_route_table_association"] = public_subnet4_route_table_association
        if public_subnet_route is not None:
            self._values["public_subnet_route"] = public_subnet_route
        if public_subnet_route_table is not None:
            self._values["public_subnet_route_table"] = public_subnet_route_table
        if scale_down_policy is not None:
            self._values["scale_down_policy"] = scale_down_policy
        if scale_up_policy is not None:
            self._values["scale_up_policy"] = scale_up_policy
        if servers_group is not None:
            self._values["servers_group"] = servers_group
        if servers_launch_configuration is not None:
            self._values["servers_launch_configuration"] = servers_launch_configuration
        if servers_security_group is not None:
            self._values["servers_security_group"] = servers_security_group
        if tgw_subnet1 is not None:
            self._values["tgw_subnet1"] = tgw_subnet1
        if tgw_subnet2 is not None:
            self._values["tgw_subnet2"] = tgw_subnet2
        if tgw_subnet3 is not None:
            self._values["tgw_subnet3"] = tgw_subnet3
        if tgw_subnet4 is not None:
            self._values["tgw_subnet4"] = tgw_subnet4
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_gateway_attachment is not None:
            self._values["vpc_gateway_attachment"] = vpc_gateway_attachment

    @builtins.property
    def address_assoc(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesAddressAssoc"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#AddressAssoc
        '''
        result = self._values.get("address_assoc")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesAddressAssoc"], result)

    @builtins.property
    def chkp_gateway_role(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesChkpGatewayRole"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ChkpGatewayRole
        '''
        result = self._values.get("chkp_gateway_role")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesChkpGatewayRole"], result)

    @builtins.property
    def cmeiam_role(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesCmeiamRole"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#CMEIAMRole
        '''
        result = self._values.get("cmeiam_role")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesCmeiamRole"], result)

    @builtins.property
    def cpu_alarm_high(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#CPUAlarmHigh
        '''
        result = self._values.get("cpu_alarm_high")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh"], result)

    @builtins.property
    def cpu_alarm_high_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#CPUAlarmHighSecurityGatewayStack
        '''
        result = self._values.get("cpu_alarm_high_security_gateway_stack")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack"], result)

    @builtins.property
    def cpu_alarm_low(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmLow"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#CPUAlarmLow
        '''
        result = self._values.get("cpu_alarm_low")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmLow"], result)

    @builtins.property
    def cpu_alarm_low_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#CPUAlarmLowSecurityGatewayStack
        '''
        result = self._values.get("cpu_alarm_low_security_gateway_stack")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack"], result)

    @builtins.property
    def elastic_load_balancer(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ElasticLoadBalancer
        '''
        result = self._values.get("elastic_load_balancer")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer"], result)

    @builtins.property
    def elb_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesElbSecurityGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ELBSecurityGroup
        '''
        result = self._values.get("elb_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesElbSecurityGroup"], result)

    @builtins.property
    def external_alb_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ExternalALBSecurityGroup
        '''
        result = self._values.get("external_alb_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup"], result)

    @builtins.property
    def external_lb_listener(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalLbListener"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ExternalLBListener
        '''
        result = self._values.get("external_lb_listener")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalLbListener"], result)

    @builtins.property
    def external_lb_target_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ExternalLBTargetGroup
        '''
        result = self._values.get("external_lb_target_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup"], result)

    @builtins.property
    def external_load_balancer(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ExternalLoadBalancer
        '''
        result = self._values.get("external_load_balancer")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer"], result)

    @builtins.property
    def gateway_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#GatewayGroup
        '''
        result = self._values.get("gateway_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayGroup"], result)

    @builtins.property
    def gateway_launch_config(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#GatewayLaunchConfig
        '''
        result = self._values.get("gateway_launch_config")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig"], result)

    @builtins.property
    def gateway_scale_down_policy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#GatewayScaleDownPolicy
        '''
        result = self._values.get("gateway_scale_down_policy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy"], result)

    @builtins.property
    def gateway_scale_up_policy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#GatewayScaleUpPolicy
        '''
        result = self._values.get("gateway_scale_up_policy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy"], result)

    @builtins.property
    def instance_profile(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInstanceProfile"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InstanceProfile
        '''
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInstanceProfile"], result)

    @builtins.property
    def instance_profile_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InstanceProfileSecurityGatewayStack
        '''
        result = self._values.get("instance_profile_security_gateway_stack")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack"], result)

    @builtins.property
    def internal_lb_listener(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalLbListener"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InternalLBListener
        '''
        result = self._values.get("internal_lb_listener")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalLbListener"], result)

    @builtins.property
    def internal_lb_target_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InternalLBTargetGroup
        '''
        result = self._values.get("internal_lb_target_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup"], result)

    @builtins.property
    def internal_load_balancer(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InternalLoadBalancer
        '''
        result = self._values.get("internal_load_balancer")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer"], result)

    @builtins.property
    def internal_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InternalSecurityGroup
        '''
        result = self._values.get("internal_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup"], result)

    @builtins.property
    def internet_gateway(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesInternetGateway"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#InternetGateway
        '''
        result = self._values.get("internet_gateway")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesInternetGateway"], result)

    @builtins.property
    def management_instance(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementInstance"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ManagementInstance
        '''
        result = self._values.get("management_instance")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementInstance"], result)

    @builtins.property
    def management_ready_condition(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementReadyCondition"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ManagementReadyCondition
        '''
        result = self._values.get("management_ready_condition")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementReadyCondition"], result)

    @builtins.property
    def management_ready_handle(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementReadyHandle"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ManagementReadyHandle
        '''
        result = self._values.get("management_ready_handle")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementReadyHandle"], result)

    @builtins.property
    def management_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ManagementSecurityGroup
        '''
        result = self._values.get("management_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup"], result)

    @builtins.property
    def notification_topic(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesNotificationTopic"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#NotificationTopic
        '''
        result = self._values.get("notification_topic")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesNotificationTopic"], result)

    @builtins.property
    def notification_topic_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#NotificationTopicSecurityGatewayStack
        '''
        result = self._values.get("notification_topic_security_gateway_stack")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack"], result)

    @builtins.property
    def permissive_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PermissiveSecurityGroup
        '''
        result = self._values.get("permissive_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup"], result)

    @builtins.property
    def private_subnet1(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet1"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PrivateSubnet1
        '''
        result = self._values.get("private_subnet1")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet1"], result)

    @builtins.property
    def private_subnet2(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet2"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PrivateSubnet2
        '''
        result = self._values.get("private_subnet2")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet2"], result)

    @builtins.property
    def private_subnet3(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet3"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PrivateSubnet3
        '''
        result = self._values.get("private_subnet3")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet3"], result)

    @builtins.property
    def private_subnet4(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet4"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PrivateSubnet4
        '''
        result = self._values.get("private_subnet4")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPrivateSubnet4"], result)

    @builtins.property
    def public_address(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicAddress"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicAddress
        '''
        result = self._values.get("public_address")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicAddress"], result)

    @builtins.property
    def public_subnet1(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet1"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet1
        '''
        result = self._values.get("public_subnet1")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet1"], result)

    @builtins.property
    def public_subnet1_route_table_association(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet1RouteTableAssociation
        '''
        result = self._values.get("public_subnet1_route_table_association")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation"], result)

    @builtins.property
    def public_subnet2(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet2"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet2
        '''
        result = self._values.get("public_subnet2")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet2"], result)

    @builtins.property
    def public_subnet2_route_table_association(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet2RouteTableAssociation
        '''
        result = self._values.get("public_subnet2_route_table_association")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation"], result)

    @builtins.property
    def public_subnet3(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet3"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet3
        '''
        result = self._values.get("public_subnet3")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet3"], result)

    @builtins.property
    def public_subnet3_route_table_association(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet3RouteTableAssociation
        '''
        result = self._values.get("public_subnet3_route_table_association")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation"], result)

    @builtins.property
    def public_subnet4(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet4"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet4
        '''
        result = self._values.get("public_subnet4")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet4"], result)

    @builtins.property
    def public_subnet4_route_table_association(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnet4RouteTableAssociation
        '''
        result = self._values.get("public_subnet4_route_table_association")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation"], result)

    @builtins.property
    def public_subnet_route(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnetRoute
        '''
        result = self._values.get("public_subnet_route")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute"], result)

    @builtins.property
    def public_subnet_route_table(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#PublicSubnetRouteTable
        '''
        result = self._values.get("public_subnet_route_table")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable"], result)

    @builtins.property
    def scale_down_policy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesScaleDownPolicy"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ScaleDownPolicy
        '''
        result = self._values.get("scale_down_policy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesScaleDownPolicy"], result)

    @builtins.property
    def scale_up_policy(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesScaleUpPolicy"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ScaleUpPolicy
        '''
        result = self._values.get("scale_up_policy")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesScaleUpPolicy"], result)

    @builtins.property
    def servers_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesServersGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ServersGroup
        '''
        result = self._values.get("servers_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesServersGroup"], result)

    @builtins.property
    def servers_launch_configuration(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ServersLaunchConfiguration
        '''
        result = self._values.get("servers_launch_configuration")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration"], result)

    @builtins.property
    def servers_security_group(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesServersSecurityGroup"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#ServersSecurityGroup
        '''
        result = self._values.get("servers_security_group")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesServersSecurityGroup"], result)

    @builtins.property
    def tgw_subnet1(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet1"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#TgwSubnet1
        '''
        result = self._values.get("tgw_subnet1")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet1"], result)

    @builtins.property
    def tgw_subnet2(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet2"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#TgwSubnet2
        '''
        result = self._values.get("tgw_subnet2")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet2"], result)

    @builtins.property
    def tgw_subnet3(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet3"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#TgwSubnet3
        '''
        result = self._values.get("tgw_subnet3")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet3"], result)

    @builtins.property
    def tgw_subnet4(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet4"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#TgwSubnet4
        '''
        result = self._values.get("tgw_subnet4")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesTgwSubnet4"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesVpc"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesVpc"], result)

    @builtins.property
    def vpc_gateway_attachment(
        self,
    ) -> typing.Optional["CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment"]:
        '''
        :schema: CfnCloudGuardQsModulePropsResources#VPCGatewayAttachment
        '''
        result = self._values.get("vpc_gateway_attachment")
        return typing.cast(typing.Optional["CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesAddressAssoc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesAddressAssoc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesAddressAssoc
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e46d231f73c0ef0b9cb6a3faa764310681c149fee8bb5c9432d267008fb9b3)
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
        :schema: CfnCloudGuardQsModulePropsResourcesAddressAssoc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesAddressAssoc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesAddressAssoc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesChkpGatewayRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesChkpGatewayRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesChkpGatewayRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7b053fa217300cc156bf3f92267f92afcda8f6122d852070e266936bf1bd017)
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
        :schema: CfnCloudGuardQsModulePropsResourcesChkpGatewayRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesChkpGatewayRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesChkpGatewayRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesCmeiamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesCmeiamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesCmeiamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4cdd701e507d71ec1b958142eba98e1639a8c2c557b96c087addea3b47c349f)
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
        :schema: CfnCloudGuardQsModulePropsResourcesCmeiamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesCmeiamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesCmeiamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f44e0d8c1e19de0f413ec011a06c32f7aba360227bd8452b638063ae6409d5)
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
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f32063e05e74ef8a9aef778e095733e52c3f2252f2d8b8a41bd38c51fe35ced)
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
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesCpuAlarmLow",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesCpuAlarmLow:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmLow
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7600191652a99ba4df1155f89b359243bdb58fc5005254651730322987f310bc)
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
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmLow#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmLow#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesCpuAlarmLow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3012dd60a3ec1c76c403fa3492238bc0bf31cf6692712e4da327219070ad984)
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
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eff52fd71a8b28b87b8bf894011ab2258455c013704f67274f9d2e8ddec294e)
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
        :schema: CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesElbSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesElbSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesElbSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__070d4e1c0c01a5b0711298a6de1896f8a309c355af035c78079d5bdda5e6aedb)
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
        :schema: CfnCloudGuardQsModulePropsResourcesElbSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesElbSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesElbSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a698f7b5dadbc041e09b3526ed0953b29eaaa14c8f758cfdd932382200c26546)
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
        :schema: CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesExternalLbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesExternalLbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesExternalLbListener
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68a39e219cc09b545d63d6ed5a05d836fafa4011b77b9395ac262dbc10aeb407)
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
        :schema: CfnCloudGuardQsModulePropsResourcesExternalLbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesExternalLbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesExternalLbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__788dea64dda779c74557e7e55b334a830d3eaf50e68aa382cb14e6ecf2630015)
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
        :schema: CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34fe958e207ab6dd29bf802846cbafc4215a4bd66658270725089c0f7165aac6)
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
        :schema: CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesGatewayGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesGatewayGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesGatewayGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04939f7ee857468967b7924e697aa719a6da442b59122131abf0187665339d28)
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
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesGatewayGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52a5395c549b732e5770d80c97e7641f35ad853d00806a9ae2563c484879902)
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
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b4152a95cf18a5588a44e141f5ad589783777fadf654959b8116264084b17e)
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
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f9254d308f2408ffbf8a07558a5f7cb443e1add9cebdf25247252a6ec8fc711)
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
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInstanceProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__838ccb47cfe1cd39ec19669d3f2192bd076a932e4b0c484034a6fff004bfd176)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__130dff780f6a201495a1646017d379863169bf022dbc8b08f1c112e50d006209)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInternalLbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInternalLbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInternalLbListener
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8924401804fedddda362ee7de4529b34eba0918767fe8aac1bdb1c154beb23a9)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInternalLbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInternalLbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInternalLbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ad310b70b15ec6b487bcc7e31d30eb483ad1fdfbe2b2c90228797b1ce46264)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a432ca1a873dc3fec8235d15c29af3b4facae81235f93fcb8a0405bbca34b74)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd7249b564a99d2fb6934a58aa47ef60c59850550586d833e85176a8c45d782)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesInternetGateway",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesInternetGateway:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesInternetGateway
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4538df9688112e681695648b3ba750d0cefd1711e070263ceeef72b8007cfeb0)
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
        :schema: CfnCloudGuardQsModulePropsResourcesInternetGateway#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesInternetGateway#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesManagementInstance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesManagementInstance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesManagementInstance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa2ed8984303b057505941d3e0026f80be31436308495883401be701955beb50)
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
        :schema: CfnCloudGuardQsModulePropsResourcesManagementInstance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesManagementInstance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesManagementInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesManagementReadyCondition",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesManagementReadyCondition:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesManagementReadyCondition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__976b2573d0366907ff191d9a41650073913cafc0ce44e9d05495fd829c8e1a3a)
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
        :schema: CfnCloudGuardQsModulePropsResourcesManagementReadyCondition#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesManagementReadyCondition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesManagementReadyCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesManagementReadyHandle",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesManagementReadyHandle:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesManagementReadyHandle
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__737affac4b02860ef7c9e25f3d21bd8dbb241a526ef8185bb008f33c44cbacc0)
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
        :schema: CfnCloudGuardQsModulePropsResourcesManagementReadyHandle#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesManagementReadyHandle#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesManagementReadyHandle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470bb7152e4523b85b73a8a5642d537d269ae64def95bf6fad757ad67e951717)
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
        :schema: CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesNotificationTopic",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesNotificationTopic:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesNotificationTopic
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e1822e9e3924b37b558d81af2178a504272e5d33c89db888640954c7756bb6)
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
        :schema: CfnCloudGuardQsModulePropsResourcesNotificationTopic#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesNotificationTopic#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesNotificationTopic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b569a6dc9a36c7625167390f8d1bd04b234fd8c9ece203089505ccc02a674ee7)
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
        :schema: CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4338d55cf9935c7a5bf8d1cabdca729ec8e605461f14723de2713621c260ae1)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPrivateSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPrivateSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093524ec362959fb433a777e936d255413aad517e08321ebbc34264d8c333e03)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPrivateSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPrivateSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPrivateSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f56e99082828c2d045df89daf7db2ff8baada208bf9fc97e7053263bfa218f)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPrivateSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPrivateSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPrivateSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f9a23b2c6388b03765374fb7270d13fc9b74403907f7d2c5566b674b6c9406)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPrivateSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPrivateSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPrivateSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0d33a3e6e916ed37d3353f3a9b295d59f95237dad96856343061b20c2db1189)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPrivateSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPrivateSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicAddress",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicAddress:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicAddress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1294e19ffbc86417fe51d10164e4661b824d58a890788e8961597de219284c3)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicAddress#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicAddress#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e292658182f08589e9a6e11a5b7becef42f0db34e006944eaa846144f9e396)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48bcdb6cd3cdcee755bec8831b380fe2f8adb0e61c5ad193b304b256a2b4879e)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a9376e9f479c3c462f309ee0622f863d8c83ec0941b77eb32b75df4417ffdc)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96951750163c3a4ec6e94b2e23a7c4e9a395baf0e3225f817250daaeac6c0034)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__657d65922053f1e1611ada3c97f40106ee7305acb4fd69ab9b8cd96d4e6a7612)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4095284260fbc080fd32b345d63b5c8ee785db1812cb2f7cc4494b83245ca7de)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60659253125bbb5976e561d26a5e845b94e0f1b39a7cdb58ff1e449f6def3bb0)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9436aac2779f60b1c8ceed95bc52cdc7bc8192044a45aee564c5831b3598a63a)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d1505d5ae581c5f61319bb02dcd991c61c20cfad6a1a742a5864e142e36f07)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9d626cc3bd5258aee23716721b562142972a3e1fe14c544fbb8a7295144a4a6)
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
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesScaleDownPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesScaleDownPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesScaleDownPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b68597ff94a86bf4c25302ac1ca06ff4918140d0bafe6613632f08be1eb548)
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
        :schema: CfnCloudGuardQsModulePropsResourcesScaleDownPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesScaleDownPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesScaleDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesScaleUpPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesScaleUpPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesScaleUpPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d516a4bcdf02d808648fd566920cb4c65d866b1545cb779ccaaa7b5d7902c74)
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
        :schema: CfnCloudGuardQsModulePropsResourcesScaleUpPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesScaleUpPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesScaleUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesServersGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesServersGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesServersGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__858b64453a89f3a341dd5afdc1c4c6f0bf0e37b99e713d99207b2942547bde74)
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
        :schema: CfnCloudGuardQsModulePropsResourcesServersGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesServersGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesServersGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f48e598dec19447b6d6403cc7ebe1afce8b11322fab7cedff685969dc555e4)
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
        :schema: CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesServersSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesServersSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesServersSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__304259aac70cb333123dedd296a87f393d510ca31c7d39fbc55cd0a277a98dc0)
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
        :schema: CfnCloudGuardQsModulePropsResourcesServersSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesServersSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesServersSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesTgwSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesTgwSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29895c2f3b6cfc899e3b54e0939b8b4bccb3dade622ff31e8bafa663601933aa)
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
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesTgwSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesTgwSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesTgwSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc009ed6a72279c6977d6665f47e9ba28b6444a427d25d5cf5f3945e4adae5c3)
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
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesTgwSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesTgwSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesTgwSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a10326df712afa822ea165e2c243218bb55e8ceec691f8d9993f69c106310bc)
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
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesTgwSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesTgwSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesTgwSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ca305c101cf196920644bf60907377a510c814624238daa20473e97718e902)
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
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesTgwSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesTgwSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesVpc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesVpc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesVpc
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdccbc35a1dfaea982289ba356cf5d0503f830471a2daf30277f44c2910cccb3)
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
        :schema: CfnCloudGuardQsModulePropsResourcesVpc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesVpc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68df5bf6f9ef53e4a0fe071639adf155ef3e3a191c3284e261bbc828931369f8)
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
        :schema: CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudGuardQsModule",
    "CfnCloudGuardQsModuleProps",
    "CfnCloudGuardQsModulePropsParameters",
    "CfnCloudGuardQsModulePropsParametersAdminCidr",
    "CfnCloudGuardQsModulePropsParametersAdminEmail",
    "CfnCloudGuardQsModulePropsParametersAlbProtocol",
    "CfnCloudGuardQsModulePropsParametersAllocatePublicAddress",
    "CfnCloudGuardQsModulePropsParametersAllowUploadDownload",
    "CfnCloudGuardQsModulePropsParametersAvailabilityZones",
    "CfnCloudGuardQsModulePropsParametersCertificate",
    "CfnCloudGuardQsModulePropsParametersCloudWatch",
    "CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress",
    "CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets",
    "CfnCloudGuardQsModulePropsParametersCreateTgwSubnets",
    "CfnCloudGuardQsModulePropsParametersElbClients",
    "CfnCloudGuardQsModulePropsParametersElbPort",
    "CfnCloudGuardQsModulePropsParametersElbType",
    "CfnCloudGuardQsModulePropsParametersEnableInstanceConnect",
    "CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption",
    "CfnCloudGuardQsModulePropsParametersGatewayInstanceType",
    "CfnCloudGuardQsModulePropsParametersGatewayManagement",
    "CfnCloudGuardQsModulePropsParametersGatewayPasswordHash",
    "CfnCloudGuardQsModulePropsParametersGatewaySicKey",
    "CfnCloudGuardQsModulePropsParametersGatewayVersion",
    "CfnCloudGuardQsModulePropsParametersGatewaysAddresses",
    "CfnCloudGuardQsModulePropsParametersGatewaysBlades",
    "CfnCloudGuardQsModulePropsParametersGatewaysMaxSize",
    "CfnCloudGuardQsModulePropsParametersGatewaysMinSize",
    "CfnCloudGuardQsModulePropsParametersGatewaysPolicy",
    "CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups",
    "CfnCloudGuardQsModulePropsParametersKeyName",
    "CfnCloudGuardQsModulePropsParametersLoadBalancersType",
    "CfnCloudGuardQsModulePropsParametersManagementDeploy",
    "CfnCloudGuardQsModulePropsParametersManagementHostname",
    "CfnCloudGuardQsModulePropsParametersManagementInstanceType",
    "CfnCloudGuardQsModulePropsParametersManagementPasswordHash",
    "CfnCloudGuardQsModulePropsParametersManagementPermissions",
    "CfnCloudGuardQsModulePropsParametersManagementPredefinedRole",
    "CfnCloudGuardQsModulePropsParametersManagementSicKey",
    "CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize",
    "CfnCloudGuardQsModulePropsParametersManagementVersion",
    "CfnCloudGuardQsModulePropsParametersNlbProtocol",
    "CfnCloudGuardQsModulePropsParametersNtpPrimary",
    "CfnCloudGuardQsModulePropsParametersNtpSecondary",
    "CfnCloudGuardQsModulePropsParametersNumberOfAZs",
    "CfnCloudGuardQsModulePropsParametersPermissions",
    "CfnCloudGuardQsModulePropsParametersPrimaryManagement",
    "CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr",
    "CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr",
    "CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr",
    "CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr",
    "CfnCloudGuardQsModulePropsParametersProvisionTag",
    "CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr",
    "CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr",
    "CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr",
    "CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr",
    "CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize",
    "CfnCloudGuardQsModulePropsParametersServerAmi",
    "CfnCloudGuardQsModulePropsParametersServerInstanceType",
    "CfnCloudGuardQsModulePropsParametersServerName",
    "CfnCloudGuardQsModulePropsParametersServersDeploy",
    "CfnCloudGuardQsModulePropsParametersServersMaxSize",
    "CfnCloudGuardQsModulePropsParametersServersMinSize",
    "CfnCloudGuardQsModulePropsParametersServersTargetGroups",
    "CfnCloudGuardQsModulePropsParametersServicePort",
    "CfnCloudGuardQsModulePropsParametersShellManagementStack",
    "CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack",
    "CfnCloudGuardQsModulePropsParametersSourceSecurityGroup",
    "CfnCloudGuardQsModulePropsParametersStsRoles",
    "CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr",
    "CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr",
    "CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr",
    "CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr",
    "CfnCloudGuardQsModulePropsParametersTrustedAccount",
    "CfnCloudGuardQsModulePropsParametersVpccidr",
    "CfnCloudGuardQsModulePropsResources",
    "CfnCloudGuardQsModulePropsResourcesAddressAssoc",
    "CfnCloudGuardQsModulePropsResourcesChkpGatewayRole",
    "CfnCloudGuardQsModulePropsResourcesCmeiamRole",
    "CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh",
    "CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack",
    "CfnCloudGuardQsModulePropsResourcesCpuAlarmLow",
    "CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack",
    "CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer",
    "CfnCloudGuardQsModulePropsResourcesElbSecurityGroup",
    "CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup",
    "CfnCloudGuardQsModulePropsResourcesExternalLbListener",
    "CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup",
    "CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer",
    "CfnCloudGuardQsModulePropsResourcesGatewayGroup",
    "CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig",
    "CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy",
    "CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy",
    "CfnCloudGuardQsModulePropsResourcesInstanceProfile",
    "CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack",
    "CfnCloudGuardQsModulePropsResourcesInternalLbListener",
    "CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup",
    "CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer",
    "CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup",
    "CfnCloudGuardQsModulePropsResourcesInternetGateway",
    "CfnCloudGuardQsModulePropsResourcesManagementInstance",
    "CfnCloudGuardQsModulePropsResourcesManagementReadyCondition",
    "CfnCloudGuardQsModulePropsResourcesManagementReadyHandle",
    "CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup",
    "CfnCloudGuardQsModulePropsResourcesNotificationTopic",
    "CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack",
    "CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup",
    "CfnCloudGuardQsModulePropsResourcesPrivateSubnet1",
    "CfnCloudGuardQsModulePropsResourcesPrivateSubnet2",
    "CfnCloudGuardQsModulePropsResourcesPrivateSubnet3",
    "CfnCloudGuardQsModulePropsResourcesPrivateSubnet4",
    "CfnCloudGuardQsModulePropsResourcesPublicAddress",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet1",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet2",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet3",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet4",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute",
    "CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable",
    "CfnCloudGuardQsModulePropsResourcesScaleDownPolicy",
    "CfnCloudGuardQsModulePropsResourcesScaleUpPolicy",
    "CfnCloudGuardQsModulePropsResourcesServersGroup",
    "CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration",
    "CfnCloudGuardQsModulePropsResourcesServersSecurityGroup",
    "CfnCloudGuardQsModulePropsResourcesTgwSubnet1",
    "CfnCloudGuardQsModulePropsResourcesTgwSubnet2",
    "CfnCloudGuardQsModulePropsResourcesTgwSubnet3",
    "CfnCloudGuardQsModulePropsResourcesTgwSubnet4",
    "CfnCloudGuardQsModulePropsResourcesVpc",
    "CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment",
]

publication.publish()

def _typecheckingstub__fff8e443652c7933b6b9f6847fe30fc28ad6cc4d8ac8bf4a83150f9af8a00289(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599eea0487839a1d4761f141456cef9fc7b05751a268093d953445b6ed361137(
    *,
    parameters: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4328a53d809df0331a47e7d45f875ff1f877db04d78578ff28b70dddf67c9c4a(
    *,
    admin_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersAdminCidr, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_email: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersAdminEmail, typing.Dict[builtins.str, typing.Any]]] = None,
    alb_protocol: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersAlbProtocol, typing.Dict[builtins.str, typing.Any]]] = None,
    allocate_public_address: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersAllocatePublicAddress, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_upload_download: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersAllowUploadDownload, typing.Dict[builtins.str, typing.Any]]] = None,
    availability_zones: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersAvailabilityZones, typing.Dict[builtins.str, typing.Any]]] = None,
    certificate: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersCertificate, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_watch: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersCloudWatch, typing.Dict[builtins.str, typing.Any]]] = None,
    control_gateway_over_private_or_public_address: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersControlGatewayOverPrivateOrPublicAddress, typing.Dict[builtins.str, typing.Any]]] = None,
    create_private_subnets: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersCreatePrivateSubnets, typing.Dict[builtins.str, typing.Any]]] = None,
    create_tgw_subnets: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersCreateTgwSubnets, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_clients: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersElbClients, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_port: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersElbPort, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_type: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersElbType, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_instance_connect: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersEnableInstanceConnect, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_volume_encryption: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersEnableVolumeEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_instance_type: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewayInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_management: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewayManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_password_hash: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewayPasswordHash, typing.Dict[builtins.str, typing.Any]]] = None,
    gateways_addresses: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaysAddresses, typing.Dict[builtins.str, typing.Any]]] = None,
    gateways_blades: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaysBlades, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_sic_key: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaySicKey, typing.Dict[builtins.str, typing.Any]]] = None,
    gateways_max_size: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaysMaxSize, typing.Dict[builtins.str, typing.Any]]] = None,
    gateways_min_size: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaysMinSize, typing.Dict[builtins.str, typing.Any]]] = None,
    gateways_policy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaysPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    gateways_target_groups: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewaysTargetGroups, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_version: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersGatewayVersion, typing.Dict[builtins.str, typing.Any]]] = None,
    key_name: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersKeyName, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancers_type: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersLoadBalancersType, typing.Dict[builtins.str, typing.Any]]] = None,
    management_deploy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementDeploy, typing.Dict[builtins.str, typing.Any]]] = None,
    management_hostname: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementHostname, typing.Dict[builtins.str, typing.Any]]] = None,
    management_instance_type: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    management_password_hash: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementPasswordHash, typing.Dict[builtins.str, typing.Any]]] = None,
    management_permissions: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementPermissions, typing.Dict[builtins.str, typing.Any]]] = None,
    management_predefined_role: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementPredefinedRole, typing.Dict[builtins.str, typing.Any]]] = None,
    management_sic_key: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementSicKey, typing.Dict[builtins.str, typing.Any]]] = None,
    management_stack_volume_size: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementStackVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    management_version: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersManagementVersion, typing.Dict[builtins.str, typing.Any]]] = None,
    nlb_protocol: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersNlbProtocol, typing.Dict[builtins.str, typing.Any]]] = None,
    ntp_primary: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersNtpPrimary, typing.Dict[builtins.str, typing.Any]]] = None,
    ntp_secondary: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersNtpSecondary, typing.Dict[builtins.str, typing.Any]]] = None,
    number_of_a_zs: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersNumberOfAZs, typing.Dict[builtins.str, typing.Any]]] = None,
    permissions: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPermissions, typing.Dict[builtins.str, typing.Any]]] = None,
    primary_management: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPrimaryManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPrivateSubnet1Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPrivateSubnet2Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPrivateSubnet3Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPrivateSubnet4Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    provision_tag: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersProvisionTag, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPublicSubnet1Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPublicSubnet2Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet3_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPublicSubnet3Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet4_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersPublicSubnet4Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    security_gateway_volume_size: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersSecurityGatewayVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    server_ami: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServerAmi, typing.Dict[builtins.str, typing.Any]]] = None,
    server_instance_type: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServerInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    server_name: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServerName, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_deploy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServersDeploy, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_max_size: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServersMaxSize, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_min_size: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServersMinSize, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_target_groups: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServersTargetGroups, typing.Dict[builtins.str, typing.Any]]] = None,
    service_port: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersServicePort, typing.Dict[builtins.str, typing.Any]]] = None,
    shell_management_stack: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersShellManagementStack, typing.Dict[builtins.str, typing.Any]]] = None,
    shell_security_gateway_stack: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersShellSecurityGatewayStack, typing.Dict[builtins.str, typing.Any]]] = None,
    source_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersSourceSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    sts_roles: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersStsRoles, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet1_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersTgwSubnet1Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet2_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersTgwSubnet2Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet3_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersTgwSubnet3Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet4_cidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersTgwSubnet4Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    trusted_account: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersTrustedAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    vpccidr: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsParametersVpccidr, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb7db9b3fa37e254ff81e31253caee6ba2db66a9b2ca252e8439bd873b165b0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9971e1bacc76211dc6fe1d9cb133d90c2fb0a8dab87b8b7301b5d1b456717e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7da7c9f79cf613725f598459cf114b398af73597f454d3fe4c387beb279f34a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca370f55f9b60908c9d43b182eea4e0ed983695bc50066340484e0430517a7b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fe51216a493fd425344504f49e8eff6d13f17cd8bffb56bcab57c15cb34ad7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955f9e7b492417d86422274972d39c846b6477bc82317015d4b1ec627c912ae0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce36a4886065f86921b904f2570a23d249df67c619f78cfe6ec3ca9efe829a00(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b26af9b98285712eee5c438b33b6f6eeb80a741c606e1862f28ffbba4cb5b07a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ac0e193822bc243f0a78999075165c89dca3cc2982534fc85519e1f22de36e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c33abb2b26622038bcf65ac573a9f33cbb04bc725a156f048bb5ed266cd78a2c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16654ffe240541f090f56fa68b9c3d37cb39195a833f5d99735ea0306b4639fb(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5990dd2c27957b9b8de505411b5699185c7a630edb58baf2145392f4ff2729aa(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf2835392ad1c3181ab5a13a4a9746c7488cde8745ca0f8e7eaa78fdf6d278f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8b3a27c3dbddbc16b321f94f9578a2d86d215ee6ccd8f14ce019523e249801c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232e57cc80211385d6a639061ad22153d24ff4ad78d8a929b80df2ad2273ceb3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d05607e4e68034f0935231a8bb50f36a4faceee9e0b177951e8806261c80cd6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7196bc9d7b9d34fc10aebe0728e101b384171c35a3a08e9cb71e8725c886b28(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6cca0be6211d5b73dfb3b21d4494db437678cbf12a0f3724203ed8e92be1c9f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43706457692e4b1e97e6051b3beb05d21bd3add49fb183736f31f57f7d65b648(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a15d7058f15881b5d42cdc436d6f182ca71d18ea15952dff80b2205aed5d3f89(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac830e922f6df56a1ff671f19948c443fccfe044abfdc08ec0fff861fd2e4c2(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c7156c890f157d1dfcd16b5c9d76d53fb15fdcac62ad1357f194adc8fd2b4e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b738ae064c628d7aa26000521c0ea96e66043577b80c4f3d7a1305a60da56609(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ce16da5f41bddd19f747435d7e8d27826cd792108e401f6e871190283ce77a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798e1ced99ede998b8eb24cbd83da0ed642d547e376813dd854603438dc00151(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53dfa8a9bc23f31e938682f11ad238b7fca940e19b0ed0b5447aa6a06a2f957c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d068a2ac936586044d1c6183b064ceb5ff3f9d42f713471d26dacaca046998f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589ef24df1010c37a0b9b9e0d38e60d666b6f394447f0cce7e5fb4c7dcffc22a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d3e6157e7d263193525fcaa60d8c70ef1c78fd059ea19118a5f9c4a98aaf117(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__371e7d2fcb02d88f8e287e31090e91d9879dc8b22e17b916f5f89c30a2f032c0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e954e6587d2ef206390d38c5d823620dd90e8f6e08db6e23c740a777edd26dc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac0cca8396d332e8c716c4f2b4dda922c7b6136a387609f3a8127010b62f17f2(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bab924efe4ec2a6f40909cc79b745b2108942e840199474a8e3c17406dfaf03(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992d85bf47e48f8bd1145209bdc30d23b8777f0203af71db046d33294cce054d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8912689afe8756723f1fa4c4ade6302ac38c1bb996c20ed08286c4f1b11286ae(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2bea786d1c72a87724b54d5b53c081e67193fdd739f2284ad4f4991132abca(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba5871ed379783bc84bcbfde956ea42c33bc94ec84953a6e427cd818e55655b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba6d0f01c650ecf0e362512a2653f9eafec713d0afcc2510950983175cfa726f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9c6efaaa36b479f698f581a73747b9df13114d9181c73223cf82e2f57196b7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cd3835895cecde5a38417f7a8bfbab8b0d4c1f5b692030d9e17747d3f8bbd3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24dfd7f25930cb8021c923aa9f497d82b08f082b0eb0930d4ce4c711b0ccc7d9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__764a7b5c4cf23095a088d04f4205b2e5636bd140af8e116e792706b102fd1d8b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428825e5971d9a728079b37ad0a9a0d63f253182153a1a0254374c205f995baf(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5cd014614433c7b5cfaba3f72fb1e09aaf95239e78ea55c6fbabeb41bdcce9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b15f560e53f6792179ff6b3797c01bed979559b4d5f05e3a1a1357ca7124ca(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4299402fc52a56427f18c9928e554a1c2bc69f6683b102ddf2b2aa2602759d9e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75fe73e699be1ab381507982fb1957c9095cf999fed90b921f08db657916d754(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96bce719059e14ff3a26def2a109ddc090497fd358e76e4c5fca4e5dda2e420(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a188641f5b9b74324d74e164029a36d236996843bafca20e8e351d9ca4233313(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2c240d4625f31af97833c35871088f447471baeb5da0824e8ab0e3475c7b08e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f292bcfb0a9a43f817dcac91bae8df0a5b5a4936d6491bc1b00488992910f8f0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b6df933b1dd80e681bc6d7d337171da44fb8ebab76eb799c1edf343bc301a13(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3aeb7a6464009648a96f2d7cc39b96b33a541fc91d50a0289152ae24654d27(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__919a0214ed436b2313cbf25b472ebdbba59dd19d7ea679020721887b7c6e9694(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fcd4edbe3ce10480789b5b1a5fb528e728860f4bf9af8584fba4a24705aeb60(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606083edcf98e0af0b6a2b928492d34257939a488e9cc9ba9a045ed8c1df34f1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910117380e221fd385a335199a65a25bb94f4f0584f6e0fa8fae91d30dfec6e9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0e0a937f6dc8d3c992750079294e147e77c0d9b91a165258d550c0e77957e1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136d9194374305cc93959e80bdb588b3479c6f46448dd4ef260b08941c2cab68(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9db38b1ae200859ac23a25dfc52a19007243906a10b755595f28c46de658c1a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c2c962741c7f0ee93ff93d8a602078bc5e3c2b12bcf13900f482da9586109a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923183299703584f359587bc024687a77cdce8ee9e481b99f9637c62e9264674(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4344843f4e5ab56fbcd4fdf3338de39e174ad7c6012515def9ec33bad9ba0a52(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5402e79db2083ed4c3bfd7c63a957e94c140343357cb7a8963de5e426be3f1c4(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bd54a85105e991d846d75c9b5928b612f43322f49d8054271302df92dc98c0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67422c6845f595119262d78a12a863f79b7c73cd4ce58fb9503f396c960d9c36(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95fc8dd08d29177b2c27c6475963cba197a994ebc454935cdfa2051bd2fd4a45(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96edeb1b7b98c137c36ee3e4a938625cad569fcc6774cc85f5ac23c2d7512b55(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9414f5166ddc59b8a0073803e22b0f72f04fe36bd5d9805a9bf9fdfb3ebaa274(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158289b86782a76f4dd8b4dd13ac4dc368a69a93c34b7c23641bee17ea88b35c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261183f64f5963780cf487a2a948949a21e29b119b748c02d7b6302e314edfac(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b1a13ab59c6e031a966f4764621ebabd74f417dc216b4dd5bdc591c11bdfff(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee95227a37dee0c2c796fd9bf5426b567fb13eefe7c40e09de4c434331a27b6c(
    *,
    address_assoc: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesAddressAssoc, typing.Dict[builtins.str, typing.Any]]] = None,
    chkp_gateway_role: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesChkpGatewayRole, typing.Dict[builtins.str, typing.Any]]] = None,
    cmeiam_role: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesCmeiamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_alarm_high: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesCpuAlarmHigh, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_alarm_high_security_gateway_stack: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesCpuAlarmHighSecurityGatewayStack, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_alarm_low: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesCpuAlarmLow, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_alarm_low_security_gateway_stack: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesCpuAlarmLowSecurityGatewayStack, typing.Dict[builtins.str, typing.Any]]] = None,
    elastic_load_balancer: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesElasticLoadBalancer, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesElbSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    external_alb_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesExternalAlbSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    external_lb_listener: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesExternalLbListener, typing.Dict[builtins.str, typing.Any]]] = None,
    external_lb_target_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesExternalLbTargetGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    external_load_balancer: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesExternalLoadBalancer, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesGatewayGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_launch_config: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesGatewayLaunchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_scale_down_policy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesGatewayScaleDownPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    gateway_scale_up_policy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesGatewayScaleUpPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_profile: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInstanceProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_profile_security_gateway_stack: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInstanceProfileSecurityGatewayStack, typing.Dict[builtins.str, typing.Any]]] = None,
    internal_lb_listener: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInternalLbListener, typing.Dict[builtins.str, typing.Any]]] = None,
    internal_lb_target_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInternalLbTargetGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    internal_load_balancer: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInternalLoadBalancer, typing.Dict[builtins.str, typing.Any]]] = None,
    internal_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInternalSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    internet_gateway: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesInternetGateway, typing.Dict[builtins.str, typing.Any]]] = None,
    management_instance: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesManagementInstance, typing.Dict[builtins.str, typing.Any]]] = None,
    management_ready_condition: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesManagementReadyCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    management_ready_handle: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesManagementReadyHandle, typing.Dict[builtins.str, typing.Any]]] = None,
    management_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesManagementSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_topic: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesNotificationTopic, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_topic_security_gateway_stack: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesNotificationTopicSecurityGatewayStack, typing.Dict[builtins.str, typing.Any]]] = None,
    permissive_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPermissiveSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPrivateSubnet1, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPrivateSubnet2, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPrivateSubnet3, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPrivateSubnet4, typing.Dict[builtins.str, typing.Any]]] = None,
    public_address: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicAddress, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet1, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_route_table_association: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet1RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet2, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_route_table_association: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet2RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet3: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet3, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet3_route_table_association: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet3RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet4: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet4, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet4_route_table_association: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnet4RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_route: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnetRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_route_table: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesPublicSubnetRouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_down_policy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesScaleDownPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_up_policy: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesScaleUpPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesServersGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_launch_configuration: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesServersLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    servers_security_group: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesServersSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet1: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesTgwSubnet1, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet2: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesTgwSubnet2, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet3: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesTgwSubnet3, typing.Dict[builtins.str, typing.Any]]] = None,
    tgw_subnet4: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesTgwSubnet4, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesVpc, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_gateway_attachment: typing.Optional[typing.Union[CfnCloudGuardQsModulePropsResourcesVpcGatewayAttachment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e46d231f73c0ef0b9cb6a3faa764310681c149fee8bb5c9432d267008fb9b3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b053fa217300cc156bf3f92267f92afcda8f6122d852070e266936bf1bd017(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4cdd701e507d71ec1b958142eba98e1639a8c2c557b96c087addea3b47c349f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f44e0d8c1e19de0f413ec011a06c32f7aba360227bd8452b638063ae6409d5(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f32063e05e74ef8a9aef778e095733e52c3f2252f2d8b8a41bd38c51fe35ced(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7600191652a99ba4df1155f89b359243bdb58fc5005254651730322987f310bc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3012dd60a3ec1c76c403fa3492238bc0bf31cf6692712e4da327219070ad984(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eff52fd71a8b28b87b8bf894011ab2258455c013704f67274f9d2e8ddec294e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__070d4e1c0c01a5b0711298a6de1896f8a309c355af035c78079d5bdda5e6aedb(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a698f7b5dadbc041e09b3526ed0953b29eaaa14c8f758cfdd932382200c26546(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68a39e219cc09b545d63d6ed5a05d836fafa4011b77b9395ac262dbc10aeb407(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__788dea64dda779c74557e7e55b334a830d3eaf50e68aa382cb14e6ecf2630015(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34fe958e207ab6dd29bf802846cbafc4215a4bd66658270725089c0f7165aac6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04939f7ee857468967b7924e697aa719a6da442b59122131abf0187665339d28(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52a5395c549b732e5770d80c97e7641f35ad853d00806a9ae2563c484879902(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b4152a95cf18a5588a44e141f5ad589783777fadf654959b8116264084b17e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9254d308f2408ffbf8a07558a5f7cb443e1add9cebdf25247252a6ec8fc711(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__838ccb47cfe1cd39ec19669d3f2192bd076a932e4b0c484034a6fff004bfd176(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__130dff780f6a201495a1646017d379863169bf022dbc8b08f1c112e50d006209(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8924401804fedddda362ee7de4529b34eba0918767fe8aac1bdb1c154beb23a9(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ad310b70b15ec6b487bcc7e31d30eb483ad1fdfbe2b2c90228797b1ce46264(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a432ca1a873dc3fec8235d15c29af3b4facae81235f93fcb8a0405bbca34b74(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd7249b564a99d2fb6934a58aa47ef60c59850550586d833e85176a8c45d782(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4538df9688112e681695648b3ba750d0cefd1711e070263ceeef72b8007cfeb0(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2ed8984303b057505941d3e0026f80be31436308495883401be701955beb50(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__976b2573d0366907ff191d9a41650073913cafc0ce44e9d05495fd829c8e1a3a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__737affac4b02860ef7c9e25f3d21bd8dbb241a526ef8185bb008f33c44cbacc0(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470bb7152e4523b85b73a8a5642d537d269ae64def95bf6fad757ad67e951717(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e1822e9e3924b37b558d81af2178a504272e5d33c89db888640954c7756bb6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b569a6dc9a36c7625167390f8d1bd04b234fd8c9ece203089505ccc02a674ee7(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4338d55cf9935c7a5bf8d1cabdca729ec8e605461f14723de2713621c260ae1(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093524ec362959fb433a777e936d255413aad517e08321ebbc34264d8c333e03(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f56e99082828c2d045df89daf7db2ff8baada208bf9fc97e7053263bfa218f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f9a23b2c6388b03765374fb7270d13fc9b74403907f7d2c5566b674b6c9406(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0d33a3e6e916ed37d3353f3a9b295d59f95237dad96856343061b20c2db1189(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1294e19ffbc86417fe51d10164e4661b824d58a890788e8961597de219284c3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e292658182f08589e9a6e11a5b7becef42f0db34e006944eaa846144f9e396(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48bcdb6cd3cdcee755bec8831b380fe2f8adb0e61c5ad193b304b256a2b4879e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a9376e9f479c3c462f309ee0622f863d8c83ec0941b77eb32b75df4417ffdc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96951750163c3a4ec6e94b2e23a7c4e9a395baf0e3225f817250daaeac6c0034(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__657d65922053f1e1611ada3c97f40106ee7305acb4fd69ab9b8cd96d4e6a7612(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4095284260fbc080fd32b345d63b5c8ee785db1812cb2f7cc4494b83245ca7de(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60659253125bbb5976e561d26a5e845b94e0f1b39a7cdb58ff1e449f6def3bb0(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9436aac2779f60b1c8ceed95bc52cdc7bc8192044a45aee564c5831b3598a63a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d1505d5ae581c5f61319bb02dcd991c61c20cfad6a1a742a5864e142e36f07(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9d626cc3bd5258aee23716721b562142972a3e1fe14c544fbb8a7295144a4a6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b68597ff94a86bf4c25302ac1ca06ff4918140d0bafe6613632f08be1eb548(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d516a4bcdf02d808648fd566920cb4c65d866b1545cb779ccaaa7b5d7902c74(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858b64453a89f3a341dd5afdc1c4c6f0bf0e37b99e713d99207b2942547bde74(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f48e598dec19447b6d6403cc7ebe1afce8b11322fab7cedff685969dc555e4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__304259aac70cb333123dedd296a87f393d510ca31c7d39fbc55cd0a277a98dc0(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29895c2f3b6cfc899e3b54e0939b8b4bccb3dade622ff31e8bafa663601933aa(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc009ed6a72279c6977d6665f47e9ba28b6444a427d25d5cf5f3945e4adae5c3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a10326df712afa822ea165e2c243218bb55e8ceec691f8d9993f69c106310bc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ca305c101cf196920644bf60907377a510c814624238daa20473e97718e902(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdccbc35a1dfaea982289ba356cf5d0503f830471a2daf30277f44c2910cccb3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68df5bf6f9ef53e4a0fe071639adf155ef3e3a191c3284e261bbc828931369f8(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

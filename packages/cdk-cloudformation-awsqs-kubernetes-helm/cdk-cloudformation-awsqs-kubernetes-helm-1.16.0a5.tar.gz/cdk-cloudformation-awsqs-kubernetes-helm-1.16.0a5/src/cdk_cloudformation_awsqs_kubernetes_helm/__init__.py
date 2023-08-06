'''
# awsqs-kubernetes-helm

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::Kubernetes::Helm` v1.16.0.

## Description

A resource provider for managing helm. Version: 1.2.1

## References

* [Documentation](https://github.com/aws-quickstart/quickstart-helm-resource-provider/blob/main/README.md)
* [Source](https://github.com/aws-quickstart/quickstart-helm-resource-provider.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::Kubernetes::Helm \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-Kubernetes-Helm \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::Kubernetes::Helm`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-kubernetes-helm+v1.16.0).
* Issues related to `AWSQS::Kubernetes::Helm` should be reported to the [publisher](https://github.com/aws-quickstart/quickstart-helm-resource-provider/blob/main/README.md).

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


class CfnHelm(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-helm.CfnHelm",
):
    '''A CloudFormation ``AWSQS::Kubernetes::Helm``.

    :cloudformationResource: AWSQS::Kubernetes::Helm
    :link: https://github.com/aws-quickstart/quickstart-helm-resource-provider.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        chart: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        kube_config: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        repository_options: typing.Optional[typing.Union["CfnHelmPropsRepositoryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Any = None,
        role_arn: typing.Optional[builtins.str] = None,
        time_out: typing.Optional[jsii.Number] = None,
        value_override_url: typing.Optional[builtins.str] = None,
        values: typing.Any = None,
        value_yaml: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_configuration: typing.Optional[typing.Union["CfnHelmPropsVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``AWSQS::Kubernetes::Helm``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param chart: Chart name.
        :param cluster_id: EKS cluster name.
        :param kube_config: Secrets Manager ARN for kubeconfig file.
        :param name: Name for the helm release.
        :param namespace: Namespace to use with helm. Created if doesn't exist and default will be used if not provided
        :param repository: Repository url. Defaults to kubernetes-charts.storage.googleapis.com Default: kubernetes-charts.storage.googleapis.com
        :param repository_options: Extra options for repository.
        :param resources: Resources from the helm charts.
        :param role_arn: IAM to use with EKS cluster authentication, if not resource execution role will be used.
        :param time_out: Timeout for resource provider. Default 60 mins
        :param value_override_url: Custom Value Yaml file can optionally be specified.
        :param values: Custom Values can optionally be specified.
        :param value_yaml: String representation of a values.yaml file.
        :param version: Version can be specified, if not latest will be used.
        :param vpc_configuration: For network connectivity to Cluster inside VPC.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf7348506ac21f4b7ee9822b428a1c123a1c4e9c7ef1bc996e624979ab063137)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHelmProps(
            chart=chart,
            cluster_id=cluster_id,
            kube_config=kube_config,
            name=name,
            namespace=namespace,
            repository=repository,
            repository_options=repository_options,
            resources=resources,
            role_arn=role_arn,
            time_out=time_out,
            value_override_url=value_override_url,
            values=values,
            value_yaml=value_yaml,
            version=version,
            vpc_configuration=vpc_configuration,
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
        '''Attribute ``AWSQS::Kubernetes::Helm.ID``.

        :link: https://github.com/aws-quickstart/quickstart-helm-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnHelmProps":
        '''Resource props.'''
        return typing.cast("CfnHelmProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-helm.CfnHelmProps",
    jsii_struct_bases=[],
    name_mapping={
        "chart": "chart",
        "cluster_id": "clusterId",
        "kube_config": "kubeConfig",
        "name": "name",
        "namespace": "namespace",
        "repository": "repository",
        "repository_options": "repositoryOptions",
        "resources": "resources",
        "role_arn": "roleArn",
        "time_out": "timeOut",
        "value_override_url": "valueOverrideUrl",
        "values": "values",
        "value_yaml": "valueYaml",
        "version": "version",
        "vpc_configuration": "vpcConfiguration",
    },
)
class CfnHelmProps:
    def __init__(
        self,
        *,
        chart: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        kube_config: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        repository_options: typing.Optional[typing.Union["CfnHelmPropsRepositoryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Any = None,
        role_arn: typing.Optional[builtins.str] = None,
        time_out: typing.Optional[jsii.Number] = None,
        value_override_url: typing.Optional[builtins.str] = None,
        values: typing.Any = None,
        value_yaml: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_configuration: typing.Optional[typing.Union["CfnHelmPropsVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''A resource provider for managing helm.

        Version: 1.2.1

        :param chart: Chart name.
        :param cluster_id: EKS cluster name.
        :param kube_config: Secrets Manager ARN for kubeconfig file.
        :param name: Name for the helm release.
        :param namespace: Namespace to use with helm. Created if doesn't exist and default will be used if not provided
        :param repository: Repository url. Defaults to kubernetes-charts.storage.googleapis.com Default: kubernetes-charts.storage.googleapis.com
        :param repository_options: Extra options for repository.
        :param resources: Resources from the helm charts.
        :param role_arn: IAM to use with EKS cluster authentication, if not resource execution role will be used.
        :param time_out: Timeout for resource provider. Default 60 mins
        :param value_override_url: Custom Value Yaml file can optionally be specified.
        :param values: Custom Values can optionally be specified.
        :param value_yaml: String representation of a values.yaml file.
        :param version: Version can be specified, if not latest will be used.
        :param vpc_configuration: For network connectivity to Cluster inside VPC.

        :schema: CfnHelmProps
        '''
        if isinstance(repository_options, dict):
            repository_options = CfnHelmPropsRepositoryOptions(**repository_options)
        if isinstance(vpc_configuration, dict):
            vpc_configuration = CfnHelmPropsVpcConfiguration(**vpc_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf179732a60d53e9ee24cb1142d5a0ac10b7f9e06f176d49496877b17cfcac0)
            check_type(argname="argument chart", value=chart, expected_type=type_hints["chart"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument kube_config", value=kube_config, expected_type=type_hints["kube_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument repository_options", value=repository_options, expected_type=type_hints["repository_options"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument time_out", value=time_out, expected_type=type_hints["time_out"])
            check_type(argname="argument value_override_url", value=value_override_url, expected_type=type_hints["value_override_url"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument value_yaml", value=value_yaml, expected_type=type_hints["value_yaml"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "chart": chart,
        }
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if kube_config is not None:
            self._values["kube_config"] = kube_config
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if repository is not None:
            self._values["repository"] = repository
        if repository_options is not None:
            self._values["repository_options"] = repository_options
        if resources is not None:
            self._values["resources"] = resources
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if time_out is not None:
            self._values["time_out"] = time_out
        if value_override_url is not None:
            self._values["value_override_url"] = value_override_url
        if values is not None:
            self._values["values"] = values
        if value_yaml is not None:
            self._values["value_yaml"] = value_yaml
        if version is not None:
            self._values["version"] = version
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

    @builtins.property
    def chart(self) -> builtins.str:
        '''Chart name.

        :schema: CfnHelmProps#Chart
        '''
        result = self._values.get("chart")
        assert result is not None, "Required property 'chart' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''EKS cluster name.

        :schema: CfnHelmProps#ClusterID
        '''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kube_config(self) -> typing.Optional[builtins.str]:
        '''Secrets Manager ARN for kubeconfig file.

        :schema: CfnHelmProps#KubeConfig
        '''
        result = self._values.get("kube_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name for the helm release.

        :schema: CfnHelmProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to use with helm.

        Created if doesn't exist and default will be used if not provided

        :schema: CfnHelmProps#Namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''Repository url.

        Defaults to kubernetes-charts.storage.googleapis.com

        :default: kubernetes-charts.storage.googleapis.com

        :schema: CfnHelmProps#Repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_options(self) -> typing.Optional["CfnHelmPropsRepositoryOptions"]:
        '''Extra options for repository.

        :schema: CfnHelmProps#RepositoryOptions
        '''
        result = self._values.get("repository_options")
        return typing.cast(typing.Optional["CfnHelmPropsRepositoryOptions"], result)

    @builtins.property
    def resources(self) -> typing.Any:
        '''Resources from the helm charts.

        :schema: CfnHelmProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Any, result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''IAM to use with EKS cluster authentication, if not resource execution role will be used.

        :schema: CfnHelmProps#RoleArn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_out(self) -> typing.Optional[jsii.Number]:
        '''Timeout for resource provider.

        Default 60 mins

        :schema: CfnHelmProps#TimeOut
        '''
        result = self._values.get("time_out")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value_override_url(self) -> typing.Optional[builtins.str]:
        '''Custom Value Yaml file can optionally be specified.

        :schema: CfnHelmProps#ValueOverrideURL
        '''
        result = self._values.get("value_override_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Any:
        '''Custom Values can optionally be specified.

        :schema: CfnHelmProps#Values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Any, result)

    @builtins.property
    def value_yaml(self) -> typing.Optional[builtins.str]:
        '''String representation of a values.yaml file.

        :schema: CfnHelmProps#ValueYaml
        '''
        result = self._values.get("value_yaml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version can be specified, if not latest will be used.

        :schema: CfnHelmProps#Version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_configuration(self) -> typing.Optional["CfnHelmPropsVpcConfiguration"]:
        '''For network connectivity to Cluster inside VPC.

        :schema: CfnHelmProps#VPCConfiguration
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional["CfnHelmPropsVpcConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHelmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-helm.CfnHelmPropsRepositoryOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ca_file": "caFile",
        "insecure_skip_tls_verify": "insecureSkipTlsVerify",
        "password": "password",
        "username": "username",
    },
)
class CfnHelmPropsRepositoryOptions:
    def __init__(
        self,
        *,
        ca_file: typing.Optional[builtins.str] = None,
        insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Extra options for repository.

        :param ca_file: Verify certificates of HTTPS-enabled servers using this CA bundle from S3.
        :param insecure_skip_tls_verify: Skip TLS certificate checks for the repository.
        :param password: Chart repository password.
        :param username: Chart repository username.

        :schema: CfnHelmPropsRepositoryOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27413f2d50b93e887f78738f56fd70e79bc175e297375ac8a194ea49497e1001)
            check_type(argname="argument ca_file", value=ca_file, expected_type=type_hints["ca_file"])
            check_type(argname="argument insecure_skip_tls_verify", value=insecure_skip_tls_verify, expected_type=type_hints["insecure_skip_tls_verify"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca_file is not None:
            self._values["ca_file"] = ca_file
        if insecure_skip_tls_verify is not None:
            self._values["insecure_skip_tls_verify"] = insecure_skip_tls_verify
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def ca_file(self) -> typing.Optional[builtins.str]:
        '''Verify certificates of HTTPS-enabled servers using this CA bundle from S3.

        :schema: CfnHelmPropsRepositoryOptions#CAFile
        '''
        result = self._values.get("ca_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_tls_verify(self) -> typing.Optional[builtins.bool]:
        '''Skip TLS certificate checks for the repository.

        :schema: CfnHelmPropsRepositoryOptions#InsecureSkipTLSVerify
        '''
        result = self._values.get("insecure_skip_tls_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Chart repository password.

        :schema: CfnHelmPropsRepositoryOptions#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Chart repository username.

        :schema: CfnHelmPropsRepositoryOptions#Username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHelmPropsRepositoryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-helm.CfnHelmPropsVpcConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class CfnHelmPropsVpcConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''For network connectivity to Cluster inside VPC.

        :param security_group_ids: Specify one or more security groups.
        :param subnet_ids: Specify one or more subnets.

        :schema: CfnHelmPropsVpcConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9801f70e9cfe393fb397f67968d666edea6f65e0e84227e4681e856c98c1ad16)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more security groups.

        :schema: CfnHelmPropsVpcConfiguration#SecurityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more subnets.

        :schema: CfnHelmPropsVpcConfiguration#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHelmPropsVpcConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnHelm",
    "CfnHelmProps",
    "CfnHelmPropsRepositoryOptions",
    "CfnHelmPropsVpcConfiguration",
]

publication.publish()

def _typecheckingstub__cf7348506ac21f4b7ee9822b428a1c123a1c4e9c7ef1bc996e624979ab063137(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    chart: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    kube_config: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    repository_options: typing.Optional[typing.Union[CfnHelmPropsRepositoryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Any = None,
    role_arn: typing.Optional[builtins.str] = None,
    time_out: typing.Optional[jsii.Number] = None,
    value_override_url: typing.Optional[builtins.str] = None,
    values: typing.Any = None,
    value_yaml: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[CfnHelmPropsVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf179732a60d53e9ee24cb1142d5a0ac10b7f9e06f176d49496877b17cfcac0(
    *,
    chart: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    kube_config: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    repository_options: typing.Optional[typing.Union[CfnHelmPropsRepositoryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Any = None,
    role_arn: typing.Optional[builtins.str] = None,
    time_out: typing.Optional[jsii.Number] = None,
    value_override_url: typing.Optional[builtins.str] = None,
    values: typing.Any = None,
    value_yaml: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[CfnHelmPropsVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27413f2d50b93e887f78738f56fd70e79bc175e297375ac8a194ea49497e1001(
    *,
    ca_file: typing.Optional[builtins.str] = None,
    insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9801f70e9cfe393fb397f67968d666edea6f65e0e84227e4681e856c98c1ad16(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

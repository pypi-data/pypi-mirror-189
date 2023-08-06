'''
# tf-aws-s3bucket

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::AWS::S3Bucket` v1.0.0.

## Description

Provides a S3 bucket resource.

-> This functionality is for managing S3 in an AWS Partition. To manage [S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html), see the [`aws_s3control_bucket`](/docs/providers/aws/r/s3control_bucket.html) resource.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3Bucket/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::AWS::S3Bucket \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-AWS-S3Bucket \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::AWS::S3Bucket`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-aws-s3bucket+v1.0.0).
* Issues related to `TF::AWS::S3Bucket` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3Bucket/docs/README.md).

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
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.AccessControlTranslationDefinition",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner"},
)
class AccessControlTranslationDefinition:
    def __init__(self, *, owner: builtins.str) -> None:
        '''
        :param owner: The override value for the owner on replicated objects. Currently only ``Destination`` is supported.

        :schema: AccessControlTranslationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d32fb5c1ee3ea6dc8f3ff0d6c5b5fbe5c9fcc375f41f5f4c57f29dde1bcf3044)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "owner": owner,
        }

    @builtins.property
    def owner(self) -> builtins.str:
        '''The override value for the owner on replicated objects.

        Currently only ``Destination`` is supported.

        :schema: AccessControlTranslationDefinition#Owner
        '''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessControlTranslationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.ApplyServerSideEncryptionByDefaultDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "sse_algorithm": "sseAlgorithm",
        "kms_master_key_id": "kmsMasterKeyId",
    },
)
class ApplyServerSideEncryptionByDefaultDefinition:
    def __init__(
        self,
        *,
        sse_algorithm: builtins.str,
        kms_master_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sse_algorithm: The server-side encryption algorithm to use. Valid values are ``AES256`` and ``aws:kms``.
        :param kms_master_key_id: The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of ``sse_algorithm`` as ``aws:kms``. The default ``aws/s3`` AWS KMS master key is used if this element is absent while the ``sse_algorithm`` is ``aws:kms``.

        :schema: ApplyServerSideEncryptionByDefaultDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c98a99f461078d2e1e10925c676688c1500a3d3ec7bde105d3fb97162da2fe1)
            check_type(argname="argument sse_algorithm", value=sse_algorithm, expected_type=type_hints["sse_algorithm"])
            check_type(argname="argument kms_master_key_id", value=kms_master_key_id, expected_type=type_hints["kms_master_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sse_algorithm": sse_algorithm,
        }
        if kms_master_key_id is not None:
            self._values["kms_master_key_id"] = kms_master_key_id

    @builtins.property
    def sse_algorithm(self) -> builtins.str:
        '''The server-side encryption algorithm to use.

        Valid values are ``AES256`` and ``aws:kms``.

        :schema: ApplyServerSideEncryptionByDefaultDefinition#SseAlgorithm
        '''
        result = self._values.get("sse_algorithm")
        assert result is not None, "Required property 'sse_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_master_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS master key ID used for the SSE-KMS encryption.

        This can only be used when you set the value of ``sse_algorithm`` as ``aws:kms``. The default ``aws/s3`` AWS KMS master key is used if this element is absent while the ``sse_algorithm`` is ``aws:kms``.

        :schema: ApplyServerSideEncryptionByDefaultDefinition#KmsMasterKeyId
        '''
        result = self._values.get("kms_master_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplyServerSideEncryptionByDefaultDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnS3Bucket(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.CfnS3Bucket",
):
    '''A CloudFormation ``TF::AWS::S3Bucket``.

    :cloudformationResource: TF::AWS::S3Bucket
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        acceleration_status: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        bucket: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cors_rule: typing.Optional[typing.Sequence[typing.Union["CorsRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        force_destroy: typing.Optional[builtins.bool] = None,
        grant: typing.Optional[typing.Sequence[typing.Union["GrantDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        lifecycle_rule: typing.Optional[typing.Sequence[typing.Union["LifecycleRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        logging: typing.Optional[typing.Sequence[typing.Union["LoggingDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_lock_configuration: typing.Optional[typing.Sequence[typing.Union["ObjectLockConfigurationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        policy: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Sequence[typing.Union["ReplicationConfigurationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        request_payer: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Sequence[typing.Union["ServerSideEncryptionConfigurationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags_all: typing.Optional[typing.Sequence[typing.Union["TagsAllDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        versioning: typing.Optional[typing.Sequence[typing.Union["VersioningDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website: typing.Optional[typing.Sequence[typing.Union["WebsiteDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website_domain: typing.Optional[builtins.str] = None,
        website_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::AWS::S3Bucket``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param acceleration_status: Sets the accelerate configuration of an existing bucket. Can be ``Enabled`` or ``Suspended``.
        :param acl: The `canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ to apply. Valid values are ``private``, ``public-read``, ``public-read-write``, ``aws-exec-read``, ``authenticated-read``, and ``log-delivery-write``. Defaults to ``private``. Conflicts with ``grant``. Default: private``. Conflicts with ``grant`.
        :param arn: 
        :param bucket: The name of the bucket. If omitted, Terraform will assign a random, unique name. Must be less than or equal to 63 characters in length.
        :param bucket_prefix: Creates a unique bucket name beginning with the specified prefix. Conflicts with ``bucket``. Must be less than or equal to 37 characters in length.
        :param cors_rule: 
        :param force_destroy: A boolean that indicates all objects (including any `locked objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html>`_) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
        :param grant: 
        :param hosted_zone_id: 
        :param lifecycle_rule: 
        :param logging: 
        :param object_lock_configuration: 
        :param policy: A valid `bucket policy <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html>`_ JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a ``terraform plan``. In this case, please make sure you use the verbose/specific version of the policy. For more information about building AWS IAM policy documents with Terraform, see the `AWS IAM Policy Document Guide <https://learn.hashicorp.com/terraform/aws/iam-policy>`_.
        :param replication_configuration: 
        :param request_payer: Specifies who should bear the cost of Amazon S3 data transfer. Can be either ``BucketOwner`` or ``Requester``. By default, the owner of the S3 bucket would incur the costs of any data transfer. See `Requester Pays Buckets <http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`_ developer guide for more information.
        :param server_side_encryption_configuration: 
        :param tags: A map of tags to assign to the bucket. If configured with a provider ```default_tags`` configuration block </docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 
        :param versioning: 
        :param website: 
        :param website_domain: 
        :param website_endpoint: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2833aaf25711017d13fe06b69537161354a7d95a641b72699a9eefef2c6c022)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnS3BucketProps(
            acceleration_status=acceleration_status,
            acl=acl,
            arn=arn,
            bucket=bucket,
            bucket_prefix=bucket_prefix,
            cors_rule=cors_rule,
            force_destroy=force_destroy,
            grant=grant,
            hosted_zone_id=hosted_zone_id,
            lifecycle_rule=lifecycle_rule,
            logging=logging,
            object_lock_configuration=object_lock_configuration,
            policy=policy,
            replication_configuration=replication_configuration,
            request_payer=request_payer,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
            tags_all=tags_all,
            versioning=versioning,
            website=website,
            website_domain=website_domain,
            website_endpoint=website_endpoint,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBucketDomainName")
    def attr_bucket_domain_name(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3Bucket.BucketDomainName``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBucketDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrBucketRegionalDomainName")
    def attr_bucket_regional_domain_name(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3Bucket.BucketRegionalDomainName``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBucketRegionalDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3Bucket.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRegion")
    def attr_region(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3Bucket.Region``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegion"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3Bucket.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnS3BucketProps":
        '''Resource props.'''
        return typing.cast("CfnS3BucketProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.CfnS3BucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "acceleration_status": "accelerationStatus",
        "acl": "acl",
        "arn": "arn",
        "bucket": "bucket",
        "bucket_prefix": "bucketPrefix",
        "cors_rule": "corsRule",
        "force_destroy": "forceDestroy",
        "grant": "grant",
        "hosted_zone_id": "hostedZoneId",
        "lifecycle_rule": "lifecycleRule",
        "logging": "logging",
        "object_lock_configuration": "objectLockConfiguration",
        "policy": "policy",
        "replication_configuration": "replicationConfiguration",
        "request_payer": "requestPayer",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "versioning": "versioning",
        "website": "website",
        "website_domain": "websiteDomain",
        "website_endpoint": "websiteEndpoint",
    },
)
class CfnS3BucketProps:
    def __init__(
        self,
        *,
        acceleration_status: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        bucket: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cors_rule: typing.Optional[typing.Sequence[typing.Union["CorsRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        force_destroy: typing.Optional[builtins.bool] = None,
        grant: typing.Optional[typing.Sequence[typing.Union["GrantDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        lifecycle_rule: typing.Optional[typing.Sequence[typing.Union["LifecycleRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        logging: typing.Optional[typing.Sequence[typing.Union["LoggingDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_lock_configuration: typing.Optional[typing.Sequence[typing.Union["ObjectLockConfigurationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        policy: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Sequence[typing.Union["ReplicationConfigurationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        request_payer: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Sequence[typing.Union["ServerSideEncryptionConfigurationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags_all: typing.Optional[typing.Sequence[typing.Union["TagsAllDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        versioning: typing.Optional[typing.Sequence[typing.Union["VersioningDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website: typing.Optional[typing.Sequence[typing.Union["WebsiteDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website_domain: typing.Optional[builtins.str] = None,
        website_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Provides a S3 bucket resource.

        -> This functionality is for managing S3 in an AWS Partition. To manage `S3 on Outposts <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html>`_, see the ```aws_s3control_bucket`` </docs/providers/aws/r/s3control_bucket.html>`_ resource.

        :param acceleration_status: Sets the accelerate configuration of an existing bucket. Can be ``Enabled`` or ``Suspended``.
        :param acl: The `canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ to apply. Valid values are ``private``, ``public-read``, ``public-read-write``, ``aws-exec-read``, ``authenticated-read``, and ``log-delivery-write``. Defaults to ``private``. Conflicts with ``grant``. Default: private``. Conflicts with ``grant`.
        :param arn: 
        :param bucket: The name of the bucket. If omitted, Terraform will assign a random, unique name. Must be less than or equal to 63 characters in length.
        :param bucket_prefix: Creates a unique bucket name beginning with the specified prefix. Conflicts with ``bucket``. Must be less than or equal to 37 characters in length.
        :param cors_rule: 
        :param force_destroy: A boolean that indicates all objects (including any `locked objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html>`_) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
        :param grant: 
        :param hosted_zone_id: 
        :param lifecycle_rule: 
        :param logging: 
        :param object_lock_configuration: 
        :param policy: A valid `bucket policy <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html>`_ JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a ``terraform plan``. In this case, please make sure you use the verbose/specific version of the policy. For more information about building AWS IAM policy documents with Terraform, see the `AWS IAM Policy Document Guide <https://learn.hashicorp.com/terraform/aws/iam-policy>`_.
        :param replication_configuration: 
        :param request_payer: Specifies who should bear the cost of Amazon S3 data transfer. Can be either ``BucketOwner`` or ``Requester``. By default, the owner of the S3 bucket would incur the costs of any data transfer. See `Requester Pays Buckets <http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`_ developer guide for more information.
        :param server_side_encryption_configuration: 
        :param tags: A map of tags to assign to the bucket. If configured with a provider ```default_tags`` configuration block </docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 
        :param versioning: 
        :param website: 
        :param website_domain: 
        :param website_endpoint: 

        :schema: CfnS3BucketProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__840af101b02176928bb0b9efc99e77072b479bb375a27758ecff6625b03185a9)
            check_type(argname="argument acceleration_status", value=acceleration_status, expected_type=type_hints["acceleration_status"])
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument cors_rule", value=cors_rule, expected_type=type_hints["cors_rule"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument grant", value=grant, expected_type=type_hints["grant"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument lifecycle_rule", value=lifecycle_rule, expected_type=type_hints["lifecycle_rule"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument object_lock_configuration", value=object_lock_configuration, expected_type=type_hints["object_lock_configuration"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
            check_type(argname="argument request_payer", value=request_payer, expected_type=type_hints["request_payer"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument versioning", value=versioning, expected_type=type_hints["versioning"])
            check_type(argname="argument website", value=website, expected_type=type_hints["website"])
            check_type(argname="argument website_domain", value=website_domain, expected_type=type_hints["website_domain"])
            check_type(argname="argument website_endpoint", value=website_endpoint, expected_type=type_hints["website_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acceleration_status is not None:
            self._values["acceleration_status"] = acceleration_status
        if acl is not None:
            self._values["acl"] = acl
        if arn is not None:
            self._values["arn"] = arn
        if bucket is not None:
            self._values["bucket"] = bucket
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if cors_rule is not None:
            self._values["cors_rule"] = cors_rule
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if grant is not None:
            self._values["grant"] = grant
        if hosted_zone_id is not None:
            self._values["hosted_zone_id"] = hosted_zone_id
        if lifecycle_rule is not None:
            self._values["lifecycle_rule"] = lifecycle_rule
        if logging is not None:
            self._values["logging"] = logging
        if object_lock_configuration is not None:
            self._values["object_lock_configuration"] = object_lock_configuration
        if policy is not None:
            self._values["policy"] = policy
        if replication_configuration is not None:
            self._values["replication_configuration"] = replication_configuration
        if request_payer is not None:
            self._values["request_payer"] = request_payer
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if versioning is not None:
            self._values["versioning"] = versioning
        if website is not None:
            self._values["website"] = website
        if website_domain is not None:
            self._values["website_domain"] = website_domain
        if website_endpoint is not None:
            self._values["website_endpoint"] = website_endpoint

    @builtins.property
    def acceleration_status(self) -> typing.Optional[builtins.str]:
        '''Sets the accelerate configuration of an existing bucket.

        Can be ``Enabled`` or ``Suspended``.

        :schema: CfnS3BucketProps#AccelerationStatus
        '''
        result = self._values.get("acceleration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''The `canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ to apply. Valid values are ``private``, ``public-read``, ``public-read-write``, ``aws-exec-read``, ``authenticated-read``, and ``log-delivery-write``. Defaults to ``private``.  Conflicts with ``grant``.

        :default: private``.  Conflicts with ``grant`.

        :schema: CfnS3BucketProps#Acl
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3BucketProps#Arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the bucket.

        If omitted, Terraform will assign a random, unique name. Must be less than or equal to 63 characters in length.

        :schema: CfnS3BucketProps#Bucket
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique bucket name beginning with the specified prefix.

        Conflicts with ``bucket``. Must be less than or equal to 37 characters in length.

        :schema: CfnS3BucketProps#BucketPrefix
        '''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cors_rule(self) -> typing.Optional[typing.List["CorsRuleDefinition"]]:
        '''
        :schema: CfnS3BucketProps#CorsRule
        '''
        result = self._values.get("cors_rule")
        return typing.cast(typing.Optional[typing.List["CorsRuleDefinition"]], result)

    @builtins.property
    def force_destroy(self) -> typing.Optional[builtins.bool]:
        '''A boolean that indicates all objects (including any `locked objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html>`_) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

        :schema: CfnS3BucketProps#ForceDestroy
        '''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def grant(self) -> typing.Optional[typing.List["GrantDefinition"]]:
        '''
        :schema: CfnS3BucketProps#Grant
        '''
        result = self._values.get("grant")
        return typing.cast(typing.Optional[typing.List["GrantDefinition"]], result)

    @builtins.property
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3BucketProps#HostedZoneId
        '''
        result = self._values.get("hosted_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_rule(self) -> typing.Optional[typing.List["LifecycleRuleDefinition"]]:
        '''
        :schema: CfnS3BucketProps#LifecycleRule
        '''
        result = self._values.get("lifecycle_rule")
        return typing.cast(typing.Optional[typing.List["LifecycleRuleDefinition"]], result)

    @builtins.property
    def logging(self) -> typing.Optional[typing.List["LoggingDefinition"]]:
        '''
        :schema: CfnS3BucketProps#Logging
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.List["LoggingDefinition"]], result)

    @builtins.property
    def object_lock_configuration(
        self,
    ) -> typing.Optional[typing.List["ObjectLockConfigurationDefinition"]]:
        '''
        :schema: CfnS3BucketProps#ObjectLockConfiguration
        '''
        result = self._values.get("object_lock_configuration")
        return typing.cast(typing.Optional[typing.List["ObjectLockConfigurationDefinition"]], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''A valid `bucket policy <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html>`_ JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a ``terraform plan``. In this case, please make sure you use the verbose/specific version of the policy. For more information about building AWS IAM policy documents with Terraform, see the `AWS IAM Policy Document Guide <https://learn.hashicorp.com/terraform/aws/iam-policy>`_.

        :schema: CfnS3BucketProps#Policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Optional[typing.List["ReplicationConfigurationDefinition"]]:
        '''
        :schema: CfnS3BucketProps#ReplicationConfiguration
        '''
        result = self._values.get("replication_configuration")
        return typing.cast(typing.Optional[typing.List["ReplicationConfigurationDefinition"]], result)

    @builtins.property
    def request_payer(self) -> typing.Optional[builtins.str]:
        '''Specifies who should bear the cost of Amazon S3 data transfer.

        Can be either ``BucketOwner`` or ``Requester``. By default, the owner of the S3 bucket would incur
        the costs of any data transfer. See `Requester Pays Buckets <http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`_
        developer guide for more information.

        :schema: CfnS3BucketProps#RequestPayer
        '''
        result = self._values.get("request_payer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.List["ServerSideEncryptionConfigurationDefinition"]]:
        '''
        :schema: CfnS3BucketProps#ServerSideEncryptionConfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.List["ServerSideEncryptionConfigurationDefinition"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagsDefinition"]]:
        '''A map of tags to assign to the bucket.

        If configured with a provider ```default_tags`` configuration block </docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.

        :schema: CfnS3BucketProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagsDefinition"]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.List["TagsAllDefinition"]]:
        '''
        :schema: CfnS3BucketProps#TagsAll
        '''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.List["TagsAllDefinition"]], result)

    @builtins.property
    def versioning(self) -> typing.Optional[typing.List["VersioningDefinition"]]:
        '''
        :schema: CfnS3BucketProps#Versioning
        '''
        result = self._values.get("versioning")
        return typing.cast(typing.Optional[typing.List["VersioningDefinition"]], result)

    @builtins.property
    def website(self) -> typing.Optional[typing.List["WebsiteDefinition"]]:
        '''
        :schema: CfnS3BucketProps#Website
        '''
        result = self._values.get("website")
        return typing.cast(typing.Optional[typing.List["WebsiteDefinition"]], result)

    @builtins.property
    def website_domain(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3BucketProps#WebsiteDomain
        '''
        result = self._values.get("website_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def website_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3BucketProps#WebsiteEndpoint
        '''
        result = self._values.get("website_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.CorsRuleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "allowed_headers": "allowedHeaders",
        "expose_headers": "exposeHeaders",
        "max_age_seconds": "maxAgeSeconds",
    },
)
class CorsRuleDefinition:
    def __init__(
        self,
        *,
        allowed_methods: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allowed_methods: 
        :param allowed_origins: 
        :param allowed_headers: 
        :param expose_headers: 
        :param max_age_seconds: 

        :schema: CorsRuleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30ec3b467b8528e425c79a45917311fb38f517d5ea550a936e9a67b9ad6dfbf1)
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age_seconds", value=max_age_seconds, expected_type=type_hints["max_age_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_methods": allowed_methods,
            "allowed_origins": allowed_origins,
        }
        if allowed_headers is not None:
            self._values["allowed_headers"] = allowed_headers
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age_seconds is not None:
            self._values["max_age_seconds"] = max_age_seconds

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''
        :schema: CorsRuleDefinition#AllowedMethods
        '''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''
        :schema: CorsRuleDefinition#AllowedOrigins
        '''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CorsRuleDefinition#AllowedHeaders
        '''
        result = self._values.get("allowed_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CorsRuleDefinition#ExposeHeaders
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CorsRuleDefinition#MaxAgeSeconds
        '''
        result = self._values.get("max_age_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CorsRuleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.DestinationDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "access_control_translation": "accessControlTranslation",
        "account_id": "accountId",
        "replica_kms_key_id": "replicaKmsKeyId",
        "storage_class": "storageClass",
    },
)
class DestinationDefinition:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        access_control_translation: typing.Optional[typing.Sequence[typing.Union[AccessControlTranslationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        account_id: typing.Optional[builtins.str] = None,
        replica_kms_key_id: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
        :param access_control_translation: 
        :param account_id: The Account ID to use for overriding the object owner on replication. Must be used in conjunction with ``access_control_translation`` override configuration.
        :param replica_kms_key_id: Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with ``sse_kms_encrypted_objects`` source selection criteria.
        :param storage_class: The class of storage used to store the object. Can be ``STANDARD``, ``REDUCED_REDUNDANCY``, ``STANDARD_IA``, ``ONEZONE_IA``, ``INTELLIGENT_TIERING``, ``GLACIER``, or ``DEEP_ARCHIVE``.

        :schema: DestinationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a62f05d0de8431cc72998899157fb3ce5bf32cfa8833e0eae2f13f238de491)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument access_control_translation", value=access_control_translation, expected_type=type_hints["access_control_translation"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument replica_kms_key_id", value=replica_kms_key_id, expected_type=type_hints["replica_kms_key_id"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if access_control_translation is not None:
            self._values["access_control_translation"] = access_control_translation
        if account_id is not None:
            self._values["account_id"] = account_id
        if replica_kms_key_id is not None:
            self._values["replica_kms_key_id"] = replica_kms_key_id
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

        :schema: DestinationDefinition#Bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_translation(
        self,
    ) -> typing.Optional[typing.List[AccessControlTranslationDefinition]]:
        '''
        :schema: DestinationDefinition#AccessControlTranslation
        '''
        result = self._values.get("access_control_translation")
        return typing.cast(typing.Optional[typing.List[AccessControlTranslationDefinition]], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The Account ID to use for overriding the object owner on replication.

        Must be used in conjunction with ``access_control_translation`` override configuration.

        :schema: DestinationDefinition#AccountId
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replica_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Destination KMS encryption key ARN for SSE-KMS replication.

        Must be used in conjunction with
        ``sse_kms_encrypted_objects`` source selection criteria.

        :schema: DestinationDefinition#ReplicaKmsKeyId
        '''
        result = self._values.get("replica_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''The class of storage used to store the object.

        Can be ``STANDARD``, ``REDUCED_REDUNDANCY``, ``STANDARD_IA``, ``ONEZONE_IA``, ``INTELLIGENT_TIERING``, ``GLACIER``, or ``DEEP_ARCHIVE``.

        :schema: DestinationDefinition#StorageClass
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.ExpirationDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "date": "date",
        "days": "days",
        "expired_object_delete_marker": "expiredObjectDeleteMarker",
    },
)
class ExpirationDefinition:
    def __init__(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param date: 
        :param days: 
        :param expired_object_delete_marker: 

        :schema: ExpirationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f82be041aebf5f7b95b960c993fc745aa34a7513cd1dafb545463355e3c25dca)
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            check_type(argname="argument expired_object_delete_marker", value=expired_object_delete_marker, expected_type=type_hints["expired_object_delete_marker"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date is not None:
            self._values["date"] = date
        if days is not None:
            self._values["days"] = days
        if expired_object_delete_marker is not None:
            self._values["expired_object_delete_marker"] = expired_object_delete_marker

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExpirationDefinition#Date
        '''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExpirationDefinition#Days
        '''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def expired_object_delete_marker(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExpirationDefinition#ExpiredObjectDeleteMarker
        '''
        result = self._values.get("expired_object_delete_marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpirationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.FilterDefinition",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "tags": "tags"},
)
class FilterDefinition:
    def __init__(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition3", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param prefix: Object keyname prefix that identifies subset of objects to which the rule applies. Must be less than or equal to 1024 characters in length.
        :param tags: A map of tags that identifies subset of objects to which the rule applies. The rule applies only to objects having all the tags in its tagset.

        :schema: FilterDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d39e375c5e02ad1a787ef993b7c63f3035edde4b09a8f00a52fa4b0a4af3e50)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Object keyname prefix that identifies subset of objects to which the rule applies.

        Must be less than or equal to 1024 characters in length.

        :schema: FilterDefinition#Prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagsDefinition3"]]:
        '''A map of tags that identifies subset of objects to which the rule applies.

        The rule applies only to objects having all the tags in its tagset.

        :schema: FilterDefinition#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagsDefinition3"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.GrantDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "type": "type",
        "id": "id",
        "uri": "uri",
    },
)
class GrantDefinition:
    def __init__(
        self,
        *,
        permissions: typing.Sequence[builtins.str],
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions: List of permissions to apply for grantee. Valid values are ``READ``, ``WRITE``, ``READ_ACP``, ``WRITE_ACP``, ``FULL_CONTROL``.
        :param type: - Type of grantee to apply for. Valid values are ``CanonicalUser`` and ``Group``. ``AmazonCustomerByEmail`` is not supported.
        :param id: Canonical user id to grant for. Used only when ``type`` is ``CanonicalUser``.
        :param uri: Uri address to grant for. Used only when ``type`` is ``Group``.

        :schema: GrantDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3080b05b73b5808a5c96e0010aead6e9f23f7959c3a6b1a5e327256844a96ab6)
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions": permissions,
            "type": type,
        }
        if id is not None:
            self._values["id"] = id
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def permissions(self) -> typing.List[builtins.str]:
        '''List of permissions to apply for grantee.

        Valid values are ``READ``, ``WRITE``, ``READ_ACP``, ``WRITE_ACP``, ``FULL_CONTROL``.

        :schema: GrantDefinition#Permissions
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''- Type of grantee to apply for.

        Valid values are ``CanonicalUser`` and ``Group``. ``AmazonCustomerByEmail`` is not supported.

        :schema: GrantDefinition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Canonical user id to grant for.

        Used only when ``type`` is ``CanonicalUser``.

        :schema: GrantDefinition#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Uri address to grant for.

        Used only when ``type`` is ``Group``.

        :schema: GrantDefinition#Uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.LifecycleRuleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "abort_incomplete_multipart_upload_days": "abortIncompleteMultipartUploadDays",
        "expiration": "expiration",
        "id": "id",
        "noncurrent_version_expiration": "noncurrentVersionExpiration",
        "noncurrent_version_transition": "noncurrentVersionTransition",
        "prefix": "prefix",
        "tags": "tags",
        "transition": "transition",
    },
)
class LifecycleRuleDefinition:
    def __init__(
        self,
        *,
        enabled: builtins.bool,
        abort_incomplete_multipart_upload_days: typing.Optional[jsii.Number] = None,
        expiration: typing.Optional[typing.Sequence[typing.Union[ExpirationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        id: typing.Optional[builtins.str] = None,
        noncurrent_version_expiration: typing.Optional[typing.Sequence[typing.Union["NoncurrentVersionExpirationDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        noncurrent_version_transition: typing.Optional[typing.Sequence[typing.Union["NoncurrentVersionTransitionDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition2", typing.Dict[builtins.str, typing.Any]]]] = None,
        transition: typing.Optional[typing.Sequence[typing.Union["TransitionDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param enabled: Specifies lifecycle rule status.
        :param abort_incomplete_multipart_upload_days: 
        :param expiration: 
        :param id: Unique identifier for the rule. Must be less than or equal to 255 characters in length.
        :param noncurrent_version_expiration: 
        :param noncurrent_version_transition: 
        :param prefix: Object key prefix identifying one or more objects to which the rule applies.
        :param tags: Specifies object tags key and value.
        :param transition: 

        :schema: LifecycleRuleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6fe7ad1055a4f6fde14e0917d1cc4ee549ab5bd4c7919d5de36a953dc2324a1)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument abort_incomplete_multipart_upload_days", value=abort_incomplete_multipart_upload_days, expected_type=type_hints["abort_incomplete_multipart_upload_days"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument noncurrent_version_expiration", value=noncurrent_version_expiration, expected_type=type_hints["noncurrent_version_expiration"])
            check_type(argname="argument noncurrent_version_transition", value=noncurrent_version_transition, expected_type=type_hints["noncurrent_version_transition"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transition", value=transition, expected_type=type_hints["transition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if abort_incomplete_multipart_upload_days is not None:
            self._values["abort_incomplete_multipart_upload_days"] = abort_incomplete_multipart_upload_days
        if expiration is not None:
            self._values["expiration"] = expiration
        if id is not None:
            self._values["id"] = id
        if noncurrent_version_expiration is not None:
            self._values["noncurrent_version_expiration"] = noncurrent_version_expiration
        if noncurrent_version_transition is not None:
            self._values["noncurrent_version_transition"] = noncurrent_version_transition
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags
        if transition is not None:
            self._values["transition"] = transition

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''Specifies lifecycle rule status.

        :schema: LifecycleRuleDefinition#Enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def abort_incomplete_multipart_upload_days(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: LifecycleRuleDefinition#AbortIncompleteMultipartUploadDays
        '''
        result = self._values.get("abort_incomplete_multipart_upload_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def expiration(self) -> typing.Optional[typing.List[ExpirationDefinition]]:
        '''
        :schema: LifecycleRuleDefinition#Expiration
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[typing.List[ExpirationDefinition]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for the rule.

        Must be less than or equal to 255 characters in length.

        :schema: LifecycleRuleDefinition#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noncurrent_version_expiration(
        self,
    ) -> typing.Optional[typing.List["NoncurrentVersionExpirationDefinition"]]:
        '''
        :schema: LifecycleRuleDefinition#NoncurrentVersionExpiration
        '''
        result = self._values.get("noncurrent_version_expiration")
        return typing.cast(typing.Optional[typing.List["NoncurrentVersionExpirationDefinition"]], result)

    @builtins.property
    def noncurrent_version_transition(
        self,
    ) -> typing.Optional[typing.List["NoncurrentVersionTransitionDefinition"]]:
        '''
        :schema: LifecycleRuleDefinition#NoncurrentVersionTransition
        '''
        result = self._values.get("noncurrent_version_transition")
        return typing.cast(typing.Optional[typing.List["NoncurrentVersionTransitionDefinition"]], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Object key prefix identifying one or more objects to which the rule applies.

        :schema: LifecycleRuleDefinition#Prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagsDefinition2"]]:
        '''Specifies object tags key and value.

        :schema: LifecycleRuleDefinition#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagsDefinition2"]], result)

    @builtins.property
    def transition(self) -> typing.Optional[typing.List["TransitionDefinition"]]:
        '''
        :schema: LifecycleRuleDefinition#Transition
        '''
        result = self._values.get("transition")
        return typing.cast(typing.Optional[typing.List["TransitionDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecycleRuleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.LoggingDefinition",
    jsii_struct_bases=[],
    name_mapping={"target_bucket": "targetBucket", "target_prefix": "targetPrefix"},
)
class LoggingDefinition:
    def __init__(
        self,
        *,
        target_bucket: builtins.str,
        target_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_bucket: The name of the bucket that will receive the log objects.
        :param target_prefix: To specify a key prefix for log objects.

        :schema: LoggingDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb740eab09c35ace7966c437e9b1585c2c7ab81fa96031167850a5218e6287bd)
            check_type(argname="argument target_bucket", value=target_bucket, expected_type=type_hints["target_bucket"])
            check_type(argname="argument target_prefix", value=target_prefix, expected_type=type_hints["target_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_bucket": target_bucket,
        }
        if target_prefix is not None:
            self._values["target_prefix"] = target_prefix

    @builtins.property
    def target_bucket(self) -> builtins.str:
        '''The name of the bucket that will receive the log objects.

        :schema: LoggingDefinition#TargetBucket
        '''
        result = self._values.get("target_bucket")
        assert result is not None, "Required property 'target_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_prefix(self) -> typing.Optional[builtins.str]:
        '''To specify a key prefix for log objects.

        :schema: LoggingDefinition#TargetPrefix
        '''
        result = self._values.get("target_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.NoncurrentVersionExpirationDefinition",
    jsii_struct_bases=[],
    name_mapping={"days": "days"},
)
class NoncurrentVersionExpirationDefinition:
    def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param days: 

        :schema: NoncurrentVersionExpirationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2759c99240bc080c7ca57ad66d803fec526af1914b92f698911e5b044d3101d1)
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: NoncurrentVersionExpirationDefinition#Days
        '''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NoncurrentVersionExpirationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.NoncurrentVersionTransitionDefinition",
    jsii_struct_bases=[],
    name_mapping={"storage_class": "storageClass", "days": "days"},
)
class NoncurrentVersionTransitionDefinition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: 
        :param days: 

        :schema: NoncurrentVersionTransitionDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8f6b948317d1283320c8c27bfb5ab01c8b3f4df2883452f7251661fa7ecc8d6)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''
        :schema: NoncurrentVersionTransitionDefinition#StorageClass
        '''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: NoncurrentVersionTransitionDefinition#Days
        '''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NoncurrentVersionTransitionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.ObjectLockConfigurationDefinition",
    jsii_struct_bases=[],
    name_mapping={"object_lock_enabled": "objectLockEnabled", "rule": "rule"},
)
class ObjectLockConfigurationDefinition:
    def __init__(
        self,
        *,
        object_lock_enabled: builtins.str,
        rule: typing.Optional[typing.Sequence[typing.Union["RuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled. Valid value is ``Enabled``.
        :param rule: 

        :schema: ObjectLockConfigurationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1813fa96166b001dac6f50ce4963fefa41fc058b871b0047b6f35d05448db9ae)
            check_type(argname="argument object_lock_enabled", value=object_lock_enabled, expected_type=type_hints["object_lock_enabled"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_lock_enabled": object_lock_enabled,
        }
        if rule is not None:
            self._values["rule"] = rule

    @builtins.property
    def object_lock_enabled(self) -> builtins.str:
        '''Indicates whether this bucket has an Object Lock configuration enabled.

        Valid value is ``Enabled``.

        :schema: ObjectLockConfigurationDefinition#ObjectLockEnabled
        '''
        result = self._values.get("object_lock_enabled")
        assert result is not None, "Required property 'object_lock_enabled' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> typing.Optional[typing.List["RuleDefinition"]]:
        '''
        :schema: ObjectLockConfigurationDefinition#Rule
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.List["RuleDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ObjectLockConfigurationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.ReplicationConfigurationDefinition",
    jsii_struct_bases=[],
    name_mapping={"role": "role", "rules": "rules"},
)
class ReplicationConfigurationDefinition:
    def __init__(
        self,
        *,
        role: builtins.str,
        rules: typing.Optional[typing.Sequence[typing.Union["RulesDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param role: The ARN of the IAM role for Amazon S3 to assume when replicating the objects.
        :param rules: 

        :schema: ReplicationConfigurationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b76a80f0e92ae37188d7f060767e43c033ae9449235c751096fbf95073655cf)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
        }
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def role(self) -> builtins.str:
        '''The ARN of the IAM role for Amazon S3 to assume when replicating the objects.

        :schema: ReplicationConfigurationDefinition#Role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List["RulesDefinition"]]:
        '''
        :schema: ReplicationConfigurationDefinition#Rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List["RulesDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationConfigurationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.RuleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "apply_server_side_encryption_by_default": "applyServerSideEncryptionByDefault",
        "bucket_key_enabled": "bucketKeyEnabled",
    },
)
class RuleDefinition:
    def __init__(
        self,
        *,
        apply_server_side_encryption_by_default: typing.Optional[typing.Sequence[typing.Union[ApplyServerSideEncryptionByDefaultDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        bucket_key_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param apply_server_side_encryption_by_default: 
        :param bucket_key_enabled: Whether or not to use `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html>`_ for SSE-KMS.

        :schema: RuleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__275b0fd6e691b88b46b8d3f3e3455731ef42896b606dcd2520719482b4cfdcf8)
            check_type(argname="argument apply_server_side_encryption_by_default", value=apply_server_side_encryption_by_default, expected_type=type_hints["apply_server_side_encryption_by_default"])
            check_type(argname="argument bucket_key_enabled", value=bucket_key_enabled, expected_type=type_hints["bucket_key_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if apply_server_side_encryption_by_default is not None:
            self._values["apply_server_side_encryption_by_default"] = apply_server_side_encryption_by_default
        if bucket_key_enabled is not None:
            self._values["bucket_key_enabled"] = bucket_key_enabled

    @builtins.property
    def apply_server_side_encryption_by_default(
        self,
    ) -> typing.Optional[typing.List[ApplyServerSideEncryptionByDefaultDefinition]]:
        '''
        :schema: RuleDefinition#ApplyServerSideEncryptionByDefault
        '''
        result = self._values.get("apply_server_side_encryption_by_default")
        return typing.cast(typing.Optional[typing.List[ApplyServerSideEncryptionByDefaultDefinition]], result)

    @builtins.property
    def bucket_key_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to use `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html>`_ for SSE-KMS.

        :schema: RuleDefinition#BucketKeyEnabled
        '''
        result = self._values.get("bucket_key_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.RulesDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "status": "status",
        "destination": "destination",
        "filter": "filter",
        "id": "id",
        "prefix": "prefix",
        "priority": "priority",
        "source_selection_criteria": "sourceSelectionCriteria",
    },
)
class RulesDefinition:
    def __init__(
        self,
        *,
        status: builtins.str,
        destination: typing.Optional[typing.Sequence[typing.Union[DestinationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        filter: typing.Optional[typing.Sequence[typing.Union[FilterDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        id: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        source_selection_criteria: typing.Optional[typing.Sequence[typing.Union["SourceSelectionCriteriaDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param status: The status of the rule. Either ``Enabled`` or ``Disabled``. The rule is ignored if status is not Enabled.
        :param destination: 
        :param filter: 
        :param id: Unique identifier for the rule. Must be less than or equal to 255 characters in length.
        :param prefix: Object keyname prefix identifying one or more objects to which the rule applies. Must be less than or equal to 1024 characters in length.
        :param priority: The priority associated with the rule.
        :param source_selection_criteria: 

        :schema: RulesDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a5ac1d7a81dc1fa681922bc4beb9611e98e87be6314b8167d6e3397df6aa019)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument source_selection_criteria", value=source_selection_criteria, expected_type=type_hints["source_selection_criteria"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }
        if destination is not None:
            self._values["destination"] = destination
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if prefix is not None:
            self._values["prefix"] = prefix
        if priority is not None:
            self._values["priority"] = priority
        if source_selection_criteria is not None:
            self._values["source_selection_criteria"] = source_selection_criteria

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the rule.

        Either ``Enabled`` or ``Disabled``. The rule is ignored if status is not Enabled.

        :schema: RulesDefinition#Status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> typing.Optional[typing.List[DestinationDefinition]]:
        '''
        :schema: RulesDefinition#Destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[typing.List[DestinationDefinition]], result)

    @builtins.property
    def filter(self) -> typing.Optional[typing.List[FilterDefinition]]:
        '''
        :schema: RulesDefinition#Filter
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.List[FilterDefinition]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for the rule.

        Must be less than or equal to 255 characters in length.

        :schema: RulesDefinition#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Object keyname prefix identifying one or more objects to which the rule applies.

        Must be less than or equal to 1024 characters in length.

        :schema: RulesDefinition#Prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority associated with the rule.

        :schema: RulesDefinition#Priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_selection_criteria(
        self,
    ) -> typing.Optional[typing.List["SourceSelectionCriteriaDefinition"]]:
        '''
        :schema: RulesDefinition#SourceSelectionCriteria
        '''
        result = self._values.get("source_selection_criteria")
        return typing.cast(typing.Optional[typing.List["SourceSelectionCriteriaDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.ServerSideEncryptionConfigurationDefinition",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule"},
)
class ServerSideEncryptionConfigurationDefinition:
    def __init__(
        self,
        *,
        rule: typing.Optional[typing.Sequence[typing.Union[RuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param rule: 

        :schema: ServerSideEncryptionConfigurationDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c03d4fb728fc8154f77370d1f0bf3f27a37470a07501ac48dc0d31e7c8a009)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if rule is not None:
            self._values["rule"] = rule

    @builtins.property
    def rule(self) -> typing.Optional[typing.List[RuleDefinition]]:
        '''
        :schema: ServerSideEncryptionConfigurationDefinition#Rule
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.List[RuleDefinition]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerSideEncryptionConfigurationDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.SourceSelectionCriteriaDefinition",
    jsii_struct_bases=[],
    name_mapping={"sse_kms_encrypted_objects": "sseKmsEncryptedObjects"},
)
class SourceSelectionCriteriaDefinition:
    def __init__(
        self,
        *,
        sse_kms_encrypted_objects: typing.Optional[typing.Sequence[typing.Union["SseKmsEncryptedObjectsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param sse_kms_encrypted_objects: 

        :schema: SourceSelectionCriteriaDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b32f60e78fa970408ba13f31e89bdee443545552e321c414a0a1dea930e0ce)
            check_type(argname="argument sse_kms_encrypted_objects", value=sse_kms_encrypted_objects, expected_type=type_hints["sse_kms_encrypted_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if sse_kms_encrypted_objects is not None:
            self._values["sse_kms_encrypted_objects"] = sse_kms_encrypted_objects

    @builtins.property
    def sse_kms_encrypted_objects(
        self,
    ) -> typing.Optional[typing.List["SseKmsEncryptedObjectsDefinition"]]:
        '''
        :schema: SourceSelectionCriteriaDefinition#SseKmsEncryptedObjects
        '''
        result = self._values.get("sse_kms_encrypted_objects")
        return typing.cast(typing.Optional[typing.List["SseKmsEncryptedObjectsDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceSelectionCriteriaDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.SseKmsEncryptedObjectsDefinition",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class SseKmsEncryptedObjectsDefinition:
    def __init__(self, *, enabled: builtins.bool) -> None:
        '''
        :param enabled: Boolean which indicates if this criteria is enabled.

        :schema: SseKmsEncryptedObjectsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d0b23a67697ab5932e7afbfb52265a4d83c49a3d56d08a61f34a38662891d03)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''Boolean which indicates if this criteria is enabled.

        :schema: SseKmsEncryptedObjectsDefinition#Enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SseKmsEncryptedObjectsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.TagsAllDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab08580cba929d56796d7708c087a95a21efbcdcd09c315dedca72d20ee8ab4c)
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
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.TagsDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cef74744791540923f61b4cea357d27ff88f60371d9bb897f99fca3c970d9c78)
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


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.TagsDefinition2",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class TagsDefinition2:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: TagsDefinition2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54da8dbb3cf3ba4879ff205340f4d126bd6fc559675a459359eb444b8be49708)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: TagsDefinition2#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: TagsDefinition2#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagsDefinition2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.TagsDefinition3",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class TagsDefinition3:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: TagsDefinition3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd00453294c1d2efe5eef6b77ec2d6016ce5a16963937edb487c3e4e4b543073)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: TagsDefinition3#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: TagsDefinition3#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagsDefinition3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.TransitionDefinition",
    jsii_struct_bases=[],
    name_mapping={"storage_class": "storageClass", "date": "date", "days": "days"},
)
class TransitionDefinition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: 
        :param date: 
        :param days: 

        :schema: TransitionDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcd28f6e410dfcd19372c9dd6084b4e8f1f1f3b616ef8cb8a8777aebf3d8cba1)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if date is not None:
            self._values["date"] = date
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''
        :schema: TransitionDefinition#StorageClass
        '''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TransitionDefinition#Date
        '''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: TransitionDefinition#Days
        '''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.VersioningDefinition",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "mfa_delete": "mfaDelete"},
)
class VersioningDefinition:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        mfa_delete: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param enabled: Enable versioning. Once you version-enable a bucket, it can never return to an unversioned state. You can, however, suspend versioning on that bucket.
        :param mfa_delete: Enable MFA delete for either ``Change the versioning state of your bucket`` or ``Permanently delete an object version``. Default is ``false``. This cannot be used to toggle this setting but is available to allow managed buckets to reflect the state in AWS. Default: false`. This cannot be used to toggle this setting but is available to allow managed buckets to reflect the state in AWS.

        :schema: VersioningDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7d5e9cb68c3d034bd4cb6866083850ff677db163514799e01a5a7945354ed65)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument mfa_delete", value=mfa_delete, expected_type=type_hints["mfa_delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if mfa_delete is not None:
            self._values["mfa_delete"] = mfa_delete

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable versioning.

        Once you version-enable a bucket, it can never return to an unversioned state. You can, however, suspend versioning on that bucket.

        :schema: VersioningDefinition#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mfa_delete(self) -> typing.Optional[builtins.bool]:
        '''Enable MFA delete for either ``Change the versioning state of your bucket`` or ``Permanently delete an object version``.

        Default is ``false``. This cannot be used to toggle this setting but is available to allow managed buckets to reflect the state in AWS.

        :default: false`. This cannot be used to toggle this setting but is available to allow managed buckets to reflect the state in AWS.

        :schema: VersioningDefinition#MfaDelete
        '''
        result = self._values.get("mfa_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersioningDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucket.WebsiteDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "error_document": "errorDocument",
        "index_document": "indexDocument",
        "redirect_all_requests_to": "redirectAllRequestsTo",
        "routing_rules": "routingRules",
    },
)
class WebsiteDefinition:
    def __init__(
        self,
        *,
        error_document: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[builtins.str] = None,
        redirect_all_requests_to: typing.Optional[builtins.str] = None,
        routing_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_document: An absolute path to the document to return in case of a 4XX error.
        :param index_document: Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.
        :param redirect_all_requests_to: A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (``http://`` or ``https://``) to use when redirecting requests. The default is the protocol that is used in the original request.
        :param routing_rules: A json array containing `routing rules <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html>`_ describing redirect behavior and when redirects are applied.

        :schema: WebsiteDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2df53e4823ef3f82500bbba89066ff313ce943656ed6bcba5e7a4b1f4b91103c)
            check_type(argname="argument error_document", value=error_document, expected_type=type_hints["error_document"])
            check_type(argname="argument index_document", value=index_document, expected_type=type_hints["index_document"])
            check_type(argname="argument redirect_all_requests_to", value=redirect_all_requests_to, expected_type=type_hints["redirect_all_requests_to"])
            check_type(argname="argument routing_rules", value=routing_rules, expected_type=type_hints["routing_rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if error_document is not None:
            self._values["error_document"] = error_document
        if index_document is not None:
            self._values["index_document"] = index_document
        if redirect_all_requests_to is not None:
            self._values["redirect_all_requests_to"] = redirect_all_requests_to
        if routing_rules is not None:
            self._values["routing_rules"] = routing_rules

    @builtins.property
    def error_document(self) -> typing.Optional[builtins.str]:
        '''An absolute path to the document to return in case of a 4XX error.

        :schema: WebsiteDefinition#ErrorDocument
        '''
        result = self._values.get("error_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_document(self) -> typing.Optional[builtins.str]:
        '''Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.

        :schema: WebsiteDefinition#IndexDocument
        '''
        result = self._values.get("index_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_all_requests_to(self) -> typing.Optional[builtins.str]:
        '''A hostname to redirect all website requests for this bucket to.

        Hostname can optionally be prefixed with a protocol (``http://`` or ``https://``) to use when redirecting requests. The default is the protocol that is used in the original request.

        :schema: WebsiteDefinition#RedirectAllRequestsTo
        '''
        result = self._values.get("redirect_all_requests_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_rules(self) -> typing.Optional[builtins.str]:
        '''A json array containing `routing rules <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html>`_ describing redirect behavior and when redirects are applied.

        :schema: WebsiteDefinition#RoutingRules
        '''
        result = self._values.get("routing_rules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebsiteDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessControlTranslationDefinition",
    "ApplyServerSideEncryptionByDefaultDefinition",
    "CfnS3Bucket",
    "CfnS3BucketProps",
    "CorsRuleDefinition",
    "DestinationDefinition",
    "ExpirationDefinition",
    "FilterDefinition",
    "GrantDefinition",
    "LifecycleRuleDefinition",
    "LoggingDefinition",
    "NoncurrentVersionExpirationDefinition",
    "NoncurrentVersionTransitionDefinition",
    "ObjectLockConfigurationDefinition",
    "ReplicationConfigurationDefinition",
    "RuleDefinition",
    "RulesDefinition",
    "ServerSideEncryptionConfigurationDefinition",
    "SourceSelectionCriteriaDefinition",
    "SseKmsEncryptedObjectsDefinition",
    "TagsAllDefinition",
    "TagsDefinition",
    "TagsDefinition2",
    "TagsDefinition3",
    "TransitionDefinition",
    "VersioningDefinition",
    "WebsiteDefinition",
]

publication.publish()

def _typecheckingstub__d32fb5c1ee3ea6dc8f3ff0d6c5b5fbe5c9fcc375f41f5f4c57f29dde1bcf3044(
    *,
    owner: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c98a99f461078d2e1e10925c676688c1500a3d3ec7bde105d3fb97162da2fe1(
    *,
    sse_algorithm: builtins.str,
    kms_master_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2833aaf25711017d13fe06b69537161354a7d95a641b72699a9eefef2c6c022(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    acceleration_status: typing.Optional[builtins.str] = None,
    acl: typing.Optional[builtins.str] = None,
    arn: typing.Optional[builtins.str] = None,
    bucket: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    cors_rule: typing.Optional[typing.Sequence[typing.Union[CorsRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    force_destroy: typing.Optional[builtins.bool] = None,
    grant: typing.Optional[typing.Sequence[typing.Union[GrantDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    lifecycle_rule: typing.Optional[typing.Sequence[typing.Union[LifecycleRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    logging: typing.Optional[typing.Sequence[typing.Union[LoggingDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_lock_configuration: typing.Optional[typing.Sequence[typing.Union[ObjectLockConfigurationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Sequence[typing.Union[ReplicationConfigurationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_payer: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Sequence[typing.Union[ServerSideEncryptionConfigurationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags_all: typing.Optional[typing.Sequence[typing.Union[TagsAllDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    versioning: typing.Optional[typing.Sequence[typing.Union[VersioningDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website: typing.Optional[typing.Sequence[typing.Union[WebsiteDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website_domain: typing.Optional[builtins.str] = None,
    website_endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840af101b02176928bb0b9efc99e77072b479bb375a27758ecff6625b03185a9(
    *,
    acceleration_status: typing.Optional[builtins.str] = None,
    acl: typing.Optional[builtins.str] = None,
    arn: typing.Optional[builtins.str] = None,
    bucket: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    cors_rule: typing.Optional[typing.Sequence[typing.Union[CorsRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    force_destroy: typing.Optional[builtins.bool] = None,
    grant: typing.Optional[typing.Sequence[typing.Union[GrantDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    lifecycle_rule: typing.Optional[typing.Sequence[typing.Union[LifecycleRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    logging: typing.Optional[typing.Sequence[typing.Union[LoggingDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_lock_configuration: typing.Optional[typing.Sequence[typing.Union[ObjectLockConfigurationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Sequence[typing.Union[ReplicationConfigurationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_payer: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Sequence[typing.Union[ServerSideEncryptionConfigurationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags_all: typing.Optional[typing.Sequence[typing.Union[TagsAllDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    versioning: typing.Optional[typing.Sequence[typing.Union[VersioningDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website: typing.Optional[typing.Sequence[typing.Union[WebsiteDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website_domain: typing.Optional[builtins.str] = None,
    website_endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ec3b467b8528e425c79a45917311fb38f517d5ea550a936e9a67b9ad6dfbf1(
    *,
    allowed_methods: typing.Sequence[builtins.str],
    allowed_origins: typing.Sequence[builtins.str],
    allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_age_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a62f05d0de8431cc72998899157fb3ce5bf32cfa8833e0eae2f13f238de491(
    *,
    bucket: builtins.str,
    access_control_translation: typing.Optional[typing.Sequence[typing.Union[AccessControlTranslationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    account_id: typing.Optional[builtins.str] = None,
    replica_kms_key_id: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82be041aebf5f7b95b960c993fc745aa34a7513cd1dafb545463355e3c25dca(
    *,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
    expired_object_delete_marker: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d39e375c5e02ad1a787ef993b7c63f3035edde4b09a8f00a52fa4b0a4af3e50(
    *,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition3, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3080b05b73b5808a5c96e0010aead6e9f23f7959c3a6b1a5e327256844a96ab6(
    *,
    permissions: typing.Sequence[builtins.str],
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6fe7ad1055a4f6fde14e0917d1cc4ee549ab5bd4c7919d5de36a953dc2324a1(
    *,
    enabled: builtins.bool,
    abort_incomplete_multipart_upload_days: typing.Optional[jsii.Number] = None,
    expiration: typing.Optional[typing.Sequence[typing.Union[ExpirationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    id: typing.Optional[builtins.str] = None,
    noncurrent_version_expiration: typing.Optional[typing.Sequence[typing.Union[NoncurrentVersionExpirationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    noncurrent_version_transition: typing.Optional[typing.Sequence[typing.Union[NoncurrentVersionTransitionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition2, typing.Dict[builtins.str, typing.Any]]]] = None,
    transition: typing.Optional[typing.Sequence[typing.Union[TransitionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb740eab09c35ace7966c437e9b1585c2c7ab81fa96031167850a5218e6287bd(
    *,
    target_bucket: builtins.str,
    target_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2759c99240bc080c7ca57ad66d803fec526af1914b92f698911e5b044d3101d1(
    *,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f6b948317d1283320c8c27bfb5ab01c8b3f4df2883452f7251661fa7ecc8d6(
    *,
    storage_class: builtins.str,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1813fa96166b001dac6f50ce4963fefa41fc058b871b0047b6f35d05448db9ae(
    *,
    object_lock_enabled: builtins.str,
    rule: typing.Optional[typing.Sequence[typing.Union[RuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b76a80f0e92ae37188d7f060767e43c033ae9449235c751096fbf95073655cf(
    *,
    role: builtins.str,
    rules: typing.Optional[typing.Sequence[typing.Union[RulesDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__275b0fd6e691b88b46b8d3f3e3455731ef42896b606dcd2520719482b4cfdcf8(
    *,
    apply_server_side_encryption_by_default: typing.Optional[typing.Sequence[typing.Union[ApplyServerSideEncryptionByDefaultDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    bucket_key_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a5ac1d7a81dc1fa681922bc4beb9611e98e87be6314b8167d6e3397df6aa019(
    *,
    status: builtins.str,
    destination: typing.Optional[typing.Sequence[typing.Union[DestinationDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    filter: typing.Optional[typing.Sequence[typing.Union[FilterDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    id: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    source_selection_criteria: typing.Optional[typing.Sequence[typing.Union[SourceSelectionCriteriaDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c03d4fb728fc8154f77370d1f0bf3f27a37470a07501ac48dc0d31e7c8a009(
    *,
    rule: typing.Optional[typing.Sequence[typing.Union[RuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b32f60e78fa970408ba13f31e89bdee443545552e321c414a0a1dea930e0ce(
    *,
    sse_kms_encrypted_objects: typing.Optional[typing.Sequence[typing.Union[SseKmsEncryptedObjectsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d0b23a67697ab5932e7afbfb52265a4d83c49a3d56d08a61f34a38662891d03(
    *,
    enabled: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab08580cba929d56796d7708c087a95a21efbcdcd09c315dedca72d20ee8ab4c(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cef74744791540923f61b4cea357d27ff88f60371d9bb897f99fca3c970d9c78(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54da8dbb3cf3ba4879ff205340f4d126bd6fc559675a459359eb444b8be49708(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd00453294c1d2efe5eef6b77ec2d6016ce5a16963937edb487c3e4e4b543073(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd28f6e410dfcd19372c9dd6084b4e8f1f1f3b616ef8cb8a8777aebf3d8cba1(
    *,
    storage_class: builtins.str,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d5e9cb68c3d034bd4cb6866083850ff677db163514799e01a5a7945354ed65(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    mfa_delete: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df53e4823ef3f82500bbba89066ff313ce943656ed6bcba5e7a4b1f4b91103c(
    *,
    error_document: typing.Optional[builtins.str] = None,
    index_document: typing.Optional[builtins.str] = None,
    redirect_all_requests_to: typing.Optional[builtins.str] = None,
    routing_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

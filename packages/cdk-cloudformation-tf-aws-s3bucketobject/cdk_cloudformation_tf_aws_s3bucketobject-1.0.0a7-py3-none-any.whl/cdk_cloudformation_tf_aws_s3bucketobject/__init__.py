'''
# tf-aws-s3bucketobject

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::AWS::S3BucketObject` v1.0.0.

## Description

Provides a S3 bucket object resource.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3BucketObject/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::AWS::S3BucketObject \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-AWS-S3BucketObject \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::AWS::S3BucketObject`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-aws-s3bucketobject+v1.0.0).
* Issues related to `TF::AWS::S3BucketObject` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3BucketObject/docs/README.md).

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


class CfnS3BucketObject(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-aws-s3bucketobject.CfnS3BucketObject",
):
    '''A CloudFormation ``TF::AWS::S3BucketObject``.

    :cloudformationResource: TF::AWS::S3BucketObject
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket: builtins.str,
        key: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        bucket_key_enabled: typing.Optional[builtins.bool] = None,
        cache_control: typing.Optional[builtins.str] = None,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        etag: typing.Optional[builtins.str] = None,
        force_destroy: typing.Optional[builtins.bool] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Sequence[typing.Union["MetadataDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_lock_legal_hold_status: typing.Optional[builtins.str] = None,
        object_lock_mode: typing.Optional[builtins.str] = None,
        object_lock_retain_until_date: typing.Optional[builtins.str] = None,
        server_side_encryption: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags_all: typing.Optional[typing.Sequence[typing.Union["TagsAllDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website_redirect: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::AWS::S3BucketObject``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bucket: The name of the bucket to put the file in. Alternatively, an `S3 access point <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html>`_ ARN can be specified.
        :param key: The name of the object once it is in the bucket.
        :param acl: The `canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ to apply. Valid values are ``private``, ``public-read``, ``public-read-write``, ``aws-exec-read``, ``authenticated-read``, ``bucket-owner-read``, and ``bucket-owner-full-control``. Defaults to ``private``. Default: private`.
        :param bucket_key_enabled: Whether or not to use `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html>`_ for SSE-KMS.
        :param cache_control: Specifies caching behavior along the request/reply chain Read `w3c cache_control <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`_ for further details.
        :param content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
        :param content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the ``gzipbase64`` function with small text strings. For larger objects, use ``source`` to stream the content from a disk file.
        :param content_disposition: Specifies presentational information for the object. Read `w3c content_disposition <http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1>`_ for further information.
        :param content_encoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read `w3c content encoding <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11>`_ for further information.
        :param content_language: The language the content is in e.g. en-US or en-GB.
        :param content_type: A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
        :param etag: Used to trigger updates. The only meaningful value is ``${filemd5("path/to/file")}`` (Terraform 0.11.12 or later) or ``${md5(file("path/to/file"))}`` (Terraform 0.11.11 or earlier). This attribute is not compatible with KMS encryption, ``kms_key_id`` or ``server_side_encryption = "aws:kms"``.
        :param force_destroy: Allow the object to be deleted by removing any legal hold on any object version. Default is ``false``. This value should be set to ``true`` only if the bucket has S3 object lock enabled. Default: false``. This value should be set to ``true` only if the bucket has S3 object lock enabled.
        :param kms_key_id: Amazon Resource Name (ARN) of the KMS Key to use for object encryption. If the S3 Bucket has server-side encryption enabled, that value will automatically be used. If referencing the ``aws_kms_key`` resource, use the ``arn`` attribute. If referencing the ``aws_kms_alias`` data source or resource, use the ``target_key_arn`` attribute. Terraform will only perform drift detection if a configuration value is provided.
        :param metadata: A map of keys/values to provision metadata (will be automatically prefixed by ``x-amz-meta-``, note that only lowercase label are currently supported by the AWS Go API).
        :param object_lock_legal_hold_status: The `legal hold <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds>`_ status that you want to apply to the specified object. Valid values are ``ON`` and ``OFF``.
        :param object_lock_mode: The object lock `retention mode <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes>`_ that you want to apply to this object. Valid values are ``GOVERNANCE`` and ``COMPLIANCE``.
        :param object_lock_retain_until_date: The date and time, in `RFC3339 format <https://tools.ietf.org/html/rfc3339#section-5.8>`_, when this object's object lock will `expire <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-periods>`_.
        :param server_side_encryption: Specifies server-side encryption of the object in S3. Valid values are "``AES256``" and "``aws:kms``".
        :param source: The path to a file that will be read and uploaded as raw bytes for the object content.
        :param storage_class: Specifies the desired `Storage Class <http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>`_ for the object. Can be either "``STANDARD``", "``REDUCED_REDUNDANCY``", "``ONEZONE_IA``", "``INTELLIGENT_TIERING``", "``GLACIER``", "``DEEP_ARCHIVE``", or "``STANDARD_IA``". Defaults to "``STANDARD``". Default: STANDARD`".
        :param tags: A map of tags to assign to the object. If configured with a provider ```default_tags`` configuration block </docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 
        :param website_redirect: Specifies a target URL for `website redirect <http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40603bea667b00facb7527351ce4a4f44a4f96f3e3b4300928713b71abb3587b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnS3BucketObjectProps(
            bucket=bucket,
            key=key,
            acl=acl,
            bucket_key_enabled=bucket_key_enabled,
            cache_control=cache_control,
            content=content,
            content_base64=content_base64,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            etag=etag,
            force_destroy=force_destroy,
            kms_key_id=kms_key_id,
            metadata=metadata,
            object_lock_legal_hold_status=object_lock_legal_hold_status,
            object_lock_mode=object_lock_mode,
            object_lock_retain_until_date=object_lock_retain_until_date,
            server_side_encryption=server_side_encryption,
            source=source,
            storage_class=storage_class,
            tags=tags,
            tags_all=tags_all,
            website_redirect=website_redirect,
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
        '''Attribute ``TF::AWS::S3BucketObject.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3BucketObject.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''Attribute ``TF::AWS::S3BucketObject.VersionId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnS3BucketObjectProps":
        '''Resource props.'''
        return typing.cast("CfnS3BucketObjectProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucketobject.CfnS3BucketObjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "key": "key",
        "acl": "acl",
        "bucket_key_enabled": "bucketKeyEnabled",
        "cache_control": "cacheControl",
        "content": "content",
        "content_base64": "contentBase64",
        "content_disposition": "contentDisposition",
        "content_encoding": "contentEncoding",
        "content_language": "contentLanguage",
        "content_type": "contentType",
        "etag": "etag",
        "force_destroy": "forceDestroy",
        "kms_key_id": "kmsKeyId",
        "metadata": "metadata",
        "object_lock_legal_hold_status": "objectLockLegalHoldStatus",
        "object_lock_mode": "objectLockMode",
        "object_lock_retain_until_date": "objectLockRetainUntilDate",
        "server_side_encryption": "serverSideEncryption",
        "source": "source",
        "storage_class": "storageClass",
        "tags": "tags",
        "tags_all": "tagsAll",
        "website_redirect": "websiteRedirect",
    },
)
class CfnS3BucketObjectProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        key: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        bucket_key_enabled: typing.Optional[builtins.bool] = None,
        cache_control: typing.Optional[builtins.str] = None,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        etag: typing.Optional[builtins.str] = None,
        force_destroy: typing.Optional[builtins.bool] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Sequence[typing.Union["MetadataDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_lock_legal_hold_status: typing.Optional[builtins.str] = None,
        object_lock_mode: typing.Optional[builtins.str] = None,
        object_lock_retain_until_date: typing.Optional[builtins.str] = None,
        server_side_encryption: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["TagsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags_all: typing.Optional[typing.Sequence[typing.Union["TagsAllDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website_redirect: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Provides a S3 bucket object resource.

        :param bucket: The name of the bucket to put the file in. Alternatively, an `S3 access point <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html>`_ ARN can be specified.
        :param key: The name of the object once it is in the bucket.
        :param acl: The `canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ to apply. Valid values are ``private``, ``public-read``, ``public-read-write``, ``aws-exec-read``, ``authenticated-read``, ``bucket-owner-read``, and ``bucket-owner-full-control``. Defaults to ``private``. Default: private`.
        :param bucket_key_enabled: Whether or not to use `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html>`_ for SSE-KMS.
        :param cache_control: Specifies caching behavior along the request/reply chain Read `w3c cache_control <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`_ for further details.
        :param content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
        :param content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the ``gzipbase64`` function with small text strings. For larger objects, use ``source`` to stream the content from a disk file.
        :param content_disposition: Specifies presentational information for the object. Read `w3c content_disposition <http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1>`_ for further information.
        :param content_encoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read `w3c content encoding <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11>`_ for further information.
        :param content_language: The language the content is in e.g. en-US or en-GB.
        :param content_type: A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
        :param etag: Used to trigger updates. The only meaningful value is ``${filemd5("path/to/file")}`` (Terraform 0.11.12 or later) or ``${md5(file("path/to/file"))}`` (Terraform 0.11.11 or earlier). This attribute is not compatible with KMS encryption, ``kms_key_id`` or ``server_side_encryption = "aws:kms"``.
        :param force_destroy: Allow the object to be deleted by removing any legal hold on any object version. Default is ``false``. This value should be set to ``true`` only if the bucket has S3 object lock enabled. Default: false``. This value should be set to ``true` only if the bucket has S3 object lock enabled.
        :param kms_key_id: Amazon Resource Name (ARN) of the KMS Key to use for object encryption. If the S3 Bucket has server-side encryption enabled, that value will automatically be used. If referencing the ``aws_kms_key`` resource, use the ``arn`` attribute. If referencing the ``aws_kms_alias`` data source or resource, use the ``target_key_arn`` attribute. Terraform will only perform drift detection if a configuration value is provided.
        :param metadata: A map of keys/values to provision metadata (will be automatically prefixed by ``x-amz-meta-``, note that only lowercase label are currently supported by the AWS Go API).
        :param object_lock_legal_hold_status: The `legal hold <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds>`_ status that you want to apply to the specified object. Valid values are ``ON`` and ``OFF``.
        :param object_lock_mode: The object lock `retention mode <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes>`_ that you want to apply to this object. Valid values are ``GOVERNANCE`` and ``COMPLIANCE``.
        :param object_lock_retain_until_date: The date and time, in `RFC3339 format <https://tools.ietf.org/html/rfc3339#section-5.8>`_, when this object's object lock will `expire <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-periods>`_.
        :param server_side_encryption: Specifies server-side encryption of the object in S3. Valid values are "``AES256``" and "``aws:kms``".
        :param source: The path to a file that will be read and uploaded as raw bytes for the object content.
        :param storage_class: Specifies the desired `Storage Class <http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>`_ for the object. Can be either "``STANDARD``", "``REDUCED_REDUNDANCY``", "``ONEZONE_IA``", "``INTELLIGENT_TIERING``", "``GLACIER``", "``DEEP_ARCHIVE``", or "``STANDARD_IA``". Defaults to "``STANDARD``". Default: STANDARD`".
        :param tags: A map of tags to assign to the object. If configured with a provider ```default_tags`` configuration block </docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 
        :param website_redirect: Specifies a target URL for `website redirect <http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html>`_.

        :schema: CfnS3BucketObjectProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367e5512166d29d0cbc04b3e83e9675dea40e5a3db0b0a48309aec39cb63e552)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument bucket_key_enabled", value=bucket_key_enabled, expected_type=type_hints["bucket_key_enabled"])
            check_type(argname="argument cache_control", value=cache_control, expected_type=type_hints["cache_control"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_base64", value=content_base64, expected_type=type_hints["content_base64"])
            check_type(argname="argument content_disposition", value=content_disposition, expected_type=type_hints["content_disposition"])
            check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
            check_type(argname="argument content_language", value=content_language, expected_type=type_hints["content_language"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument object_lock_legal_hold_status", value=object_lock_legal_hold_status, expected_type=type_hints["object_lock_legal_hold_status"])
            check_type(argname="argument object_lock_mode", value=object_lock_mode, expected_type=type_hints["object_lock_mode"])
            check_type(argname="argument object_lock_retain_until_date", value=object_lock_retain_until_date, expected_type=type_hints["object_lock_retain_until_date"])
            check_type(argname="argument server_side_encryption", value=server_side_encryption, expected_type=type_hints["server_side_encryption"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument website_redirect", value=website_redirect, expected_type=type_hints["website_redirect"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }
        if acl is not None:
            self._values["acl"] = acl
        if bucket_key_enabled is not None:
            self._values["bucket_key_enabled"] = bucket_key_enabled
        if cache_control is not None:
            self._values["cache_control"] = cache_control
        if content is not None:
            self._values["content"] = content
        if content_base64 is not None:
            self._values["content_base64"] = content_base64
        if content_disposition is not None:
            self._values["content_disposition"] = content_disposition
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding
        if content_language is not None:
            self._values["content_language"] = content_language
        if content_type is not None:
            self._values["content_type"] = content_type
        if etag is not None:
            self._values["etag"] = etag
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if metadata is not None:
            self._values["metadata"] = metadata
        if object_lock_legal_hold_status is not None:
            self._values["object_lock_legal_hold_status"] = object_lock_legal_hold_status
        if object_lock_mode is not None:
            self._values["object_lock_mode"] = object_lock_mode
        if object_lock_retain_until_date is not None:
            self._values["object_lock_retain_until_date"] = object_lock_retain_until_date
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if source is not None:
            self._values["source"] = source
        if storage_class is not None:
            self._values["storage_class"] = storage_class
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if website_redirect is not None:
            self._values["website_redirect"] = website_redirect

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the bucket to put the file in.

        Alternatively, an `S3 access point <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html>`_ ARN can be specified.

        :schema: CfnS3BucketObjectProps#Bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''The name of the object once it is in the bucket.

        :schema: CfnS3BucketObjectProps#Key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''The `canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ to apply. Valid values are ``private``, ``public-read``, ``public-read-write``, ``aws-exec-read``, ``authenticated-read``, ``bucket-owner-read``, and ``bucket-owner-full-control``. Defaults to ``private``.

        :default: private`.

        :schema: CfnS3BucketObjectProps#Acl
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_key_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to use `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html>`_ for SSE-KMS.

        :schema: CfnS3BucketObjectProps#BucketKeyEnabled
        '''
        result = self._values.get("bucket_key_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cache_control(self) -> typing.Optional[builtins.str]:
        '''Specifies caching behavior along the request/reply chain Read `w3c cache_control <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`_ for further details.

        :schema: CfnS3BucketObjectProps#CacheControl
        '''
        result = self._values.get("cache_control")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

        :schema: CfnS3BucketObjectProps#Content
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_base64(self) -> typing.Optional[builtins.str]:
        '''Base64-encoded data that will be decoded and uploaded as raw bytes for the object content.

        This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the ``gzipbase64`` function with small text strings. For larger objects, use ``source`` to stream the content from a disk file.

        :schema: CfnS3BucketObjectProps#ContentBase64
        '''
        result = self._values.get("content_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies presentational information for the object.

        Read `w3c content_disposition <http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1>`_ for further information.

        :schema: CfnS3BucketObjectProps#ContentDisposition
        '''
        result = self._values.get("content_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

        Read `w3c content encoding <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11>`_ for further information.

        :schema: CfnS3BucketObjectProps#ContentEncoding
        '''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_language(self) -> typing.Optional[builtins.str]:
        '''The language the content is in e.g. en-US or en-GB.

        :schema: CfnS3BucketObjectProps#ContentLanguage
        '''
        result = self._values.get("content_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

        :schema: CfnS3BucketObjectProps#ContentType
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def etag(self) -> typing.Optional[builtins.str]:
        '''Used to trigger updates.

        The only meaningful value is ``${filemd5("path/to/file")}`` (Terraform 0.11.12 or later) or ``${md5(file("path/to/file"))}`` (Terraform 0.11.11 or earlier).
        This attribute is not compatible with KMS encryption, ``kms_key_id`` or ``server_side_encryption = "aws:kms"``.

        :schema: CfnS3BucketObjectProps#Etag
        '''
        result = self._values.get("etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_destroy(self) -> typing.Optional[builtins.bool]:
        '''Allow the object to be deleted by removing any legal hold on any object version.

        Default is ``false``. This value should be set to ``true`` only if the bucket has S3 object lock enabled.

        :default: false``. This value should be set to ``true` only if the bucket has S3 object lock enabled.

        :schema: CfnS3BucketObjectProps#ForceDestroy
        '''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) of the KMS Key to use for object encryption.

        If the S3 Bucket has server-side encryption enabled, that value will automatically be used. If referencing the
        ``aws_kms_key`` resource, use the ``arn`` attribute. If referencing the ``aws_kms_alias`` data source or resource, use the ``target_key_arn`` attribute. Terraform will only perform drift detection if a configuration value
        is provided.

        :schema: CfnS3BucketObjectProps#KmsKeyId
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List["MetadataDefinition"]]:
        '''A map of keys/values to provision metadata (will be automatically prefixed by ``x-amz-meta-``, note that only lowercase label are currently supported by the AWS Go API).

        :schema: CfnS3BucketObjectProps#Metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List["MetadataDefinition"]], result)

    @builtins.property
    def object_lock_legal_hold_status(self) -> typing.Optional[builtins.str]:
        '''The `legal hold <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds>`_ status that you want to apply to the specified object. Valid values are ``ON`` and ``OFF``.

        :schema: CfnS3BucketObjectProps#ObjectLockLegalHoldStatus
        '''
        result = self._values.get("object_lock_legal_hold_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_lock_mode(self) -> typing.Optional[builtins.str]:
        '''The object lock `retention mode <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes>`_ that you want to apply to this object. Valid values are ``GOVERNANCE`` and ``COMPLIANCE``.

        :schema: CfnS3BucketObjectProps#ObjectLockMode
        '''
        result = self._values.get("object_lock_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_lock_retain_until_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in `RFC3339 format <https://tools.ietf.org/html/rfc3339#section-5.8>`_, when this object's object lock will `expire <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-periods>`_.

        :schema: CfnS3BucketObjectProps#ObjectLockRetainUntilDate
        '''
        result = self._values.get("object_lock_retain_until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption(self) -> typing.Optional[builtins.str]:
        '''Specifies server-side encryption of the object in S3.

        Valid values are "``AES256``" and "``aws:kms``".

        :schema: CfnS3BucketObjectProps#ServerSideEncryption
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The path to a file that will be read and uploaded as raw bytes for the object content.

        :schema: CfnS3BucketObjectProps#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Specifies the desired `Storage Class <http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>`_ for the object. Can be either "``STANDARD``", "``REDUCED_REDUNDANCY``", "``ONEZONE_IA``", "``INTELLIGENT_TIERING``", "``GLACIER``", "``DEEP_ARCHIVE``", or "``STANDARD_IA``". Defaults to "``STANDARD``".

        :default: STANDARD`".

        :schema: CfnS3BucketObjectProps#StorageClass
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagsDefinition"]]:
        '''A map of tags to assign to the object.

        If configured with a provider ```default_tags`` configuration block </docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.

        :schema: CfnS3BucketObjectProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagsDefinition"]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.List["TagsAllDefinition"]]:
        '''
        :schema: CfnS3BucketObjectProps#TagsAll
        '''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.List["TagsAllDefinition"]], result)

    @builtins.property
    def website_redirect(self) -> typing.Optional[builtins.str]:
        '''Specifies a target URL for `website redirect <http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html>`_.

        :schema: CfnS3BucketObjectProps#WebsiteRedirect
        '''
        result = self._values.get("website_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketObjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucketobject.MetadataDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class MetadataDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: MetadataDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c6989b303d6569cbe3cab03114c10793dbec05bf413d1cf942c4424b1a604b)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: MetadataDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: MetadataDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetadataDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-s3bucketobject.TagsAllDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5e85a2720b95046840b292243d570b941f8568f42b39a94b99563014ea60ecc)
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
    jsii_type="@cdk-cloudformation/tf-aws-s3bucketobject.TagsDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a3936478a0a016e76fdca40529c5c30f6f36f9dc41f9c087a626b750ea5ba11)
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
    "CfnS3BucketObject",
    "CfnS3BucketObjectProps",
    "MetadataDefinition",
    "TagsAllDefinition",
    "TagsDefinition",
]

publication.publish()

def _typecheckingstub__40603bea667b00facb7527351ce4a4f44a4f96f3e3b4300928713b71abb3587b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: builtins.str,
    key: builtins.str,
    acl: typing.Optional[builtins.str] = None,
    bucket_key_enabled: typing.Optional[builtins.bool] = None,
    cache_control: typing.Optional[builtins.str] = None,
    content: typing.Optional[builtins.str] = None,
    content_base64: typing.Optional[builtins.str] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_language: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    etag: typing.Optional[builtins.str] = None,
    force_destroy: typing.Optional[builtins.bool] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Sequence[typing.Union[MetadataDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_lock_legal_hold_status: typing.Optional[builtins.str] = None,
    object_lock_mode: typing.Optional[builtins.str] = None,
    object_lock_retain_until_date: typing.Optional[builtins.str] = None,
    server_side_encryption: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags_all: typing.Optional[typing.Sequence[typing.Union[TagsAllDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website_redirect: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367e5512166d29d0cbc04b3e83e9675dea40e5a3db0b0a48309aec39cb63e552(
    *,
    bucket: builtins.str,
    key: builtins.str,
    acl: typing.Optional[builtins.str] = None,
    bucket_key_enabled: typing.Optional[builtins.bool] = None,
    cache_control: typing.Optional[builtins.str] = None,
    content: typing.Optional[builtins.str] = None,
    content_base64: typing.Optional[builtins.str] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_language: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    etag: typing.Optional[builtins.str] = None,
    force_destroy: typing.Optional[builtins.bool] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Sequence[typing.Union[MetadataDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_lock_legal_hold_status: typing.Optional[builtins.str] = None,
    object_lock_mode: typing.Optional[builtins.str] = None,
    object_lock_retain_until_date: typing.Optional[builtins.str] = None,
    server_side_encryption: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[TagsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags_all: typing.Optional[typing.Sequence[typing.Union[TagsAllDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website_redirect: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c6989b303d6569cbe3cab03114c10793dbec05bf413d1cf942c4424b1a604b(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e85a2720b95046840b292243d570b941f8568f42b39a94b99563014ea60ecc(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3936478a0a016e76fdca40529c5c30f6f36f9dc41f9c087a626b750ea5ba11(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

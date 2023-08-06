# org-test-sample-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `ORG::TEST::SAMPLE::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type ORG::TEST::SAMPLE::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name ORG::TEST::SAMPLE::MODULE \
  --publisher-id 5b05ef5a51fcbc931d63aafe139bec8a97389a21 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/5b05ef5a51fcbc931d63aafe139bec8a97389a21/ORG-TEST-SAMPLE-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `ORG::TEST::SAMPLE::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Forg-test-sample-module+v1.0.0).
* Issues related to `ORG::TEST::SAMPLE::MODULE` should be reported to the [publisher](undefined).

## License

Distributed under the Apache-2.0 License.

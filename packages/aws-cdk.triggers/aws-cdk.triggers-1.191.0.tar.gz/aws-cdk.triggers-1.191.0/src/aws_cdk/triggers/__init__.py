'''
# Triggers

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

Triggers allows you to execute code during deployments. This can be used for a
variety of use cases such as:

* Self tests: validate something after a resource/construct been provisioned
* Data priming: add initial data to resources after they are created
* Preconditions: check things such as account limits or external dependencies
  before deployment.

## Usage

The `TriggerFunction` construct will define an AWS Lambda function which is
triggered *during* deployment:

```python
import aws_cdk.aws_lambda as lambda_
import aws_cdk.triggers as triggers
from aws_cdk.core import Stack

# stack: Stack

triggers.TriggerFunction(stack, "MyTrigger",
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler",
    code=lambda_.Code.from_asset(__dirname + "/my-trigger")
)
```

In the above example, the AWS Lambda function defined in `myLambdaFunction` will
be invoked when the stack is deployed.

## Trigger Failures

If the trigger handler fails (e.g. an exception is raised), the CloudFormation
deployment will fail, as if a resource failed to provision. This makes it easy
to implement "self tests" via triggers by simply making a set of assertions on
some provisioned infrastructure.

## Order of Execution

By default, a trigger will be executed by CloudFormation after the associated
handler is provisioned. This means that if the handler takes an implicit
dependency on other resources (e.g. via environment variables), those resources
will be provisioned *before* the trigger is executed.

In most cases, implicit ordering should be sufficient, but you can also use
`executeAfter` and `executeBefore` to control the order of execution.

The following example defines the following order: `(hello, world) => myTrigger => goodbye`.
The resources under `hello` and `world` will be provisioned in
parallel, and then the trigger `myTrigger` will be executed. Only then the
resources under `goodbye` will be provisioned:

```python
from constructs import Construct, Node
import aws_cdk.triggers as triggers

# my_trigger: triggers.Trigger
# hello: Construct
# world: Construct
# goodbye: Construct

my_trigger.execute_after(hello, world)
my_trigger.execute_before(goodbye)
```

Note that `hello` and `world` are construct *scopes*. This means that they can
be specific resources (such as an `s3.Bucket` object) or groups of resources
composed together into constructs.

## Re-execution of Triggers

By default, `executeOnHandlerChange` is enabled. This implies that the trigger
is re-executed every time the handler function code or configuration changes. If
this option is disabled, the trigger will be executed only once upon first
deployment.

In the future we will consider adding support for additional re-execution modes:

* `executeOnEveryDeployment: boolean` - re-executes every time the stack is
  deployed (add random "salt" during synthesis).
* `executeOnResourceChange: Construct[]` - re-executes when one of the resources
  under the specified scopes has changed (add the hash the CloudFormation
  resource specs).
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

import aws_cdk.aws_codeguruprofiler as _aws_cdk_aws_codeguruprofiler_5a603484
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_67de8e8d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_940a1ce0
import aws_cdk.aws_kms as _aws_cdk_aws_kms_e491a92b
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_5443dbc3
import aws_cdk.aws_logs as _aws_cdk_aws_logs_6c4320fb
import aws_cdk.aws_sns as _aws_cdk_aws_sns_889c7272
import aws_cdk.aws_sqs as _aws_cdk_aws_sqs_48bffef9
import aws_cdk.core as _aws_cdk_core_f4b25747
import constructs as _constructs_77d1e7e8


@jsii.interface(jsii_type="@aws-cdk/triggers.ITrigger")
class ITrigger(_aws_cdk_core_f4b25747.IConstruct, typing_extensions.Protocol):
    '''Interface for triggers.'''

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: A list of construct scopes which this trigger will depend on.
        '''
        ...

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: A list of construct scopes which will take a dependency on this trigger.
        '''
        ...


class _ITriggerProxy(
    jsii.proxy_for(_aws_cdk_core_f4b25747.IConstruct), # type: ignore[misc]
):
    '''Interface for triggers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/triggers.ITrigger"

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: A list of construct scopes which this trigger will depend on.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772b0ebcd0ea24ec4d9e35a4a75156d3933ed8cd336d1137fd9a196ee0b9fabf)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeAfter", [*scopes]))

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: A list of construct scopes which will take a dependency on this trigger.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4194716a50693fe250532d8b28ac047c5b02c9345dac2b8b884e0bfd3881d175)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeBefore", [*scopes]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrigger).__jsii_proxy_class__ = lambda : _ITriggerProxy


@jsii.implements(ITrigger)
class Trigger(
    _aws_cdk_core_f4b25747.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/triggers.Trigger",
):
    '''Triggers an AWS Lambda function during deployment.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lambda as lambda_
        import aws_cdk.triggers as triggers
        import constructs as constructs
        
        # construct: constructs.Construct
        # function_: lambda.Function
        
        trigger = triggers.Trigger(self, "MyTrigger",
            handler=function_,
        
            # the properties below are optional
            execute_after=[construct],
            execute_before=[construct],
            execute_on_handler_change=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        handler: _aws_cdk_aws_lambda_5443dbc3.Function,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param handler: The AWS Lambda function of the handler to execute.
        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd0d8a01ba67c8ad399ed34fac5c3bd78f8e8e0382dcdffee695fffa3d6bd34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TriggerProps(
            handler=handler,
            execute_after=execute_after,
            execute_before=execute_before,
            execute_on_handler_change=execute_on_handler_change,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f322d440f00090e13b2d4a8f7e6c63b0b5f2731b527bb5b81acbc7a885c6fb28)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeAfter", [*scopes]))

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e68b2e721de8b0904e8334549f2edc2e7983fc2350c5f4bcfb8b85147b8b62e3)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeBefore", [*scopes]))


@jsii.implements(ITrigger)
class TriggerFunction(
    _aws_cdk_aws_lambda_5443dbc3.Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/triggers.TriggerFunction",
):
    '''Invokes an AWS Lambda function during deployment.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        import aws_cdk.triggers as triggers
        from aws_cdk.core import Stack
        
        # stack: Stack
        
        triggers.TriggerFunction(stack, "MyTrigger",
            runtime=lambda_.Runtime.NODEJS_14_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(__dirname + "/my-trigger")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        code: _aws_cdk_aws_lambda_5443dbc3.Code,
        handler: builtins.str,
        runtime: _aws_cdk_aws_lambda_5443dbc3.Runtime,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Architecture] = None,
        architectures: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.Architecture]] = None,
        code_signing_config: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_48bffef9.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
        ephemeral_storage_size: typing.Optional[_aws_cdk_core_f4b25747.Size] = None,
        events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.IEventSource]] = None,
        filesystem: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_940a1ce0.PolicyStatement]] = None,
        insights_version: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LambdaInsightsVersion] = None,
        layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.ILayerVersion]] = None,
        log_retention: typing.Optional[_aws_cdk_aws_logs_6c4320fb.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_5a603484.IProfilingGroup] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
        security_group: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]] = None,
        timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        tracing: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Tracing] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_67de8e8d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        max_event_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        on_failure: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
        on_success: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.
        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param architectures: (deprecated) DEPRECATED. Default: [Architecture.X86_64]
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a3e8d58049004daa6ec38db57bed4d3d96880fe985b0b56ca84ba3c983fb9f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TriggerFunctionProps(
            code=code,
            handler=handler,
            runtime=runtime,
            execute_after=execute_after,
            execute_before=execute_before,
            execute_on_handler_change=execute_on_handler_change,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            architecture=architecture,
            architectures=architectures,
            code_signing_config=code_signing_config,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            dead_letter_topic=dead_letter_topic,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            ephemeral_storage_size=ephemeral_storage_size,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            insights_version=insights_version,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            security_group=security_group,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a489373d521db5b5d65fc6173734c6424613802a7314d33a83ca501d83af2e36)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeAfter", [*scopes]))

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__396a111453b069c21785a0a902b59069267a4bd7ef8bcfa11f28536d6f813b38)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeBefore", [*scopes]))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(self) -> Trigger:
        '''The underlying trigger resource.'''
        return typing.cast(Trigger, jsii.get(self, "trigger"))


@jsii.enum(jsii_type="@aws-cdk/triggers.TriggerInvalidation")
class TriggerInvalidation(enum.Enum):
    '''Determines.'''

    HANDLER_CHANGE = "HANDLER_CHANGE"
    '''The trigger will be executed every time the handler (or its configuration) changes.

    This is implemented by associated the trigger with the ``currentVersion``
    of the AWS Lambda function, which gets recreated every time the handler changes.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/triggers.TriggerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "execute_after": "executeAfter",
        "execute_before": "executeBefore",
        "execute_on_handler_change": "executeOnHandlerChange",
    },
)
class TriggerOptions:
    def __init__(
        self,
        *,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for ``Trigger``.

        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.triggers as triggers
            import constructs as constructs
            
            # construct: constructs.Construct
            
            trigger_options = triggers.TriggerOptions(
                execute_after=[construct],
                execute_before=[construct],
                execute_on_handler_change=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7df9e9a21404a8d6ae775fc231a73f5639274ce4e3c87f9cedfc98e103551c)
            check_type(argname="argument execute_after", value=execute_after, expected_type=type_hints["execute_after"])
            check_type(argname="argument execute_before", value=execute_before, expected_type=type_hints["execute_before"])
            check_type(argname="argument execute_on_handler_change", value=execute_on_handler_change, expected_type=type_hints["execute_on_handler_change"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if execute_after is not None:
            self._values["execute_after"] = execute_after
        if execute_before is not None:
            self._values["execute_before"] = execute_before
        if execute_on_handler_change is not None:
            self._values["execute_on_handler_change"] = execute_on_handler_change

    @builtins.property
    def execute_after(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned.

        You can also use ``trigger.executeAfter()`` to add additional dependencies.

        :default: []
        '''
        result = self._values.get("execute_after")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_before(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        You can also use ``trigger.executeBefore()`` to add additional dependants.

        :default: []
        '''
        result = self._values.get("execute_before")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_on_handler_change(self) -> typing.Optional[builtins.bool]:
        '''Re-executes the trigger every time the handler changes.

        This implies that the trigger is associated with the ``currentVersion`` of
        the handler, which gets recreated every time the handler or its
        configuration is updated.

        :default: true
        '''
        result = self._values.get("execute_on_handler_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/triggers.TriggerProps",
    jsii_struct_bases=[TriggerOptions],
    name_mapping={
        "execute_after": "executeAfter",
        "execute_before": "executeBefore",
        "execute_on_handler_change": "executeOnHandlerChange",
        "handler": "handler",
    },
)
class TriggerProps(TriggerOptions):
    def __init__(
        self,
        *,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
        handler: _aws_cdk_aws_lambda_5443dbc3.Function,
    ) -> None:
        '''Props for ``Trigger``.

        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true
        :param handler: The AWS Lambda function of the handler to execute.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lambda as lambda_
            import aws_cdk.triggers as triggers
            import constructs as constructs
            
            # construct: constructs.Construct
            # function_: lambda.Function
            
            trigger_props = triggers.TriggerProps(
                handler=function_,
            
                # the properties below are optional
                execute_after=[construct],
                execute_before=[construct],
                execute_on_handler_change=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8742d0cb8f02f1cc73d5b7228b14f678f03640c42cc88b60451a32ca4bd248)
            check_type(argname="argument execute_after", value=execute_after, expected_type=type_hints["execute_after"])
            check_type(argname="argument execute_before", value=execute_before, expected_type=type_hints["execute_before"])
            check_type(argname="argument execute_on_handler_change", value=execute_on_handler_change, expected_type=type_hints["execute_on_handler_change"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "handler": handler,
        }
        if execute_after is not None:
            self._values["execute_after"] = execute_after
        if execute_before is not None:
            self._values["execute_before"] = execute_before
        if execute_on_handler_change is not None:
            self._values["execute_on_handler_change"] = execute_on_handler_change

    @builtins.property
    def execute_after(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned.

        You can also use ``trigger.executeAfter()`` to add additional dependencies.

        :default: []
        '''
        result = self._values.get("execute_after")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_before(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        You can also use ``trigger.executeBefore()`` to add additional dependants.

        :default: []
        '''
        result = self._values.get("execute_before")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_on_handler_change(self) -> typing.Optional[builtins.bool]:
        '''Re-executes the trigger every time the handler changes.

        This implies that the trigger is associated with the ``currentVersion`` of
        the handler, which gets recreated every time the handler or its
        configuration is updated.

        :default: true
        '''
        result = self._values.get("execute_on_handler_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def handler(self) -> _aws_cdk_aws_lambda_5443dbc3.Function:
        '''The AWS Lambda function of the handler to execute.'''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(_aws_cdk_aws_lambda_5443dbc3.Function, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/triggers.TriggerFunctionProps",
    jsii_struct_bases=[_aws_cdk_aws_lambda_5443dbc3.FunctionProps, TriggerOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "architecture": "architecture",
        "architectures": "architectures",
        "code_signing_config": "codeSigningConfig",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "dead_letter_topic": "deadLetterTopic",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "insights_version": "insightsVersion",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "code": "code",
        "handler": "handler",
        "runtime": "runtime",
        "execute_after": "executeAfter",
        "execute_before": "executeBefore",
        "execute_on_handler_change": "executeOnHandlerChange",
    },
)
class TriggerFunctionProps(_aws_cdk_aws_lambda_5443dbc3.FunctionProps, TriggerOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        on_failure: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
        on_success: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Architecture] = None,
        architectures: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.Architecture]] = None,
        code_signing_config: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_48bffef9.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
        ephemeral_storage_size: typing.Optional[_aws_cdk_core_f4b25747.Size] = None,
        events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.IEventSource]] = None,
        filesystem: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_940a1ce0.PolicyStatement]] = None,
        insights_version: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LambdaInsightsVersion] = None,
        layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.ILayerVersion]] = None,
        log_retention: typing.Optional[_aws_cdk_aws_logs_6c4320fb.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_5a603484.IProfilingGroup] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
        security_group: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]] = None,
        timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        tracing: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Tracing] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_67de8e8d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        code: _aws_cdk_aws_lambda_5443dbc3.Code,
        handler: builtins.str,
        runtime: _aws_cdk_aws_lambda_5443dbc3.Runtime,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Props for ``InvokeFunction``.

        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param architectures: (deprecated) DEPRECATED. Default: [Architecture.X86_64]
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.
        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            import aws_cdk.triggers as triggers
            from aws_cdk.core import Stack
            
            # stack: Stack
            
            triggers.TriggerFunction(stack, "MyTrigger",
                runtime=lambda_.Runtime.NODEJS_14_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(__dirname + "/my-trigger")
            )
        '''
        if isinstance(current_version_options, dict):
            current_version_options = _aws_cdk_aws_lambda_5443dbc3.VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = _aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_67de8e8d.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8b57462558f9750acc436e66756d8e69b95369b583e3c95480a0900ba2bcd25)
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument architectures", value=architectures, expected_type=type_hints["architectures"])
            check_type(argname="argument code_signing_config", value=code_signing_config, expected_type=type_hints["code_signing_config"])
            check_type(argname="argument current_version_options", value=current_version_options, expected_type=type_hints["current_version_options"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument dead_letter_queue_enabled", value=dead_letter_queue_enabled, expected_type=type_hints["dead_letter_queue_enabled"])
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument environment_encryption", value=environment_encryption, expected_type=type_hints["environment_encryption"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument initial_policy", value=initial_policy, expected_type=type_hints["initial_policy"])
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument profiling", value=profiling, expected_type=type_hints["profiling"])
            check_type(argname="argument profiling_group", value=profiling_group, expected_type=type_hints["profiling_group"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument execute_after", value=execute_after, expected_type=type_hints["execute_after"])
            check_type(argname="argument execute_before", value=execute_before, expected_type=type_hints["execute_before"])
            check_type(argname="argument execute_on_handler_change", value=execute_on_handler_change, expected_type=type_hints["execute_on_handler_change"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code": code,
            "handler": handler,
            "runtime": runtime,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if architecture is not None:
            self._values["architecture"] = architecture
        if architectures is not None:
            self._values["architectures"] = architectures
        if code_signing_config is not None:
            self._values["code_signing_config"] = code_signing_config
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if insights_version is not None:
            self._values["insights_version"] = insights_version
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if execute_after is not None:
            self._values["execute_after"] = execute_after
        if execute_before is not None:
            self._values["execute_before"] = execute_before
        if execute_on_handler_change is not None:
            self._values["execute_on_handler_change"] = execute_on_handler_change

    @builtins.property
    def max_event_age(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def on_failure(self) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination]:
        '''The destination for failed invocations.

        :default: - no destination
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination], result)

    @builtins.property
    def on_success(self) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination]:
        '''The destination for successful invocations.

        :default: - no destination
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def architecture(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Architecture]:
        '''The system architectures compatible with this lambda function.

        :default: Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Architecture], result)

    @builtins.property
    def architectures(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_lambda_5443dbc3.Architecture]]:
        '''(deprecated) DEPRECATED.

        :default: [Architecture.X86_64]

        :deprecated: use ``architecture``

        :stability: deprecated
        '''
        result = self._values.get("architectures")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_lambda_5443dbc3.Architecture]], result)

    @builtins.property
    def code_signing_config(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.ICodeSigningConfig]:
        '''Code signing config associated with this function.

        :default: - Not Sign the Code
        '''
        result = self._values.get("code_signing_config")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.ICodeSigningConfig], result)

    @builtins.property
    def current_version_options(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.VersionOptions]:
        '''Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``
        '''
        result = self._values.get("current_version_options")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.VersionOptions], result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_aws_cdk_aws_sqs_48bffef9.IQueue]:
        '''The SQS queue to use if DLQ is enabled.

        If SNS topic is desired, specify ``deadLetterTopic`` property instead.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_aws_cdk_aws_sqs_48bffef9.IQueue], result)

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        '''
        result = self._values.get("dead_letter_queue_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic]:
        '''The SNS topic to use as a DLQ.

        Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created
        rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly.

        :default: - no SNS topic
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey]:
        '''The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        '''
        result = self._values.get("environment_encryption")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[_aws_cdk_core_f4b25747.Size]:
        '''The size of the function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Size], result)

    @builtins.property
    def events(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_lambda_5443dbc3.IEventSource]]:
        '''Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_lambda_5443dbc3.IEventSource]], result)

    @builtins.property
    def filesystem(self) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.FileSystem]:
        '''The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.FileSystem], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_policy(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_iam_940a1ce0.PolicyStatement]]:
        '''Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.
        '''
        result = self._values.get("initial_policy")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_iam_940a1ce0.PolicyStatement]], result)

    @builtins.property
    def insights_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LambdaInsightsVersion]:
        '''Specify the version of CloudWatch Lambda insights to use for monitoring.

        :default: - No Lambda Insights

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html
        '''
        result = self._values.get("insights_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LambdaInsightsVersion], result)

    @builtins.property
    def layers(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_lambda_5443dbc3.ILayerVersion]]:
        '''A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by multiple functions.

        :default: - No layers.
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_lambda_5443dbc3.ILayerVersion]], result)

    @builtins.property
    def log_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_6c4320fb.RetentionDays]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_6c4320fb.RetentionDays], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        '''Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profiling_group(
        self,
    ) -> typing.Optional[_aws_cdk_aws_codeguruprofiler_5a603484.IProfilingGroup]:
        '''Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling_group")
        return typing.cast(typing.Optional[_aws_cdk_aws_codeguruprofiler_5a603484.IProfilingGroup], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole]:
        '''Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole], result)

    @builtins.property
    def security_group(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]:
        '''(deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead.

        Only used if 'vpc' is supplied.

        Use securityGroups property instead.
        Function constructor will throw an error if both are specified.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroups prop, a dedicated security
        group will be created for this function.

        :deprecated: - This property is deprecated, use securityGroups instead

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]]:
        '''The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def tracing(self) -> typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Tracing]:
        '''Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Tracing], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_67de8e8d.IVpc]:
        '''VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.

        :default: - Function is not placed within a VPC.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_67de8e8d.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_67de8e8d.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_67de8e8d.SubnetSelection], result)

    @builtins.property
    def code(self) -> _aws_cdk_aws_lambda_5443dbc3.Code:
        '''The source code of your Lambda function.

        You can point to a file in an
        Amazon Simple Storage Service (Amazon S3) bucket or specify your source
        code as inline text.
        '''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(_aws_cdk_aws_lambda_5443dbc3.Code, result)

    @builtins.property
    def handler(self) -> builtins.str:
        '''The name of the method within your code that Lambda calls to execute your function.

        The format includes the file name. It can also include
        namespaces and other qualifiers, depending on the runtime.
        For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel.

        Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image.

        NOTE: If you specify your source code as inline text by specifying the
        ZipFile property within the Code property, specify index.function_name as
        the handler.
        '''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime(self) -> _aws_cdk_aws_lambda_5443dbc3.Runtime:
        '''The runtime environment for the Lambda function that you are uploading.

        For valid values, see the Runtime property in the AWS Lambda Developer
        Guide.

        Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.
        '''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast(_aws_cdk_aws_lambda_5443dbc3.Runtime, result)

    @builtins.property
    def execute_after(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned.

        You can also use ``trigger.executeAfter()`` to add additional dependencies.

        :default: []
        '''
        result = self._values.get("execute_after")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_before(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        You can also use ``trigger.executeBefore()`` to add additional dependants.

        :default: []
        '''
        result = self._values.get("execute_before")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_on_handler_change(self) -> typing.Optional[builtins.bool]:
        '''Re-executes the trigger every time the handler changes.

        This implies that the trigger is associated with the ``currentVersion`` of
        the handler, which gets recreated every time the handler or its
        configuration is updated.

        :default: true
        '''
        result = self._values.get("execute_on_handler_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ITrigger",
    "Trigger",
    "TriggerFunction",
    "TriggerFunctionProps",
    "TriggerInvalidation",
    "TriggerOptions",
    "TriggerProps",
]

publication.publish()

def _typecheckingstub__772b0ebcd0ea24ec4d9e35a4a75156d3933ed8cd336d1137fd9a196ee0b9fabf(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4194716a50693fe250532d8b28ac047c5b02c9345dac2b8b884e0bfd3881d175(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd0d8a01ba67c8ad399ed34fac5c3bd78f8e8e0382dcdffee695fffa3d6bd34(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    handler: _aws_cdk_aws_lambda_5443dbc3.Function,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f322d440f00090e13b2d4a8f7e6c63b0b5f2731b527bb5b81acbc7a885c6fb28(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e68b2e721de8b0904e8334549f2edc2e7983fc2350c5f4bcfb8b85147b8b62e3(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a3e8d58049004daa6ec38db57bed4d3d96880fe985b0b56ca84ba3c983fb9f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    code: _aws_cdk_aws_lambda_5443dbc3.Code,
    handler: builtins.str,
    runtime: _aws_cdk_aws_lambda_5443dbc3.Runtime,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    architecture: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Architecture] = None,
    architectures: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.Architecture]] = None,
    code_signing_config: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.ICodeSigningConfig] = None,
    current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_48bffef9.IQueue] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
    ephemeral_storage_size: typing.Optional[_aws_cdk_core_f4b25747.Size] = None,
    events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.IEventSource]] = None,
    filesystem: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.FileSystem] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_940a1ce0.PolicyStatement]] = None,
    insights_version: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LambdaInsightsVersion] = None,
    layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.ILayerVersion]] = None,
    log_retention: typing.Optional[_aws_cdk_aws_logs_6c4320fb.RetentionDays] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_5a603484.IProfilingGroup] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    security_group: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]] = None,
    timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    tracing: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Tracing] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.IVpc] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_67de8e8d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    max_event_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    on_failure: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
    on_success: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a489373d521db5b5d65fc6173734c6424613802a7314d33a83ca501d83af2e36(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396a111453b069c21785a0a902b59069267a4bd7ef8bcfa11f28536d6f813b38(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7df9e9a21404a8d6ae775fc231a73f5639274ce4e3c87f9cedfc98e103551c(
    *,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8742d0cb8f02f1cc73d5b7228b14f678f03640c42cc88b60451a32ca4bd248(
    *,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
    handler: _aws_cdk_aws_lambda_5443dbc3.Function,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8b57462558f9750acc436e66756d8e69b95369b583e3c95480a0900ba2bcd25(
    *,
    max_event_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    on_failure: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
    on_success: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.IDestination] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    architecture: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Architecture] = None,
    architectures: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.Architecture]] = None,
    code_signing_config: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.ICodeSigningConfig] = None,
    current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_48bffef9.IQueue] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
    ephemeral_storage_size: typing.Optional[_aws_cdk_core_f4b25747.Size] = None,
    events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.IEventSource]] = None,
    filesystem: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.FileSystem] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_940a1ce0.PolicyStatement]] = None,
    insights_version: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.LambdaInsightsVersion] = None,
    layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_5443dbc3.ILayerVersion]] = None,
    log_retention: typing.Optional[_aws_cdk_aws_logs_6c4320fb.RetentionDays] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_5443dbc3.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_5a603484.IProfilingGroup] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    security_group: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_67de8e8d.ISecurityGroup]] = None,
    timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    tracing: typing.Optional[_aws_cdk_aws_lambda_5443dbc3.Tracing] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_67de8e8d.IVpc] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_67de8e8d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    code: _aws_cdk_aws_lambda_5443dbc3.Code,
    handler: builtins.str,
    runtime: _aws_cdk_aws_lambda_5443dbc3.Runtime,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

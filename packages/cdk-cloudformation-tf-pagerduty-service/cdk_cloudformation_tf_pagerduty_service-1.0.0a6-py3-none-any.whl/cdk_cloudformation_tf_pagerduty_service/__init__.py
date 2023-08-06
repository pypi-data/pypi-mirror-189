'''
# tf-pagerduty-service

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::PagerDuty::Service` v1.0.0.

## Description

A [service](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services) represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/pagerduty/TF-PagerDuty-Service/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::PagerDuty::Service \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-PagerDuty-Service \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::PagerDuty::Service`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-pagerduty-service+v1.0.0).
* Issues related to `TF::PagerDuty::Service` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/pagerduty/TF-PagerDuty-Service/docs/README.md).

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
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.AtDefinition",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class AtDefinition:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param type: 

        :schema: AtDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d665b43f3ce40e4b78539ac81db107b1a0b8474c8ad46f7898a35f270bbed832)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AtDefinition#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AtDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AtDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnService(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.CfnService",
):
    '''A CloudFormation ``TF::PagerDuty::Service``.

    :cloudformationResource: TF::PagerDuty::Service
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        escalation_policy: builtins.str,
        name: builtins.str,
        acknowledgement_timeout: typing.Optional[builtins.str] = None,
        alert_creation: typing.Optional[builtins.str] = None,
        alert_grouping: typing.Optional[builtins.str] = None,
        alert_grouping_timeout: typing.Optional[jsii.Number] = None,
        auto_resolve_timeout: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        incident_urgency_rule: typing.Optional[typing.Sequence[typing.Union["IncidentUrgencyRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        scheduled_actions: typing.Optional[typing.Sequence[typing.Union["ScheduledActionsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        support_hours: typing.Optional[typing.Sequence[typing.Union["SupportHoursDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``TF::PagerDuty::Service``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param escalation_policy: The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param name: Designates either the start or the end of the scheduled action. Can be ``support_hours_start`` or ``support_hours_end``.
        :param acknowledgement_timeout: Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string. - ``escalation_policy`` - (Required) The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param alert_creation: Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param alert_grouping: Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param alert_grouping_timeout: The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param auto_resolve_timeout: Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the ``"null"`` string. - ``acknowledgement_timeout`` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string. - ``escalation_policy`` - (Required) The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param description: A human-friendly description of the service. If not set, a placeholder of "Managed by Terraform" will be set. - ``auto_resolve_timeout`` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the ``"null"`` string. - ``acknowledgement_timeout`` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string. - ``escalation_policy`` - (Required) The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param incident_urgency_rule: 
        :param scheduled_actions: 
        :param support_hours: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dac356bd9d120f3ebef9cf76e7f35ec0e19692b7331189ec217900d87005ae7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            escalation_policy=escalation_policy,
            name=name,
            acknowledgement_timeout=acknowledgement_timeout,
            alert_creation=alert_creation,
            alert_grouping=alert_grouping,
            alert_grouping_timeout=alert_grouping_timeout,
            auto_resolve_timeout=auto_resolve_timeout,
            description=description,
            incident_urgency_rule=incident_urgency_rule,
            scheduled_actions=scheduled_actions,
            support_hours=support_hours,
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
        '''Attribute ``TF::PagerDuty::Service.CreatedAt``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrHtmlUrl")
    def attr_html_url(self) -> builtins.str:
        '''Attribute ``TF::PagerDuty::Service.HtmlUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHtmlUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::PagerDuty::Service.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastIncidentTimestamp")
    def attr_last_incident_timestamp(self) -> builtins.str:
        '''Attribute ``TF::PagerDuty::Service.LastIncidentTimestamp``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastIncidentTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Attribute ``TF::PagerDuty::Service.Status``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::PagerDuty::Service.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnServiceProps":
        '''Resource props.'''
        return typing.cast("CfnServiceProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "escalation_policy": "escalationPolicy",
        "name": "name",
        "acknowledgement_timeout": "acknowledgementTimeout",
        "alert_creation": "alertCreation",
        "alert_grouping": "alertGrouping",
        "alert_grouping_timeout": "alertGroupingTimeout",
        "auto_resolve_timeout": "autoResolveTimeout",
        "description": "description",
        "incident_urgency_rule": "incidentUrgencyRule",
        "scheduled_actions": "scheduledActions",
        "support_hours": "supportHours",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        escalation_policy: builtins.str,
        name: builtins.str,
        acknowledgement_timeout: typing.Optional[builtins.str] = None,
        alert_creation: typing.Optional[builtins.str] = None,
        alert_grouping: typing.Optional[builtins.str] = None,
        alert_grouping_timeout: typing.Optional[jsii.Number] = None,
        auto_resolve_timeout: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        incident_urgency_rule: typing.Optional[typing.Sequence[typing.Union["IncidentUrgencyRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        scheduled_actions: typing.Optional[typing.Sequence[typing.Union["ScheduledActionsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        support_hours: typing.Optional[typing.Sequence[typing.Union["SupportHoursDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''A `service <https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services>`_ represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.

        :param escalation_policy: The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param name: Designates either the start or the end of the scheduled action. Can be ``support_hours_start`` or ``support_hours_end``.
        :param acknowledgement_timeout: Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string. - ``escalation_policy`` - (Required) The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param alert_creation: Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param alert_grouping: Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param alert_grouping_timeout: The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param auto_resolve_timeout: Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the ``"null"`` string. - ``acknowledgement_timeout`` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string. - ``escalation_policy`` - (Required) The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param description: A human-friendly description of the service. If not set, a placeholder of "Managed by Terraform" will be set. - ``auto_resolve_timeout`` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the ``"null"`` string. - ``acknowledgement_timeout`` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string. - ``escalation_policy`` - (Required) The escalation policy used by this service. - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended. - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan. - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.
        :param incident_urgency_rule: 
        :param scheduled_actions: 
        :param support_hours: 

        :schema: CfnServiceProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079071ee923650c59ae826665b940e8e9a180fa08ca27ea6f6a507d1f532b68b)
            check_type(argname="argument escalation_policy", value=escalation_policy, expected_type=type_hints["escalation_policy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument acknowledgement_timeout", value=acknowledgement_timeout, expected_type=type_hints["acknowledgement_timeout"])
            check_type(argname="argument alert_creation", value=alert_creation, expected_type=type_hints["alert_creation"])
            check_type(argname="argument alert_grouping", value=alert_grouping, expected_type=type_hints["alert_grouping"])
            check_type(argname="argument alert_grouping_timeout", value=alert_grouping_timeout, expected_type=type_hints["alert_grouping_timeout"])
            check_type(argname="argument auto_resolve_timeout", value=auto_resolve_timeout, expected_type=type_hints["auto_resolve_timeout"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument incident_urgency_rule", value=incident_urgency_rule, expected_type=type_hints["incident_urgency_rule"])
            check_type(argname="argument scheduled_actions", value=scheduled_actions, expected_type=type_hints["scheduled_actions"])
            check_type(argname="argument support_hours", value=support_hours, expected_type=type_hints["support_hours"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "escalation_policy": escalation_policy,
            "name": name,
        }
        if acknowledgement_timeout is not None:
            self._values["acknowledgement_timeout"] = acknowledgement_timeout
        if alert_creation is not None:
            self._values["alert_creation"] = alert_creation
        if alert_grouping is not None:
            self._values["alert_grouping"] = alert_grouping
        if alert_grouping_timeout is not None:
            self._values["alert_grouping_timeout"] = alert_grouping_timeout
        if auto_resolve_timeout is not None:
            self._values["auto_resolve_timeout"] = auto_resolve_timeout
        if description is not None:
            self._values["description"] = description
        if incident_urgency_rule is not None:
            self._values["incident_urgency_rule"] = incident_urgency_rule
        if scheduled_actions is not None:
            self._values["scheduled_actions"] = scheduled_actions
        if support_hours is not None:
            self._values["support_hours"] = support_hours

    @builtins.property
    def escalation_policy(self) -> builtins.str:
        '''The escalation policy used by this service.

        - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.
        - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
        - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#EscalationPolicy
        '''
        result = self._values.get("escalation_policy")
        assert result is not None, "Required property 'escalation_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Designates either the start or the end of the scheduled action.

        Can be ``support_hours_start`` or ``support_hours_end``.

        :schema: CfnServiceProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acknowledgement_timeout(self) -> typing.Optional[builtins.str]:
        '''Time in seconds that an incident changes to the Triggered State after being Acknowledged.

        Disabled if set to the ``"null"`` string.

        - ``escalation_policy`` - (Required) The escalation policy used by this service.
        - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.
        - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
        - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#AcknowledgementTimeout
        '''
        result = self._values.get("acknowledgement_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_creation(self) -> typing.Optional[builtins.str]:
        '''Must be one of two values.

        PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.

        - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
        - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#AlertCreation
        '''
        result = self._values.get("alert_creation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_grouping(self) -> typing.Optional[builtins.str]:
        '''Defines how alerts on this service will be automatically grouped into incidents.

        Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.

        - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#AlertGrouping
        '''
        result = self._values.get("alert_grouping")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_grouping_timeout(self) -> typing.Optional[jsii.Number]:
        '''The duration in minutes within which to automatically group incoming alerts.

        This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#AlertGroupingTimeout
        '''
        result = self._values.get("alert_grouping_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def auto_resolve_timeout(self) -> typing.Optional[builtins.str]:
        '''Time in seconds that an incident is automatically resolved if left open for that long.

        Disabled if set to the ``"null"`` string.

        - ``acknowledgement_timeout`` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string.
        - ``escalation_policy`` - (Required) The escalation policy used by this service.
        - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.
        - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
        - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#AutoResolveTimeout
        '''
        result = self._values.get("auto_resolve_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-friendly description of the service.

        If not set, a placeholder of "Managed by Terraform" will be set.

        - ``auto_resolve_timeout`` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the ``"null"`` string.
        - ``acknowledgement_timeout`` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the ``"null"`` string.
        - ``escalation_policy`` - (Required) The escalation policy used by this service.
        - ``alert_creation`` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.
        - ``alert_grouping`` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to ``time``: All alerts within a specified duration will be grouped into the same incident. This duration is set in the ``alert_grouping_timeout`` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to ``intelligent`` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
        - ``alert_grouping_timeout`` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when ``alert_grouping`` is set to ``time``. To continue grouping alerts until the incident is resolved, set this value to ``0``.

        :schema: CfnServiceProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def incident_urgency_rule(
        self,
    ) -> typing.Optional[typing.List["IncidentUrgencyRuleDefinition"]]:
        '''
        :schema: CfnServiceProps#IncidentUrgencyRule
        '''
        result = self._values.get("incident_urgency_rule")
        return typing.cast(typing.Optional[typing.List["IncidentUrgencyRuleDefinition"]], result)

    @builtins.property
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.List["ScheduledActionsDefinition"]]:
        '''
        :schema: CfnServiceProps#ScheduledActions
        '''
        result = self._values.get("scheduled_actions")
        return typing.cast(typing.Optional[typing.List["ScheduledActionsDefinition"]], result)

    @builtins.property
    def support_hours(self) -> typing.Optional[typing.List["SupportHoursDefinition"]]:
        '''
        :schema: CfnServiceProps#SupportHours
        '''
        result = self._values.get("support_hours")
        return typing.cast(typing.Optional[typing.List["SupportHoursDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.DuringSupportHoursDefinition",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "urgency": "urgency"},
)
class DuringSupportHoursDefinition:
    def __init__(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        urgency: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: 
        :param urgency: 

        :schema: DuringSupportHoursDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5ad5f61c0861b14ac8dabba78a1ae0d130bfc12d3bb63db1de046e2200afde)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument urgency", value=urgency, expected_type=type_hints["urgency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if urgency is not None:
            self._values["urgency"] = urgency

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DuringSupportHoursDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def urgency(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DuringSupportHoursDefinition#Urgency
        '''
        result = self._values.get("urgency")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DuringSupportHoursDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.IncidentUrgencyRuleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "during_support_hours": "duringSupportHours",
        "outside_support_hours": "outsideSupportHours",
        "urgency": "urgency",
    },
)
class IncidentUrgencyRuleDefinition:
    def __init__(
        self,
        *,
        type: builtins.str,
        during_support_hours: typing.Optional[typing.Sequence[typing.Union[DuringSupportHoursDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        outside_support_hours: typing.Optional[typing.Sequence[typing.Union["OutsideSupportHoursDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        urgency: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: 
        :param during_support_hours: 
        :param outside_support_hours: 
        :param urgency: 

        :schema: IncidentUrgencyRuleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d074d4b4bc88c4e888d509900a2a445a59d7529445f52ffeff8799d9d708014)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument during_support_hours", value=during_support_hours, expected_type=type_hints["during_support_hours"])
            check_type(argname="argument outside_support_hours", value=outside_support_hours, expected_type=type_hints["outside_support_hours"])
            check_type(argname="argument urgency", value=urgency, expected_type=type_hints["urgency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if during_support_hours is not None:
            self._values["during_support_hours"] = during_support_hours
        if outside_support_hours is not None:
            self._values["outside_support_hours"] = outside_support_hours
        if urgency is not None:
            self._values["urgency"] = urgency

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: IncidentUrgencyRuleDefinition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def during_support_hours(
        self,
    ) -> typing.Optional[typing.List[DuringSupportHoursDefinition]]:
        '''
        :schema: IncidentUrgencyRuleDefinition#DuringSupportHours
        '''
        result = self._values.get("during_support_hours")
        return typing.cast(typing.Optional[typing.List[DuringSupportHoursDefinition]], result)

    @builtins.property
    def outside_support_hours(
        self,
    ) -> typing.Optional[typing.List["OutsideSupportHoursDefinition"]]:
        '''
        :schema: IncidentUrgencyRuleDefinition#OutsideSupportHours
        '''
        result = self._values.get("outside_support_hours")
        return typing.cast(typing.Optional[typing.List["OutsideSupportHoursDefinition"]], result)

    @builtins.property
    def urgency(self) -> typing.Optional[builtins.str]:
        '''
        :schema: IncidentUrgencyRuleDefinition#Urgency
        '''
        result = self._values.get("urgency")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IncidentUrgencyRuleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.OutsideSupportHoursDefinition",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "urgency": "urgency"},
)
class OutsideSupportHoursDefinition:
    def __init__(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        urgency: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: 
        :param urgency: 

        :schema: OutsideSupportHoursDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a32776b01d53e2010291161833ec9749d87935d407e317c27269653c641f16)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument urgency", value=urgency, expected_type=type_hints["urgency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if urgency is not None:
            self._values["urgency"] = urgency

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: OutsideSupportHoursDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def urgency(self) -> typing.Optional[builtins.str]:
        '''
        :schema: OutsideSupportHoursDefinition#Urgency
        '''
        result = self._values.get("urgency")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutsideSupportHoursDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.ScheduledActionsDefinition",
    jsii_struct_bases=[],
    name_mapping={"at": "at", "to_urgency": "toUrgency", "type": "type"},
)
class ScheduledActionsDefinition:
    def __init__(
        self,
        *,
        at: typing.Optional[typing.Sequence[typing.Union[AtDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        to_urgency: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param at: 
        :param to_urgency: 
        :param type: 

        :schema: ScheduledActionsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa066d64ce136a49daebbcd12b5c23606e7da7b580d3bf702d0561ccb2a421c6)
            check_type(argname="argument at", value=at, expected_type=type_hints["at"])
            check_type(argname="argument to_urgency", value=to_urgency, expected_type=type_hints["to_urgency"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if at is not None:
            self._values["at"] = at
        if to_urgency is not None:
            self._values["to_urgency"] = to_urgency
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def at(self) -> typing.Optional[typing.List[AtDefinition]]:
        '''
        :schema: ScheduledActionsDefinition#At
        '''
        result = self._values.get("at")
        return typing.cast(typing.Optional[typing.List[AtDefinition]], result)

    @builtins.property
    def to_urgency(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScheduledActionsDefinition#ToUrgency
        '''
        result = self._values.get("to_urgency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScheduledActionsDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduledActionsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-pagerduty-service.SupportHoursDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_week": "daysOfWeek",
        "end_time": "endTime",
        "start_time": "startTime",
        "time_zone": "timeZone",
        "type": "type",
    },
)
class SupportHoursDefinition:
    def __init__(
        self,
        *,
        days_of_week: typing.Optional[typing.Sequence[jsii.Number]] = None,
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param days_of_week: 
        :param end_time: 
        :param start_time: 
        :param time_zone: 
        :param type: 

        :schema: SupportHoursDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d268fa0e570bacb75449c4ba71b661fe4ee29e5da0e237d14e488f5c1073e0)
            check_type(argname="argument days_of_week", value=days_of_week, expected_type=type_hints["days_of_week"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if days_of_week is not None:
            self._values["days_of_week"] = days_of_week
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time
        if time_zone is not None:
            self._values["time_zone"] = time_zone
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def days_of_week(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''
        :schema: SupportHoursDefinition#DaysOfWeek
        '''
        result = self._values.get("days_of_week")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SupportHoursDefinition#EndTime
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SupportHoursDefinition#StartTime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SupportHoursDefinition#TimeZone
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SupportHoursDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SupportHoursDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AtDefinition",
    "CfnService",
    "CfnServiceProps",
    "DuringSupportHoursDefinition",
    "IncidentUrgencyRuleDefinition",
    "OutsideSupportHoursDefinition",
    "ScheduledActionsDefinition",
    "SupportHoursDefinition",
]

publication.publish()

def _typecheckingstub__d665b43f3ce40e4b78539ac81db107b1a0b8474c8ad46f7898a35f270bbed832(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dac356bd9d120f3ebef9cf76e7f35ec0e19692b7331189ec217900d87005ae7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    escalation_policy: builtins.str,
    name: builtins.str,
    acknowledgement_timeout: typing.Optional[builtins.str] = None,
    alert_creation: typing.Optional[builtins.str] = None,
    alert_grouping: typing.Optional[builtins.str] = None,
    alert_grouping_timeout: typing.Optional[jsii.Number] = None,
    auto_resolve_timeout: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    incident_urgency_rule: typing.Optional[typing.Sequence[typing.Union[IncidentUrgencyRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    scheduled_actions: typing.Optional[typing.Sequence[typing.Union[ScheduledActionsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    support_hours: typing.Optional[typing.Sequence[typing.Union[SupportHoursDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079071ee923650c59ae826665b940e8e9a180fa08ca27ea6f6a507d1f532b68b(
    *,
    escalation_policy: builtins.str,
    name: builtins.str,
    acknowledgement_timeout: typing.Optional[builtins.str] = None,
    alert_creation: typing.Optional[builtins.str] = None,
    alert_grouping: typing.Optional[builtins.str] = None,
    alert_grouping_timeout: typing.Optional[jsii.Number] = None,
    auto_resolve_timeout: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    incident_urgency_rule: typing.Optional[typing.Sequence[typing.Union[IncidentUrgencyRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    scheduled_actions: typing.Optional[typing.Sequence[typing.Union[ScheduledActionsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    support_hours: typing.Optional[typing.Sequence[typing.Union[SupportHoursDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5ad5f61c0861b14ac8dabba78a1ae0d130bfc12d3bb63db1de046e2200afde(
    *,
    type: typing.Optional[builtins.str] = None,
    urgency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d074d4b4bc88c4e888d509900a2a445a59d7529445f52ffeff8799d9d708014(
    *,
    type: builtins.str,
    during_support_hours: typing.Optional[typing.Sequence[typing.Union[DuringSupportHoursDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    outside_support_hours: typing.Optional[typing.Sequence[typing.Union[OutsideSupportHoursDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    urgency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a32776b01d53e2010291161833ec9749d87935d407e317c27269653c641f16(
    *,
    type: typing.Optional[builtins.str] = None,
    urgency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa066d64ce136a49daebbcd12b5c23606e7da7b580d3bf702d0561ccb2a421c6(
    *,
    at: typing.Optional[typing.Sequence[typing.Union[AtDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    to_urgency: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d268fa0e570bacb75449c4ba71b661fe4ee29e5da0e237d14e488f5c1073e0(
    *,
    days_of_week: typing.Optional[typing.Sequence[jsii.Number]] = None,
    end_time: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

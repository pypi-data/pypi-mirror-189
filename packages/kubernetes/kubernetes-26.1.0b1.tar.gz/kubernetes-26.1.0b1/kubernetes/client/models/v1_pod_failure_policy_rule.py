# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.26
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1PodFailurePolicyRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'action': 'str',
        'on_exit_codes': 'V1PodFailurePolicyOnExitCodesRequirement',
        'on_pod_conditions': 'list[V1PodFailurePolicyOnPodConditionsPattern]'
    }

    attribute_map = {
        'action': 'action',
        'on_exit_codes': 'onExitCodes',
        'on_pod_conditions': 'onPodConditions'
    }

    def __init__(self, action=None, on_exit_codes=None, on_pod_conditions=None, local_vars_configuration=None):  # noqa: E501
        """V1PodFailurePolicyRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._on_exit_codes = None
        self._on_pod_conditions = None
        self.discriminator = None

        self.action = action
        if on_exit_codes is not None:
            self.on_exit_codes = on_exit_codes
        self.on_pod_conditions = on_pod_conditions

    @property
    def action(self):
        """Gets the action of this V1PodFailurePolicyRule.  # noqa: E501

        Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod's job is marked as Failed and all   running pods are terminated. - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.    # noqa: E501

        :return: The action of this V1PodFailurePolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1PodFailurePolicyRule.

        Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod's job is marked as Failed and all   running pods are terminated. - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.    # noqa: E501

        :param action: The action of this V1PodFailurePolicyRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def on_exit_codes(self):
        """Gets the on_exit_codes of this V1PodFailurePolicyRule.  # noqa: E501


        :return: The on_exit_codes of this V1PodFailurePolicyRule.  # noqa: E501
        :rtype: V1PodFailurePolicyOnExitCodesRequirement
        """
        return self._on_exit_codes

    @on_exit_codes.setter
    def on_exit_codes(self, on_exit_codes):
        """Sets the on_exit_codes of this V1PodFailurePolicyRule.


        :param on_exit_codes: The on_exit_codes of this V1PodFailurePolicyRule.  # noqa: E501
        :type: V1PodFailurePolicyOnExitCodesRequirement
        """

        self._on_exit_codes = on_exit_codes

    @property
    def on_pod_conditions(self):
        """Gets the on_pod_conditions of this V1PodFailurePolicyRule.  # noqa: E501

        Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.  # noqa: E501

        :return: The on_pod_conditions of this V1PodFailurePolicyRule.  # noqa: E501
        :rtype: list[V1PodFailurePolicyOnPodConditionsPattern]
        """
        return self._on_pod_conditions

    @on_pod_conditions.setter
    def on_pod_conditions(self, on_pod_conditions):
        """Sets the on_pod_conditions of this V1PodFailurePolicyRule.

        Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.  # noqa: E501

        :param on_pod_conditions: The on_pod_conditions of this V1PodFailurePolicyRule.  # noqa: E501
        :type: list[V1PodFailurePolicyOnPodConditionsPattern]
        """
        if self.local_vars_configuration.client_side_validation and on_pod_conditions is None:  # noqa: E501
            raise ValueError("Invalid value for `on_pod_conditions`, must not be `None`")  # noqa: E501

        self._on_pod_conditions = on_pod_conditions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1PodFailurePolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodFailurePolicyRule):
            return True

        return self.to_dict() != other.to_dict()

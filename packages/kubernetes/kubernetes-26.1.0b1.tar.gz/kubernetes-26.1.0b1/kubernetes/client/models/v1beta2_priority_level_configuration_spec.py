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


class V1beta2PriorityLevelConfigurationSpec(object):
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
        'limited': 'V1beta2LimitedPriorityLevelConfiguration',
        'type': 'str'
    }

    attribute_map = {
        'limited': 'limited',
        'type': 'type'
    }

    def __init__(self, limited=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1beta2PriorityLevelConfigurationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._limited = None
        self._type = None
        self.discriminator = None

        if limited is not None:
            self.limited = limited
        self.type = type

    @property
    def limited(self):
        """Gets the limited of this V1beta2PriorityLevelConfigurationSpec.  # noqa: E501


        :return: The limited of this V1beta2PriorityLevelConfigurationSpec.  # noqa: E501
        :rtype: V1beta2LimitedPriorityLevelConfiguration
        """
        return self._limited

    @limited.setter
    def limited(self, limited):
        """Sets the limited of this V1beta2PriorityLevelConfigurationSpec.


        :param limited: The limited of this V1beta2PriorityLevelConfigurationSpec.  # noqa: E501
        :type: V1beta2LimitedPriorityLevelConfiguration
        """

        self._limited = limited

    @property
    def type(self):
        """Gets the type of this V1beta2PriorityLevelConfigurationSpec.  # noqa: E501

        `type` indicates whether this priority level is subject to limitation on request execution.  A value of `\"Exempt\"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `\"Limited\"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.  # noqa: E501

        :return: The type of this V1beta2PriorityLevelConfigurationSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1beta2PriorityLevelConfigurationSpec.

        `type` indicates whether this priority level is subject to limitation on request execution.  A value of `\"Exempt\"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `\"Limited\"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.  # noqa: E501

        :param type: The type of this V1beta2PriorityLevelConfigurationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1beta2PriorityLevelConfigurationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta2PriorityLevelConfigurationSpec):
            return True

        return self.to_dict() != other.to_dict()

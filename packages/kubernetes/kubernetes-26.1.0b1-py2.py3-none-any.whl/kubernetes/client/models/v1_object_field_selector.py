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


class V1ObjectFieldSelector(object):
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
        'api_version': 'str',
        'field_path': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'field_path': 'fieldPath'
    }

    def __init__(self, api_version=None, field_path=None, local_vars_configuration=None):  # noqa: E501
        """V1ObjectFieldSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._field_path = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        self.field_path = field_path

    @property
    def api_version(self):
        """Gets the api_version of this V1ObjectFieldSelector.  # noqa: E501

        Version of the schema the FieldPath is written in terms of, defaults to \"v1\".  # noqa: E501

        :return: The api_version of this V1ObjectFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1ObjectFieldSelector.

        Version of the schema the FieldPath is written in terms of, defaults to \"v1\".  # noqa: E501

        :param api_version: The api_version of this V1ObjectFieldSelector.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def field_path(self):
        """Gets the field_path of this V1ObjectFieldSelector.  # noqa: E501

        Path of the field to select in the specified API version.  # noqa: E501

        :return: The field_path of this V1ObjectFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._field_path

    @field_path.setter
    def field_path(self, field_path):
        """Sets the field_path of this V1ObjectFieldSelector.

        Path of the field to select in the specified API version.  # noqa: E501

        :param field_path: The field_path of this V1ObjectFieldSelector.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and field_path is None:  # noqa: E501
            raise ValueError("Invalid value for `field_path`, must not be `None`")  # noqa: E501

        self._field_path = field_path

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
        if not isinstance(other, V1ObjectFieldSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ObjectFieldSelector):
            return True

        return self.to_dict() != other.to_dict()

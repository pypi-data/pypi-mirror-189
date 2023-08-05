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


class V1EphemeralVolumeSource(object):
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
        'volume_claim_template': 'V1PersistentVolumeClaimTemplate'
    }

    attribute_map = {
        'volume_claim_template': 'volumeClaimTemplate'
    }

    def __init__(self, volume_claim_template=None, local_vars_configuration=None):  # noqa: E501
        """V1EphemeralVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._volume_claim_template = None
        self.discriminator = None

        if volume_claim_template is not None:
            self.volume_claim_template = volume_claim_template

    @property
    def volume_claim_template(self):
        """Gets the volume_claim_template of this V1EphemeralVolumeSource.  # noqa: E501


        :return: The volume_claim_template of this V1EphemeralVolumeSource.  # noqa: E501
        :rtype: V1PersistentVolumeClaimTemplate
        """
        return self._volume_claim_template

    @volume_claim_template.setter
    def volume_claim_template(self, volume_claim_template):
        """Sets the volume_claim_template of this V1EphemeralVolumeSource.


        :param volume_claim_template: The volume_claim_template of this V1EphemeralVolumeSource.  # noqa: E501
        :type: V1PersistentVolumeClaimTemplate
        """

        self._volume_claim_template = volume_claim_template

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
        if not isinstance(other, V1EphemeralVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EphemeralVolumeSource):
            return True

        return self.to_dict() != other.to_dict()

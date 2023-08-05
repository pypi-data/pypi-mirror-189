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


class V1PersistentVolumeClaimSpec(object):
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
        'access_modes': 'list[str]',
        'data_source': 'V1TypedLocalObjectReference',
        'data_source_ref': 'V1TypedObjectReference',
        'resources': 'V1ResourceRequirements',
        'selector': 'V1LabelSelector',
        'storage_class_name': 'str',
        'volume_mode': 'str',
        'volume_name': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'data_source': 'dataSource',
        'data_source_ref': 'dataSourceRef',
        'resources': 'resources',
        'selector': 'selector',
        'storage_class_name': 'storageClassName',
        'volume_mode': 'volumeMode',
        'volume_name': 'volumeName'
    }

    def __init__(self, access_modes=None, data_source=None, data_source_ref=None, resources=None, selector=None, storage_class_name=None, volume_mode=None, volume_name=None, local_vars_configuration=None):  # noqa: E501
        """V1PersistentVolumeClaimSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_modes = None
        self._data_source = None
        self._data_source_ref = None
        self._resources = None
        self._selector = None
        self._storage_class_name = None
        self._volume_mode = None
        self._volume_name = None
        self.discriminator = None

        if access_modes is not None:
            self.access_modes = access_modes
        if data_source is not None:
            self.data_source = data_source
        if data_source_ref is not None:
            self.data_source_ref = data_source_ref
        if resources is not None:
            self.resources = resources
        if selector is not None:
            self.selector = selector
        if storage_class_name is not None:
            self.storage_class_name = storage_class_name
        if volume_mode is not None:
            self.volume_mode = volume_mode
        if volume_name is not None:
            self.volume_name = volume_name

    @property
    def access_modes(self):
        """Gets the access_modes of this V1PersistentVolumeClaimSpec.  # noqa: E501

        accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :return: The access_modes of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this V1PersistentVolumeClaimSpec.

        accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :param access_modes: The access_modes of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def data_source(self):
        """Gets the data_source of this V1PersistentVolumeClaimSpec.  # noqa: E501


        :return: The data_source of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: V1TypedLocalObjectReference
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this V1PersistentVolumeClaimSpec.


        :param data_source: The data_source of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: V1TypedLocalObjectReference
        """

        self._data_source = data_source

    @property
    def data_source_ref(self):
        """Gets the data_source_ref of this V1PersistentVolumeClaimSpec.  # noqa: E501


        :return: The data_source_ref of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: V1TypedObjectReference
        """
        return self._data_source_ref

    @data_source_ref.setter
    def data_source_ref(self, data_source_ref):
        """Sets the data_source_ref of this V1PersistentVolumeClaimSpec.


        :param data_source_ref: The data_source_ref of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: V1TypedObjectReference
        """

        self._data_source_ref = data_source_ref

    @property
    def resources(self):
        """Gets the resources of this V1PersistentVolumeClaimSpec.  # noqa: E501


        :return: The resources of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1PersistentVolumeClaimSpec.


        :param resources: The resources of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def selector(self):
        """Gets the selector of this V1PersistentVolumeClaimSpec.  # noqa: E501


        :return: The selector of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1PersistentVolumeClaimSpec.


        :param selector: The selector of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def storage_class_name(self):
        """Gets the storage_class_name of this V1PersistentVolumeClaimSpec.  # noqa: E501

        storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1  # noqa: E501

        :return: The storage_class_name of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: str
        """
        return self._storage_class_name

    @storage_class_name.setter
    def storage_class_name(self, storage_class_name):
        """Sets the storage_class_name of this V1PersistentVolumeClaimSpec.

        storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1  # noqa: E501

        :param storage_class_name: The storage_class_name of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: str
        """

        self._storage_class_name = storage_class_name

    @property
    def volume_mode(self):
        """Gets the volume_mode of this V1PersistentVolumeClaimSpec.  # noqa: E501

        volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  # noqa: E501

        :return: The volume_mode of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: str
        """
        return self._volume_mode

    @volume_mode.setter
    def volume_mode(self, volume_mode):
        """Sets the volume_mode of this V1PersistentVolumeClaimSpec.

        volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  # noqa: E501

        :param volume_mode: The volume_mode of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: str
        """

        self._volume_mode = volume_mode

    @property
    def volume_name(self):
        """Gets the volume_name of this V1PersistentVolumeClaimSpec.  # noqa: E501

        volumeName is the binding reference to the PersistentVolume backing this claim.  # noqa: E501

        :return: The volume_name of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this V1PersistentVolumeClaimSpec.

        volumeName is the binding reference to the PersistentVolume backing this claim.  # noqa: E501

        :param volume_name: The volume_name of this V1PersistentVolumeClaimSpec.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

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
        if not isinstance(other, V1PersistentVolumeClaimSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PersistentVolumeClaimSpec):
            return True

        return self.to_dict() != other.to_dict()

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


class V1AWSElasticBlockStoreVolumeSource(object):
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
        'fs_type': 'str',
        'partition': 'int',
        'read_only': 'bool',
        'volume_id': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'partition': 'partition',
        'read_only': 'readOnly',
        'volume_id': 'volumeID'
    }

    def __init__(self, fs_type=None, partition=None, read_only=None, volume_id=None, local_vars_configuration=None):  # noqa: E501
        """V1AWSElasticBlockStoreVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fs_type = None
        self._partition = None
        self._read_only = None
        self._volume_id = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if partition is not None:
            self.partition = partition
        if read_only is not None:
            self.read_only = read_only
        self.volume_id = volume_id

    @property
    def fs_type(self):
        """Gets the fs_type of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501

        fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore  # noqa: E501

        :return: The fs_type of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1AWSElasticBlockStoreVolumeSource.

        fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore  # noqa: E501

        :param fs_type: The fs_type of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def partition(self):
        """Gets the partition of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501

        partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty).  # noqa: E501

        :return: The partition of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this V1AWSElasticBlockStoreVolumeSource.

        partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty).  # noqa: E501

        :param partition: The partition of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :type: int
        """

        self._partition = partition

    @property
    def read_only(self):
        """Gets the read_only of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501

        readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore  # noqa: E501

        :return: The read_only of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1AWSElasticBlockStoreVolumeSource.

        readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore  # noqa: E501

        :param read_only: The read_only of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def volume_id(self):
        """Gets the volume_id of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501

        volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore  # noqa: E501

        :return: The volume_id of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this V1AWSElasticBlockStoreVolumeSource.

        volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore  # noqa: E501

        :param volume_id: The volume_id of this V1AWSElasticBlockStoreVolumeSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

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
        if not isinstance(other, V1AWSElasticBlockStoreVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AWSElasticBlockStoreVolumeSource):
            return True

        return self.to_dict() != other.to_dict()

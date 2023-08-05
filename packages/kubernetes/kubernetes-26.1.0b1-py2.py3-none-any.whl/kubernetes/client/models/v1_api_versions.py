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


class V1APIVersions(object):
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
        'kind': 'str',
        'server_address_by_client_cid_rs': 'list[V1ServerAddressByClientCIDR]',
        'versions': 'list[str]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'server_address_by_client_cid_rs': 'serverAddressByClientCIDRs',
        'versions': 'versions'
    }

    def __init__(self, api_version=None, kind=None, server_address_by_client_cid_rs=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """V1APIVersions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._kind = None
        self._server_address_by_client_cid_rs = None
        self._versions = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        self.server_address_by_client_cid_rs = server_address_by_client_cid_rs
        self.versions = versions

    @property
    def api_version(self):
        """Gets the api_version of this V1APIVersions.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1APIVersions.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1APIVersions.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1APIVersions.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this V1APIVersions.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1APIVersions.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1APIVersions.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1APIVersions.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def server_address_by_client_cid_rs(self):
        """Gets the server_address_by_client_cid_rs of this V1APIVersions.  # noqa: E501

        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.  # noqa: E501

        :return: The server_address_by_client_cid_rs of this V1APIVersions.  # noqa: E501
        :rtype: list[V1ServerAddressByClientCIDR]
        """
        return self._server_address_by_client_cid_rs

    @server_address_by_client_cid_rs.setter
    def server_address_by_client_cid_rs(self, server_address_by_client_cid_rs):
        """Sets the server_address_by_client_cid_rs of this V1APIVersions.

        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.  # noqa: E501

        :param server_address_by_client_cid_rs: The server_address_by_client_cid_rs of this V1APIVersions.  # noqa: E501
        :type: list[V1ServerAddressByClientCIDR]
        """
        if self.local_vars_configuration.client_side_validation and server_address_by_client_cid_rs is None:  # noqa: E501
            raise ValueError("Invalid value for `server_address_by_client_cid_rs`, must not be `None`")  # noqa: E501

        self._server_address_by_client_cid_rs = server_address_by_client_cid_rs

    @property
    def versions(self):
        """Gets the versions of this V1APIVersions.  # noqa: E501

        versions are the api versions that are available.  # noqa: E501

        :return: The versions of this V1APIVersions.  # noqa: E501
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this V1APIVersions.

        versions are the api versions that are available.  # noqa: E501

        :param versions: The versions of this V1APIVersions.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and versions is None:  # noqa: E501
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501

        self._versions = versions

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
        if not isinstance(other, V1APIVersions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1APIVersions):
            return True

        return self.to_dict() != other.to_dict()

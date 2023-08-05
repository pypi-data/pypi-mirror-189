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


class V1JobStatus(object):
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
        'active': 'int',
        'completed_indexes': 'str',
        'completion_time': 'datetime',
        'conditions': 'list[V1JobCondition]',
        'failed': 'int',
        'ready': 'int',
        'start_time': 'datetime',
        'succeeded': 'int',
        'uncounted_terminated_pods': 'V1UncountedTerminatedPods'
    }

    attribute_map = {
        'active': 'active',
        'completed_indexes': 'completedIndexes',
        'completion_time': 'completionTime',
        'conditions': 'conditions',
        'failed': 'failed',
        'ready': 'ready',
        'start_time': 'startTime',
        'succeeded': 'succeeded',
        'uncounted_terminated_pods': 'uncountedTerminatedPods'
    }

    def __init__(self, active=None, completed_indexes=None, completion_time=None, conditions=None, failed=None, ready=None, start_time=None, succeeded=None, uncounted_terminated_pods=None, local_vars_configuration=None):  # noqa: E501
        """V1JobStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._completed_indexes = None
        self._completion_time = None
        self._conditions = None
        self._failed = None
        self._ready = None
        self._start_time = None
        self._succeeded = None
        self._uncounted_terminated_pods = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if completed_indexes is not None:
            self.completed_indexes = completed_indexes
        if completion_time is not None:
            self.completion_time = completion_time
        if conditions is not None:
            self.conditions = conditions
        if failed is not None:
            self.failed = failed
        if ready is not None:
            self.ready = ready
        if start_time is not None:
            self.start_time = start_time
        if succeeded is not None:
            self.succeeded = succeeded
        if uncounted_terminated_pods is not None:
            self.uncounted_terminated_pods = uncounted_terminated_pods

    @property
    def active(self):
        """Gets the active of this V1JobStatus.  # noqa: E501

        The number of pending and running pods.  # noqa: E501

        :return: The active of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this V1JobStatus.

        The number of pending and running pods.  # noqa: E501

        :param active: The active of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._active = active

    @property
    def completed_indexes(self):
        """Gets the completed_indexes of this V1JobStatus.  # noqa: E501

        CompletedIndexes holds the completed indexes when .spec.completionMode = \"Indexed\" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as \"1,3-5,7\".  # noqa: E501

        :return: The completed_indexes of this V1JobStatus.  # noqa: E501
        :rtype: str
        """
        return self._completed_indexes

    @completed_indexes.setter
    def completed_indexes(self, completed_indexes):
        """Sets the completed_indexes of this V1JobStatus.

        CompletedIndexes holds the completed indexes when .spec.completionMode = \"Indexed\" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as \"1,3-5,7\".  # noqa: E501

        :param completed_indexes: The completed_indexes of this V1JobStatus.  # noqa: E501
        :type: str
        """

        self._completed_indexes = completed_indexes

    @property
    def completion_time(self):
        """Gets the completion_time of this V1JobStatus.  # noqa: E501

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is only set when the job finishes successfully.  # noqa: E501

        :return: The completion_time of this V1JobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this V1JobStatus.

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is only set when the job finishes successfully.  # noqa: E501

        :param completion_time: The completion_time of this V1JobStatus.  # noqa: E501
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def conditions(self):
        """Gets the conditions of this V1JobStatus.  # noqa: E501

        The latest available observations of an object's current state. When a Job fails, one of the conditions will have type \"Failed\" and status true. When a Job is suspended, one of the conditions will have type \"Suspended\" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type \"Complete\" and status true. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The conditions of this V1JobStatus.  # noqa: E501
        :rtype: list[V1JobCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1JobStatus.

        The latest available observations of an object's current state. When a Job fails, one of the conditions will have type \"Failed\" and status true. When a Job is suspended, one of the conditions will have type \"Suspended\" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type \"Complete\" and status true. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param conditions: The conditions of this V1JobStatus.  # noqa: E501
        :type: list[V1JobCondition]
        """

        self._conditions = conditions

    @property
    def failed(self):
        """Gets the failed of this V1JobStatus.  # noqa: E501

        The number of pods which reached phase Failed.  # noqa: E501

        :return: The failed of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this V1JobStatus.

        The number of pods which reached phase Failed.  # noqa: E501

        :param failed: The failed of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def ready(self):
        """Gets the ready of this V1JobStatus.  # noqa: E501

        The number of pods which have a Ready condition.  This field is beta-level. The job controller populates the field when the feature gate JobReadyPods is enabled (enabled by default).  # noqa: E501

        :return: The ready of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this V1JobStatus.

        The number of pods which have a Ready condition.  This field is beta-level. The job controller populates the field when the feature gate JobReadyPods is enabled (enabled by default).  # noqa: E501

        :param ready: The ready of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._ready = ready

    @property
    def start_time(self):
        """Gets the start_time of this V1JobStatus.  # noqa: E501

        Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The start_time of this V1JobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1JobStatus.

        Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param start_time: The start_time of this V1JobStatus.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def succeeded(self):
        """Gets the succeeded of this V1JobStatus.  # noqa: E501

        The number of pods which reached phase Succeeded.  # noqa: E501

        :return: The succeeded of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this V1JobStatus.

        The number of pods which reached phase Succeeded.  # noqa: E501

        :param succeeded: The succeeded of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._succeeded = succeeded

    @property
    def uncounted_terminated_pods(self):
        """Gets the uncounted_terminated_pods of this V1JobStatus.  # noqa: E501


        :return: The uncounted_terminated_pods of this V1JobStatus.  # noqa: E501
        :rtype: V1UncountedTerminatedPods
        """
        return self._uncounted_terminated_pods

    @uncounted_terminated_pods.setter
    def uncounted_terminated_pods(self, uncounted_terminated_pods):
        """Sets the uncounted_terminated_pods of this V1JobStatus.


        :param uncounted_terminated_pods: The uncounted_terminated_pods of this V1JobStatus.  # noqa: E501
        :type: V1UncountedTerminatedPods
        """

        self._uncounted_terminated_pods = uncounted_terminated_pods

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
        if not isinstance(other, V1JobStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1JobStatus):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 59.1.2-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class CapsulesOverwriteInputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'capsules': 'list[CapsuleInputV1]',
        'interval': 'IntervalV1'
    }

    attribute_map = {
        'capsules': 'capsules',
        'interval': 'interval'
    }

    def __init__(self, capsules=None, interval=None):
        """
        CapsulesOverwriteInputV1 - a model defined in Swagger
        """

        self._capsules = None
        self._interval = None

        if capsules is not None:
          self.capsules = capsules
        if interval is not None:
          self.interval = interval

    @property
    def capsules(self):
        """
        Gets the capsules of this CapsulesOverwriteInputV1.
        The list of capsules

        :return: The capsules of this CapsulesOverwriteInputV1.
        :rtype: list[CapsuleInputV1]
        """
        return self._capsules

    @capsules.setter
    def capsules(self, capsules):
        """
        Sets the capsules of this CapsulesOverwriteInputV1.
        The list of capsules

        :param capsules: The capsules of this CapsulesOverwriteInputV1.
        :type: list[CapsuleInputV1]
        """
        if capsules is None:
            raise ValueError("Invalid value for `capsules`, must not be `None`")

        self._capsules = capsules

    @property
    def interval(self):
        """
        Gets the interval of this CapsulesOverwriteInputV1.

        :return: The interval of this CapsulesOverwriteInputV1.
        :rtype: IntervalV1
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this CapsulesOverwriteInputV1.

        :param interval: The interval of this CapsulesOverwriteInputV1.
        :type: IntervalV1
        """

        self._interval = interval

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CapsulesOverwriteInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 57.3.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class AnnotationInterestInputV1(object):
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
        'detail_id': 'str',
        'interest_id': 'str'
    }

    attribute_map = {
        'detail_id': 'detailId',
        'interest_id': 'interestId'
    }

    def __init__(self, detail_id=None, interest_id=None):
        """
        AnnotationInterestInputV1 - a model defined in Swagger
        """

        self._detail_id = None
        self._interest_id = None

        if detail_id is not None:
          self.detail_id = detail_id
        if interest_id is not None:
          self.interest_id = interest_id

    @property
    def detail_id(self):
        """
        Gets the detail_id of this AnnotationInterestInputV1.
        An optional secondary ID for a specific datum in the set of interest

        :return: The detail_id of this AnnotationInterestInputV1.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """
        Sets the detail_id of this AnnotationInterestInputV1.
        An optional secondary ID for a specific datum in the set of interest

        :param detail_id: The detail_id of this AnnotationInterestInputV1.
        :type: str
        """

        self._detail_id = detail_id

    @property
    def interest_id(self):
        """
        Gets the interest_id of this AnnotationInterestInputV1.
        The ID of the item being annotated

        :return: The interest_id of this AnnotationInterestInputV1.
        :rtype: str
        """
        return self._interest_id

    @interest_id.setter
    def interest_id(self, interest_id):
        """
        Sets the interest_id of this AnnotationInterestInputV1.
        The ID of the item being annotated

        :param interest_id: The interest_id of this AnnotationInterestInputV1.
        :type: str
        """
        if interest_id is None:
            raise ValueError("Invalid value for `interest_id`, must not be `None`")

        self._interest_id = interest_id

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
        if not isinstance(other, AnnotationInterestInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

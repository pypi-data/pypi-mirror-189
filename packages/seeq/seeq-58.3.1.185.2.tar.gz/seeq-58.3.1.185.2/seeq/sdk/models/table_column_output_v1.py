# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 58.3.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class TableColumnOutputV1(object):
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
        'name': 'str',
        'type': 'str',
        'units': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'units': 'units'
    }

    def __init__(self, name=None, type=None, units=None):
        """
        TableColumnOutputV1 - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._units = None

        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if units is not None:
          self.units = units

    @property
    def name(self):
        """
        Gets the name of this TableColumnOutputV1.
        The name of the column

        :return: The name of this TableColumnOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TableColumnOutputV1.
        The name of the column

        :param name: The name of this TableColumnOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this TableColumnOutputV1.
        The type of the column. Valid values include 'string', 'number', and 'date'. Booleans are reported as 'number'

        :return: The type of this TableColumnOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TableColumnOutputV1.
        The type of the column. Valid values include 'string', 'number', and 'date'. Booleans are reported as 'number'

        :param type: The type of this TableColumnOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def units(self):
        """
        Gets the units of this TableColumnOutputV1.
        The units of the column. Only provided if type is 'number'

        :return: The units of this TableColumnOutputV1.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this TableColumnOutputV1.
        The units of the column. Only provided if type is 'number'

        :param units: The units of this TableColumnOutputV1.
        :type: str
        """

        self._units = units

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
        if not isinstance(other, TableColumnOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

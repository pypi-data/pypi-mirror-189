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


class UnitsOfMeasureItemV1(object):
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
        'canonical_uom': 'str',
        'input': 'str'
    }

    attribute_map = {
        'canonical_uom': 'canonicalUom',
        'input': 'input'
    }

    def __init__(self, canonical_uom=None, input=None):
        """
        UnitsOfMeasureItemV1 - a model defined in Swagger
        """

        self._canonical_uom = None
        self._input = None

        if canonical_uom is not None:
          self.canonical_uom = canonical_uom
        if input is not None:
          self.input = input

    @property
    def canonical_uom(self):
        """
        Gets the canonical_uom of this UnitsOfMeasureItemV1.
        The canonical unit of measure string, if the input was parsable, otherwise null

        :return: The canonical_uom of this UnitsOfMeasureItemV1.
        :rtype: str
        """
        return self._canonical_uom

    @canonical_uom.setter
    def canonical_uom(self, canonical_uom):
        """
        Sets the canonical_uom of this UnitsOfMeasureItemV1.
        The canonical unit of measure string, if the input was parsable, otherwise null

        :param canonical_uom: The canonical_uom of this UnitsOfMeasureItemV1.
        :type: str
        """

        self._canonical_uom = canonical_uom

    @property
    def input(self):
        """
        Gets the input of this UnitsOfMeasureItemV1.
        The unit of measure string that was input

        :return: The input of this UnitsOfMeasureItemV1.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this UnitsOfMeasureItemV1.
        The unit of measure string that was input

        :param input: The input of this UnitsOfMeasureItemV1.
        :type: str
        """

        self._input = input

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
        if not isinstance(other, UnitsOfMeasureItemV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

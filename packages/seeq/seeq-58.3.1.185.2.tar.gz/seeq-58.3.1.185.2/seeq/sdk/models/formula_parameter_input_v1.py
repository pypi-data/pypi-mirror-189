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


class FormulaParameterInputV1(object):
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
        'formula': 'str',
        'id': 'str',
        'name': 'str',
        'unbound': 'bool'
    }

    attribute_map = {
        'formula': 'formula',
        'id': 'id',
        'name': 'name',
        'unbound': 'unbound'
    }

    def __init__(self, formula=None, id=None, name=None, unbound=False):
        """
        FormulaParameterInputV1 - a model defined in Swagger
        """

        self._formula = None
        self._id = None
        self._name = None
        self._unbound = None

        if formula is not None:
          self.formula = formula
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if unbound is not None:
          self.unbound = unbound

    @property
    def formula(self):
        """
        Gets the formula of this FormulaParameterInputV1.
        The formula that defines this parameter. This is required if 'unbound' is true. This field or 'id' must be specified

        :return: The formula of this FormulaParameterInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FormulaParameterInputV1.
        The formula that defines this parameter. This is required if 'unbound' is true. This field or 'id' must be specified

        :param formula: The formula of this FormulaParameterInputV1.
        :type: str
        """

        self._formula = formula

    @property
    def id(self):
        """
        Gets the id of this FormulaParameterInputV1.
        The ID of the item that is the value of this parameter. This can't be specified if 'unbound' is true. This field or 'formula' must be specified

        :return: The id of this FormulaParameterInputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FormulaParameterInputV1.
        The ID of the item that is the value of this parameter. This can't be specified if 'unbound' is true. This field or 'formula' must be specified

        :param id: The id of this FormulaParameterInputV1.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FormulaParameterInputV1.
        The name of the parameter as used in the formula. It should not include the '$' prefix

        :return: The name of this FormulaParameterInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormulaParameterInputV1.
        The name of the parameter as used in the formula. It should not include the '$' prefix

        :param name: The name of this FormulaParameterInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def unbound(self):
        """
        Gets the unbound of this FormulaParameterInputV1.
        Indicate the value of this parameter will be provided at runtime. When true, it requires a sample formula to be specified in the 'formula' field so that the validity of the entire function can be validated. Default is false

        :return: The unbound of this FormulaParameterInputV1.
        :rtype: bool
        """
        return self._unbound

    @unbound.setter
    def unbound(self, unbound):
        """
        Sets the unbound of this FormulaParameterInputV1.
        Indicate the value of this parameter will be provided at runtime. When true, it requires a sample formula to be specified in the 'formula' field so that the validity of the entire function can be validated. Default is false

        :param unbound: The unbound of this FormulaParameterInputV1.
        :type: bool
        """

        self._unbound = unbound

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
        if not isinstance(other, FormulaParameterInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

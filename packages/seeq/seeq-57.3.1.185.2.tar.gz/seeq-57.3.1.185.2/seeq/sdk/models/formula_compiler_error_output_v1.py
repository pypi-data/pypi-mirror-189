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


class FormulaCompilerErrorOutputV1(object):
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
        'column': 'int',
        'error_category': 'str',
        'error_type': 'str',
        'function_id': 'str',
        'item_id': 'str',
        'line': 'int',
        'message': 'str'
    }

    attribute_map = {
        'column': 'column',
        'error_category': 'errorCategory',
        'error_type': 'errorType',
        'function_id': 'functionId',
        'item_id': 'itemId',
        'line': 'line',
        'message': 'message'
    }

    def __init__(self, column=None, error_category=None, error_type=None, function_id=None, item_id=None, line=None, message=None):
        """
        FormulaCompilerErrorOutputV1 - a model defined in Swagger
        """

        self._column = None
        self._error_category = None
        self._error_type = None
        self._function_id = None
        self._item_id = None
        self._line = None
        self._message = None

        if column is not None:
          self.column = column
        if error_category is not None:
          self.error_category = error_category
        if error_type is not None:
          self.error_type = error_type
        if function_id is not None:
          self.function_id = function_id
        if item_id is not None:
          self.item_id = item_id
        if line is not None:
          self.line = line
        if message is not None:
          self.message = message

    @property
    def column(self):
        """
        Gets the column of this FormulaCompilerErrorOutputV1.
        The column of the formula that resulted in an error

        :return: The column of this FormulaCompilerErrorOutputV1.
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this FormulaCompilerErrorOutputV1.
        The column of the formula that resulted in an error

        :param column: The column of this FormulaCompilerErrorOutputV1.
        :type: int
        """

        self._column = column

    @property
    def error_category(self):
        """
        Gets the error_category of this FormulaCompilerErrorOutputV1.
        The category of the formula error, i.e. when it was encountered

        :return: The error_category of this FormulaCompilerErrorOutputV1.
        :rtype: str
        """
        return self._error_category

    @error_category.setter
    def error_category(self, error_category):
        """
        Sets the error_category of this FormulaCompilerErrorOutputV1.
        The category of the formula error, i.e. when it was encountered

        :param error_category: The error_category of this FormulaCompilerErrorOutputV1.
        :type: str
        """

        self._error_category = error_category

    @property
    def error_type(self):
        """
        Gets the error_type of this FormulaCompilerErrorOutputV1.
        The type of formula error that occurred

        :return: The error_type of this FormulaCompilerErrorOutputV1.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this FormulaCompilerErrorOutputV1.
        The type of formula error that occurred

        :param error_type: The error_type of this FormulaCompilerErrorOutputV1.
        :type: str
        """

        self._error_type = error_type

    @property
    def function_id(self):
        """
        Gets the function_id of this FormulaCompilerErrorOutputV1.
        The function where the error occurred

        :return: The function_id of this FormulaCompilerErrorOutputV1.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this FormulaCompilerErrorOutputV1.
        The function where the error occurred

        :param function_id: The function_id of this FormulaCompilerErrorOutputV1.
        :type: str
        """

        self._function_id = function_id

    @property
    def item_id(self):
        """
        Gets the item_id of this FormulaCompilerErrorOutputV1.
        The itemId that is the cause of the error

        :return: The item_id of this FormulaCompilerErrorOutputV1.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this FormulaCompilerErrorOutputV1.
        The itemId that is the cause of the error

        :param item_id: The item_id of this FormulaCompilerErrorOutputV1.
        :type: str
        """

        self._item_id = item_id

    @property
    def line(self):
        """
        Gets the line of this FormulaCompilerErrorOutputV1.
        The line of the formula that resulted in an error

        :return: The line of this FormulaCompilerErrorOutputV1.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """
        Sets the line of this FormulaCompilerErrorOutputV1.
        The line of the formula that resulted in an error

        :param line: The line of this FormulaCompilerErrorOutputV1.
        :type: int
        """

        self._line = line

    @property
    def message(self):
        """
        Gets the message of this FormulaCompilerErrorOutputV1.
        An error message for the compiled formula

        :return: The message of this FormulaCompilerErrorOutputV1.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this FormulaCompilerErrorOutputV1.
        An error message for the compiled formula

        :param message: The message of this FormulaCompilerErrorOutputV1.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, FormulaCompilerErrorOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

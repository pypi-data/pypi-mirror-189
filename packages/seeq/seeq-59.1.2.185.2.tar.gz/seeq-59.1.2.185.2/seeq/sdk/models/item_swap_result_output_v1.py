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


class ItemSwapResultOutputV1(object):
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
        'error_message': 'str',
        'item': 'ItemPreviewWithAssetsV1',
        'parent': 'ItemPreviewV1'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'item': 'item',
        'parent': 'parent'
    }

    def __init__(self, error_message=None, item=None, parent=None):
        """
        ItemSwapResultOutputV1 - a model defined in Swagger
        """

        self._error_message = None
        self._item = None
        self._parent = None

        if error_message is not None:
          self.error_message = error_message
        if item is not None:
          self.item = item
        if parent is not None:
          self.parent = parent

    @property
    def error_message(self):
        """
        Gets the error_message of this ItemSwapResultOutputV1.
        If the item could not be created, this field will contain an error message explaining the problem

        :return: The error_message of this ItemSwapResultOutputV1.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ItemSwapResultOutputV1.
        If the item could not be created, this field will contain an error message explaining the problem

        :param error_message: The error_message of this ItemSwapResultOutputV1.
        :type: str
        """

        self._error_message = error_message

    @property
    def item(self):
        """
        Gets the item of this ItemSwapResultOutputV1.

        :return: The item of this ItemSwapResultOutputV1.
        :rtype: ItemPreviewWithAssetsV1
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this ItemSwapResultOutputV1.

        :param item: The item of this ItemSwapResultOutputV1.
        :type: ItemPreviewWithAssetsV1
        """

        self._item = item

    @property
    def parent(self):
        """
        Gets the parent of this ItemSwapResultOutputV1.

        :return: The parent of this ItemSwapResultOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ItemSwapResultOutputV1.

        :param parent: The parent of this ItemSwapResultOutputV1.
        :type: ItemPreviewV1
        """

        self._parent = parent

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
        if not isinstance(other, ItemSwapResultOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

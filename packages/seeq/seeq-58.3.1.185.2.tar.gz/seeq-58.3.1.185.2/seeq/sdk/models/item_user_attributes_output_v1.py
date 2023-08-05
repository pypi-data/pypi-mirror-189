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


class ItemUserAttributesOutputV1(object):
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
        'item_id': 'str',
        'opened_at': 'str',
        'status_message': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'item_id': 'itemId',
        'opened_at': 'openedAt',
        'status_message': 'statusMessage',
        'user_id': 'userId'
    }

    def __init__(self, item_id=None, opened_at=None, status_message=None, user_id=None):
        """
        ItemUserAttributesOutputV1 - a model defined in Swagger
        """

        self._item_id = None
        self._opened_at = None
        self._status_message = None
        self._user_id = None

        if item_id is not None:
          self.item_id = item_id
        if opened_at is not None:
          self.opened_at = opened_at
        if status_message is not None:
          self.status_message = status_message
        if user_id is not None:
          self.user_id = user_id

    @property
    def item_id(self):
        """
        Gets the item_id of this ItemUserAttributesOutputV1.
        The ID of the item

        :return: The item_id of this ItemUserAttributesOutputV1.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this ItemUserAttributesOutputV1.
        The ID of the item

        :param item_id: The item_id of this ItemUserAttributesOutputV1.
        :type: str
        """

        self._item_id = item_id

    @property
    def opened_at(self):
        """
        Gets the opened_at of this ItemUserAttributesOutputV1.
        The opened date of the item. Null if unset. Formatted as an ISO-8601 string.

        :return: The opened_at of this ItemUserAttributesOutputV1.
        :rtype: str
        """
        return self._opened_at

    @opened_at.setter
    def opened_at(self, opened_at):
        """
        Sets the opened_at of this ItemUserAttributesOutputV1.
        The opened date of the item. Null if unset. Formatted as an ISO-8601 string.

        :param opened_at: The opened_at of this ItemUserAttributesOutputV1.
        :type: str
        """

        self._opened_at = opened_at

    @property
    def status_message(self):
        """
        Gets the status_message of this ItemUserAttributesOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ItemUserAttributesOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ItemUserAttributesOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ItemUserAttributesOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def user_id(self):
        """
        Gets the user_id of this ItemUserAttributesOutputV1.
        The ID of the user

        :return: The user_id of this ItemUserAttributesOutputV1.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ItemUserAttributesOutputV1.
        The ID of the user

        :param user_id: The user_id of this ItemUserAttributesOutputV1.
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, ItemUserAttributesOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

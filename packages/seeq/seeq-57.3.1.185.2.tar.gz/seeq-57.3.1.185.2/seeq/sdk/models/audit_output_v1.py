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


class AuditOutputV1(object):
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
        'after_summary': 'str',
        'before_summary': 'str',
        'change_type': 'str',
        'item_id': 'str',
        'item_name': 'str',
        'item_type': 'str',
        'time_stamp': 'str',
        'user_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'after_summary': 'afterSummary',
        'before_summary': 'beforeSummary',
        'change_type': 'changeType',
        'item_id': 'itemId',
        'item_name': 'itemName',
        'item_type': 'itemType',
        'time_stamp': 'timeStamp',
        'user_id': 'userId',
        'user_name': 'userName'
    }

    def __init__(self, after_summary=None, before_summary=None, change_type=None, item_id=None, item_name=None, item_type=None, time_stamp=None, user_id=None, user_name=None):
        """
        AuditOutputV1 - a model defined in Swagger
        """

        self._after_summary = None
        self._before_summary = None
        self._change_type = None
        self._item_id = None
        self._item_name = None
        self._item_type = None
        self._time_stamp = None
        self._user_id = None
        self._user_name = None

        if after_summary is not None:
          self.after_summary = after_summary
        if before_summary is not None:
          self.before_summary = before_summary
        if change_type is not None:
          self.change_type = change_type
        if item_id is not None:
          self.item_id = item_id
        if item_name is not None:
          self.item_name = item_name
        if item_type is not None:
          self.item_type = item_type
        if time_stamp is not None:
          self.time_stamp = time_stamp
        if user_id is not None:
          self.user_id = user_id
        if user_name is not None:
          self.user_name = user_name

    @property
    def after_summary(self):
        """
        Gets the after_summary of this AuditOutputV1.
        A summary of the changed fields after the change was made.

        :return: The after_summary of this AuditOutputV1.
        :rtype: str
        """
        return self._after_summary

    @after_summary.setter
    def after_summary(self, after_summary):
        """
        Sets the after_summary of this AuditOutputV1.
        A summary of the changed fields after the change was made.

        :param after_summary: The after_summary of this AuditOutputV1.
        :type: str
        """

        self._after_summary = after_summary

    @property
    def before_summary(self):
        """
        Gets the before_summary of this AuditOutputV1.
        A summary of the changed fields before the change was made.

        :return: The before_summary of this AuditOutputV1.
        :rtype: str
        """
        return self._before_summary

    @before_summary.setter
    def before_summary(self, before_summary):
        """
        Sets the before_summary of this AuditOutputV1.
        A summary of the changed fields before the change was made.

        :param before_summary: The before_summary of this AuditOutputV1.
        :type: str
        """

        self._before_summary = before_summary

    @property
    def change_type(self):
        """
        Gets the change_type of this AuditOutputV1.
        The type of change that was made (Create, Update, or Delete).

        :return: The change_type of this AuditOutputV1.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """
        Sets the change_type of this AuditOutputV1.
        The type of change that was made (Create, Update, or Delete).

        :param change_type: The change_type of this AuditOutputV1.
        :type: str
        """
        allowed_values = ["CREATE", "UPDATE", "DELETE"]
        if change_type not in allowed_values:
            raise ValueError(
                "Invalid value for `change_type` ({0}), must be one of {1}"
                .format(change_type, allowed_values)
            )

        self._change_type = change_type

    @property
    def item_id(self):
        """
        Gets the item_id of this AuditOutputV1.
        The ID of the modified item.

        :return: The item_id of this AuditOutputV1.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this AuditOutputV1.
        The ID of the modified item.

        :param item_id: The item_id of this AuditOutputV1.
        :type: str
        """

        self._item_id = item_id

    @property
    def item_name(self):
        """
        Gets the item_name of this AuditOutputV1.
        The name of the modified item.

        :return: The item_name of this AuditOutputV1.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """
        Sets the item_name of this AuditOutputV1.
        The name of the modified item.

        :param item_name: The item_name of this AuditOutputV1.
        :type: str
        """

        self._item_name = item_name

    @property
    def item_type(self):
        """
        Gets the item_type of this AuditOutputV1.
        The type of the modified item.

        :return: The item_type of this AuditOutputV1.
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """
        Sets the item_type of this AuditOutputV1.
        The type of the modified item.

        :param item_type: The item_type of this AuditOutputV1.
        :type: str
        """

        self._item_type = item_type

    @property
    def time_stamp(self):
        """
        Gets the time_stamp of this AuditOutputV1.
        The date and time when the change was made.

        :return: The time_stamp of this AuditOutputV1.
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this AuditOutputV1.
        The date and time when the change was made.

        :param time_stamp: The time_stamp of this AuditOutputV1.
        :type: str
        """

        self._time_stamp = time_stamp

    @property
    def user_id(self):
        """
        Gets the user_id of this AuditOutputV1.
        The ID of the user who made the change.

        :return: The user_id of this AuditOutputV1.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AuditOutputV1.
        The ID of the user who made the change.

        :param user_id: The user_id of this AuditOutputV1.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """
        Gets the user_name of this AuditOutputV1.
        The username of the user who made the change.

        :return: The user_name of this AuditOutputV1.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this AuditOutputV1.
        The username of the user who made the change.

        :param user_name: The user_name of this AuditOutputV1.
        :type: str
        """

        self._user_name = user_name

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
        if not isinstance(other, AuditOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

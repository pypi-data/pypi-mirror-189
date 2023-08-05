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


class AccessKeyOutputListV1(object):
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
        'keys': 'list[AccessKeyOutputV1]',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'keys': 'keys',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'status_message': 'statusMessage'
    }

    def __init__(self, keys=None, limit=None, next=None, offset=None, prev=None, status_message=None):
        """
        AccessKeyOutputListV1 - a model defined in Swagger
        """

        self._keys = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._status_message = None

        if keys is not None:
          self.keys = keys
        if limit is not None:
          self.limit = limit
        if next is not None:
          self.next = next
        if offset is not None:
          self.offset = offset
        if prev is not None:
          self.prev = prev
        if status_message is not None:
          self.status_message = status_message

    @property
    def keys(self):
        """
        Gets the keys of this AccessKeyOutputListV1.
        The list of API Keys

        :return: The keys of this AccessKeyOutputListV1.
        :rtype: list[AccessKeyOutputV1]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """
        Sets the keys of this AccessKeyOutputListV1.
        The list of API Keys

        :param keys: The keys of this AccessKeyOutputListV1.
        :type: list[AccessKeyOutputV1]
        """

        self._keys = keys

    @property
    def limit(self):
        """
        Gets the limit of this AccessKeyOutputListV1.
        The pagination limit, the total number of collection items that will be returned in this page of results

        :return: The limit of this AccessKeyOutputListV1.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this AccessKeyOutputListV1.
        The pagination limit, the total number of collection items that will be returned in this page of results

        :param limit: The limit of this AccessKeyOutputListV1.
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """
        Gets the next of this AccessKeyOutputListV1.
        The href of the next set of paginated results

        :return: The next of this AccessKeyOutputListV1.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this AccessKeyOutputListV1.
        The href of the next set of paginated results

        :param next: The next of this AccessKeyOutputListV1.
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """
        Gets the offset of this AccessKeyOutputListV1.
        The pagination offset, the index of the first collection item that will be returned in this page of results

        :return: The offset of this AccessKeyOutputListV1.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this AccessKeyOutputListV1.
        The pagination offset, the index of the first collection item that will be returned in this page of results

        :param offset: The offset of this AccessKeyOutputListV1.
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """
        Gets the prev of this AccessKeyOutputListV1.
        The href of the previous set of paginated results

        :return: The prev of this AccessKeyOutputListV1.
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """
        Sets the prev of this AccessKeyOutputListV1.
        The href of the previous set of paginated results

        :param prev: The prev of this AccessKeyOutputListV1.
        :type: str
        """

        self._prev = prev

    @property
    def status_message(self):
        """
        Gets the status_message of this AccessKeyOutputListV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this AccessKeyOutputListV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this AccessKeyOutputListV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this AccessKeyOutputListV1.
        :type: str
        """

        self._status_message = status_message

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
        if not isinstance(other, AccessKeyOutputListV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

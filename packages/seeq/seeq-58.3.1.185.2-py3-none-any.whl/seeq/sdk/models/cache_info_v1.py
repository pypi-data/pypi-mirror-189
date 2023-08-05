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


class CacheInfoV1(object):
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
        'cache_id': 'str',
        'cached_regions': 'ValidityRegionsOutputV1',
        'status_message': 'str'
    }

    attribute_map = {
        'cache_id': 'cacheId',
        'cached_regions': 'cachedRegions',
        'status_message': 'statusMessage'
    }

    def __init__(self, cache_id=None, cached_regions=None, status_message=None):
        """
        CacheInfoV1 - a model defined in Swagger
        """

        self._cache_id = None
        self._cached_regions = None
        self._status_message = None

        if cache_id is not None:
          self.cache_id = cache_id
        if cached_regions is not None:
          self.cached_regions = cached_regions
        if status_message is not None:
          self.status_message = status_message

    @property
    def cache_id(self):
        """
        Gets the cache_id of this CacheInfoV1.
        The ID of the cache for this item

        :return: The cache_id of this CacheInfoV1.
        :rtype: str
        """
        return self._cache_id

    @cache_id.setter
    def cache_id(self, cache_id):
        """
        Sets the cache_id of this CacheInfoV1.
        The ID of the cache for this item

        :param cache_id: The cache_id of this CacheInfoV1.
        :type: str
        """

        self._cache_id = cache_id

    @property
    def cached_regions(self):
        """
        Gets the cached_regions of this CacheInfoV1.

        :return: The cached_regions of this CacheInfoV1.
        :rtype: ValidityRegionsOutputV1
        """
        return self._cached_regions

    @cached_regions.setter
    def cached_regions(self, cached_regions):
        """
        Sets the cached_regions of this CacheInfoV1.

        :param cached_regions: The cached_regions of this CacheInfoV1.
        :type: ValidityRegionsOutputV1
        """

        self._cached_regions = cached_regions

    @property
    def status_message(self):
        """
        Gets the status_message of this CacheInfoV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this CacheInfoV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this CacheInfoV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this CacheInfoV1.
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
        if not isinstance(other, CacheInfoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

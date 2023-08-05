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


class IndexingParametersInputV1(object):
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
        'source_agent_name': 'str',
        'sync_mode': 'str'
    }

    attribute_map = {
        'source_agent_name': 'sourceAgentName',
        'sync_mode': 'syncMode'
    }

    def __init__(self, source_agent_name=None, sync_mode=None):
        """
        IndexingParametersInputV1 - a model defined in Swagger
        """

        self._source_agent_name = None
        self._sync_mode = None

        if source_agent_name is not None:
          self.source_agent_name = source_agent_name
        if sync_mode is not None:
          self.sync_mode = sync_mode

    @property
    def source_agent_name(self):
        """
        Gets the source_agent_name of this IndexingParametersInputV1.
        The name of the agent requesting the index.

        :return: The source_agent_name of this IndexingParametersInputV1.
        :rtype: str
        """
        return self._source_agent_name

    @source_agent_name.setter
    def source_agent_name(self, source_agent_name):
        """
        Sets the source_agent_name of this IndexingParametersInputV1.
        The name of the agent requesting the index.

        :param source_agent_name: The source_agent_name of this IndexingParametersInputV1.
        :type: str
        """

        self._source_agent_name = source_agent_name

    @property
    def sync_mode(self):
        """
        Gets the sync_mode of this IndexingParametersInputV1.
        The sync mode. Please use one of: FULL, INCREMENTAL

        :return: The sync_mode of this IndexingParametersInputV1.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        """
        Sets the sync_mode of this IndexingParametersInputV1.
        The sync mode. Please use one of: FULL, INCREMENTAL

        :param sync_mode: The sync_mode of this IndexingParametersInputV1.
        :type: str
        """

        self._sync_mode = sync_mode

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
        if not isinstance(other, IndexingParametersInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

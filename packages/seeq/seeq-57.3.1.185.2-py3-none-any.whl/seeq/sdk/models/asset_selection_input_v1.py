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


class AssetSelectionInputV1(object):
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
        'archived': 'bool',
        'asset_id': 'str',
        'asset_path_depth': 'int',
        'description': 'str',
        'name': 'str',
        'report_id': 'str',
        'selection_id': 'str'
    }

    attribute_map = {
        'archived': 'archived',
        'asset_id': 'assetId',
        'asset_path_depth': 'assetPathDepth',
        'description': 'description',
        'name': 'name',
        'report_id': 'reportId',
        'selection_id': 'selectionId'
    }

    def __init__(self, archived=False, asset_id=None, asset_path_depth=None, description=None, name=None, report_id=None, selection_id=None):
        """
        AssetSelectionInputV1 - a model defined in Swagger
        """

        self._archived = None
        self._asset_id = None
        self._asset_path_depth = None
        self._description = None
        self._name = None
        self._report_id = None
        self._selection_id = None

        if archived is not None:
          self.archived = archived
        if asset_id is not None:
          self.asset_id = asset_id
        if asset_path_depth is not None:
          self.asset_path_depth = asset_path_depth
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if report_id is not None:
          self.report_id = report_id
        if selection_id is not None:
          self.selection_id = selection_id

    @property
    def archived(self):
        """
        Gets the archived of this AssetSelectionInputV1.
        Whether the assetSelection should be archived

        :return: The archived of this AssetSelectionInputV1.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this AssetSelectionInputV1.
        Whether the assetSelection should be archived

        :param archived: The archived of this AssetSelectionInputV1.
        :type: bool
        """

        self._archived = archived

    @property
    def asset_id(self):
        """
        Gets the asset_id of this AssetSelectionInputV1.
        The asset selected

        :return: The asset_id of this AssetSelectionInputV1.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """
        Sets the asset_id of this AssetSelectionInputV1.
        The asset selected

        :param asset_id: The asset_id of this AssetSelectionInputV1.
        :type: str
        """
        if asset_id is None:
            raise ValueError("Invalid value for `asset_id`, must not be `None`")

        self._asset_id = asset_id

    @property
    def asset_path_depth(self):
        """
        Gets the asset_path_depth of this AssetSelectionInputV1.
        Max depth for asset path name for this selection

        :return: The asset_path_depth of this AssetSelectionInputV1.
        :rtype: int
        """
        return self._asset_path_depth

    @asset_path_depth.setter
    def asset_path_depth(self, asset_path_depth):
        """
        Sets the asset_path_depth of this AssetSelectionInputV1.
        Max depth for asset path name for this selection

        :param asset_path_depth: The asset_path_depth of this AssetSelectionInputV1.
        :type: int
        """

        self._asset_path_depth = asset_path_depth

    @property
    def description(self):
        """
        Gets the description of this AssetSelectionInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :return: The description of this AssetSelectionInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AssetSelectionInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :param description: The description of this AssetSelectionInputV1.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this AssetSelectionInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this AssetSelectionInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssetSelectionInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this AssetSelectionInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def report_id(self):
        """
        Gets the report_id of this AssetSelectionInputV1.
        The asset selection's report

        :return: The report_id of this AssetSelectionInputV1.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """
        Sets the report_id of this AssetSelectionInputV1.
        The asset selection's report

        :param report_id: The report_id of this AssetSelectionInputV1.
        :type: str
        """

        self._report_id = report_id

    @property
    def selection_id(self):
        """
        Gets the selection_id of this AssetSelectionInputV1.
        Seeq Id for the asset selection

        :return: The selection_id of this AssetSelectionInputV1.
        :rtype: str
        """
        return self._selection_id

    @selection_id.setter
    def selection_id(self, selection_id):
        """
        Sets the selection_id of this AssetSelectionInputV1.
        Seeq Id for the asset selection

        :param selection_id: The selection_id of this AssetSelectionInputV1.
        :type: str
        """

        self._selection_id = selection_id

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
        if not isinstance(other, AssetSelectionInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

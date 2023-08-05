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


class AssetGroupInputV1(object):
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
        'child_assets': 'list[AssetGroupAssetInputV1]',
        'root_asset': 'AssetGroupRootInputV1'
    }

    attribute_map = {
        'child_assets': 'childAssets',
        'root_asset': 'rootAsset'
    }

    def __init__(self, child_assets=None, root_asset=None):
        """
        AssetGroupInputV1 - a model defined in Swagger
        """

        self._child_assets = None
        self._root_asset = None

        if child_assets is not None:
          self.child_assets = child_assets
        if root_asset is not None:
          self.root_asset = root_asset

    @property
    def child_assets(self):
        """
        Gets the child_assets of this AssetGroupInputV1.
        List of children for the asset tree

        :return: The child_assets of this AssetGroupInputV1.
        :rtype: list[AssetGroupAssetInputV1]
        """
        return self._child_assets

    @child_assets.setter
    def child_assets(self, child_assets):
        """
        Sets the child_assets of this AssetGroupInputV1.
        List of children for the asset tree

        :param child_assets: The child_assets of this AssetGroupInputV1.
        :type: list[AssetGroupAssetInputV1]
        """

        self._child_assets = child_assets

    @property
    def root_asset(self):
        """
        Gets the root_asset of this AssetGroupInputV1.

        :return: The root_asset of this AssetGroupInputV1.
        :rtype: AssetGroupRootInputV1
        """
        return self._root_asset

    @root_asset.setter
    def root_asset(self, root_asset):
        """
        Sets the root_asset of this AssetGroupInputV1.

        :param root_asset: The root_asset of this AssetGroupInputV1.
        :type: AssetGroupRootInputV1
        """

        self._root_asset = root_asset

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
        if not isinstance(other, AssetGroupInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

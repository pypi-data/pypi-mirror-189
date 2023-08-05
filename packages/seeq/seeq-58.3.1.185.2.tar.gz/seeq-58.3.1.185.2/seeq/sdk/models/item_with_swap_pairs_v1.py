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


class ItemWithSwapPairsV1(object):
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
        'item': 'ItemPreviewWithAssetsV1',
        'parameter_match': 'float',
        'swap_pairs': 'list[SwapInputV1]'
    }

    attribute_map = {
        'item': 'item',
        'parameter_match': 'parameterMatch',
        'swap_pairs': 'swapPairs'
    }

    def __init__(self, item=None, parameter_match=None, swap_pairs=None):
        """
        ItemWithSwapPairsV1 - a model defined in Swagger
        """

        self._item = None
        self._parameter_match = None
        self._swap_pairs = None

        if item is not None:
          self.item = item
        if parameter_match is not None:
          self.parameter_match = parameter_match
        if swap_pairs is not None:
          self.swap_pairs = swap_pairs

    @property
    def item(self):
        """
        Gets the item of this ItemWithSwapPairsV1.

        :return: The item of this ItemWithSwapPairsV1.
        :rtype: ItemPreviewWithAssetsV1
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this ItemWithSwapPairsV1.

        :param item: The item of this ItemWithSwapPairsV1.
        :type: ItemPreviewWithAssetsV1
        """
        if item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")

        self._item = item

    @property
    def parameter_match(self):
        """
        Gets the parameter_match of this ItemWithSwapPairsV1.
        The ratio of matched to total parameters

        :return: The parameter_match of this ItemWithSwapPairsV1.
        :rtype: float
        """
        return self._parameter_match

    @parameter_match.setter
    def parameter_match(self, parameter_match):
        """
        Sets the parameter_match of this ItemWithSwapPairsV1.
        The ratio of matched to total parameters

        :param parameter_match: The parameter_match of this ItemWithSwapPairsV1.
        :type: float
        """
        if parameter_match is None:
            raise ValueError("Invalid value for `parameter_match`, must not be `None`")

        self._parameter_match = parameter_match

    @property
    def swap_pairs(self):
        """
        Gets the swap_pairs of this ItemWithSwapPairsV1.
        The list of swap pairs needed to perform the swap.

        :return: The swap_pairs of this ItemWithSwapPairsV1.
        :rtype: list[SwapInputV1]
        """
        return self._swap_pairs

    @swap_pairs.setter
    def swap_pairs(self, swap_pairs):
        """
        Sets the swap_pairs of this ItemWithSwapPairsV1.
        The list of swap pairs needed to perform the swap.

        :param swap_pairs: The swap_pairs of this ItemWithSwapPairsV1.
        :type: list[SwapInputV1]
        """
        if swap_pairs is None:
            raise ValueError("Invalid value for `swap_pairs`, must not be `None`")

        self._swap_pairs = swap_pairs

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
        if not isinstance(other, ItemWithSwapPairsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class SeeAlsoDocOutputV1(object):
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
        'children': 'list[SeeAlsoDocOutputV1]',
        'documentation_href': 'str',
        'short_description': 'str',
        'title': 'str'
    }

    attribute_map = {
        'children': 'children',
        'documentation_href': 'documentationHref',
        'short_description': 'shortDescription',
        'title': 'title'
    }

    def __init__(self, children=None, documentation_href=None, short_description=None, title=None):
        """
        SeeAlsoDocOutputV1 - a model defined in Swagger
        """

        self._children = None
        self._documentation_href = None
        self._short_description = None
        self._title = None

        if children is not None:
          self.children = children
        if documentation_href is not None:
          self.documentation_href = documentation_href
        if short_description is not None:
          self.short_description = short_description
        if title is not None:
          self.title = title

    @property
    def children(self):
        """
        Gets the children of this SeeAlsoDocOutputV1.
        Children links of this document

        :return: The children of this SeeAlsoDocOutputV1.
        :rtype: list[SeeAlsoDocOutputV1]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this SeeAlsoDocOutputV1.
        Children links of this document

        :param children: The children of this SeeAlsoDocOutputV1.
        :type: list[SeeAlsoDocOutputV1]
        """

        self._children = children

    @property
    def documentation_href(self):
        """
        Gets the documentation_href of this SeeAlsoDocOutputV1.
        The href of the link

        :return: The documentation_href of this SeeAlsoDocOutputV1.
        :rtype: str
        """
        return self._documentation_href

    @documentation_href.setter
    def documentation_href(self, documentation_href):
        """
        Sets the documentation_href of this SeeAlsoDocOutputV1.
        The href of the link

        :param documentation_href: The documentation_href of this SeeAlsoDocOutputV1.
        :type: str
        """

        self._documentation_href = documentation_href

    @property
    def short_description(self):
        """
        Gets the short_description of this SeeAlsoDocOutputV1.
        A short description of the linked content

        :return: The short_description of this SeeAlsoDocOutputV1.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this SeeAlsoDocOutputV1.
        A short description of the linked content

        :param short_description: The short_description of this SeeAlsoDocOutputV1.
        :type: str
        """

        self._short_description = short_description

    @property
    def title(self):
        """
        Gets the title of this SeeAlsoDocOutputV1.
        The title of the link

        :return: The title of this SeeAlsoDocOutputV1.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this SeeAlsoDocOutputV1.
        The title of the link

        :param title: The title of this SeeAlsoDocOutputV1.
        :type: str
        """

        self._title = title

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
        if not isinstance(other, SeeAlsoDocOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

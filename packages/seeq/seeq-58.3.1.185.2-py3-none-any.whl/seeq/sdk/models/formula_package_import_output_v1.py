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


class FormulaPackageImportOutputV1(object):
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
        'docs': 'list[FormulaDocOutputV1]',
        'errors': 'list[str]',
        'formula_package': 'FormulaPackageOutputV1',
        'functions': 'list[CalculatedItemOutputV1]'
    }

    attribute_map = {
        'docs': 'docs',
        'errors': 'errors',
        'formula_package': 'formulaPackage',
        'functions': 'functions'
    }

    def __init__(self, docs=None, errors=None, formula_package=None, functions=None):
        """
        FormulaPackageImportOutputV1 - a model defined in Swagger
        """

        self._docs = None
        self._errors = None
        self._formula_package = None
        self._functions = None

        if docs is not None:
          self.docs = docs
        if errors is not None:
          self.errors = errors
        if formula_package is not None:
          self.formula_package = formula_package
        if functions is not None:
          self.functions = functions

    @property
    def docs(self):
        """
        Gets the docs of this FormulaPackageImportOutputV1.
        The list of results from doc updates. The Nth output corresponds to the Nth input.

        :return: The docs of this FormulaPackageImportOutputV1.
        :rtype: list[FormulaDocOutputV1]
        """
        return self._docs

    @docs.setter
    def docs(self, docs):
        """
        Sets the docs of this FormulaPackageImportOutputV1.
        The list of results from doc updates. The Nth output corresponds to the Nth input.

        :param docs: The docs of this FormulaPackageImportOutputV1.
        :type: list[FormulaDocOutputV1]
        """

        self._docs = docs

    @property
    def errors(self):
        """
        Gets the errors of this FormulaPackageImportOutputV1.
        If there were any errors during sync, they will be listed here and the other objects will be empty.

        :return: The errors of this FormulaPackageImportOutputV1.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this FormulaPackageImportOutputV1.
        If there were any errors during sync, they will be listed here and the other objects will be empty.

        :param errors: The errors of this FormulaPackageImportOutputV1.
        :type: list[str]
        """

        self._errors = errors

    @property
    def formula_package(self):
        """
        Gets the formula_package of this FormulaPackageImportOutputV1.

        :return: The formula_package of this FormulaPackageImportOutputV1.
        :rtype: FormulaPackageOutputV1
        """
        return self._formula_package

    @formula_package.setter
    def formula_package(self, formula_package):
        """
        Sets the formula_package of this FormulaPackageImportOutputV1.

        :param formula_package: The formula_package of this FormulaPackageImportOutputV1.
        :type: FormulaPackageOutputV1
        """

        self._formula_package = formula_package

    @property
    def functions(self):
        """
        Gets the functions of this FormulaPackageImportOutputV1.
        The list of results from the function updates. The Nth output corresponds to the Nth input.

        :return: The functions of this FormulaPackageImportOutputV1.
        :rtype: list[CalculatedItemOutputV1]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this FormulaPackageImportOutputV1.
        The list of results from the function updates. The Nth output corresponds to the Nth input.

        :param functions: The functions of this FormulaPackageImportOutputV1.
        :type: list[CalculatedItemOutputV1]
        """

        self._functions = functions

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
        if not isinstance(other, FormulaPackageImportOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

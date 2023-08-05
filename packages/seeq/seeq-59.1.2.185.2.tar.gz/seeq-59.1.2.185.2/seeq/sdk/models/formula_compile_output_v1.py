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


class FormulaCompileOutputV1(object):
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
        'errors': 'list[FormulaCompilerErrorOutputV1]',
        'metadata': 'dict(str, str)',
        'return_type': 'str',
        'status_message': 'str',
        'upgrade_details': 'FormulaUpgradeOutputV1'
    }

    attribute_map = {
        'errors': 'errors',
        'metadata': 'metadata',
        'return_type': 'returnType',
        'status_message': 'statusMessage',
        'upgrade_details': 'upgradeDetails'
    }

    def __init__(self, errors=None, metadata=None, return_type=None, status_message=None, upgrade_details=None):
        """
        FormulaCompileOutputV1 - a model defined in Swagger
        """

        self._errors = None
        self._metadata = None
        self._return_type = None
        self._status_message = None
        self._upgrade_details = None

        if errors is not None:
          self.errors = errors
        if metadata is not None:
          self.metadata = metadata
        if return_type is not None:
          self.return_type = return_type
        if status_message is not None:
          self.status_message = status_message
        if upgrade_details is not None:
          self.upgrade_details = upgrade_details

    @property
    def errors(self):
        """
        Gets the errors of this FormulaCompileOutputV1.
        Errors (if any) from the formula

        :return: The errors of this FormulaCompileOutputV1.
        :rtype: list[FormulaCompilerErrorOutputV1]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this FormulaCompileOutputV1.
        Errors (if any) from the formula

        :param errors: The errors of this FormulaCompileOutputV1.
        :type: list[FormulaCompilerErrorOutputV1]
        """

        self._errors = errors

    @property
    def metadata(self):
        """
        Gets the metadata of this FormulaCompileOutputV1.
        Metadata describing the compiled formula's result

        :return: The metadata of this FormulaCompileOutputV1.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this FormulaCompileOutputV1.
        Metadata describing the compiled formula's result

        :param metadata: The metadata of this FormulaCompileOutputV1.
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def return_type(self):
        """
        Gets the return_type of this FormulaCompileOutputV1.
        The data type of the compiled formula's result

        :return: The return_type of this FormulaCompileOutputV1.
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """
        Sets the return_type of this FormulaCompileOutputV1.
        The data type of the compiled formula's result

        :param return_type: The return_type of this FormulaCompileOutputV1.
        :type: str
        """

        self._return_type = return_type

    @property
    def status_message(self):
        """
        Gets the status_message of this FormulaCompileOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this FormulaCompileOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this FormulaCompileOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this FormulaCompileOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def upgrade_details(self):
        """
        Gets the upgrade_details of this FormulaCompileOutputV1.

        :return: The upgrade_details of this FormulaCompileOutputV1.
        :rtype: FormulaUpgradeOutputV1
        """
        return self._upgrade_details

    @upgrade_details.setter
    def upgrade_details(self, upgrade_details):
        """
        Sets the upgrade_details of this FormulaCompileOutputV1.

        :param upgrade_details: The upgrade_details of this FormulaCompileOutputV1.
        :type: FormulaUpgradeOutputV1
        """

        self._upgrade_details = upgrade_details

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
        if not isinstance(other, FormulaCompileOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class LicenseImporterOutputV1(object):
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
        'license_imported': 'str',
        'licenses_archived': 'list[str]'
    }

    attribute_map = {
        'license_imported': 'licenseImported',
        'licenses_archived': 'licensesArchived'
    }

    def __init__(self, license_imported=None, licenses_archived=None):
        """
        LicenseImporterOutputV1 - a model defined in Swagger
        """

        self._license_imported = None
        self._licenses_archived = None

        if license_imported is not None:
          self.license_imported = license_imported
        if licenses_archived is not None:
          self.licenses_archived = licenses_archived

    @property
    def license_imported(self):
        """
        Gets the license_imported of this LicenseImporterOutputV1.
        The name of the license that was imported

        :return: The license_imported of this LicenseImporterOutputV1.
        :rtype: str
        """
        return self._license_imported

    @license_imported.setter
    def license_imported(self, license_imported):
        """
        Sets the license_imported of this LicenseImporterOutputV1.
        The name of the license that was imported

        :param license_imported: The license_imported of this LicenseImporterOutputV1.
        :type: str
        """

        self._license_imported = license_imported

    @property
    def licenses_archived(self):
        """
        Gets the licenses_archived of this LicenseImporterOutputV1.
        The names of licenses that were archived to the 'licenses/old' folder

        :return: The licenses_archived of this LicenseImporterOutputV1.
        :rtype: list[str]
        """
        return self._licenses_archived

    @licenses_archived.setter
    def licenses_archived(self, licenses_archived):
        """
        Sets the licenses_archived of this LicenseImporterOutputV1.
        The names of licenses that were archived to the 'licenses/old' folder

        :param licenses_archived: The licenses_archived of this LicenseImporterOutputV1.
        :type: list[str]
        """

        self._licenses_archived = licenses_archived

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
        if not isinstance(other, LicenseImporterOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

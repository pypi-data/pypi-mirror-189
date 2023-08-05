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


class ConfigurationOptionOutputV1(object):
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
        'advanced': 'bool',
        'allowed_values': 'str',
        'default_dependencies': 'list[str]',
        'default_description': 'str',
        'default_value': 'object',
        'description': 'str',
        'modifiable': 'bool',
        'note': 'str',
        'path': 'str',
        'registration': 'str',
        'registration_description': 'str',
        'units': 'str',
        'value': 'object'
    }

    attribute_map = {
        'advanced': 'advanced',
        'allowed_values': 'allowedValues',
        'default_dependencies': 'defaultDependencies',
        'default_description': 'defaultDescription',
        'default_value': 'defaultValue',
        'description': 'description',
        'modifiable': 'modifiable',
        'note': 'note',
        'path': 'path',
        'registration': 'registration',
        'registration_description': 'registrationDescription',
        'units': 'units',
        'value': 'value'
    }

    def __init__(self, advanced=None, allowed_values=None, default_dependencies=None, default_description=None, default_value=None, description=None, modifiable=None, note=None, path=None, registration=None, registration_description=None, units=None, value=None):
        """
        ConfigurationOptionOutputV1 - a model defined in Swagger
        """

        self._advanced = None
        self._allowed_values = None
        self._default_dependencies = None
        self._default_description = None
        self._default_value = None
        self._description = None
        self._modifiable = None
        self._note = None
        self._path = None
        self._registration = None
        self._registration_description = None
        self._units = None
        self._value = None

        if advanced is not None:
          self.advanced = advanced
        if allowed_values is not None:
          self.allowed_values = allowed_values
        if default_dependencies is not None:
          self.default_dependencies = default_dependencies
        if default_description is not None:
          self.default_description = default_description
        if default_value is not None:
          self.default_value = default_value
        if description is not None:
          self.description = description
        if modifiable is not None:
          self.modifiable = modifiable
        if note is not None:
          self.note = note
        if path is not None:
          self.path = path
        if registration is not None:
          self.registration = registration
        if registration_description is not None:
          self.registration_description = registration_description
        if units is not None:
          self.units = units
        if value is not None:
          self.value = value

    @property
    def advanced(self):
        """
        Gets the advanced of this ConfigurationOptionOutputV1.

        :return: The advanced of this ConfigurationOptionOutputV1.
        :rtype: bool
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """
        Sets the advanced of this ConfigurationOptionOutputV1.

        :param advanced: The advanced of this ConfigurationOptionOutputV1.
        :type: bool
        """

        self._advanced = advanced

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this ConfigurationOptionOutputV1.

        :return: The allowed_values of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this ConfigurationOptionOutputV1.

        :param allowed_values: The allowed_values of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._allowed_values = allowed_values

    @property
    def default_dependencies(self):
        """
        Gets the default_dependencies of this ConfigurationOptionOutputV1.

        :return: The default_dependencies of this ConfigurationOptionOutputV1.
        :rtype: list[str]
        """
        return self._default_dependencies

    @default_dependencies.setter
    def default_dependencies(self, default_dependencies):
        """
        Sets the default_dependencies of this ConfigurationOptionOutputV1.

        :param default_dependencies: The default_dependencies of this ConfigurationOptionOutputV1.
        :type: list[str]
        """

        self._default_dependencies = default_dependencies

    @property
    def default_description(self):
        """
        Gets the default_description of this ConfigurationOptionOutputV1.

        :return: The default_description of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._default_description

    @default_description.setter
    def default_description(self, default_description):
        """
        Sets the default_description of this ConfigurationOptionOutputV1.

        :param default_description: The default_description of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._default_description = default_description

    @property
    def default_value(self):
        """
        Gets the default_value of this ConfigurationOptionOutputV1.

        :return: The default_value of this ConfigurationOptionOutputV1.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ConfigurationOptionOutputV1.

        :param default_value: The default_value of this ConfigurationOptionOutputV1.
        :type: object
        """

        self._default_value = default_value

    @property
    def description(self):
        """
        Gets the description of this ConfigurationOptionOutputV1.

        :return: The description of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationOptionOutputV1.

        :param description: The description of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._description = description

    @property
    def modifiable(self):
        """
        Gets the modifiable of this ConfigurationOptionOutputV1.

        :return: The modifiable of this ConfigurationOptionOutputV1.
        :rtype: bool
        """
        return self._modifiable

    @modifiable.setter
    def modifiable(self, modifiable):
        """
        Sets the modifiable of this ConfigurationOptionOutputV1.

        :param modifiable: The modifiable of this ConfigurationOptionOutputV1.
        :type: bool
        """

        self._modifiable = modifiable

    @property
    def note(self):
        """
        Gets the note of this ConfigurationOptionOutputV1.

        :return: The note of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this ConfigurationOptionOutputV1.

        :param note: The note of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._note = note

    @property
    def path(self):
        """
        Gets the path of this ConfigurationOptionOutputV1.

        :return: The path of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ConfigurationOptionOutputV1.

        :param path: The path of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._path = path

    @property
    def registration(self):
        """
        Gets the registration of this ConfigurationOptionOutputV1.

        :return: The registration of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._registration

    @registration.setter
    def registration(self, registration):
        """
        Sets the registration of this ConfigurationOptionOutputV1.

        :param registration: The registration of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._registration = registration

    @property
    def registration_description(self):
        """
        Gets the registration_description of this ConfigurationOptionOutputV1.

        :return: The registration_description of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._registration_description

    @registration_description.setter
    def registration_description(self, registration_description):
        """
        Sets the registration_description of this ConfigurationOptionOutputV1.

        :param registration_description: The registration_description of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._registration_description = registration_description

    @property
    def units(self):
        """
        Gets the units of this ConfigurationOptionOutputV1.

        :return: The units of this ConfigurationOptionOutputV1.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this ConfigurationOptionOutputV1.

        :param units: The units of this ConfigurationOptionOutputV1.
        :type: str
        """

        self._units = units

    @property
    def value(self):
        """
        Gets the value of this ConfigurationOptionOutputV1.

        :return: The value of this ConfigurationOptionOutputV1.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ConfigurationOptionOutputV1.

        :param value: The value of this ConfigurationOptionOutputV1.
        :type: object
        """

        self._value = value

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
        if not isinstance(other, ConfigurationOptionOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

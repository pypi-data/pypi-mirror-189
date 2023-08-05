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


class FormulaItemInputV1(object):
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
        'additional_properties': 'list[ScalarPropertyV1]',
        'data_id': 'str',
        'data_version_check': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'dependencies': 'list[FormulaDependencyInputV1]',
        'description': 'str',
        'formula': 'str',
        'host_id': 'str',
        'id': 'str',
        'name': 'str',
        'package_name': 'str',
        'parameters': 'list[FormulaParameterInputV1]',
        'scoped_to': 'str',
        'security_string': 'str',
        'source_security_string': 'str',
        'sync_token': 'str',
        'type': 'str'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'data_id': 'dataId',
        'data_version_check': 'dataVersionCheck',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'dependencies': 'dependencies',
        'description': 'description',
        'formula': 'formula',
        'host_id': 'hostId',
        'id': 'id',
        'name': 'name',
        'package_name': 'packageName',
        'parameters': 'parameters',
        'scoped_to': 'scopedTo',
        'security_string': 'securityString',
        'source_security_string': 'sourceSecurityString',
        'sync_token': 'syncToken',
        'type': 'type'
    }

    def __init__(self, additional_properties=None, data_id=None, data_version_check=None, datasource_class=None, datasource_id=None, dependencies=None, description=None, formula=None, host_id=None, id=None, name=None, package_name=None, parameters=None, scoped_to=None, security_string=None, source_security_string=None, sync_token=None, type=None):
        """
        FormulaItemInputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._data_id = None
        self._data_version_check = None
        self._datasource_class = None
        self._datasource_id = None
        self._dependencies = None
        self._description = None
        self._formula = None
        self._host_id = None
        self._id = None
        self._name = None
        self._package_name = None
        self._parameters = None
        self._scoped_to = None
        self._security_string = None
        self._source_security_string = None
        self._sync_token = None
        self._type = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if data_id is not None:
          self.data_id = data_id
        if data_version_check is not None:
          self.data_version_check = data_version_check
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if dependencies is not None:
          self.dependencies = dependencies
        if description is not None:
          self.description = description
        if formula is not None:
          self.formula = formula
        if host_id is not None:
          self.host_id = host_id
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if package_name is not None:
          self.package_name = package_name
        if parameters is not None:
          self.parameters = parameters
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if security_string is not None:
          self.security_string = security_string
        if source_security_string is not None:
          self.source_security_string = source_security_string
        if sync_token is not None:
          self.sync_token = sync_token
        if type is not None:
          self.type = type

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this FormulaItemInputV1.
        Additional properties to set on this item. A property consists of a name, a value, and a unit of measure.

        :return: The additional_properties of this FormulaItemInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this FormulaItemInputV1.
        Additional properties to set on this item. A property consists of a name, a value, and a unit of measure.

        :param additional_properties: The additional_properties of this FormulaItemInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def data_id(self):
        """
        Gets the data_id of this FormulaItemInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this FormulaItemInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this FormulaItemInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this FormulaItemInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def data_version_check(self):
        """
        Gets the data_version_check of this FormulaItemInputV1.
        The data version check string. When updating an existing series, if the data version check string is unchanged, then the update will be skipped.

        :return: The data_version_check of this FormulaItemInputV1.
        :rtype: str
        """
        return self._data_version_check

    @data_version_check.setter
    def data_version_check(self, data_version_check):
        """
        Sets the data_version_check of this FormulaItemInputV1.
        The data version check string. When updating an existing series, if the data version check string is unchanged, then the update will be skipped.

        :param data_version_check: The data_version_check of this FormulaItemInputV1.
        :type: str
        """

        self._data_version_check = data_version_check

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this FormulaItemInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_class of this FormulaItemInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this FormulaItemInputV1.
        Along with the Datasource ID, the Datasource Class uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_class: The datasource_class of this FormulaItemInputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this FormulaItemInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :return: The datasource_id of this FormulaItemInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this FormulaItemInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an OSIsoft PI historian.

        :param datasource_id: The datasource_id of this FormulaItemInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def dependencies(self):
        """
        Gets the dependencies of this FormulaItemInputV1.
        List of items the formula is dependent on

        :return: The dependencies of this FormulaItemInputV1.
        :rtype: list[FormulaDependencyInputV1]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this FormulaItemInputV1.
        List of items the formula is dependent on

        :param dependencies: The dependencies of this FormulaItemInputV1.
        :type: list[FormulaDependencyInputV1]
        """

        self._dependencies = dependencies

    @property
    def description(self):
        """
        Gets the description of this FormulaItemInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :return: The description of this FormulaItemInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FormulaItemInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :param description: The description of this FormulaItemInputV1.
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """
        Gets the formula of this FormulaItemInputV1.
        The formula that represents the body of the function

        :return: The formula of this FormulaItemInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FormulaItemInputV1.
        The formula that represents the body of the function

        :param formula: The formula of this FormulaItemInputV1.
        :type: str
        """
        if formula is None:
            raise ValueError("Invalid value for `formula`, must not be `None`")

        self._formula = formula

    @property
    def host_id(self):
        """
        Gets the host_id of this FormulaItemInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :return: The host_id of this FormulaItemInputV1.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this FormulaItemInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :param host_id: The host_id of this FormulaItemInputV1.
        :type: str
        """

        self._host_id = host_id

    @property
    def id(self):
        """
        Gets the id of this FormulaItemInputV1.
        The Seeq id of the formula item

        :return: The id of this FormulaItemInputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FormulaItemInputV1.
        The Seeq id of the formula item

        :param id: The id of this FormulaItemInputV1.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FormulaItemInputV1.
        Human readable name. Null or whitespace names are not permitted.

        :return: The name of this FormulaItemInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormulaItemInputV1.
        Human readable name. Null or whitespace names are not permitted.

        :param name: The name of this FormulaItemInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def package_name(self):
        """
        Gets the package_name of this FormulaItemInputV1.
        The name of the package that contains this function. Valid only for UserDefinedFormulaFunctions.

        :return: The package_name of this FormulaItemInputV1.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this FormulaItemInputV1.
        The name of the package that contains this function. Valid only for UserDefinedFormulaFunctions.

        :param package_name: The package_name of this FormulaItemInputV1.
        :type: str
        """

        self._package_name = package_name

    @property
    def parameters(self):
        """
        Gets the parameters of this FormulaItemInputV1.
        Any parameters that should be placed in the context of the executing formula. At least one unbound parameter is required.

        :return: The parameters of this FormulaItemInputV1.
        :rtype: list[FormulaParameterInputV1]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this FormulaItemInputV1.
        Any parameters that should be placed in the context of the executing formula. At least one unbound parameter is required.

        :param parameters: The parameters of this FormulaItemInputV1.
        :type: list[FormulaParameterInputV1]
        """

        self._parameters = parameters

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this FormulaItemInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this FormulaItemInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this FormulaItemInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this FormulaItemInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def security_string(self):
        """
        Gets the security_string of this FormulaItemInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :return: The security_string of this FormulaItemInputV1.
        :rtype: str
        """
        return self._security_string

    @security_string.setter
    def security_string(self, security_string):
        """
        Sets the security_string of this FormulaItemInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :param security_string: The security_string of this FormulaItemInputV1.
        :type: str
        """

        self._security_string = security_string

    @property
    def source_security_string(self):
        """
        Gets the source_security_string of this FormulaItemInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :return: The source_security_string of this FormulaItemInputV1.
        :rtype: str
        """
        return self._source_security_string

    @source_security_string.setter
    def source_security_string(self, source_security_string):
        """
        Sets the source_security_string of this FormulaItemInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :param source_security_string: The source_security_string of this FormulaItemInputV1.
        :type: str
        """

        self._source_security_string = source_security_string

    @property
    def sync_token(self):
        """
        Gets the sync_token of this FormulaItemInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :return: The sync_token of this FormulaItemInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this FormulaItemInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this FormulaItemInputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def type(self):
        """
        Gets the type of this FormulaItemInputV1.
        The item subtype for a Formula Function. Valid types include 'AggregatingFormulaFunction', 'UserDefinedFormulaFunction', and 'Chart'

        :return: The type of this FormulaItemInputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FormulaItemInputV1.
        The item subtype for a Formula Function. Valid types include 'AggregatingFormulaFunction', 'UserDefinedFormulaFunction', and 'Chart'

        :param type: The type of this FormulaItemInputV1.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, FormulaItemInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

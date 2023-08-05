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


class FormulaDocOutputV1(object):
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
        'constants': 'list[str]',
        'description': 'str',
        'doc_created_at': 'str',
        'doc_updated_at': 'str',
        'documentation_href': 'str',
        'examples': 'list[FormulaExampleOutputV1]',
        'excel_synonyms': 'list[str]',
        'function_group_id': 'str',
        'functions': 'list[FunctionVariantOutputV1]',
        'keywords': 'list[str]',
        'package_created_at': 'str',
        'package_creator_contact_info': 'str',
        'package_creator_name': 'str',
        'package_id': 'str',
        'package_installer_name': 'str',
        'package_updated_at': 'str',
        'package_version': 'str',
        'parameters': 'list[ParameterDocOutputV1]',
        'parents': 'list[SeeAlsoDocOutputV1]',
        'see_alsos': 'list[SeeAlsoDocOutputV1]',
        'title': 'str'
    }

    attribute_map = {
        'children': 'children',
        'constants': 'constants',
        'description': 'description',
        'doc_created_at': 'docCreatedAt',
        'doc_updated_at': 'docUpdatedAt',
        'documentation_href': 'documentationHref',
        'examples': 'examples',
        'excel_synonyms': 'excelSynonyms',
        'function_group_id': 'functionGroupId',
        'functions': 'functions',
        'keywords': 'keywords',
        'package_created_at': 'packageCreatedAt',
        'package_creator_contact_info': 'packageCreatorContactInfo',
        'package_creator_name': 'packageCreatorName',
        'package_id': 'packageId',
        'package_installer_name': 'packageInstallerName',
        'package_updated_at': 'packageUpdatedAt',
        'package_version': 'packageVersion',
        'parameters': 'parameters',
        'parents': 'parents',
        'see_alsos': 'seeAlsos',
        'title': 'title'
    }

    def __init__(self, children=None, constants=None, description=None, doc_created_at=None, doc_updated_at=None, documentation_href=None, examples=None, excel_synonyms=None, function_group_id=None, functions=None, keywords=None, package_created_at=None, package_creator_contact_info=None, package_creator_name=None, package_id=None, package_installer_name=None, package_updated_at=None, package_version=None, parameters=None, parents=None, see_alsos=None, title=None):
        """
        FormulaDocOutputV1 - a model defined in Swagger
        """

        self._children = None
        self._constants = None
        self._description = None
        self._doc_created_at = None
        self._doc_updated_at = None
        self._documentation_href = None
        self._examples = None
        self._excel_synonyms = None
        self._function_group_id = None
        self._functions = None
        self._keywords = None
        self._package_created_at = None
        self._package_creator_contact_info = None
        self._package_creator_name = None
        self._package_id = None
        self._package_installer_name = None
        self._package_updated_at = None
        self._package_version = None
        self._parameters = None
        self._parents = None
        self._see_alsos = None
        self._title = None

        if children is not None:
          self.children = children
        if constants is not None:
          self.constants = constants
        if description is not None:
          self.description = description
        if doc_created_at is not None:
          self.doc_created_at = doc_created_at
        if doc_updated_at is not None:
          self.doc_updated_at = doc_updated_at
        if documentation_href is not None:
          self.documentation_href = documentation_href
        if examples is not None:
          self.examples = examples
        if excel_synonyms is not None:
          self.excel_synonyms = excel_synonyms
        if function_group_id is not None:
          self.function_group_id = function_group_id
        if functions is not None:
          self.functions = functions
        if keywords is not None:
          self.keywords = keywords
        if package_created_at is not None:
          self.package_created_at = package_created_at
        if package_creator_contact_info is not None:
          self.package_creator_contact_info = package_creator_contact_info
        if package_creator_name is not None:
          self.package_creator_name = package_creator_name
        if package_id is not None:
          self.package_id = package_id
        if package_installer_name is not None:
          self.package_installer_name = package_installer_name
        if package_updated_at is not None:
          self.package_updated_at = package_updated_at
        if package_version is not None:
          self.package_version = package_version
        if parameters is not None:
          self.parameters = parameters
        if parents is not None:
          self.parents = parents
        if see_alsos is not None:
          self.see_alsos = see_alsos
        if title is not None:
          self.title = title

    @property
    def children(self):
        """
        Gets the children of this FormulaDocOutputV1.
        Child links of this document

        :return: The children of this FormulaDocOutputV1.
        :rtype: list[SeeAlsoDocOutputV1]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this FormulaDocOutputV1.
        Child links of this document

        :param children: The children of this FormulaDocOutputV1.
        :type: list[SeeAlsoDocOutputV1]
        """

        self._children = children

    @property
    def constants(self):
        """
        Gets the constants of this FormulaDocOutputV1.
        Constants provided by this document

        :return: The constants of this FormulaDocOutputV1.
        :rtype: list[str]
        """
        return self._constants

    @constants.setter
    def constants(self, constants):
        """
        Sets the constants of this FormulaDocOutputV1.
        Constants provided by this document

        :param constants: The constants of this FormulaDocOutputV1.
        :type: list[str]
        """

        self._constants = constants

    @property
    def description(self):
        """
        Gets the description of this FormulaDocOutputV1.
        The body of this document

        :return: The description of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FormulaDocOutputV1.
        The body of this document

        :param description: The description of this FormulaDocOutputV1.
        :type: str
        """

        self._description = description

    @property
    def doc_created_at(self):
        """
        Gets the doc_created_at of this FormulaDocOutputV1.
        The timestamp that this document was created at

        :return: The doc_created_at of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._doc_created_at

    @doc_created_at.setter
    def doc_created_at(self, doc_created_at):
        """
        Sets the doc_created_at of this FormulaDocOutputV1.
        The timestamp that this document was created at

        :param doc_created_at: The doc_created_at of this FormulaDocOutputV1.
        :type: str
        """

        self._doc_created_at = doc_created_at

    @property
    def doc_updated_at(self):
        """
        Gets the doc_updated_at of this FormulaDocOutputV1.
        The timestamp that this document was last updated at

        :return: The doc_updated_at of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._doc_updated_at

    @doc_updated_at.setter
    def doc_updated_at(self, doc_updated_at):
        """
        Sets the doc_updated_at of this FormulaDocOutputV1.
        The timestamp that this document was last updated at

        :param doc_updated_at: The doc_updated_at of this FormulaDocOutputV1.
        :type: str
        """

        self._doc_updated_at = doc_updated_at

    @property
    def documentation_href(self):
        """
        Gets the documentation_href of this FormulaDocOutputV1.
        The href of this document

        :return: The documentation_href of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._documentation_href

    @documentation_href.setter
    def documentation_href(self, documentation_href):
        """
        Sets the documentation_href of this FormulaDocOutputV1.
        The href of this document

        :param documentation_href: The documentation_href of this FormulaDocOutputV1.
        :type: str
        """

        self._documentation_href = documentation_href

    @property
    def examples(self):
        """
        Gets the examples of this FormulaDocOutputV1.
        Formula examples demonstrating the functions in this document

        :return: The examples of this FormulaDocOutputV1.
        :rtype: list[FormulaExampleOutputV1]
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """
        Sets the examples of this FormulaDocOutputV1.
        Formula examples demonstrating the functions in this document

        :param examples: The examples of this FormulaDocOutputV1.
        :type: list[FormulaExampleOutputV1]
        """

        self._examples = examples

    @property
    def excel_synonyms(self):
        """
        Gets the excel_synonyms of this FormulaDocOutputV1.
        Search synonyms for this document, generally corresponding to an excel function

        :return: The excel_synonyms of this FormulaDocOutputV1.
        :rtype: list[str]
        """
        return self._excel_synonyms

    @excel_synonyms.setter
    def excel_synonyms(self, excel_synonyms):
        """
        Sets the excel_synonyms of this FormulaDocOutputV1.
        Search synonyms for this document, generally corresponding to an excel function

        :param excel_synonyms: The excel_synonyms of this FormulaDocOutputV1.
        :type: list[str]
        """

        self._excel_synonyms = excel_synonyms

    @property
    def function_group_id(self):
        """
        Gets the function_group_id of this FormulaDocOutputV1.
        The identifier of this document

        :return: The function_group_id of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._function_group_id

    @function_group_id.setter
    def function_group_id(self, function_group_id):
        """
        Sets the function_group_id of this FormulaDocOutputV1.
        The identifier of this document

        :param function_group_id: The function_group_id of this FormulaDocOutputV1.
        :type: str
        """

        self._function_group_id = function_group_id

    @property
    def functions(self):
        """
        Gets the functions of this FormulaDocOutputV1.
        Functions in this document

        :return: The functions of this FormulaDocOutputV1.
        :rtype: list[FunctionVariantOutputV1]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this FormulaDocOutputV1.
        Functions in this document

        :param functions: The functions of this FormulaDocOutputV1.
        :type: list[FunctionVariantOutputV1]
        """

        self._functions = functions

    @property
    def keywords(self):
        """
        Gets the keywords of this FormulaDocOutputV1.
        Search keywords for this document

        :return: The keywords of this FormulaDocOutputV1.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this FormulaDocOutputV1.
        Search keywords for this document

        :param keywords: The keywords of this FormulaDocOutputV1.
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def package_created_at(self):
        """
        Gets the package_created_at of this FormulaDocOutputV1.
        The timestamp that the Package was created at

        :return: The package_created_at of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_created_at

    @package_created_at.setter
    def package_created_at(self, package_created_at):
        """
        Sets the package_created_at of this FormulaDocOutputV1.
        The timestamp that the Package was created at

        :param package_created_at: The package_created_at of this FormulaDocOutputV1.
        :type: str
        """

        self._package_created_at = package_created_at

    @property
    def package_creator_contact_info(self):
        """
        Gets the package_creator_contact_info of this FormulaDocOutputV1.
        The contact information of the Package creator

        :return: The package_creator_contact_info of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_creator_contact_info

    @package_creator_contact_info.setter
    def package_creator_contact_info(self, package_creator_contact_info):
        """
        Sets the package_creator_contact_info of this FormulaDocOutputV1.
        The contact information of the Package creator

        :param package_creator_contact_info: The package_creator_contact_info of this FormulaDocOutputV1.
        :type: str
        """

        self._package_creator_contact_info = package_creator_contact_info

    @property
    def package_creator_name(self):
        """
        Gets the package_creator_name of this FormulaDocOutputV1.
        The name of the Package creator

        :return: The package_creator_name of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_creator_name

    @package_creator_name.setter
    def package_creator_name(self, package_creator_name):
        """
        Sets the package_creator_name of this FormulaDocOutputV1.
        The name of the Package creator

        :param package_creator_name: The package_creator_name of this FormulaDocOutputV1.
        :type: str
        """

        self._package_creator_name = package_creator_name

    @property
    def package_id(self):
        """
        Gets the package_id of this FormulaDocOutputV1.
        The package containing this document

        :return: The package_id of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """
        Sets the package_id of this FormulaDocOutputV1.
        The package containing this document

        :param package_id: The package_id of this FormulaDocOutputV1.
        :type: str
        """

        self._package_id = package_id

    @property
    def package_installer_name(self):
        """
        Gets the package_installer_name of this FormulaDocOutputV1.
        The name of the Package installer

        :return: The package_installer_name of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_installer_name

    @package_installer_name.setter
    def package_installer_name(self, package_installer_name):
        """
        Sets the package_installer_name of this FormulaDocOutputV1.
        The name of the Package installer

        :param package_installer_name: The package_installer_name of this FormulaDocOutputV1.
        :type: str
        """

        self._package_installer_name = package_installer_name

    @property
    def package_updated_at(self):
        """
        Gets the package_updated_at of this FormulaDocOutputV1.
        The timestamp that the Package was last updated at

        :return: The package_updated_at of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_updated_at

    @package_updated_at.setter
    def package_updated_at(self, package_updated_at):
        """
        Sets the package_updated_at of this FormulaDocOutputV1.
        The timestamp that the Package was last updated at

        :param package_updated_at: The package_updated_at of this FormulaDocOutputV1.
        :type: str
        """

        self._package_updated_at = package_updated_at

    @property
    def package_version(self):
        """
        Gets the package_version of this FormulaDocOutputV1.
        The version of the Package

        :return: The package_version of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this FormulaDocOutputV1.
        The version of the Package

        :param package_version: The package_version of this FormulaDocOutputV1.
        :type: str
        """

        self._package_version = package_version

    @property
    def parameters(self):
        """
        Gets the parameters of this FormulaDocOutputV1.
        Parameters of the functions in this document

        :return: The parameters of this FormulaDocOutputV1.
        :rtype: list[ParameterDocOutputV1]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this FormulaDocOutputV1.
        Parameters of the functions in this document

        :param parameters: The parameters of this FormulaDocOutputV1.
        :type: list[ParameterDocOutputV1]
        """

        self._parameters = parameters

    @property
    def parents(self):
        """
        Gets the parents of this FormulaDocOutputV1.
        Parent link of this document

        :return: The parents of this FormulaDocOutputV1.
        :rtype: list[SeeAlsoDocOutputV1]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """
        Sets the parents of this FormulaDocOutputV1.
        Parent link of this document

        :param parents: The parents of this FormulaDocOutputV1.
        :type: list[SeeAlsoDocOutputV1]
        """

        self._parents = parents

    @property
    def see_alsos(self):
        """
        Gets the see_alsos of this FormulaDocOutputV1.
        Related links of this document

        :return: The see_alsos of this FormulaDocOutputV1.
        :rtype: list[SeeAlsoDocOutputV1]
        """
        return self._see_alsos

    @see_alsos.setter
    def see_alsos(self, see_alsos):
        """
        Sets the see_alsos of this FormulaDocOutputV1.
        Related links of this document

        :param see_alsos: The see_alsos of this FormulaDocOutputV1.
        :type: list[SeeAlsoDocOutputV1]
        """

        self._see_alsos = see_alsos

    @property
    def title(self):
        """
        Gets the title of this FormulaDocOutputV1.
        The title of this document

        :return: The title of this FormulaDocOutputV1.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this FormulaDocOutputV1.
        The title of this document

        :param title: The title of this FormulaDocOutputV1.
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
        if not isinstance(other, FormulaDocOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

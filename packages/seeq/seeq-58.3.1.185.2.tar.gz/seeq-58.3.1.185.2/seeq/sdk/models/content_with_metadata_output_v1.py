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


class ContentWithMetadataOutputV1(object):
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
        'asset_selection': 'AssetSelectionOutputV1',
        'current_workstep_blob': 'WorkstepOutputV1',
        'date_range': 'DateRangeOutputV1',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'hash_code': 'str',
        'height': 'int',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'react': 'bool',
        'report': 'ItemPreviewV1',
        'scale': 'float',
        'selector': 'str',
        'source_url': 'str',
        'source_workbook': 'str',
        'source_worksheet': 'str',
        'source_workstep': 'str',
        'source_workstep_blob': 'WorkstepOutputV1',
        'status_message': 'str',
        'summary_type': 'str',
        'summary_value': 'str',
        'timezone': 'str',
        'translation_key': 'str',
        'type': 'str',
        'warning': 'str',
        'width': 'int',
        'workbook_preview': 'ItemPreviewV1',
        'worksheet_preview': 'ItemPreviewV1'
    }

    attribute_map = {
        'archived': 'archived',
        'asset_selection': 'assetSelection',
        'current_workstep_blob': 'currentWorkstepBlob',
        'date_range': 'dateRange',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'hash_code': 'hashCode',
        'height': 'height',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'react': 'react',
        'report': 'report',
        'scale': 'scale',
        'selector': 'selector',
        'source_url': 'sourceUrl',
        'source_workbook': 'sourceWorkbook',
        'source_worksheet': 'sourceWorksheet',
        'source_workstep': 'sourceWorkstep',
        'source_workstep_blob': 'sourceWorkstepBlob',
        'status_message': 'statusMessage',
        'summary_type': 'summaryType',
        'summary_value': 'summaryValue',
        'timezone': 'timezone',
        'translation_key': 'translationKey',
        'type': 'type',
        'warning': 'warning',
        'width': 'width',
        'workbook_preview': 'workbookPreview',
        'worksheet_preview': 'worksheetPreview'
    }

    def __init__(self, archived=False, asset_selection=None, current_workstep_blob=None, date_range=None, description=None, effective_permissions=None, hash_code=None, height=None, id=None, is_archived=False, is_redacted=False, name=None, react=False, report=None, scale=None, selector=None, source_url=None, source_workbook=None, source_worksheet=None, source_workstep=None, source_workstep_blob=None, status_message=None, summary_type=None, summary_value=None, timezone=None, translation_key=None, type=None, warning=None, width=None, workbook_preview=None, worksheet_preview=None):
        """
        ContentWithMetadataOutputV1 - a model defined in Swagger
        """

        self._archived = None
        self._asset_selection = None
        self._current_workstep_blob = None
        self._date_range = None
        self._description = None
        self._effective_permissions = None
        self._hash_code = None
        self._height = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._react = None
        self._report = None
        self._scale = None
        self._selector = None
        self._source_url = None
        self._source_workbook = None
        self._source_worksheet = None
        self._source_workstep = None
        self._source_workstep_blob = None
        self._status_message = None
        self._summary_type = None
        self._summary_value = None
        self._timezone = None
        self._translation_key = None
        self._type = None
        self._warning = None
        self._width = None
        self._workbook_preview = None
        self._worksheet_preview = None

        if archived is not None:
          self.archived = archived
        if asset_selection is not None:
          self.asset_selection = asset_selection
        if current_workstep_blob is not None:
          self.current_workstep_blob = current_workstep_blob
        if date_range is not None:
          self.date_range = date_range
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if hash_code is not None:
          self.hash_code = hash_code
        if height is not None:
          self.height = height
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if react is not None:
          self.react = react
        if report is not None:
          self.report = report
        if scale is not None:
          self.scale = scale
        if selector is not None:
          self.selector = selector
        if source_url is not None:
          self.source_url = source_url
        if source_workbook is not None:
          self.source_workbook = source_workbook
        if source_worksheet is not None:
          self.source_worksheet = source_worksheet
        if source_workstep is not None:
          self.source_workstep = source_workstep
        if source_workstep_blob is not None:
          self.source_workstep_blob = source_workstep_blob
        if status_message is not None:
          self.status_message = status_message
        if summary_type is not None:
          self.summary_type = summary_type
        if summary_value is not None:
          self.summary_value = summary_value
        if timezone is not None:
          self.timezone = timezone
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if warning is not None:
          self.warning = warning
        if width is not None:
          self.width = width
        if workbook_preview is not None:
          self.workbook_preview = workbook_preview
        if worksheet_preview is not None:
          self.worksheet_preview = worksheet_preview

    @property
    def archived(self):
        """
        Gets the archived of this ContentWithMetadataOutputV1.
        Whether this content is archived

        :return: The archived of this ContentWithMetadataOutputV1.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this ContentWithMetadataOutputV1.
        Whether this content is archived

        :param archived: The archived of this ContentWithMetadataOutputV1.
        :type: bool
        """

        self._archived = archived

    @property
    def asset_selection(self):
        """
        Gets the asset_selection of this ContentWithMetadataOutputV1.

        :return: The asset_selection of this ContentWithMetadataOutputV1.
        :rtype: AssetSelectionOutputV1
        """
        return self._asset_selection

    @asset_selection.setter
    def asset_selection(self, asset_selection):
        """
        Sets the asset_selection of this ContentWithMetadataOutputV1.

        :param asset_selection: The asset_selection of this ContentWithMetadataOutputV1.
        :type: AssetSelectionOutputV1
        """

        self._asset_selection = asset_selection

    @property
    def current_workstep_blob(self):
        """
        Gets the current_workstep_blob of this ContentWithMetadataOutputV1.

        :return: The current_workstep_blob of this ContentWithMetadataOutputV1.
        :rtype: WorkstepOutputV1
        """
        return self._current_workstep_blob

    @current_workstep_blob.setter
    def current_workstep_blob(self, current_workstep_blob):
        """
        Sets the current_workstep_blob of this ContentWithMetadataOutputV1.

        :param current_workstep_blob: The current_workstep_blob of this ContentWithMetadataOutputV1.
        :type: WorkstepOutputV1
        """

        self._current_workstep_blob = current_workstep_blob

    @property
    def date_range(self):
        """
        Gets the date_range of this ContentWithMetadataOutputV1.

        :return: The date_range of this ContentWithMetadataOutputV1.
        :rtype: DateRangeOutputV1
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """
        Sets the date_range of this ContentWithMetadataOutputV1.

        :param date_range: The date_range of this ContentWithMetadataOutputV1.
        :type: DateRangeOutputV1
        """

        self._date_range = date_range

    @property
    def description(self):
        """
        Gets the description of this ContentWithMetadataOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ContentWithMetadataOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this ContentWithMetadataOutputV1.

        :return: The effective_permissions of this ContentWithMetadataOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this ContentWithMetadataOutputV1.

        :param effective_permissions: The effective_permissions of this ContentWithMetadataOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def hash_code(self):
        """
        Gets the hash_code of this ContentWithMetadataOutputV1.
        A unique identifier that identifies the current variant of the image, if it has been generated, otherwise null

        :return: The hash_code of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._hash_code

    @hash_code.setter
    def hash_code(self, hash_code):
        """
        Sets the hash_code of this ContentWithMetadataOutputV1.
        A unique identifier that identifies the current variant of the image, if it has been generated, otherwise null

        :param hash_code: The hash_code of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._hash_code = hash_code

    @property
    def height(self):
        """
        Gets the height of this ContentWithMetadataOutputV1.
        Desired content height

        :return: The height of this ContentWithMetadataOutputV1.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ContentWithMetadataOutputV1.
        Desired content height

        :param height: The height of this ContentWithMetadataOutputV1.
        :type: int
        """

        self._height = height

    @property
    def id(self):
        """
        Gets the id of this ContentWithMetadataOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContentWithMetadataOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ContentWithMetadataOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ContentWithMetadataOutputV1.
        Whether item is archived

        :return: The is_archived of this ContentWithMetadataOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ContentWithMetadataOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this ContentWithMetadataOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this ContentWithMetadataOutputV1.
        Whether item is redacted

        :return: The is_redacted of this ContentWithMetadataOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this ContentWithMetadataOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this ContentWithMetadataOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this ContentWithMetadataOutputV1.
        The human readable name

        :return: The name of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContentWithMetadataOutputV1.
        The human readable name

        :param name: The name of this ContentWithMetadataOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def react(self):
        """
        Gets the react of this ContentWithMetadataOutputV1.
        Whether or not the content is for a react component

        :return: The react of this ContentWithMetadataOutputV1.
        :rtype: bool
        """
        return self._react

    @react.setter
    def react(self, react):
        """
        Sets the react of this ContentWithMetadataOutputV1.
        Whether or not the content is for a react component

        :param react: The react of this ContentWithMetadataOutputV1.
        :type: bool
        """

        self._react = react

    @property
    def report(self):
        """
        Gets the report of this ContentWithMetadataOutputV1.

        :return: The report of this ContentWithMetadataOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._report

    @report.setter
    def report(self, report):
        """
        Sets the report of this ContentWithMetadataOutputV1.

        :param report: The report of this ContentWithMetadataOutputV1.
        :type: ItemPreviewV1
        """

        self._report = report

    @property
    def scale(self):
        """
        Gets the scale of this ContentWithMetadataOutputV1.
        Desired content scale

        :return: The scale of this ContentWithMetadataOutputV1.
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this ContentWithMetadataOutputV1.
        Desired content scale

        :param scale: The scale of this ContentWithMetadataOutputV1.
        :type: float
        """

        self._scale = scale

    @property
    def selector(self):
        """
        Gets the selector of this ContentWithMetadataOutputV1.
        Desired content selector, if present

        :return: The selector of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this ContentWithMetadataOutputV1.
        Desired content selector, if present

        :param selector: The selector of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._selector = selector

    @property
    def source_url(self):
        """
        Gets the source_url of this ContentWithMetadataOutputV1.
        A URL that will redirect to the source worksheet used to generate the content

        :return: The source_url of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """
        Sets the source_url of this ContentWithMetadataOutputV1.
        A URL that will redirect to the source worksheet used to generate the content

        :param source_url: The source_url of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._source_url = source_url

    @property
    def source_workbook(self):
        """
        Gets the source_workbook of this ContentWithMetadataOutputV1.
        Source workbook of the content

        :return: The source_workbook of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._source_workbook

    @source_workbook.setter
    def source_workbook(self, source_workbook):
        """
        Sets the source_workbook of this ContentWithMetadataOutputV1.
        Source workbook of the content

        :param source_workbook: The source_workbook of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._source_workbook = source_workbook

    @property
    def source_worksheet(self):
        """
        Gets the source_worksheet of this ContentWithMetadataOutputV1.
        Source worksheet of the content

        :return: The source_worksheet of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._source_worksheet

    @source_worksheet.setter
    def source_worksheet(self, source_worksheet):
        """
        Sets the source_worksheet of this ContentWithMetadataOutputV1.
        Source worksheet of the content

        :param source_worksheet: The source_worksheet of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._source_worksheet = source_worksheet

    @property
    def source_workstep(self):
        """
        Gets the source_workstep of this ContentWithMetadataOutputV1.
        Source workstep of the content

        :return: The source_workstep of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._source_workstep

    @source_workstep.setter
    def source_workstep(self, source_workstep):
        """
        Sets the source_workstep of this ContentWithMetadataOutputV1.
        Source workstep of the content

        :param source_workstep: The source_workstep of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._source_workstep = source_workstep

    @property
    def source_workstep_blob(self):
        """
        Gets the source_workstep_blob of this ContentWithMetadataOutputV1.

        :return: The source_workstep_blob of this ContentWithMetadataOutputV1.
        :rtype: WorkstepOutputV1
        """
        return self._source_workstep_blob

    @source_workstep_blob.setter
    def source_workstep_blob(self, source_workstep_blob):
        """
        Sets the source_workstep_blob of this ContentWithMetadataOutputV1.

        :param source_workstep_blob: The source_workstep_blob of this ContentWithMetadataOutputV1.
        :type: WorkstepOutputV1
        """

        self._source_workstep_blob = source_workstep_blob

    @property
    def status_message(self):
        """
        Gets the status_message of this ContentWithMetadataOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ContentWithMetadataOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def summary_type(self):
        """
        Gets the summary_type of this ContentWithMetadataOutputV1.
        The summary type for this screenshot if a summary is being applied. One of DISCRETE, AUTO

        :return: The summary_type of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._summary_type

    @summary_type.setter
    def summary_type(self, summary_type):
        """
        Sets the summary_type of this ContentWithMetadataOutputV1.
        The summary type for this screenshot if a summary is being applied. One of DISCRETE, AUTO

        :param summary_type: The summary_type of this ContentWithMetadataOutputV1.
        :type: str
        """
        allowed_values = ["DISCRETE", "AUTO", "NONE"]
        if summary_type not in allowed_values:
            raise ValueError(
                "Invalid value for `summary_type` ({0}), must be one of {1}"
                .format(summary_type, allowed_values)
            )

        self._summary_type = summary_type

    @property
    def summary_value(self):
        """
        Gets the summary_value of this ContentWithMetadataOutputV1.
        The value for the given summary type. If discrete, a time + unit pairing (1min, 2days). If auto, a fixed value (1-10).

        :return: The summary_value of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._summary_value

    @summary_value.setter
    def summary_value(self, summary_value):
        """
        Sets the summary_value of this ContentWithMetadataOutputV1.
        The value for the given summary type. If discrete, a time + unit pairing (1min, 2days). If auto, a fixed value (1-10).

        :param summary_value: The summary_value of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._summary_value = summary_value

    @property
    def timezone(self):
        """
        Gets the timezone of this ContentWithMetadataOutputV1.
        Desired content timezone, if present

        :return: The timezone of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ContentWithMetadataOutputV1.
        Desired content timezone, if present

        :param timezone: The timezone of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._timezone = timezone

    @property
    def translation_key(self):
        """
        Gets the translation_key of this ContentWithMetadataOutputV1.
        The item's translation key, if any

        :return: The translation_key of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this ContentWithMetadataOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this ContentWithMetadataOutputV1.
        The type of the item

        :return: The type of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ContentWithMetadataOutputV1.
        The type of the item

        :param type: The type of this ContentWithMetadataOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def warning(self):
        """
        Gets the warning of this ContentWithMetadataOutputV1.
        A warning if one was attached to this content while rendering

        :return: The warning of this ContentWithMetadataOutputV1.
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """
        Sets the warning of this ContentWithMetadataOutputV1.
        A warning if one was attached to this content while rendering

        :param warning: The warning of this ContentWithMetadataOutputV1.
        :type: str
        """

        self._warning = warning

    @property
    def width(self):
        """
        Gets the width of this ContentWithMetadataOutputV1.
        Desired content width

        :return: The width of this ContentWithMetadataOutputV1.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ContentWithMetadataOutputV1.
        Desired content width

        :param width: The width of this ContentWithMetadataOutputV1.
        :type: int
        """

        self._width = width

    @property
    def workbook_preview(self):
        """
        Gets the workbook_preview of this ContentWithMetadataOutputV1.

        :return: The workbook_preview of this ContentWithMetadataOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._workbook_preview

    @workbook_preview.setter
    def workbook_preview(self, workbook_preview):
        """
        Sets the workbook_preview of this ContentWithMetadataOutputV1.

        :param workbook_preview: The workbook_preview of this ContentWithMetadataOutputV1.
        :type: ItemPreviewV1
        """

        self._workbook_preview = workbook_preview

    @property
    def worksheet_preview(self):
        """
        Gets the worksheet_preview of this ContentWithMetadataOutputV1.

        :return: The worksheet_preview of this ContentWithMetadataOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._worksheet_preview

    @worksheet_preview.setter
    def worksheet_preview(self, worksheet_preview):
        """
        Sets the worksheet_preview of this ContentWithMetadataOutputV1.

        :param worksheet_preview: The worksheet_preview of this ContentWithMetadataOutputV1.
        :type: ItemPreviewV1
        """

        self._worksheet_preview = worksheet_preview

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
        if not isinstance(other, ContentWithMetadataOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

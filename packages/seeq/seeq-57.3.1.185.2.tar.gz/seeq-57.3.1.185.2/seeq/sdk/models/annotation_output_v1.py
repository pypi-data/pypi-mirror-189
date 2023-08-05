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


class AnnotationOutputV1(object):
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
        'asset_selection_ids': 'list[str]',
        'background': 'bool',
        'backups': 'list[DocumentBackupOutputV1]',
        'ck_enabled': 'bool',
        'content_ids': 'list[str]',
        'created_at': 'str',
        'created_by': 'ItemPreviewV1',
        'cron_schedule': 'list[str]',
        'date_range_ids': 'list[str]',
        'description': 'str',
        'discoverable': 'bool',
        'document': 'str',
        'effective_permissions': 'PermissionsV1',
        'enabled': 'bool',
        'fixed_width': 'bool',
        'id': 'str',
        'interests': 'list[AnnotationInterestOutputV1]',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'next_run_time': 'str',
        'published_at': 'str',
        'replies': 'list[AnnotationOutputV1]',
        'replies_to': 'str',
        'reports_on': 'str',
        'status_message': 'str',
        'translation_key': 'str',
        'type': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'asset_selection_ids': 'assetSelectionIds',
        'background': 'background',
        'backups': 'backups',
        'ck_enabled': 'ckEnabled',
        'content_ids': 'contentIds',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'cron_schedule': 'cronSchedule',
        'date_range_ids': 'dateRangeIds',
        'description': 'description',
        'discoverable': 'discoverable',
        'document': 'document',
        'effective_permissions': 'effectivePermissions',
        'enabled': 'enabled',
        'fixed_width': 'fixedWidth',
        'id': 'id',
        'interests': 'interests',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'next_run_time': 'nextRunTime',
        'published_at': 'publishedAt',
        'replies': 'replies',
        'replies_to': 'repliesTo',
        'reports_on': 'reportsOn',
        'status_message': 'statusMessage',
        'translation_key': 'translationKey',
        'type': 'type',
        'updated_at': 'updatedAt'
    }

    def __init__(self, asset_selection_ids=None, background=False, backups=None, ck_enabled=False, content_ids=None, created_at=None, created_by=None, cron_schedule=None, date_range_ids=None, description=None, discoverable=False, document=None, effective_permissions=None, enabled=False, fixed_width=False, id=None, interests=None, is_archived=False, is_redacted=False, name=None, next_run_time=None, published_at=None, replies=None, replies_to=None, reports_on=None, status_message=None, translation_key=None, type=None, updated_at=None):
        """
        AnnotationOutputV1 - a model defined in Swagger
        """

        self._asset_selection_ids = None
        self._background = None
        self._backups = None
        self._ck_enabled = None
        self._content_ids = None
        self._created_at = None
        self._created_by = None
        self._cron_schedule = None
        self._date_range_ids = None
        self._description = None
        self._discoverable = None
        self._document = None
        self._effective_permissions = None
        self._enabled = None
        self._fixed_width = None
        self._id = None
        self._interests = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._next_run_time = None
        self._published_at = None
        self._replies = None
        self._replies_to = None
        self._reports_on = None
        self._status_message = None
        self._translation_key = None
        self._type = None
        self._updated_at = None

        if asset_selection_ids is not None:
          self.asset_selection_ids = asset_selection_ids
        if background is not None:
          self.background = background
        if backups is not None:
          self.backups = backups
        if ck_enabled is not None:
          self.ck_enabled = ck_enabled
        if content_ids is not None:
          self.content_ids = content_ids
        if created_at is not None:
          self.created_at = created_at
        if created_by is not None:
          self.created_by = created_by
        if cron_schedule is not None:
          self.cron_schedule = cron_schedule
        if date_range_ids is not None:
          self.date_range_ids = date_range_ids
        if description is not None:
          self.description = description
        if discoverable is not None:
          self.discoverable = discoverable
        if document is not None:
          self.document = document
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if enabled is not None:
          self.enabled = enabled
        if fixed_width is not None:
          self.fixed_width = fixed_width
        if id is not None:
          self.id = id
        if interests is not None:
          self.interests = interests
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if next_run_time is not None:
          self.next_run_time = next_run_time
        if published_at is not None:
          self.published_at = published_at
        if replies is not None:
          self.replies = replies
        if replies_to is not None:
          self.replies_to = replies_to
        if reports_on is not None:
          self.reports_on = reports_on
        if status_message is not None:
          self.status_message = status_message
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if updated_at is not None:
          self.updated_at = updated_at

    @property
    def asset_selection_ids(self):
        """
        Gets the asset_selection_ids of this AnnotationOutputV1.
        The IDs of Asset Selections included in this Report. Ignored for Journals

        :return: The asset_selection_ids of this AnnotationOutputV1.
        :rtype: list[str]
        """
        return self._asset_selection_ids

    @asset_selection_ids.setter
    def asset_selection_ids(self, asset_selection_ids):
        """
        Sets the asset_selection_ids of this AnnotationOutputV1.
        The IDs of Asset Selections included in this Report. Ignored for Journals

        :param asset_selection_ids: The asset_selection_ids of this AnnotationOutputV1.
        :type: list[str]
        """

        self._asset_selection_ids = asset_selection_ids

    @property
    def background(self):
        """
        Gets the background of this AnnotationOutputV1.
        Whether the Report, if scheduled, should continue to update if there are no subscribers (i.e. in the background). Ignored for Journals

        :return: The background of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background of this AnnotationOutputV1.
        Whether the Report, if scheduled, should continue to update if there are no subscribers (i.e. in the background). Ignored for Journals

        :param background: The background of this AnnotationOutputV1.
        :type: bool
        """

        self._background = background

    @property
    def backups(self):
        """
        Gets the backups of this AnnotationOutputV1.
        The list of backups for this Annotation's Document property

        :return: The backups of this AnnotationOutputV1.
        :rtype: list[DocumentBackupOutputV1]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """
        Sets the backups of this AnnotationOutputV1.
        The list of backups for this Annotation's Document property

        :param backups: The backups of this AnnotationOutputV1.
        :type: list[DocumentBackupOutputV1]
        """

        self._backups = backups

    @property
    def ck_enabled(self):
        """
        Gets the ck_enabled of this AnnotationOutputV1.
        Whether the Report/Journal is using CKEditor

        :return: The ck_enabled of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._ck_enabled

    @ck_enabled.setter
    def ck_enabled(self, ck_enabled):
        """
        Sets the ck_enabled of this AnnotationOutputV1.
        Whether the Report/Journal is using CKEditor

        :param ck_enabled: The ck_enabled of this AnnotationOutputV1.
        :type: bool
        """

        self._ck_enabled = ck_enabled

    @property
    def content_ids(self):
        """
        Gets the content_ids of this AnnotationOutputV1.
        The IDs of Content included in this Report. Ignored for Journals

        :return: The content_ids of this AnnotationOutputV1.
        :rtype: list[str]
        """
        return self._content_ids

    @content_ids.setter
    def content_ids(self, content_ids):
        """
        Sets the content_ids of this AnnotationOutputV1.
        The IDs of Content included in this Report. Ignored for Journals

        :param content_ids: The content_ids of this AnnotationOutputV1.
        :type: list[str]
        """

        self._content_ids = content_ids

    @property
    def created_at(self):
        """
        Gets the created_at of this AnnotationOutputV1.
        The ISO 8601 date of when the annotation was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The created_at of this AnnotationOutputV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this AnnotationOutputV1.
        The ISO 8601 date of when the annotation was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param created_at: The created_at of this AnnotationOutputV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """
        Gets the created_by of this AnnotationOutputV1.

        :return: The created_by of this AnnotationOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this AnnotationOutputV1.

        :param created_by: The created_by of this AnnotationOutputV1.
        :type: ItemPreviewV1
        """

        self._created_by = created_by

    @property
    def cron_schedule(self):
        """
        Gets the cron_schedule of this AnnotationOutputV1.
        Report update period. Ignored for Journals

        :return: The cron_schedule of this AnnotationOutputV1.
        :rtype: list[str]
        """
        return self._cron_schedule

    @cron_schedule.setter
    def cron_schedule(self, cron_schedule):
        """
        Sets the cron_schedule of this AnnotationOutputV1.
        Report update period. Ignored for Journals

        :param cron_schedule: The cron_schedule of this AnnotationOutputV1.
        :type: list[str]
        """

        self._cron_schedule = cron_schedule

    @property
    def date_range_ids(self):
        """
        Gets the date_range_ids of this AnnotationOutputV1.
        The IDs of Date Ranges included in this Report. Ignored for Journals

        :return: The date_range_ids of this AnnotationOutputV1.
        :rtype: list[str]
        """
        return self._date_range_ids

    @date_range_ids.setter
    def date_range_ids(self, date_range_ids):
        """
        Sets the date_range_ids of this AnnotationOutputV1.
        The IDs of Date Ranges included in this Report. Ignored for Journals

        :param date_range_ids: The date_range_ids of this AnnotationOutputV1.
        :type: list[str]
        """

        self._date_range_ids = date_range_ids

    @property
    def description(self):
        """
        Gets the description of this AnnotationOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this AnnotationOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AnnotationOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this AnnotationOutputV1.
        :type: str
        """

        self._description = description

    @property
    def discoverable(self):
        """
        Gets the discoverable of this AnnotationOutputV1.
        Flag indicating whether this annotation is discoverable

        :return: The discoverable of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._discoverable

    @discoverable.setter
    def discoverable(self, discoverable):
        """
        Sets the discoverable of this AnnotationOutputV1.
        Flag indicating whether this annotation is discoverable

        :param discoverable: The discoverable of this AnnotationOutputV1.
        :type: bool
        """

        self._discoverable = discoverable

    @property
    def document(self):
        """
        Gets the document of this AnnotationOutputV1.
        This annotation's document.

        :return: The document of this AnnotationOutputV1.
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """
        Sets the document of this AnnotationOutputV1.
        This annotation's document.

        :param document: The document of this AnnotationOutputV1.
        :type: str
        """

        self._document = document

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this AnnotationOutputV1.

        :return: The effective_permissions of this AnnotationOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this AnnotationOutputV1.

        :param effective_permissions: The effective_permissions of this AnnotationOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def enabled(self):
        """
        Gets the enabled of this AnnotationOutputV1.
        Whether the Report is enabled to run jobs. Ignored for Journals

        :return: The enabled of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AnnotationOutputV1.
        Whether the Report is enabled to run jobs. Ignored for Journals

        :param enabled: The enabled of this AnnotationOutputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def fixed_width(self):
        """
        Gets the fixed_width of this AnnotationOutputV1.
        Whether the Report has a fixed width. Ignored for Journals

        :return: The fixed_width of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._fixed_width

    @fixed_width.setter
    def fixed_width(self, fixed_width):
        """
        Sets the fixed_width of this AnnotationOutputV1.
        Whether the Report has a fixed width. Ignored for Journals

        :param fixed_width: The fixed_width of this AnnotationOutputV1.
        :type: bool
        """

        self._fixed_width = fixed_width

    @property
    def id(self):
        """
        Gets the id of this AnnotationOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this AnnotationOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AnnotationOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this AnnotationOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def interests(self):
        """
        Gets the interests of this AnnotationOutputV1.
        The list of the annotation's items of interest

        :return: The interests of this AnnotationOutputV1.
        :rtype: list[AnnotationInterestOutputV1]
        """
        return self._interests

    @interests.setter
    def interests(self, interests):
        """
        Sets the interests of this AnnotationOutputV1.
        The list of the annotation's items of interest

        :param interests: The interests of this AnnotationOutputV1.
        :type: list[AnnotationInterestOutputV1]
        """

        self._interests = interests

    @property
    def is_archived(self):
        """
        Gets the is_archived of this AnnotationOutputV1.
        Whether item is archived

        :return: The is_archived of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this AnnotationOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this AnnotationOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this AnnotationOutputV1.
        Whether item is redacted

        :return: The is_redacted of this AnnotationOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this AnnotationOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this AnnotationOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this AnnotationOutputV1.
        The human readable name

        :return: The name of this AnnotationOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AnnotationOutputV1.
        The human readable name

        :param name: The name of this AnnotationOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def next_run_time(self):
        """
        Gets the next_run_time of this AnnotationOutputV1.
        The next scheduled runtime for this Report, based on its Date Ranges. Ignored for Journals

        :return: The next_run_time of this AnnotationOutputV1.
        :rtype: str
        """
        return self._next_run_time

    @next_run_time.setter
    def next_run_time(self, next_run_time):
        """
        Sets the next_run_time of this AnnotationOutputV1.
        The next scheduled runtime for this Report, based on its Date Ranges. Ignored for Journals

        :param next_run_time: The next_run_time of this AnnotationOutputV1.
        :type: str
        """

        self._next_run_time = next_run_time

    @property
    def published_at(self):
        """
        Gets the published_at of this AnnotationOutputV1.
        The ISO 8601 date of when the report was published (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The published_at of this AnnotationOutputV1.
        :rtype: str
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """
        Sets the published_at of this AnnotationOutputV1.
        The ISO 8601 date of when the report was published (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param published_at: The published_at of this AnnotationOutputV1.
        :type: str
        """

        self._published_at = published_at

    @property
    def replies(self):
        """
        Gets the replies of this AnnotationOutputV1.
        The list of Annotations that are replies to this one

        :return: The replies of this AnnotationOutputV1.
        :rtype: list[AnnotationOutputV1]
        """
        return self._replies

    @replies.setter
    def replies(self, replies):
        """
        Sets the replies of this AnnotationOutputV1.
        The list of Annotations that are replies to this one

        :param replies: The replies of this AnnotationOutputV1.
        :type: list[AnnotationOutputV1]
        """

        self._replies = replies

    @property
    def replies_to(self):
        """
        Gets the replies_to of this AnnotationOutputV1.
        ID of the Annotation to which this is a reply

        :return: The replies_to of this AnnotationOutputV1.
        :rtype: str
        """
        return self._replies_to

    @replies_to.setter
    def replies_to(self, replies_to):
        """
        Sets the replies_to of this AnnotationOutputV1.
        ID of the Annotation to which this is a reply

        :param replies_to: The replies_to of this AnnotationOutputV1.
        :type: str
        """

        self._replies_to = replies_to

    @property
    def reports_on(self):
        """
        Gets the reports_on of this AnnotationOutputV1.
        The ID of the Worksheet that the Report is associated to

        :return: The reports_on of this AnnotationOutputV1.
        :rtype: str
        """
        return self._reports_on

    @reports_on.setter
    def reports_on(self, reports_on):
        """
        Sets the reports_on of this AnnotationOutputV1.
        The ID of the Worksheet that the Report is associated to

        :param reports_on: The reports_on of this AnnotationOutputV1.
        :type: str
        """

        self._reports_on = reports_on

    @property
    def status_message(self):
        """
        Gets the status_message of this AnnotationOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this AnnotationOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this AnnotationOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this AnnotationOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def translation_key(self):
        """
        Gets the translation_key of this AnnotationOutputV1.
        The item's translation key, if any

        :return: The translation_key of this AnnotationOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this AnnotationOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this AnnotationOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this AnnotationOutputV1.
        The type of the item

        :return: The type of this AnnotationOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AnnotationOutputV1.
        The type of the item

        :param type: The type of this AnnotationOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def updated_at(self):
        """
        Gets the updated_at of this AnnotationOutputV1.
        The ISO 8601 date of when the annotation was updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The updated_at of this AnnotationOutputV1.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this AnnotationOutputV1.
        The ISO 8601 date of when the annotation was updated (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param updated_at: The updated_at of this AnnotationOutputV1.
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AnnotationOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

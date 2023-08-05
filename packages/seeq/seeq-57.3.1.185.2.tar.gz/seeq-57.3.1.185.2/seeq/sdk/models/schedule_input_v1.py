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


class ScheduleInputV1(object):
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
        'cron_schedule': 'str',
        'key': 'str'
    }

    attribute_map = {
        'cron_schedule': 'cronSchedule',
        'key': 'key'
    }

    def __init__(self, cron_schedule=None, key=None):
        """
        ScheduleInputV1 - a model defined in Swagger
        """

        self._cron_schedule = None
        self._key = None

        if cron_schedule is not None:
          self.cron_schedule = cron_schedule
        if key is not None:
          self.key = key

    @property
    def cron_schedule(self):
        """
        Gets the cron_schedule of this ScheduleInputV1.
        The Notebook's run schedule as a cron expression (see http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)

        :return: The cron_schedule of this ScheduleInputV1.
        :rtype: str
        """
        return self._cron_schedule

    @cron_schedule.setter
    def cron_schedule(self, cron_schedule):
        """
        Sets the cron_schedule of this ScheduleInputV1.
        The Notebook's run schedule as a cron expression (see http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)

        :param cron_schedule: The cron_schedule of this ScheduleInputV1.
        :type: str
        """

        self._cron_schedule = cron_schedule

    @property
    def key(self):
        """
        Gets the key of this ScheduleInputV1.
        An optional key for the schedule that should be unique among all schedules for the Notebook-label combination.

        :return: The key of this ScheduleInputV1.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ScheduleInputV1.
        An optional key for the schedule that should be unique among all schedules for the Notebook-label combination.

        :param key: The key of this ScheduleInputV1.
        :type: str
        """

        self._key = key

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
        if not isinstance(other, ScheduleInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

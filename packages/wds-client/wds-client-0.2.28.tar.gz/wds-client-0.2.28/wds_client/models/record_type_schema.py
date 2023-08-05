# coding: utf-8

"""
    Workspace Data Service

    This page lists both current and proposed APIs. The proposed APIs which have not yet been implemented are marked as deprecated. This is incongruous, but by using the deprecated flag, we can force swagger-ui to display those endpoints differently.  Error codes and responses for proposed APIs are likely to change as we gain more clarity on their implementation.  As of v0.2, all APIs are subject to change without notice.   # noqa: E501

    The version of the OpenAPI document: v0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wds_client.configuration import Configuration


class RecordTypeSchema(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'attributes': 'list[AttributeSchema]',
        'count': 'int',
        'primary_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'attributes': 'attributes',
        'count': 'count',
        'primary_key': 'primaryKey'
    }

    def __init__(self, name=None, attributes=None, count=None, primary_key=None, local_vars_configuration=None):  # noqa: E501
        """RecordTypeSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._attributes = None
        self._count = None
        self._primary_key = None
        self.discriminator = None

        self.name = name
        self.attributes = attributes
        self.count = count
        self.primary_key = primary_key

    @property
    def name(self):
        """Gets the name of this RecordTypeSchema.  # noqa: E501

        Record type name, valid characters for record type names are limited to letters, numbers, spaces, dashes, and underscores.  # noqa: E501

        :return: The name of this RecordTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecordTypeSchema.

        Record type name, valid characters for record type names are limited to letters, numbers, spaces, dashes, and underscores.  # noqa: E501

        :param name: The name of this RecordTypeSchema.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def attributes(self):
        """Gets the attributes of this RecordTypeSchema.  # noqa: E501


        :return: The attributes of this RecordTypeSchema.  # noqa: E501
        :rtype: list[AttributeSchema]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this RecordTypeSchema.


        :param attributes: The attributes of this RecordTypeSchema.  # noqa: E501
        :type: list[AttributeSchema]
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def count(self):
        """Gets the count of this RecordTypeSchema.  # noqa: E501

        Number of records of this type  # noqa: E501

        :return: The count of this RecordTypeSchema.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RecordTypeSchema.

        Number of records of this type  # noqa: E501

        :param count: The count of this RecordTypeSchema.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def primary_key(self):
        """Gets the primary_key of this RecordTypeSchema.  # noqa: E501

        Attribute name that contains the value to uniquely identify each record, defined as a primary key column in the underlying table.  # noqa: E501

        :return: The primary_key of this RecordTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this RecordTypeSchema.

        Attribute name that contains the value to uniquely identify each record, defined as a primary key column in the underlying table.  # noqa: E501

        :param primary_key: The primary_key of this RecordTypeSchema.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and primary_key is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_key`, must not be `None`")  # noqa: E501

        self._primary_key = primary_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecordTypeSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordTypeSchema):
            return True

        return self.to_dict() != other.to_dict()

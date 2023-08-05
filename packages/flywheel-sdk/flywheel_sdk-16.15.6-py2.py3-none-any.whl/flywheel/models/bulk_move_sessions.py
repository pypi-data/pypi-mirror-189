# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class BulkMoveSessions(object):

    swagger_types = {
        'destination_container_type': 'str',
        'sources': 'list[str]',
        'destinations': 'list[str]',
        'conflict_mode': 'str'
    }

    attribute_map = {
        'destination_container_type': 'destination_container_type',
        'sources': 'sources',
        'destinations': 'destinations',
        'conflict_mode': 'conflict_mode'
    }

    rattribute_map = {
        'destination_container_type': 'destination_container_type',
        'sources': 'sources',
        'destinations': 'destinations',
        'conflict_mode': 'conflict_mode'
    }

    def __init__(self, destination_container_type=None, sources=None, destinations=None, conflict_mode=None):  # noqa: E501
        """BulkMoveSessions - a model defined in Swagger"""
        super(BulkMoveSessions, self).__init__()

        self._destination_container_type = None
        self._sources = None
        self._destinations = None
        self._conflict_mode = None
        self.discriminator = None
        self.alt_discriminator = None

        self.destination_container_type = destination_container_type
        self.sources = sources
        self.destinations = destinations
        self.conflict_mode = conflict_mode

    @property
    def destination_container_type(self):
        """Gets the destination_container_type of this BulkMoveSessions.

        The type of destination container

        :return: The destination_container_type of this BulkMoveSessions.
        :rtype: str
        """
        return self._destination_container_type

    @destination_container_type.setter
    def destination_container_type(self, destination_container_type):
        """Sets the destination_container_type of this BulkMoveSessions.

        The type of destination container

        :param destination_container_type: The destination_container_type of this BulkMoveSessions.  # noqa: E501
        :type: str
        """

        self._destination_container_type = destination_container_type

    @property
    def sources(self):
        """Gets the sources of this BulkMoveSessions.

        Array of continer Ids that you would like to bulk move

        :return: The sources of this BulkMoveSessions.
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this BulkMoveSessions.

        Array of continer Ids that you would like to bulk move

        :param sources: The sources of this BulkMoveSessions.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def destinations(self):
        """Gets the destinations of this BulkMoveSessions.

        Array with a single continer Id of the destination container's Id

        :return: The destinations of this BulkMoveSessions.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this BulkMoveSessions.

        Array with a single continer Id of the destination container's Id

        :param destinations: The destinations of this BulkMoveSessions.  # noqa: E501
        :type: list[str]
        """

        self._destinations = destinations

    @property
    def conflict_mode(self):
        """Gets the conflict_mode of this BulkMoveSessions.

        How to handle conflicts. Required even if no conflicts are found

        :return: The conflict_mode of this BulkMoveSessions.
        :rtype: str
        """
        return self._conflict_mode

    @conflict_mode.setter
    def conflict_mode(self, conflict_mode):
        """Sets the conflict_mode of this BulkMoveSessions.

        How to handle conflicts. Required even if no conflicts are found

        :param conflict_mode: The conflict_mode of this BulkMoveSessions.  # noqa: E501
        :type: str
        """

        self._conflict_mode = conflict_mode


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, BulkMoveSessions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result

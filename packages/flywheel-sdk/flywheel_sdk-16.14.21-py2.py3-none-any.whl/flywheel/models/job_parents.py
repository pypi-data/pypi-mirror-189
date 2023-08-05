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


class JobParents(object):

    swagger_types = {
        'group': 'str',
        'project': 'str',
        'subject': 'str',
        'session': 'str',
        'acquisition': 'str',
        'analysis': 'str'
    }

    attribute_map = {
        'group': 'group',
        'project': 'project',
        'subject': 'subject',
        'session': 'session',
        'acquisition': 'acquisition',
        'analysis': 'analysis'
    }

    rattribute_map = {
        'group': 'group',
        'project': 'project',
        'subject': 'subject',
        'session': 'session',
        'acquisition': 'acquisition',
        'analysis': 'analysis'
    }

    def __init__(self, group=None, project=None, subject=None, session=None, acquisition=None, analysis=None):  # noqa: E501
        """JobParents - a model defined in Swagger"""
        super(JobParents, self).__init__()

        self._group = None
        self._project = None
        self._subject = None
        self._session = None
        self._acquisition = None
        self._analysis = None
        self.discriminator = None
        self.alt_discriminator = None

        self.group = group
        self.project = project
        if subject is not None:
            self.subject = subject
        if session is not None:
            self.session = session
        if acquisition is not None:
            self.acquisition = acquisition
        if analysis is not None:
            self.analysis = analysis

    @property
    def group(self):
        """Gets the group of this JobParents.


        :return: The group of this JobParents.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this JobParents.


        :param group: The group of this JobParents.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def project(self):
        """Gets the project of this JobParents.


        :return: The project of this JobParents.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this JobParents.


        :param project: The project of this JobParents.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def subject(self):
        """Gets the subject of this JobParents.


        :return: The subject of this JobParents.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this JobParents.


        :param subject: The subject of this JobParents.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def session(self):
        """Gets the session of this JobParents.


        :return: The session of this JobParents.
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this JobParents.


        :param session: The session of this JobParents.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def acquisition(self):
        """Gets the acquisition of this JobParents.


        :return: The acquisition of this JobParents.
        :rtype: str
        """
        return self._acquisition

    @acquisition.setter
    def acquisition(self, acquisition):
        """Sets the acquisition of this JobParents.


        :param acquisition: The acquisition of this JobParents.  # noqa: E501
        :type: str
        """

        self._acquisition = acquisition

    @property
    def analysis(self):
        """Gets the analysis of this JobParents.


        :return: The analysis of this JobParents.
        :rtype: str
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this JobParents.


        :param analysis: The analysis of this JobParents.  # noqa: E501
        :type: str
        """

        self._analysis = analysis


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
        if not isinstance(other, JobParents):
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

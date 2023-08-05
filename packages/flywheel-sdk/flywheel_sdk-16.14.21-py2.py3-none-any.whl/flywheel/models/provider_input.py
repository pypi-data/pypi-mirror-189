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


class ProviderInput(object):

    swagger_types = {
        'provider_class': 'str',
        'provider_type': 'str',
        'access_type': 'str',
        'label': 'str',
        'config': 'object',
        'creds': 'object'
    }

    attribute_map = {
        'provider_class': 'provider_class',
        'provider_type': 'provider_type',
        'access_type': 'access_type',
        'label': 'label',
        'config': 'config',
        'creds': 'creds'
    }

    rattribute_map = {
        'provider_class': 'provider_class',
        'provider_type': 'provider_type',
        'access_type': 'access_type',
        'label': 'label',
        'config': 'config',
        'creds': 'creds'
    }

    def __init__(self, provider_class=None, provider_type=None, access_type=None, label=None, config=None, creds=None):  # noqa: E501
        """ProviderInput - a model defined in Swagger"""
        super(ProviderInput, self).__init__()

        self._provider_class = None
        self._provider_type = None
        self._access_type = None
        self._label = None
        self._config = None
        self._creds = None
        self.discriminator = None
        self.alt_discriminator = None

        if provider_class is not None:
            self.provider_class = provider_class
        if provider_type is not None:
            self.provider_type = provider_type
        if access_type is not None:
            self.access_type = access_type
        if label is not None:
            self.label = label
        if config is not None:
            self.config = config
        if creds is not None:
            self.creds = creds

    @property
    def provider_class(self):
        """Gets the provider_class of this ProviderInput.

        The provider class - one of compute or storage

        :return: The provider_class of this ProviderInput.
        :rtype: str
        """
        return self._provider_class

    @provider_class.setter
    def provider_class(self, provider_class):
        """Sets the provider_class of this ProviderInput.

        The provider class - one of compute or storage

        :param provider_class: The provider_class of this ProviderInput.  # noqa: E501
        :type: str
        """

        self._provider_class = provider_class

    @property
    def provider_type(self):
        """Gets the provider_type of this ProviderInput.

        The provider type (e.g. static or gcloud)

        :return: The provider_type of this ProviderInput.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ProviderInput.

        The provider type (e.g. static or gcloud)

        :param provider_type: The provider_type of this ProviderInput.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def access_type(self):
        """Gets the access_type of this ProviderInput.

        The access type - required for storage class providers

        :return: The access_type of this ProviderInput.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this ProviderInput.

        The access type - required for storage class providers

        :param access_type: The access_type of this ProviderInput.  # noqa: E501
        :type: str
        """

        self._access_type = access_type

    @property
    def label(self):
        """Gets the label of this ProviderInput.

        A human readable label for the provider

        :return: The label of this ProviderInput.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ProviderInput.

        A human readable label for the provider

        :param label: The label of this ProviderInput.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def config(self):
        """Gets the config of this ProviderInput.

        The provider-specific configuration fields.

        :return: The config of this ProviderInput.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ProviderInput.

        The provider-specific configuration fields.

        :param config: The config of this ProviderInput.  # noqa: E501
        :type: object
        """

        self._config = config

    @property
    def creds(self):
        """Gets the creds of this ProviderInput.

        The provider-specific credential fields.

        :return: The creds of this ProviderInput.
        :rtype: object
        """
        return self._creds

    @creds.setter
    def creds(self, creds):
        """Sets the creds of this ProviderInput.

        The provider-specific credential fields.

        :param creds: The creds of this ProviderInput.  # noqa: E501
        :type: object
        """

        self._creds = creds


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
        if not isinstance(other, ProviderInput):
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

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


class ExecutorInfo(object):

    swagger_types = {
        'name': 'str',
        'host': 'str',
        'instance_type': 'str',
        'cpu_cores': 'int',
        'gpu': 'bool',
        'memory_bytes': 'int',
        'disk_bytes': 'int',
        'swap_bytes': 'int'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'instance_type': 'instance_type',
        'cpu_cores': 'cpu_cores',
        'gpu': 'gpu',
        'memory_bytes': 'memory_bytes',
        'disk_bytes': 'disk_bytes',
        'swap_bytes': 'swap_bytes'
    }

    rattribute_map = {
        'name': 'name',
        'host': 'host',
        'instance_type': 'instance_type',
        'cpu_cores': 'cpu_cores',
        'gpu': 'gpu',
        'memory_bytes': 'memory_bytes',
        'disk_bytes': 'disk_bytes',
        'swap_bytes': 'swap_bytes'
    }

    def __init__(self, name=None, host=None, instance_type=None, cpu_cores=None, gpu=None, memory_bytes=None, disk_bytes=None, swap_bytes=None):  # noqa: E501
        """ExecutorInfo - a model defined in Swagger"""
        super(ExecutorInfo, self).__init__()

        self._name = None
        self._host = None
        self._instance_type = None
        self._cpu_cores = None
        self._gpu = None
        self._memory_bytes = None
        self._disk_bytes = None
        self._swap_bytes = None
        self.discriminator = None
        self.alt_discriminator = None

        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if instance_type is not None:
            self.instance_type = instance_type
        if cpu_cores is not None:
            self.cpu_cores = cpu_cores
        if gpu is not None:
            self.gpu = gpu
        if memory_bytes is not None:
            self.memory_bytes = memory_bytes
        if disk_bytes is not None:
            self.disk_bytes = disk_bytes
        if swap_bytes is not None:
            self.swap_bytes = swap_bytes

    @property
    def name(self):
        """Gets the name of this ExecutorInfo.


        :return: The name of this ExecutorInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecutorInfo.


        :param name: The name of this ExecutorInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this ExecutorInfo.


        :return: The host of this ExecutorInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ExecutorInfo.


        :param host: The host of this ExecutorInfo.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def instance_type(self):
        """Gets the instance_type of this ExecutorInfo.


        :return: The instance_type of this ExecutorInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ExecutorInfo.


        :param instance_type: The instance_type of this ExecutorInfo.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this ExecutorInfo.


        :return: The cpu_cores of this ExecutorInfo.
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this ExecutorInfo.


        :param cpu_cores: The cpu_cores of this ExecutorInfo.  # noqa: E501
        :type: int
        """

        self._cpu_cores = cpu_cores

    @property
    def gpu(self):
        """Gets the gpu of this ExecutorInfo.


        :return: The gpu of this ExecutorInfo.
        :rtype: bool
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this ExecutorInfo.


        :param gpu: The gpu of this ExecutorInfo.  # noqa: E501
        :type: bool
        """

        self._gpu = gpu

    @property
    def memory_bytes(self):
        """Gets the memory_bytes of this ExecutorInfo.


        :return: The memory_bytes of this ExecutorInfo.
        :rtype: int
        """
        return self._memory_bytes

    @memory_bytes.setter
    def memory_bytes(self, memory_bytes):
        """Sets the memory_bytes of this ExecutorInfo.


        :param memory_bytes: The memory_bytes of this ExecutorInfo.  # noqa: E501
        :type: int
        """

        self._memory_bytes = memory_bytes

    @property
    def disk_bytes(self):
        """Gets the disk_bytes of this ExecutorInfo.


        :return: The disk_bytes of this ExecutorInfo.
        :rtype: int
        """
        return self._disk_bytes

    @disk_bytes.setter
    def disk_bytes(self, disk_bytes):
        """Sets the disk_bytes of this ExecutorInfo.


        :param disk_bytes: The disk_bytes of this ExecutorInfo.  # noqa: E501
        :type: int
        """

        self._disk_bytes = disk_bytes

    @property
    def swap_bytes(self):
        """Gets the swap_bytes of this ExecutorInfo.


        :return: The swap_bytes of this ExecutorInfo.
        :rtype: int
        """
        return self._swap_bytes

    @swap_bytes.setter
    def swap_bytes(self, swap_bytes):
        """Sets the swap_bytes of this ExecutorInfo.


        :param swap_bytes: The swap_bytes of this ExecutorInfo.  # noqa: E501
        :type: int
        """

        self._swap_bytes = swap_bytes


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
        if not isinstance(other, ExecutorInfo):
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

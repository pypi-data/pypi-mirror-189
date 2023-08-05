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

from flywheel.models.container_reference import ContainerReference  # noqa: F401,E501
from flywheel.models.deid_log_skip_reason import DeidLogSkipReason  # noqa: F401,E501
from flywheel.models.file_gear_info import FileGearInfo  # noqa: F401,E501
from flywheel.models.file_parents import FileParents  # noqa: F401,E501
from flywheel.models.file_version import FileVersion  # noqa: F401,E501
from flywheel.models.file_version_copy_of import FileVersionCopyOf  # noqa: F401,E501
from flywheel.models.origin import Origin  # noqa: F401,E501
from flywheel.models.virus_scan import VirusScan  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class FileOutput(object):

    swagger_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'file_id': 'str',
        'version': 'int',
        'mimetype': 'str',
        'modality': 'str',
        'deid_log_id': 'str',
        'deid_log_skip_reason': 'DeidLogSkipReason',
        'classification': 'dict(str, list[str])',
        'tags': 'list[str]',
        'provider_id': 'str',
        'parent_ref': 'ContainerReference',
        'parents': 'FileParents',
        'restored_from': 'int',
        'restored_by': 'Origin',
        'path': 'str',
        'reference': 'bool',
        'origin': 'Origin',
        'virus_scan': 'VirusScan',
        'created': 'datetime',
        'modified': 'datetime',
        'replaced': 'datetime',
        'deleted': 'datetime',
        'size': 'int',
        'hash': 'str',
        'client_hash': 'str',
        'info': 'object',
        'info_exists': 'bool',
        'zip_member_count': 'int',
        'gear_info': 'FileGearInfo',
        'copy_of': 'FileVersionCopyOf',
        'original_copy_of': 'FileVersion'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'type': 'type',
        'file_id': 'file_id',
        'version': 'version',
        'mimetype': 'mimetype',
        'modality': 'modality',
        'deid_log_id': 'deid_log_id',
        'deid_log_skip_reason': 'deid_log_skip_reason',
        'classification': 'classification',
        'tags': 'tags',
        'provider_id': 'provider_id',
        'parent_ref': 'parent_ref',
        'parents': 'parents',
        'restored_from': 'restored_from',
        'restored_by': 'restored_by',
        'path': 'path',
        'reference': 'reference',
        'origin': 'origin',
        'virus_scan': 'virus_scan',
        'created': 'created',
        'modified': 'modified',
        'replaced': 'replaced',
        'deleted': 'deleted',
        'size': 'size',
        'hash': 'hash',
        'client_hash': 'client_hash',
        'info': 'info',
        'info_exists': 'info_exists',
        'zip_member_count': 'zip_member_count',
        'gear_info': 'gear_info',
        'copy_of': 'copy_of',
        'original_copy_of': 'original_copy_of'
    }

    rattribute_map = {
        '_id': 'id',
        'name': 'name',
        'type': 'type',
        'file_id': 'file_id',
        'version': 'version',
        'mimetype': 'mimetype',
        'modality': 'modality',
        'deid_log_id': 'deid_log_id',
        'deid_log_skip_reason': 'deid_log_skip_reason',
        'classification': 'classification',
        'tags': 'tags',
        'provider_id': 'provider_id',
        'parent_ref': 'parent_ref',
        'parents': 'parents',
        'restored_from': 'restored_from',
        'restored_by': 'restored_by',
        'path': 'path',
        'reference': 'reference',
        'origin': 'origin',
        'virus_scan': 'virus_scan',
        'created': 'created',
        'modified': 'modified',
        'replaced': 'replaced',
        'deleted': 'deleted',
        'size': 'size',
        'hash': 'hash',
        'client_hash': 'client_hash',
        'info': 'info',
        'info_exists': 'info_exists',
        'zip_member_count': 'zip_member_count',
        'gear_info': 'gear_info',
        'copy_of': 'copy_of',
        'original_copy_of': 'original_copy_of'
    }

    def __init__(self, id=None, name=None, type=None, file_id=None, version=None, mimetype=None, modality=None, deid_log_id=None, deid_log_skip_reason=None, classification=None, tags=None, provider_id=None, parent_ref=None, parents=None, restored_from=None, restored_by=None, path=None, reference=None, origin=None, virus_scan=None, created=None, modified=None, replaced=None, deleted=None, size=None, hash=None, client_hash=None, info=None, info_exists=False, zip_member_count=None, gear_info=None, copy_of=None, original_copy_of=None):  # noqa: E501
        """FileOutput - a model defined in Swagger"""
        super(FileOutput, self).__init__()

        self._id = None
        self._name = None
        self._type = None
        self._file_id = None
        self._version = None
        self._mimetype = None
        self._modality = None
        self._deid_log_id = None
        self._deid_log_skip_reason = None
        self._classification = None
        self._tags = None
        self._provider_id = None
        self._parent_ref = None
        self._parents = None
        self._restored_from = None
        self._restored_by = None
        self._path = None
        self._reference = None
        self._origin = None
        self._virus_scan = None
        self._created = None
        self._modified = None
        self._replaced = None
        self._deleted = None
        self._size = None
        self._hash = None
        self._client_hash = None
        self._info = None
        self._info_exists = None
        self._zip_member_count = None
        self._gear_info = None
        self._copy_of = None
        self._original_copy_of = None
        self.discriminator = None
        self.alt_discriminator = None

        self.id = id
        self.name = name
        if type is not None:
            self.type = type
        self.file_id = file_id
        self.version = version
        self.mimetype = mimetype
        if modality is not None:
            self.modality = modality
        if deid_log_id is not None:
            self.deid_log_id = deid_log_id
        if deid_log_skip_reason is not None:
            self.deid_log_skip_reason = deid_log_skip_reason
        if classification is not None:
            self.classification = classification
        if tags is not None:
            self.tags = tags
        self.provider_id = provider_id
        self.parent_ref = parent_ref
        if parents is not None:
            self.parents = parents
        if restored_from is not None:
            self.restored_from = restored_from
        if restored_by is not None:
            self.restored_by = restored_by
        if path is not None:
            self.path = path
        if reference is not None:
            self.reference = reference
        self.origin = origin
        if virus_scan is not None:
            self.virus_scan = virus_scan
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if replaced is not None:
            self.replaced = replaced
        if deleted is not None:
            self.deleted = deleted
        self.size = size
        if hash is not None:
            self.hash = hash
        if client_hash is not None:
            self.client_hash = client_hash
        self.info = info
        if info_exists is not None:
            self.info_exists = info_exists
        if zip_member_count is not None:
            self.zip_member_count = zip_member_count
        if gear_info is not None:
            self.gear_info = gear_info
        if copy_of is not None:
            self.copy_of = copy_of
        if original_copy_of is not None:
            self.original_copy_of = original_copy_of

    @property
    def id(self):
        """Gets the id of this FileOutput.


        :return: The id of this FileOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileOutput.


        :param id: The id of this FileOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileOutput.


        :return: The name of this FileOutput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileOutput.


        :param name: The name of this FileOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this FileOutput.


        :return: The type of this FileOutput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileOutput.


        :param type: The type of this FileOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def file_id(self):
        """Gets the file_id of this FileOutput.


        :return: The file_id of this FileOutput.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileOutput.


        :param file_id: The file_id of this FileOutput.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def version(self):
        """Gets the version of this FileOutput.


        :return: The version of this FileOutput.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileOutput.


        :param version: The version of this FileOutput.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def mimetype(self):
        """Gets the mimetype of this FileOutput.


        :return: The mimetype of this FileOutput.
        :rtype: str
        """
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        """Sets the mimetype of this FileOutput.


        :param mimetype: The mimetype of this FileOutput.  # noqa: E501
        :type: str
        """

        self._mimetype = mimetype

    @property
    def modality(self):
        """Gets the modality of this FileOutput.


        :return: The modality of this FileOutput.
        :rtype: str
        """
        return self._modality

    @modality.setter
    def modality(self, modality):
        """Sets the modality of this FileOutput.


        :param modality: The modality of this FileOutput.  # noqa: E501
        :type: str
        """

        self._modality = modality

    @property
    def deid_log_id(self):
        """Gets the deid_log_id of this FileOutput.


        :return: The deid_log_id of this FileOutput.
        :rtype: str
        """
        return self._deid_log_id

    @deid_log_id.setter
    def deid_log_id(self, deid_log_id):
        """Sets the deid_log_id of this FileOutput.


        :param deid_log_id: The deid_log_id of this FileOutput.  # noqa: E501
        :type: str
        """

        self._deid_log_id = deid_log_id

    @property
    def deid_log_skip_reason(self):
        """Gets the deid_log_skip_reason of this FileOutput.


        :return: The deid_log_skip_reason of this FileOutput.
        :rtype: DeidLogSkipReason
        """
        return self._deid_log_skip_reason

    @deid_log_skip_reason.setter
    def deid_log_skip_reason(self, deid_log_skip_reason):
        """Sets the deid_log_skip_reason of this FileOutput.


        :param deid_log_skip_reason: The deid_log_skip_reason of this FileOutput.  # noqa: E501
        :type: DeidLogSkipReason
        """

        self._deid_log_skip_reason = deid_log_skip_reason

    @property
    def classification(self):
        """Gets the classification of this FileOutput.


        :return: The classification of this FileOutput.
        :rtype: dict(str, list[str])
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this FileOutput.


        :param classification: The classification of this FileOutput.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._classification = classification

    @property
    def tags(self):
        """Gets the tags of this FileOutput.


        :return: The tags of this FileOutput.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FileOutput.


        :param tags: The tags of this FileOutput.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def provider_id(self):
        """Gets the provider_id of this FileOutput.


        :return: The provider_id of this FileOutput.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this FileOutput.


        :param provider_id: The provider_id of this FileOutput.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def parent_ref(self):
        """Gets the parent_ref of this FileOutput.


        :return: The parent_ref of this FileOutput.
        :rtype: ContainerReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """Sets the parent_ref of this FileOutput.


        :param parent_ref: The parent_ref of this FileOutput.  # noqa: E501
        :type: ContainerReference
        """

        self._parent_ref = parent_ref

    @property
    def parents(self):
        """Gets the parents of this FileOutput.


        :return: The parents of this FileOutput.
        :rtype: FileParents
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this FileOutput.


        :param parents: The parents of this FileOutput.  # noqa: E501
        :type: FileParents
        """

        self._parents = parents

    @property
    def restored_from(self):
        """Gets the restored_from of this FileOutput.


        :return: The restored_from of this FileOutput.
        :rtype: int
        """
        return self._restored_from

    @restored_from.setter
    def restored_from(self, restored_from):
        """Sets the restored_from of this FileOutput.


        :param restored_from: The restored_from of this FileOutput.  # noqa: E501
        :type: int
        """

        self._restored_from = restored_from

    @property
    def restored_by(self):
        """Gets the restored_by of this FileOutput.


        :return: The restored_by of this FileOutput.
        :rtype: Origin
        """
        return self._restored_by

    @restored_by.setter
    def restored_by(self, restored_by):
        """Sets the restored_by of this FileOutput.


        :param restored_by: The restored_by of this FileOutput.  # noqa: E501
        :type: Origin
        """

        self._restored_by = restored_by

    @property
    def path(self):
        """Gets the path of this FileOutput.


        :return: The path of this FileOutput.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileOutput.


        :param path: The path of this FileOutput.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def reference(self):
        """Gets the reference of this FileOutput.


        :return: The reference of this FileOutput.
        :rtype: bool
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this FileOutput.


        :param reference: The reference of this FileOutput.  # noqa: E501
        :type: bool
        """

        self._reference = reference

    @property
    def origin(self):
        """Gets the origin of this FileOutput.


        :return: The origin of this FileOutput.
        :rtype: Origin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this FileOutput.


        :param origin: The origin of this FileOutput.  # noqa: E501
        :type: Origin
        """

        self._origin = origin

    @property
    def virus_scan(self):
        """Gets the virus_scan of this FileOutput.


        :return: The virus_scan of this FileOutput.
        :rtype: VirusScan
        """
        return self._virus_scan

    @virus_scan.setter
    def virus_scan(self, virus_scan):
        """Sets the virus_scan of this FileOutput.


        :param virus_scan: The virus_scan of this FileOutput.  # noqa: E501
        :type: VirusScan
        """

        self._virus_scan = virus_scan

    @property
    def created(self):
        """Gets the created of this FileOutput.


        :return: The created of this FileOutput.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileOutput.


        :param created: The created of this FileOutput.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this FileOutput.


        :return: The modified of this FileOutput.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this FileOutput.


        :param modified: The modified of this FileOutput.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def replaced(self):
        """Gets the replaced of this FileOutput.


        :return: The replaced of this FileOutput.
        :rtype: datetime
        """
        return self._replaced

    @replaced.setter
    def replaced(self, replaced):
        """Sets the replaced of this FileOutput.


        :param replaced: The replaced of this FileOutput.  # noqa: E501
        :type: datetime
        """

        self._replaced = replaced

    @property
    def deleted(self):
        """Gets the deleted of this FileOutput.


        :return: The deleted of this FileOutput.
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this FileOutput.


        :param deleted: The deleted of this FileOutput.  # noqa: E501
        :type: datetime
        """

        self._deleted = deleted

    @property
    def size(self):
        """Gets the size of this FileOutput.


        :return: The size of this FileOutput.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileOutput.


        :param size: The size of this FileOutput.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def hash(self):
        """Gets the hash of this FileOutput.


        :return: The hash of this FileOutput.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this FileOutput.


        :param hash: The hash of this FileOutput.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def client_hash(self):
        """Gets the client_hash of this FileOutput.


        :return: The client_hash of this FileOutput.
        :rtype: str
        """
        return self._client_hash

    @client_hash.setter
    def client_hash(self, client_hash):
        """Sets the client_hash of this FileOutput.


        :param client_hash: The client_hash of this FileOutput.  # noqa: E501
        :type: str
        """

        self._client_hash = client_hash

    @property
    def info(self):
        """Gets the info of this FileOutput.


        :return: The info of this FileOutput.
        :rtype: object
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this FileOutput.


        :param info: The info of this FileOutput.  # noqa: E501
        :type: object
        """

        self._info = info

    @property
    def info_exists(self):
        """Gets the info_exists of this FileOutput.


        :return: The info_exists of this FileOutput.
        :rtype: bool
        """
        return self._info_exists

    @info_exists.setter
    def info_exists(self, info_exists):
        """Sets the info_exists of this FileOutput.


        :param info_exists: The info_exists of this FileOutput.  # noqa: E501
        :type: bool
        """

        self._info_exists = info_exists

    @property
    def zip_member_count(self):
        """Gets the zip_member_count of this FileOutput.


        :return: The zip_member_count of this FileOutput.
        :rtype: int
        """
        return self._zip_member_count

    @zip_member_count.setter
    def zip_member_count(self, zip_member_count):
        """Sets the zip_member_count of this FileOutput.


        :param zip_member_count: The zip_member_count of this FileOutput.  # noqa: E501
        :type: int
        """

        self._zip_member_count = zip_member_count

    @property
    def gear_info(self):
        """Gets the gear_info of this FileOutput.


        :return: The gear_info of this FileOutput.
        :rtype: FileGearInfo
        """
        return self._gear_info

    @gear_info.setter
    def gear_info(self, gear_info):
        """Sets the gear_info of this FileOutput.


        :param gear_info: The gear_info of this FileOutput.  # noqa: E501
        :type: FileGearInfo
        """

        self._gear_info = gear_info

    @property
    def copy_of(self):
        """Gets the copy_of of this FileOutput.


        :return: The copy_of of this FileOutput.
        :rtype: FileVersionCopyOf
        """
        return self._copy_of

    @copy_of.setter
    def copy_of(self, copy_of):
        """Sets the copy_of of this FileOutput.


        :param copy_of: The copy_of of this FileOutput.  # noqa: E501
        :type: FileVersionCopyOf
        """

        self._copy_of = copy_of

    @property
    def original_copy_of(self):
        """Gets the original_copy_of of this FileOutput.


        :return: The original_copy_of of this FileOutput.
        :rtype: FileVersion
        """
        return self._original_copy_of

    @original_copy_of.setter
    def original_copy_of(self, original_copy_of):
        """Sets the original_copy_of of this FileOutput.


        :param original_copy_of: The original_copy_of of this FileOutput.  # noqa: E501
        :type: FileVersion
        """

        self._original_copy_of = original_copy_of


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
        if not isinstance(other, FileOutput):
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

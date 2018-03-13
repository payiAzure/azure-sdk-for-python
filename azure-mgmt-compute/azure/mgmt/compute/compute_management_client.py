# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION


class ComputeManagementClientConfiguration(AzureConfiguration):
    """Configuration for ComputeManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ComputeManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('computemanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ComputeManagementClient(object):
    """Compute Client.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation 
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: ComputeManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A dict using operation group name to API version.
    :type profile: dict[str, str]
    """

    DEFAULT_API_VERSION = '2017-12-01'
    DEFAULT_PROFILE = {
        'disks': '2017-03-30',
        'resource_skus': '2017-09-01',
        'snapshots': '2017-03-30',
    }

    def __init__(self, credentials, subscription_id, api_version=DEFAULT_API_VERSION, base_url=None, profile=DEFAULT_PROFILE):

        self.config = ComputeManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        self.api_version = api_version
        self.profile = dict(profile) if profile is not None else {}

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-06-15: :mod:`v2015_06_15.models<azure.mgmt.compute.v2015_06_15.models>`
           * 2016-03-30: :mod:`v2016_03_30.models<azure.mgmt.compute.v2016_03_30.models>`
           * 2016-04-30-preview: :mod:`v2016_04_30_preview.models<azure.mgmt.compute.v2016_04_30_preview.models>`
           * 2017-03-30: :mod:`v2017_03_30.models<azure.mgmt.compute.v2017_03_30.models>`
           * 2017-09-01: :mod:`v2017_09_01.models<azure.mgmt.compute.v2017_09_01.models>`
           * 2017-12-01: :mod:`v2017_12_01.models<azure.mgmt.compute.v2017_12_01.models>`
        """
        if api_version == '2015-06-15':
            from .v2015_06_15 import models
            return models
        elif api_version == '2016-03-30':
            from .v2016_03_30 import models
            return models
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview import models
            return models
        elif api_version == '2017-03-30':
            from .v2017_03_30 import models
            return models
        elif api_version == '2017-09-01':
            from .v2017_09_01 import models
            return models
        elif api_version == '2017-12-01':
            from .v2017_12_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
    
    @property
    def availability_sets(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`AvailabilitySetsOperations<azure.mgmt.compute.v2015_06_15.operations.AvailabilitySetsOperations>`
           * 2016-03-30: :class:`AvailabilitySetsOperations<azure.mgmt.compute.v2016_03_30.operations.AvailabilitySetsOperations>`
           * 2016-04-30-preview: :class:`AvailabilitySetsOperations<azure.mgmt.compute.v2016_04_30_preview.operations.AvailabilitySetsOperations>`
           * 2017-03-30: :class:`AvailabilitySetsOperations<azure.mgmt.compute.v2017_03_30.operations.AvailabilitySetsOperations>`
           * 2017-12-01: :class:`AvailabilitySetsOperations<azure.mgmt.compute.v2017_12_01.operations.AvailabilitySetsOperations>`
        """
        api_version = self.profile.get('availability_sets', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import AvailabilitySetsOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import AvailabilitySetsOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import AvailabilitySetsOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import AvailabilitySetsOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import AvailabilitySetsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def disks(self):
        """Instance depends on the API version:

           * 2016-04-30-preview: :class:`DisksOperations<azure.mgmt.compute.v2016_04_30_preview.operations.DisksOperations>`
           * 2017-03-30: :class:`DisksOperations<azure.mgmt.compute.v2017_03_30.operations.DisksOperations>`
        """
        api_version = self.profile.get('disks', self.api_version)
        if api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import DisksOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import DisksOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def images(self):
        """Instance depends on the API version:

           * 2016-04-30-preview: :class:`ImagesOperations<azure.mgmt.compute.v2016_04_30_preview.operations.ImagesOperations>`
           * 2017-03-30: :class:`ImagesOperations<azure.mgmt.compute.v2017_03_30.operations.ImagesOperations>`
           * 2017-12-01: :class:`ImagesOperations<azure.mgmt.compute.v2017_12_01.operations.ImagesOperations>`
        """
        api_version = self.profile.get('images', self.api_version)
        if api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import ImagesOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import ImagesOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import ImagesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def log_analytics(self):
        """Instance depends on the API version:

           * 2017-12-01: :class:`LogAnalyticsOperations<azure.mgmt.compute.v2017_12_01.operations.LogAnalyticsOperations>`
        """
        api_version = self.profile.get('log_analytics', self.api_version)
        if api_version == '2017-12-01':
            from .v2017_12_01.operations import LogAnalyticsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2017-12-01: :class:`Operations<azure.mgmt.compute.v2017_12_01.operations.Operations>`
        """
        api_version = self.profile.get('operations', self.api_version)
        if api_version == '2017-12-01':
            from .v2017_12_01.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def resource_skus(self):
        """Instance depends on the API version:

           * 2017-03-30: :class:`ResourceSkusOperations<azure.mgmt.compute.v2017_03_30.operations.ResourceSkusOperations>`
           * 2017-09-01: :class:`ResourceSkusOperations<azure.mgmt.compute.v2017_09_01.operations.ResourceSkusOperations>`
        """
        api_version = self.profile.get('resource_skus', self.api_version)
        if api_version == '2017-03-30':
            from .v2017_03_30.operations import ResourceSkusOperations as OperationClass
        elif api_version == '2017-09-01':
            from .v2017_09_01.operations import ResourceSkusOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def snapshots(self):
        """Instance depends on the API version:

           * 2016-04-30-preview: :class:`SnapshotsOperations<azure.mgmt.compute.v2016_04_30_preview.operations.SnapshotsOperations>`
           * 2017-03-30: :class:`SnapshotsOperations<azure.mgmt.compute.v2017_03_30.operations.SnapshotsOperations>`
        """
        api_version = self.profile.get('snapshots', self.api_version)
        if api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import SnapshotsOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import SnapshotsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def usage(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`UsageOperations<azure.mgmt.compute.v2015_06_15.operations.UsageOperations>`
           * 2016-03-30: :class:`UsageOperations<azure.mgmt.compute.v2016_03_30.operations.UsageOperations>`
           * 2016-04-30-preview: :class:`UsageOperations<azure.mgmt.compute.v2016_04_30_preview.operations.UsageOperations>`
           * 2017-03-30: :class:`UsageOperations<azure.mgmt.compute.v2017_03_30.operations.UsageOperations>`
           * 2017-12-01: :class:`UsageOperations<azure.mgmt.compute.v2017_12_01.operations.UsageOperations>`
        """
        api_version = self.profile.get('usage', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import UsageOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import UsageOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import UsageOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import UsageOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import UsageOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_extension_images(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachineExtensionImagesOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachineExtensionImagesOperations>`
           * 2016-03-30: :class:`VirtualMachineExtensionImagesOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachineExtensionImagesOperations>`
           * 2016-04-30-preview: :class:`VirtualMachineExtensionImagesOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineExtensionImagesOperations>`
           * 2017-03-30: :class:`VirtualMachineExtensionImagesOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineExtensionImagesOperations>`
           * 2017-12-01: :class:`VirtualMachineExtensionImagesOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineExtensionImagesOperations>`
        """
        api_version = self.profile.get('virtual_machine_extension_images', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachineExtensionImagesOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachineExtensionImagesOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachineExtensionImagesOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineExtensionImagesOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineExtensionImagesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_extensions(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachineExtensionsOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachineExtensionsOperations>`
           * 2016-03-30: :class:`VirtualMachineExtensionsOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachineExtensionsOperations>`
           * 2016-04-30-preview: :class:`VirtualMachineExtensionsOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineExtensionsOperations>`
           * 2017-03-30: :class:`VirtualMachineExtensionsOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineExtensionsOperations>`
           * 2017-12-01: :class:`VirtualMachineExtensionsOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineExtensionsOperations>`
        """
        api_version = self.profile.get('virtual_machine_extensions', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachineExtensionsOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachineExtensionsOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachineExtensionsOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineExtensionsOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineExtensionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_images(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachineImagesOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachineImagesOperations>`
           * 2016-03-30: :class:`VirtualMachineImagesOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachineImagesOperations>`
           * 2016-04-30-preview: :class:`VirtualMachineImagesOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineImagesOperations>`
           * 2017-03-30: :class:`VirtualMachineImagesOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineImagesOperations>`
           * 2017-12-01: :class:`VirtualMachineImagesOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineImagesOperations>`
        """
        api_version = self.profile.get('virtual_machine_images', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachineImagesOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachineImagesOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachineImagesOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineImagesOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineImagesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_run_commands(self):
        """Instance depends on the API version:

           * 2017-03-30: :class:`VirtualMachineRunCommandsOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineRunCommandsOperations>`
           * 2017-12-01: :class:`VirtualMachineRunCommandsOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineRunCommandsOperations>`
        """
        api_version = self.profile.get('virtual_machine_run_commands', self.api_version)
        if api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineRunCommandsOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineRunCommandsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_scale_set_extensions(self):
        """Instance depends on the API version:

           * 2017-03-30: :class:`VirtualMachineScaleSetExtensionsOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetExtensionsOperations>`
           * 2017-12-01: :class:`VirtualMachineScaleSetExtensionsOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineScaleSetExtensionsOperations>`
        """
        api_version = self.profile.get('virtual_machine_scale_set_extensions', self.api_version)
        if api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineScaleSetExtensionsOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineScaleSetExtensionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_scale_set_rolling_upgrades(self):
        """Instance depends on the API version:

           * 2017-03-30: :class:`VirtualMachineScaleSetRollingUpgradesOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetRollingUpgradesOperations>`
           * 2017-12-01: :class:`VirtualMachineScaleSetRollingUpgradesOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineScaleSetRollingUpgradesOperations>`
        """
        api_version = self.profile.get('virtual_machine_scale_set_rolling_upgrades', self.api_version)
        if api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineScaleSetRollingUpgradesOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineScaleSetRollingUpgradesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_scale_set_vms(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachineScaleSetVMsOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachineScaleSetVMsOperations>`
           * 2016-03-30: :class:`VirtualMachineScaleSetVMsOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachineScaleSetVMsOperations>`
           * 2016-04-30-preview: :class:`VirtualMachineScaleSetVMsOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineScaleSetVMsOperations>`
           * 2017-03-30: :class:`VirtualMachineScaleSetVMsOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetVMsOperations>`
           * 2017-12-01: :class:`VirtualMachineScaleSetVMsOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineScaleSetVMsOperations>`
        """
        api_version = self.profile.get('virtual_machine_scale_set_vms', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachineScaleSetVMsOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachineScaleSetVMsOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachineScaleSetVMsOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineScaleSetVMsOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineScaleSetVMsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_scale_sets(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachineScaleSetsOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachineScaleSetsOperations>`
           * 2016-03-30: :class:`VirtualMachineScaleSetsOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachineScaleSetsOperations>`
           * 2016-04-30-preview: :class:`VirtualMachineScaleSetsOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineScaleSetsOperations>`
           * 2017-03-30: :class:`VirtualMachineScaleSetsOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetsOperations>`
           * 2017-12-01: :class:`VirtualMachineScaleSetsOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineScaleSetsOperations>`
        """
        api_version = self.profile.get('virtual_machine_scale_sets', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachineScaleSetsOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachineScaleSetsOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachineScaleSetsOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineScaleSetsOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineScaleSetsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machine_sizes(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachineSizesOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachineSizesOperations>`
           * 2016-03-30: :class:`VirtualMachineSizesOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachineSizesOperations>`
           * 2016-04-30-preview: :class:`VirtualMachineSizesOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineSizesOperations>`
           * 2017-03-30: :class:`VirtualMachineSizesOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachineSizesOperations>`
           * 2017-12-01: :class:`VirtualMachineSizesOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachineSizesOperations>`
        """
        api_version = self.profile.get('virtual_machine_sizes', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachineSizesOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachineSizesOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachineSizesOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachineSizesOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachineSizesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_machines(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`VirtualMachinesOperations<azure.mgmt.compute.v2015_06_15.operations.VirtualMachinesOperations>`
           * 2016-03-30: :class:`VirtualMachinesOperations<azure.mgmt.compute.v2016_03_30.operations.VirtualMachinesOperations>`
           * 2016-04-30-preview: :class:`VirtualMachinesOperations<azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachinesOperations>`
           * 2017-03-30: :class:`VirtualMachinesOperations<azure.mgmt.compute.v2017_03_30.operations.VirtualMachinesOperations>`
           * 2017-12-01: :class:`VirtualMachinesOperations<azure.mgmt.compute.v2017_12_01.operations.VirtualMachinesOperations>`
        """
        api_version = self.profile.get('virtual_machines', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import VirtualMachinesOperations as OperationClass
        elif api_version == '2016-03-30':
            from .v2016_03_30.operations import VirtualMachinesOperations as OperationClass
        elif api_version == '2016-04-30-preview':
            from .v2016_04_30_preview.operations import VirtualMachinesOperations as OperationClass
        elif api_version == '2017-03-30':
            from .v2017_03_30.operations import VirtualMachinesOperations as OperationClass
        elif api_version == '2017-12-01':
            from .v2017_12_01.operations import VirtualMachinesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

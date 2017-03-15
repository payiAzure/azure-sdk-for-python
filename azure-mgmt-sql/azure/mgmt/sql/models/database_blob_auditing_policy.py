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

from .sql_typed_sub_resource import SqlTypedSubResource


class DatabaseBlobAuditingPolicy(SqlTypedSubResource):
    """Contains information about a database Blob Auditing policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name
    :vartype name: str
    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: Resource type
    :vartype type: str
    :param state: Specifies the state of the policy. If state is Enabled,
     storageEndpoint and storageAccountAccessKey are required. Possible values
     include: 'Enabled', 'Disabled'
    :type state: str or :class:`BlobAuditingPolicyState
     <azure.mgmt.sql.models.BlobAuditingPolicyState>`
    :param storage_endpoint: Specifies the blob storage endpoint (e.g.
     https://MyAccount.blob.core.windows.net). If state is Enabled,
     storageEndpoint is required.
    :type storage_endpoint: str
    :param storage_account_access_key: Specifies the identifier key of the
     auditing storage account. If state is Enabled, storageAccountAccessKey is
     required.
    :type storage_account_access_key: str
    :param retention_days: Specifies the number of days to keep in the audit
     logs.
    :type retention_days: int
    :param audit_actions_and_groups: Specifies the Actions and Actions-Groups
     to audit.
    :type audit_actions_and_groups: list of str
    :param storage_account_subscription_id: Specifies the blob storage
     subscription Id.
    :type storage_account_subscription_id: str
    :param is_storage_secondary_key_in_use: Specifies whether
     storageAccountAccessKey value is the storage’s secondary key.
    :type is_storage_secondary_key_in_use: bool
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'BlobAuditingPolicyState'},
        'storage_endpoint': {'key': 'properties.storageEndpoint', 'type': 'str'},
        'storage_account_access_key': {'key': 'properties.storageAccountAccessKey', 'type': 'str'},
        'retention_days': {'key': 'properties.retentionDays', 'type': 'int'},
        'audit_actions_and_groups': {'key': 'properties.auditActionsAndGroups', 'type': '[str]'},
        'storage_account_subscription_id': {'key': 'properties.storageAccountSubscriptionId', 'type': 'str'},
        'is_storage_secondary_key_in_use': {'key': 'properties.isStorageSecondaryKeyInUse', 'type': 'bool'},
    }

    def __init__(self, state, storage_endpoint=None, storage_account_access_key=None, retention_days=None, audit_actions_and_groups=None, storage_account_subscription_id=None, is_storage_secondary_key_in_use=None):
        super(DatabaseBlobAuditingPolicy, self).__init__()
        self.state = state
        self.storage_endpoint = storage_endpoint
        self.storage_account_access_key = storage_account_access_key
        self.retention_days = retention_days
        self.audit_actions_and_groups = audit_actions_and_groups
        self.storage_account_subscription_id = storage_account_subscription_id
        self.is_storage_secondary_key_in_use = is_storage_secondary_key_in_use
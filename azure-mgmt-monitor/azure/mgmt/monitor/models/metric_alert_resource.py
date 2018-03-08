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

from .resource import Resource


class MetricAlertResource(Resource):
    """The metric alert resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param description: Required. the description of the metric alert that
     will be included in the alert email.
    :type description: str
    :param severity: Required. Alert severity {0, 1, 2, 3, 4}
    :type severity: int
    :param enabled: Required. the flag that indicates whether the metric alert
     is enabled.
    :type enabled: bool
    :param scopes: the list of resource id's that this metric alert is scoped
     to.
    :type scopes: list[str]
    :param evaluation_frequency: Required. how often the metric alert is
     evaluated represented in ISO 8601 duration format.
    :type evaluation_frequency: timedelta
    :param window_size: Required. the period of time (in ISO 8601 duration
     format) that is used to monitor alert activity based on the threshold.
    :type window_size: timedelta
    :param criteria_schema_id: Required. schema to use to interpret the
     criteria JSON.
    :type criteria_schema_id: str
    :param criteria: Required. json data that follows the schema defined by
     criteria schema id.
    :type criteria: str
    :param actions: the array of actions that are performed when the alert
     rule becomes active, and when an alert condition is resolved.
    :type actions: list[~azure.mgmt.monitor.models.Action]
    :ivar current_status: the current metric alert status.
    :vartype current_status: ~azure.mgmt.monitor.models.AlertStatus
    :ivar last_updated_time: Last time the rule was updated in ISO8601 format.
    :vartype last_updated_time: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'description': {'required': True},
        'severity': {'required': True},
        'enabled': {'required': True},
        'evaluation_frequency': {'required': True},
        'window_size': {'required': True},
        'criteria_schema_id': {'required': True},
        'criteria': {'required': True},
        'current_status': {'readonly': True},
        'last_updated_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'int'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'scopes': {'key': 'properties.scopes', 'type': '[str]'},
        'evaluation_frequency': {'key': 'properties.evaluationFrequency', 'type': 'duration'},
        'window_size': {'key': 'properties.windowSize', 'type': 'duration'},
        'criteria_schema_id': {'key': 'properties.criteriaSchemaId', 'type': 'str'},
        'criteria': {'key': 'properties.criteria', 'type': 'str'},
        'actions': {'key': 'properties.actions', 'type': '[Action]'},
        'current_status': {'key': 'properties.currentStatus', 'type': 'AlertStatus'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(MetricAlertResource, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.severity = kwargs.get('severity', None)
        self.enabled = kwargs.get('enabled', None)
        self.scopes = kwargs.get('scopes', None)
        self.evaluation_frequency = kwargs.get('evaluation_frequency', None)
        self.window_size = kwargs.get('window_size', None)
        self.criteria_schema_id = kwargs.get('criteria_schema_id', None)
        self.criteria = kwargs.get('criteria', None)
        self.actions = kwargs.get('actions', None)
        self.current_status = None
        self.last_updated_time = None

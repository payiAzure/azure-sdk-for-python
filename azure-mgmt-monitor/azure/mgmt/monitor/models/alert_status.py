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

from msrest.serialization import Model


class AlertStatus(Model):
    """An alert status.

    :param value: status value
    :type value: str
    :param timestamp: UTC time when the status was checked.
    :type timestamp: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AlertStatus, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.timestamp = kwargs.get('timestamp', None)

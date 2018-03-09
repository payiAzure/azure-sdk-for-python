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


class QueryTroubleshootingParameters(Model):
    """Parameters that define the resource to query the troubleshooting result.

    All required parameters must be populated in order to send to Azure.

    :param target_resource_id: Required. The target resource ID to query the
     troubleshooting result.
    :type target_resource_id: str
    """

    _validation = {
        'target_resource_id': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
    }

    def __init__(self, *, target_resource_id: str, **kwargs) -> None:
        super(QueryTroubleshootingParameters, self).__init__(**kwargs)
        self.target_resource_id = target_resource_id

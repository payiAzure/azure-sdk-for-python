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


class FileServerStatus(Model):
    """Status of the file server.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Status Type and Status Code. Status Type and Status Code:
     PowerState/Creating - The fileServer is just getting created.
     PowerState/Running - The file server has been created and is available to
     be used. PowerState/Suspended - The file Server has been suspended.
     PowerState/Suspending. The user has requested that the file Server to be
     suspended, but the deallocation operation has not yet completed.
     PowerState/Deleting - The user has requested that the cluster be deleted,
     but the delete operation has not yet completed.
     PowerState/Failed/ErrorCode - The file server creation has failed with the
     specified errorCode. Details about the error code are specified in the
     message field. Possible values include: 'PowerState/Creating',
     'PowerState/Running', 'PowerState/Suspended', 'PowerState/Suspending',
     'PowerState/Deleting', 'PowerState/Failed/ErrorCode'
    :vartype code: str or :class:`Code <azure.mgmt.batchai.models.Code>`
    :ivar transition_time: State transition time for the status changed.
    :vartype transition_time: datetime
    :ivar message: Detailed message about the status.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'transition_time': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'transition_time': {'key': 'transitionTime', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self):
        self.code = None
        self.transition_time = None
        self.message = None
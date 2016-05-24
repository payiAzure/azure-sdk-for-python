# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AclStatus(Model):
    """
    Data Lake Store file or directory Access Control List information.

    :param entries: Gets or sets the list of ACLSpec entries on a file or
     directory.
    :type entries: list of str
    :param group: Gets or sets the group owner, an AAD Object ID.
    :type group: str
    :param owner: Gets or sets the user owner, an AAD Object ID.
    :type owner: str
    :param sticky_bit: Gets or sets the indicator of whether the sticky bit
     is on or off.
    :type sticky_bit: bool
    """ 

    _attribute_map = {
        'entries': {'key': 'entries', 'type': '[str]'},
        'group': {'key': 'group', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'},
        'sticky_bit': {'key': 'stickyBit', 'type': 'bool'},
    }

    def __init__(self, entries=None, group=None, owner=None, sticky_bit=None):
        self.entries = entries
        self.group = group
        self.owner = owner
        self.sticky_bit = sticky_bit
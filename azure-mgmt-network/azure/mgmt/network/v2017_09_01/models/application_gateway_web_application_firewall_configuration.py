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


class ApplicationGatewayWebApplicationFirewallConfiguration(Model):
    """Application gateway web application firewall configuration.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Whether the web application firewall is enabled
     or not.
    :type enabled: bool
    :param firewall_mode: Required. Web application firewall mode. Possible
     values include: 'Detection', 'Prevention'
    :type firewall_mode: str or
     ~azure.mgmt.network.v2017_09_01.models.ApplicationGatewayFirewallMode
    :param rule_set_type: Required. The type of the web application firewall
     rule set. Possible values are: 'OWASP'.
    :type rule_set_type: str
    :param rule_set_version: Required. The version of the rule set type.
    :type rule_set_version: str
    :param disabled_rule_groups: The disabled rule groups.
    :type disabled_rule_groups:
     list[~azure.mgmt.network.v2017_09_01.models.ApplicationGatewayFirewallDisabledRuleGroup]
    """

    _validation = {
        'enabled': {'required': True},
        'firewall_mode': {'required': True},
        'rule_set_type': {'required': True},
        'rule_set_version': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'firewall_mode': {'key': 'firewallMode', 'type': 'str'},
        'rule_set_type': {'key': 'ruleSetType', 'type': 'str'},
        'rule_set_version': {'key': 'ruleSetVersion', 'type': 'str'},
        'disabled_rule_groups': {'key': 'disabledRuleGroups', 'type': '[ApplicationGatewayFirewallDisabledRuleGroup]'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayWebApplicationFirewallConfiguration, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.firewall_mode = kwargs.get('firewall_mode', None)
        self.rule_set_type = kwargs.get('rule_set_type', None)
        self.rule_set_version = kwargs.get('rule_set_version', None)
        self.disabled_rule_groups = kwargs.get('disabled_rule_groups', None)

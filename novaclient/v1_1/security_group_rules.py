# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Security group rules interface (1.1 extension).
"""

from novaclient import base


class SecurityGroupRule(base.Resource):
    def __str__(self):
        return self.uuid

    @property
    def uuid(self):
        return self.name

    def delete(self):
        self.manager.delete(self)


class SecurityGroupRuleManager(base.ManagerWithFind):
    resource_class = SecurityGroupRule

    def create(self, parent_group_id, ip_protocol=None, from_port=None, to_port=None, cidr=None, group_id=None):
    	"""
        Create a security group

        :param parent_group_id: Security group name for the created rule
        """
        body = { "security_group_rule": { 
                            "ip_protocol": ip_protocol,
                            "from_port": from_port,
                            "to_port": to_port,
                            "cidr": cidr,
                            "group_id": group_id,
                            "parent_group_id": parent_group_id }}

        return self._create('/extras/security_group_rules', body, "security_group_rule")

    def delete(self, id):
    	"""
        Delete a security group rule

        :param id: The security group rule ID to delete
        """
        return self._delete('/extras/security_group_rules/%s' % id)

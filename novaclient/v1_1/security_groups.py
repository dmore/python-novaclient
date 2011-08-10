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
Security group interface (1.1 extension).
"""

from novaclient import base


class SecurityGroup(base.Resource):

    def __repr__(self):
        return "<Security_group: %s>" % self.uuid

    def __str__(self):
        return self.uuid

    @property
    def uuid(self):
        return self.name

    def delete(self):
        self.manager.delete(self)


class SecurityGroupManager(base.ManagerWithFind):
    resource_class = SecurityGroup

    def create(self, name, description):
    	"""
        Create a security group

        :param name: name for the security group to create
        :param description: description of the security group
        """
        body = {"security_group": {"name": name, 'description': description}}
        return self._create('/extras/security_groups', body, 'security_group')

    def delete(self, id):
    	"""
        Delete a security group

        :param id: The security group ID to delete
        """
        return self._delete('/extras/security_groups/%s' % id)

    def get(self, id):
    	"""
        Get a security group

        :param id: The security group ID to get
        :rtype: :class:`SecurityGroup`
    	"""
        return self._get('/extras/security_groups/%s' % id, 'security_group')

    def list(self):
        """
        Get a list of all security_groups

        :rtype: list of :class:`SecurityGroup`
        """
        return self._list("/extras/security_groups", "security_groups")

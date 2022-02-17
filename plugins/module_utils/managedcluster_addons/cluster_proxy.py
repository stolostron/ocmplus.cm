from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from .addon_base import addon_base


# subclass
class cluster_proxy(addon_base):
    def __init__(self, module: AnsibleModule, hub_client, managed_cluster_name, addon_name, wait=False, timeout=60):
        super().__init__(module, hub_client, managed_cluster_name, addon_name, wait, timeout)


    def check_feature(self):
        self.check_multi_cluster_hub_feature(
            self.module,
            self.hub_client,
            self.addon_name
        )

    def enable_addon(self):
        return self.enable_managed_cluster_addon(
            self.module,
            self.hub_client,
            self.managed_cluster_name,
            self.addon_name,
            self.wait,
            self.timeout
        )

    def disable_addon(self):
        return self.disable_managed_cluster_addon(
            self.module,
            self.hub_client,
            self.managed_cluster_name,
            self.addon_name,
            self.wait,
            self.timeout
        )

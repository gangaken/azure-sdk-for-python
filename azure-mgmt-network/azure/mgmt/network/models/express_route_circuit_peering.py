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

from .sub_resource import SubResource


class ExpressRouteCircuitPeering(SubResource):
    """
    Peering in a ExpressRouteCircuit resource

    :param str id: Resource Id
    :param str peering_type: Gets or sets PeeringType. Possible values
     include: 'AzurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'
    :param str state: Gets or sets state of Peering. Possible values include:
     'Disabled', 'Enabled'
    :param int azure_asn: Gets or sets the azure ASN
    :param int peer_asn: Gets or sets the peer ASN
    :param str primary_peer_address_prefix: Gets or sets the primary address
     prefix
    :param str secondary_peer_address_prefix: Gets or sets the secondary
     address prefix
    :param str primary_azure_port: Gets or sets the primary port
    :param str secondary_azure_port: Gets or sets the secondary port
    :param str shared_key: Gets or sets the shared key
    :param int vlan_id: Gets or sets the vlan id
    :param ExpressRouteCircuitPeeringConfig microsoft_peering_config: Gets or
     sets the mircosoft peering config
    :param ExpressRouteCircuitStats stats: Gets or peering stats
    :param str provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :param str name: Gets name of the resource that is unique within a
     resource group. This name can be used to access the resource
    :param str etag: A unique read-only string that changes whenever the
     resource is updated
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'peering_type': {'key': 'properties.peeringType', 'type': 'ExpressRouteCircuitPeeringType'},
        'state': {'key': 'properties.state', 'type': 'ExpressRouteCircuitPeeringState'},
        'azure_asn': {'key': 'properties.azureASN', 'type': 'int'},
        'peer_asn': {'key': 'properties.peerASN', 'type': 'int'},
        'primary_peer_address_prefix': {'key': 'properties.primaryPeerAddressPrefix', 'type': 'str'},
        'secondary_peer_address_prefix': {'key': 'properties.secondaryPeerAddressPrefix', 'type': 'str'},
        'primary_azure_port': {'key': 'properties.primaryAzurePort', 'type': 'str'},
        'secondary_azure_port': {'key': 'properties.secondaryAzurePort', 'type': 'str'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'vlan_id': {'key': 'properties.vlanId', 'type': 'int'},
        'microsoft_peering_config': {'key': 'properties.microsoftPeeringConfig', 'type': 'ExpressRouteCircuitPeeringConfig'},
        'stats': {'key': 'properties.stats', 'type': 'ExpressRouteCircuitStats'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, peering_type=None, state=None, azure_asn=None, peer_asn=None, primary_peer_address_prefix=None, secondary_peer_address_prefix=None, primary_azure_port=None, secondary_azure_port=None, shared_key=None, vlan_id=None, microsoft_peering_config=None, stats=None, provisioning_state=None, name=None, etag=None, **kwargs):
        super(ExpressRouteCircuitPeering, self).__init__(id=id, **kwargs)
        self.peering_type = peering_type
        self.state = state
        self.azure_asn = azure_asn
        self.peer_asn = peer_asn
        self.primary_peer_address_prefix = primary_peer_address_prefix
        self.secondary_peer_address_prefix = secondary_peer_address_prefix
        self.primary_azure_port = primary_azure_port
        self.secondary_azure_port = secondary_azure_port
        self.shared_key = shared_key
        self.vlan_id = vlan_id
        self.microsoft_peering_config = microsoft_peering_config
        self.stats = stats
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
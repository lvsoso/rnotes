/*
Gitea API

This documentation describes the Gitea API.

API version: {{AppVer | JSEscape | Safe}}
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// NodeInfoServices NodeInfoServices contains the third party sites this server can connect to via their application API
type NodeInfoServices struct {
	Inbound *[]string `json:"inbound,omitempty"`
	Outbound *[]string `json:"outbound,omitempty"`
}

// NewNodeInfoServices instantiates a new NodeInfoServices object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewNodeInfoServices() *NodeInfoServices {
	this := NodeInfoServices{}
	return &this
}

// NewNodeInfoServicesWithDefaults instantiates a new NodeInfoServices object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewNodeInfoServicesWithDefaults() *NodeInfoServices {
	this := NodeInfoServices{}
	return &this
}

// GetInbound returns the Inbound field value if set, zero value otherwise.
func (o *NodeInfoServices) GetInbound() []string {
	if o == nil || o.Inbound == nil {
		var ret []string
		return ret
	}
	return *o.Inbound
}

// GetInboundOk returns a tuple with the Inbound field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NodeInfoServices) GetInboundOk() (*[]string, bool) {
	if o == nil || o.Inbound == nil {
		return nil, false
	}
	return o.Inbound, true
}

// HasInbound returns a boolean if a field has been set.
func (o *NodeInfoServices) HasInbound() bool {
	if o != nil && o.Inbound != nil {
		return true
	}

	return false
}

// SetInbound gets a reference to the given []string and assigns it to the Inbound field.
func (o *NodeInfoServices) SetInbound(v []string) {
	o.Inbound = &v
}

// GetOutbound returns the Outbound field value if set, zero value otherwise.
func (o *NodeInfoServices) GetOutbound() []string {
	if o == nil || o.Outbound == nil {
		var ret []string
		return ret
	}
	return *o.Outbound
}

// GetOutboundOk returns a tuple with the Outbound field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NodeInfoServices) GetOutboundOk() (*[]string, bool) {
	if o == nil || o.Outbound == nil {
		return nil, false
	}
	return o.Outbound, true
}

// HasOutbound returns a boolean if a field has been set.
func (o *NodeInfoServices) HasOutbound() bool {
	if o != nil && o.Outbound != nil {
		return true
	}

	return false
}

// SetOutbound gets a reference to the given []string and assigns it to the Outbound field.
func (o *NodeInfoServices) SetOutbound(v []string) {
	o.Outbound = &v
}

func (o NodeInfoServices) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Inbound != nil {
		toSerialize["inbound"] = o.Inbound
	}
	if o.Outbound != nil {
		toSerialize["outbound"] = o.Outbound
	}
	return json.Marshal(toSerialize)
}

type NullableNodeInfoServices struct {
	value *NodeInfoServices
	isSet bool
}

func (v NullableNodeInfoServices) Get() *NodeInfoServices {
	return v.value
}

func (v *NullableNodeInfoServices) Set(val *NodeInfoServices) {
	v.value = val
	v.isSet = true
}

func (v NullableNodeInfoServices) IsSet() bool {
	return v.isSet
}

func (v *NullableNodeInfoServices) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableNodeInfoServices(val *NodeInfoServices) *NullableNodeInfoServices {
	return &NullableNodeInfoServices{value: val, isSet: true}
}

func (v NullableNodeInfoServices) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableNodeInfoServices) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



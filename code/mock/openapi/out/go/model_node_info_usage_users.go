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

// NodeInfoUsageUsers NodeInfoUsageUsers contains statistics about the users of this server
type NodeInfoUsageUsers struct {
	ActiveHalfyear *int64 `json:"activeHalfyear,omitempty"`
	ActiveMonth *int64 `json:"activeMonth,omitempty"`
	Total *int64 `json:"total,omitempty"`
}

// NewNodeInfoUsageUsers instantiates a new NodeInfoUsageUsers object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewNodeInfoUsageUsers() *NodeInfoUsageUsers {
	this := NodeInfoUsageUsers{}
	return &this
}

// NewNodeInfoUsageUsersWithDefaults instantiates a new NodeInfoUsageUsers object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewNodeInfoUsageUsersWithDefaults() *NodeInfoUsageUsers {
	this := NodeInfoUsageUsers{}
	return &this
}

// GetActiveHalfyear returns the ActiveHalfyear field value if set, zero value otherwise.
func (o *NodeInfoUsageUsers) GetActiveHalfyear() int64 {
	if o == nil || o.ActiveHalfyear == nil {
		var ret int64
		return ret
	}
	return *o.ActiveHalfyear
}

// GetActiveHalfyearOk returns a tuple with the ActiveHalfyear field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NodeInfoUsageUsers) GetActiveHalfyearOk() (*int64, bool) {
	if o == nil || o.ActiveHalfyear == nil {
		return nil, false
	}
	return o.ActiveHalfyear, true
}

// HasActiveHalfyear returns a boolean if a field has been set.
func (o *NodeInfoUsageUsers) HasActiveHalfyear() bool {
	if o != nil && o.ActiveHalfyear != nil {
		return true
	}

	return false
}

// SetActiveHalfyear gets a reference to the given int64 and assigns it to the ActiveHalfyear field.
func (o *NodeInfoUsageUsers) SetActiveHalfyear(v int64) {
	o.ActiveHalfyear = &v
}

// GetActiveMonth returns the ActiveMonth field value if set, zero value otherwise.
func (o *NodeInfoUsageUsers) GetActiveMonth() int64 {
	if o == nil || o.ActiveMonth == nil {
		var ret int64
		return ret
	}
	return *o.ActiveMonth
}

// GetActiveMonthOk returns a tuple with the ActiveMonth field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NodeInfoUsageUsers) GetActiveMonthOk() (*int64, bool) {
	if o == nil || o.ActiveMonth == nil {
		return nil, false
	}
	return o.ActiveMonth, true
}

// HasActiveMonth returns a boolean if a field has been set.
func (o *NodeInfoUsageUsers) HasActiveMonth() bool {
	if o != nil && o.ActiveMonth != nil {
		return true
	}

	return false
}

// SetActiveMonth gets a reference to the given int64 and assigns it to the ActiveMonth field.
func (o *NodeInfoUsageUsers) SetActiveMonth(v int64) {
	o.ActiveMonth = &v
}

// GetTotal returns the Total field value if set, zero value otherwise.
func (o *NodeInfoUsageUsers) GetTotal() int64 {
	if o == nil || o.Total == nil {
		var ret int64
		return ret
	}
	return *o.Total
}

// GetTotalOk returns a tuple with the Total field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NodeInfoUsageUsers) GetTotalOk() (*int64, bool) {
	if o == nil || o.Total == nil {
		return nil, false
	}
	return o.Total, true
}

// HasTotal returns a boolean if a field has been set.
func (o *NodeInfoUsageUsers) HasTotal() bool {
	if o != nil && o.Total != nil {
		return true
	}

	return false
}

// SetTotal gets a reference to the given int64 and assigns it to the Total field.
func (o *NodeInfoUsageUsers) SetTotal(v int64) {
	o.Total = &v
}

func (o NodeInfoUsageUsers) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.ActiveHalfyear != nil {
		toSerialize["activeHalfyear"] = o.ActiveHalfyear
	}
	if o.ActiveMonth != nil {
		toSerialize["activeMonth"] = o.ActiveMonth
	}
	if o.Total != nil {
		toSerialize["total"] = o.Total
	}
	return json.Marshal(toSerialize)
}

type NullableNodeInfoUsageUsers struct {
	value *NodeInfoUsageUsers
	isSet bool
}

func (v NullableNodeInfoUsageUsers) Get() *NodeInfoUsageUsers {
	return v.value
}

func (v *NullableNodeInfoUsageUsers) Set(val *NodeInfoUsageUsers) {
	v.value = val
	v.isSet = true
}

func (v NullableNodeInfoUsageUsers) IsSet() bool {
	return v.isSet
}

func (v *NullableNodeInfoUsageUsers) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableNodeInfoUsageUsers(val *NodeInfoUsageUsers) *NullableNodeInfoUsageUsers {
	return &NullableNodeInfoUsageUsers{value: val, isSet: true}
}

func (v NullableNodeInfoUsageUsers) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableNodeInfoUsageUsers) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



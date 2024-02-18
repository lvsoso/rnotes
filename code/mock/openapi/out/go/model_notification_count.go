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

// NotificationCount NotificationCount number of unread notifications
type NotificationCount struct {
	New *int64 `json:"new,omitempty"`
}

// NewNotificationCount instantiates a new NotificationCount object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewNotificationCount() *NotificationCount {
	this := NotificationCount{}
	return &this
}

// NewNotificationCountWithDefaults instantiates a new NotificationCount object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewNotificationCountWithDefaults() *NotificationCount {
	this := NotificationCount{}
	return &this
}

// GetNew returns the New field value if set, zero value otherwise.
func (o *NotificationCount) GetNew() int64 {
	if o == nil || o.New == nil {
		var ret int64
		return ret
	}
	return *o.New
}

// GetNewOk returns a tuple with the New field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationCount) GetNewOk() (*int64, bool) {
	if o == nil || o.New == nil {
		return nil, false
	}
	return o.New, true
}

// HasNew returns a boolean if a field has been set.
func (o *NotificationCount) HasNew() bool {
	if o != nil && o.New != nil {
		return true
	}

	return false
}

// SetNew gets a reference to the given int64 and assigns it to the New field.
func (o *NotificationCount) SetNew(v int64) {
	o.New = &v
}

func (o NotificationCount) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.New != nil {
		toSerialize["new"] = o.New
	}
	return json.Marshal(toSerialize)
}

type NullableNotificationCount struct {
	value *NotificationCount
	isSet bool
}

func (v NullableNotificationCount) Get() *NotificationCount {
	return v.value
}

func (v *NullableNotificationCount) Set(val *NotificationCount) {
	v.value = val
	v.isSet = true
}

func (v NullableNotificationCount) IsSet() bool {
	return v.isSet
}

func (v *NullableNotificationCount) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableNotificationCount(val *NotificationCount) *NullableNotificationCount {
	return &NullableNotificationCount{value: val, isSet: true}
}

func (v NullableNotificationCount) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableNotificationCount) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



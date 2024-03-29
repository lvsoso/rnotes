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

// ServerVersion ServerVersion wraps the version of the server
type ServerVersion struct {
	Version *string `json:"version,omitempty"`
}

// NewServerVersion instantiates a new ServerVersion object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewServerVersion() *ServerVersion {
	this := ServerVersion{}
	return &this
}

// NewServerVersionWithDefaults instantiates a new ServerVersion object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewServerVersionWithDefaults() *ServerVersion {
	this := ServerVersion{}
	return &this
}

// GetVersion returns the Version field value if set, zero value otherwise.
func (o *ServerVersion) GetVersion() string {
	if o == nil || o.Version == nil {
		var ret string
		return ret
	}
	return *o.Version
}

// GetVersionOk returns a tuple with the Version field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServerVersion) GetVersionOk() (*string, bool) {
	if o == nil || o.Version == nil {
		return nil, false
	}
	return o.Version, true
}

// HasVersion returns a boolean if a field has been set.
func (o *ServerVersion) HasVersion() bool {
	if o != nil && o.Version != nil {
		return true
	}

	return false
}

// SetVersion gets a reference to the given string and assigns it to the Version field.
func (o *ServerVersion) SetVersion(v string) {
	o.Version = &v
}

func (o ServerVersion) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Version != nil {
		toSerialize["version"] = o.Version
	}
	return json.Marshal(toSerialize)
}

type NullableServerVersion struct {
	value *ServerVersion
	isSet bool
}

func (v NullableServerVersion) Get() *ServerVersion {
	return v.value
}

func (v *NullableServerVersion) Set(val *ServerVersion) {
	v.value = val
	v.isSet = true
}

func (v NullableServerVersion) IsSet() bool {
	return v.isSet
}

func (v *NullableServerVersion) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableServerVersion(val *ServerVersion) *NullableServerVersion {
	return &NullableServerVersion{value: val, isSet: true}
}

func (v NullableServerVersion) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableServerVersion) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



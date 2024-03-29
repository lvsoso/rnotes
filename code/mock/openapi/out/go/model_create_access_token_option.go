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

// CreateAccessTokenOption CreateAccessTokenOption options when create access token
type CreateAccessTokenOption struct {
	Name string `json:"name"`
	Scopes *[]string `json:"scopes,omitempty"`
}

// NewCreateAccessTokenOption instantiates a new CreateAccessTokenOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateAccessTokenOption(name string) *CreateAccessTokenOption {
	this := CreateAccessTokenOption{}
	this.Name = name
	return &this
}

// NewCreateAccessTokenOptionWithDefaults instantiates a new CreateAccessTokenOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateAccessTokenOptionWithDefaults() *CreateAccessTokenOption {
	this := CreateAccessTokenOption{}
	return &this
}

// GetName returns the Name field value
func (o *CreateAccessTokenOption) GetName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Name
}

// GetNameOk returns a tuple with the Name field value
// and a boolean to check if the value has been set.
func (o *CreateAccessTokenOption) GetNameOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Name, true
}

// SetName sets field value
func (o *CreateAccessTokenOption) SetName(v string) {
	o.Name = v
}

// GetScopes returns the Scopes field value if set, zero value otherwise.
func (o *CreateAccessTokenOption) GetScopes() []string {
	if o == nil || o.Scopes == nil {
		var ret []string
		return ret
	}
	return *o.Scopes
}

// GetScopesOk returns a tuple with the Scopes field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateAccessTokenOption) GetScopesOk() (*[]string, bool) {
	if o == nil || o.Scopes == nil {
		return nil, false
	}
	return o.Scopes, true
}

// HasScopes returns a boolean if a field has been set.
func (o *CreateAccessTokenOption) HasScopes() bool {
	if o != nil && o.Scopes != nil {
		return true
	}

	return false
}

// SetScopes gets a reference to the given []string and assigns it to the Scopes field.
func (o *CreateAccessTokenOption) SetScopes(v []string) {
	o.Scopes = &v
}

func (o CreateAccessTokenOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["name"] = o.Name
	}
	if o.Scopes != nil {
		toSerialize["scopes"] = o.Scopes
	}
	return json.Marshal(toSerialize)
}

type NullableCreateAccessTokenOption struct {
	value *CreateAccessTokenOption
	isSet bool
}

func (v NullableCreateAccessTokenOption) Get() *CreateAccessTokenOption {
	return v.value
}

func (v *NullableCreateAccessTokenOption) Set(val *CreateAccessTokenOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateAccessTokenOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateAccessTokenOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateAccessTokenOption(val *CreateAccessTokenOption) *NullableCreateAccessTokenOption {
	return &NullableCreateAccessTokenOption{value: val, isSet: true}
}

func (v NullableCreateAccessTokenOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateAccessTokenOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



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

// CreateForkOption CreateForkOption options for creating a fork
type CreateForkOption struct {
	// name of the forked repository
	Name *string `json:"name,omitempty"`
	// organization name, if forking into an organization
	Organization *string `json:"organization,omitempty"`
}

// NewCreateForkOption instantiates a new CreateForkOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateForkOption() *CreateForkOption {
	this := CreateForkOption{}
	return &this
}

// NewCreateForkOptionWithDefaults instantiates a new CreateForkOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateForkOptionWithDefaults() *CreateForkOption {
	this := CreateForkOption{}
	return &this
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *CreateForkOption) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateForkOption) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *CreateForkOption) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *CreateForkOption) SetName(v string) {
	o.Name = &v
}

// GetOrganization returns the Organization field value if set, zero value otherwise.
func (o *CreateForkOption) GetOrganization() string {
	if o == nil || o.Organization == nil {
		var ret string
		return ret
	}
	return *o.Organization
}

// GetOrganizationOk returns a tuple with the Organization field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateForkOption) GetOrganizationOk() (*string, bool) {
	if o == nil || o.Organization == nil {
		return nil, false
	}
	return o.Organization, true
}

// HasOrganization returns a boolean if a field has been set.
func (o *CreateForkOption) HasOrganization() bool {
	if o != nil && o.Organization != nil {
		return true
	}

	return false
}

// SetOrganization gets a reference to the given string and assigns it to the Organization field.
func (o *CreateForkOption) SetOrganization(v string) {
	o.Organization = &v
}

func (o CreateForkOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.Organization != nil {
		toSerialize["organization"] = o.Organization
	}
	return json.Marshal(toSerialize)
}

type NullableCreateForkOption struct {
	value *CreateForkOption
	isSet bool
}

func (v NullableCreateForkOption) Get() *CreateForkOption {
	return v.value
}

func (v *NullableCreateForkOption) Set(val *CreateForkOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateForkOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateForkOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateForkOption(val *CreateForkOption) *NullableCreateForkOption {
	return &NullableCreateForkOption{value: val, isSet: true}
}

func (v NullableCreateForkOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateForkOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



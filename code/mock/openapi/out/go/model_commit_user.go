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

// CommitUser struct for CommitUser
type CommitUser struct {
	Date *string `json:"date,omitempty"`
	Email *string `json:"email,omitempty"`
	Name *string `json:"name,omitempty"`
}

// NewCommitUser instantiates a new CommitUser object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCommitUser() *CommitUser {
	this := CommitUser{}
	return &this
}

// NewCommitUserWithDefaults instantiates a new CommitUser object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCommitUserWithDefaults() *CommitUser {
	this := CommitUser{}
	return &this
}

// GetDate returns the Date field value if set, zero value otherwise.
func (o *CommitUser) GetDate() string {
	if o == nil || o.Date == nil {
		var ret string
		return ret
	}
	return *o.Date
}

// GetDateOk returns a tuple with the Date field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CommitUser) GetDateOk() (*string, bool) {
	if o == nil || o.Date == nil {
		return nil, false
	}
	return o.Date, true
}

// HasDate returns a boolean if a field has been set.
func (o *CommitUser) HasDate() bool {
	if o != nil && o.Date != nil {
		return true
	}

	return false
}

// SetDate gets a reference to the given string and assigns it to the Date field.
func (o *CommitUser) SetDate(v string) {
	o.Date = &v
}

// GetEmail returns the Email field value if set, zero value otherwise.
func (o *CommitUser) GetEmail() string {
	if o == nil || o.Email == nil {
		var ret string
		return ret
	}
	return *o.Email
}

// GetEmailOk returns a tuple with the Email field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CommitUser) GetEmailOk() (*string, bool) {
	if o == nil || o.Email == nil {
		return nil, false
	}
	return o.Email, true
}

// HasEmail returns a boolean if a field has been set.
func (o *CommitUser) HasEmail() bool {
	if o != nil && o.Email != nil {
		return true
	}

	return false
}

// SetEmail gets a reference to the given string and assigns it to the Email field.
func (o *CommitUser) SetEmail(v string) {
	o.Email = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *CommitUser) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CommitUser) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *CommitUser) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *CommitUser) SetName(v string) {
	o.Name = &v
}

func (o CommitUser) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Date != nil {
		toSerialize["date"] = o.Date
	}
	if o.Email != nil {
		toSerialize["email"] = o.Email
	}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	return json.Marshal(toSerialize)
}

type NullableCommitUser struct {
	value *CommitUser
	isSet bool
}

func (v NullableCommitUser) Get() *CommitUser {
	return v.value
}

func (v *NullableCommitUser) Set(val *CommitUser) {
	v.value = val
	v.isSet = true
}

func (v NullableCommitUser) IsSet() bool {
	return v.isSet
}

func (v *NullableCommitUser) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCommitUser(val *CommitUser) *NullableCommitUser {
	return &NullableCommitUser{value: val, isSet: true}
}

func (v NullableCommitUser) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCommitUser) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



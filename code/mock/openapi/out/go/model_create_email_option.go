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

// CreateEmailOption CreateEmailOption options when creating email addresses
type CreateEmailOption struct {
	// email addresses to add
	Emails *[]string `json:"emails,omitempty"`
}

// NewCreateEmailOption instantiates a new CreateEmailOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateEmailOption() *CreateEmailOption {
	this := CreateEmailOption{}
	return &this
}

// NewCreateEmailOptionWithDefaults instantiates a new CreateEmailOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateEmailOptionWithDefaults() *CreateEmailOption {
	this := CreateEmailOption{}
	return &this
}

// GetEmails returns the Emails field value if set, zero value otherwise.
func (o *CreateEmailOption) GetEmails() []string {
	if o == nil || o.Emails == nil {
		var ret []string
		return ret
	}
	return *o.Emails
}

// GetEmailsOk returns a tuple with the Emails field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateEmailOption) GetEmailsOk() (*[]string, bool) {
	if o == nil || o.Emails == nil {
		return nil, false
	}
	return o.Emails, true
}

// HasEmails returns a boolean if a field has been set.
func (o *CreateEmailOption) HasEmails() bool {
	if o != nil && o.Emails != nil {
		return true
	}

	return false
}

// SetEmails gets a reference to the given []string and assigns it to the Emails field.
func (o *CreateEmailOption) SetEmails(v []string) {
	o.Emails = &v
}

func (o CreateEmailOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Emails != nil {
		toSerialize["emails"] = o.Emails
	}
	return json.Marshal(toSerialize)
}

type NullableCreateEmailOption struct {
	value *CreateEmailOption
	isSet bool
}

func (v NullableCreateEmailOption) Get() *CreateEmailOption {
	return v.value
}

func (v *NullableCreateEmailOption) Set(val *CreateEmailOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateEmailOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateEmailOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateEmailOption(val *CreateEmailOption) *NullableCreateEmailOption {
	return &NullableCreateEmailOption{value: val, isSet: true}
}

func (v NullableCreateEmailOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateEmailOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



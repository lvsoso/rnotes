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

// CreateTagOption CreateTagOption options when creating a tag
type CreateTagOption struct {
	Message *string `json:"message,omitempty"`
	TagName string `json:"tag_name"`
	Target *string `json:"target,omitempty"`
}

// NewCreateTagOption instantiates a new CreateTagOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateTagOption(tagName string) *CreateTagOption {
	this := CreateTagOption{}
	this.TagName = tagName
	return &this
}

// NewCreateTagOptionWithDefaults instantiates a new CreateTagOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateTagOptionWithDefaults() *CreateTagOption {
	this := CreateTagOption{}
	return &this
}

// GetMessage returns the Message field value if set, zero value otherwise.
func (o *CreateTagOption) GetMessage() string {
	if o == nil || o.Message == nil {
		var ret string
		return ret
	}
	return *o.Message
}

// GetMessageOk returns a tuple with the Message field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateTagOption) GetMessageOk() (*string, bool) {
	if o == nil || o.Message == nil {
		return nil, false
	}
	return o.Message, true
}

// HasMessage returns a boolean if a field has been set.
func (o *CreateTagOption) HasMessage() bool {
	if o != nil && o.Message != nil {
		return true
	}

	return false
}

// SetMessage gets a reference to the given string and assigns it to the Message field.
func (o *CreateTagOption) SetMessage(v string) {
	o.Message = &v
}

// GetTagName returns the TagName field value
func (o *CreateTagOption) GetTagName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.TagName
}

// GetTagNameOk returns a tuple with the TagName field value
// and a boolean to check if the value has been set.
func (o *CreateTagOption) GetTagNameOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.TagName, true
}

// SetTagName sets field value
func (o *CreateTagOption) SetTagName(v string) {
	o.TagName = v
}

// GetTarget returns the Target field value if set, zero value otherwise.
func (o *CreateTagOption) GetTarget() string {
	if o == nil || o.Target == nil {
		var ret string
		return ret
	}
	return *o.Target
}

// GetTargetOk returns a tuple with the Target field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateTagOption) GetTargetOk() (*string, bool) {
	if o == nil || o.Target == nil {
		return nil, false
	}
	return o.Target, true
}

// HasTarget returns a boolean if a field has been set.
func (o *CreateTagOption) HasTarget() bool {
	if o != nil && o.Target != nil {
		return true
	}

	return false
}

// SetTarget gets a reference to the given string and assigns it to the Target field.
func (o *CreateTagOption) SetTarget(v string) {
	o.Target = &v
}

func (o CreateTagOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Message != nil {
		toSerialize["message"] = o.Message
	}
	if true {
		toSerialize["tag_name"] = o.TagName
	}
	if o.Target != nil {
		toSerialize["target"] = o.Target
	}
	return json.Marshal(toSerialize)
}

type NullableCreateTagOption struct {
	value *CreateTagOption
	isSet bool
}

func (v NullableCreateTagOption) Get() *CreateTagOption {
	return v.value
}

func (v *NullableCreateTagOption) Set(val *CreateTagOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateTagOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateTagOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateTagOption(val *CreateTagOption) *NullableCreateTagOption {
	return &NullableCreateTagOption{value: val, isSet: true}
}

func (v NullableCreateTagOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateTagOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


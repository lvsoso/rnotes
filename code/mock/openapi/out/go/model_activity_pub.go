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

// ActivityPub ActivityPub type
type ActivityPub struct {
	Context *string `json:"@context,omitempty"`
}

// NewActivityPub instantiates a new ActivityPub object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewActivityPub() *ActivityPub {
	this := ActivityPub{}
	return &this
}

// NewActivityPubWithDefaults instantiates a new ActivityPub object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewActivityPubWithDefaults() *ActivityPub {
	this := ActivityPub{}
	return &this
}

// GetContext returns the Context field value if set, zero value otherwise.
func (o *ActivityPub) GetContext() string {
	if o == nil || o.Context == nil {
		var ret string
		return ret
	}
	return *o.Context
}

// GetContextOk returns a tuple with the Context field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ActivityPub) GetContextOk() (*string, bool) {
	if o == nil || o.Context == nil {
		return nil, false
	}
	return o.Context, true
}

// HasContext returns a boolean if a field has been set.
func (o *ActivityPub) HasContext() bool {
	if o != nil && o.Context != nil {
		return true
	}

	return false
}

// SetContext gets a reference to the given string and assigns it to the Context field.
func (o *ActivityPub) SetContext(v string) {
	o.Context = &v
}

func (o ActivityPub) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Context != nil {
		toSerialize["@context"] = o.Context
	}
	return json.Marshal(toSerialize)
}

type NullableActivityPub struct {
	value *ActivityPub
	isSet bool
}

func (v NullableActivityPub) Get() *ActivityPub {
	return v.value
}

func (v *NullableActivityPub) Set(val *ActivityPub) {
	v.value = val
	v.isSet = true
}

func (v NullableActivityPub) IsSet() bool {
	return v.isSet
}

func (v *NullableActivityPub) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableActivityPub(val *ActivityPub) *NullableActivityPub {
	return &NullableActivityPub{value: val, isSet: true}
}

func (v NullableActivityPub) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableActivityPub) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



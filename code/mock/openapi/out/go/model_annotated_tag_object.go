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

// AnnotatedTagObject AnnotatedTagObject contains meta information of the tag object
type AnnotatedTagObject struct {
	Sha *string `json:"sha,omitempty"`
	Type *string `json:"type,omitempty"`
	Url *string `json:"url,omitempty"`
}

// NewAnnotatedTagObject instantiates a new AnnotatedTagObject object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewAnnotatedTagObject() *AnnotatedTagObject {
	this := AnnotatedTagObject{}
	return &this
}

// NewAnnotatedTagObjectWithDefaults instantiates a new AnnotatedTagObject object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewAnnotatedTagObjectWithDefaults() *AnnotatedTagObject {
	this := AnnotatedTagObject{}
	return &this
}

// GetSha returns the Sha field value if set, zero value otherwise.
func (o *AnnotatedTagObject) GetSha() string {
	if o == nil || o.Sha == nil {
		var ret string
		return ret
	}
	return *o.Sha
}

// GetShaOk returns a tuple with the Sha field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *AnnotatedTagObject) GetShaOk() (*string, bool) {
	if o == nil || o.Sha == nil {
		return nil, false
	}
	return o.Sha, true
}

// HasSha returns a boolean if a field has been set.
func (o *AnnotatedTagObject) HasSha() bool {
	if o != nil && o.Sha != nil {
		return true
	}

	return false
}

// SetSha gets a reference to the given string and assigns it to the Sha field.
func (o *AnnotatedTagObject) SetSha(v string) {
	o.Sha = &v
}

// GetType returns the Type field value if set, zero value otherwise.
func (o *AnnotatedTagObject) GetType() string {
	if o == nil || o.Type == nil {
		var ret string
		return ret
	}
	return *o.Type
}

// GetTypeOk returns a tuple with the Type field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *AnnotatedTagObject) GetTypeOk() (*string, bool) {
	if o == nil || o.Type == nil {
		return nil, false
	}
	return o.Type, true
}

// HasType returns a boolean if a field has been set.
func (o *AnnotatedTagObject) HasType() bool {
	if o != nil && o.Type != nil {
		return true
	}

	return false
}

// SetType gets a reference to the given string and assigns it to the Type field.
func (o *AnnotatedTagObject) SetType(v string) {
	o.Type = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *AnnotatedTagObject) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *AnnotatedTagObject) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *AnnotatedTagObject) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *AnnotatedTagObject) SetUrl(v string) {
	o.Url = &v
}

func (o AnnotatedTagObject) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Sha != nil {
		toSerialize["sha"] = o.Sha
	}
	if o.Type != nil {
		toSerialize["type"] = o.Type
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	return json.Marshal(toSerialize)
}

type NullableAnnotatedTagObject struct {
	value *AnnotatedTagObject
	isSet bool
}

func (v NullableAnnotatedTagObject) Get() *AnnotatedTagObject {
	return v.value
}

func (v *NullableAnnotatedTagObject) Set(val *AnnotatedTagObject) {
	v.value = val
	v.isSet = true
}

func (v NullableAnnotatedTagObject) IsSet() bool {
	return v.isSet
}

func (v *NullableAnnotatedTagObject) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableAnnotatedTagObject(val *AnnotatedTagObject) *NullableAnnotatedTagObject {
	return &NullableAnnotatedTagObject{value: val, isSet: true}
}

func (v NullableAnnotatedTagObject) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableAnnotatedTagObject) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



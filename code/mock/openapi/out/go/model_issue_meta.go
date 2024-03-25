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

// IssueMeta IssueMeta basic issue information
type IssueMeta struct {
	Index *int64 `json:"index,omitempty"`
	Owner *string `json:"owner,omitempty"`
	Repo *string `json:"repo,omitempty"`
}

// NewIssueMeta instantiates a new IssueMeta object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewIssueMeta() *IssueMeta {
	this := IssueMeta{}
	return &this
}

// NewIssueMetaWithDefaults instantiates a new IssueMeta object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewIssueMetaWithDefaults() *IssueMeta {
	this := IssueMeta{}
	return &this
}

// GetIndex returns the Index field value if set, zero value otherwise.
func (o *IssueMeta) GetIndex() int64 {
	if o == nil || o.Index == nil {
		var ret int64
		return ret
	}
	return *o.Index
}

// GetIndexOk returns a tuple with the Index field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *IssueMeta) GetIndexOk() (*int64, bool) {
	if o == nil || o.Index == nil {
		return nil, false
	}
	return o.Index, true
}

// HasIndex returns a boolean if a field has been set.
func (o *IssueMeta) HasIndex() bool {
	if o != nil && o.Index != nil {
		return true
	}

	return false
}

// SetIndex gets a reference to the given int64 and assigns it to the Index field.
func (o *IssueMeta) SetIndex(v int64) {
	o.Index = &v
}

// GetOwner returns the Owner field value if set, zero value otherwise.
func (o *IssueMeta) GetOwner() string {
	if o == nil || o.Owner == nil {
		var ret string
		return ret
	}
	return *o.Owner
}

// GetOwnerOk returns a tuple with the Owner field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *IssueMeta) GetOwnerOk() (*string, bool) {
	if o == nil || o.Owner == nil {
		return nil, false
	}
	return o.Owner, true
}

// HasOwner returns a boolean if a field has been set.
func (o *IssueMeta) HasOwner() bool {
	if o != nil && o.Owner != nil {
		return true
	}

	return false
}

// SetOwner gets a reference to the given string and assigns it to the Owner field.
func (o *IssueMeta) SetOwner(v string) {
	o.Owner = &v
}

// GetRepo returns the Repo field value if set, zero value otherwise.
func (o *IssueMeta) GetRepo() string {
	if o == nil || o.Repo == nil {
		var ret string
		return ret
	}
	return *o.Repo
}

// GetRepoOk returns a tuple with the Repo field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *IssueMeta) GetRepoOk() (*string, bool) {
	if o == nil || o.Repo == nil {
		return nil, false
	}
	return o.Repo, true
}

// HasRepo returns a boolean if a field has been set.
func (o *IssueMeta) HasRepo() bool {
	if o != nil && o.Repo != nil {
		return true
	}

	return false
}

// SetRepo gets a reference to the given string and assigns it to the Repo field.
func (o *IssueMeta) SetRepo(v string) {
	o.Repo = &v
}

func (o IssueMeta) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Index != nil {
		toSerialize["index"] = o.Index
	}
	if o.Owner != nil {
		toSerialize["owner"] = o.Owner
	}
	if o.Repo != nil {
		toSerialize["repo"] = o.Repo
	}
	return json.Marshal(toSerialize)
}

type NullableIssueMeta struct {
	value *IssueMeta
	isSet bool
}

func (v NullableIssueMeta) Get() *IssueMeta {
	return v.value
}

func (v *NullableIssueMeta) Set(val *IssueMeta) {
	v.value = val
	v.isSet = true
}

func (v NullableIssueMeta) IsSet() bool {
	return v.isSet
}

func (v *NullableIssueMeta) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableIssueMeta(val *IssueMeta) *NullableIssueMeta {
	return &NullableIssueMeta{value: val, isSet: true}
}

func (v NullableIssueMeta) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableIssueMeta) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


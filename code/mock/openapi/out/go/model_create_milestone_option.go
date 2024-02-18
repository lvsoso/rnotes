/*
Gitea API

This documentation describes the Gitea API.

API version: {{AppVer | JSEscape | Safe}}
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
	"time"
)

// CreateMilestoneOption CreateMilestoneOption options for creating a milestone
type CreateMilestoneOption struct {
	Description *string `json:"description,omitempty"`
	DueOn *time.Time `json:"due_on,omitempty"`
	State *string `json:"state,omitempty"`
	Title *string `json:"title,omitempty"`
}

// NewCreateMilestoneOption instantiates a new CreateMilestoneOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateMilestoneOption() *CreateMilestoneOption {
	this := CreateMilestoneOption{}
	return &this
}

// NewCreateMilestoneOptionWithDefaults instantiates a new CreateMilestoneOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateMilestoneOptionWithDefaults() *CreateMilestoneOption {
	this := CreateMilestoneOption{}
	return &this
}

// GetDescription returns the Description field value if set, zero value otherwise.
func (o *CreateMilestoneOption) GetDescription() string {
	if o == nil || o.Description == nil {
		var ret string
		return ret
	}
	return *o.Description
}

// GetDescriptionOk returns a tuple with the Description field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateMilestoneOption) GetDescriptionOk() (*string, bool) {
	if o == nil || o.Description == nil {
		return nil, false
	}
	return o.Description, true
}

// HasDescription returns a boolean if a field has been set.
func (o *CreateMilestoneOption) HasDescription() bool {
	if o != nil && o.Description != nil {
		return true
	}

	return false
}

// SetDescription gets a reference to the given string and assigns it to the Description field.
func (o *CreateMilestoneOption) SetDescription(v string) {
	o.Description = &v
}

// GetDueOn returns the DueOn field value if set, zero value otherwise.
func (o *CreateMilestoneOption) GetDueOn() time.Time {
	if o == nil || o.DueOn == nil {
		var ret time.Time
		return ret
	}
	return *o.DueOn
}

// GetDueOnOk returns a tuple with the DueOn field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateMilestoneOption) GetDueOnOk() (*time.Time, bool) {
	if o == nil || o.DueOn == nil {
		return nil, false
	}
	return o.DueOn, true
}

// HasDueOn returns a boolean if a field has been set.
func (o *CreateMilestoneOption) HasDueOn() bool {
	if o != nil && o.DueOn != nil {
		return true
	}

	return false
}

// SetDueOn gets a reference to the given time.Time and assigns it to the DueOn field.
func (o *CreateMilestoneOption) SetDueOn(v time.Time) {
	o.DueOn = &v
}

// GetState returns the State field value if set, zero value otherwise.
func (o *CreateMilestoneOption) GetState() string {
	if o == nil || o.State == nil {
		var ret string
		return ret
	}
	return *o.State
}

// GetStateOk returns a tuple with the State field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateMilestoneOption) GetStateOk() (*string, bool) {
	if o == nil || o.State == nil {
		return nil, false
	}
	return o.State, true
}

// HasState returns a boolean if a field has been set.
func (o *CreateMilestoneOption) HasState() bool {
	if o != nil && o.State != nil {
		return true
	}

	return false
}

// SetState gets a reference to the given string and assigns it to the State field.
func (o *CreateMilestoneOption) SetState(v string) {
	o.State = &v
}

// GetTitle returns the Title field value if set, zero value otherwise.
func (o *CreateMilestoneOption) GetTitle() string {
	if o == nil || o.Title == nil {
		var ret string
		return ret
	}
	return *o.Title
}

// GetTitleOk returns a tuple with the Title field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateMilestoneOption) GetTitleOk() (*string, bool) {
	if o == nil || o.Title == nil {
		return nil, false
	}
	return o.Title, true
}

// HasTitle returns a boolean if a field has been set.
func (o *CreateMilestoneOption) HasTitle() bool {
	if o != nil && o.Title != nil {
		return true
	}

	return false
}

// SetTitle gets a reference to the given string and assigns it to the Title field.
func (o *CreateMilestoneOption) SetTitle(v string) {
	o.Title = &v
}

func (o CreateMilestoneOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Description != nil {
		toSerialize["description"] = o.Description
	}
	if o.DueOn != nil {
		toSerialize["due_on"] = o.DueOn
	}
	if o.State != nil {
		toSerialize["state"] = o.State
	}
	if o.Title != nil {
		toSerialize["title"] = o.Title
	}
	return json.Marshal(toSerialize)
}

type NullableCreateMilestoneOption struct {
	value *CreateMilestoneOption
	isSet bool
}

func (v NullableCreateMilestoneOption) Get() *CreateMilestoneOption {
	return v.value
}

func (v *NullableCreateMilestoneOption) Set(val *CreateMilestoneOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateMilestoneOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateMilestoneOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateMilestoneOption(val *CreateMilestoneOption) *NullableCreateMilestoneOption {
	return &NullableCreateMilestoneOption{value: val, isSet: true}
}

func (v NullableCreateMilestoneOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateMilestoneOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



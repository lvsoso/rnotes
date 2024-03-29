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

// Label Label a label to an issue or a pr
type Label struct {
	Color *string `json:"color,omitempty"`
	Description *string `json:"description,omitempty"`
	Exclusive *bool `json:"exclusive,omitempty"`
	Id *int64 `json:"id,omitempty"`
	IsArchived *bool `json:"is_archived,omitempty"`
	Name *string `json:"name,omitempty"`
	Url *string `json:"url,omitempty"`
}

// NewLabel instantiates a new Label object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewLabel() *Label {
	this := Label{}
	return &this
}

// NewLabelWithDefaults instantiates a new Label object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewLabelWithDefaults() *Label {
	this := Label{}
	return &this
}

// GetColor returns the Color field value if set, zero value otherwise.
func (o *Label) GetColor() string {
	if o == nil || o.Color == nil {
		var ret string
		return ret
	}
	return *o.Color
}

// GetColorOk returns a tuple with the Color field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetColorOk() (*string, bool) {
	if o == nil || o.Color == nil {
		return nil, false
	}
	return o.Color, true
}

// HasColor returns a boolean if a field has been set.
func (o *Label) HasColor() bool {
	if o != nil && o.Color != nil {
		return true
	}

	return false
}

// SetColor gets a reference to the given string and assigns it to the Color field.
func (o *Label) SetColor(v string) {
	o.Color = &v
}

// GetDescription returns the Description field value if set, zero value otherwise.
func (o *Label) GetDescription() string {
	if o == nil || o.Description == nil {
		var ret string
		return ret
	}
	return *o.Description
}

// GetDescriptionOk returns a tuple with the Description field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetDescriptionOk() (*string, bool) {
	if o == nil || o.Description == nil {
		return nil, false
	}
	return o.Description, true
}

// HasDescription returns a boolean if a field has been set.
func (o *Label) HasDescription() bool {
	if o != nil && o.Description != nil {
		return true
	}

	return false
}

// SetDescription gets a reference to the given string and assigns it to the Description field.
func (o *Label) SetDescription(v string) {
	o.Description = &v
}

// GetExclusive returns the Exclusive field value if set, zero value otherwise.
func (o *Label) GetExclusive() bool {
	if o == nil || o.Exclusive == nil {
		var ret bool
		return ret
	}
	return *o.Exclusive
}

// GetExclusiveOk returns a tuple with the Exclusive field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetExclusiveOk() (*bool, bool) {
	if o == nil || o.Exclusive == nil {
		return nil, false
	}
	return o.Exclusive, true
}

// HasExclusive returns a boolean if a field has been set.
func (o *Label) HasExclusive() bool {
	if o != nil && o.Exclusive != nil {
		return true
	}

	return false
}

// SetExclusive gets a reference to the given bool and assigns it to the Exclusive field.
func (o *Label) SetExclusive(v bool) {
	o.Exclusive = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Label) GetId() int64 {
	if o == nil || o.Id == nil {
		var ret int64
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetIdOk() (*int64, bool) {
	if o == nil || o.Id == nil {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Label) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given int64 and assigns it to the Id field.
func (o *Label) SetId(v int64) {
	o.Id = &v
}

// GetIsArchived returns the IsArchived field value if set, zero value otherwise.
func (o *Label) GetIsArchived() bool {
	if o == nil || o.IsArchived == nil {
		var ret bool
		return ret
	}
	return *o.IsArchived
}

// GetIsArchivedOk returns a tuple with the IsArchived field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetIsArchivedOk() (*bool, bool) {
	if o == nil || o.IsArchived == nil {
		return nil, false
	}
	return o.IsArchived, true
}

// HasIsArchived returns a boolean if a field has been set.
func (o *Label) HasIsArchived() bool {
	if o != nil && o.IsArchived != nil {
		return true
	}

	return false
}

// SetIsArchived gets a reference to the given bool and assigns it to the IsArchived field.
func (o *Label) SetIsArchived(v bool) {
	o.IsArchived = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Label) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Label) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Label) SetName(v string) {
	o.Name = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *Label) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Label) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *Label) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *Label) SetUrl(v string) {
	o.Url = &v
}

func (o Label) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Color != nil {
		toSerialize["color"] = o.Color
	}
	if o.Description != nil {
		toSerialize["description"] = o.Description
	}
	if o.Exclusive != nil {
		toSerialize["exclusive"] = o.Exclusive
	}
	if o.Id != nil {
		toSerialize["id"] = o.Id
	}
	if o.IsArchived != nil {
		toSerialize["is_archived"] = o.IsArchived
	}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	return json.Marshal(toSerialize)
}

type NullableLabel struct {
	value *Label
	isSet bool
}

func (v NullableLabel) Get() *Label {
	return v.value
}

func (v *NullableLabel) Set(val *Label) {
	v.value = val
	v.isSet = true
}

func (v NullableLabel) IsSet() bool {
	return v.isSet
}

func (v *NullableLabel) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableLabel(val *Label) *NullableLabel {
	return &NullableLabel{value: val, isSet: true}
}

func (v NullableLabel) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableLabel) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



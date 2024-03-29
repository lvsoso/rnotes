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

// UserHeatmapData UserHeatmapData represents the data needed to create a heatmap
type UserHeatmapData struct {
	Contributions *int64 `json:"contributions,omitempty"`
	// TimeStamp defines a timestamp
	Timestamp *int64 `json:"timestamp,omitempty"`
}

// NewUserHeatmapData instantiates a new UserHeatmapData object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewUserHeatmapData() *UserHeatmapData {
	this := UserHeatmapData{}
	return &this
}

// NewUserHeatmapDataWithDefaults instantiates a new UserHeatmapData object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewUserHeatmapDataWithDefaults() *UserHeatmapData {
	this := UserHeatmapData{}
	return &this
}

// GetContributions returns the Contributions field value if set, zero value otherwise.
func (o *UserHeatmapData) GetContributions() int64 {
	if o == nil || o.Contributions == nil {
		var ret int64
		return ret
	}
	return *o.Contributions
}

// GetContributionsOk returns a tuple with the Contributions field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *UserHeatmapData) GetContributionsOk() (*int64, bool) {
	if o == nil || o.Contributions == nil {
		return nil, false
	}
	return o.Contributions, true
}

// HasContributions returns a boolean if a field has been set.
func (o *UserHeatmapData) HasContributions() bool {
	if o != nil && o.Contributions != nil {
		return true
	}

	return false
}

// SetContributions gets a reference to the given int64 and assigns it to the Contributions field.
func (o *UserHeatmapData) SetContributions(v int64) {
	o.Contributions = &v
}

// GetTimestamp returns the Timestamp field value if set, zero value otherwise.
func (o *UserHeatmapData) GetTimestamp() int64 {
	if o == nil || o.Timestamp == nil {
		var ret int64
		return ret
	}
	return *o.Timestamp
}

// GetTimestampOk returns a tuple with the Timestamp field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *UserHeatmapData) GetTimestampOk() (*int64, bool) {
	if o == nil || o.Timestamp == nil {
		return nil, false
	}
	return o.Timestamp, true
}

// HasTimestamp returns a boolean if a field has been set.
func (o *UserHeatmapData) HasTimestamp() bool {
	if o != nil && o.Timestamp != nil {
		return true
	}

	return false
}

// SetTimestamp gets a reference to the given int64 and assigns it to the Timestamp field.
func (o *UserHeatmapData) SetTimestamp(v int64) {
	o.Timestamp = &v
}

func (o UserHeatmapData) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Contributions != nil {
		toSerialize["contributions"] = o.Contributions
	}
	if o.Timestamp != nil {
		toSerialize["timestamp"] = o.Timestamp
	}
	return json.Marshal(toSerialize)
}

type NullableUserHeatmapData struct {
	value *UserHeatmapData
	isSet bool
}

func (v NullableUserHeatmapData) Get() *UserHeatmapData {
	return v.value
}

func (v *NullableUserHeatmapData) Set(val *UserHeatmapData) {
	v.value = val
	v.isSet = true
}

func (v NullableUserHeatmapData) IsSet() bool {
	return v.isSet
}

func (v *NullableUserHeatmapData) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableUserHeatmapData(val *UserHeatmapData) *NullableUserHeatmapData {
	return &NullableUserHeatmapData{value: val, isSet: true}
}

func (v NullableUserHeatmapData) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableUserHeatmapData) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



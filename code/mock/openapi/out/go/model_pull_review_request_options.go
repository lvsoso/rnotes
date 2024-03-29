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

// PullReviewRequestOptions PullReviewRequestOptions are options to add or remove pull review requests
type PullReviewRequestOptions struct {
	Reviewers *[]string `json:"reviewers,omitempty"`
	TeamReviewers *[]string `json:"team_reviewers,omitempty"`
}

// NewPullReviewRequestOptions instantiates a new PullReviewRequestOptions object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPullReviewRequestOptions() *PullReviewRequestOptions {
	this := PullReviewRequestOptions{}
	return &this
}

// NewPullReviewRequestOptionsWithDefaults instantiates a new PullReviewRequestOptions object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPullReviewRequestOptionsWithDefaults() *PullReviewRequestOptions {
	this := PullReviewRequestOptions{}
	return &this
}

// GetReviewers returns the Reviewers field value if set, zero value otherwise.
func (o *PullReviewRequestOptions) GetReviewers() []string {
	if o == nil || o.Reviewers == nil {
		var ret []string
		return ret
	}
	return *o.Reviewers
}

// GetReviewersOk returns a tuple with the Reviewers field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewRequestOptions) GetReviewersOk() (*[]string, bool) {
	if o == nil || o.Reviewers == nil {
		return nil, false
	}
	return o.Reviewers, true
}

// HasReviewers returns a boolean if a field has been set.
func (o *PullReviewRequestOptions) HasReviewers() bool {
	if o != nil && o.Reviewers != nil {
		return true
	}

	return false
}

// SetReviewers gets a reference to the given []string and assigns it to the Reviewers field.
func (o *PullReviewRequestOptions) SetReviewers(v []string) {
	o.Reviewers = &v
}

// GetTeamReviewers returns the TeamReviewers field value if set, zero value otherwise.
func (o *PullReviewRequestOptions) GetTeamReviewers() []string {
	if o == nil || o.TeamReviewers == nil {
		var ret []string
		return ret
	}
	return *o.TeamReviewers
}

// GetTeamReviewersOk returns a tuple with the TeamReviewers field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewRequestOptions) GetTeamReviewersOk() (*[]string, bool) {
	if o == nil || o.TeamReviewers == nil {
		return nil, false
	}
	return o.TeamReviewers, true
}

// HasTeamReviewers returns a boolean if a field has been set.
func (o *PullReviewRequestOptions) HasTeamReviewers() bool {
	if o != nil && o.TeamReviewers != nil {
		return true
	}

	return false
}

// SetTeamReviewers gets a reference to the given []string and assigns it to the TeamReviewers field.
func (o *PullReviewRequestOptions) SetTeamReviewers(v []string) {
	o.TeamReviewers = &v
}

func (o PullReviewRequestOptions) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Reviewers != nil {
		toSerialize["reviewers"] = o.Reviewers
	}
	if o.TeamReviewers != nil {
		toSerialize["team_reviewers"] = o.TeamReviewers
	}
	return json.Marshal(toSerialize)
}

type NullablePullReviewRequestOptions struct {
	value *PullReviewRequestOptions
	isSet bool
}

func (v NullablePullReviewRequestOptions) Get() *PullReviewRequestOptions {
	return v.value
}

func (v *NullablePullReviewRequestOptions) Set(val *PullReviewRequestOptions) {
	v.value = val
	v.isSet = true
}

func (v NullablePullReviewRequestOptions) IsSet() bool {
	return v.isSet
}

func (v *NullablePullReviewRequestOptions) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePullReviewRequestOptions(val *PullReviewRequestOptions) *NullablePullReviewRequestOptions {
	return &NullablePullReviewRequestOptions{value: val, isSet: true}
}

func (v NullablePullReviewRequestOptions) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePullReviewRequestOptions) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



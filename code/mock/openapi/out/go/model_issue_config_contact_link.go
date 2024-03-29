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

// IssueConfigContactLink struct for IssueConfigContactLink
type IssueConfigContactLink struct {
	About *string `json:"about,omitempty"`
	Name *string `json:"name,omitempty"`
	Url *string `json:"url,omitempty"`
}

// NewIssueConfigContactLink instantiates a new IssueConfigContactLink object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewIssueConfigContactLink() *IssueConfigContactLink {
	this := IssueConfigContactLink{}
	return &this
}

// NewIssueConfigContactLinkWithDefaults instantiates a new IssueConfigContactLink object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewIssueConfigContactLinkWithDefaults() *IssueConfigContactLink {
	this := IssueConfigContactLink{}
	return &this
}

// GetAbout returns the About field value if set, zero value otherwise.
func (o *IssueConfigContactLink) GetAbout() string {
	if o == nil || o.About == nil {
		var ret string
		return ret
	}
	return *o.About
}

// GetAboutOk returns a tuple with the About field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *IssueConfigContactLink) GetAboutOk() (*string, bool) {
	if o == nil || o.About == nil {
		return nil, false
	}
	return o.About, true
}

// HasAbout returns a boolean if a field has been set.
func (o *IssueConfigContactLink) HasAbout() bool {
	if o != nil && o.About != nil {
		return true
	}

	return false
}

// SetAbout gets a reference to the given string and assigns it to the About field.
func (o *IssueConfigContactLink) SetAbout(v string) {
	o.About = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *IssueConfigContactLink) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *IssueConfigContactLink) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *IssueConfigContactLink) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *IssueConfigContactLink) SetName(v string) {
	o.Name = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *IssueConfigContactLink) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *IssueConfigContactLink) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *IssueConfigContactLink) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *IssueConfigContactLink) SetUrl(v string) {
	o.Url = &v
}

func (o IssueConfigContactLink) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.About != nil {
		toSerialize["about"] = o.About
	}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	return json.Marshal(toSerialize)
}

type NullableIssueConfigContactLink struct {
	value *IssueConfigContactLink
	isSet bool
}

func (v NullableIssueConfigContactLink) Get() *IssueConfigContactLink {
	return v.value
}

func (v *NullableIssueConfigContactLink) Set(val *IssueConfigContactLink) {
	v.value = val
	v.isSet = true
}

func (v NullableIssueConfigContactLink) IsSet() bool {
	return v.isSet
}

func (v *NullableIssueConfigContactLink) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableIssueConfigContactLink(val *IssueConfigContactLink) *NullableIssueConfigContactLink {
	return &NullableIssueConfigContactLink{value: val, isSet: true}
}

func (v NullableIssueConfigContactLink) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableIssueConfigContactLink) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



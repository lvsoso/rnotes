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

// ExternalWiki ExternalWiki represents setting for external wiki
type ExternalWiki struct {
	// URL of external wiki.
	ExternalWikiUrl *string `json:"external_wiki_url,omitempty"`
}

// NewExternalWiki instantiates a new ExternalWiki object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewExternalWiki() *ExternalWiki {
	this := ExternalWiki{}
	return &this
}

// NewExternalWikiWithDefaults instantiates a new ExternalWiki object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewExternalWikiWithDefaults() *ExternalWiki {
	this := ExternalWiki{}
	return &this
}

// GetExternalWikiUrl returns the ExternalWikiUrl field value if set, zero value otherwise.
func (o *ExternalWiki) GetExternalWikiUrl() string {
	if o == nil || o.ExternalWikiUrl == nil {
		var ret string
		return ret
	}
	return *o.ExternalWikiUrl
}

// GetExternalWikiUrlOk returns a tuple with the ExternalWikiUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ExternalWiki) GetExternalWikiUrlOk() (*string, bool) {
	if o == nil || o.ExternalWikiUrl == nil {
		return nil, false
	}
	return o.ExternalWikiUrl, true
}

// HasExternalWikiUrl returns a boolean if a field has been set.
func (o *ExternalWiki) HasExternalWikiUrl() bool {
	if o != nil && o.ExternalWikiUrl != nil {
		return true
	}

	return false
}

// SetExternalWikiUrl gets a reference to the given string and assigns it to the ExternalWikiUrl field.
func (o *ExternalWiki) SetExternalWikiUrl(v string) {
	o.ExternalWikiUrl = &v
}

func (o ExternalWiki) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.ExternalWikiUrl != nil {
		toSerialize["external_wiki_url"] = o.ExternalWikiUrl
	}
	return json.Marshal(toSerialize)
}

type NullableExternalWiki struct {
	value *ExternalWiki
	isSet bool
}

func (v NullableExternalWiki) Get() *ExternalWiki {
	return v.value
}

func (v *NullableExternalWiki) Set(val *ExternalWiki) {
	v.value = val
	v.isSet = true
}

func (v NullableExternalWiki) IsSet() bool {
	return v.isSet
}

func (v *NullableExternalWiki) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableExternalWiki(val *ExternalWiki) *NullableExternalWiki {
	return &NullableExternalWiki{value: val, isSet: true}
}

func (v NullableExternalWiki) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableExternalWiki) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



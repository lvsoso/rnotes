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

// WikiPageMetaData WikiPageMetaData wiki page meta information
type WikiPageMetaData struct {
	HtmlUrl *string `json:"html_url,omitempty"`
	LastCommit *WikiCommit `json:"last_commit,omitempty"`
	SubUrl *string `json:"sub_url,omitempty"`
	Title *string `json:"title,omitempty"`
}

// NewWikiPageMetaData instantiates a new WikiPageMetaData object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewWikiPageMetaData() *WikiPageMetaData {
	this := WikiPageMetaData{}
	return &this
}

// NewWikiPageMetaDataWithDefaults instantiates a new WikiPageMetaData object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewWikiPageMetaDataWithDefaults() *WikiPageMetaData {
	this := WikiPageMetaData{}
	return &this
}

// GetHtmlUrl returns the HtmlUrl field value if set, zero value otherwise.
func (o *WikiPageMetaData) GetHtmlUrl() string {
	if o == nil || o.HtmlUrl == nil {
		var ret string
		return ret
	}
	return *o.HtmlUrl
}

// GetHtmlUrlOk returns a tuple with the HtmlUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *WikiPageMetaData) GetHtmlUrlOk() (*string, bool) {
	if o == nil || o.HtmlUrl == nil {
		return nil, false
	}
	return o.HtmlUrl, true
}

// HasHtmlUrl returns a boolean if a field has been set.
func (o *WikiPageMetaData) HasHtmlUrl() bool {
	if o != nil && o.HtmlUrl != nil {
		return true
	}

	return false
}

// SetHtmlUrl gets a reference to the given string and assigns it to the HtmlUrl field.
func (o *WikiPageMetaData) SetHtmlUrl(v string) {
	o.HtmlUrl = &v
}

// GetLastCommit returns the LastCommit field value if set, zero value otherwise.
func (o *WikiPageMetaData) GetLastCommit() WikiCommit {
	if o == nil || o.LastCommit == nil {
		var ret WikiCommit
		return ret
	}
	return *o.LastCommit
}

// GetLastCommitOk returns a tuple with the LastCommit field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *WikiPageMetaData) GetLastCommitOk() (*WikiCommit, bool) {
	if o == nil || o.LastCommit == nil {
		return nil, false
	}
	return o.LastCommit, true
}

// HasLastCommit returns a boolean if a field has been set.
func (o *WikiPageMetaData) HasLastCommit() bool {
	if o != nil && o.LastCommit != nil {
		return true
	}

	return false
}

// SetLastCommit gets a reference to the given WikiCommit and assigns it to the LastCommit field.
func (o *WikiPageMetaData) SetLastCommit(v WikiCommit) {
	o.LastCommit = &v
}

// GetSubUrl returns the SubUrl field value if set, zero value otherwise.
func (o *WikiPageMetaData) GetSubUrl() string {
	if o == nil || o.SubUrl == nil {
		var ret string
		return ret
	}
	return *o.SubUrl
}

// GetSubUrlOk returns a tuple with the SubUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *WikiPageMetaData) GetSubUrlOk() (*string, bool) {
	if o == nil || o.SubUrl == nil {
		return nil, false
	}
	return o.SubUrl, true
}

// HasSubUrl returns a boolean if a field has been set.
func (o *WikiPageMetaData) HasSubUrl() bool {
	if o != nil && o.SubUrl != nil {
		return true
	}

	return false
}

// SetSubUrl gets a reference to the given string and assigns it to the SubUrl field.
func (o *WikiPageMetaData) SetSubUrl(v string) {
	o.SubUrl = &v
}

// GetTitle returns the Title field value if set, zero value otherwise.
func (o *WikiPageMetaData) GetTitle() string {
	if o == nil || o.Title == nil {
		var ret string
		return ret
	}
	return *o.Title
}

// GetTitleOk returns a tuple with the Title field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *WikiPageMetaData) GetTitleOk() (*string, bool) {
	if o == nil || o.Title == nil {
		return nil, false
	}
	return o.Title, true
}

// HasTitle returns a boolean if a field has been set.
func (o *WikiPageMetaData) HasTitle() bool {
	if o != nil && o.Title != nil {
		return true
	}

	return false
}

// SetTitle gets a reference to the given string and assigns it to the Title field.
func (o *WikiPageMetaData) SetTitle(v string) {
	o.Title = &v
}

func (o WikiPageMetaData) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.HtmlUrl != nil {
		toSerialize["html_url"] = o.HtmlUrl
	}
	if o.LastCommit != nil {
		toSerialize["last_commit"] = o.LastCommit
	}
	if o.SubUrl != nil {
		toSerialize["sub_url"] = o.SubUrl
	}
	if o.Title != nil {
		toSerialize["title"] = o.Title
	}
	return json.Marshal(toSerialize)
}

type NullableWikiPageMetaData struct {
	value *WikiPageMetaData
	isSet bool
}

func (v NullableWikiPageMetaData) Get() *WikiPageMetaData {
	return v.value
}

func (v *NullableWikiPageMetaData) Set(val *WikiPageMetaData) {
	v.value = val
	v.isSet = true
}

func (v NullableWikiPageMetaData) IsSet() bool {
	return v.isSet
}

func (v *NullableWikiPageMetaData) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableWikiPageMetaData(val *WikiPageMetaData) *NullableWikiPageMetaData {
	return &NullableWikiPageMetaData{value: val, isSet: true}
}

func (v NullableWikiPageMetaData) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableWikiPageMetaData) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



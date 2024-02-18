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

// GitTreeResponse GitTreeResponse returns a git tree
type GitTreeResponse struct {
	Page *int64 `json:"page,omitempty"`
	Sha *string `json:"sha,omitempty"`
	TotalCount *int64 `json:"total_count,omitempty"`
	Tree *[]GitEntry `json:"tree,omitempty"`
	Truncated *bool `json:"truncated,omitempty"`
	Url *string `json:"url,omitempty"`
}

// NewGitTreeResponse instantiates a new GitTreeResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewGitTreeResponse() *GitTreeResponse {
	this := GitTreeResponse{}
	return &this
}

// NewGitTreeResponseWithDefaults instantiates a new GitTreeResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewGitTreeResponseWithDefaults() *GitTreeResponse {
	this := GitTreeResponse{}
	return &this
}

// GetPage returns the Page field value if set, zero value otherwise.
func (o *GitTreeResponse) GetPage() int64 {
	if o == nil || o.Page == nil {
		var ret int64
		return ret
	}
	return *o.Page
}

// GetPageOk returns a tuple with the Page field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitTreeResponse) GetPageOk() (*int64, bool) {
	if o == nil || o.Page == nil {
		return nil, false
	}
	return o.Page, true
}

// HasPage returns a boolean if a field has been set.
func (o *GitTreeResponse) HasPage() bool {
	if o != nil && o.Page != nil {
		return true
	}

	return false
}

// SetPage gets a reference to the given int64 and assigns it to the Page field.
func (o *GitTreeResponse) SetPage(v int64) {
	o.Page = &v
}

// GetSha returns the Sha field value if set, zero value otherwise.
func (o *GitTreeResponse) GetSha() string {
	if o == nil || o.Sha == nil {
		var ret string
		return ret
	}
	return *o.Sha
}

// GetShaOk returns a tuple with the Sha field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitTreeResponse) GetShaOk() (*string, bool) {
	if o == nil || o.Sha == nil {
		return nil, false
	}
	return o.Sha, true
}

// HasSha returns a boolean if a field has been set.
func (o *GitTreeResponse) HasSha() bool {
	if o != nil && o.Sha != nil {
		return true
	}

	return false
}

// SetSha gets a reference to the given string and assigns it to the Sha field.
func (o *GitTreeResponse) SetSha(v string) {
	o.Sha = &v
}

// GetTotalCount returns the TotalCount field value if set, zero value otherwise.
func (o *GitTreeResponse) GetTotalCount() int64 {
	if o == nil || o.TotalCount == nil {
		var ret int64
		return ret
	}
	return *o.TotalCount
}

// GetTotalCountOk returns a tuple with the TotalCount field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitTreeResponse) GetTotalCountOk() (*int64, bool) {
	if o == nil || o.TotalCount == nil {
		return nil, false
	}
	return o.TotalCount, true
}

// HasTotalCount returns a boolean if a field has been set.
func (o *GitTreeResponse) HasTotalCount() bool {
	if o != nil && o.TotalCount != nil {
		return true
	}

	return false
}

// SetTotalCount gets a reference to the given int64 and assigns it to the TotalCount field.
func (o *GitTreeResponse) SetTotalCount(v int64) {
	o.TotalCount = &v
}

// GetTree returns the Tree field value if set, zero value otherwise.
func (o *GitTreeResponse) GetTree() []GitEntry {
	if o == nil || o.Tree == nil {
		var ret []GitEntry
		return ret
	}
	return *o.Tree
}

// GetTreeOk returns a tuple with the Tree field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitTreeResponse) GetTreeOk() (*[]GitEntry, bool) {
	if o == nil || o.Tree == nil {
		return nil, false
	}
	return o.Tree, true
}

// HasTree returns a boolean if a field has been set.
func (o *GitTreeResponse) HasTree() bool {
	if o != nil && o.Tree != nil {
		return true
	}

	return false
}

// SetTree gets a reference to the given []GitEntry and assigns it to the Tree field.
func (o *GitTreeResponse) SetTree(v []GitEntry) {
	o.Tree = &v
}

// GetTruncated returns the Truncated field value if set, zero value otherwise.
func (o *GitTreeResponse) GetTruncated() bool {
	if o == nil || o.Truncated == nil {
		var ret bool
		return ret
	}
	return *o.Truncated
}

// GetTruncatedOk returns a tuple with the Truncated field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitTreeResponse) GetTruncatedOk() (*bool, bool) {
	if o == nil || o.Truncated == nil {
		return nil, false
	}
	return o.Truncated, true
}

// HasTruncated returns a boolean if a field has been set.
func (o *GitTreeResponse) HasTruncated() bool {
	if o != nil && o.Truncated != nil {
		return true
	}

	return false
}

// SetTruncated gets a reference to the given bool and assigns it to the Truncated field.
func (o *GitTreeResponse) SetTruncated(v bool) {
	o.Truncated = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *GitTreeResponse) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitTreeResponse) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *GitTreeResponse) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *GitTreeResponse) SetUrl(v string) {
	o.Url = &v
}

func (o GitTreeResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Page != nil {
		toSerialize["page"] = o.Page
	}
	if o.Sha != nil {
		toSerialize["sha"] = o.Sha
	}
	if o.TotalCount != nil {
		toSerialize["total_count"] = o.TotalCount
	}
	if o.Tree != nil {
		toSerialize["tree"] = o.Tree
	}
	if o.Truncated != nil {
		toSerialize["truncated"] = o.Truncated
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	return json.Marshal(toSerialize)
}

type NullableGitTreeResponse struct {
	value *GitTreeResponse
	isSet bool
}

func (v NullableGitTreeResponse) Get() *GitTreeResponse {
	return v.value
}

func (v *NullableGitTreeResponse) Set(val *GitTreeResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableGitTreeResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableGitTreeResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableGitTreeResponse(val *GitTreeResponse) *NullableGitTreeResponse {
	return &NullableGitTreeResponse{value: val, isSet: true}
}

func (v NullableGitTreeResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableGitTreeResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



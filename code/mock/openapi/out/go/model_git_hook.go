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

// GitHook GitHook represents a Git repository hook
type GitHook struct {
	Content *string `json:"content,omitempty"`
	IsActive *bool `json:"is_active,omitempty"`
	Name *string `json:"name,omitempty"`
}

// NewGitHook instantiates a new GitHook object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewGitHook() *GitHook {
	this := GitHook{}
	return &this
}

// NewGitHookWithDefaults instantiates a new GitHook object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewGitHookWithDefaults() *GitHook {
	this := GitHook{}
	return &this
}

// GetContent returns the Content field value if set, zero value otherwise.
func (o *GitHook) GetContent() string {
	if o == nil || o.Content == nil {
		var ret string
		return ret
	}
	return *o.Content
}

// GetContentOk returns a tuple with the Content field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitHook) GetContentOk() (*string, bool) {
	if o == nil || o.Content == nil {
		return nil, false
	}
	return o.Content, true
}

// HasContent returns a boolean if a field has been set.
func (o *GitHook) HasContent() bool {
	if o != nil && o.Content != nil {
		return true
	}

	return false
}

// SetContent gets a reference to the given string and assigns it to the Content field.
func (o *GitHook) SetContent(v string) {
	o.Content = &v
}

// GetIsActive returns the IsActive field value if set, zero value otherwise.
func (o *GitHook) GetIsActive() bool {
	if o == nil || o.IsActive == nil {
		var ret bool
		return ret
	}
	return *o.IsActive
}

// GetIsActiveOk returns a tuple with the IsActive field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitHook) GetIsActiveOk() (*bool, bool) {
	if o == nil || o.IsActive == nil {
		return nil, false
	}
	return o.IsActive, true
}

// HasIsActive returns a boolean if a field has been set.
func (o *GitHook) HasIsActive() bool {
	if o != nil && o.IsActive != nil {
		return true
	}

	return false
}

// SetIsActive gets a reference to the given bool and assigns it to the IsActive field.
func (o *GitHook) SetIsActive(v bool) {
	o.IsActive = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *GitHook) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GitHook) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *GitHook) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *GitHook) SetName(v string) {
	o.Name = &v
}

func (o GitHook) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Content != nil {
		toSerialize["content"] = o.Content
	}
	if o.IsActive != nil {
		toSerialize["is_active"] = o.IsActive
	}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	return json.Marshal(toSerialize)
}

type NullableGitHook struct {
	value *GitHook
	isSet bool
}

func (v NullableGitHook) Get() *GitHook {
	return v.value
}

func (v *NullableGitHook) Set(val *GitHook) {
	v.value = val
	v.isSet = true
}

func (v NullableGitHook) IsSet() bool {
	return v.isSet
}

func (v *NullableGitHook) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableGitHook(val *GitHook) *NullableGitHook {
	return &NullableGitHook{value: val, isSet: true}
}

func (v NullableGitHook) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableGitHook) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


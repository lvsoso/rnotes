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

// FileCommitResponse struct for FileCommitResponse
type FileCommitResponse struct {
	Author *CommitUser `json:"author,omitempty"`
	Committer *CommitUser `json:"committer,omitempty"`
	Created *time.Time `json:"created,omitempty"`
	HtmlUrl *string `json:"html_url,omitempty"`
	Message *string `json:"message,omitempty"`
	Parents *[]CommitMeta `json:"parents,omitempty"`
	Sha *string `json:"sha,omitempty"`
	Tree *CommitMeta `json:"tree,omitempty"`
	Url *string `json:"url,omitempty"`
}

// NewFileCommitResponse instantiates a new FileCommitResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewFileCommitResponse() *FileCommitResponse {
	this := FileCommitResponse{}
	return &this
}

// NewFileCommitResponseWithDefaults instantiates a new FileCommitResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewFileCommitResponseWithDefaults() *FileCommitResponse {
	this := FileCommitResponse{}
	return &this
}

// GetAuthor returns the Author field value if set, zero value otherwise.
func (o *FileCommitResponse) GetAuthor() CommitUser {
	if o == nil || o.Author == nil {
		var ret CommitUser
		return ret
	}
	return *o.Author
}

// GetAuthorOk returns a tuple with the Author field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetAuthorOk() (*CommitUser, bool) {
	if o == nil || o.Author == nil {
		return nil, false
	}
	return o.Author, true
}

// HasAuthor returns a boolean if a field has been set.
func (o *FileCommitResponse) HasAuthor() bool {
	if o != nil && o.Author != nil {
		return true
	}

	return false
}

// SetAuthor gets a reference to the given CommitUser and assigns it to the Author field.
func (o *FileCommitResponse) SetAuthor(v CommitUser) {
	o.Author = &v
}

// GetCommitter returns the Committer field value if set, zero value otherwise.
func (o *FileCommitResponse) GetCommitter() CommitUser {
	if o == nil || o.Committer == nil {
		var ret CommitUser
		return ret
	}
	return *o.Committer
}

// GetCommitterOk returns a tuple with the Committer field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetCommitterOk() (*CommitUser, bool) {
	if o == nil || o.Committer == nil {
		return nil, false
	}
	return o.Committer, true
}

// HasCommitter returns a boolean if a field has been set.
func (o *FileCommitResponse) HasCommitter() bool {
	if o != nil && o.Committer != nil {
		return true
	}

	return false
}

// SetCommitter gets a reference to the given CommitUser and assigns it to the Committer field.
func (o *FileCommitResponse) SetCommitter(v CommitUser) {
	o.Committer = &v
}

// GetCreated returns the Created field value if set, zero value otherwise.
func (o *FileCommitResponse) GetCreated() time.Time {
	if o == nil || o.Created == nil {
		var ret time.Time
		return ret
	}
	return *o.Created
}

// GetCreatedOk returns a tuple with the Created field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetCreatedOk() (*time.Time, bool) {
	if o == nil || o.Created == nil {
		return nil, false
	}
	return o.Created, true
}

// HasCreated returns a boolean if a field has been set.
func (o *FileCommitResponse) HasCreated() bool {
	if o != nil && o.Created != nil {
		return true
	}

	return false
}

// SetCreated gets a reference to the given time.Time and assigns it to the Created field.
func (o *FileCommitResponse) SetCreated(v time.Time) {
	o.Created = &v
}

// GetHtmlUrl returns the HtmlUrl field value if set, zero value otherwise.
func (o *FileCommitResponse) GetHtmlUrl() string {
	if o == nil || o.HtmlUrl == nil {
		var ret string
		return ret
	}
	return *o.HtmlUrl
}

// GetHtmlUrlOk returns a tuple with the HtmlUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetHtmlUrlOk() (*string, bool) {
	if o == nil || o.HtmlUrl == nil {
		return nil, false
	}
	return o.HtmlUrl, true
}

// HasHtmlUrl returns a boolean if a field has been set.
func (o *FileCommitResponse) HasHtmlUrl() bool {
	if o != nil && o.HtmlUrl != nil {
		return true
	}

	return false
}

// SetHtmlUrl gets a reference to the given string and assigns it to the HtmlUrl field.
func (o *FileCommitResponse) SetHtmlUrl(v string) {
	o.HtmlUrl = &v
}

// GetMessage returns the Message field value if set, zero value otherwise.
func (o *FileCommitResponse) GetMessage() string {
	if o == nil || o.Message == nil {
		var ret string
		return ret
	}
	return *o.Message
}

// GetMessageOk returns a tuple with the Message field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetMessageOk() (*string, bool) {
	if o == nil || o.Message == nil {
		return nil, false
	}
	return o.Message, true
}

// HasMessage returns a boolean if a field has been set.
func (o *FileCommitResponse) HasMessage() bool {
	if o != nil && o.Message != nil {
		return true
	}

	return false
}

// SetMessage gets a reference to the given string and assigns it to the Message field.
func (o *FileCommitResponse) SetMessage(v string) {
	o.Message = &v
}

// GetParents returns the Parents field value if set, zero value otherwise.
func (o *FileCommitResponse) GetParents() []CommitMeta {
	if o == nil || o.Parents == nil {
		var ret []CommitMeta
		return ret
	}
	return *o.Parents
}

// GetParentsOk returns a tuple with the Parents field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetParentsOk() (*[]CommitMeta, bool) {
	if o == nil || o.Parents == nil {
		return nil, false
	}
	return o.Parents, true
}

// HasParents returns a boolean if a field has been set.
func (o *FileCommitResponse) HasParents() bool {
	if o != nil && o.Parents != nil {
		return true
	}

	return false
}

// SetParents gets a reference to the given []CommitMeta and assigns it to the Parents field.
func (o *FileCommitResponse) SetParents(v []CommitMeta) {
	o.Parents = &v
}

// GetSha returns the Sha field value if set, zero value otherwise.
func (o *FileCommitResponse) GetSha() string {
	if o == nil || o.Sha == nil {
		var ret string
		return ret
	}
	return *o.Sha
}

// GetShaOk returns a tuple with the Sha field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetShaOk() (*string, bool) {
	if o == nil || o.Sha == nil {
		return nil, false
	}
	return o.Sha, true
}

// HasSha returns a boolean if a field has been set.
func (o *FileCommitResponse) HasSha() bool {
	if o != nil && o.Sha != nil {
		return true
	}

	return false
}

// SetSha gets a reference to the given string and assigns it to the Sha field.
func (o *FileCommitResponse) SetSha(v string) {
	o.Sha = &v
}

// GetTree returns the Tree field value if set, zero value otherwise.
func (o *FileCommitResponse) GetTree() CommitMeta {
	if o == nil || o.Tree == nil {
		var ret CommitMeta
		return ret
	}
	return *o.Tree
}

// GetTreeOk returns a tuple with the Tree field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetTreeOk() (*CommitMeta, bool) {
	if o == nil || o.Tree == nil {
		return nil, false
	}
	return o.Tree, true
}

// HasTree returns a boolean if a field has been set.
func (o *FileCommitResponse) HasTree() bool {
	if o != nil && o.Tree != nil {
		return true
	}

	return false
}

// SetTree gets a reference to the given CommitMeta and assigns it to the Tree field.
func (o *FileCommitResponse) SetTree(v CommitMeta) {
	o.Tree = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *FileCommitResponse) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *FileCommitResponse) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *FileCommitResponse) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *FileCommitResponse) SetUrl(v string) {
	o.Url = &v
}

func (o FileCommitResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Author != nil {
		toSerialize["author"] = o.Author
	}
	if o.Committer != nil {
		toSerialize["committer"] = o.Committer
	}
	if o.Created != nil {
		toSerialize["created"] = o.Created
	}
	if o.HtmlUrl != nil {
		toSerialize["html_url"] = o.HtmlUrl
	}
	if o.Message != nil {
		toSerialize["message"] = o.Message
	}
	if o.Parents != nil {
		toSerialize["parents"] = o.Parents
	}
	if o.Sha != nil {
		toSerialize["sha"] = o.Sha
	}
	if o.Tree != nil {
		toSerialize["tree"] = o.Tree
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	return json.Marshal(toSerialize)
}

type NullableFileCommitResponse struct {
	value *FileCommitResponse
	isSet bool
}

func (v NullableFileCommitResponse) Get() *FileCommitResponse {
	return v.value
}

func (v *NullableFileCommitResponse) Set(val *FileCommitResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableFileCommitResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableFileCommitResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableFileCommitResponse(val *FileCommitResponse) *NullableFileCommitResponse {
	return &NullableFileCommitResponse{value: val, isSet: true}
}

func (v NullableFileCommitResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableFileCommitResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


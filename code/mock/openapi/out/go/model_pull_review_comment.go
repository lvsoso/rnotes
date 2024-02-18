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

// PullReviewComment PullReviewComment represents a comment on a pull request review
type PullReviewComment struct {
	Body *string `json:"body,omitempty"`
	CommitId *string `json:"commit_id,omitempty"`
	CreatedAt *time.Time `json:"created_at,omitempty"`
	DiffHunk *string `json:"diff_hunk,omitempty"`
	HtmlUrl *string `json:"html_url,omitempty"`
	Id *int64 `json:"id,omitempty"`
	OriginalCommitId *string `json:"original_commit_id,omitempty"`
	OriginalPosition *int32 `json:"original_position,omitempty"`
	Path *string `json:"path,omitempty"`
	Position *int32 `json:"position,omitempty"`
	PullRequestReviewId *int64 `json:"pull_request_review_id,omitempty"`
	PullRequestUrl *string `json:"pull_request_url,omitempty"`
	Resolver *User `json:"resolver,omitempty"`
	UpdatedAt *time.Time `json:"updated_at,omitempty"`
	User *User `json:"user,omitempty"`
}

// NewPullReviewComment instantiates a new PullReviewComment object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPullReviewComment() *PullReviewComment {
	this := PullReviewComment{}
	return &this
}

// NewPullReviewCommentWithDefaults instantiates a new PullReviewComment object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPullReviewCommentWithDefaults() *PullReviewComment {
	this := PullReviewComment{}
	return &this
}

// GetBody returns the Body field value if set, zero value otherwise.
func (o *PullReviewComment) GetBody() string {
	if o == nil || o.Body == nil {
		var ret string
		return ret
	}
	return *o.Body
}

// GetBodyOk returns a tuple with the Body field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetBodyOk() (*string, bool) {
	if o == nil || o.Body == nil {
		return nil, false
	}
	return o.Body, true
}

// HasBody returns a boolean if a field has been set.
func (o *PullReviewComment) HasBody() bool {
	if o != nil && o.Body != nil {
		return true
	}

	return false
}

// SetBody gets a reference to the given string and assigns it to the Body field.
func (o *PullReviewComment) SetBody(v string) {
	o.Body = &v
}

// GetCommitId returns the CommitId field value if set, zero value otherwise.
func (o *PullReviewComment) GetCommitId() string {
	if o == nil || o.CommitId == nil {
		var ret string
		return ret
	}
	return *o.CommitId
}

// GetCommitIdOk returns a tuple with the CommitId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetCommitIdOk() (*string, bool) {
	if o == nil || o.CommitId == nil {
		return nil, false
	}
	return o.CommitId, true
}

// HasCommitId returns a boolean if a field has been set.
func (o *PullReviewComment) HasCommitId() bool {
	if o != nil && o.CommitId != nil {
		return true
	}

	return false
}

// SetCommitId gets a reference to the given string and assigns it to the CommitId field.
func (o *PullReviewComment) SetCommitId(v string) {
	o.CommitId = &v
}

// GetCreatedAt returns the CreatedAt field value if set, zero value otherwise.
func (o *PullReviewComment) GetCreatedAt() time.Time {
	if o == nil || o.CreatedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.CreatedAt
}

// GetCreatedAtOk returns a tuple with the CreatedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetCreatedAtOk() (*time.Time, bool) {
	if o == nil || o.CreatedAt == nil {
		return nil, false
	}
	return o.CreatedAt, true
}

// HasCreatedAt returns a boolean if a field has been set.
func (o *PullReviewComment) HasCreatedAt() bool {
	if o != nil && o.CreatedAt != nil {
		return true
	}

	return false
}

// SetCreatedAt gets a reference to the given time.Time and assigns it to the CreatedAt field.
func (o *PullReviewComment) SetCreatedAt(v time.Time) {
	o.CreatedAt = &v
}

// GetDiffHunk returns the DiffHunk field value if set, zero value otherwise.
func (o *PullReviewComment) GetDiffHunk() string {
	if o == nil || o.DiffHunk == nil {
		var ret string
		return ret
	}
	return *o.DiffHunk
}

// GetDiffHunkOk returns a tuple with the DiffHunk field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetDiffHunkOk() (*string, bool) {
	if o == nil || o.DiffHunk == nil {
		return nil, false
	}
	return o.DiffHunk, true
}

// HasDiffHunk returns a boolean if a field has been set.
func (o *PullReviewComment) HasDiffHunk() bool {
	if o != nil && o.DiffHunk != nil {
		return true
	}

	return false
}

// SetDiffHunk gets a reference to the given string and assigns it to the DiffHunk field.
func (o *PullReviewComment) SetDiffHunk(v string) {
	o.DiffHunk = &v
}

// GetHtmlUrl returns the HtmlUrl field value if set, zero value otherwise.
func (o *PullReviewComment) GetHtmlUrl() string {
	if o == nil || o.HtmlUrl == nil {
		var ret string
		return ret
	}
	return *o.HtmlUrl
}

// GetHtmlUrlOk returns a tuple with the HtmlUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetHtmlUrlOk() (*string, bool) {
	if o == nil || o.HtmlUrl == nil {
		return nil, false
	}
	return o.HtmlUrl, true
}

// HasHtmlUrl returns a boolean if a field has been set.
func (o *PullReviewComment) HasHtmlUrl() bool {
	if o != nil && o.HtmlUrl != nil {
		return true
	}

	return false
}

// SetHtmlUrl gets a reference to the given string and assigns it to the HtmlUrl field.
func (o *PullReviewComment) SetHtmlUrl(v string) {
	o.HtmlUrl = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *PullReviewComment) GetId() int64 {
	if o == nil || o.Id == nil {
		var ret int64
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetIdOk() (*int64, bool) {
	if o == nil || o.Id == nil {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *PullReviewComment) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given int64 and assigns it to the Id field.
func (o *PullReviewComment) SetId(v int64) {
	o.Id = &v
}

// GetOriginalCommitId returns the OriginalCommitId field value if set, zero value otherwise.
func (o *PullReviewComment) GetOriginalCommitId() string {
	if o == nil || o.OriginalCommitId == nil {
		var ret string
		return ret
	}
	return *o.OriginalCommitId
}

// GetOriginalCommitIdOk returns a tuple with the OriginalCommitId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetOriginalCommitIdOk() (*string, bool) {
	if o == nil || o.OriginalCommitId == nil {
		return nil, false
	}
	return o.OriginalCommitId, true
}

// HasOriginalCommitId returns a boolean if a field has been set.
func (o *PullReviewComment) HasOriginalCommitId() bool {
	if o != nil && o.OriginalCommitId != nil {
		return true
	}

	return false
}

// SetOriginalCommitId gets a reference to the given string and assigns it to the OriginalCommitId field.
func (o *PullReviewComment) SetOriginalCommitId(v string) {
	o.OriginalCommitId = &v
}

// GetOriginalPosition returns the OriginalPosition field value if set, zero value otherwise.
func (o *PullReviewComment) GetOriginalPosition() int32 {
	if o == nil || o.OriginalPosition == nil {
		var ret int32
		return ret
	}
	return *o.OriginalPosition
}

// GetOriginalPositionOk returns a tuple with the OriginalPosition field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetOriginalPositionOk() (*int32, bool) {
	if o == nil || o.OriginalPosition == nil {
		return nil, false
	}
	return o.OriginalPosition, true
}

// HasOriginalPosition returns a boolean if a field has been set.
func (o *PullReviewComment) HasOriginalPosition() bool {
	if o != nil && o.OriginalPosition != nil {
		return true
	}

	return false
}

// SetOriginalPosition gets a reference to the given int32 and assigns it to the OriginalPosition field.
func (o *PullReviewComment) SetOriginalPosition(v int32) {
	o.OriginalPosition = &v
}

// GetPath returns the Path field value if set, zero value otherwise.
func (o *PullReviewComment) GetPath() string {
	if o == nil || o.Path == nil {
		var ret string
		return ret
	}
	return *o.Path
}

// GetPathOk returns a tuple with the Path field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetPathOk() (*string, bool) {
	if o == nil || o.Path == nil {
		return nil, false
	}
	return o.Path, true
}

// HasPath returns a boolean if a field has been set.
func (o *PullReviewComment) HasPath() bool {
	if o != nil && o.Path != nil {
		return true
	}

	return false
}

// SetPath gets a reference to the given string and assigns it to the Path field.
func (o *PullReviewComment) SetPath(v string) {
	o.Path = &v
}

// GetPosition returns the Position field value if set, zero value otherwise.
func (o *PullReviewComment) GetPosition() int32 {
	if o == nil || o.Position == nil {
		var ret int32
		return ret
	}
	return *o.Position
}

// GetPositionOk returns a tuple with the Position field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetPositionOk() (*int32, bool) {
	if o == nil || o.Position == nil {
		return nil, false
	}
	return o.Position, true
}

// HasPosition returns a boolean if a field has been set.
func (o *PullReviewComment) HasPosition() bool {
	if o != nil && o.Position != nil {
		return true
	}

	return false
}

// SetPosition gets a reference to the given int32 and assigns it to the Position field.
func (o *PullReviewComment) SetPosition(v int32) {
	o.Position = &v
}

// GetPullRequestReviewId returns the PullRequestReviewId field value if set, zero value otherwise.
func (o *PullReviewComment) GetPullRequestReviewId() int64 {
	if o == nil || o.PullRequestReviewId == nil {
		var ret int64
		return ret
	}
	return *o.PullRequestReviewId
}

// GetPullRequestReviewIdOk returns a tuple with the PullRequestReviewId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetPullRequestReviewIdOk() (*int64, bool) {
	if o == nil || o.PullRequestReviewId == nil {
		return nil, false
	}
	return o.PullRequestReviewId, true
}

// HasPullRequestReviewId returns a boolean if a field has been set.
func (o *PullReviewComment) HasPullRequestReviewId() bool {
	if o != nil && o.PullRequestReviewId != nil {
		return true
	}

	return false
}

// SetPullRequestReviewId gets a reference to the given int64 and assigns it to the PullRequestReviewId field.
func (o *PullReviewComment) SetPullRequestReviewId(v int64) {
	o.PullRequestReviewId = &v
}

// GetPullRequestUrl returns the PullRequestUrl field value if set, zero value otherwise.
func (o *PullReviewComment) GetPullRequestUrl() string {
	if o == nil || o.PullRequestUrl == nil {
		var ret string
		return ret
	}
	return *o.PullRequestUrl
}

// GetPullRequestUrlOk returns a tuple with the PullRequestUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetPullRequestUrlOk() (*string, bool) {
	if o == nil || o.PullRequestUrl == nil {
		return nil, false
	}
	return o.PullRequestUrl, true
}

// HasPullRequestUrl returns a boolean if a field has been set.
func (o *PullReviewComment) HasPullRequestUrl() bool {
	if o != nil && o.PullRequestUrl != nil {
		return true
	}

	return false
}

// SetPullRequestUrl gets a reference to the given string and assigns it to the PullRequestUrl field.
func (o *PullReviewComment) SetPullRequestUrl(v string) {
	o.PullRequestUrl = &v
}

// GetResolver returns the Resolver field value if set, zero value otherwise.
func (o *PullReviewComment) GetResolver() User {
	if o == nil || o.Resolver == nil {
		var ret User
		return ret
	}
	return *o.Resolver
}

// GetResolverOk returns a tuple with the Resolver field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetResolverOk() (*User, bool) {
	if o == nil || o.Resolver == nil {
		return nil, false
	}
	return o.Resolver, true
}

// HasResolver returns a boolean if a field has been set.
func (o *PullReviewComment) HasResolver() bool {
	if o != nil && o.Resolver != nil {
		return true
	}

	return false
}

// SetResolver gets a reference to the given User and assigns it to the Resolver field.
func (o *PullReviewComment) SetResolver(v User) {
	o.Resolver = &v
}

// GetUpdatedAt returns the UpdatedAt field value if set, zero value otherwise.
func (o *PullReviewComment) GetUpdatedAt() time.Time {
	if o == nil || o.UpdatedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.UpdatedAt
}

// GetUpdatedAtOk returns a tuple with the UpdatedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetUpdatedAtOk() (*time.Time, bool) {
	if o == nil || o.UpdatedAt == nil {
		return nil, false
	}
	return o.UpdatedAt, true
}

// HasUpdatedAt returns a boolean if a field has been set.
func (o *PullReviewComment) HasUpdatedAt() bool {
	if o != nil && o.UpdatedAt != nil {
		return true
	}

	return false
}

// SetUpdatedAt gets a reference to the given time.Time and assigns it to the UpdatedAt field.
func (o *PullReviewComment) SetUpdatedAt(v time.Time) {
	o.UpdatedAt = &v
}

// GetUser returns the User field value if set, zero value otherwise.
func (o *PullReviewComment) GetUser() User {
	if o == nil || o.User == nil {
		var ret User
		return ret
	}
	return *o.User
}

// GetUserOk returns a tuple with the User field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PullReviewComment) GetUserOk() (*User, bool) {
	if o == nil || o.User == nil {
		return nil, false
	}
	return o.User, true
}

// HasUser returns a boolean if a field has been set.
func (o *PullReviewComment) HasUser() bool {
	if o != nil && o.User != nil {
		return true
	}

	return false
}

// SetUser gets a reference to the given User and assigns it to the User field.
func (o *PullReviewComment) SetUser(v User) {
	o.User = &v
}

func (o PullReviewComment) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Body != nil {
		toSerialize["body"] = o.Body
	}
	if o.CommitId != nil {
		toSerialize["commit_id"] = o.CommitId
	}
	if o.CreatedAt != nil {
		toSerialize["created_at"] = o.CreatedAt
	}
	if o.DiffHunk != nil {
		toSerialize["diff_hunk"] = o.DiffHunk
	}
	if o.HtmlUrl != nil {
		toSerialize["html_url"] = o.HtmlUrl
	}
	if o.Id != nil {
		toSerialize["id"] = o.Id
	}
	if o.OriginalCommitId != nil {
		toSerialize["original_commit_id"] = o.OriginalCommitId
	}
	if o.OriginalPosition != nil {
		toSerialize["original_position"] = o.OriginalPosition
	}
	if o.Path != nil {
		toSerialize["path"] = o.Path
	}
	if o.Position != nil {
		toSerialize["position"] = o.Position
	}
	if o.PullRequestReviewId != nil {
		toSerialize["pull_request_review_id"] = o.PullRequestReviewId
	}
	if o.PullRequestUrl != nil {
		toSerialize["pull_request_url"] = o.PullRequestUrl
	}
	if o.Resolver != nil {
		toSerialize["resolver"] = o.Resolver
	}
	if o.UpdatedAt != nil {
		toSerialize["updated_at"] = o.UpdatedAt
	}
	if o.User != nil {
		toSerialize["user"] = o.User
	}
	return json.Marshal(toSerialize)
}

type NullablePullReviewComment struct {
	value *PullReviewComment
	isSet bool
}

func (v NullablePullReviewComment) Get() *PullReviewComment {
	return v.value
}

func (v *NullablePullReviewComment) Set(val *PullReviewComment) {
	v.value = val
	v.isSet = true
}

func (v NullablePullReviewComment) IsSet() bool {
	return v.isSet
}

func (v *NullablePullReviewComment) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePullReviewComment(val *PullReviewComment) *NullablePullReviewComment {
	return &NullablePullReviewComment{value: val, isSet: true}
}

func (v NullablePullReviewComment) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePullReviewComment) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



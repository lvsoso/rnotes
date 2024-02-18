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

// NotificationThread NotificationThread expose Notification on API
type NotificationThread struct {
	Id *int64 `json:"id,omitempty"`
	Pinned *bool `json:"pinned,omitempty"`
	Repository *Repository `json:"repository,omitempty"`
	Subject *NotificationSubject `json:"subject,omitempty"`
	Unread *bool `json:"unread,omitempty"`
	UpdatedAt *time.Time `json:"updated_at,omitempty"`
	Url *string `json:"url,omitempty"`
}

// NewNotificationThread instantiates a new NotificationThread object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewNotificationThread() *NotificationThread {
	this := NotificationThread{}
	return &this
}

// NewNotificationThreadWithDefaults instantiates a new NotificationThread object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewNotificationThreadWithDefaults() *NotificationThread {
	this := NotificationThread{}
	return &this
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *NotificationThread) GetId() int64 {
	if o == nil || o.Id == nil {
		var ret int64
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetIdOk() (*int64, bool) {
	if o == nil || o.Id == nil {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *NotificationThread) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given int64 and assigns it to the Id field.
func (o *NotificationThread) SetId(v int64) {
	o.Id = &v
}

// GetPinned returns the Pinned field value if set, zero value otherwise.
func (o *NotificationThread) GetPinned() bool {
	if o == nil || o.Pinned == nil {
		var ret bool
		return ret
	}
	return *o.Pinned
}

// GetPinnedOk returns a tuple with the Pinned field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetPinnedOk() (*bool, bool) {
	if o == nil || o.Pinned == nil {
		return nil, false
	}
	return o.Pinned, true
}

// HasPinned returns a boolean if a field has been set.
func (o *NotificationThread) HasPinned() bool {
	if o != nil && o.Pinned != nil {
		return true
	}

	return false
}

// SetPinned gets a reference to the given bool and assigns it to the Pinned field.
func (o *NotificationThread) SetPinned(v bool) {
	o.Pinned = &v
}

// GetRepository returns the Repository field value if set, zero value otherwise.
func (o *NotificationThread) GetRepository() Repository {
	if o == nil || o.Repository == nil {
		var ret Repository
		return ret
	}
	return *o.Repository
}

// GetRepositoryOk returns a tuple with the Repository field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetRepositoryOk() (*Repository, bool) {
	if o == nil || o.Repository == nil {
		return nil, false
	}
	return o.Repository, true
}

// HasRepository returns a boolean if a field has been set.
func (o *NotificationThread) HasRepository() bool {
	if o != nil && o.Repository != nil {
		return true
	}

	return false
}

// SetRepository gets a reference to the given Repository and assigns it to the Repository field.
func (o *NotificationThread) SetRepository(v Repository) {
	o.Repository = &v
}

// GetSubject returns the Subject field value if set, zero value otherwise.
func (o *NotificationThread) GetSubject() NotificationSubject {
	if o == nil || o.Subject == nil {
		var ret NotificationSubject
		return ret
	}
	return *o.Subject
}

// GetSubjectOk returns a tuple with the Subject field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetSubjectOk() (*NotificationSubject, bool) {
	if o == nil || o.Subject == nil {
		return nil, false
	}
	return o.Subject, true
}

// HasSubject returns a boolean if a field has been set.
func (o *NotificationThread) HasSubject() bool {
	if o != nil && o.Subject != nil {
		return true
	}

	return false
}

// SetSubject gets a reference to the given NotificationSubject and assigns it to the Subject field.
func (o *NotificationThread) SetSubject(v NotificationSubject) {
	o.Subject = &v
}

// GetUnread returns the Unread field value if set, zero value otherwise.
func (o *NotificationThread) GetUnread() bool {
	if o == nil || o.Unread == nil {
		var ret bool
		return ret
	}
	return *o.Unread
}

// GetUnreadOk returns a tuple with the Unread field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetUnreadOk() (*bool, bool) {
	if o == nil || o.Unread == nil {
		return nil, false
	}
	return o.Unread, true
}

// HasUnread returns a boolean if a field has been set.
func (o *NotificationThread) HasUnread() bool {
	if o != nil && o.Unread != nil {
		return true
	}

	return false
}

// SetUnread gets a reference to the given bool and assigns it to the Unread field.
func (o *NotificationThread) SetUnread(v bool) {
	o.Unread = &v
}

// GetUpdatedAt returns the UpdatedAt field value if set, zero value otherwise.
func (o *NotificationThread) GetUpdatedAt() time.Time {
	if o == nil || o.UpdatedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.UpdatedAt
}

// GetUpdatedAtOk returns a tuple with the UpdatedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetUpdatedAtOk() (*time.Time, bool) {
	if o == nil || o.UpdatedAt == nil {
		return nil, false
	}
	return o.UpdatedAt, true
}

// HasUpdatedAt returns a boolean if a field has been set.
func (o *NotificationThread) HasUpdatedAt() bool {
	if o != nil && o.UpdatedAt != nil {
		return true
	}

	return false
}

// SetUpdatedAt gets a reference to the given time.Time and assigns it to the UpdatedAt field.
func (o *NotificationThread) SetUpdatedAt(v time.Time) {
	o.UpdatedAt = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *NotificationThread) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *NotificationThread) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *NotificationThread) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *NotificationThread) SetUrl(v string) {
	o.Url = &v
}

func (o NotificationThread) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Id != nil {
		toSerialize["id"] = o.Id
	}
	if o.Pinned != nil {
		toSerialize["pinned"] = o.Pinned
	}
	if o.Repository != nil {
		toSerialize["repository"] = o.Repository
	}
	if o.Subject != nil {
		toSerialize["subject"] = o.Subject
	}
	if o.Unread != nil {
		toSerialize["unread"] = o.Unread
	}
	if o.UpdatedAt != nil {
		toSerialize["updated_at"] = o.UpdatedAt
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	return json.Marshal(toSerialize)
}

type NullableNotificationThread struct {
	value *NotificationThread
	isSet bool
}

func (v NullableNotificationThread) Get() *NotificationThread {
	return v.value
}

func (v *NullableNotificationThread) Set(val *NotificationThread) {
	v.value = val
	v.isSet = true
}

func (v NullableNotificationThread) IsSet() bool {
	return v.isSet
}

func (v *NullableNotificationThread) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableNotificationThread(val *NotificationThread) *NullableNotificationThread {
	return &NullableNotificationThread{value: val, isSet: true}
}

func (v NullableNotificationThread) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableNotificationThread) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



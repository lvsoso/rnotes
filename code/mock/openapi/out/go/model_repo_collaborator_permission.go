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

// RepoCollaboratorPermission RepoCollaboratorPermission to get repository permission for a collaborator
type RepoCollaboratorPermission struct {
	Permission *string `json:"permission,omitempty"`
	RoleName *string `json:"role_name,omitempty"`
	User *User `json:"user,omitempty"`
}

// NewRepoCollaboratorPermission instantiates a new RepoCollaboratorPermission object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewRepoCollaboratorPermission() *RepoCollaboratorPermission {
	this := RepoCollaboratorPermission{}
	return &this
}

// NewRepoCollaboratorPermissionWithDefaults instantiates a new RepoCollaboratorPermission object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewRepoCollaboratorPermissionWithDefaults() *RepoCollaboratorPermission {
	this := RepoCollaboratorPermission{}
	return &this
}

// GetPermission returns the Permission field value if set, zero value otherwise.
func (o *RepoCollaboratorPermission) GetPermission() string {
	if o == nil || o.Permission == nil {
		var ret string
		return ret
	}
	return *o.Permission
}

// GetPermissionOk returns a tuple with the Permission field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *RepoCollaboratorPermission) GetPermissionOk() (*string, bool) {
	if o == nil || o.Permission == nil {
		return nil, false
	}
	return o.Permission, true
}

// HasPermission returns a boolean if a field has been set.
func (o *RepoCollaboratorPermission) HasPermission() bool {
	if o != nil && o.Permission != nil {
		return true
	}

	return false
}

// SetPermission gets a reference to the given string and assigns it to the Permission field.
func (o *RepoCollaboratorPermission) SetPermission(v string) {
	o.Permission = &v
}

// GetRoleName returns the RoleName field value if set, zero value otherwise.
func (o *RepoCollaboratorPermission) GetRoleName() string {
	if o == nil || o.RoleName == nil {
		var ret string
		return ret
	}
	return *o.RoleName
}

// GetRoleNameOk returns a tuple with the RoleName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *RepoCollaboratorPermission) GetRoleNameOk() (*string, bool) {
	if o == nil || o.RoleName == nil {
		return nil, false
	}
	return o.RoleName, true
}

// HasRoleName returns a boolean if a field has been set.
func (o *RepoCollaboratorPermission) HasRoleName() bool {
	if o != nil && o.RoleName != nil {
		return true
	}

	return false
}

// SetRoleName gets a reference to the given string and assigns it to the RoleName field.
func (o *RepoCollaboratorPermission) SetRoleName(v string) {
	o.RoleName = &v
}

// GetUser returns the User field value if set, zero value otherwise.
func (o *RepoCollaboratorPermission) GetUser() User {
	if o == nil || o.User == nil {
		var ret User
		return ret
	}
	return *o.User
}

// GetUserOk returns a tuple with the User field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *RepoCollaboratorPermission) GetUserOk() (*User, bool) {
	if o == nil || o.User == nil {
		return nil, false
	}
	return o.User, true
}

// HasUser returns a boolean if a field has been set.
func (o *RepoCollaboratorPermission) HasUser() bool {
	if o != nil && o.User != nil {
		return true
	}

	return false
}

// SetUser gets a reference to the given User and assigns it to the User field.
func (o *RepoCollaboratorPermission) SetUser(v User) {
	o.User = &v
}

func (o RepoCollaboratorPermission) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Permission != nil {
		toSerialize["permission"] = o.Permission
	}
	if o.RoleName != nil {
		toSerialize["role_name"] = o.RoleName
	}
	if o.User != nil {
		toSerialize["user"] = o.User
	}
	return json.Marshal(toSerialize)
}

type NullableRepoCollaboratorPermission struct {
	value *RepoCollaboratorPermission
	isSet bool
}

func (v NullableRepoCollaboratorPermission) Get() *RepoCollaboratorPermission {
	return v.value
}

func (v *NullableRepoCollaboratorPermission) Set(val *RepoCollaboratorPermission) {
	v.value = val
	v.isSet = true
}

func (v NullableRepoCollaboratorPermission) IsSet() bool {
	return v.isSet
}

func (v *NullableRepoCollaboratorPermission) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableRepoCollaboratorPermission(val *RepoCollaboratorPermission) *NullableRepoCollaboratorPermission {
	return &NullableRepoCollaboratorPermission{value: val, isSet: true}
}

func (v NullableRepoCollaboratorPermission) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableRepoCollaboratorPermission) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



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

// Package Package represents a package
type Package struct {
	CreatedAt *time.Time `json:"created_at,omitempty"`
	Creator *User `json:"creator,omitempty"`
	HtmlUrl *string `json:"html_url,omitempty"`
	Id *int64 `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Owner *User `json:"owner,omitempty"`
	Repository *Repository `json:"repository,omitempty"`
	Type *string `json:"type,omitempty"`
	Version *string `json:"version,omitempty"`
}

// NewPackage instantiates a new Package object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPackage() *Package {
	this := Package{}
	return &this
}

// NewPackageWithDefaults instantiates a new Package object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPackageWithDefaults() *Package {
	this := Package{}
	return &this
}

// GetCreatedAt returns the CreatedAt field value if set, zero value otherwise.
func (o *Package) GetCreatedAt() time.Time {
	if o == nil || o.CreatedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.CreatedAt
}

// GetCreatedAtOk returns a tuple with the CreatedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetCreatedAtOk() (*time.Time, bool) {
	if o == nil || o.CreatedAt == nil {
		return nil, false
	}
	return o.CreatedAt, true
}

// HasCreatedAt returns a boolean if a field has been set.
func (o *Package) HasCreatedAt() bool {
	if o != nil && o.CreatedAt != nil {
		return true
	}

	return false
}

// SetCreatedAt gets a reference to the given time.Time and assigns it to the CreatedAt field.
func (o *Package) SetCreatedAt(v time.Time) {
	o.CreatedAt = &v
}

// GetCreator returns the Creator field value if set, zero value otherwise.
func (o *Package) GetCreator() User {
	if o == nil || o.Creator == nil {
		var ret User
		return ret
	}
	return *o.Creator
}

// GetCreatorOk returns a tuple with the Creator field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetCreatorOk() (*User, bool) {
	if o == nil || o.Creator == nil {
		return nil, false
	}
	return o.Creator, true
}

// HasCreator returns a boolean if a field has been set.
func (o *Package) HasCreator() bool {
	if o != nil && o.Creator != nil {
		return true
	}

	return false
}

// SetCreator gets a reference to the given User and assigns it to the Creator field.
func (o *Package) SetCreator(v User) {
	o.Creator = &v
}

// GetHtmlUrl returns the HtmlUrl field value if set, zero value otherwise.
func (o *Package) GetHtmlUrl() string {
	if o == nil || o.HtmlUrl == nil {
		var ret string
		return ret
	}
	return *o.HtmlUrl
}

// GetHtmlUrlOk returns a tuple with the HtmlUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetHtmlUrlOk() (*string, bool) {
	if o == nil || o.HtmlUrl == nil {
		return nil, false
	}
	return o.HtmlUrl, true
}

// HasHtmlUrl returns a boolean if a field has been set.
func (o *Package) HasHtmlUrl() bool {
	if o != nil && o.HtmlUrl != nil {
		return true
	}

	return false
}

// SetHtmlUrl gets a reference to the given string and assigns it to the HtmlUrl field.
func (o *Package) SetHtmlUrl(v string) {
	o.HtmlUrl = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Package) GetId() int64 {
	if o == nil || o.Id == nil {
		var ret int64
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetIdOk() (*int64, bool) {
	if o == nil || o.Id == nil {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Package) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given int64 and assigns it to the Id field.
func (o *Package) SetId(v int64) {
	o.Id = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Package) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Package) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Package) SetName(v string) {
	o.Name = &v
}

// GetOwner returns the Owner field value if set, zero value otherwise.
func (o *Package) GetOwner() User {
	if o == nil || o.Owner == nil {
		var ret User
		return ret
	}
	return *o.Owner
}

// GetOwnerOk returns a tuple with the Owner field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetOwnerOk() (*User, bool) {
	if o == nil || o.Owner == nil {
		return nil, false
	}
	return o.Owner, true
}

// HasOwner returns a boolean if a field has been set.
func (o *Package) HasOwner() bool {
	if o != nil && o.Owner != nil {
		return true
	}

	return false
}

// SetOwner gets a reference to the given User and assigns it to the Owner field.
func (o *Package) SetOwner(v User) {
	o.Owner = &v
}

// GetRepository returns the Repository field value if set, zero value otherwise.
func (o *Package) GetRepository() Repository {
	if o == nil || o.Repository == nil {
		var ret Repository
		return ret
	}
	return *o.Repository
}

// GetRepositoryOk returns a tuple with the Repository field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetRepositoryOk() (*Repository, bool) {
	if o == nil || o.Repository == nil {
		return nil, false
	}
	return o.Repository, true
}

// HasRepository returns a boolean if a field has been set.
func (o *Package) HasRepository() bool {
	if o != nil && o.Repository != nil {
		return true
	}

	return false
}

// SetRepository gets a reference to the given Repository and assigns it to the Repository field.
func (o *Package) SetRepository(v Repository) {
	o.Repository = &v
}

// GetType returns the Type field value if set, zero value otherwise.
func (o *Package) GetType() string {
	if o == nil || o.Type == nil {
		var ret string
		return ret
	}
	return *o.Type
}

// GetTypeOk returns a tuple with the Type field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetTypeOk() (*string, bool) {
	if o == nil || o.Type == nil {
		return nil, false
	}
	return o.Type, true
}

// HasType returns a boolean if a field has been set.
func (o *Package) HasType() bool {
	if o != nil && o.Type != nil {
		return true
	}

	return false
}

// SetType gets a reference to the given string and assigns it to the Type field.
func (o *Package) SetType(v string) {
	o.Type = &v
}

// GetVersion returns the Version field value if set, zero value otherwise.
func (o *Package) GetVersion() string {
	if o == nil || o.Version == nil {
		var ret string
		return ret
	}
	return *o.Version
}

// GetVersionOk returns a tuple with the Version field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Package) GetVersionOk() (*string, bool) {
	if o == nil || o.Version == nil {
		return nil, false
	}
	return o.Version, true
}

// HasVersion returns a boolean if a field has been set.
func (o *Package) HasVersion() bool {
	if o != nil && o.Version != nil {
		return true
	}

	return false
}

// SetVersion gets a reference to the given string and assigns it to the Version field.
func (o *Package) SetVersion(v string) {
	o.Version = &v
}

func (o Package) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.CreatedAt != nil {
		toSerialize["created_at"] = o.CreatedAt
	}
	if o.Creator != nil {
		toSerialize["creator"] = o.Creator
	}
	if o.HtmlUrl != nil {
		toSerialize["html_url"] = o.HtmlUrl
	}
	if o.Id != nil {
		toSerialize["id"] = o.Id
	}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.Owner != nil {
		toSerialize["owner"] = o.Owner
	}
	if o.Repository != nil {
		toSerialize["repository"] = o.Repository
	}
	if o.Type != nil {
		toSerialize["type"] = o.Type
	}
	if o.Version != nil {
		toSerialize["version"] = o.Version
	}
	return json.Marshal(toSerialize)
}

type NullablePackage struct {
	value *Package
	isSet bool
}

func (v NullablePackage) Get() *Package {
	return v.value
}

func (v *NullablePackage) Set(val *Package) {
	v.value = val
	v.isSet = true
}

func (v NullablePackage) IsSet() bool {
	return v.isSet
}

func (v *NullablePackage) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePackage(val *Package) *NullablePackage {
	return &NullablePackage{value: val, isSet: true}
}

func (v NullablePackage) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePackage) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



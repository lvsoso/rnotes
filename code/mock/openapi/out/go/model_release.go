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

// Release Release represents a repository release
type Release struct {
	Assets *[]Attachment `json:"assets,omitempty"`
	Author *User `json:"author,omitempty"`
	Body *string `json:"body,omitempty"`
	CreatedAt *time.Time `json:"created_at,omitempty"`
	Draft *bool `json:"draft,omitempty"`
	HtmlUrl *string `json:"html_url,omitempty"`
	Id *int64 `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Prerelease *bool `json:"prerelease,omitempty"`
	PublishedAt *time.Time `json:"published_at,omitempty"`
	TagName *string `json:"tag_name,omitempty"`
	TarballUrl *string `json:"tarball_url,omitempty"`
	TargetCommitish *string `json:"target_commitish,omitempty"`
	UploadUrl *string `json:"upload_url,omitempty"`
	Url *string `json:"url,omitempty"`
	ZipballUrl *string `json:"zipball_url,omitempty"`
}

// NewRelease instantiates a new Release object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewRelease() *Release {
	this := Release{}
	return &this
}

// NewReleaseWithDefaults instantiates a new Release object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewReleaseWithDefaults() *Release {
	this := Release{}
	return &this
}

// GetAssets returns the Assets field value if set, zero value otherwise.
func (o *Release) GetAssets() []Attachment {
	if o == nil || o.Assets == nil {
		var ret []Attachment
		return ret
	}
	return *o.Assets
}

// GetAssetsOk returns a tuple with the Assets field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetAssetsOk() (*[]Attachment, bool) {
	if o == nil || o.Assets == nil {
		return nil, false
	}
	return o.Assets, true
}

// HasAssets returns a boolean if a field has been set.
func (o *Release) HasAssets() bool {
	if o != nil && o.Assets != nil {
		return true
	}

	return false
}

// SetAssets gets a reference to the given []Attachment and assigns it to the Assets field.
func (o *Release) SetAssets(v []Attachment) {
	o.Assets = &v
}

// GetAuthor returns the Author field value if set, zero value otherwise.
func (o *Release) GetAuthor() User {
	if o == nil || o.Author == nil {
		var ret User
		return ret
	}
	return *o.Author
}

// GetAuthorOk returns a tuple with the Author field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetAuthorOk() (*User, bool) {
	if o == nil || o.Author == nil {
		return nil, false
	}
	return o.Author, true
}

// HasAuthor returns a boolean if a field has been set.
func (o *Release) HasAuthor() bool {
	if o != nil && o.Author != nil {
		return true
	}

	return false
}

// SetAuthor gets a reference to the given User and assigns it to the Author field.
func (o *Release) SetAuthor(v User) {
	o.Author = &v
}

// GetBody returns the Body field value if set, zero value otherwise.
func (o *Release) GetBody() string {
	if o == nil || o.Body == nil {
		var ret string
		return ret
	}
	return *o.Body
}

// GetBodyOk returns a tuple with the Body field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetBodyOk() (*string, bool) {
	if o == nil || o.Body == nil {
		return nil, false
	}
	return o.Body, true
}

// HasBody returns a boolean if a field has been set.
func (o *Release) HasBody() bool {
	if o != nil && o.Body != nil {
		return true
	}

	return false
}

// SetBody gets a reference to the given string and assigns it to the Body field.
func (o *Release) SetBody(v string) {
	o.Body = &v
}

// GetCreatedAt returns the CreatedAt field value if set, zero value otherwise.
func (o *Release) GetCreatedAt() time.Time {
	if o == nil || o.CreatedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.CreatedAt
}

// GetCreatedAtOk returns a tuple with the CreatedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetCreatedAtOk() (*time.Time, bool) {
	if o == nil || o.CreatedAt == nil {
		return nil, false
	}
	return o.CreatedAt, true
}

// HasCreatedAt returns a boolean if a field has been set.
func (o *Release) HasCreatedAt() bool {
	if o != nil && o.CreatedAt != nil {
		return true
	}

	return false
}

// SetCreatedAt gets a reference to the given time.Time and assigns it to the CreatedAt field.
func (o *Release) SetCreatedAt(v time.Time) {
	o.CreatedAt = &v
}

// GetDraft returns the Draft field value if set, zero value otherwise.
func (o *Release) GetDraft() bool {
	if o == nil || o.Draft == nil {
		var ret bool
		return ret
	}
	return *o.Draft
}

// GetDraftOk returns a tuple with the Draft field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetDraftOk() (*bool, bool) {
	if o == nil || o.Draft == nil {
		return nil, false
	}
	return o.Draft, true
}

// HasDraft returns a boolean if a field has been set.
func (o *Release) HasDraft() bool {
	if o != nil && o.Draft != nil {
		return true
	}

	return false
}

// SetDraft gets a reference to the given bool and assigns it to the Draft field.
func (o *Release) SetDraft(v bool) {
	o.Draft = &v
}

// GetHtmlUrl returns the HtmlUrl field value if set, zero value otherwise.
func (o *Release) GetHtmlUrl() string {
	if o == nil || o.HtmlUrl == nil {
		var ret string
		return ret
	}
	return *o.HtmlUrl
}

// GetHtmlUrlOk returns a tuple with the HtmlUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetHtmlUrlOk() (*string, bool) {
	if o == nil || o.HtmlUrl == nil {
		return nil, false
	}
	return o.HtmlUrl, true
}

// HasHtmlUrl returns a boolean if a field has been set.
func (o *Release) HasHtmlUrl() bool {
	if o != nil && o.HtmlUrl != nil {
		return true
	}

	return false
}

// SetHtmlUrl gets a reference to the given string and assigns it to the HtmlUrl field.
func (o *Release) SetHtmlUrl(v string) {
	o.HtmlUrl = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Release) GetId() int64 {
	if o == nil || o.Id == nil {
		var ret int64
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetIdOk() (*int64, bool) {
	if o == nil || o.Id == nil {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Release) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given int64 and assigns it to the Id field.
func (o *Release) SetId(v int64) {
	o.Id = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Release) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Release) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Release) SetName(v string) {
	o.Name = &v
}

// GetPrerelease returns the Prerelease field value if set, zero value otherwise.
func (o *Release) GetPrerelease() bool {
	if o == nil || o.Prerelease == nil {
		var ret bool
		return ret
	}
	return *o.Prerelease
}

// GetPrereleaseOk returns a tuple with the Prerelease field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetPrereleaseOk() (*bool, bool) {
	if o == nil || o.Prerelease == nil {
		return nil, false
	}
	return o.Prerelease, true
}

// HasPrerelease returns a boolean if a field has been set.
func (o *Release) HasPrerelease() bool {
	if o != nil && o.Prerelease != nil {
		return true
	}

	return false
}

// SetPrerelease gets a reference to the given bool and assigns it to the Prerelease field.
func (o *Release) SetPrerelease(v bool) {
	o.Prerelease = &v
}

// GetPublishedAt returns the PublishedAt field value if set, zero value otherwise.
func (o *Release) GetPublishedAt() time.Time {
	if o == nil || o.PublishedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.PublishedAt
}

// GetPublishedAtOk returns a tuple with the PublishedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetPublishedAtOk() (*time.Time, bool) {
	if o == nil || o.PublishedAt == nil {
		return nil, false
	}
	return o.PublishedAt, true
}

// HasPublishedAt returns a boolean if a field has been set.
func (o *Release) HasPublishedAt() bool {
	if o != nil && o.PublishedAt != nil {
		return true
	}

	return false
}

// SetPublishedAt gets a reference to the given time.Time and assigns it to the PublishedAt field.
func (o *Release) SetPublishedAt(v time.Time) {
	o.PublishedAt = &v
}

// GetTagName returns the TagName field value if set, zero value otherwise.
func (o *Release) GetTagName() string {
	if o == nil || o.TagName == nil {
		var ret string
		return ret
	}
	return *o.TagName
}

// GetTagNameOk returns a tuple with the TagName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetTagNameOk() (*string, bool) {
	if o == nil || o.TagName == nil {
		return nil, false
	}
	return o.TagName, true
}

// HasTagName returns a boolean if a field has been set.
func (o *Release) HasTagName() bool {
	if o != nil && o.TagName != nil {
		return true
	}

	return false
}

// SetTagName gets a reference to the given string and assigns it to the TagName field.
func (o *Release) SetTagName(v string) {
	o.TagName = &v
}

// GetTarballUrl returns the TarballUrl field value if set, zero value otherwise.
func (o *Release) GetTarballUrl() string {
	if o == nil || o.TarballUrl == nil {
		var ret string
		return ret
	}
	return *o.TarballUrl
}

// GetTarballUrlOk returns a tuple with the TarballUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetTarballUrlOk() (*string, bool) {
	if o == nil || o.TarballUrl == nil {
		return nil, false
	}
	return o.TarballUrl, true
}

// HasTarballUrl returns a boolean if a field has been set.
func (o *Release) HasTarballUrl() bool {
	if o != nil && o.TarballUrl != nil {
		return true
	}

	return false
}

// SetTarballUrl gets a reference to the given string and assigns it to the TarballUrl field.
func (o *Release) SetTarballUrl(v string) {
	o.TarballUrl = &v
}

// GetTargetCommitish returns the TargetCommitish field value if set, zero value otherwise.
func (o *Release) GetTargetCommitish() string {
	if o == nil || o.TargetCommitish == nil {
		var ret string
		return ret
	}
	return *o.TargetCommitish
}

// GetTargetCommitishOk returns a tuple with the TargetCommitish field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetTargetCommitishOk() (*string, bool) {
	if o == nil || o.TargetCommitish == nil {
		return nil, false
	}
	return o.TargetCommitish, true
}

// HasTargetCommitish returns a boolean if a field has been set.
func (o *Release) HasTargetCommitish() bool {
	if o != nil && o.TargetCommitish != nil {
		return true
	}

	return false
}

// SetTargetCommitish gets a reference to the given string and assigns it to the TargetCommitish field.
func (o *Release) SetTargetCommitish(v string) {
	o.TargetCommitish = &v
}

// GetUploadUrl returns the UploadUrl field value if set, zero value otherwise.
func (o *Release) GetUploadUrl() string {
	if o == nil || o.UploadUrl == nil {
		var ret string
		return ret
	}
	return *o.UploadUrl
}

// GetUploadUrlOk returns a tuple with the UploadUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetUploadUrlOk() (*string, bool) {
	if o == nil || o.UploadUrl == nil {
		return nil, false
	}
	return o.UploadUrl, true
}

// HasUploadUrl returns a boolean if a field has been set.
func (o *Release) HasUploadUrl() bool {
	if o != nil && o.UploadUrl != nil {
		return true
	}

	return false
}

// SetUploadUrl gets a reference to the given string and assigns it to the UploadUrl field.
func (o *Release) SetUploadUrl(v string) {
	o.UploadUrl = &v
}

// GetUrl returns the Url field value if set, zero value otherwise.
func (o *Release) GetUrl() string {
	if o == nil || o.Url == nil {
		var ret string
		return ret
	}
	return *o.Url
}

// GetUrlOk returns a tuple with the Url field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetUrlOk() (*string, bool) {
	if o == nil || o.Url == nil {
		return nil, false
	}
	return o.Url, true
}

// HasUrl returns a boolean if a field has been set.
func (o *Release) HasUrl() bool {
	if o != nil && o.Url != nil {
		return true
	}

	return false
}

// SetUrl gets a reference to the given string and assigns it to the Url field.
func (o *Release) SetUrl(v string) {
	o.Url = &v
}

// GetZipballUrl returns the ZipballUrl field value if set, zero value otherwise.
func (o *Release) GetZipballUrl() string {
	if o == nil || o.ZipballUrl == nil {
		var ret string
		return ret
	}
	return *o.ZipballUrl
}

// GetZipballUrlOk returns a tuple with the ZipballUrl field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Release) GetZipballUrlOk() (*string, bool) {
	if o == nil || o.ZipballUrl == nil {
		return nil, false
	}
	return o.ZipballUrl, true
}

// HasZipballUrl returns a boolean if a field has been set.
func (o *Release) HasZipballUrl() bool {
	if o != nil && o.ZipballUrl != nil {
		return true
	}

	return false
}

// SetZipballUrl gets a reference to the given string and assigns it to the ZipballUrl field.
func (o *Release) SetZipballUrl(v string) {
	o.ZipballUrl = &v
}

func (o Release) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Assets != nil {
		toSerialize["assets"] = o.Assets
	}
	if o.Author != nil {
		toSerialize["author"] = o.Author
	}
	if o.Body != nil {
		toSerialize["body"] = o.Body
	}
	if o.CreatedAt != nil {
		toSerialize["created_at"] = o.CreatedAt
	}
	if o.Draft != nil {
		toSerialize["draft"] = o.Draft
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
	if o.Prerelease != nil {
		toSerialize["prerelease"] = o.Prerelease
	}
	if o.PublishedAt != nil {
		toSerialize["published_at"] = o.PublishedAt
	}
	if o.TagName != nil {
		toSerialize["tag_name"] = o.TagName
	}
	if o.TarballUrl != nil {
		toSerialize["tarball_url"] = o.TarballUrl
	}
	if o.TargetCommitish != nil {
		toSerialize["target_commitish"] = o.TargetCommitish
	}
	if o.UploadUrl != nil {
		toSerialize["upload_url"] = o.UploadUrl
	}
	if o.Url != nil {
		toSerialize["url"] = o.Url
	}
	if o.ZipballUrl != nil {
		toSerialize["zipball_url"] = o.ZipballUrl
	}
	return json.Marshal(toSerialize)
}

type NullableRelease struct {
	value *Release
	isSet bool
}

func (v NullableRelease) Get() *Release {
	return v.value
}

func (v *NullableRelease) Set(val *Release) {
	v.value = val
	v.isSet = true
}

func (v NullableRelease) IsSet() bool {
	return v.isSet
}

func (v *NullableRelease) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableRelease(val *Release) *NullableRelease {
	return &NullableRelease{value: val, isSet: true}
}

func (v NullableRelease) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableRelease) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



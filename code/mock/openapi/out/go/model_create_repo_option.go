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

// CreateRepoOption CreateRepoOption options when creating repository
type CreateRepoOption struct {
	// Whether the repository should be auto-initialized?
	AutoInit *bool `json:"auto_init,omitempty"`
	// DefaultBranch of the repository (used when initializes and in template)
	DefaultBranch *string `json:"default_branch,omitempty"`
	// Description of the repository to create
	Description *string `json:"description,omitempty"`
	// Gitignores to use
	Gitignores *string `json:"gitignores,omitempty"`
	// Label-Set to use
	IssueLabels *string `json:"issue_labels,omitempty"`
	// License to use
	License *string `json:"license,omitempty"`
	// Name of the repository to create
	Name string `json:"name"`
	// ObjectFormatName of the underlying git repository
	ObjectFormatName *string `json:"object_format_name,omitempty"`
	// Whether the repository is private
	Private *bool `json:"private,omitempty"`
	// Readme of the repository to create
	Readme *string `json:"readme,omitempty"`
	// Whether the repository is template
	Template *bool `json:"template,omitempty"`
	// TrustModel of the repository
	TrustModel *string `json:"trust_model,omitempty"`
}

// NewCreateRepoOption instantiates a new CreateRepoOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateRepoOption(name string) *CreateRepoOption {
	this := CreateRepoOption{}
	this.Name = name
	return &this
}

// NewCreateRepoOptionWithDefaults instantiates a new CreateRepoOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateRepoOptionWithDefaults() *CreateRepoOption {
	this := CreateRepoOption{}
	return &this
}

// GetAutoInit returns the AutoInit field value if set, zero value otherwise.
func (o *CreateRepoOption) GetAutoInit() bool {
	if o == nil || o.AutoInit == nil {
		var ret bool
		return ret
	}
	return *o.AutoInit
}

// GetAutoInitOk returns a tuple with the AutoInit field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetAutoInitOk() (*bool, bool) {
	if o == nil || o.AutoInit == nil {
		return nil, false
	}
	return o.AutoInit, true
}

// HasAutoInit returns a boolean if a field has been set.
func (o *CreateRepoOption) HasAutoInit() bool {
	if o != nil && o.AutoInit != nil {
		return true
	}

	return false
}

// SetAutoInit gets a reference to the given bool and assigns it to the AutoInit field.
func (o *CreateRepoOption) SetAutoInit(v bool) {
	o.AutoInit = &v
}

// GetDefaultBranch returns the DefaultBranch field value if set, zero value otherwise.
func (o *CreateRepoOption) GetDefaultBranch() string {
	if o == nil || o.DefaultBranch == nil {
		var ret string
		return ret
	}
	return *o.DefaultBranch
}

// GetDefaultBranchOk returns a tuple with the DefaultBranch field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetDefaultBranchOk() (*string, bool) {
	if o == nil || o.DefaultBranch == nil {
		return nil, false
	}
	return o.DefaultBranch, true
}

// HasDefaultBranch returns a boolean if a field has been set.
func (o *CreateRepoOption) HasDefaultBranch() bool {
	if o != nil && o.DefaultBranch != nil {
		return true
	}

	return false
}

// SetDefaultBranch gets a reference to the given string and assigns it to the DefaultBranch field.
func (o *CreateRepoOption) SetDefaultBranch(v string) {
	o.DefaultBranch = &v
}

// GetDescription returns the Description field value if set, zero value otherwise.
func (o *CreateRepoOption) GetDescription() string {
	if o == nil || o.Description == nil {
		var ret string
		return ret
	}
	return *o.Description
}

// GetDescriptionOk returns a tuple with the Description field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetDescriptionOk() (*string, bool) {
	if o == nil || o.Description == nil {
		return nil, false
	}
	return o.Description, true
}

// HasDescription returns a boolean if a field has been set.
func (o *CreateRepoOption) HasDescription() bool {
	if o != nil && o.Description != nil {
		return true
	}

	return false
}

// SetDescription gets a reference to the given string and assigns it to the Description field.
func (o *CreateRepoOption) SetDescription(v string) {
	o.Description = &v
}

// GetGitignores returns the Gitignores field value if set, zero value otherwise.
func (o *CreateRepoOption) GetGitignores() string {
	if o == nil || o.Gitignores == nil {
		var ret string
		return ret
	}
	return *o.Gitignores
}

// GetGitignoresOk returns a tuple with the Gitignores field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetGitignoresOk() (*string, bool) {
	if o == nil || o.Gitignores == nil {
		return nil, false
	}
	return o.Gitignores, true
}

// HasGitignores returns a boolean if a field has been set.
func (o *CreateRepoOption) HasGitignores() bool {
	if o != nil && o.Gitignores != nil {
		return true
	}

	return false
}

// SetGitignores gets a reference to the given string and assigns it to the Gitignores field.
func (o *CreateRepoOption) SetGitignores(v string) {
	o.Gitignores = &v
}

// GetIssueLabels returns the IssueLabels field value if set, zero value otherwise.
func (o *CreateRepoOption) GetIssueLabels() string {
	if o == nil || o.IssueLabels == nil {
		var ret string
		return ret
	}
	return *o.IssueLabels
}

// GetIssueLabelsOk returns a tuple with the IssueLabels field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetIssueLabelsOk() (*string, bool) {
	if o == nil || o.IssueLabels == nil {
		return nil, false
	}
	return o.IssueLabels, true
}

// HasIssueLabels returns a boolean if a field has been set.
func (o *CreateRepoOption) HasIssueLabels() bool {
	if o != nil && o.IssueLabels != nil {
		return true
	}

	return false
}

// SetIssueLabels gets a reference to the given string and assigns it to the IssueLabels field.
func (o *CreateRepoOption) SetIssueLabels(v string) {
	o.IssueLabels = &v
}

// GetLicense returns the License field value if set, zero value otherwise.
func (o *CreateRepoOption) GetLicense() string {
	if o == nil || o.License == nil {
		var ret string
		return ret
	}
	return *o.License
}

// GetLicenseOk returns a tuple with the License field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetLicenseOk() (*string, bool) {
	if o == nil || o.License == nil {
		return nil, false
	}
	return o.License, true
}

// HasLicense returns a boolean if a field has been set.
func (o *CreateRepoOption) HasLicense() bool {
	if o != nil && o.License != nil {
		return true
	}

	return false
}

// SetLicense gets a reference to the given string and assigns it to the License field.
func (o *CreateRepoOption) SetLicense(v string) {
	o.License = &v
}

// GetName returns the Name field value
func (o *CreateRepoOption) GetName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Name
}

// GetNameOk returns a tuple with the Name field value
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetNameOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Name, true
}

// SetName sets field value
func (o *CreateRepoOption) SetName(v string) {
	o.Name = v
}

// GetObjectFormatName returns the ObjectFormatName field value if set, zero value otherwise.
func (o *CreateRepoOption) GetObjectFormatName() string {
	if o == nil || o.ObjectFormatName == nil {
		var ret string
		return ret
	}
	return *o.ObjectFormatName
}

// GetObjectFormatNameOk returns a tuple with the ObjectFormatName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetObjectFormatNameOk() (*string, bool) {
	if o == nil || o.ObjectFormatName == nil {
		return nil, false
	}
	return o.ObjectFormatName, true
}

// HasObjectFormatName returns a boolean if a field has been set.
func (o *CreateRepoOption) HasObjectFormatName() bool {
	if o != nil && o.ObjectFormatName != nil {
		return true
	}

	return false
}

// SetObjectFormatName gets a reference to the given string and assigns it to the ObjectFormatName field.
func (o *CreateRepoOption) SetObjectFormatName(v string) {
	o.ObjectFormatName = &v
}

// GetPrivate returns the Private field value if set, zero value otherwise.
func (o *CreateRepoOption) GetPrivate() bool {
	if o == nil || o.Private == nil {
		var ret bool
		return ret
	}
	return *o.Private
}

// GetPrivateOk returns a tuple with the Private field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetPrivateOk() (*bool, bool) {
	if o == nil || o.Private == nil {
		return nil, false
	}
	return o.Private, true
}

// HasPrivate returns a boolean if a field has been set.
func (o *CreateRepoOption) HasPrivate() bool {
	if o != nil && o.Private != nil {
		return true
	}

	return false
}

// SetPrivate gets a reference to the given bool and assigns it to the Private field.
func (o *CreateRepoOption) SetPrivate(v bool) {
	o.Private = &v
}

// GetReadme returns the Readme field value if set, zero value otherwise.
func (o *CreateRepoOption) GetReadme() string {
	if o == nil || o.Readme == nil {
		var ret string
		return ret
	}
	return *o.Readme
}

// GetReadmeOk returns a tuple with the Readme field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetReadmeOk() (*string, bool) {
	if o == nil || o.Readme == nil {
		return nil, false
	}
	return o.Readme, true
}

// HasReadme returns a boolean if a field has been set.
func (o *CreateRepoOption) HasReadme() bool {
	if o != nil && o.Readme != nil {
		return true
	}

	return false
}

// SetReadme gets a reference to the given string and assigns it to the Readme field.
func (o *CreateRepoOption) SetReadme(v string) {
	o.Readme = &v
}

// GetTemplate returns the Template field value if set, zero value otherwise.
func (o *CreateRepoOption) GetTemplate() bool {
	if o == nil || o.Template == nil {
		var ret bool
		return ret
	}
	return *o.Template
}

// GetTemplateOk returns a tuple with the Template field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetTemplateOk() (*bool, bool) {
	if o == nil || o.Template == nil {
		return nil, false
	}
	return o.Template, true
}

// HasTemplate returns a boolean if a field has been set.
func (o *CreateRepoOption) HasTemplate() bool {
	if o != nil && o.Template != nil {
		return true
	}

	return false
}

// SetTemplate gets a reference to the given bool and assigns it to the Template field.
func (o *CreateRepoOption) SetTemplate(v bool) {
	o.Template = &v
}

// GetTrustModel returns the TrustModel field value if set, zero value otherwise.
func (o *CreateRepoOption) GetTrustModel() string {
	if o == nil || o.TrustModel == nil {
		var ret string
		return ret
	}
	return *o.TrustModel
}

// GetTrustModelOk returns a tuple with the TrustModel field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateRepoOption) GetTrustModelOk() (*string, bool) {
	if o == nil || o.TrustModel == nil {
		return nil, false
	}
	return o.TrustModel, true
}

// HasTrustModel returns a boolean if a field has been set.
func (o *CreateRepoOption) HasTrustModel() bool {
	if o != nil && o.TrustModel != nil {
		return true
	}

	return false
}

// SetTrustModel gets a reference to the given string and assigns it to the TrustModel field.
func (o *CreateRepoOption) SetTrustModel(v string) {
	o.TrustModel = &v
}

func (o CreateRepoOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.AutoInit != nil {
		toSerialize["auto_init"] = o.AutoInit
	}
	if o.DefaultBranch != nil {
		toSerialize["default_branch"] = o.DefaultBranch
	}
	if o.Description != nil {
		toSerialize["description"] = o.Description
	}
	if o.Gitignores != nil {
		toSerialize["gitignores"] = o.Gitignores
	}
	if o.IssueLabels != nil {
		toSerialize["issue_labels"] = o.IssueLabels
	}
	if o.License != nil {
		toSerialize["license"] = o.License
	}
	if true {
		toSerialize["name"] = o.Name
	}
	if o.ObjectFormatName != nil {
		toSerialize["object_format_name"] = o.ObjectFormatName
	}
	if o.Private != nil {
		toSerialize["private"] = o.Private
	}
	if o.Readme != nil {
		toSerialize["readme"] = o.Readme
	}
	if o.Template != nil {
		toSerialize["template"] = o.Template
	}
	if o.TrustModel != nil {
		toSerialize["trust_model"] = o.TrustModel
	}
	return json.Marshal(toSerialize)
}

type NullableCreateRepoOption struct {
	value *CreateRepoOption
	isSet bool
}

func (v NullableCreateRepoOption) Get() *CreateRepoOption {
	return v.value
}

func (v *NullableCreateRepoOption) Set(val *CreateRepoOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateRepoOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateRepoOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateRepoOption(val *CreateRepoOption) *NullableCreateRepoOption {
	return &NullableCreateRepoOption{value: val, isSet: true}
}

func (v NullableCreateRepoOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateRepoOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}



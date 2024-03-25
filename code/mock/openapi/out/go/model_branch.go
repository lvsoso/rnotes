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

// Branch Branch represents a repository branch
type Branch struct {
	Commit *PayloadCommit `json:"commit,omitempty"`
	EffectiveBranchProtectionName *string `json:"effective_branch_protection_name,omitempty"`
	EnableStatusCheck *bool `json:"enable_status_check,omitempty"`
	Name *string `json:"name,omitempty"`
	Protected *bool `json:"protected,omitempty"`
	RequiredApprovals *int64 `json:"required_approvals,omitempty"`
	StatusCheckContexts *[]string `json:"status_check_contexts,omitempty"`
	UserCanMerge *bool `json:"user_can_merge,omitempty"`
	UserCanPush *bool `json:"user_can_push,omitempty"`
}

// NewBranch instantiates a new Branch object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewBranch() *Branch {
	this := Branch{}
	return &this
}

// NewBranchWithDefaults instantiates a new Branch object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewBranchWithDefaults() *Branch {
	this := Branch{}
	return &this
}

// GetCommit returns the Commit field value if set, zero value otherwise.
func (o *Branch) GetCommit() PayloadCommit {
	if o == nil || o.Commit == nil {
		var ret PayloadCommit
		return ret
	}
	return *o.Commit
}

// GetCommitOk returns a tuple with the Commit field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetCommitOk() (*PayloadCommit, bool) {
	if o == nil || o.Commit == nil {
		return nil, false
	}
	return o.Commit, true
}

// HasCommit returns a boolean if a field has been set.
func (o *Branch) HasCommit() bool {
	if o != nil && o.Commit != nil {
		return true
	}

	return false
}

// SetCommit gets a reference to the given PayloadCommit and assigns it to the Commit field.
func (o *Branch) SetCommit(v PayloadCommit) {
	o.Commit = &v
}

// GetEffectiveBranchProtectionName returns the EffectiveBranchProtectionName field value if set, zero value otherwise.
func (o *Branch) GetEffectiveBranchProtectionName() string {
	if o == nil || o.EffectiveBranchProtectionName == nil {
		var ret string
		return ret
	}
	return *o.EffectiveBranchProtectionName
}

// GetEffectiveBranchProtectionNameOk returns a tuple with the EffectiveBranchProtectionName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetEffectiveBranchProtectionNameOk() (*string, bool) {
	if o == nil || o.EffectiveBranchProtectionName == nil {
		return nil, false
	}
	return o.EffectiveBranchProtectionName, true
}

// HasEffectiveBranchProtectionName returns a boolean if a field has been set.
func (o *Branch) HasEffectiveBranchProtectionName() bool {
	if o != nil && o.EffectiveBranchProtectionName != nil {
		return true
	}

	return false
}

// SetEffectiveBranchProtectionName gets a reference to the given string and assigns it to the EffectiveBranchProtectionName field.
func (o *Branch) SetEffectiveBranchProtectionName(v string) {
	o.EffectiveBranchProtectionName = &v
}

// GetEnableStatusCheck returns the EnableStatusCheck field value if set, zero value otherwise.
func (o *Branch) GetEnableStatusCheck() bool {
	if o == nil || o.EnableStatusCheck == nil {
		var ret bool
		return ret
	}
	return *o.EnableStatusCheck
}

// GetEnableStatusCheckOk returns a tuple with the EnableStatusCheck field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetEnableStatusCheckOk() (*bool, bool) {
	if o == nil || o.EnableStatusCheck == nil {
		return nil, false
	}
	return o.EnableStatusCheck, true
}

// HasEnableStatusCheck returns a boolean if a field has been set.
func (o *Branch) HasEnableStatusCheck() bool {
	if o != nil && o.EnableStatusCheck != nil {
		return true
	}

	return false
}

// SetEnableStatusCheck gets a reference to the given bool and assigns it to the EnableStatusCheck field.
func (o *Branch) SetEnableStatusCheck(v bool) {
	o.EnableStatusCheck = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Branch) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Branch) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Branch) SetName(v string) {
	o.Name = &v
}

// GetProtected returns the Protected field value if set, zero value otherwise.
func (o *Branch) GetProtected() bool {
	if o == nil || o.Protected == nil {
		var ret bool
		return ret
	}
	return *o.Protected
}

// GetProtectedOk returns a tuple with the Protected field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetProtectedOk() (*bool, bool) {
	if o == nil || o.Protected == nil {
		return nil, false
	}
	return o.Protected, true
}

// HasProtected returns a boolean if a field has been set.
func (o *Branch) HasProtected() bool {
	if o != nil && o.Protected != nil {
		return true
	}

	return false
}

// SetProtected gets a reference to the given bool and assigns it to the Protected field.
func (o *Branch) SetProtected(v bool) {
	o.Protected = &v
}

// GetRequiredApprovals returns the RequiredApprovals field value if set, zero value otherwise.
func (o *Branch) GetRequiredApprovals() int64 {
	if o == nil || o.RequiredApprovals == nil {
		var ret int64
		return ret
	}
	return *o.RequiredApprovals
}

// GetRequiredApprovalsOk returns a tuple with the RequiredApprovals field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetRequiredApprovalsOk() (*int64, bool) {
	if o == nil || o.RequiredApprovals == nil {
		return nil, false
	}
	return o.RequiredApprovals, true
}

// HasRequiredApprovals returns a boolean if a field has been set.
func (o *Branch) HasRequiredApprovals() bool {
	if o != nil && o.RequiredApprovals != nil {
		return true
	}

	return false
}

// SetRequiredApprovals gets a reference to the given int64 and assigns it to the RequiredApprovals field.
func (o *Branch) SetRequiredApprovals(v int64) {
	o.RequiredApprovals = &v
}

// GetStatusCheckContexts returns the StatusCheckContexts field value if set, zero value otherwise.
func (o *Branch) GetStatusCheckContexts() []string {
	if o == nil || o.StatusCheckContexts == nil {
		var ret []string
		return ret
	}
	return *o.StatusCheckContexts
}

// GetStatusCheckContextsOk returns a tuple with the StatusCheckContexts field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetStatusCheckContextsOk() (*[]string, bool) {
	if o == nil || o.StatusCheckContexts == nil {
		return nil, false
	}
	return o.StatusCheckContexts, true
}

// HasStatusCheckContexts returns a boolean if a field has been set.
func (o *Branch) HasStatusCheckContexts() bool {
	if o != nil && o.StatusCheckContexts != nil {
		return true
	}

	return false
}

// SetStatusCheckContexts gets a reference to the given []string and assigns it to the StatusCheckContexts field.
func (o *Branch) SetStatusCheckContexts(v []string) {
	o.StatusCheckContexts = &v
}

// GetUserCanMerge returns the UserCanMerge field value if set, zero value otherwise.
func (o *Branch) GetUserCanMerge() bool {
	if o == nil || o.UserCanMerge == nil {
		var ret bool
		return ret
	}
	return *o.UserCanMerge
}

// GetUserCanMergeOk returns a tuple with the UserCanMerge field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetUserCanMergeOk() (*bool, bool) {
	if o == nil || o.UserCanMerge == nil {
		return nil, false
	}
	return o.UserCanMerge, true
}

// HasUserCanMerge returns a boolean if a field has been set.
func (o *Branch) HasUserCanMerge() bool {
	if o != nil && o.UserCanMerge != nil {
		return true
	}

	return false
}

// SetUserCanMerge gets a reference to the given bool and assigns it to the UserCanMerge field.
func (o *Branch) SetUserCanMerge(v bool) {
	o.UserCanMerge = &v
}

// GetUserCanPush returns the UserCanPush field value if set, zero value otherwise.
func (o *Branch) GetUserCanPush() bool {
	if o == nil || o.UserCanPush == nil {
		var ret bool
		return ret
	}
	return *o.UserCanPush
}

// GetUserCanPushOk returns a tuple with the UserCanPush field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Branch) GetUserCanPushOk() (*bool, bool) {
	if o == nil || o.UserCanPush == nil {
		return nil, false
	}
	return o.UserCanPush, true
}

// HasUserCanPush returns a boolean if a field has been set.
func (o *Branch) HasUserCanPush() bool {
	if o != nil && o.UserCanPush != nil {
		return true
	}

	return false
}

// SetUserCanPush gets a reference to the given bool and assigns it to the UserCanPush field.
func (o *Branch) SetUserCanPush(v bool) {
	o.UserCanPush = &v
}

func (o Branch) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Commit != nil {
		toSerialize["commit"] = o.Commit
	}
	if o.EffectiveBranchProtectionName != nil {
		toSerialize["effective_branch_protection_name"] = o.EffectiveBranchProtectionName
	}
	if o.EnableStatusCheck != nil {
		toSerialize["enable_status_check"] = o.EnableStatusCheck
	}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.Protected != nil {
		toSerialize["protected"] = o.Protected
	}
	if o.RequiredApprovals != nil {
		toSerialize["required_approvals"] = o.RequiredApprovals
	}
	if o.StatusCheckContexts != nil {
		toSerialize["status_check_contexts"] = o.StatusCheckContexts
	}
	if o.UserCanMerge != nil {
		toSerialize["user_can_merge"] = o.UserCanMerge
	}
	if o.UserCanPush != nil {
		toSerialize["user_can_push"] = o.UserCanPush
	}
	return json.Marshal(toSerialize)
}

type NullableBranch struct {
	value *Branch
	isSet bool
}

func (v NullableBranch) Get() *Branch {
	return v.value
}

func (v *NullableBranch) Set(val *Branch) {
	v.value = val
	v.isSet = true
}

func (v NullableBranch) IsSet() bool {
	return v.isSet
}

func (v *NullableBranch) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableBranch(val *Branch) *NullableBranch {
	return &NullableBranch{value: val, isSet: true}
}

func (v NullableBranch) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableBranch) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


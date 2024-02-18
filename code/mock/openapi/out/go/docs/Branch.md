# Branch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Commit** | Pointer to [**PayloadCommit**](PayloadCommit.md) |  | [optional] 
**EffectiveBranchProtectionName** | Pointer to **string** |  | [optional] 
**EnableStatusCheck** | Pointer to **bool** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Protected** | Pointer to **bool** |  | [optional] 
**RequiredApprovals** | Pointer to **int64** |  | [optional] 
**StatusCheckContexts** | Pointer to **[]string** |  | [optional] 
**UserCanMerge** | Pointer to **bool** |  | [optional] 
**UserCanPush** | Pointer to **bool** |  | [optional] 

## Methods

### NewBranch

`func NewBranch() *Branch`

NewBranch instantiates a new Branch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBranchWithDefaults

`func NewBranchWithDefaults() *Branch`

NewBranchWithDefaults instantiates a new Branch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommit

`func (o *Branch) GetCommit() PayloadCommit`

GetCommit returns the Commit field if non-nil, zero value otherwise.

### GetCommitOk

`func (o *Branch) GetCommitOk() (*PayloadCommit, bool)`

GetCommitOk returns a tuple with the Commit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommit

`func (o *Branch) SetCommit(v PayloadCommit)`

SetCommit sets Commit field to given value.

### HasCommit

`func (o *Branch) HasCommit() bool`

HasCommit returns a boolean if a field has been set.

### GetEffectiveBranchProtectionName

`func (o *Branch) GetEffectiveBranchProtectionName() string`

GetEffectiveBranchProtectionName returns the EffectiveBranchProtectionName field if non-nil, zero value otherwise.

### GetEffectiveBranchProtectionNameOk

`func (o *Branch) GetEffectiveBranchProtectionNameOk() (*string, bool)`

GetEffectiveBranchProtectionNameOk returns a tuple with the EffectiveBranchProtectionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEffectiveBranchProtectionName

`func (o *Branch) SetEffectiveBranchProtectionName(v string)`

SetEffectiveBranchProtectionName sets EffectiveBranchProtectionName field to given value.

### HasEffectiveBranchProtectionName

`func (o *Branch) HasEffectiveBranchProtectionName() bool`

HasEffectiveBranchProtectionName returns a boolean if a field has been set.

### GetEnableStatusCheck

`func (o *Branch) GetEnableStatusCheck() bool`

GetEnableStatusCheck returns the EnableStatusCheck field if non-nil, zero value otherwise.

### GetEnableStatusCheckOk

`func (o *Branch) GetEnableStatusCheckOk() (*bool, bool)`

GetEnableStatusCheckOk returns a tuple with the EnableStatusCheck field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableStatusCheck

`func (o *Branch) SetEnableStatusCheck(v bool)`

SetEnableStatusCheck sets EnableStatusCheck field to given value.

### HasEnableStatusCheck

`func (o *Branch) HasEnableStatusCheck() bool`

HasEnableStatusCheck returns a boolean if a field has been set.

### GetName

`func (o *Branch) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Branch) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Branch) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Branch) HasName() bool`

HasName returns a boolean if a field has been set.

### GetProtected

`func (o *Branch) GetProtected() bool`

GetProtected returns the Protected field if non-nil, zero value otherwise.

### GetProtectedOk

`func (o *Branch) GetProtectedOk() (*bool, bool)`

GetProtectedOk returns a tuple with the Protected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtected

`func (o *Branch) SetProtected(v bool)`

SetProtected sets Protected field to given value.

### HasProtected

`func (o *Branch) HasProtected() bool`

HasProtected returns a boolean if a field has been set.

### GetRequiredApprovals

`func (o *Branch) GetRequiredApprovals() int64`

GetRequiredApprovals returns the RequiredApprovals field if non-nil, zero value otherwise.

### GetRequiredApprovalsOk

`func (o *Branch) GetRequiredApprovalsOk() (*int64, bool)`

GetRequiredApprovalsOk returns a tuple with the RequiredApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredApprovals

`func (o *Branch) SetRequiredApprovals(v int64)`

SetRequiredApprovals sets RequiredApprovals field to given value.

### HasRequiredApprovals

`func (o *Branch) HasRequiredApprovals() bool`

HasRequiredApprovals returns a boolean if a field has been set.

### GetStatusCheckContexts

`func (o *Branch) GetStatusCheckContexts() []string`

GetStatusCheckContexts returns the StatusCheckContexts field if non-nil, zero value otherwise.

### GetStatusCheckContextsOk

`func (o *Branch) GetStatusCheckContextsOk() (*[]string, bool)`

GetStatusCheckContextsOk returns a tuple with the StatusCheckContexts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCheckContexts

`func (o *Branch) SetStatusCheckContexts(v []string)`

SetStatusCheckContexts sets StatusCheckContexts field to given value.

### HasStatusCheckContexts

`func (o *Branch) HasStatusCheckContexts() bool`

HasStatusCheckContexts returns a boolean if a field has been set.

### GetUserCanMerge

`func (o *Branch) GetUserCanMerge() bool`

GetUserCanMerge returns the UserCanMerge field if non-nil, zero value otherwise.

### GetUserCanMergeOk

`func (o *Branch) GetUserCanMergeOk() (*bool, bool)`

GetUserCanMergeOk returns a tuple with the UserCanMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserCanMerge

`func (o *Branch) SetUserCanMerge(v bool)`

SetUserCanMerge sets UserCanMerge field to given value.

### HasUserCanMerge

`func (o *Branch) HasUserCanMerge() bool`

HasUserCanMerge returns a boolean if a field has been set.

### GetUserCanPush

`func (o *Branch) GetUserCanPush() bool`

GetUserCanPush returns the UserCanPush field if non-nil, zero value otherwise.

### GetUserCanPushOk

`func (o *Branch) GetUserCanPushOk() (*bool, bool)`

GetUserCanPushOk returns a tuple with the UserCanPush field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserCanPush

`func (o *Branch) SetUserCanPush(v bool)`

SetUserCanPush sets UserCanPush field to given value.

### HasUserCanPush

`func (o *Branch) HasUserCanPush() bool`

HasUserCanPush returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



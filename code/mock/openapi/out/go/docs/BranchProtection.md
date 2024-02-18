# BranchProtection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApprovalsWhitelistTeams** | Pointer to **[]string** |  | [optional] 
**ApprovalsWhitelistUsername** | Pointer to **[]string** |  | [optional] 
**BlockOnOfficialReviewRequests** | Pointer to **bool** |  | [optional] 
**BlockOnOutdatedBranch** | Pointer to **bool** |  | [optional] 
**BlockOnRejectedReviews** | Pointer to **bool** |  | [optional] 
**BranchName** | Pointer to **string** | Deprecated: true | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**DismissStaleApprovals** | Pointer to **bool** |  | [optional] 
**EnableApprovalsWhitelist** | Pointer to **bool** |  | [optional] 
**EnableMergeWhitelist** | Pointer to **bool** |  | [optional] 
**EnablePush** | Pointer to **bool** |  | [optional] 
**EnablePushWhitelist** | Pointer to **bool** |  | [optional] 
**EnableStatusCheck** | Pointer to **bool** |  | [optional] 
**IgnoreStaleApprovals** | Pointer to **bool** |  | [optional] 
**MergeWhitelistTeams** | Pointer to **[]string** |  | [optional] 
**MergeWhitelistUsernames** | Pointer to **[]string** |  | [optional] 
**ProtectedFilePatterns** | Pointer to **string** |  | [optional] 
**PushWhitelistDeployKeys** | Pointer to **bool** |  | [optional] 
**PushWhitelistTeams** | Pointer to **[]string** |  | [optional] 
**PushWhitelistUsernames** | Pointer to **[]string** |  | [optional] 
**RequireSignedCommits** | Pointer to **bool** |  | [optional] 
**RequiredApprovals** | Pointer to **int64** |  | [optional] 
**RuleName** | Pointer to **string** |  | [optional] 
**StatusCheckContexts** | Pointer to **[]string** |  | [optional] 
**UnprotectedFilePatterns** | Pointer to **string** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewBranchProtection

`func NewBranchProtection() *BranchProtection`

NewBranchProtection instantiates a new BranchProtection object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBranchProtectionWithDefaults

`func NewBranchProtectionWithDefaults() *BranchProtection`

NewBranchProtectionWithDefaults instantiates a new BranchProtection object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApprovalsWhitelistTeams

`func (o *BranchProtection) GetApprovalsWhitelistTeams() []string`

GetApprovalsWhitelistTeams returns the ApprovalsWhitelistTeams field if non-nil, zero value otherwise.

### GetApprovalsWhitelistTeamsOk

`func (o *BranchProtection) GetApprovalsWhitelistTeamsOk() (*[]string, bool)`

GetApprovalsWhitelistTeamsOk returns a tuple with the ApprovalsWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalsWhitelistTeams

`func (o *BranchProtection) SetApprovalsWhitelistTeams(v []string)`

SetApprovalsWhitelistTeams sets ApprovalsWhitelistTeams field to given value.

### HasApprovalsWhitelistTeams

`func (o *BranchProtection) HasApprovalsWhitelistTeams() bool`

HasApprovalsWhitelistTeams returns a boolean if a field has been set.

### GetApprovalsWhitelistUsername

`func (o *BranchProtection) GetApprovalsWhitelistUsername() []string`

GetApprovalsWhitelistUsername returns the ApprovalsWhitelistUsername field if non-nil, zero value otherwise.

### GetApprovalsWhitelistUsernameOk

`func (o *BranchProtection) GetApprovalsWhitelistUsernameOk() (*[]string, bool)`

GetApprovalsWhitelistUsernameOk returns a tuple with the ApprovalsWhitelistUsername field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalsWhitelistUsername

`func (o *BranchProtection) SetApprovalsWhitelistUsername(v []string)`

SetApprovalsWhitelistUsername sets ApprovalsWhitelistUsername field to given value.

### HasApprovalsWhitelistUsername

`func (o *BranchProtection) HasApprovalsWhitelistUsername() bool`

HasApprovalsWhitelistUsername returns a boolean if a field has been set.

### GetBlockOnOfficialReviewRequests

`func (o *BranchProtection) GetBlockOnOfficialReviewRequests() bool`

GetBlockOnOfficialReviewRequests returns the BlockOnOfficialReviewRequests field if non-nil, zero value otherwise.

### GetBlockOnOfficialReviewRequestsOk

`func (o *BranchProtection) GetBlockOnOfficialReviewRequestsOk() (*bool, bool)`

GetBlockOnOfficialReviewRequestsOk returns a tuple with the BlockOnOfficialReviewRequests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnOfficialReviewRequests

`func (o *BranchProtection) SetBlockOnOfficialReviewRequests(v bool)`

SetBlockOnOfficialReviewRequests sets BlockOnOfficialReviewRequests field to given value.

### HasBlockOnOfficialReviewRequests

`func (o *BranchProtection) HasBlockOnOfficialReviewRequests() bool`

HasBlockOnOfficialReviewRequests returns a boolean if a field has been set.

### GetBlockOnOutdatedBranch

`func (o *BranchProtection) GetBlockOnOutdatedBranch() bool`

GetBlockOnOutdatedBranch returns the BlockOnOutdatedBranch field if non-nil, zero value otherwise.

### GetBlockOnOutdatedBranchOk

`func (o *BranchProtection) GetBlockOnOutdatedBranchOk() (*bool, bool)`

GetBlockOnOutdatedBranchOk returns a tuple with the BlockOnOutdatedBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnOutdatedBranch

`func (o *BranchProtection) SetBlockOnOutdatedBranch(v bool)`

SetBlockOnOutdatedBranch sets BlockOnOutdatedBranch field to given value.

### HasBlockOnOutdatedBranch

`func (o *BranchProtection) HasBlockOnOutdatedBranch() bool`

HasBlockOnOutdatedBranch returns a boolean if a field has been set.

### GetBlockOnRejectedReviews

`func (o *BranchProtection) GetBlockOnRejectedReviews() bool`

GetBlockOnRejectedReviews returns the BlockOnRejectedReviews field if non-nil, zero value otherwise.

### GetBlockOnRejectedReviewsOk

`func (o *BranchProtection) GetBlockOnRejectedReviewsOk() (*bool, bool)`

GetBlockOnRejectedReviewsOk returns a tuple with the BlockOnRejectedReviews field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnRejectedReviews

`func (o *BranchProtection) SetBlockOnRejectedReviews(v bool)`

SetBlockOnRejectedReviews sets BlockOnRejectedReviews field to given value.

### HasBlockOnRejectedReviews

`func (o *BranchProtection) HasBlockOnRejectedReviews() bool`

HasBlockOnRejectedReviews returns a boolean if a field has been set.

### GetBranchName

`func (o *BranchProtection) GetBranchName() string`

GetBranchName returns the BranchName field if non-nil, zero value otherwise.

### GetBranchNameOk

`func (o *BranchProtection) GetBranchNameOk() (*string, bool)`

GetBranchNameOk returns a tuple with the BranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchName

`func (o *BranchProtection) SetBranchName(v string)`

SetBranchName sets BranchName field to given value.

### HasBranchName

`func (o *BranchProtection) HasBranchName() bool`

HasBranchName returns a boolean if a field has been set.

### GetCreatedAt

`func (o *BranchProtection) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *BranchProtection) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *BranchProtection) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *BranchProtection) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDismissStaleApprovals

`func (o *BranchProtection) GetDismissStaleApprovals() bool`

GetDismissStaleApprovals returns the DismissStaleApprovals field if non-nil, zero value otherwise.

### GetDismissStaleApprovalsOk

`func (o *BranchProtection) GetDismissStaleApprovalsOk() (*bool, bool)`

GetDismissStaleApprovalsOk returns a tuple with the DismissStaleApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDismissStaleApprovals

`func (o *BranchProtection) SetDismissStaleApprovals(v bool)`

SetDismissStaleApprovals sets DismissStaleApprovals field to given value.

### HasDismissStaleApprovals

`func (o *BranchProtection) HasDismissStaleApprovals() bool`

HasDismissStaleApprovals returns a boolean if a field has been set.

### GetEnableApprovalsWhitelist

`func (o *BranchProtection) GetEnableApprovalsWhitelist() bool`

GetEnableApprovalsWhitelist returns the EnableApprovalsWhitelist field if non-nil, zero value otherwise.

### GetEnableApprovalsWhitelistOk

`func (o *BranchProtection) GetEnableApprovalsWhitelistOk() (*bool, bool)`

GetEnableApprovalsWhitelistOk returns a tuple with the EnableApprovalsWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableApprovalsWhitelist

`func (o *BranchProtection) SetEnableApprovalsWhitelist(v bool)`

SetEnableApprovalsWhitelist sets EnableApprovalsWhitelist field to given value.

### HasEnableApprovalsWhitelist

`func (o *BranchProtection) HasEnableApprovalsWhitelist() bool`

HasEnableApprovalsWhitelist returns a boolean if a field has been set.

### GetEnableMergeWhitelist

`func (o *BranchProtection) GetEnableMergeWhitelist() bool`

GetEnableMergeWhitelist returns the EnableMergeWhitelist field if non-nil, zero value otherwise.

### GetEnableMergeWhitelistOk

`func (o *BranchProtection) GetEnableMergeWhitelistOk() (*bool, bool)`

GetEnableMergeWhitelistOk returns a tuple with the EnableMergeWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableMergeWhitelist

`func (o *BranchProtection) SetEnableMergeWhitelist(v bool)`

SetEnableMergeWhitelist sets EnableMergeWhitelist field to given value.

### HasEnableMergeWhitelist

`func (o *BranchProtection) HasEnableMergeWhitelist() bool`

HasEnableMergeWhitelist returns a boolean if a field has been set.

### GetEnablePush

`func (o *BranchProtection) GetEnablePush() bool`

GetEnablePush returns the EnablePush field if non-nil, zero value otherwise.

### GetEnablePushOk

`func (o *BranchProtection) GetEnablePushOk() (*bool, bool)`

GetEnablePushOk returns a tuple with the EnablePush field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePush

`func (o *BranchProtection) SetEnablePush(v bool)`

SetEnablePush sets EnablePush field to given value.

### HasEnablePush

`func (o *BranchProtection) HasEnablePush() bool`

HasEnablePush returns a boolean if a field has been set.

### GetEnablePushWhitelist

`func (o *BranchProtection) GetEnablePushWhitelist() bool`

GetEnablePushWhitelist returns the EnablePushWhitelist field if non-nil, zero value otherwise.

### GetEnablePushWhitelistOk

`func (o *BranchProtection) GetEnablePushWhitelistOk() (*bool, bool)`

GetEnablePushWhitelistOk returns a tuple with the EnablePushWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePushWhitelist

`func (o *BranchProtection) SetEnablePushWhitelist(v bool)`

SetEnablePushWhitelist sets EnablePushWhitelist field to given value.

### HasEnablePushWhitelist

`func (o *BranchProtection) HasEnablePushWhitelist() bool`

HasEnablePushWhitelist returns a boolean if a field has been set.

### GetEnableStatusCheck

`func (o *BranchProtection) GetEnableStatusCheck() bool`

GetEnableStatusCheck returns the EnableStatusCheck field if non-nil, zero value otherwise.

### GetEnableStatusCheckOk

`func (o *BranchProtection) GetEnableStatusCheckOk() (*bool, bool)`

GetEnableStatusCheckOk returns a tuple with the EnableStatusCheck field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableStatusCheck

`func (o *BranchProtection) SetEnableStatusCheck(v bool)`

SetEnableStatusCheck sets EnableStatusCheck field to given value.

### HasEnableStatusCheck

`func (o *BranchProtection) HasEnableStatusCheck() bool`

HasEnableStatusCheck returns a boolean if a field has been set.

### GetIgnoreStaleApprovals

`func (o *BranchProtection) GetIgnoreStaleApprovals() bool`

GetIgnoreStaleApprovals returns the IgnoreStaleApprovals field if non-nil, zero value otherwise.

### GetIgnoreStaleApprovalsOk

`func (o *BranchProtection) GetIgnoreStaleApprovalsOk() (*bool, bool)`

GetIgnoreStaleApprovalsOk returns a tuple with the IgnoreStaleApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIgnoreStaleApprovals

`func (o *BranchProtection) SetIgnoreStaleApprovals(v bool)`

SetIgnoreStaleApprovals sets IgnoreStaleApprovals field to given value.

### HasIgnoreStaleApprovals

`func (o *BranchProtection) HasIgnoreStaleApprovals() bool`

HasIgnoreStaleApprovals returns a boolean if a field has been set.

### GetMergeWhitelistTeams

`func (o *BranchProtection) GetMergeWhitelistTeams() []string`

GetMergeWhitelistTeams returns the MergeWhitelistTeams field if non-nil, zero value otherwise.

### GetMergeWhitelistTeamsOk

`func (o *BranchProtection) GetMergeWhitelistTeamsOk() (*[]string, bool)`

GetMergeWhitelistTeamsOk returns a tuple with the MergeWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhitelistTeams

`func (o *BranchProtection) SetMergeWhitelistTeams(v []string)`

SetMergeWhitelistTeams sets MergeWhitelistTeams field to given value.

### HasMergeWhitelistTeams

`func (o *BranchProtection) HasMergeWhitelistTeams() bool`

HasMergeWhitelistTeams returns a boolean if a field has been set.

### GetMergeWhitelistUsernames

`func (o *BranchProtection) GetMergeWhitelistUsernames() []string`

GetMergeWhitelistUsernames returns the MergeWhitelistUsernames field if non-nil, zero value otherwise.

### GetMergeWhitelistUsernamesOk

`func (o *BranchProtection) GetMergeWhitelistUsernamesOk() (*[]string, bool)`

GetMergeWhitelistUsernamesOk returns a tuple with the MergeWhitelistUsernames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhitelistUsernames

`func (o *BranchProtection) SetMergeWhitelistUsernames(v []string)`

SetMergeWhitelistUsernames sets MergeWhitelistUsernames field to given value.

### HasMergeWhitelistUsernames

`func (o *BranchProtection) HasMergeWhitelistUsernames() bool`

HasMergeWhitelistUsernames returns a boolean if a field has been set.

### GetProtectedFilePatterns

`func (o *BranchProtection) GetProtectedFilePatterns() string`

GetProtectedFilePatterns returns the ProtectedFilePatterns field if non-nil, zero value otherwise.

### GetProtectedFilePatternsOk

`func (o *BranchProtection) GetProtectedFilePatternsOk() (*string, bool)`

GetProtectedFilePatternsOk returns a tuple with the ProtectedFilePatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtectedFilePatterns

`func (o *BranchProtection) SetProtectedFilePatterns(v string)`

SetProtectedFilePatterns sets ProtectedFilePatterns field to given value.

### HasProtectedFilePatterns

`func (o *BranchProtection) HasProtectedFilePatterns() bool`

HasProtectedFilePatterns returns a boolean if a field has been set.

### GetPushWhitelistDeployKeys

`func (o *BranchProtection) GetPushWhitelistDeployKeys() bool`

GetPushWhitelistDeployKeys returns the PushWhitelistDeployKeys field if non-nil, zero value otherwise.

### GetPushWhitelistDeployKeysOk

`func (o *BranchProtection) GetPushWhitelistDeployKeysOk() (*bool, bool)`

GetPushWhitelistDeployKeysOk returns a tuple with the PushWhitelistDeployKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistDeployKeys

`func (o *BranchProtection) SetPushWhitelistDeployKeys(v bool)`

SetPushWhitelistDeployKeys sets PushWhitelistDeployKeys field to given value.

### HasPushWhitelistDeployKeys

`func (o *BranchProtection) HasPushWhitelistDeployKeys() bool`

HasPushWhitelistDeployKeys returns a boolean if a field has been set.

### GetPushWhitelistTeams

`func (o *BranchProtection) GetPushWhitelistTeams() []string`

GetPushWhitelistTeams returns the PushWhitelistTeams field if non-nil, zero value otherwise.

### GetPushWhitelistTeamsOk

`func (o *BranchProtection) GetPushWhitelistTeamsOk() (*[]string, bool)`

GetPushWhitelistTeamsOk returns a tuple with the PushWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistTeams

`func (o *BranchProtection) SetPushWhitelistTeams(v []string)`

SetPushWhitelistTeams sets PushWhitelistTeams field to given value.

### HasPushWhitelistTeams

`func (o *BranchProtection) HasPushWhitelistTeams() bool`

HasPushWhitelistTeams returns a boolean if a field has been set.

### GetPushWhitelistUsernames

`func (o *BranchProtection) GetPushWhitelistUsernames() []string`

GetPushWhitelistUsernames returns the PushWhitelistUsernames field if non-nil, zero value otherwise.

### GetPushWhitelistUsernamesOk

`func (o *BranchProtection) GetPushWhitelistUsernamesOk() (*[]string, bool)`

GetPushWhitelistUsernamesOk returns a tuple with the PushWhitelistUsernames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistUsernames

`func (o *BranchProtection) SetPushWhitelistUsernames(v []string)`

SetPushWhitelistUsernames sets PushWhitelistUsernames field to given value.

### HasPushWhitelistUsernames

`func (o *BranchProtection) HasPushWhitelistUsernames() bool`

HasPushWhitelistUsernames returns a boolean if a field has been set.

### GetRequireSignedCommits

`func (o *BranchProtection) GetRequireSignedCommits() bool`

GetRequireSignedCommits returns the RequireSignedCommits field if non-nil, zero value otherwise.

### GetRequireSignedCommitsOk

`func (o *BranchProtection) GetRequireSignedCommitsOk() (*bool, bool)`

GetRequireSignedCommitsOk returns a tuple with the RequireSignedCommits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequireSignedCommits

`func (o *BranchProtection) SetRequireSignedCommits(v bool)`

SetRequireSignedCommits sets RequireSignedCommits field to given value.

### HasRequireSignedCommits

`func (o *BranchProtection) HasRequireSignedCommits() bool`

HasRequireSignedCommits returns a boolean if a field has been set.

### GetRequiredApprovals

`func (o *BranchProtection) GetRequiredApprovals() int64`

GetRequiredApprovals returns the RequiredApprovals field if non-nil, zero value otherwise.

### GetRequiredApprovalsOk

`func (o *BranchProtection) GetRequiredApprovalsOk() (*int64, bool)`

GetRequiredApprovalsOk returns a tuple with the RequiredApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredApprovals

`func (o *BranchProtection) SetRequiredApprovals(v int64)`

SetRequiredApprovals sets RequiredApprovals field to given value.

### HasRequiredApprovals

`func (o *BranchProtection) HasRequiredApprovals() bool`

HasRequiredApprovals returns a boolean if a field has been set.

### GetRuleName

`func (o *BranchProtection) GetRuleName() string`

GetRuleName returns the RuleName field if non-nil, zero value otherwise.

### GetRuleNameOk

`func (o *BranchProtection) GetRuleNameOk() (*string, bool)`

GetRuleNameOk returns a tuple with the RuleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleName

`func (o *BranchProtection) SetRuleName(v string)`

SetRuleName sets RuleName field to given value.

### HasRuleName

`func (o *BranchProtection) HasRuleName() bool`

HasRuleName returns a boolean if a field has been set.

### GetStatusCheckContexts

`func (o *BranchProtection) GetStatusCheckContexts() []string`

GetStatusCheckContexts returns the StatusCheckContexts field if non-nil, zero value otherwise.

### GetStatusCheckContextsOk

`func (o *BranchProtection) GetStatusCheckContextsOk() (*[]string, bool)`

GetStatusCheckContextsOk returns a tuple with the StatusCheckContexts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCheckContexts

`func (o *BranchProtection) SetStatusCheckContexts(v []string)`

SetStatusCheckContexts sets StatusCheckContexts field to given value.

### HasStatusCheckContexts

`func (o *BranchProtection) HasStatusCheckContexts() bool`

HasStatusCheckContexts returns a boolean if a field has been set.

### GetUnprotectedFilePatterns

`func (o *BranchProtection) GetUnprotectedFilePatterns() string`

GetUnprotectedFilePatterns returns the UnprotectedFilePatterns field if non-nil, zero value otherwise.

### GetUnprotectedFilePatternsOk

`func (o *BranchProtection) GetUnprotectedFilePatternsOk() (*string, bool)`

GetUnprotectedFilePatternsOk returns a tuple with the UnprotectedFilePatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnprotectedFilePatterns

`func (o *BranchProtection) SetUnprotectedFilePatterns(v string)`

SetUnprotectedFilePatterns sets UnprotectedFilePatterns field to given value.

### HasUnprotectedFilePatterns

`func (o *BranchProtection) HasUnprotectedFilePatterns() bool`

HasUnprotectedFilePatterns returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *BranchProtection) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *BranchProtection) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *BranchProtection) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *BranchProtection) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



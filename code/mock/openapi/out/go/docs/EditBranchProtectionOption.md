# EditBranchProtectionOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApprovalsWhitelistTeams** | Pointer to **[]string** |  | [optional] 
**ApprovalsWhitelistUsername** | Pointer to **[]string** |  | [optional] 
**BlockOnOfficialReviewRequests** | Pointer to **bool** |  | [optional] 
**BlockOnOutdatedBranch** | Pointer to **bool** |  | [optional] 
**BlockOnRejectedReviews** | Pointer to **bool** |  | [optional] 
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
**StatusCheckContexts** | Pointer to **[]string** |  | [optional] 
**UnprotectedFilePatterns** | Pointer to **string** |  | [optional] 

## Methods

### NewEditBranchProtectionOption

`func NewEditBranchProtectionOption() *EditBranchProtectionOption`

NewEditBranchProtectionOption instantiates a new EditBranchProtectionOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditBranchProtectionOptionWithDefaults

`func NewEditBranchProtectionOptionWithDefaults() *EditBranchProtectionOption`

NewEditBranchProtectionOptionWithDefaults instantiates a new EditBranchProtectionOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApprovalsWhitelistTeams

`func (o *EditBranchProtectionOption) GetApprovalsWhitelistTeams() []string`

GetApprovalsWhitelistTeams returns the ApprovalsWhitelistTeams field if non-nil, zero value otherwise.

### GetApprovalsWhitelistTeamsOk

`func (o *EditBranchProtectionOption) GetApprovalsWhitelistTeamsOk() (*[]string, bool)`

GetApprovalsWhitelistTeamsOk returns a tuple with the ApprovalsWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalsWhitelistTeams

`func (o *EditBranchProtectionOption) SetApprovalsWhitelistTeams(v []string)`

SetApprovalsWhitelistTeams sets ApprovalsWhitelistTeams field to given value.

### HasApprovalsWhitelistTeams

`func (o *EditBranchProtectionOption) HasApprovalsWhitelistTeams() bool`

HasApprovalsWhitelistTeams returns a boolean if a field has been set.

### GetApprovalsWhitelistUsername

`func (o *EditBranchProtectionOption) GetApprovalsWhitelistUsername() []string`

GetApprovalsWhitelistUsername returns the ApprovalsWhitelistUsername field if non-nil, zero value otherwise.

### GetApprovalsWhitelistUsernameOk

`func (o *EditBranchProtectionOption) GetApprovalsWhitelistUsernameOk() (*[]string, bool)`

GetApprovalsWhitelistUsernameOk returns a tuple with the ApprovalsWhitelistUsername field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalsWhitelistUsername

`func (o *EditBranchProtectionOption) SetApprovalsWhitelistUsername(v []string)`

SetApprovalsWhitelistUsername sets ApprovalsWhitelistUsername field to given value.

### HasApprovalsWhitelistUsername

`func (o *EditBranchProtectionOption) HasApprovalsWhitelistUsername() bool`

HasApprovalsWhitelistUsername returns a boolean if a field has been set.

### GetBlockOnOfficialReviewRequests

`func (o *EditBranchProtectionOption) GetBlockOnOfficialReviewRequests() bool`

GetBlockOnOfficialReviewRequests returns the BlockOnOfficialReviewRequests field if non-nil, zero value otherwise.

### GetBlockOnOfficialReviewRequestsOk

`func (o *EditBranchProtectionOption) GetBlockOnOfficialReviewRequestsOk() (*bool, bool)`

GetBlockOnOfficialReviewRequestsOk returns a tuple with the BlockOnOfficialReviewRequests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnOfficialReviewRequests

`func (o *EditBranchProtectionOption) SetBlockOnOfficialReviewRequests(v bool)`

SetBlockOnOfficialReviewRequests sets BlockOnOfficialReviewRequests field to given value.

### HasBlockOnOfficialReviewRequests

`func (o *EditBranchProtectionOption) HasBlockOnOfficialReviewRequests() bool`

HasBlockOnOfficialReviewRequests returns a boolean if a field has been set.

### GetBlockOnOutdatedBranch

`func (o *EditBranchProtectionOption) GetBlockOnOutdatedBranch() bool`

GetBlockOnOutdatedBranch returns the BlockOnOutdatedBranch field if non-nil, zero value otherwise.

### GetBlockOnOutdatedBranchOk

`func (o *EditBranchProtectionOption) GetBlockOnOutdatedBranchOk() (*bool, bool)`

GetBlockOnOutdatedBranchOk returns a tuple with the BlockOnOutdatedBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnOutdatedBranch

`func (o *EditBranchProtectionOption) SetBlockOnOutdatedBranch(v bool)`

SetBlockOnOutdatedBranch sets BlockOnOutdatedBranch field to given value.

### HasBlockOnOutdatedBranch

`func (o *EditBranchProtectionOption) HasBlockOnOutdatedBranch() bool`

HasBlockOnOutdatedBranch returns a boolean if a field has been set.

### GetBlockOnRejectedReviews

`func (o *EditBranchProtectionOption) GetBlockOnRejectedReviews() bool`

GetBlockOnRejectedReviews returns the BlockOnRejectedReviews field if non-nil, zero value otherwise.

### GetBlockOnRejectedReviewsOk

`func (o *EditBranchProtectionOption) GetBlockOnRejectedReviewsOk() (*bool, bool)`

GetBlockOnRejectedReviewsOk returns a tuple with the BlockOnRejectedReviews field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnRejectedReviews

`func (o *EditBranchProtectionOption) SetBlockOnRejectedReviews(v bool)`

SetBlockOnRejectedReviews sets BlockOnRejectedReviews field to given value.

### HasBlockOnRejectedReviews

`func (o *EditBranchProtectionOption) HasBlockOnRejectedReviews() bool`

HasBlockOnRejectedReviews returns a boolean if a field has been set.

### GetDismissStaleApprovals

`func (o *EditBranchProtectionOption) GetDismissStaleApprovals() bool`

GetDismissStaleApprovals returns the DismissStaleApprovals field if non-nil, zero value otherwise.

### GetDismissStaleApprovalsOk

`func (o *EditBranchProtectionOption) GetDismissStaleApprovalsOk() (*bool, bool)`

GetDismissStaleApprovalsOk returns a tuple with the DismissStaleApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDismissStaleApprovals

`func (o *EditBranchProtectionOption) SetDismissStaleApprovals(v bool)`

SetDismissStaleApprovals sets DismissStaleApprovals field to given value.

### HasDismissStaleApprovals

`func (o *EditBranchProtectionOption) HasDismissStaleApprovals() bool`

HasDismissStaleApprovals returns a boolean if a field has been set.

### GetEnableApprovalsWhitelist

`func (o *EditBranchProtectionOption) GetEnableApprovalsWhitelist() bool`

GetEnableApprovalsWhitelist returns the EnableApprovalsWhitelist field if non-nil, zero value otherwise.

### GetEnableApprovalsWhitelistOk

`func (o *EditBranchProtectionOption) GetEnableApprovalsWhitelistOk() (*bool, bool)`

GetEnableApprovalsWhitelistOk returns a tuple with the EnableApprovalsWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableApprovalsWhitelist

`func (o *EditBranchProtectionOption) SetEnableApprovalsWhitelist(v bool)`

SetEnableApprovalsWhitelist sets EnableApprovalsWhitelist field to given value.

### HasEnableApprovalsWhitelist

`func (o *EditBranchProtectionOption) HasEnableApprovalsWhitelist() bool`

HasEnableApprovalsWhitelist returns a boolean if a field has been set.

### GetEnableMergeWhitelist

`func (o *EditBranchProtectionOption) GetEnableMergeWhitelist() bool`

GetEnableMergeWhitelist returns the EnableMergeWhitelist field if non-nil, zero value otherwise.

### GetEnableMergeWhitelistOk

`func (o *EditBranchProtectionOption) GetEnableMergeWhitelistOk() (*bool, bool)`

GetEnableMergeWhitelistOk returns a tuple with the EnableMergeWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableMergeWhitelist

`func (o *EditBranchProtectionOption) SetEnableMergeWhitelist(v bool)`

SetEnableMergeWhitelist sets EnableMergeWhitelist field to given value.

### HasEnableMergeWhitelist

`func (o *EditBranchProtectionOption) HasEnableMergeWhitelist() bool`

HasEnableMergeWhitelist returns a boolean if a field has been set.

### GetEnablePush

`func (o *EditBranchProtectionOption) GetEnablePush() bool`

GetEnablePush returns the EnablePush field if non-nil, zero value otherwise.

### GetEnablePushOk

`func (o *EditBranchProtectionOption) GetEnablePushOk() (*bool, bool)`

GetEnablePushOk returns a tuple with the EnablePush field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePush

`func (o *EditBranchProtectionOption) SetEnablePush(v bool)`

SetEnablePush sets EnablePush field to given value.

### HasEnablePush

`func (o *EditBranchProtectionOption) HasEnablePush() bool`

HasEnablePush returns a boolean if a field has been set.

### GetEnablePushWhitelist

`func (o *EditBranchProtectionOption) GetEnablePushWhitelist() bool`

GetEnablePushWhitelist returns the EnablePushWhitelist field if non-nil, zero value otherwise.

### GetEnablePushWhitelistOk

`func (o *EditBranchProtectionOption) GetEnablePushWhitelistOk() (*bool, bool)`

GetEnablePushWhitelistOk returns a tuple with the EnablePushWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePushWhitelist

`func (o *EditBranchProtectionOption) SetEnablePushWhitelist(v bool)`

SetEnablePushWhitelist sets EnablePushWhitelist field to given value.

### HasEnablePushWhitelist

`func (o *EditBranchProtectionOption) HasEnablePushWhitelist() bool`

HasEnablePushWhitelist returns a boolean if a field has been set.

### GetEnableStatusCheck

`func (o *EditBranchProtectionOption) GetEnableStatusCheck() bool`

GetEnableStatusCheck returns the EnableStatusCheck field if non-nil, zero value otherwise.

### GetEnableStatusCheckOk

`func (o *EditBranchProtectionOption) GetEnableStatusCheckOk() (*bool, bool)`

GetEnableStatusCheckOk returns a tuple with the EnableStatusCheck field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableStatusCheck

`func (o *EditBranchProtectionOption) SetEnableStatusCheck(v bool)`

SetEnableStatusCheck sets EnableStatusCheck field to given value.

### HasEnableStatusCheck

`func (o *EditBranchProtectionOption) HasEnableStatusCheck() bool`

HasEnableStatusCheck returns a boolean if a field has been set.

### GetIgnoreStaleApprovals

`func (o *EditBranchProtectionOption) GetIgnoreStaleApprovals() bool`

GetIgnoreStaleApprovals returns the IgnoreStaleApprovals field if non-nil, zero value otherwise.

### GetIgnoreStaleApprovalsOk

`func (o *EditBranchProtectionOption) GetIgnoreStaleApprovalsOk() (*bool, bool)`

GetIgnoreStaleApprovalsOk returns a tuple with the IgnoreStaleApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIgnoreStaleApprovals

`func (o *EditBranchProtectionOption) SetIgnoreStaleApprovals(v bool)`

SetIgnoreStaleApprovals sets IgnoreStaleApprovals field to given value.

### HasIgnoreStaleApprovals

`func (o *EditBranchProtectionOption) HasIgnoreStaleApprovals() bool`

HasIgnoreStaleApprovals returns a boolean if a field has been set.

### GetMergeWhitelistTeams

`func (o *EditBranchProtectionOption) GetMergeWhitelistTeams() []string`

GetMergeWhitelistTeams returns the MergeWhitelistTeams field if non-nil, zero value otherwise.

### GetMergeWhitelistTeamsOk

`func (o *EditBranchProtectionOption) GetMergeWhitelistTeamsOk() (*[]string, bool)`

GetMergeWhitelistTeamsOk returns a tuple with the MergeWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhitelistTeams

`func (o *EditBranchProtectionOption) SetMergeWhitelistTeams(v []string)`

SetMergeWhitelistTeams sets MergeWhitelistTeams field to given value.

### HasMergeWhitelistTeams

`func (o *EditBranchProtectionOption) HasMergeWhitelistTeams() bool`

HasMergeWhitelistTeams returns a boolean if a field has been set.

### GetMergeWhitelistUsernames

`func (o *EditBranchProtectionOption) GetMergeWhitelistUsernames() []string`

GetMergeWhitelistUsernames returns the MergeWhitelistUsernames field if non-nil, zero value otherwise.

### GetMergeWhitelistUsernamesOk

`func (o *EditBranchProtectionOption) GetMergeWhitelistUsernamesOk() (*[]string, bool)`

GetMergeWhitelistUsernamesOk returns a tuple with the MergeWhitelistUsernames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhitelistUsernames

`func (o *EditBranchProtectionOption) SetMergeWhitelistUsernames(v []string)`

SetMergeWhitelistUsernames sets MergeWhitelistUsernames field to given value.

### HasMergeWhitelistUsernames

`func (o *EditBranchProtectionOption) HasMergeWhitelistUsernames() bool`

HasMergeWhitelistUsernames returns a boolean if a field has been set.

### GetProtectedFilePatterns

`func (o *EditBranchProtectionOption) GetProtectedFilePatterns() string`

GetProtectedFilePatterns returns the ProtectedFilePatterns field if non-nil, zero value otherwise.

### GetProtectedFilePatternsOk

`func (o *EditBranchProtectionOption) GetProtectedFilePatternsOk() (*string, bool)`

GetProtectedFilePatternsOk returns a tuple with the ProtectedFilePatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtectedFilePatterns

`func (o *EditBranchProtectionOption) SetProtectedFilePatterns(v string)`

SetProtectedFilePatterns sets ProtectedFilePatterns field to given value.

### HasProtectedFilePatterns

`func (o *EditBranchProtectionOption) HasProtectedFilePatterns() bool`

HasProtectedFilePatterns returns a boolean if a field has been set.

### GetPushWhitelistDeployKeys

`func (o *EditBranchProtectionOption) GetPushWhitelistDeployKeys() bool`

GetPushWhitelistDeployKeys returns the PushWhitelistDeployKeys field if non-nil, zero value otherwise.

### GetPushWhitelistDeployKeysOk

`func (o *EditBranchProtectionOption) GetPushWhitelistDeployKeysOk() (*bool, bool)`

GetPushWhitelistDeployKeysOk returns a tuple with the PushWhitelistDeployKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistDeployKeys

`func (o *EditBranchProtectionOption) SetPushWhitelistDeployKeys(v bool)`

SetPushWhitelistDeployKeys sets PushWhitelistDeployKeys field to given value.

### HasPushWhitelistDeployKeys

`func (o *EditBranchProtectionOption) HasPushWhitelistDeployKeys() bool`

HasPushWhitelistDeployKeys returns a boolean if a field has been set.

### GetPushWhitelistTeams

`func (o *EditBranchProtectionOption) GetPushWhitelistTeams() []string`

GetPushWhitelistTeams returns the PushWhitelistTeams field if non-nil, zero value otherwise.

### GetPushWhitelistTeamsOk

`func (o *EditBranchProtectionOption) GetPushWhitelistTeamsOk() (*[]string, bool)`

GetPushWhitelistTeamsOk returns a tuple with the PushWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistTeams

`func (o *EditBranchProtectionOption) SetPushWhitelistTeams(v []string)`

SetPushWhitelistTeams sets PushWhitelistTeams field to given value.

### HasPushWhitelistTeams

`func (o *EditBranchProtectionOption) HasPushWhitelistTeams() bool`

HasPushWhitelistTeams returns a boolean if a field has been set.

### GetPushWhitelistUsernames

`func (o *EditBranchProtectionOption) GetPushWhitelistUsernames() []string`

GetPushWhitelistUsernames returns the PushWhitelistUsernames field if non-nil, zero value otherwise.

### GetPushWhitelistUsernamesOk

`func (o *EditBranchProtectionOption) GetPushWhitelistUsernamesOk() (*[]string, bool)`

GetPushWhitelistUsernamesOk returns a tuple with the PushWhitelistUsernames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistUsernames

`func (o *EditBranchProtectionOption) SetPushWhitelistUsernames(v []string)`

SetPushWhitelistUsernames sets PushWhitelistUsernames field to given value.

### HasPushWhitelistUsernames

`func (o *EditBranchProtectionOption) HasPushWhitelistUsernames() bool`

HasPushWhitelistUsernames returns a boolean if a field has been set.

### GetRequireSignedCommits

`func (o *EditBranchProtectionOption) GetRequireSignedCommits() bool`

GetRequireSignedCommits returns the RequireSignedCommits field if non-nil, zero value otherwise.

### GetRequireSignedCommitsOk

`func (o *EditBranchProtectionOption) GetRequireSignedCommitsOk() (*bool, bool)`

GetRequireSignedCommitsOk returns a tuple with the RequireSignedCommits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequireSignedCommits

`func (o *EditBranchProtectionOption) SetRequireSignedCommits(v bool)`

SetRequireSignedCommits sets RequireSignedCommits field to given value.

### HasRequireSignedCommits

`func (o *EditBranchProtectionOption) HasRequireSignedCommits() bool`

HasRequireSignedCommits returns a boolean if a field has been set.

### GetRequiredApprovals

`func (o *EditBranchProtectionOption) GetRequiredApprovals() int64`

GetRequiredApprovals returns the RequiredApprovals field if non-nil, zero value otherwise.

### GetRequiredApprovalsOk

`func (o *EditBranchProtectionOption) GetRequiredApprovalsOk() (*int64, bool)`

GetRequiredApprovalsOk returns a tuple with the RequiredApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredApprovals

`func (o *EditBranchProtectionOption) SetRequiredApprovals(v int64)`

SetRequiredApprovals sets RequiredApprovals field to given value.

### HasRequiredApprovals

`func (o *EditBranchProtectionOption) HasRequiredApprovals() bool`

HasRequiredApprovals returns a boolean if a field has been set.

### GetStatusCheckContexts

`func (o *EditBranchProtectionOption) GetStatusCheckContexts() []string`

GetStatusCheckContexts returns the StatusCheckContexts field if non-nil, zero value otherwise.

### GetStatusCheckContextsOk

`func (o *EditBranchProtectionOption) GetStatusCheckContextsOk() (*[]string, bool)`

GetStatusCheckContextsOk returns a tuple with the StatusCheckContexts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCheckContexts

`func (o *EditBranchProtectionOption) SetStatusCheckContexts(v []string)`

SetStatusCheckContexts sets StatusCheckContexts field to given value.

### HasStatusCheckContexts

`func (o *EditBranchProtectionOption) HasStatusCheckContexts() bool`

HasStatusCheckContexts returns a boolean if a field has been set.

### GetUnprotectedFilePatterns

`func (o *EditBranchProtectionOption) GetUnprotectedFilePatterns() string`

GetUnprotectedFilePatterns returns the UnprotectedFilePatterns field if non-nil, zero value otherwise.

### GetUnprotectedFilePatternsOk

`func (o *EditBranchProtectionOption) GetUnprotectedFilePatternsOk() (*string, bool)`

GetUnprotectedFilePatternsOk returns a tuple with the UnprotectedFilePatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnprotectedFilePatterns

`func (o *EditBranchProtectionOption) SetUnprotectedFilePatterns(v string)`

SetUnprotectedFilePatterns sets UnprotectedFilePatterns field to given value.

### HasUnprotectedFilePatterns

`func (o *EditBranchProtectionOption) HasUnprotectedFilePatterns() bool`

HasUnprotectedFilePatterns returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



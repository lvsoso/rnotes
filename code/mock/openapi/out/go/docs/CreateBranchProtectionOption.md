# CreateBranchProtectionOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApprovalsWhitelistTeams** | Pointer to **[]string** |  | [optional] 
**ApprovalsWhitelistUsername** | Pointer to **[]string** |  | [optional] 
**BlockOnOfficialReviewRequests** | Pointer to **bool** |  | [optional] 
**BlockOnOutdatedBranch** | Pointer to **bool** |  | [optional] 
**BlockOnRejectedReviews** | Pointer to **bool** |  | [optional] 
**BranchName** | Pointer to **string** | Deprecated: true | [optional] 
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

## Methods

### NewCreateBranchProtectionOption

`func NewCreateBranchProtectionOption() *CreateBranchProtectionOption`

NewCreateBranchProtectionOption instantiates a new CreateBranchProtectionOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateBranchProtectionOptionWithDefaults

`func NewCreateBranchProtectionOptionWithDefaults() *CreateBranchProtectionOption`

NewCreateBranchProtectionOptionWithDefaults instantiates a new CreateBranchProtectionOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApprovalsWhitelistTeams

`func (o *CreateBranchProtectionOption) GetApprovalsWhitelistTeams() []string`

GetApprovalsWhitelistTeams returns the ApprovalsWhitelistTeams field if non-nil, zero value otherwise.

### GetApprovalsWhitelistTeamsOk

`func (o *CreateBranchProtectionOption) GetApprovalsWhitelistTeamsOk() (*[]string, bool)`

GetApprovalsWhitelistTeamsOk returns a tuple with the ApprovalsWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalsWhitelistTeams

`func (o *CreateBranchProtectionOption) SetApprovalsWhitelistTeams(v []string)`

SetApprovalsWhitelistTeams sets ApprovalsWhitelistTeams field to given value.

### HasApprovalsWhitelistTeams

`func (o *CreateBranchProtectionOption) HasApprovalsWhitelistTeams() bool`

HasApprovalsWhitelistTeams returns a boolean if a field has been set.

### GetApprovalsWhitelistUsername

`func (o *CreateBranchProtectionOption) GetApprovalsWhitelistUsername() []string`

GetApprovalsWhitelistUsername returns the ApprovalsWhitelistUsername field if non-nil, zero value otherwise.

### GetApprovalsWhitelistUsernameOk

`func (o *CreateBranchProtectionOption) GetApprovalsWhitelistUsernameOk() (*[]string, bool)`

GetApprovalsWhitelistUsernameOk returns a tuple with the ApprovalsWhitelistUsername field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovalsWhitelistUsername

`func (o *CreateBranchProtectionOption) SetApprovalsWhitelistUsername(v []string)`

SetApprovalsWhitelistUsername sets ApprovalsWhitelistUsername field to given value.

### HasApprovalsWhitelistUsername

`func (o *CreateBranchProtectionOption) HasApprovalsWhitelistUsername() bool`

HasApprovalsWhitelistUsername returns a boolean if a field has been set.

### GetBlockOnOfficialReviewRequests

`func (o *CreateBranchProtectionOption) GetBlockOnOfficialReviewRequests() bool`

GetBlockOnOfficialReviewRequests returns the BlockOnOfficialReviewRequests field if non-nil, zero value otherwise.

### GetBlockOnOfficialReviewRequestsOk

`func (o *CreateBranchProtectionOption) GetBlockOnOfficialReviewRequestsOk() (*bool, bool)`

GetBlockOnOfficialReviewRequestsOk returns a tuple with the BlockOnOfficialReviewRequests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnOfficialReviewRequests

`func (o *CreateBranchProtectionOption) SetBlockOnOfficialReviewRequests(v bool)`

SetBlockOnOfficialReviewRequests sets BlockOnOfficialReviewRequests field to given value.

### HasBlockOnOfficialReviewRequests

`func (o *CreateBranchProtectionOption) HasBlockOnOfficialReviewRequests() bool`

HasBlockOnOfficialReviewRequests returns a boolean if a field has been set.

### GetBlockOnOutdatedBranch

`func (o *CreateBranchProtectionOption) GetBlockOnOutdatedBranch() bool`

GetBlockOnOutdatedBranch returns the BlockOnOutdatedBranch field if non-nil, zero value otherwise.

### GetBlockOnOutdatedBranchOk

`func (o *CreateBranchProtectionOption) GetBlockOnOutdatedBranchOk() (*bool, bool)`

GetBlockOnOutdatedBranchOk returns a tuple with the BlockOnOutdatedBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnOutdatedBranch

`func (o *CreateBranchProtectionOption) SetBlockOnOutdatedBranch(v bool)`

SetBlockOnOutdatedBranch sets BlockOnOutdatedBranch field to given value.

### HasBlockOnOutdatedBranch

`func (o *CreateBranchProtectionOption) HasBlockOnOutdatedBranch() bool`

HasBlockOnOutdatedBranch returns a boolean if a field has been set.

### GetBlockOnRejectedReviews

`func (o *CreateBranchProtectionOption) GetBlockOnRejectedReviews() bool`

GetBlockOnRejectedReviews returns the BlockOnRejectedReviews field if non-nil, zero value otherwise.

### GetBlockOnRejectedReviewsOk

`func (o *CreateBranchProtectionOption) GetBlockOnRejectedReviewsOk() (*bool, bool)`

GetBlockOnRejectedReviewsOk returns a tuple with the BlockOnRejectedReviews field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlockOnRejectedReviews

`func (o *CreateBranchProtectionOption) SetBlockOnRejectedReviews(v bool)`

SetBlockOnRejectedReviews sets BlockOnRejectedReviews field to given value.

### HasBlockOnRejectedReviews

`func (o *CreateBranchProtectionOption) HasBlockOnRejectedReviews() bool`

HasBlockOnRejectedReviews returns a boolean if a field has been set.

### GetBranchName

`func (o *CreateBranchProtectionOption) GetBranchName() string`

GetBranchName returns the BranchName field if non-nil, zero value otherwise.

### GetBranchNameOk

`func (o *CreateBranchProtectionOption) GetBranchNameOk() (*string, bool)`

GetBranchNameOk returns a tuple with the BranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchName

`func (o *CreateBranchProtectionOption) SetBranchName(v string)`

SetBranchName sets BranchName field to given value.

### HasBranchName

`func (o *CreateBranchProtectionOption) HasBranchName() bool`

HasBranchName returns a boolean if a field has been set.

### GetDismissStaleApprovals

`func (o *CreateBranchProtectionOption) GetDismissStaleApprovals() bool`

GetDismissStaleApprovals returns the DismissStaleApprovals field if non-nil, zero value otherwise.

### GetDismissStaleApprovalsOk

`func (o *CreateBranchProtectionOption) GetDismissStaleApprovalsOk() (*bool, bool)`

GetDismissStaleApprovalsOk returns a tuple with the DismissStaleApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDismissStaleApprovals

`func (o *CreateBranchProtectionOption) SetDismissStaleApprovals(v bool)`

SetDismissStaleApprovals sets DismissStaleApprovals field to given value.

### HasDismissStaleApprovals

`func (o *CreateBranchProtectionOption) HasDismissStaleApprovals() bool`

HasDismissStaleApprovals returns a boolean if a field has been set.

### GetEnableApprovalsWhitelist

`func (o *CreateBranchProtectionOption) GetEnableApprovalsWhitelist() bool`

GetEnableApprovalsWhitelist returns the EnableApprovalsWhitelist field if non-nil, zero value otherwise.

### GetEnableApprovalsWhitelistOk

`func (o *CreateBranchProtectionOption) GetEnableApprovalsWhitelistOk() (*bool, bool)`

GetEnableApprovalsWhitelistOk returns a tuple with the EnableApprovalsWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableApprovalsWhitelist

`func (o *CreateBranchProtectionOption) SetEnableApprovalsWhitelist(v bool)`

SetEnableApprovalsWhitelist sets EnableApprovalsWhitelist field to given value.

### HasEnableApprovalsWhitelist

`func (o *CreateBranchProtectionOption) HasEnableApprovalsWhitelist() bool`

HasEnableApprovalsWhitelist returns a boolean if a field has been set.

### GetEnableMergeWhitelist

`func (o *CreateBranchProtectionOption) GetEnableMergeWhitelist() bool`

GetEnableMergeWhitelist returns the EnableMergeWhitelist field if non-nil, zero value otherwise.

### GetEnableMergeWhitelistOk

`func (o *CreateBranchProtectionOption) GetEnableMergeWhitelistOk() (*bool, bool)`

GetEnableMergeWhitelistOk returns a tuple with the EnableMergeWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableMergeWhitelist

`func (o *CreateBranchProtectionOption) SetEnableMergeWhitelist(v bool)`

SetEnableMergeWhitelist sets EnableMergeWhitelist field to given value.

### HasEnableMergeWhitelist

`func (o *CreateBranchProtectionOption) HasEnableMergeWhitelist() bool`

HasEnableMergeWhitelist returns a boolean if a field has been set.

### GetEnablePush

`func (o *CreateBranchProtectionOption) GetEnablePush() bool`

GetEnablePush returns the EnablePush field if non-nil, zero value otherwise.

### GetEnablePushOk

`func (o *CreateBranchProtectionOption) GetEnablePushOk() (*bool, bool)`

GetEnablePushOk returns a tuple with the EnablePush field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePush

`func (o *CreateBranchProtectionOption) SetEnablePush(v bool)`

SetEnablePush sets EnablePush field to given value.

### HasEnablePush

`func (o *CreateBranchProtectionOption) HasEnablePush() bool`

HasEnablePush returns a boolean if a field has been set.

### GetEnablePushWhitelist

`func (o *CreateBranchProtectionOption) GetEnablePushWhitelist() bool`

GetEnablePushWhitelist returns the EnablePushWhitelist field if non-nil, zero value otherwise.

### GetEnablePushWhitelistOk

`func (o *CreateBranchProtectionOption) GetEnablePushWhitelistOk() (*bool, bool)`

GetEnablePushWhitelistOk returns a tuple with the EnablePushWhitelist field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePushWhitelist

`func (o *CreateBranchProtectionOption) SetEnablePushWhitelist(v bool)`

SetEnablePushWhitelist sets EnablePushWhitelist field to given value.

### HasEnablePushWhitelist

`func (o *CreateBranchProtectionOption) HasEnablePushWhitelist() bool`

HasEnablePushWhitelist returns a boolean if a field has been set.

### GetEnableStatusCheck

`func (o *CreateBranchProtectionOption) GetEnableStatusCheck() bool`

GetEnableStatusCheck returns the EnableStatusCheck field if non-nil, zero value otherwise.

### GetEnableStatusCheckOk

`func (o *CreateBranchProtectionOption) GetEnableStatusCheckOk() (*bool, bool)`

GetEnableStatusCheckOk returns a tuple with the EnableStatusCheck field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableStatusCheck

`func (o *CreateBranchProtectionOption) SetEnableStatusCheck(v bool)`

SetEnableStatusCheck sets EnableStatusCheck field to given value.

### HasEnableStatusCheck

`func (o *CreateBranchProtectionOption) HasEnableStatusCheck() bool`

HasEnableStatusCheck returns a boolean if a field has been set.

### GetIgnoreStaleApprovals

`func (o *CreateBranchProtectionOption) GetIgnoreStaleApprovals() bool`

GetIgnoreStaleApprovals returns the IgnoreStaleApprovals field if non-nil, zero value otherwise.

### GetIgnoreStaleApprovalsOk

`func (o *CreateBranchProtectionOption) GetIgnoreStaleApprovalsOk() (*bool, bool)`

GetIgnoreStaleApprovalsOk returns a tuple with the IgnoreStaleApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIgnoreStaleApprovals

`func (o *CreateBranchProtectionOption) SetIgnoreStaleApprovals(v bool)`

SetIgnoreStaleApprovals sets IgnoreStaleApprovals field to given value.

### HasIgnoreStaleApprovals

`func (o *CreateBranchProtectionOption) HasIgnoreStaleApprovals() bool`

HasIgnoreStaleApprovals returns a boolean if a field has been set.

### GetMergeWhitelistTeams

`func (o *CreateBranchProtectionOption) GetMergeWhitelistTeams() []string`

GetMergeWhitelistTeams returns the MergeWhitelistTeams field if non-nil, zero value otherwise.

### GetMergeWhitelistTeamsOk

`func (o *CreateBranchProtectionOption) GetMergeWhitelistTeamsOk() (*[]string, bool)`

GetMergeWhitelistTeamsOk returns a tuple with the MergeWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhitelistTeams

`func (o *CreateBranchProtectionOption) SetMergeWhitelistTeams(v []string)`

SetMergeWhitelistTeams sets MergeWhitelistTeams field to given value.

### HasMergeWhitelistTeams

`func (o *CreateBranchProtectionOption) HasMergeWhitelistTeams() bool`

HasMergeWhitelistTeams returns a boolean if a field has been set.

### GetMergeWhitelistUsernames

`func (o *CreateBranchProtectionOption) GetMergeWhitelistUsernames() []string`

GetMergeWhitelistUsernames returns the MergeWhitelistUsernames field if non-nil, zero value otherwise.

### GetMergeWhitelistUsernamesOk

`func (o *CreateBranchProtectionOption) GetMergeWhitelistUsernamesOk() (*[]string, bool)`

GetMergeWhitelistUsernamesOk returns a tuple with the MergeWhitelistUsernames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhitelistUsernames

`func (o *CreateBranchProtectionOption) SetMergeWhitelistUsernames(v []string)`

SetMergeWhitelistUsernames sets MergeWhitelistUsernames field to given value.

### HasMergeWhitelistUsernames

`func (o *CreateBranchProtectionOption) HasMergeWhitelistUsernames() bool`

HasMergeWhitelistUsernames returns a boolean if a field has been set.

### GetProtectedFilePatterns

`func (o *CreateBranchProtectionOption) GetProtectedFilePatterns() string`

GetProtectedFilePatterns returns the ProtectedFilePatterns field if non-nil, zero value otherwise.

### GetProtectedFilePatternsOk

`func (o *CreateBranchProtectionOption) GetProtectedFilePatternsOk() (*string, bool)`

GetProtectedFilePatternsOk returns a tuple with the ProtectedFilePatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtectedFilePatterns

`func (o *CreateBranchProtectionOption) SetProtectedFilePatterns(v string)`

SetProtectedFilePatterns sets ProtectedFilePatterns field to given value.

### HasProtectedFilePatterns

`func (o *CreateBranchProtectionOption) HasProtectedFilePatterns() bool`

HasProtectedFilePatterns returns a boolean if a field has been set.

### GetPushWhitelistDeployKeys

`func (o *CreateBranchProtectionOption) GetPushWhitelistDeployKeys() bool`

GetPushWhitelistDeployKeys returns the PushWhitelistDeployKeys field if non-nil, zero value otherwise.

### GetPushWhitelistDeployKeysOk

`func (o *CreateBranchProtectionOption) GetPushWhitelistDeployKeysOk() (*bool, bool)`

GetPushWhitelistDeployKeysOk returns a tuple with the PushWhitelistDeployKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistDeployKeys

`func (o *CreateBranchProtectionOption) SetPushWhitelistDeployKeys(v bool)`

SetPushWhitelistDeployKeys sets PushWhitelistDeployKeys field to given value.

### HasPushWhitelistDeployKeys

`func (o *CreateBranchProtectionOption) HasPushWhitelistDeployKeys() bool`

HasPushWhitelistDeployKeys returns a boolean if a field has been set.

### GetPushWhitelistTeams

`func (o *CreateBranchProtectionOption) GetPushWhitelistTeams() []string`

GetPushWhitelistTeams returns the PushWhitelistTeams field if non-nil, zero value otherwise.

### GetPushWhitelistTeamsOk

`func (o *CreateBranchProtectionOption) GetPushWhitelistTeamsOk() (*[]string, bool)`

GetPushWhitelistTeamsOk returns a tuple with the PushWhitelistTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistTeams

`func (o *CreateBranchProtectionOption) SetPushWhitelistTeams(v []string)`

SetPushWhitelistTeams sets PushWhitelistTeams field to given value.

### HasPushWhitelistTeams

`func (o *CreateBranchProtectionOption) HasPushWhitelistTeams() bool`

HasPushWhitelistTeams returns a boolean if a field has been set.

### GetPushWhitelistUsernames

`func (o *CreateBranchProtectionOption) GetPushWhitelistUsernames() []string`

GetPushWhitelistUsernames returns the PushWhitelistUsernames field if non-nil, zero value otherwise.

### GetPushWhitelistUsernamesOk

`func (o *CreateBranchProtectionOption) GetPushWhitelistUsernamesOk() (*[]string, bool)`

GetPushWhitelistUsernamesOk returns a tuple with the PushWhitelistUsernames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPushWhitelistUsernames

`func (o *CreateBranchProtectionOption) SetPushWhitelistUsernames(v []string)`

SetPushWhitelistUsernames sets PushWhitelistUsernames field to given value.

### HasPushWhitelistUsernames

`func (o *CreateBranchProtectionOption) HasPushWhitelistUsernames() bool`

HasPushWhitelistUsernames returns a boolean if a field has been set.

### GetRequireSignedCommits

`func (o *CreateBranchProtectionOption) GetRequireSignedCommits() bool`

GetRequireSignedCommits returns the RequireSignedCommits field if non-nil, zero value otherwise.

### GetRequireSignedCommitsOk

`func (o *CreateBranchProtectionOption) GetRequireSignedCommitsOk() (*bool, bool)`

GetRequireSignedCommitsOk returns a tuple with the RequireSignedCommits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequireSignedCommits

`func (o *CreateBranchProtectionOption) SetRequireSignedCommits(v bool)`

SetRequireSignedCommits sets RequireSignedCommits field to given value.

### HasRequireSignedCommits

`func (o *CreateBranchProtectionOption) HasRequireSignedCommits() bool`

HasRequireSignedCommits returns a boolean if a field has been set.

### GetRequiredApprovals

`func (o *CreateBranchProtectionOption) GetRequiredApprovals() int64`

GetRequiredApprovals returns the RequiredApprovals field if non-nil, zero value otherwise.

### GetRequiredApprovalsOk

`func (o *CreateBranchProtectionOption) GetRequiredApprovalsOk() (*int64, bool)`

GetRequiredApprovalsOk returns a tuple with the RequiredApprovals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredApprovals

`func (o *CreateBranchProtectionOption) SetRequiredApprovals(v int64)`

SetRequiredApprovals sets RequiredApprovals field to given value.

### HasRequiredApprovals

`func (o *CreateBranchProtectionOption) HasRequiredApprovals() bool`

HasRequiredApprovals returns a boolean if a field has been set.

### GetRuleName

`func (o *CreateBranchProtectionOption) GetRuleName() string`

GetRuleName returns the RuleName field if non-nil, zero value otherwise.

### GetRuleNameOk

`func (o *CreateBranchProtectionOption) GetRuleNameOk() (*string, bool)`

GetRuleNameOk returns a tuple with the RuleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleName

`func (o *CreateBranchProtectionOption) SetRuleName(v string)`

SetRuleName sets RuleName field to given value.

### HasRuleName

`func (o *CreateBranchProtectionOption) HasRuleName() bool`

HasRuleName returns a boolean if a field has been set.

### GetStatusCheckContexts

`func (o *CreateBranchProtectionOption) GetStatusCheckContexts() []string`

GetStatusCheckContexts returns the StatusCheckContexts field if non-nil, zero value otherwise.

### GetStatusCheckContextsOk

`func (o *CreateBranchProtectionOption) GetStatusCheckContextsOk() (*[]string, bool)`

GetStatusCheckContextsOk returns a tuple with the StatusCheckContexts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCheckContexts

`func (o *CreateBranchProtectionOption) SetStatusCheckContexts(v []string)`

SetStatusCheckContexts sets StatusCheckContexts field to given value.

### HasStatusCheckContexts

`func (o *CreateBranchProtectionOption) HasStatusCheckContexts() bool`

HasStatusCheckContexts returns a boolean if a field has been set.

### GetUnprotectedFilePatterns

`func (o *CreateBranchProtectionOption) GetUnprotectedFilePatterns() string`

GetUnprotectedFilePatterns returns the UnprotectedFilePatterns field if non-nil, zero value otherwise.

### GetUnprotectedFilePatternsOk

`func (o *CreateBranchProtectionOption) GetUnprotectedFilePatternsOk() (*string, bool)`

GetUnprotectedFilePatternsOk returns a tuple with the UnprotectedFilePatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnprotectedFilePatterns

`func (o *CreateBranchProtectionOption) SetUnprotectedFilePatterns(v string)`

SetUnprotectedFilePatterns sets UnprotectedFilePatterns field to given value.

### HasUnprotectedFilePatterns

`func (o *CreateBranchProtectionOption) HasUnprotectedFilePatterns() bool`

HasUnprotectedFilePatterns returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



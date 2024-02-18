# PullRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AllowMaintainerEdit** | Pointer to **bool** |  | [optional] 
**Assignee** | Pointer to [**User**](User.md) |  | [optional] 
**Assignees** | Pointer to [**[]User**](User.md) |  | [optional] 
**Base** | Pointer to [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**ClosedAt** | Pointer to **time.Time** |  | [optional] 
**Comments** | Pointer to **int64** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**DiffUrl** | Pointer to **string** |  | [optional] 
**DueDate** | Pointer to **time.Time** |  | [optional] 
**Head** | Pointer to [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IsLocked** | Pointer to **bool** |  | [optional] 
**Labels** | Pointer to [**[]Label**](Label.md) |  | [optional] 
**MergeBase** | Pointer to **string** |  | [optional] 
**MergeCommitSha** | Pointer to **string** |  | [optional] 
**Mergeable** | Pointer to **bool** |  | [optional] 
**Merged** | Pointer to **bool** |  | [optional] 
**MergedAt** | Pointer to **time.Time** |  | [optional] 
**MergedBy** | Pointer to [**User**](User.md) |  | [optional] 
**Milestone** | Pointer to [**Milestone**](Milestone.md) |  | [optional] 
**Number** | Pointer to **int64** |  | [optional] 
**PatchUrl** | Pointer to **string** |  | [optional] 
**PinOrder** | Pointer to **int64** |  | [optional] 
**RequestedReviewers** | Pointer to [**[]User**](User.md) |  | [optional] 
**State** | Pointer to **string** | StateType issue state type | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewPullRequest

`func NewPullRequest() *PullRequest`

NewPullRequest instantiates a new PullRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPullRequestWithDefaults

`func NewPullRequestWithDefaults() *PullRequest`

NewPullRequestWithDefaults instantiates a new PullRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAllowMaintainerEdit

`func (o *PullRequest) GetAllowMaintainerEdit() bool`

GetAllowMaintainerEdit returns the AllowMaintainerEdit field if non-nil, zero value otherwise.

### GetAllowMaintainerEditOk

`func (o *PullRequest) GetAllowMaintainerEditOk() (*bool, bool)`

GetAllowMaintainerEditOk returns a tuple with the AllowMaintainerEdit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowMaintainerEdit

`func (o *PullRequest) SetAllowMaintainerEdit(v bool)`

SetAllowMaintainerEdit sets AllowMaintainerEdit field to given value.

### HasAllowMaintainerEdit

`func (o *PullRequest) HasAllowMaintainerEdit() bool`

HasAllowMaintainerEdit returns a boolean if a field has been set.

### GetAssignee

`func (o *PullRequest) GetAssignee() User`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *PullRequest) GetAssigneeOk() (*User, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *PullRequest) SetAssignee(v User)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *PullRequest) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssignees

`func (o *PullRequest) GetAssignees() []User`

GetAssignees returns the Assignees field if non-nil, zero value otherwise.

### GetAssigneesOk

`func (o *PullRequest) GetAssigneesOk() (*[]User, bool)`

GetAssigneesOk returns a tuple with the Assignees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignees

`func (o *PullRequest) SetAssignees(v []User)`

SetAssignees sets Assignees field to given value.

### HasAssignees

`func (o *PullRequest) HasAssignees() bool`

HasAssignees returns a boolean if a field has been set.

### GetBase

`func (o *PullRequest) GetBase() PRBranchInfo`

GetBase returns the Base field if non-nil, zero value otherwise.

### GetBaseOk

`func (o *PullRequest) GetBaseOk() (*PRBranchInfo, bool)`

GetBaseOk returns a tuple with the Base field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBase

`func (o *PullRequest) SetBase(v PRBranchInfo)`

SetBase sets Base field to given value.

### HasBase

`func (o *PullRequest) HasBase() bool`

HasBase returns a boolean if a field has been set.

### GetBody

`func (o *PullRequest) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *PullRequest) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *PullRequest) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *PullRequest) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetClosedAt

`func (o *PullRequest) GetClosedAt() time.Time`

GetClosedAt returns the ClosedAt field if non-nil, zero value otherwise.

### GetClosedAtOk

`func (o *PullRequest) GetClosedAtOk() (*time.Time, bool)`

GetClosedAtOk returns a tuple with the ClosedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedAt

`func (o *PullRequest) SetClosedAt(v time.Time)`

SetClosedAt sets ClosedAt field to given value.

### HasClosedAt

`func (o *PullRequest) HasClosedAt() bool`

HasClosedAt returns a boolean if a field has been set.

### GetComments

`func (o *PullRequest) GetComments() int64`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PullRequest) GetCommentsOk() (*int64, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PullRequest) SetComments(v int64)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PullRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCreatedAt

`func (o *PullRequest) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *PullRequest) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *PullRequest) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *PullRequest) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDiffUrl

`func (o *PullRequest) GetDiffUrl() string`

GetDiffUrl returns the DiffUrl field if non-nil, zero value otherwise.

### GetDiffUrlOk

`func (o *PullRequest) GetDiffUrlOk() (*string, bool)`

GetDiffUrlOk returns a tuple with the DiffUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffUrl

`func (o *PullRequest) SetDiffUrl(v string)`

SetDiffUrl sets DiffUrl field to given value.

### HasDiffUrl

`func (o *PullRequest) HasDiffUrl() bool`

HasDiffUrl returns a boolean if a field has been set.

### GetDueDate

`func (o *PullRequest) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *PullRequest) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *PullRequest) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.

### HasDueDate

`func (o *PullRequest) HasDueDate() bool`

HasDueDate returns a boolean if a field has been set.

### GetHead

`func (o *PullRequest) GetHead() PRBranchInfo`

GetHead returns the Head field if non-nil, zero value otherwise.

### GetHeadOk

`func (o *PullRequest) GetHeadOk() (*PRBranchInfo, bool)`

GetHeadOk returns a tuple with the Head field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHead

`func (o *PullRequest) SetHead(v PRBranchInfo)`

SetHead sets Head field to given value.

### HasHead

`func (o *PullRequest) HasHead() bool`

HasHead returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *PullRequest) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *PullRequest) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *PullRequest) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *PullRequest) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *PullRequest) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PullRequest) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PullRequest) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *PullRequest) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIsLocked

`func (o *PullRequest) GetIsLocked() bool`

GetIsLocked returns the IsLocked field if non-nil, zero value otherwise.

### GetIsLockedOk

`func (o *PullRequest) GetIsLockedOk() (*bool, bool)`

GetIsLockedOk returns a tuple with the IsLocked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsLocked

`func (o *PullRequest) SetIsLocked(v bool)`

SetIsLocked sets IsLocked field to given value.

### HasIsLocked

`func (o *PullRequest) HasIsLocked() bool`

HasIsLocked returns a boolean if a field has been set.

### GetLabels

`func (o *PullRequest) GetLabels() []Label`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *PullRequest) GetLabelsOk() (*[]Label, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *PullRequest) SetLabels(v []Label)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *PullRequest) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetMergeBase

`func (o *PullRequest) GetMergeBase() string`

GetMergeBase returns the MergeBase field if non-nil, zero value otherwise.

### GetMergeBaseOk

`func (o *PullRequest) GetMergeBaseOk() (*string, bool)`

GetMergeBaseOk returns a tuple with the MergeBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeBase

`func (o *PullRequest) SetMergeBase(v string)`

SetMergeBase sets MergeBase field to given value.

### HasMergeBase

`func (o *PullRequest) HasMergeBase() bool`

HasMergeBase returns a boolean if a field has been set.

### GetMergeCommitSha

`func (o *PullRequest) GetMergeCommitSha() string`

GetMergeCommitSha returns the MergeCommitSha field if non-nil, zero value otherwise.

### GetMergeCommitShaOk

`func (o *PullRequest) GetMergeCommitShaOk() (*string, bool)`

GetMergeCommitShaOk returns a tuple with the MergeCommitSha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeCommitSha

`func (o *PullRequest) SetMergeCommitSha(v string)`

SetMergeCommitSha sets MergeCommitSha field to given value.

### HasMergeCommitSha

`func (o *PullRequest) HasMergeCommitSha() bool`

HasMergeCommitSha returns a boolean if a field has been set.

### GetMergeable

`func (o *PullRequest) GetMergeable() bool`

GetMergeable returns the Mergeable field if non-nil, zero value otherwise.

### GetMergeableOk

`func (o *PullRequest) GetMergeableOk() (*bool, bool)`

GetMergeableOk returns a tuple with the Mergeable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeable

`func (o *PullRequest) SetMergeable(v bool)`

SetMergeable sets Mergeable field to given value.

### HasMergeable

`func (o *PullRequest) HasMergeable() bool`

HasMergeable returns a boolean if a field has been set.

### GetMerged

`func (o *PullRequest) GetMerged() bool`

GetMerged returns the Merged field if non-nil, zero value otherwise.

### GetMergedOk

`func (o *PullRequest) GetMergedOk() (*bool, bool)`

GetMergedOk returns a tuple with the Merged field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMerged

`func (o *PullRequest) SetMerged(v bool)`

SetMerged sets Merged field to given value.

### HasMerged

`func (o *PullRequest) HasMerged() bool`

HasMerged returns a boolean if a field has been set.

### GetMergedAt

`func (o *PullRequest) GetMergedAt() time.Time`

GetMergedAt returns the MergedAt field if non-nil, zero value otherwise.

### GetMergedAtOk

`func (o *PullRequest) GetMergedAtOk() (*time.Time, bool)`

GetMergedAtOk returns a tuple with the MergedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergedAt

`func (o *PullRequest) SetMergedAt(v time.Time)`

SetMergedAt sets MergedAt field to given value.

### HasMergedAt

`func (o *PullRequest) HasMergedAt() bool`

HasMergedAt returns a boolean if a field has been set.

### GetMergedBy

`func (o *PullRequest) GetMergedBy() User`

GetMergedBy returns the MergedBy field if non-nil, zero value otherwise.

### GetMergedByOk

`func (o *PullRequest) GetMergedByOk() (*User, bool)`

GetMergedByOk returns a tuple with the MergedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergedBy

`func (o *PullRequest) SetMergedBy(v User)`

SetMergedBy sets MergedBy field to given value.

### HasMergedBy

`func (o *PullRequest) HasMergedBy() bool`

HasMergedBy returns a boolean if a field has been set.

### GetMilestone

`func (o *PullRequest) GetMilestone() Milestone`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *PullRequest) GetMilestoneOk() (*Milestone, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *PullRequest) SetMilestone(v Milestone)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *PullRequest) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetNumber

`func (o *PullRequest) GetNumber() int64`

GetNumber returns the Number field if non-nil, zero value otherwise.

### GetNumberOk

`func (o *PullRequest) GetNumberOk() (*int64, bool)`

GetNumberOk returns a tuple with the Number field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumber

`func (o *PullRequest) SetNumber(v int64)`

SetNumber sets Number field to given value.

### HasNumber

`func (o *PullRequest) HasNumber() bool`

HasNumber returns a boolean if a field has been set.

### GetPatchUrl

`func (o *PullRequest) GetPatchUrl() string`

GetPatchUrl returns the PatchUrl field if non-nil, zero value otherwise.

### GetPatchUrlOk

`func (o *PullRequest) GetPatchUrlOk() (*string, bool)`

GetPatchUrlOk returns a tuple with the PatchUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPatchUrl

`func (o *PullRequest) SetPatchUrl(v string)`

SetPatchUrl sets PatchUrl field to given value.

### HasPatchUrl

`func (o *PullRequest) HasPatchUrl() bool`

HasPatchUrl returns a boolean if a field has been set.

### GetPinOrder

`func (o *PullRequest) GetPinOrder() int64`

GetPinOrder returns the PinOrder field if non-nil, zero value otherwise.

### GetPinOrderOk

`func (o *PullRequest) GetPinOrderOk() (*int64, bool)`

GetPinOrderOk returns a tuple with the PinOrder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPinOrder

`func (o *PullRequest) SetPinOrder(v int64)`

SetPinOrder sets PinOrder field to given value.

### HasPinOrder

`func (o *PullRequest) HasPinOrder() bool`

HasPinOrder returns a boolean if a field has been set.

### GetRequestedReviewers

`func (o *PullRequest) GetRequestedReviewers() []User`

GetRequestedReviewers returns the RequestedReviewers field if non-nil, zero value otherwise.

### GetRequestedReviewersOk

`func (o *PullRequest) GetRequestedReviewersOk() (*[]User, bool)`

GetRequestedReviewersOk returns a tuple with the RequestedReviewers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestedReviewers

`func (o *PullRequest) SetRequestedReviewers(v []User)`

SetRequestedReviewers sets RequestedReviewers field to given value.

### HasRequestedReviewers

`func (o *PullRequest) HasRequestedReviewers() bool`

HasRequestedReviewers returns a boolean if a field has been set.

### GetState

`func (o *PullRequest) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *PullRequest) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *PullRequest) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *PullRequest) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *PullRequest) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *PullRequest) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *PullRequest) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *PullRequest) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *PullRequest) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *PullRequest) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *PullRequest) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *PullRequest) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUrl

`func (o *PullRequest) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *PullRequest) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *PullRequest) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *PullRequest) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetUser

`func (o *PullRequest) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *PullRequest) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *PullRequest) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *PullRequest) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



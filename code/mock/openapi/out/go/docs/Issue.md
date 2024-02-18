# Issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assets** | Pointer to [**[]Attachment**](Attachment.md) |  | [optional] 
**Assignee** | Pointer to [**User**](User.md) |  | [optional] 
**Assignees** | Pointer to [**[]User**](User.md) |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**ClosedAt** | Pointer to **time.Time** |  | [optional] 
**Comments** | Pointer to **int64** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**DueDate** | Pointer to **time.Time** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IsLocked** | Pointer to **bool** |  | [optional] 
**Labels** | Pointer to [**[]Label**](Label.md) |  | [optional] 
**Milestone** | Pointer to [**Milestone**](Milestone.md) |  | [optional] 
**Number** | Pointer to **int64** |  | [optional] 
**OriginalAuthor** | Pointer to **string** |  | [optional] 
**OriginalAuthorId** | Pointer to **int64** |  | [optional] 
**PinOrder** | Pointer to **int64** |  | [optional] 
**PullRequest** | Pointer to [**PullRequestMeta**](PullRequestMeta.md) |  | [optional] 
**Ref** | Pointer to **string** |  | [optional] 
**Repository** | Pointer to [**RepositoryMeta**](RepositoryMeta.md) |  | [optional] 
**State** | Pointer to **string** | StateType issue state type | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewIssue

`func NewIssue() *Issue`

NewIssue instantiates a new Issue object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIssueWithDefaults

`func NewIssueWithDefaults() *Issue`

NewIssueWithDefaults instantiates a new Issue object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssets

`func (o *Issue) GetAssets() []Attachment`

GetAssets returns the Assets field if non-nil, zero value otherwise.

### GetAssetsOk

`func (o *Issue) GetAssetsOk() (*[]Attachment, bool)`

GetAssetsOk returns a tuple with the Assets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssets

`func (o *Issue) SetAssets(v []Attachment)`

SetAssets sets Assets field to given value.

### HasAssets

`func (o *Issue) HasAssets() bool`

HasAssets returns a boolean if a field has been set.

### GetAssignee

`func (o *Issue) GetAssignee() User`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *Issue) GetAssigneeOk() (*User, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *Issue) SetAssignee(v User)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *Issue) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssignees

`func (o *Issue) GetAssignees() []User`

GetAssignees returns the Assignees field if non-nil, zero value otherwise.

### GetAssigneesOk

`func (o *Issue) GetAssigneesOk() (*[]User, bool)`

GetAssigneesOk returns a tuple with the Assignees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignees

`func (o *Issue) SetAssignees(v []User)`

SetAssignees sets Assignees field to given value.

### HasAssignees

`func (o *Issue) HasAssignees() bool`

HasAssignees returns a boolean if a field has been set.

### GetBody

`func (o *Issue) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *Issue) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *Issue) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *Issue) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetClosedAt

`func (o *Issue) GetClosedAt() time.Time`

GetClosedAt returns the ClosedAt field if non-nil, zero value otherwise.

### GetClosedAtOk

`func (o *Issue) GetClosedAtOk() (*time.Time, bool)`

GetClosedAtOk returns a tuple with the ClosedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedAt

`func (o *Issue) SetClosedAt(v time.Time)`

SetClosedAt sets ClosedAt field to given value.

### HasClosedAt

`func (o *Issue) HasClosedAt() bool`

HasClosedAt returns a boolean if a field has been set.

### GetComments

`func (o *Issue) GetComments() int64`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *Issue) GetCommentsOk() (*int64, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *Issue) SetComments(v int64)`

SetComments sets Comments field to given value.

### HasComments

`func (o *Issue) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Issue) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Issue) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Issue) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Issue) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDueDate

`func (o *Issue) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *Issue) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *Issue) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.

### HasDueDate

`func (o *Issue) HasDueDate() bool`

HasDueDate returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *Issue) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *Issue) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *Issue) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *Issue) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *Issue) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Issue) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Issue) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Issue) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIsLocked

`func (o *Issue) GetIsLocked() bool`

GetIsLocked returns the IsLocked field if non-nil, zero value otherwise.

### GetIsLockedOk

`func (o *Issue) GetIsLockedOk() (*bool, bool)`

GetIsLockedOk returns a tuple with the IsLocked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsLocked

`func (o *Issue) SetIsLocked(v bool)`

SetIsLocked sets IsLocked field to given value.

### HasIsLocked

`func (o *Issue) HasIsLocked() bool`

HasIsLocked returns a boolean if a field has been set.

### GetLabels

`func (o *Issue) GetLabels() []Label`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *Issue) GetLabelsOk() (*[]Label, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *Issue) SetLabels(v []Label)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *Issue) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetMilestone

`func (o *Issue) GetMilestone() Milestone`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *Issue) GetMilestoneOk() (*Milestone, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *Issue) SetMilestone(v Milestone)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *Issue) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetNumber

`func (o *Issue) GetNumber() int64`

GetNumber returns the Number field if non-nil, zero value otherwise.

### GetNumberOk

`func (o *Issue) GetNumberOk() (*int64, bool)`

GetNumberOk returns a tuple with the Number field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumber

`func (o *Issue) SetNumber(v int64)`

SetNumber sets Number field to given value.

### HasNumber

`func (o *Issue) HasNumber() bool`

HasNumber returns a boolean if a field has been set.

### GetOriginalAuthor

`func (o *Issue) GetOriginalAuthor() string`

GetOriginalAuthor returns the OriginalAuthor field if non-nil, zero value otherwise.

### GetOriginalAuthorOk

`func (o *Issue) GetOriginalAuthorOk() (*string, bool)`

GetOriginalAuthorOk returns a tuple with the OriginalAuthor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalAuthor

`func (o *Issue) SetOriginalAuthor(v string)`

SetOriginalAuthor sets OriginalAuthor field to given value.

### HasOriginalAuthor

`func (o *Issue) HasOriginalAuthor() bool`

HasOriginalAuthor returns a boolean if a field has been set.

### GetOriginalAuthorId

`func (o *Issue) GetOriginalAuthorId() int64`

GetOriginalAuthorId returns the OriginalAuthorId field if non-nil, zero value otherwise.

### GetOriginalAuthorIdOk

`func (o *Issue) GetOriginalAuthorIdOk() (*int64, bool)`

GetOriginalAuthorIdOk returns a tuple with the OriginalAuthorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalAuthorId

`func (o *Issue) SetOriginalAuthorId(v int64)`

SetOriginalAuthorId sets OriginalAuthorId field to given value.

### HasOriginalAuthorId

`func (o *Issue) HasOriginalAuthorId() bool`

HasOriginalAuthorId returns a boolean if a field has been set.

### GetPinOrder

`func (o *Issue) GetPinOrder() int64`

GetPinOrder returns the PinOrder field if non-nil, zero value otherwise.

### GetPinOrderOk

`func (o *Issue) GetPinOrderOk() (*int64, bool)`

GetPinOrderOk returns a tuple with the PinOrder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPinOrder

`func (o *Issue) SetPinOrder(v int64)`

SetPinOrder sets PinOrder field to given value.

### HasPinOrder

`func (o *Issue) HasPinOrder() bool`

HasPinOrder returns a boolean if a field has been set.

### GetPullRequest

`func (o *Issue) GetPullRequest() PullRequestMeta`

GetPullRequest returns the PullRequest field if non-nil, zero value otherwise.

### GetPullRequestOk

`func (o *Issue) GetPullRequestOk() (*PullRequestMeta, bool)`

GetPullRequestOk returns a tuple with the PullRequest field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequest

`func (o *Issue) SetPullRequest(v PullRequestMeta)`

SetPullRequest sets PullRequest field to given value.

### HasPullRequest

`func (o *Issue) HasPullRequest() bool`

HasPullRequest returns a boolean if a field has been set.

### GetRef

`func (o *Issue) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *Issue) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *Issue) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *Issue) HasRef() bool`

HasRef returns a boolean if a field has been set.

### GetRepository

`func (o *Issue) GetRepository() RepositoryMeta`

GetRepository returns the Repository field if non-nil, zero value otherwise.

### GetRepositoryOk

`func (o *Issue) GetRepositoryOk() (*RepositoryMeta, bool)`

GetRepositoryOk returns a tuple with the Repository field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepository

`func (o *Issue) SetRepository(v RepositoryMeta)`

SetRepository sets Repository field to given value.

### HasRepository

`func (o *Issue) HasRepository() bool`

HasRepository returns a boolean if a field has been set.

### GetState

`func (o *Issue) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Issue) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Issue) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *Issue) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *Issue) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *Issue) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *Issue) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *Issue) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Issue) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Issue) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Issue) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Issue) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUrl

`func (o *Issue) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Issue) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Issue) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *Issue) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetUser

`func (o *Issue) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *Issue) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *Issue) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *Issue) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



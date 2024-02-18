# TimelineComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assignee** | Pointer to [**User**](User.md) |  | [optional] 
**AssigneeTeam** | Pointer to [**Team**](Team.md) |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**DependentIssue** | Pointer to [**Issue**](Issue.md) |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IssueUrl** | Pointer to **string** |  | [optional] 
**Label** | Pointer to [**Label**](Label.md) |  | [optional] 
**Milestone** | Pointer to [**Milestone**](Milestone.md) |  | [optional] 
**NewRef** | Pointer to **string** |  | [optional] 
**NewTitle** | Pointer to **string** |  | [optional] 
**OldMilestone** | Pointer to [**Milestone**](Milestone.md) |  | [optional] 
**OldProjectId** | Pointer to **int64** |  | [optional] 
**OldRef** | Pointer to **string** |  | [optional] 
**OldTitle** | Pointer to **string** |  | [optional] 
**ProjectId** | Pointer to **int64** |  | [optional] 
**PullRequestUrl** | Pointer to **string** |  | [optional] 
**RefAction** | Pointer to **string** |  | [optional] 
**RefComment** | Pointer to [**Comment**](Comment.md) |  | [optional] 
**RefCommitSha** | Pointer to **string** | commit SHA where issue/PR was referenced | [optional] 
**RefIssue** | Pointer to [**Issue**](Issue.md) |  | [optional] 
**RemovedAssignee** | Pointer to **bool** | whether the assignees were removed or added | [optional] 
**ResolveDoer** | Pointer to [**User**](User.md) |  | [optional] 
**ReviewId** | Pointer to **int64** |  | [optional] 
**TrackedTime** | Pointer to [**TrackedTime**](TrackedTime.md) |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewTimelineComment

`func NewTimelineComment() *TimelineComment`

NewTimelineComment instantiates a new TimelineComment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimelineCommentWithDefaults

`func NewTimelineCommentWithDefaults() *TimelineComment`

NewTimelineCommentWithDefaults instantiates a new TimelineComment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignee

`func (o *TimelineComment) GetAssignee() User`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *TimelineComment) GetAssigneeOk() (*User, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *TimelineComment) SetAssignee(v User)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *TimelineComment) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssigneeTeam

`func (o *TimelineComment) GetAssigneeTeam() Team`

GetAssigneeTeam returns the AssigneeTeam field if non-nil, zero value otherwise.

### GetAssigneeTeamOk

`func (o *TimelineComment) GetAssigneeTeamOk() (*Team, bool)`

GetAssigneeTeamOk returns a tuple with the AssigneeTeam field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssigneeTeam

`func (o *TimelineComment) SetAssigneeTeam(v Team)`

SetAssigneeTeam sets AssigneeTeam field to given value.

### HasAssigneeTeam

`func (o *TimelineComment) HasAssigneeTeam() bool`

HasAssigneeTeam returns a boolean if a field has been set.

### GetBody

`func (o *TimelineComment) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *TimelineComment) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *TimelineComment) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *TimelineComment) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetCreatedAt

`func (o *TimelineComment) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TimelineComment) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TimelineComment) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *TimelineComment) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDependentIssue

`func (o *TimelineComment) GetDependentIssue() Issue`

GetDependentIssue returns the DependentIssue field if non-nil, zero value otherwise.

### GetDependentIssueOk

`func (o *TimelineComment) GetDependentIssueOk() (*Issue, bool)`

GetDependentIssueOk returns a tuple with the DependentIssue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependentIssue

`func (o *TimelineComment) SetDependentIssue(v Issue)`

SetDependentIssue sets DependentIssue field to given value.

### HasDependentIssue

`func (o *TimelineComment) HasDependentIssue() bool`

HasDependentIssue returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *TimelineComment) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *TimelineComment) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *TimelineComment) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *TimelineComment) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *TimelineComment) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TimelineComment) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TimelineComment) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *TimelineComment) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIssueUrl

`func (o *TimelineComment) GetIssueUrl() string`

GetIssueUrl returns the IssueUrl field if non-nil, zero value otherwise.

### GetIssueUrlOk

`func (o *TimelineComment) GetIssueUrlOk() (*string, bool)`

GetIssueUrlOk returns a tuple with the IssueUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUrl

`func (o *TimelineComment) SetIssueUrl(v string)`

SetIssueUrl sets IssueUrl field to given value.

### HasIssueUrl

`func (o *TimelineComment) HasIssueUrl() bool`

HasIssueUrl returns a boolean if a field has been set.

### GetLabel

`func (o *TimelineComment) GetLabel() Label`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *TimelineComment) GetLabelOk() (*Label, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *TimelineComment) SetLabel(v Label)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *TimelineComment) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetMilestone

`func (o *TimelineComment) GetMilestone() Milestone`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *TimelineComment) GetMilestoneOk() (*Milestone, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *TimelineComment) SetMilestone(v Milestone)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *TimelineComment) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetNewRef

`func (o *TimelineComment) GetNewRef() string`

GetNewRef returns the NewRef field if non-nil, zero value otherwise.

### GetNewRefOk

`func (o *TimelineComment) GetNewRefOk() (*string, bool)`

GetNewRefOk returns a tuple with the NewRef field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewRef

`func (o *TimelineComment) SetNewRef(v string)`

SetNewRef sets NewRef field to given value.

### HasNewRef

`func (o *TimelineComment) HasNewRef() bool`

HasNewRef returns a boolean if a field has been set.

### GetNewTitle

`func (o *TimelineComment) GetNewTitle() string`

GetNewTitle returns the NewTitle field if non-nil, zero value otherwise.

### GetNewTitleOk

`func (o *TimelineComment) GetNewTitleOk() (*string, bool)`

GetNewTitleOk returns a tuple with the NewTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewTitle

`func (o *TimelineComment) SetNewTitle(v string)`

SetNewTitle sets NewTitle field to given value.

### HasNewTitle

`func (o *TimelineComment) HasNewTitle() bool`

HasNewTitle returns a boolean if a field has been set.

### GetOldMilestone

`func (o *TimelineComment) GetOldMilestone() Milestone`

GetOldMilestone returns the OldMilestone field if non-nil, zero value otherwise.

### GetOldMilestoneOk

`func (o *TimelineComment) GetOldMilestoneOk() (*Milestone, bool)`

GetOldMilestoneOk returns a tuple with the OldMilestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldMilestone

`func (o *TimelineComment) SetOldMilestone(v Milestone)`

SetOldMilestone sets OldMilestone field to given value.

### HasOldMilestone

`func (o *TimelineComment) HasOldMilestone() bool`

HasOldMilestone returns a boolean if a field has been set.

### GetOldProjectId

`func (o *TimelineComment) GetOldProjectId() int64`

GetOldProjectId returns the OldProjectId field if non-nil, zero value otherwise.

### GetOldProjectIdOk

`func (o *TimelineComment) GetOldProjectIdOk() (*int64, bool)`

GetOldProjectIdOk returns a tuple with the OldProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldProjectId

`func (o *TimelineComment) SetOldProjectId(v int64)`

SetOldProjectId sets OldProjectId field to given value.

### HasOldProjectId

`func (o *TimelineComment) HasOldProjectId() bool`

HasOldProjectId returns a boolean if a field has been set.

### GetOldRef

`func (o *TimelineComment) GetOldRef() string`

GetOldRef returns the OldRef field if non-nil, zero value otherwise.

### GetOldRefOk

`func (o *TimelineComment) GetOldRefOk() (*string, bool)`

GetOldRefOk returns a tuple with the OldRef field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldRef

`func (o *TimelineComment) SetOldRef(v string)`

SetOldRef sets OldRef field to given value.

### HasOldRef

`func (o *TimelineComment) HasOldRef() bool`

HasOldRef returns a boolean if a field has been set.

### GetOldTitle

`func (o *TimelineComment) GetOldTitle() string`

GetOldTitle returns the OldTitle field if non-nil, zero value otherwise.

### GetOldTitleOk

`func (o *TimelineComment) GetOldTitleOk() (*string, bool)`

GetOldTitleOk returns a tuple with the OldTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldTitle

`func (o *TimelineComment) SetOldTitle(v string)`

SetOldTitle sets OldTitle field to given value.

### HasOldTitle

`func (o *TimelineComment) HasOldTitle() bool`

HasOldTitle returns a boolean if a field has been set.

### GetProjectId

`func (o *TimelineComment) GetProjectId() int64`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *TimelineComment) GetProjectIdOk() (*int64, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *TimelineComment) SetProjectId(v int64)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *TimelineComment) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetPullRequestUrl

`func (o *TimelineComment) GetPullRequestUrl() string`

GetPullRequestUrl returns the PullRequestUrl field if non-nil, zero value otherwise.

### GetPullRequestUrlOk

`func (o *TimelineComment) GetPullRequestUrlOk() (*string, bool)`

GetPullRequestUrlOk returns a tuple with the PullRequestUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequestUrl

`func (o *TimelineComment) SetPullRequestUrl(v string)`

SetPullRequestUrl sets PullRequestUrl field to given value.

### HasPullRequestUrl

`func (o *TimelineComment) HasPullRequestUrl() bool`

HasPullRequestUrl returns a boolean if a field has been set.

### GetRefAction

`func (o *TimelineComment) GetRefAction() string`

GetRefAction returns the RefAction field if non-nil, zero value otherwise.

### GetRefActionOk

`func (o *TimelineComment) GetRefActionOk() (*string, bool)`

GetRefActionOk returns a tuple with the RefAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefAction

`func (o *TimelineComment) SetRefAction(v string)`

SetRefAction sets RefAction field to given value.

### HasRefAction

`func (o *TimelineComment) HasRefAction() bool`

HasRefAction returns a boolean if a field has been set.

### GetRefComment

`func (o *TimelineComment) GetRefComment() Comment`

GetRefComment returns the RefComment field if non-nil, zero value otherwise.

### GetRefCommentOk

`func (o *TimelineComment) GetRefCommentOk() (*Comment, bool)`

GetRefCommentOk returns a tuple with the RefComment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefComment

`func (o *TimelineComment) SetRefComment(v Comment)`

SetRefComment sets RefComment field to given value.

### HasRefComment

`func (o *TimelineComment) HasRefComment() bool`

HasRefComment returns a boolean if a field has been set.

### GetRefCommitSha

`func (o *TimelineComment) GetRefCommitSha() string`

GetRefCommitSha returns the RefCommitSha field if non-nil, zero value otherwise.

### GetRefCommitShaOk

`func (o *TimelineComment) GetRefCommitShaOk() (*string, bool)`

GetRefCommitShaOk returns a tuple with the RefCommitSha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefCommitSha

`func (o *TimelineComment) SetRefCommitSha(v string)`

SetRefCommitSha sets RefCommitSha field to given value.

### HasRefCommitSha

`func (o *TimelineComment) HasRefCommitSha() bool`

HasRefCommitSha returns a boolean if a field has been set.

### GetRefIssue

`func (o *TimelineComment) GetRefIssue() Issue`

GetRefIssue returns the RefIssue field if non-nil, zero value otherwise.

### GetRefIssueOk

`func (o *TimelineComment) GetRefIssueOk() (*Issue, bool)`

GetRefIssueOk returns a tuple with the RefIssue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefIssue

`func (o *TimelineComment) SetRefIssue(v Issue)`

SetRefIssue sets RefIssue field to given value.

### HasRefIssue

`func (o *TimelineComment) HasRefIssue() bool`

HasRefIssue returns a boolean if a field has been set.

### GetRemovedAssignee

`func (o *TimelineComment) GetRemovedAssignee() bool`

GetRemovedAssignee returns the RemovedAssignee field if non-nil, zero value otherwise.

### GetRemovedAssigneeOk

`func (o *TimelineComment) GetRemovedAssigneeOk() (*bool, bool)`

GetRemovedAssigneeOk returns a tuple with the RemovedAssignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemovedAssignee

`func (o *TimelineComment) SetRemovedAssignee(v bool)`

SetRemovedAssignee sets RemovedAssignee field to given value.

### HasRemovedAssignee

`func (o *TimelineComment) HasRemovedAssignee() bool`

HasRemovedAssignee returns a boolean if a field has been set.

### GetResolveDoer

`func (o *TimelineComment) GetResolveDoer() User`

GetResolveDoer returns the ResolveDoer field if non-nil, zero value otherwise.

### GetResolveDoerOk

`func (o *TimelineComment) GetResolveDoerOk() (*User, bool)`

GetResolveDoerOk returns a tuple with the ResolveDoer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResolveDoer

`func (o *TimelineComment) SetResolveDoer(v User)`

SetResolveDoer sets ResolveDoer field to given value.

### HasResolveDoer

`func (o *TimelineComment) HasResolveDoer() bool`

HasResolveDoer returns a boolean if a field has been set.

### GetReviewId

`func (o *TimelineComment) GetReviewId() int64`

GetReviewId returns the ReviewId field if non-nil, zero value otherwise.

### GetReviewIdOk

`func (o *TimelineComment) GetReviewIdOk() (*int64, bool)`

GetReviewIdOk returns a tuple with the ReviewId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewId

`func (o *TimelineComment) SetReviewId(v int64)`

SetReviewId sets ReviewId field to given value.

### HasReviewId

`func (o *TimelineComment) HasReviewId() bool`

HasReviewId returns a boolean if a field has been set.

### GetTrackedTime

`func (o *TimelineComment) GetTrackedTime() TrackedTime`

GetTrackedTime returns the TrackedTime field if non-nil, zero value otherwise.

### GetTrackedTimeOk

`func (o *TimelineComment) GetTrackedTimeOk() (*TrackedTime, bool)`

GetTrackedTimeOk returns a tuple with the TrackedTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedTime

`func (o *TimelineComment) SetTrackedTime(v TrackedTime)`

SetTrackedTime sets TrackedTime field to given value.

### HasTrackedTime

`func (o *TimelineComment) HasTrackedTime() bool`

HasTrackedTime returns a boolean if a field has been set.

### GetType

`func (o *TimelineComment) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TimelineComment) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TimelineComment) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *TimelineComment) HasType() bool`

HasType returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *TimelineComment) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *TimelineComment) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *TimelineComment) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *TimelineComment) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUser

`func (o *TimelineComment) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *TimelineComment) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *TimelineComment) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *TimelineComment) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



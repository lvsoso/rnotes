# PullReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** |  | [optional] 
**CommentsCount** | Pointer to **int64** |  | [optional] 
**CommitId** | Pointer to **string** |  | [optional] 
**Dismissed** | Pointer to **bool** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**Official** | Pointer to **bool** |  | [optional] 
**PullRequestUrl** | Pointer to **string** |  | [optional] 
**Stale** | Pointer to **bool** |  | [optional] 
**State** | Pointer to **string** | ReviewStateType review state type | [optional] 
**SubmittedAt** | Pointer to **time.Time** |  | [optional] 
**Team** | Pointer to [**Team**](Team.md) |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewPullReview

`func NewPullReview() *PullReview`

NewPullReview instantiates a new PullReview object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPullReviewWithDefaults

`func NewPullReviewWithDefaults() *PullReview`

NewPullReviewWithDefaults instantiates a new PullReview object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBody

`func (o *PullReview) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *PullReview) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *PullReview) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *PullReview) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetCommentsCount

`func (o *PullReview) GetCommentsCount() int64`

GetCommentsCount returns the CommentsCount field if non-nil, zero value otherwise.

### GetCommentsCountOk

`func (o *PullReview) GetCommentsCountOk() (*int64, bool)`

GetCommentsCountOk returns a tuple with the CommentsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommentsCount

`func (o *PullReview) SetCommentsCount(v int64)`

SetCommentsCount sets CommentsCount field to given value.

### HasCommentsCount

`func (o *PullReview) HasCommentsCount() bool`

HasCommentsCount returns a boolean if a field has been set.

### GetCommitId

`func (o *PullReview) GetCommitId() string`

GetCommitId returns the CommitId field if non-nil, zero value otherwise.

### GetCommitIdOk

`func (o *PullReview) GetCommitIdOk() (*string, bool)`

GetCommitIdOk returns a tuple with the CommitId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitId

`func (o *PullReview) SetCommitId(v string)`

SetCommitId sets CommitId field to given value.

### HasCommitId

`func (o *PullReview) HasCommitId() bool`

HasCommitId returns a boolean if a field has been set.

### GetDismissed

`func (o *PullReview) GetDismissed() bool`

GetDismissed returns the Dismissed field if non-nil, zero value otherwise.

### GetDismissedOk

`func (o *PullReview) GetDismissedOk() (*bool, bool)`

GetDismissedOk returns a tuple with the Dismissed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDismissed

`func (o *PullReview) SetDismissed(v bool)`

SetDismissed sets Dismissed field to given value.

### HasDismissed

`func (o *PullReview) HasDismissed() bool`

HasDismissed returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *PullReview) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *PullReview) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *PullReview) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *PullReview) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *PullReview) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PullReview) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PullReview) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *PullReview) HasId() bool`

HasId returns a boolean if a field has been set.

### GetOfficial

`func (o *PullReview) GetOfficial() bool`

GetOfficial returns the Official field if non-nil, zero value otherwise.

### GetOfficialOk

`func (o *PullReview) GetOfficialOk() (*bool, bool)`

GetOfficialOk returns a tuple with the Official field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOfficial

`func (o *PullReview) SetOfficial(v bool)`

SetOfficial sets Official field to given value.

### HasOfficial

`func (o *PullReview) HasOfficial() bool`

HasOfficial returns a boolean if a field has been set.

### GetPullRequestUrl

`func (o *PullReview) GetPullRequestUrl() string`

GetPullRequestUrl returns the PullRequestUrl field if non-nil, zero value otherwise.

### GetPullRequestUrlOk

`func (o *PullReview) GetPullRequestUrlOk() (*string, bool)`

GetPullRequestUrlOk returns a tuple with the PullRequestUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequestUrl

`func (o *PullReview) SetPullRequestUrl(v string)`

SetPullRequestUrl sets PullRequestUrl field to given value.

### HasPullRequestUrl

`func (o *PullReview) HasPullRequestUrl() bool`

HasPullRequestUrl returns a boolean if a field has been set.

### GetStale

`func (o *PullReview) GetStale() bool`

GetStale returns the Stale field if non-nil, zero value otherwise.

### GetStaleOk

`func (o *PullReview) GetStaleOk() (*bool, bool)`

GetStaleOk returns a tuple with the Stale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStale

`func (o *PullReview) SetStale(v bool)`

SetStale sets Stale field to given value.

### HasStale

`func (o *PullReview) HasStale() bool`

HasStale returns a boolean if a field has been set.

### GetState

`func (o *PullReview) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *PullReview) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *PullReview) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *PullReview) HasState() bool`

HasState returns a boolean if a field has been set.

### GetSubmittedAt

`func (o *PullReview) GetSubmittedAt() time.Time`

GetSubmittedAt returns the SubmittedAt field if non-nil, zero value otherwise.

### GetSubmittedAtOk

`func (o *PullReview) GetSubmittedAtOk() (*time.Time, bool)`

GetSubmittedAtOk returns a tuple with the SubmittedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubmittedAt

`func (o *PullReview) SetSubmittedAt(v time.Time)`

SetSubmittedAt sets SubmittedAt field to given value.

### HasSubmittedAt

`func (o *PullReview) HasSubmittedAt() bool`

HasSubmittedAt returns a boolean if a field has been set.

### GetTeam

`func (o *PullReview) GetTeam() Team`

GetTeam returns the Team field if non-nil, zero value otherwise.

### GetTeamOk

`func (o *PullReview) GetTeamOk() (*Team, bool)`

GetTeamOk returns a tuple with the Team field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeam

`func (o *PullReview) SetTeam(v Team)`

SetTeam sets Team field to given value.

### HasTeam

`func (o *PullReview) HasTeam() bool`

HasTeam returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *PullReview) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *PullReview) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *PullReview) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *PullReview) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUser

`func (o *PullReview) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *PullReview) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *PullReview) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *PullReview) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



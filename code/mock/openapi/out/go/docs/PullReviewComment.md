# PullReviewComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** |  | [optional] 
**CommitId** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**DiffHunk** | Pointer to **string** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**OriginalCommitId** | Pointer to **string** |  | [optional] 
**OriginalPosition** | Pointer to **int32** |  | [optional] 
**Path** | Pointer to **string** |  | [optional] 
**Position** | Pointer to **int32** |  | [optional] 
**PullRequestReviewId** | Pointer to **int64** |  | [optional] 
**PullRequestUrl** | Pointer to **string** |  | [optional] 
**Resolver** | Pointer to [**User**](User.md) |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewPullReviewComment

`func NewPullReviewComment() *PullReviewComment`

NewPullReviewComment instantiates a new PullReviewComment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPullReviewCommentWithDefaults

`func NewPullReviewCommentWithDefaults() *PullReviewComment`

NewPullReviewCommentWithDefaults instantiates a new PullReviewComment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBody

`func (o *PullReviewComment) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *PullReviewComment) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *PullReviewComment) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *PullReviewComment) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetCommitId

`func (o *PullReviewComment) GetCommitId() string`

GetCommitId returns the CommitId field if non-nil, zero value otherwise.

### GetCommitIdOk

`func (o *PullReviewComment) GetCommitIdOk() (*string, bool)`

GetCommitIdOk returns a tuple with the CommitId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitId

`func (o *PullReviewComment) SetCommitId(v string)`

SetCommitId sets CommitId field to given value.

### HasCommitId

`func (o *PullReviewComment) HasCommitId() bool`

HasCommitId returns a boolean if a field has been set.

### GetCreatedAt

`func (o *PullReviewComment) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *PullReviewComment) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *PullReviewComment) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *PullReviewComment) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDiffHunk

`func (o *PullReviewComment) GetDiffHunk() string`

GetDiffHunk returns the DiffHunk field if non-nil, zero value otherwise.

### GetDiffHunkOk

`func (o *PullReviewComment) GetDiffHunkOk() (*string, bool)`

GetDiffHunkOk returns a tuple with the DiffHunk field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffHunk

`func (o *PullReviewComment) SetDiffHunk(v string)`

SetDiffHunk sets DiffHunk field to given value.

### HasDiffHunk

`func (o *PullReviewComment) HasDiffHunk() bool`

HasDiffHunk returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *PullReviewComment) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *PullReviewComment) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *PullReviewComment) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *PullReviewComment) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *PullReviewComment) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PullReviewComment) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PullReviewComment) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *PullReviewComment) HasId() bool`

HasId returns a boolean if a field has been set.

### GetOriginalCommitId

`func (o *PullReviewComment) GetOriginalCommitId() string`

GetOriginalCommitId returns the OriginalCommitId field if non-nil, zero value otherwise.

### GetOriginalCommitIdOk

`func (o *PullReviewComment) GetOriginalCommitIdOk() (*string, bool)`

GetOriginalCommitIdOk returns a tuple with the OriginalCommitId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalCommitId

`func (o *PullReviewComment) SetOriginalCommitId(v string)`

SetOriginalCommitId sets OriginalCommitId field to given value.

### HasOriginalCommitId

`func (o *PullReviewComment) HasOriginalCommitId() bool`

HasOriginalCommitId returns a boolean if a field has been set.

### GetOriginalPosition

`func (o *PullReviewComment) GetOriginalPosition() int32`

GetOriginalPosition returns the OriginalPosition field if non-nil, zero value otherwise.

### GetOriginalPositionOk

`func (o *PullReviewComment) GetOriginalPositionOk() (*int32, bool)`

GetOriginalPositionOk returns a tuple with the OriginalPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalPosition

`func (o *PullReviewComment) SetOriginalPosition(v int32)`

SetOriginalPosition sets OriginalPosition field to given value.

### HasOriginalPosition

`func (o *PullReviewComment) HasOriginalPosition() bool`

HasOriginalPosition returns a boolean if a field has been set.

### GetPath

`func (o *PullReviewComment) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *PullReviewComment) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *PullReviewComment) SetPath(v string)`

SetPath sets Path field to given value.

### HasPath

`func (o *PullReviewComment) HasPath() bool`

HasPath returns a boolean if a field has been set.

### GetPosition

`func (o *PullReviewComment) GetPosition() int32`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *PullReviewComment) GetPositionOk() (*int32, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *PullReviewComment) SetPosition(v int32)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *PullReviewComment) HasPosition() bool`

HasPosition returns a boolean if a field has been set.

### GetPullRequestReviewId

`func (o *PullReviewComment) GetPullRequestReviewId() int64`

GetPullRequestReviewId returns the PullRequestReviewId field if non-nil, zero value otherwise.

### GetPullRequestReviewIdOk

`func (o *PullReviewComment) GetPullRequestReviewIdOk() (*int64, bool)`

GetPullRequestReviewIdOk returns a tuple with the PullRequestReviewId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequestReviewId

`func (o *PullReviewComment) SetPullRequestReviewId(v int64)`

SetPullRequestReviewId sets PullRequestReviewId field to given value.

### HasPullRequestReviewId

`func (o *PullReviewComment) HasPullRequestReviewId() bool`

HasPullRequestReviewId returns a boolean if a field has been set.

### GetPullRequestUrl

`func (o *PullReviewComment) GetPullRequestUrl() string`

GetPullRequestUrl returns the PullRequestUrl field if non-nil, zero value otherwise.

### GetPullRequestUrlOk

`func (o *PullReviewComment) GetPullRequestUrlOk() (*string, bool)`

GetPullRequestUrlOk returns a tuple with the PullRequestUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequestUrl

`func (o *PullReviewComment) SetPullRequestUrl(v string)`

SetPullRequestUrl sets PullRequestUrl field to given value.

### HasPullRequestUrl

`func (o *PullReviewComment) HasPullRequestUrl() bool`

HasPullRequestUrl returns a boolean if a field has been set.

### GetResolver

`func (o *PullReviewComment) GetResolver() User`

GetResolver returns the Resolver field if non-nil, zero value otherwise.

### GetResolverOk

`func (o *PullReviewComment) GetResolverOk() (*User, bool)`

GetResolverOk returns a tuple with the Resolver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResolver

`func (o *PullReviewComment) SetResolver(v User)`

SetResolver sets Resolver field to given value.

### HasResolver

`func (o *PullReviewComment) HasResolver() bool`

HasResolver returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *PullReviewComment) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *PullReviewComment) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *PullReviewComment) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *PullReviewComment) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUser

`func (o *PullReviewComment) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *PullReviewComment) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *PullReviewComment) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *PullReviewComment) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



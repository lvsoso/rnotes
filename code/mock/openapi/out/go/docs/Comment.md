# Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assets** | Pointer to [**[]Attachment**](Attachment.md) |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IssueUrl** | Pointer to **string** |  | [optional] 
**OriginalAuthor** | Pointer to **string** |  | [optional] 
**OriginalAuthorId** | Pointer to **int64** |  | [optional] 
**PullRequestUrl** | Pointer to **string** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewComment

`func NewComment() *Comment`

NewComment instantiates a new Comment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCommentWithDefaults

`func NewCommentWithDefaults() *Comment`

NewCommentWithDefaults instantiates a new Comment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssets

`func (o *Comment) GetAssets() []Attachment`

GetAssets returns the Assets field if non-nil, zero value otherwise.

### GetAssetsOk

`func (o *Comment) GetAssetsOk() (*[]Attachment, bool)`

GetAssetsOk returns a tuple with the Assets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssets

`func (o *Comment) SetAssets(v []Attachment)`

SetAssets sets Assets field to given value.

### HasAssets

`func (o *Comment) HasAssets() bool`

HasAssets returns a boolean if a field has been set.

### GetBody

`func (o *Comment) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *Comment) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *Comment) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *Comment) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Comment) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Comment) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Comment) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Comment) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *Comment) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *Comment) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *Comment) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *Comment) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *Comment) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Comment) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Comment) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Comment) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIssueUrl

`func (o *Comment) GetIssueUrl() string`

GetIssueUrl returns the IssueUrl field if non-nil, zero value otherwise.

### GetIssueUrlOk

`func (o *Comment) GetIssueUrlOk() (*string, bool)`

GetIssueUrlOk returns a tuple with the IssueUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUrl

`func (o *Comment) SetIssueUrl(v string)`

SetIssueUrl sets IssueUrl field to given value.

### HasIssueUrl

`func (o *Comment) HasIssueUrl() bool`

HasIssueUrl returns a boolean if a field has been set.

### GetOriginalAuthor

`func (o *Comment) GetOriginalAuthor() string`

GetOriginalAuthor returns the OriginalAuthor field if non-nil, zero value otherwise.

### GetOriginalAuthorOk

`func (o *Comment) GetOriginalAuthorOk() (*string, bool)`

GetOriginalAuthorOk returns a tuple with the OriginalAuthor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalAuthor

`func (o *Comment) SetOriginalAuthor(v string)`

SetOriginalAuthor sets OriginalAuthor field to given value.

### HasOriginalAuthor

`func (o *Comment) HasOriginalAuthor() bool`

HasOriginalAuthor returns a boolean if a field has been set.

### GetOriginalAuthorId

`func (o *Comment) GetOriginalAuthorId() int64`

GetOriginalAuthorId returns the OriginalAuthorId field if non-nil, zero value otherwise.

### GetOriginalAuthorIdOk

`func (o *Comment) GetOriginalAuthorIdOk() (*int64, bool)`

GetOriginalAuthorIdOk returns a tuple with the OriginalAuthorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalAuthorId

`func (o *Comment) SetOriginalAuthorId(v int64)`

SetOriginalAuthorId sets OriginalAuthorId field to given value.

### HasOriginalAuthorId

`func (o *Comment) HasOriginalAuthorId() bool`

HasOriginalAuthorId returns a boolean if a field has been set.

### GetPullRequestUrl

`func (o *Comment) GetPullRequestUrl() string`

GetPullRequestUrl returns the PullRequestUrl field if non-nil, zero value otherwise.

### GetPullRequestUrlOk

`func (o *Comment) GetPullRequestUrlOk() (*string, bool)`

GetPullRequestUrlOk returns a tuple with the PullRequestUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequestUrl

`func (o *Comment) SetPullRequestUrl(v string)`

SetPullRequestUrl sets PullRequestUrl field to given value.

### HasPullRequestUrl

`func (o *Comment) HasPullRequestUrl() bool`

HasPullRequestUrl returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Comment) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Comment) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Comment) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Comment) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUser

`func (o *Comment) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *Comment) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *Comment) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *Comment) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



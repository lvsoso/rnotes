# Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActUser** | Pointer to [**User**](User.md) |  | [optional] 
**ActUserId** | Pointer to **int64** |  | [optional] 
**Comment** | Pointer to [**Comment**](Comment.md) |  | [optional] 
**CommentId** | Pointer to **int64** |  | [optional] 
**Content** | Pointer to **string** |  | [optional] 
**Created** | Pointer to **time.Time** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IsPrivate** | Pointer to **bool** |  | [optional] 
**OpType** | Pointer to **string** |  | [optional] 
**RefName** | Pointer to **string** |  | [optional] 
**Repo** | Pointer to [**Repository**](Repository.md) |  | [optional] 
**RepoId** | Pointer to **int64** |  | [optional] 
**UserId** | Pointer to **int64** |  | [optional] 

## Methods

### NewActivity

`func NewActivity() *Activity`

NewActivity instantiates a new Activity object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewActivityWithDefaults

`func NewActivityWithDefaults() *Activity`

NewActivityWithDefaults instantiates a new Activity object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActUser

`func (o *Activity) GetActUser() User`

GetActUser returns the ActUser field if non-nil, zero value otherwise.

### GetActUserOk

`func (o *Activity) GetActUserOk() (*User, bool)`

GetActUserOk returns a tuple with the ActUser field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActUser

`func (o *Activity) SetActUser(v User)`

SetActUser sets ActUser field to given value.

### HasActUser

`func (o *Activity) HasActUser() bool`

HasActUser returns a boolean if a field has been set.

### GetActUserId

`func (o *Activity) GetActUserId() int64`

GetActUserId returns the ActUserId field if non-nil, zero value otherwise.

### GetActUserIdOk

`func (o *Activity) GetActUserIdOk() (*int64, bool)`

GetActUserIdOk returns a tuple with the ActUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActUserId

`func (o *Activity) SetActUserId(v int64)`

SetActUserId sets ActUserId field to given value.

### HasActUserId

`func (o *Activity) HasActUserId() bool`

HasActUserId returns a boolean if a field has been set.

### GetComment

`func (o *Activity) GetComment() Comment`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *Activity) GetCommentOk() (*Comment, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *Activity) SetComment(v Comment)`

SetComment sets Comment field to given value.

### HasComment

`func (o *Activity) HasComment() bool`

HasComment returns a boolean if a field has been set.

### GetCommentId

`func (o *Activity) GetCommentId() int64`

GetCommentId returns the CommentId field if non-nil, zero value otherwise.

### GetCommentIdOk

`func (o *Activity) GetCommentIdOk() (*int64, bool)`

GetCommentIdOk returns a tuple with the CommentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommentId

`func (o *Activity) SetCommentId(v int64)`

SetCommentId sets CommentId field to given value.

### HasCommentId

`func (o *Activity) HasCommentId() bool`

HasCommentId returns a boolean if a field has been set.

### GetContent

`func (o *Activity) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *Activity) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *Activity) SetContent(v string)`

SetContent sets Content field to given value.

### HasContent

`func (o *Activity) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetCreated

`func (o *Activity) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *Activity) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *Activity) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *Activity) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetId

`func (o *Activity) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Activity) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Activity) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Activity) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIsPrivate

`func (o *Activity) GetIsPrivate() bool`

GetIsPrivate returns the IsPrivate field if non-nil, zero value otherwise.

### GetIsPrivateOk

`func (o *Activity) GetIsPrivateOk() (*bool, bool)`

GetIsPrivateOk returns a tuple with the IsPrivate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPrivate

`func (o *Activity) SetIsPrivate(v bool)`

SetIsPrivate sets IsPrivate field to given value.

### HasIsPrivate

`func (o *Activity) HasIsPrivate() bool`

HasIsPrivate returns a boolean if a field has been set.

### GetOpType

`func (o *Activity) GetOpType() string`

GetOpType returns the OpType field if non-nil, zero value otherwise.

### GetOpTypeOk

`func (o *Activity) GetOpTypeOk() (*string, bool)`

GetOpTypeOk returns a tuple with the OpType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpType

`func (o *Activity) SetOpType(v string)`

SetOpType sets OpType field to given value.

### HasOpType

`func (o *Activity) HasOpType() bool`

HasOpType returns a boolean if a field has been set.

### GetRefName

`func (o *Activity) GetRefName() string`

GetRefName returns the RefName field if non-nil, zero value otherwise.

### GetRefNameOk

`func (o *Activity) GetRefNameOk() (*string, bool)`

GetRefNameOk returns a tuple with the RefName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefName

`func (o *Activity) SetRefName(v string)`

SetRefName sets RefName field to given value.

### HasRefName

`func (o *Activity) HasRefName() bool`

HasRefName returns a boolean if a field has been set.

### GetRepo

`func (o *Activity) GetRepo() Repository`

GetRepo returns the Repo field if non-nil, zero value otherwise.

### GetRepoOk

`func (o *Activity) GetRepoOk() (*Repository, bool)`

GetRepoOk returns a tuple with the Repo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepo

`func (o *Activity) SetRepo(v Repository)`

SetRepo sets Repo field to given value.

### HasRepo

`func (o *Activity) HasRepo() bool`

HasRepo returns a boolean if a field has been set.

### GetRepoId

`func (o *Activity) GetRepoId() int64`

GetRepoId returns the RepoId field if non-nil, zero value otherwise.

### GetRepoIdOk

`func (o *Activity) GetRepoIdOk() (*int64, bool)`

GetRepoIdOk returns a tuple with the RepoId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoId

`func (o *Activity) SetRepoId(v int64)`

SetRepoId sets RepoId field to given value.

### HasRepoId

`func (o *Activity) HasRepoId() bool`

HasRepoId returns a boolean if a field has been set.

### GetUserId

`func (o *Activity) GetUserId() int64`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *Activity) GetUserIdOk() (*int64, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *Activity) SetUserId(v int64)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *Activity) HasUserId() bool`

HasUserId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



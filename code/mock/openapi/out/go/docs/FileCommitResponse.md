# FileCommitResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Committer** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Created** | Pointer to **time.Time** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Message** | Pointer to **string** |  | [optional] 
**Parents** | Pointer to [**[]CommitMeta**](CommitMeta.md) |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**Tree** | Pointer to [**CommitMeta**](CommitMeta.md) |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewFileCommitResponse

`func NewFileCommitResponse() *FileCommitResponse`

NewFileCommitResponse instantiates a new FileCommitResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileCommitResponseWithDefaults

`func NewFileCommitResponseWithDefaults() *FileCommitResponse`

NewFileCommitResponseWithDefaults instantiates a new FileCommitResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *FileCommitResponse) GetAuthor() CommitUser`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *FileCommitResponse) GetAuthorOk() (*CommitUser, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *FileCommitResponse) SetAuthor(v CommitUser)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *FileCommitResponse) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetCommitter

`func (o *FileCommitResponse) GetCommitter() CommitUser`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *FileCommitResponse) GetCommitterOk() (*CommitUser, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *FileCommitResponse) SetCommitter(v CommitUser)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *FileCommitResponse) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetCreated

`func (o *FileCommitResponse) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *FileCommitResponse) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *FileCommitResponse) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *FileCommitResponse) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *FileCommitResponse) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *FileCommitResponse) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *FileCommitResponse) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *FileCommitResponse) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetMessage

`func (o *FileCommitResponse) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *FileCommitResponse) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *FileCommitResponse) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *FileCommitResponse) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetParents

`func (o *FileCommitResponse) GetParents() []CommitMeta`

GetParents returns the Parents field if non-nil, zero value otherwise.

### GetParentsOk

`func (o *FileCommitResponse) GetParentsOk() (*[]CommitMeta, bool)`

GetParentsOk returns a tuple with the Parents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParents

`func (o *FileCommitResponse) SetParents(v []CommitMeta)`

SetParents sets Parents field to given value.

### HasParents

`func (o *FileCommitResponse) HasParents() bool`

HasParents returns a boolean if a field has been set.

### GetSha

`func (o *FileCommitResponse) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *FileCommitResponse) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *FileCommitResponse) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *FileCommitResponse) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetTree

`func (o *FileCommitResponse) GetTree() CommitMeta`

GetTree returns the Tree field if non-nil, zero value otherwise.

### GetTreeOk

`func (o *FileCommitResponse) GetTreeOk() (*CommitMeta, bool)`

GetTreeOk returns a tuple with the Tree field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTree

`func (o *FileCommitResponse) SetTree(v CommitMeta)`

SetTree sets Tree field to given value.

### HasTree

`func (o *FileCommitResponse) HasTree() bool`

HasTree returns a boolean if a field has been set.

### GetUrl

`func (o *FileCommitResponse) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *FileCommitResponse) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *FileCommitResponse) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *FileCommitResponse) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



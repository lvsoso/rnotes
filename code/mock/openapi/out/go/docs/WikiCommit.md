# WikiCommit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Commiter** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Message** | Pointer to **string** |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 

## Methods

### NewWikiCommit

`func NewWikiCommit() *WikiCommit`

NewWikiCommit instantiates a new WikiCommit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWikiCommitWithDefaults

`func NewWikiCommitWithDefaults() *WikiCommit`

NewWikiCommitWithDefaults instantiates a new WikiCommit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *WikiCommit) GetAuthor() CommitUser`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *WikiCommit) GetAuthorOk() (*CommitUser, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *WikiCommit) SetAuthor(v CommitUser)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *WikiCommit) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetCommiter

`func (o *WikiCommit) GetCommiter() CommitUser`

GetCommiter returns the Commiter field if non-nil, zero value otherwise.

### GetCommiterOk

`func (o *WikiCommit) GetCommiterOk() (*CommitUser, bool)`

GetCommiterOk returns a tuple with the Commiter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommiter

`func (o *WikiCommit) SetCommiter(v CommitUser)`

SetCommiter sets Commiter field to given value.

### HasCommiter

`func (o *WikiCommit) HasCommiter() bool`

HasCommiter returns a boolean if a field has been set.

### GetMessage

`func (o *WikiCommit) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *WikiCommit) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *WikiCommit) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *WikiCommit) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetSha

`func (o *WikiCommit) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *WikiCommit) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *WikiCommit) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *WikiCommit) HasSha() bool`

HasSha returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RepoCommit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Committer** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Message** | Pointer to **string** |  | [optional] 
**Tree** | Pointer to [**CommitMeta**](CommitMeta.md) |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**Verification** | Pointer to [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Methods

### NewRepoCommit

`func NewRepoCommit() *RepoCommit`

NewRepoCommit instantiates a new RepoCommit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepoCommitWithDefaults

`func NewRepoCommitWithDefaults() *RepoCommit`

NewRepoCommitWithDefaults instantiates a new RepoCommit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *RepoCommit) GetAuthor() CommitUser`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *RepoCommit) GetAuthorOk() (*CommitUser, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *RepoCommit) SetAuthor(v CommitUser)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *RepoCommit) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetCommitter

`func (o *RepoCommit) GetCommitter() CommitUser`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *RepoCommit) GetCommitterOk() (*CommitUser, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *RepoCommit) SetCommitter(v CommitUser)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *RepoCommit) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetMessage

`func (o *RepoCommit) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *RepoCommit) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *RepoCommit) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *RepoCommit) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetTree

`func (o *RepoCommit) GetTree() CommitMeta`

GetTree returns the Tree field if non-nil, zero value otherwise.

### GetTreeOk

`func (o *RepoCommit) GetTreeOk() (*CommitMeta, bool)`

GetTreeOk returns a tuple with the Tree field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTree

`func (o *RepoCommit) SetTree(v CommitMeta)`

SetTree sets Tree field to given value.

### HasTree

`func (o *RepoCommit) HasTree() bool`

HasTree returns a boolean if a field has been set.

### GetUrl

`func (o *RepoCommit) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *RepoCommit) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *RepoCommit) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *RepoCommit) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetVerification

`func (o *RepoCommit) GetVerification() PayloadCommitVerification`

GetVerification returns the Verification field if non-nil, zero value otherwise.

### GetVerificationOk

`func (o *RepoCommit) GetVerificationOk() (*PayloadCommitVerification, bool)`

GetVerificationOk returns a tuple with the Verification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerification

`func (o *RepoCommit) SetVerification(v PayloadCommitVerification)`

SetVerification sets Verification field to given value.

### HasVerification

`func (o *RepoCommit) HasVerification() bool`

HasVerification returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



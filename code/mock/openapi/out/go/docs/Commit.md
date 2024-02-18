# Commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**User**](User.md) |  | [optional] 
**Commit** | Pointer to [**RepoCommit**](RepoCommit.md) |  | [optional] 
**Committer** | Pointer to [**User**](User.md) |  | [optional] 
**Created** | Pointer to **time.Time** |  | [optional] 
**Files** | Pointer to [**[]CommitAffectedFiles**](CommitAffectedFiles.md) |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Parents** | Pointer to [**[]CommitMeta**](CommitMeta.md) |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**Stats** | Pointer to [**CommitStats**](CommitStats.md) |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewCommit

`func NewCommit() *Commit`

NewCommit instantiates a new Commit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCommitWithDefaults

`func NewCommitWithDefaults() *Commit`

NewCommitWithDefaults instantiates a new Commit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *Commit) GetAuthor() User`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *Commit) GetAuthorOk() (*User, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *Commit) SetAuthor(v User)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *Commit) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetCommit

`func (o *Commit) GetCommit() RepoCommit`

GetCommit returns the Commit field if non-nil, zero value otherwise.

### GetCommitOk

`func (o *Commit) GetCommitOk() (*RepoCommit, bool)`

GetCommitOk returns a tuple with the Commit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommit

`func (o *Commit) SetCommit(v RepoCommit)`

SetCommit sets Commit field to given value.

### HasCommit

`func (o *Commit) HasCommit() bool`

HasCommit returns a boolean if a field has been set.

### GetCommitter

`func (o *Commit) GetCommitter() User`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *Commit) GetCommitterOk() (*User, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *Commit) SetCommitter(v User)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *Commit) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetCreated

`func (o *Commit) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *Commit) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *Commit) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *Commit) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetFiles

`func (o *Commit) GetFiles() []CommitAffectedFiles`

GetFiles returns the Files field if non-nil, zero value otherwise.

### GetFilesOk

`func (o *Commit) GetFilesOk() (*[]CommitAffectedFiles, bool)`

GetFilesOk returns a tuple with the Files field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiles

`func (o *Commit) SetFiles(v []CommitAffectedFiles)`

SetFiles sets Files field to given value.

### HasFiles

`func (o *Commit) HasFiles() bool`

HasFiles returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *Commit) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *Commit) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *Commit) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *Commit) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetParents

`func (o *Commit) GetParents() []CommitMeta`

GetParents returns the Parents field if non-nil, zero value otherwise.

### GetParentsOk

`func (o *Commit) GetParentsOk() (*[]CommitMeta, bool)`

GetParentsOk returns a tuple with the Parents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParents

`func (o *Commit) SetParents(v []CommitMeta)`

SetParents sets Parents field to given value.

### HasParents

`func (o *Commit) HasParents() bool`

HasParents returns a boolean if a field has been set.

### GetSha

`func (o *Commit) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *Commit) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *Commit) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *Commit) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetStats

`func (o *Commit) GetStats() CommitStats`

GetStats returns the Stats field if non-nil, zero value otherwise.

### GetStatsOk

`func (o *Commit) GetStatsOk() (*CommitStats, bool)`

GetStatsOk returns a tuple with the Stats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStats

`func (o *Commit) SetStats(v CommitStats)`

SetStats sets Stats field to given value.

### HasStats

`func (o *Commit) HasStats() bool`

HasStats returns a boolean if a field has been set.

### GetUrl

`func (o *Commit) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Commit) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Commit) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *Commit) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



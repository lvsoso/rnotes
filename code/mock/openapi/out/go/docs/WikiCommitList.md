# WikiCommitList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Commits** | Pointer to [**[]WikiCommit**](WikiCommit.md) |  | [optional] 
**Count** | Pointer to **int64** |  | [optional] 

## Methods

### NewWikiCommitList

`func NewWikiCommitList() *WikiCommitList`

NewWikiCommitList instantiates a new WikiCommitList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWikiCommitListWithDefaults

`func NewWikiCommitListWithDefaults() *WikiCommitList`

NewWikiCommitListWithDefaults instantiates a new WikiCommitList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommits

`func (o *WikiCommitList) GetCommits() []WikiCommit`

GetCommits returns the Commits field if non-nil, zero value otherwise.

### GetCommitsOk

`func (o *WikiCommitList) GetCommitsOk() (*[]WikiCommit, bool)`

GetCommitsOk returns a tuple with the Commits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommits

`func (o *WikiCommitList) SetCommits(v []WikiCommit)`

SetCommits sets Commits field to given value.

### HasCommits

`func (o *WikiCommitList) HasCommits() bool`

HasCommits returns a boolean if a field has been set.

### GetCount

`func (o *WikiCommitList) GetCount() int64`

GetCount returns the Count field if non-nil, zero value otherwise.

### GetCountOk

`func (o *WikiCommitList) GetCountOk() (*int64, bool)`

GetCountOk returns a tuple with the Count field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCount

`func (o *WikiCommitList) SetCount(v int64)`

SetCount sets Count field to given value.

### HasCount

`func (o *WikiCommitList) HasCount() bool`

HasCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



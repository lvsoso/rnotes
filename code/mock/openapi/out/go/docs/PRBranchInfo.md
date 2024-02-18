# PRBranchInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Label** | Pointer to **string** |  | [optional] 
**Ref** | Pointer to **string** |  | [optional] 
**Repo** | Pointer to [**Repository**](Repository.md) |  | [optional] 
**RepoId** | Pointer to **int64** |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 

## Methods

### NewPRBranchInfo

`func NewPRBranchInfo() *PRBranchInfo`

NewPRBranchInfo instantiates a new PRBranchInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPRBranchInfoWithDefaults

`func NewPRBranchInfoWithDefaults() *PRBranchInfo`

NewPRBranchInfoWithDefaults instantiates a new PRBranchInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLabel

`func (o *PRBranchInfo) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *PRBranchInfo) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *PRBranchInfo) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *PRBranchInfo) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetRef

`func (o *PRBranchInfo) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *PRBranchInfo) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *PRBranchInfo) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *PRBranchInfo) HasRef() bool`

HasRef returns a boolean if a field has been set.

### GetRepo

`func (o *PRBranchInfo) GetRepo() Repository`

GetRepo returns the Repo field if non-nil, zero value otherwise.

### GetRepoOk

`func (o *PRBranchInfo) GetRepoOk() (*Repository, bool)`

GetRepoOk returns a tuple with the Repo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepo

`func (o *PRBranchInfo) SetRepo(v Repository)`

SetRepo sets Repo field to given value.

### HasRepo

`func (o *PRBranchInfo) HasRepo() bool`

HasRepo returns a boolean if a field has been set.

### GetRepoId

`func (o *PRBranchInfo) GetRepoId() int64`

GetRepoId returns the RepoId field if non-nil, zero value otherwise.

### GetRepoIdOk

`func (o *PRBranchInfo) GetRepoIdOk() (*int64, bool)`

GetRepoIdOk returns a tuple with the RepoId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoId

`func (o *PRBranchInfo) SetRepoId(v int64)`

SetRepoId sets RepoId field to given value.

### HasRepoId

`func (o *PRBranchInfo) HasRepoId() bool`

HasRepoId returns a boolean if a field has been set.

### GetSha

`func (o *PRBranchInfo) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *PRBranchInfo) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *PRBranchInfo) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *PRBranchInfo) HasSha() bool`

HasSha returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



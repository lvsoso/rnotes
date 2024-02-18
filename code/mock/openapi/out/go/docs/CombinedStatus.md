# CombinedStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CommitUrl** | Pointer to **string** |  | [optional] 
**Repository** | Pointer to [**Repository**](Repository.md) |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**State** | Pointer to **string** | CommitStatusState holds the state of a CommitStatus It can be \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot; and \&quot;failure\&quot; | [optional] 
**Statuses** | Pointer to [**[]CommitStatus**](CommitStatus.md) |  | [optional] 
**TotalCount** | Pointer to **int64** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewCombinedStatus

`func NewCombinedStatus() *CombinedStatus`

NewCombinedStatus instantiates a new CombinedStatus object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCombinedStatusWithDefaults

`func NewCombinedStatusWithDefaults() *CombinedStatus`

NewCombinedStatusWithDefaults instantiates a new CombinedStatus object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommitUrl

`func (o *CombinedStatus) GetCommitUrl() string`

GetCommitUrl returns the CommitUrl field if non-nil, zero value otherwise.

### GetCommitUrlOk

`func (o *CombinedStatus) GetCommitUrlOk() (*string, bool)`

GetCommitUrlOk returns a tuple with the CommitUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitUrl

`func (o *CombinedStatus) SetCommitUrl(v string)`

SetCommitUrl sets CommitUrl field to given value.

### HasCommitUrl

`func (o *CombinedStatus) HasCommitUrl() bool`

HasCommitUrl returns a boolean if a field has been set.

### GetRepository

`func (o *CombinedStatus) GetRepository() Repository`

GetRepository returns the Repository field if non-nil, zero value otherwise.

### GetRepositoryOk

`func (o *CombinedStatus) GetRepositoryOk() (*Repository, bool)`

GetRepositoryOk returns a tuple with the Repository field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepository

`func (o *CombinedStatus) SetRepository(v Repository)`

SetRepository sets Repository field to given value.

### HasRepository

`func (o *CombinedStatus) HasRepository() bool`

HasRepository returns a boolean if a field has been set.

### GetSha

`func (o *CombinedStatus) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *CombinedStatus) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *CombinedStatus) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *CombinedStatus) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetState

`func (o *CombinedStatus) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *CombinedStatus) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *CombinedStatus) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *CombinedStatus) HasState() bool`

HasState returns a boolean if a field has been set.

### GetStatuses

`func (o *CombinedStatus) GetStatuses() []CommitStatus`

GetStatuses returns the Statuses field if non-nil, zero value otherwise.

### GetStatusesOk

`func (o *CombinedStatus) GetStatusesOk() (*[]CommitStatus, bool)`

GetStatusesOk returns a tuple with the Statuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatuses

`func (o *CombinedStatus) SetStatuses(v []CommitStatus)`

SetStatuses sets Statuses field to given value.

### HasStatuses

`func (o *CombinedStatus) HasStatuses() bool`

HasStatuses returns a boolean if a field has been set.

### GetTotalCount

`func (o *CombinedStatus) GetTotalCount() int64`

GetTotalCount returns the TotalCount field if non-nil, zero value otherwise.

### GetTotalCountOk

`func (o *CombinedStatus) GetTotalCountOk() (*int64, bool)`

GetTotalCountOk returns a tuple with the TotalCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCount

`func (o *CombinedStatus) SetTotalCount(v int64)`

SetTotalCount sets TotalCount field to given value.

### HasTotalCount

`func (o *CombinedStatus) HasTotalCount() bool`

HasTotalCount returns a boolean if a field has been set.

### GetUrl

`func (o *CombinedStatus) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *CombinedStatus) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *CombinedStatus) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *CombinedStatus) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



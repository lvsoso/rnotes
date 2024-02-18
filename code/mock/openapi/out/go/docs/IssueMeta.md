# IssueMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Index** | Pointer to **int64** |  | [optional] 
**Owner** | Pointer to **string** |  | [optional] 
**Repo** | Pointer to **string** |  | [optional] 

## Methods

### NewIssueMeta

`func NewIssueMeta() *IssueMeta`

NewIssueMeta instantiates a new IssueMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIssueMetaWithDefaults

`func NewIssueMetaWithDefaults() *IssueMeta`

NewIssueMetaWithDefaults instantiates a new IssueMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIndex

`func (o *IssueMeta) GetIndex() int64`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *IssueMeta) GetIndexOk() (*int64, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *IssueMeta) SetIndex(v int64)`

SetIndex sets Index field to given value.

### HasIndex

`func (o *IssueMeta) HasIndex() bool`

HasIndex returns a boolean if a field has been set.

### GetOwner

`func (o *IssueMeta) GetOwner() string`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *IssueMeta) GetOwnerOk() (*string, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *IssueMeta) SetOwner(v string)`

SetOwner sets Owner field to given value.

### HasOwner

`func (o *IssueMeta) HasOwner() bool`

HasOwner returns a boolean if a field has been set.

### GetRepo

`func (o *IssueMeta) GetRepo() string`

GetRepo returns the Repo field if non-nil, zero value otherwise.

### GetRepoOk

`func (o *IssueMeta) GetRepoOk() (*string, bool)`

GetRepoOk returns a tuple with the Repo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepo

`func (o *IssueMeta) SetRepo(v string)`

SetRepo sets Repo field to given value.

### HasRepo

`func (o *IssueMeta) HasRepo() bool`

HasRepo returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



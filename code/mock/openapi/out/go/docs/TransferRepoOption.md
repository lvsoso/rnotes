# TransferRepoOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NewOwner** | **string** |  | 
**TeamIds** | Pointer to **[]int64** | ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories. | [optional] 

## Methods

### NewTransferRepoOption

`func NewTransferRepoOption(newOwner string, ) *TransferRepoOption`

NewTransferRepoOption instantiates a new TransferRepoOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTransferRepoOptionWithDefaults

`func NewTransferRepoOptionWithDefaults() *TransferRepoOption`

NewTransferRepoOptionWithDefaults instantiates a new TransferRepoOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNewOwner

`func (o *TransferRepoOption) GetNewOwner() string`

GetNewOwner returns the NewOwner field if non-nil, zero value otherwise.

### GetNewOwnerOk

`func (o *TransferRepoOption) GetNewOwnerOk() (*string, bool)`

GetNewOwnerOk returns a tuple with the NewOwner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewOwner

`func (o *TransferRepoOption) SetNewOwner(v string)`

SetNewOwner sets NewOwner field to given value.


### GetTeamIds

`func (o *TransferRepoOption) GetTeamIds() []int64`

GetTeamIds returns the TeamIds field if non-nil, zero value otherwise.

### GetTeamIdsOk

`func (o *TransferRepoOption) GetTeamIdsOk() (*[]int64, bool)`

GetTeamIdsOk returns a tuple with the TeamIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamIds

`func (o *TransferRepoOption) SetTeamIds(v []int64)`

SetTeamIds sets TeamIds field to given value.

### HasTeamIds

`func (o *TransferRepoOption) HasTeamIds() bool`

HasTeamIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



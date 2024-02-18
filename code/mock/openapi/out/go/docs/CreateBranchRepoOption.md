# CreateBranchRepoOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NewBranchName** | **string** | Name of the branch to create | 
**OldBranchName** | Pointer to **string** | Deprecated: true Name of the old branch to create from | [optional] 
**OldRefName** | Pointer to **string** | Name of the old branch/tag/commit to create from | [optional] 

## Methods

### NewCreateBranchRepoOption

`func NewCreateBranchRepoOption(newBranchName string, ) *CreateBranchRepoOption`

NewCreateBranchRepoOption instantiates a new CreateBranchRepoOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateBranchRepoOptionWithDefaults

`func NewCreateBranchRepoOptionWithDefaults() *CreateBranchRepoOption`

NewCreateBranchRepoOptionWithDefaults instantiates a new CreateBranchRepoOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNewBranchName

`func (o *CreateBranchRepoOption) GetNewBranchName() string`

GetNewBranchName returns the NewBranchName field if non-nil, zero value otherwise.

### GetNewBranchNameOk

`func (o *CreateBranchRepoOption) GetNewBranchNameOk() (*string, bool)`

GetNewBranchNameOk returns a tuple with the NewBranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewBranchName

`func (o *CreateBranchRepoOption) SetNewBranchName(v string)`

SetNewBranchName sets NewBranchName field to given value.


### GetOldBranchName

`func (o *CreateBranchRepoOption) GetOldBranchName() string`

GetOldBranchName returns the OldBranchName field if non-nil, zero value otherwise.

### GetOldBranchNameOk

`func (o *CreateBranchRepoOption) GetOldBranchNameOk() (*string, bool)`

GetOldBranchNameOk returns a tuple with the OldBranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldBranchName

`func (o *CreateBranchRepoOption) SetOldBranchName(v string)`

SetOldBranchName sets OldBranchName field to given value.

### HasOldBranchName

`func (o *CreateBranchRepoOption) HasOldBranchName() bool`

HasOldBranchName returns a boolean if a field has been set.

### GetOldRefName

`func (o *CreateBranchRepoOption) GetOldRefName() string`

GetOldRefName returns the OldRefName field if non-nil, zero value otherwise.

### GetOldRefNameOk

`func (o *CreateBranchRepoOption) GetOldRefNameOk() (*string, bool)`

GetOldRefNameOk returns a tuple with the OldRefName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldRefName

`func (o *CreateBranchRepoOption) SetOldRefName(v string)`

SetOldRefName sets OldRefName field to given value.

### HasOldRefName

`func (o *CreateBranchRepoOption) HasOldRefName() bool`

HasOldRefName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



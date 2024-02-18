# EditTeamOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanCreateOrgRepo** | Pointer to **bool** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**IncludesAllRepositories** | Pointer to **bool** |  | [optional] 
**Name** | **string** |  | 
**Permission** | Pointer to **string** |  | [optional] 
**Units** | Pointer to **[]string** |  | [optional] 
**UnitsMap** | Pointer to **map[string]string** |  | [optional] 

## Methods

### NewEditTeamOption

`func NewEditTeamOption(name string, ) *EditTeamOption`

NewEditTeamOption instantiates a new EditTeamOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditTeamOptionWithDefaults

`func NewEditTeamOptionWithDefaults() *EditTeamOption`

NewEditTeamOptionWithDefaults instantiates a new EditTeamOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanCreateOrgRepo

`func (o *EditTeamOption) GetCanCreateOrgRepo() bool`

GetCanCreateOrgRepo returns the CanCreateOrgRepo field if non-nil, zero value otherwise.

### GetCanCreateOrgRepoOk

`func (o *EditTeamOption) GetCanCreateOrgRepoOk() (*bool, bool)`

GetCanCreateOrgRepoOk returns a tuple with the CanCreateOrgRepo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanCreateOrgRepo

`func (o *EditTeamOption) SetCanCreateOrgRepo(v bool)`

SetCanCreateOrgRepo sets CanCreateOrgRepo field to given value.

### HasCanCreateOrgRepo

`func (o *EditTeamOption) HasCanCreateOrgRepo() bool`

HasCanCreateOrgRepo returns a boolean if a field has been set.

### GetDescription

`func (o *EditTeamOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *EditTeamOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *EditTeamOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *EditTeamOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetIncludesAllRepositories

`func (o *EditTeamOption) GetIncludesAllRepositories() bool`

GetIncludesAllRepositories returns the IncludesAllRepositories field if non-nil, zero value otherwise.

### GetIncludesAllRepositoriesOk

`func (o *EditTeamOption) GetIncludesAllRepositoriesOk() (*bool, bool)`

GetIncludesAllRepositoriesOk returns a tuple with the IncludesAllRepositories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludesAllRepositories

`func (o *EditTeamOption) SetIncludesAllRepositories(v bool)`

SetIncludesAllRepositories sets IncludesAllRepositories field to given value.

### HasIncludesAllRepositories

`func (o *EditTeamOption) HasIncludesAllRepositories() bool`

HasIncludesAllRepositories returns a boolean if a field has been set.

### GetName

`func (o *EditTeamOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EditTeamOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *EditTeamOption) SetName(v string)`

SetName sets Name field to given value.


### GetPermission

`func (o *EditTeamOption) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *EditTeamOption) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *EditTeamOption) SetPermission(v string)`

SetPermission sets Permission field to given value.

### HasPermission

`func (o *EditTeamOption) HasPermission() bool`

HasPermission returns a boolean if a field has been set.

### GetUnits

`func (o *EditTeamOption) GetUnits() []string`

GetUnits returns the Units field if non-nil, zero value otherwise.

### GetUnitsOk

`func (o *EditTeamOption) GetUnitsOk() (*[]string, bool)`

GetUnitsOk returns a tuple with the Units field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnits

`func (o *EditTeamOption) SetUnits(v []string)`

SetUnits sets Units field to given value.

### HasUnits

`func (o *EditTeamOption) HasUnits() bool`

HasUnits returns a boolean if a field has been set.

### GetUnitsMap

`func (o *EditTeamOption) GetUnitsMap() map[string]string`

GetUnitsMap returns the UnitsMap field if non-nil, zero value otherwise.

### GetUnitsMapOk

`func (o *EditTeamOption) GetUnitsMapOk() (*map[string]string, bool)`

GetUnitsMapOk returns a tuple with the UnitsMap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnitsMap

`func (o *EditTeamOption) SetUnitsMap(v map[string]string)`

SetUnitsMap sets UnitsMap field to given value.

### HasUnitsMap

`func (o *EditTeamOption) HasUnitsMap() bool`

HasUnitsMap returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



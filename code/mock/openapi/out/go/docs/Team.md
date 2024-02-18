# Team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanCreateOrgRepo** | Pointer to **bool** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IncludesAllRepositories** | Pointer to **bool** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Organization** | Pointer to [**Organization**](Organization.md) |  | [optional] 
**Permission** | Pointer to **string** |  | [optional] 
**Units** | Pointer to **[]string** |  | [optional] 
**UnitsMap** | Pointer to **map[string]string** |  | [optional] 

## Methods

### NewTeam

`func NewTeam() *Team`

NewTeam instantiates a new Team object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamWithDefaults

`func NewTeamWithDefaults() *Team`

NewTeamWithDefaults instantiates a new Team object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanCreateOrgRepo

`func (o *Team) GetCanCreateOrgRepo() bool`

GetCanCreateOrgRepo returns the CanCreateOrgRepo field if non-nil, zero value otherwise.

### GetCanCreateOrgRepoOk

`func (o *Team) GetCanCreateOrgRepoOk() (*bool, bool)`

GetCanCreateOrgRepoOk returns a tuple with the CanCreateOrgRepo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanCreateOrgRepo

`func (o *Team) SetCanCreateOrgRepo(v bool)`

SetCanCreateOrgRepo sets CanCreateOrgRepo field to given value.

### HasCanCreateOrgRepo

`func (o *Team) HasCanCreateOrgRepo() bool`

HasCanCreateOrgRepo returns a boolean if a field has been set.

### GetDescription

`func (o *Team) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Team) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Team) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Team) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetId

`func (o *Team) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Team) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Team) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Team) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIncludesAllRepositories

`func (o *Team) GetIncludesAllRepositories() bool`

GetIncludesAllRepositories returns the IncludesAllRepositories field if non-nil, zero value otherwise.

### GetIncludesAllRepositoriesOk

`func (o *Team) GetIncludesAllRepositoriesOk() (*bool, bool)`

GetIncludesAllRepositoriesOk returns a tuple with the IncludesAllRepositories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludesAllRepositories

`func (o *Team) SetIncludesAllRepositories(v bool)`

SetIncludesAllRepositories sets IncludesAllRepositories field to given value.

### HasIncludesAllRepositories

`func (o *Team) HasIncludesAllRepositories() bool`

HasIncludesAllRepositories returns a boolean if a field has been set.

### GetName

`func (o *Team) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Team) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Team) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Team) HasName() bool`

HasName returns a boolean if a field has been set.

### GetOrganization

`func (o *Team) GetOrganization() Organization`

GetOrganization returns the Organization field if non-nil, zero value otherwise.

### GetOrganizationOk

`func (o *Team) GetOrganizationOk() (*Organization, bool)`

GetOrganizationOk returns a tuple with the Organization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganization

`func (o *Team) SetOrganization(v Organization)`

SetOrganization sets Organization field to given value.

### HasOrganization

`func (o *Team) HasOrganization() bool`

HasOrganization returns a boolean if a field has been set.

### GetPermission

`func (o *Team) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *Team) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *Team) SetPermission(v string)`

SetPermission sets Permission field to given value.

### HasPermission

`func (o *Team) HasPermission() bool`

HasPermission returns a boolean if a field has been set.

### GetUnits

`func (o *Team) GetUnits() []string`

GetUnits returns the Units field if non-nil, zero value otherwise.

### GetUnitsOk

`func (o *Team) GetUnitsOk() (*[]string, bool)`

GetUnitsOk returns a tuple with the Units field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnits

`func (o *Team) SetUnits(v []string)`

SetUnits sets Units field to given value.

### HasUnits

`func (o *Team) HasUnits() bool`

HasUnits returns a boolean if a field has been set.

### GetUnitsMap

`func (o *Team) GetUnitsMap() map[string]string`

GetUnitsMap returns the UnitsMap field if non-nil, zero value otherwise.

### GetUnitsMapOk

`func (o *Team) GetUnitsMapOk() (*map[string]string, bool)`

GetUnitsMapOk returns a tuple with the UnitsMap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnitsMap

`func (o *Team) SetUnitsMap(v map[string]string)`

SetUnitsMap sets UnitsMap field to given value.

### HasUnitsMap

`func (o *Team) HasUnitsMap() bool`

HasUnitsMap returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



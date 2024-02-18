# RepoCollaboratorPermission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Permission** | Pointer to **string** |  | [optional] 
**RoleName** | Pointer to **string** |  | [optional] 
**User** | Pointer to [**User**](User.md) |  | [optional] 

## Methods

### NewRepoCollaboratorPermission

`func NewRepoCollaboratorPermission() *RepoCollaboratorPermission`

NewRepoCollaboratorPermission instantiates a new RepoCollaboratorPermission object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepoCollaboratorPermissionWithDefaults

`func NewRepoCollaboratorPermissionWithDefaults() *RepoCollaboratorPermission`

NewRepoCollaboratorPermissionWithDefaults instantiates a new RepoCollaboratorPermission object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPermission

`func (o *RepoCollaboratorPermission) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *RepoCollaboratorPermission) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *RepoCollaboratorPermission) SetPermission(v string)`

SetPermission sets Permission field to given value.

### HasPermission

`func (o *RepoCollaboratorPermission) HasPermission() bool`

HasPermission returns a boolean if a field has been set.

### GetRoleName

`func (o *RepoCollaboratorPermission) GetRoleName() string`

GetRoleName returns the RoleName field if non-nil, zero value otherwise.

### GetRoleNameOk

`func (o *RepoCollaboratorPermission) GetRoleNameOk() (*string, bool)`

GetRoleNameOk returns a tuple with the RoleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoleName

`func (o *RepoCollaboratorPermission) SetRoleName(v string)`

SetRoleName sets RoleName field to given value.

### HasRoleName

`func (o *RepoCollaboratorPermission) HasRoleName() bool`

HasRoleName returns a boolean if a field has been set.

### GetUser

`func (o *RepoCollaboratorPermission) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *RepoCollaboratorPermission) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *RepoCollaboratorPermission) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *RepoCollaboratorPermission) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



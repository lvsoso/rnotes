# OrganizationPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanCreateRepository** | Pointer to **bool** |  | [optional] 
**CanRead** | Pointer to **bool** |  | [optional] 
**CanWrite** | Pointer to **bool** |  | [optional] 
**IsAdmin** | Pointer to **bool** |  | [optional] 
**IsOwner** | Pointer to **bool** |  | [optional] 

## Methods

### NewOrganizationPermissions

`func NewOrganizationPermissions() *OrganizationPermissions`

NewOrganizationPermissions instantiates a new OrganizationPermissions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrganizationPermissionsWithDefaults

`func NewOrganizationPermissionsWithDefaults() *OrganizationPermissions`

NewOrganizationPermissionsWithDefaults instantiates a new OrganizationPermissions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanCreateRepository

`func (o *OrganizationPermissions) GetCanCreateRepository() bool`

GetCanCreateRepository returns the CanCreateRepository field if non-nil, zero value otherwise.

### GetCanCreateRepositoryOk

`func (o *OrganizationPermissions) GetCanCreateRepositoryOk() (*bool, bool)`

GetCanCreateRepositoryOk returns a tuple with the CanCreateRepository field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanCreateRepository

`func (o *OrganizationPermissions) SetCanCreateRepository(v bool)`

SetCanCreateRepository sets CanCreateRepository field to given value.

### HasCanCreateRepository

`func (o *OrganizationPermissions) HasCanCreateRepository() bool`

HasCanCreateRepository returns a boolean if a field has been set.

### GetCanRead

`func (o *OrganizationPermissions) GetCanRead() bool`

GetCanRead returns the CanRead field if non-nil, zero value otherwise.

### GetCanReadOk

`func (o *OrganizationPermissions) GetCanReadOk() (*bool, bool)`

GetCanReadOk returns a tuple with the CanRead field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanRead

`func (o *OrganizationPermissions) SetCanRead(v bool)`

SetCanRead sets CanRead field to given value.

### HasCanRead

`func (o *OrganizationPermissions) HasCanRead() bool`

HasCanRead returns a boolean if a field has been set.

### GetCanWrite

`func (o *OrganizationPermissions) GetCanWrite() bool`

GetCanWrite returns the CanWrite field if non-nil, zero value otherwise.

### GetCanWriteOk

`func (o *OrganizationPermissions) GetCanWriteOk() (*bool, bool)`

GetCanWriteOk returns a tuple with the CanWrite field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanWrite

`func (o *OrganizationPermissions) SetCanWrite(v bool)`

SetCanWrite sets CanWrite field to given value.

### HasCanWrite

`func (o *OrganizationPermissions) HasCanWrite() bool`

HasCanWrite returns a boolean if a field has been set.

### GetIsAdmin

`func (o *OrganizationPermissions) GetIsAdmin() bool`

GetIsAdmin returns the IsAdmin field if non-nil, zero value otherwise.

### GetIsAdminOk

`func (o *OrganizationPermissions) GetIsAdminOk() (*bool, bool)`

GetIsAdminOk returns a tuple with the IsAdmin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsAdmin

`func (o *OrganizationPermissions) SetIsAdmin(v bool)`

SetIsAdmin sets IsAdmin field to given value.

### HasIsAdmin

`func (o *OrganizationPermissions) HasIsAdmin() bool`

HasIsAdmin returns a boolean if a field has been set.

### GetIsOwner

`func (o *OrganizationPermissions) GetIsOwner() bool`

GetIsOwner returns the IsOwner field if non-nil, zero value otherwise.

### GetIsOwnerOk

`func (o *OrganizationPermissions) GetIsOwnerOk() (*bool, bool)`

GetIsOwnerOk returns a tuple with the IsOwner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsOwner

`func (o *OrganizationPermissions) SetIsOwner(v bool)`

SetIsOwner sets IsOwner field to given value.

### HasIsOwner

`func (o *OrganizationPermissions) HasIsOwner() bool`

HasIsOwner returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



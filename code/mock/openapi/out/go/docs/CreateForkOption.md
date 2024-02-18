# CreateForkOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | name of the forked repository | [optional] 
**Organization** | Pointer to **string** | organization name, if forking into an organization | [optional] 

## Methods

### NewCreateForkOption

`func NewCreateForkOption() *CreateForkOption`

NewCreateForkOption instantiates a new CreateForkOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateForkOptionWithDefaults

`func NewCreateForkOptionWithDefaults() *CreateForkOption`

NewCreateForkOptionWithDefaults instantiates a new CreateForkOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateForkOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateForkOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateForkOption) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CreateForkOption) HasName() bool`

HasName returns a boolean if a field has been set.

### GetOrganization

`func (o *CreateForkOption) GetOrganization() string`

GetOrganization returns the Organization field if non-nil, zero value otherwise.

### GetOrganizationOk

`func (o *CreateForkOption) GetOrganizationOk() (*string, bool)`

GetOrganizationOk returns a tuple with the Organization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganization

`func (o *CreateForkOption) SetOrganization(v string)`

SetOrganization sets Organization field to given value.

### HasOrganization

`func (o *CreateForkOption) HasOrganization() bool`

HasOrganization returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



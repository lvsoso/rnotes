# CreateAccessTokenOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Scopes** | Pointer to **[]string** |  | [optional] 

## Methods

### NewCreateAccessTokenOption

`func NewCreateAccessTokenOption(name string, ) *CreateAccessTokenOption`

NewCreateAccessTokenOption instantiates a new CreateAccessTokenOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAccessTokenOptionWithDefaults

`func NewCreateAccessTokenOptionWithDefaults() *CreateAccessTokenOption`

NewCreateAccessTokenOptionWithDefaults instantiates a new CreateAccessTokenOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateAccessTokenOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateAccessTokenOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateAccessTokenOption) SetName(v string)`

SetName sets Name field to given value.


### GetScopes

`func (o *CreateAccessTokenOption) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *CreateAccessTokenOption) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *CreateAccessTokenOption) SetScopes(v []string)`

SetScopes sets Scopes field to given value.

### HasScopes

`func (o *CreateAccessTokenOption) HasScopes() bool`

HasScopes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



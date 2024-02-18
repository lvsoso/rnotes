# AccessToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Scopes** | Pointer to **[]string** |  | [optional] 
**Sha1** | Pointer to **string** |  | [optional] 
**TokenLastEight** | Pointer to **string** |  | [optional] 

## Methods

### NewAccessToken

`func NewAccessToken() *AccessToken`

NewAccessToken instantiates a new AccessToken object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccessTokenWithDefaults

`func NewAccessTokenWithDefaults() *AccessToken`

NewAccessTokenWithDefaults instantiates a new AccessToken object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AccessToken) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AccessToken) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AccessToken) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *AccessToken) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *AccessToken) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AccessToken) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AccessToken) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *AccessToken) HasName() bool`

HasName returns a boolean if a field has been set.

### GetScopes

`func (o *AccessToken) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *AccessToken) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *AccessToken) SetScopes(v []string)`

SetScopes sets Scopes field to given value.

### HasScopes

`func (o *AccessToken) HasScopes() bool`

HasScopes returns a boolean if a field has been set.

### GetSha1

`func (o *AccessToken) GetSha1() string`

GetSha1 returns the Sha1 field if non-nil, zero value otherwise.

### GetSha1Ok

`func (o *AccessToken) GetSha1Ok() (*string, bool)`

GetSha1Ok returns a tuple with the Sha1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha1

`func (o *AccessToken) SetSha1(v string)`

SetSha1 sets Sha1 field to given value.

### HasSha1

`func (o *AccessToken) HasSha1() bool`

HasSha1 returns a boolean if a field has been set.

### GetTokenLastEight

`func (o *AccessToken) GetTokenLastEight() string`

GetTokenLastEight returns the TokenLastEight field if non-nil, zero value otherwise.

### GetTokenLastEightOk

`func (o *AccessToken) GetTokenLastEightOk() (*string, bool)`

GetTokenLastEightOk returns a tuple with the TokenLastEight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenLastEight

`func (o *AccessToken) SetTokenLastEight(v string)`

SetTokenLastEight sets TokenLastEight field to given value.

### HasTokenLastEight

`func (o *AccessToken) HasTokenLastEight() bool`

HasTokenLastEight returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



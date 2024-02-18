# OAuth2Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClientId** | Pointer to **string** |  | [optional] 
**ClientSecret** | Pointer to **string** |  | [optional] 
**ConfidentialClient** | Pointer to **bool** |  | [optional] 
**Created** | Pointer to **time.Time** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**RedirectUris** | Pointer to **[]string** |  | [optional] 

## Methods

### NewOAuth2Application

`func NewOAuth2Application() *OAuth2Application`

NewOAuth2Application instantiates a new OAuth2Application object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOAuth2ApplicationWithDefaults

`func NewOAuth2ApplicationWithDefaults() *OAuth2Application`

NewOAuth2ApplicationWithDefaults instantiates a new OAuth2Application object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClientId

`func (o *OAuth2Application) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *OAuth2Application) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *OAuth2Application) SetClientId(v string)`

SetClientId sets ClientId field to given value.

### HasClientId

`func (o *OAuth2Application) HasClientId() bool`

HasClientId returns a boolean if a field has been set.

### GetClientSecret

`func (o *OAuth2Application) GetClientSecret() string`

GetClientSecret returns the ClientSecret field if non-nil, zero value otherwise.

### GetClientSecretOk

`func (o *OAuth2Application) GetClientSecretOk() (*string, bool)`

GetClientSecretOk returns a tuple with the ClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientSecret

`func (o *OAuth2Application) SetClientSecret(v string)`

SetClientSecret sets ClientSecret field to given value.

### HasClientSecret

`func (o *OAuth2Application) HasClientSecret() bool`

HasClientSecret returns a boolean if a field has been set.

### GetConfidentialClient

`func (o *OAuth2Application) GetConfidentialClient() bool`

GetConfidentialClient returns the ConfidentialClient field if non-nil, zero value otherwise.

### GetConfidentialClientOk

`func (o *OAuth2Application) GetConfidentialClientOk() (*bool, bool)`

GetConfidentialClientOk returns a tuple with the ConfidentialClient field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfidentialClient

`func (o *OAuth2Application) SetConfidentialClient(v bool)`

SetConfidentialClient sets ConfidentialClient field to given value.

### HasConfidentialClient

`func (o *OAuth2Application) HasConfidentialClient() bool`

HasConfidentialClient returns a boolean if a field has been set.

### GetCreated

`func (o *OAuth2Application) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *OAuth2Application) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *OAuth2Application) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *OAuth2Application) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetId

`func (o *OAuth2Application) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *OAuth2Application) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *OAuth2Application) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *OAuth2Application) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *OAuth2Application) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OAuth2Application) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OAuth2Application) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *OAuth2Application) HasName() bool`

HasName returns a boolean if a field has been set.

### GetRedirectUris

`func (o *OAuth2Application) GetRedirectUris() []string`

GetRedirectUris returns the RedirectUris field if non-nil, zero value otherwise.

### GetRedirectUrisOk

`func (o *OAuth2Application) GetRedirectUrisOk() (*[]string, bool)`

GetRedirectUrisOk returns a tuple with the RedirectUris field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectUris

`func (o *OAuth2Application) SetRedirectUris(v []string)`

SetRedirectUris sets RedirectUris field to given value.

### HasRedirectUris

`func (o *OAuth2Application) HasRedirectUris() bool`

HasRedirectUris returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



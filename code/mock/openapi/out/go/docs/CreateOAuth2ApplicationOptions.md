# CreateOAuth2ApplicationOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ConfidentialClient** | Pointer to **bool** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**RedirectUris** | Pointer to **[]string** |  | [optional] 

## Methods

### NewCreateOAuth2ApplicationOptions

`func NewCreateOAuth2ApplicationOptions() *CreateOAuth2ApplicationOptions`

NewCreateOAuth2ApplicationOptions instantiates a new CreateOAuth2ApplicationOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateOAuth2ApplicationOptionsWithDefaults

`func NewCreateOAuth2ApplicationOptionsWithDefaults() *CreateOAuth2ApplicationOptions`

NewCreateOAuth2ApplicationOptionsWithDefaults instantiates a new CreateOAuth2ApplicationOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetConfidentialClient

`func (o *CreateOAuth2ApplicationOptions) GetConfidentialClient() bool`

GetConfidentialClient returns the ConfidentialClient field if non-nil, zero value otherwise.

### GetConfidentialClientOk

`func (o *CreateOAuth2ApplicationOptions) GetConfidentialClientOk() (*bool, bool)`

GetConfidentialClientOk returns a tuple with the ConfidentialClient field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfidentialClient

`func (o *CreateOAuth2ApplicationOptions) SetConfidentialClient(v bool)`

SetConfidentialClient sets ConfidentialClient field to given value.

### HasConfidentialClient

`func (o *CreateOAuth2ApplicationOptions) HasConfidentialClient() bool`

HasConfidentialClient returns a boolean if a field has been set.

### GetName

`func (o *CreateOAuth2ApplicationOptions) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateOAuth2ApplicationOptions) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateOAuth2ApplicationOptions) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CreateOAuth2ApplicationOptions) HasName() bool`

HasName returns a boolean if a field has been set.

### GetRedirectUris

`func (o *CreateOAuth2ApplicationOptions) GetRedirectUris() []string`

GetRedirectUris returns the RedirectUris field if non-nil, zero value otherwise.

### GetRedirectUrisOk

`func (o *CreateOAuth2ApplicationOptions) GetRedirectUrisOk() (*[]string, bool)`

GetRedirectUrisOk returns a tuple with the RedirectUris field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectUris

`func (o *CreateOAuth2ApplicationOptions) SetRedirectUris(v []string)`

SetRedirectUris sets RedirectUris field to given value.

### HasRedirectUris

`func (o *CreateOAuth2ApplicationOptions) HasRedirectUris() bool`

HasRedirectUris returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



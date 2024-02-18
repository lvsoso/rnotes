# CreateGPGKeyOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArmoredPublicKey** | **string** | An armored GPG key to add | 
**ArmoredSignature** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateGPGKeyOption

`func NewCreateGPGKeyOption(armoredPublicKey string, ) *CreateGPGKeyOption`

NewCreateGPGKeyOption instantiates a new CreateGPGKeyOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateGPGKeyOptionWithDefaults

`func NewCreateGPGKeyOptionWithDefaults() *CreateGPGKeyOption`

NewCreateGPGKeyOptionWithDefaults instantiates a new CreateGPGKeyOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArmoredPublicKey

`func (o *CreateGPGKeyOption) GetArmoredPublicKey() string`

GetArmoredPublicKey returns the ArmoredPublicKey field if non-nil, zero value otherwise.

### GetArmoredPublicKeyOk

`func (o *CreateGPGKeyOption) GetArmoredPublicKeyOk() (*string, bool)`

GetArmoredPublicKeyOk returns a tuple with the ArmoredPublicKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArmoredPublicKey

`func (o *CreateGPGKeyOption) SetArmoredPublicKey(v string)`

SetArmoredPublicKey sets ArmoredPublicKey field to given value.


### GetArmoredSignature

`func (o *CreateGPGKeyOption) GetArmoredSignature() string`

GetArmoredSignature returns the ArmoredSignature field if non-nil, zero value otherwise.

### GetArmoredSignatureOk

`func (o *CreateGPGKeyOption) GetArmoredSignatureOk() (*string, bool)`

GetArmoredSignatureOk returns a tuple with the ArmoredSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArmoredSignature

`func (o *CreateGPGKeyOption) SetArmoredSignature(v string)`

SetArmoredSignature sets ArmoredSignature field to given value.

### HasArmoredSignature

`func (o *CreateGPGKeyOption) HasArmoredSignature() bool`

HasArmoredSignature returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



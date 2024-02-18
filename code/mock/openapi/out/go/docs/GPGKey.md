# GPGKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanCertify** | Pointer to **bool** |  | [optional] 
**CanEncryptComms** | Pointer to **bool** |  | [optional] 
**CanEncryptStorage** | Pointer to **bool** |  | [optional] 
**CanSign** | Pointer to **bool** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**Emails** | Pointer to [**[]GPGKeyEmail**](GPGKeyEmail.md) |  | [optional] 
**ExpiresAt** | Pointer to **time.Time** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**KeyId** | Pointer to **string** |  | [optional] 
**PrimaryKeyId** | Pointer to **string** |  | [optional] 
**PublicKey** | Pointer to **string** |  | [optional] 
**Subkeys** | Pointer to [**[]GPGKey**](GPGKey.md) |  | [optional] 
**Verified** | Pointer to **bool** |  | [optional] 

## Methods

### NewGPGKey

`func NewGPGKey() *GPGKey`

NewGPGKey instantiates a new GPGKey object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGPGKeyWithDefaults

`func NewGPGKeyWithDefaults() *GPGKey`

NewGPGKeyWithDefaults instantiates a new GPGKey object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCanCertify

`func (o *GPGKey) GetCanCertify() bool`

GetCanCertify returns the CanCertify field if non-nil, zero value otherwise.

### GetCanCertifyOk

`func (o *GPGKey) GetCanCertifyOk() (*bool, bool)`

GetCanCertifyOk returns a tuple with the CanCertify field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanCertify

`func (o *GPGKey) SetCanCertify(v bool)`

SetCanCertify sets CanCertify field to given value.

### HasCanCertify

`func (o *GPGKey) HasCanCertify() bool`

HasCanCertify returns a boolean if a field has been set.

### GetCanEncryptComms

`func (o *GPGKey) GetCanEncryptComms() bool`

GetCanEncryptComms returns the CanEncryptComms field if non-nil, zero value otherwise.

### GetCanEncryptCommsOk

`func (o *GPGKey) GetCanEncryptCommsOk() (*bool, bool)`

GetCanEncryptCommsOk returns a tuple with the CanEncryptComms field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanEncryptComms

`func (o *GPGKey) SetCanEncryptComms(v bool)`

SetCanEncryptComms sets CanEncryptComms field to given value.

### HasCanEncryptComms

`func (o *GPGKey) HasCanEncryptComms() bool`

HasCanEncryptComms returns a boolean if a field has been set.

### GetCanEncryptStorage

`func (o *GPGKey) GetCanEncryptStorage() bool`

GetCanEncryptStorage returns the CanEncryptStorage field if non-nil, zero value otherwise.

### GetCanEncryptStorageOk

`func (o *GPGKey) GetCanEncryptStorageOk() (*bool, bool)`

GetCanEncryptStorageOk returns a tuple with the CanEncryptStorage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanEncryptStorage

`func (o *GPGKey) SetCanEncryptStorage(v bool)`

SetCanEncryptStorage sets CanEncryptStorage field to given value.

### HasCanEncryptStorage

`func (o *GPGKey) HasCanEncryptStorage() bool`

HasCanEncryptStorage returns a boolean if a field has been set.

### GetCanSign

`func (o *GPGKey) GetCanSign() bool`

GetCanSign returns the CanSign field if non-nil, zero value otherwise.

### GetCanSignOk

`func (o *GPGKey) GetCanSignOk() (*bool, bool)`

GetCanSignOk returns a tuple with the CanSign field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanSign

`func (o *GPGKey) SetCanSign(v bool)`

SetCanSign sets CanSign field to given value.

### HasCanSign

`func (o *GPGKey) HasCanSign() bool`

HasCanSign returns a boolean if a field has been set.

### GetCreatedAt

`func (o *GPGKey) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *GPGKey) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *GPGKey) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *GPGKey) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetEmails

`func (o *GPGKey) GetEmails() []GPGKeyEmail`

GetEmails returns the Emails field if non-nil, zero value otherwise.

### GetEmailsOk

`func (o *GPGKey) GetEmailsOk() (*[]GPGKeyEmail, bool)`

GetEmailsOk returns a tuple with the Emails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmails

`func (o *GPGKey) SetEmails(v []GPGKeyEmail)`

SetEmails sets Emails field to given value.

### HasEmails

`func (o *GPGKey) HasEmails() bool`

HasEmails returns a boolean if a field has been set.

### GetExpiresAt

`func (o *GPGKey) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GPGKey) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GPGKey) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *GPGKey) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### GetId

`func (o *GPGKey) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GPGKey) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GPGKey) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *GPGKey) HasId() bool`

HasId returns a boolean if a field has been set.

### GetKeyId

`func (o *GPGKey) GetKeyId() string`

GetKeyId returns the KeyId field if non-nil, zero value otherwise.

### GetKeyIdOk

`func (o *GPGKey) GetKeyIdOk() (*string, bool)`

GetKeyIdOk returns a tuple with the KeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeyId

`func (o *GPGKey) SetKeyId(v string)`

SetKeyId sets KeyId field to given value.

### HasKeyId

`func (o *GPGKey) HasKeyId() bool`

HasKeyId returns a boolean if a field has been set.

### GetPrimaryKeyId

`func (o *GPGKey) GetPrimaryKeyId() string`

GetPrimaryKeyId returns the PrimaryKeyId field if non-nil, zero value otherwise.

### GetPrimaryKeyIdOk

`func (o *GPGKey) GetPrimaryKeyIdOk() (*string, bool)`

GetPrimaryKeyIdOk returns a tuple with the PrimaryKeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryKeyId

`func (o *GPGKey) SetPrimaryKeyId(v string)`

SetPrimaryKeyId sets PrimaryKeyId field to given value.

### HasPrimaryKeyId

`func (o *GPGKey) HasPrimaryKeyId() bool`

HasPrimaryKeyId returns a boolean if a field has been set.

### GetPublicKey

`func (o *GPGKey) GetPublicKey() string`

GetPublicKey returns the PublicKey field if non-nil, zero value otherwise.

### GetPublicKeyOk

`func (o *GPGKey) GetPublicKeyOk() (*string, bool)`

GetPublicKeyOk returns a tuple with the PublicKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicKey

`func (o *GPGKey) SetPublicKey(v string)`

SetPublicKey sets PublicKey field to given value.

### HasPublicKey

`func (o *GPGKey) HasPublicKey() bool`

HasPublicKey returns a boolean if a field has been set.

### GetSubkeys

`func (o *GPGKey) GetSubkeys() []GPGKey`

GetSubkeys returns the Subkeys field if non-nil, zero value otherwise.

### GetSubkeysOk

`func (o *GPGKey) GetSubkeysOk() (*[]GPGKey, bool)`

GetSubkeysOk returns a tuple with the Subkeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubkeys

`func (o *GPGKey) SetSubkeys(v []GPGKey)`

SetSubkeys sets Subkeys field to given value.

### HasSubkeys

`func (o *GPGKey) HasSubkeys() bool`

HasSubkeys returns a boolean if a field has been set.

### GetVerified

`func (o *GPGKey) GetVerified() bool`

GetVerified returns the Verified field if non-nil, zero value otherwise.

### GetVerifiedOk

`func (o *GPGKey) GetVerifiedOk() (*bool, bool)`

GetVerifiedOk returns a tuple with the Verified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerified

`func (o *GPGKey) SetVerified(v bool)`

SetVerified sets Verified field to given value.

### HasVerified

`func (o *GPGKey) HasVerified() bool`

HasVerified returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



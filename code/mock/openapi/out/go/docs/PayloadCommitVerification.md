# PayloadCommitVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Payload** | Pointer to **string** |  | [optional] 
**Reason** | Pointer to **string** |  | [optional] 
**Signature** | Pointer to **string** |  | [optional] 
**Signer** | Pointer to [**PayloadUser**](PayloadUser.md) |  | [optional] 
**Verified** | Pointer to **bool** |  | [optional] 

## Methods

### NewPayloadCommitVerification

`func NewPayloadCommitVerification() *PayloadCommitVerification`

NewPayloadCommitVerification instantiates a new PayloadCommitVerification object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPayloadCommitVerificationWithDefaults

`func NewPayloadCommitVerificationWithDefaults() *PayloadCommitVerification`

NewPayloadCommitVerificationWithDefaults instantiates a new PayloadCommitVerification object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPayload

`func (o *PayloadCommitVerification) GetPayload() string`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *PayloadCommitVerification) GetPayloadOk() (*string, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *PayloadCommitVerification) SetPayload(v string)`

SetPayload sets Payload field to given value.

### HasPayload

`func (o *PayloadCommitVerification) HasPayload() bool`

HasPayload returns a boolean if a field has been set.

### GetReason

`func (o *PayloadCommitVerification) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *PayloadCommitVerification) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *PayloadCommitVerification) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *PayloadCommitVerification) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetSignature

`func (o *PayloadCommitVerification) GetSignature() string`

GetSignature returns the Signature field if non-nil, zero value otherwise.

### GetSignatureOk

`func (o *PayloadCommitVerification) GetSignatureOk() (*string, bool)`

GetSignatureOk returns a tuple with the Signature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignature

`func (o *PayloadCommitVerification) SetSignature(v string)`

SetSignature sets Signature field to given value.

### HasSignature

`func (o *PayloadCommitVerification) HasSignature() bool`

HasSignature returns a boolean if a field has been set.

### GetSigner

`func (o *PayloadCommitVerification) GetSigner() PayloadUser`

GetSigner returns the Signer field if non-nil, zero value otherwise.

### GetSignerOk

`func (o *PayloadCommitVerification) GetSignerOk() (*PayloadUser, bool)`

GetSignerOk returns a tuple with the Signer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSigner

`func (o *PayloadCommitVerification) SetSigner(v PayloadUser)`

SetSigner sets Signer field to given value.

### HasSigner

`func (o *PayloadCommitVerification) HasSigner() bool`

HasSigner returns a boolean if a field has been set.

### GetVerified

`func (o *PayloadCommitVerification) GetVerified() bool`

GetVerified returns the Verified field if non-nil, zero value otherwise.

### GetVerifiedOk

`func (o *PayloadCommitVerification) GetVerifiedOk() (*bool, bool)`

GetVerifiedOk returns a tuple with the Verified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerified

`func (o *PayloadCommitVerification) SetVerified(v bool)`

SetVerified sets Verified field to given value.

### HasVerified

`func (o *PayloadCommitVerification) HasVerified() bool`

HasVerified returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



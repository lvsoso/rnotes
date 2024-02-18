# PayloadUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** | Full name of the commit author | [optional] 
**Username** | Pointer to **string** |  | [optional] 

## Methods

### NewPayloadUser

`func NewPayloadUser() *PayloadUser`

NewPayloadUser instantiates a new PayloadUser object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPayloadUserWithDefaults

`func NewPayloadUserWithDefaults() *PayloadUser`

NewPayloadUserWithDefaults instantiates a new PayloadUser object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmail

`func (o *PayloadUser) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *PayloadUser) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *PayloadUser) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *PayloadUser) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetName

`func (o *PayloadUser) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PayloadUser) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PayloadUser) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PayloadUser) HasName() bool`

HasName returns a boolean if a field has been set.

### GetUsername

`func (o *PayloadUser) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *PayloadUser) GetUsernameOk() (*string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsername

`func (o *PayloadUser) SetUsername(v string)`

SetUsername sets Username field to given value.

### HasUsername

`func (o *PayloadUser) HasUsername() bool`

HasUsername returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



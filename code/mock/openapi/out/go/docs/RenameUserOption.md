# RenameUserOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NewUsername** | **string** | New username for this user. This name cannot be in use yet by any other user. | 

## Methods

### NewRenameUserOption

`func NewRenameUserOption(newUsername string, ) *RenameUserOption`

NewRenameUserOption instantiates a new RenameUserOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRenameUserOptionWithDefaults

`func NewRenameUserOptionWithDefaults() *RenameUserOption`

NewRenameUserOptionWithDefaults instantiates a new RenameUserOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNewUsername

`func (o *RenameUserOption) GetNewUsername() string`

GetNewUsername returns the NewUsername field if non-nil, zero value otherwise.

### GetNewUsernameOk

`func (o *RenameUserOption) GetNewUsernameOk() (*string, bool)`

GetNewUsernameOk returns a tuple with the NewUsername field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewUsername

`func (o *RenameUserOption) SetNewUsername(v string)`

SetNewUsername sets NewUsername field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



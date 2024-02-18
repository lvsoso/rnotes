# CreateKeyOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **string** | An armored SSH key to add | 
**ReadOnly** | Pointer to **bool** | Describe if the key has only read access or read/write | [optional] 
**Title** | **string** | Title of the key to add | 

## Methods

### NewCreateKeyOption

`func NewCreateKeyOption(key string, title string, ) *CreateKeyOption`

NewCreateKeyOption instantiates a new CreateKeyOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateKeyOptionWithDefaults

`func NewCreateKeyOptionWithDefaults() *CreateKeyOption`

NewCreateKeyOptionWithDefaults instantiates a new CreateKeyOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *CreateKeyOption) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *CreateKeyOption) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *CreateKeyOption) SetKey(v string)`

SetKey sets Key field to given value.


### GetReadOnly

`func (o *CreateKeyOption) GetReadOnly() bool`

GetReadOnly returns the ReadOnly field if non-nil, zero value otherwise.

### GetReadOnlyOk

`func (o *CreateKeyOption) GetReadOnlyOk() (*bool, bool)`

GetReadOnlyOk returns a tuple with the ReadOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReadOnly

`func (o *CreateKeyOption) SetReadOnly(v bool)`

SetReadOnly sets ReadOnly field to given value.

### HasReadOnly

`func (o *CreateKeyOption) HasReadOnly() bool`

HasReadOnly returns a boolean if a field has been set.

### GetTitle

`func (o *CreateKeyOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CreateKeyOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CreateKeyOption) SetTitle(v string)`

SetTitle sets Title field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateLabelOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Color** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Exclusive** | Pointer to **bool** |  | [optional] 
**IsArchived** | Pointer to **bool** |  | [optional] 
**Name** | **string** |  | 

## Methods

### NewCreateLabelOption

`func NewCreateLabelOption(color string, name string, ) *CreateLabelOption`

NewCreateLabelOption instantiates a new CreateLabelOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateLabelOptionWithDefaults

`func NewCreateLabelOptionWithDefaults() *CreateLabelOption`

NewCreateLabelOptionWithDefaults instantiates a new CreateLabelOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColor

`func (o *CreateLabelOption) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *CreateLabelOption) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *CreateLabelOption) SetColor(v string)`

SetColor sets Color field to given value.


### GetDescription

`func (o *CreateLabelOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateLabelOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateLabelOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateLabelOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetExclusive

`func (o *CreateLabelOption) GetExclusive() bool`

GetExclusive returns the Exclusive field if non-nil, zero value otherwise.

### GetExclusiveOk

`func (o *CreateLabelOption) GetExclusiveOk() (*bool, bool)`

GetExclusiveOk returns a tuple with the Exclusive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExclusive

`func (o *CreateLabelOption) SetExclusive(v bool)`

SetExclusive sets Exclusive field to given value.

### HasExclusive

`func (o *CreateLabelOption) HasExclusive() bool`

HasExclusive returns a boolean if a field has been set.

### GetIsArchived

`func (o *CreateLabelOption) GetIsArchived() bool`

GetIsArchived returns the IsArchived field if non-nil, zero value otherwise.

### GetIsArchivedOk

`func (o *CreateLabelOption) GetIsArchivedOk() (*bool, bool)`

GetIsArchivedOk returns a tuple with the IsArchived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsArchived

`func (o *CreateLabelOption) SetIsArchived(v bool)`

SetIsArchived sets IsArchived field to given value.

### HasIsArchived

`func (o *CreateLabelOption) HasIsArchived() bool`

HasIsArchived returns a boolean if a field has been set.

### GetName

`func (o *CreateLabelOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateLabelOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateLabelOption) SetName(v string)`

SetName sets Name field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



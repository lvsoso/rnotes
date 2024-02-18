# CreateTagOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | Pointer to **string** |  | [optional] 
**TagName** | **string** |  | 
**Target** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateTagOption

`func NewCreateTagOption(tagName string, ) *CreateTagOption`

NewCreateTagOption instantiates a new CreateTagOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateTagOptionWithDefaults

`func NewCreateTagOptionWithDefaults() *CreateTagOption`

NewCreateTagOptionWithDefaults instantiates a new CreateTagOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *CreateTagOption) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *CreateTagOption) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *CreateTagOption) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *CreateTagOption) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetTagName

`func (o *CreateTagOption) GetTagName() string`

GetTagName returns the TagName field if non-nil, zero value otherwise.

### GetTagNameOk

`func (o *CreateTagOption) GetTagNameOk() (*string, bool)`

GetTagNameOk returns a tuple with the TagName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagName

`func (o *CreateTagOption) SetTagName(v string)`

SetTagName sets TagName field to given value.


### GetTarget

`func (o *CreateTagOption) GetTarget() string`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *CreateTagOption) GetTargetOk() (*string, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *CreateTagOption) SetTarget(v string)`

SetTarget sets Target field to given value.

### HasTarget

`func (o *CreateTagOption) HasTarget() bool`

HasTarget returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



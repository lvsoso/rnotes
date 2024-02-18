# CreateMilestoneOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | Pointer to **string** |  | [optional] 
**DueOn** | Pointer to **time.Time** |  | [optional] 
**State** | Pointer to **string** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateMilestoneOption

`func NewCreateMilestoneOption() *CreateMilestoneOption`

NewCreateMilestoneOption instantiates a new CreateMilestoneOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateMilestoneOptionWithDefaults

`func NewCreateMilestoneOptionWithDefaults() *CreateMilestoneOption`

NewCreateMilestoneOptionWithDefaults instantiates a new CreateMilestoneOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *CreateMilestoneOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateMilestoneOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateMilestoneOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateMilestoneOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetDueOn

`func (o *CreateMilestoneOption) GetDueOn() time.Time`

GetDueOn returns the DueOn field if non-nil, zero value otherwise.

### GetDueOnOk

`func (o *CreateMilestoneOption) GetDueOnOk() (*time.Time, bool)`

GetDueOnOk returns a tuple with the DueOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueOn

`func (o *CreateMilestoneOption) SetDueOn(v time.Time)`

SetDueOn sets DueOn field to given value.

### HasDueOn

`func (o *CreateMilestoneOption) HasDueOn() bool`

HasDueOn returns a boolean if a field has been set.

### GetState

`func (o *CreateMilestoneOption) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *CreateMilestoneOption) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *CreateMilestoneOption) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *CreateMilestoneOption) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *CreateMilestoneOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CreateMilestoneOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CreateMilestoneOption) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *CreateMilestoneOption) HasTitle() bool`

HasTitle returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



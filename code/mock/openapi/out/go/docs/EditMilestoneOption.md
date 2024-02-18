# EditMilestoneOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | Pointer to **string** |  | [optional] 
**DueOn** | Pointer to **time.Time** |  | [optional] 
**State** | Pointer to **string** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 

## Methods

### NewEditMilestoneOption

`func NewEditMilestoneOption() *EditMilestoneOption`

NewEditMilestoneOption instantiates a new EditMilestoneOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditMilestoneOptionWithDefaults

`func NewEditMilestoneOptionWithDefaults() *EditMilestoneOption`

NewEditMilestoneOptionWithDefaults instantiates a new EditMilestoneOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *EditMilestoneOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *EditMilestoneOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *EditMilestoneOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *EditMilestoneOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetDueOn

`func (o *EditMilestoneOption) GetDueOn() time.Time`

GetDueOn returns the DueOn field if non-nil, zero value otherwise.

### GetDueOnOk

`func (o *EditMilestoneOption) GetDueOnOk() (*time.Time, bool)`

GetDueOnOk returns a tuple with the DueOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueOn

`func (o *EditMilestoneOption) SetDueOn(v time.Time)`

SetDueOn sets DueOn field to given value.

### HasDueOn

`func (o *EditMilestoneOption) HasDueOn() bool`

HasDueOn returns a boolean if a field has been set.

### GetState

`func (o *EditMilestoneOption) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *EditMilestoneOption) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *EditMilestoneOption) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *EditMilestoneOption) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *EditMilestoneOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *EditMilestoneOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *EditMilestoneOption) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *EditMilestoneOption) HasTitle() bool`

HasTitle returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Milestone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClosedAt** | Pointer to **time.Time** |  | [optional] 
**ClosedIssues** | Pointer to **int64** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**DueOn** | Pointer to **time.Time** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**OpenIssues** | Pointer to **int64** |  | [optional] 
**State** | Pointer to **string** | StateType issue state type | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewMilestone

`func NewMilestone() *Milestone`

NewMilestone instantiates a new Milestone object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMilestoneWithDefaults

`func NewMilestoneWithDefaults() *Milestone`

NewMilestoneWithDefaults instantiates a new Milestone object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClosedAt

`func (o *Milestone) GetClosedAt() time.Time`

GetClosedAt returns the ClosedAt field if non-nil, zero value otherwise.

### GetClosedAtOk

`func (o *Milestone) GetClosedAtOk() (*time.Time, bool)`

GetClosedAtOk returns a tuple with the ClosedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedAt

`func (o *Milestone) SetClosedAt(v time.Time)`

SetClosedAt sets ClosedAt field to given value.

### HasClosedAt

`func (o *Milestone) HasClosedAt() bool`

HasClosedAt returns a boolean if a field has been set.

### GetClosedIssues

`func (o *Milestone) GetClosedIssues() int64`

GetClosedIssues returns the ClosedIssues field if non-nil, zero value otherwise.

### GetClosedIssuesOk

`func (o *Milestone) GetClosedIssuesOk() (*int64, bool)`

GetClosedIssuesOk returns a tuple with the ClosedIssues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedIssues

`func (o *Milestone) SetClosedIssues(v int64)`

SetClosedIssues sets ClosedIssues field to given value.

### HasClosedIssues

`func (o *Milestone) HasClosedIssues() bool`

HasClosedIssues returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Milestone) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Milestone) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Milestone) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Milestone) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDescription

`func (o *Milestone) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Milestone) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Milestone) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Milestone) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetDueOn

`func (o *Milestone) GetDueOn() time.Time`

GetDueOn returns the DueOn field if non-nil, zero value otherwise.

### GetDueOnOk

`func (o *Milestone) GetDueOnOk() (*time.Time, bool)`

GetDueOnOk returns a tuple with the DueOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueOn

`func (o *Milestone) SetDueOn(v time.Time)`

SetDueOn sets DueOn field to given value.

### HasDueOn

`func (o *Milestone) HasDueOn() bool`

HasDueOn returns a boolean if a field has been set.

### GetId

`func (o *Milestone) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Milestone) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Milestone) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Milestone) HasId() bool`

HasId returns a boolean if a field has been set.

### GetOpenIssues

`func (o *Milestone) GetOpenIssues() int64`

GetOpenIssues returns the OpenIssues field if non-nil, zero value otherwise.

### GetOpenIssuesOk

`func (o *Milestone) GetOpenIssuesOk() (*int64, bool)`

GetOpenIssuesOk returns a tuple with the OpenIssues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenIssues

`func (o *Milestone) SetOpenIssues(v int64)`

SetOpenIssues sets OpenIssues field to given value.

### HasOpenIssues

`func (o *Milestone) HasOpenIssues() bool`

HasOpenIssues returns a boolean if a field has been set.

### GetState

`func (o *Milestone) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Milestone) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Milestone) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *Milestone) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *Milestone) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *Milestone) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *Milestone) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *Milestone) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Milestone) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Milestone) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Milestone) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Milestone) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



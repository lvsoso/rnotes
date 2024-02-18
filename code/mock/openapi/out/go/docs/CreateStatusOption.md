# CreateStatusOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Context** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**State** | Pointer to **string** | CommitStatusState holds the state of a CommitStatus It can be \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot; and \&quot;failure\&quot; | [optional] 
**TargetUrl** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateStatusOption

`func NewCreateStatusOption() *CreateStatusOption`

NewCreateStatusOption instantiates a new CreateStatusOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateStatusOptionWithDefaults

`func NewCreateStatusOptionWithDefaults() *CreateStatusOption`

NewCreateStatusOptionWithDefaults instantiates a new CreateStatusOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContext

`func (o *CreateStatusOption) GetContext() string`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *CreateStatusOption) GetContextOk() (*string, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *CreateStatusOption) SetContext(v string)`

SetContext sets Context field to given value.

### HasContext

`func (o *CreateStatusOption) HasContext() bool`

HasContext returns a boolean if a field has been set.

### GetDescription

`func (o *CreateStatusOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateStatusOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateStatusOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateStatusOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetState

`func (o *CreateStatusOption) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *CreateStatusOption) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *CreateStatusOption) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *CreateStatusOption) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTargetUrl

`func (o *CreateStatusOption) GetTargetUrl() string`

GetTargetUrl returns the TargetUrl field if non-nil, zero value otherwise.

### GetTargetUrlOk

`func (o *CreateStatusOption) GetTargetUrlOk() (*string, bool)`

GetTargetUrlOk returns a tuple with the TargetUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetUrl

`func (o *CreateStatusOption) SetTargetUrl(v string)`

SetTargetUrl sets TargetUrl field to given value.

### HasTargetUrl

`func (o *CreateStatusOption) HasTargetUrl() bool`

HasTargetUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



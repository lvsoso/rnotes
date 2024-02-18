# EditHookOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Active** | Pointer to **bool** |  | [optional] 
**AuthorizationHeader** | Pointer to **string** |  | [optional] 
**BranchFilter** | Pointer to **string** |  | [optional] 
**Config** | Pointer to **map[string]string** |  | [optional] 
**Events** | Pointer to **[]string** |  | [optional] 

## Methods

### NewEditHookOption

`func NewEditHookOption() *EditHookOption`

NewEditHookOption instantiates a new EditHookOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditHookOptionWithDefaults

`func NewEditHookOptionWithDefaults() *EditHookOption`

NewEditHookOptionWithDefaults instantiates a new EditHookOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActive

`func (o *EditHookOption) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *EditHookOption) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *EditHookOption) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *EditHookOption) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetAuthorizationHeader

`func (o *EditHookOption) GetAuthorizationHeader() string`

GetAuthorizationHeader returns the AuthorizationHeader field if non-nil, zero value otherwise.

### GetAuthorizationHeaderOk

`func (o *EditHookOption) GetAuthorizationHeaderOk() (*string, bool)`

GetAuthorizationHeaderOk returns a tuple with the AuthorizationHeader field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationHeader

`func (o *EditHookOption) SetAuthorizationHeader(v string)`

SetAuthorizationHeader sets AuthorizationHeader field to given value.

### HasAuthorizationHeader

`func (o *EditHookOption) HasAuthorizationHeader() bool`

HasAuthorizationHeader returns a boolean if a field has been set.

### GetBranchFilter

`func (o *EditHookOption) GetBranchFilter() string`

GetBranchFilter returns the BranchFilter field if non-nil, zero value otherwise.

### GetBranchFilterOk

`func (o *EditHookOption) GetBranchFilterOk() (*string, bool)`

GetBranchFilterOk returns a tuple with the BranchFilter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchFilter

`func (o *EditHookOption) SetBranchFilter(v string)`

SetBranchFilter sets BranchFilter field to given value.

### HasBranchFilter

`func (o *EditHookOption) HasBranchFilter() bool`

HasBranchFilter returns a boolean if a field has been set.

### GetConfig

`func (o *EditHookOption) GetConfig() map[string]string`

GetConfig returns the Config field if non-nil, zero value otherwise.

### GetConfigOk

`func (o *EditHookOption) GetConfigOk() (*map[string]string, bool)`

GetConfigOk returns a tuple with the Config field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfig

`func (o *EditHookOption) SetConfig(v map[string]string)`

SetConfig sets Config field to given value.

### HasConfig

`func (o *EditHookOption) HasConfig() bool`

HasConfig returns a boolean if a field has been set.

### GetEvents

`func (o *EditHookOption) GetEvents() []string`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *EditHookOption) GetEventsOk() (*[]string, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *EditHookOption) SetEvents(v []string)`

SetEvents sets Events field to given value.

### HasEvents

`func (o *EditHookOption) HasEvents() bool`

HasEvents returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



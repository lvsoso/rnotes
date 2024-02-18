# CreateHookOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Active** | Pointer to **bool** |  | [optional] [default to false]
**AuthorizationHeader** | Pointer to **string** |  | [optional] 
**BranchFilter** | Pointer to **string** |  | [optional] 
**Config** | **map[string]string** | CreateHookOptionConfig has all config options in it required are \&quot;content_type\&quot; and \&quot;url\&quot; Required | 
**Events** | Pointer to **[]string** |  | [optional] 
**Type** | **string** |  | 

## Methods

### NewCreateHookOption

`func NewCreateHookOption(config map[string]string, type_ string, ) *CreateHookOption`

NewCreateHookOption instantiates a new CreateHookOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateHookOptionWithDefaults

`func NewCreateHookOptionWithDefaults() *CreateHookOption`

NewCreateHookOptionWithDefaults instantiates a new CreateHookOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActive

`func (o *CreateHookOption) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *CreateHookOption) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *CreateHookOption) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *CreateHookOption) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetAuthorizationHeader

`func (o *CreateHookOption) GetAuthorizationHeader() string`

GetAuthorizationHeader returns the AuthorizationHeader field if non-nil, zero value otherwise.

### GetAuthorizationHeaderOk

`func (o *CreateHookOption) GetAuthorizationHeaderOk() (*string, bool)`

GetAuthorizationHeaderOk returns a tuple with the AuthorizationHeader field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationHeader

`func (o *CreateHookOption) SetAuthorizationHeader(v string)`

SetAuthorizationHeader sets AuthorizationHeader field to given value.

### HasAuthorizationHeader

`func (o *CreateHookOption) HasAuthorizationHeader() bool`

HasAuthorizationHeader returns a boolean if a field has been set.

### GetBranchFilter

`func (o *CreateHookOption) GetBranchFilter() string`

GetBranchFilter returns the BranchFilter field if non-nil, zero value otherwise.

### GetBranchFilterOk

`func (o *CreateHookOption) GetBranchFilterOk() (*string, bool)`

GetBranchFilterOk returns a tuple with the BranchFilter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchFilter

`func (o *CreateHookOption) SetBranchFilter(v string)`

SetBranchFilter sets BranchFilter field to given value.

### HasBranchFilter

`func (o *CreateHookOption) HasBranchFilter() bool`

HasBranchFilter returns a boolean if a field has been set.

### GetConfig

`func (o *CreateHookOption) GetConfig() map[string]string`

GetConfig returns the Config field if non-nil, zero value otherwise.

### GetConfigOk

`func (o *CreateHookOption) GetConfigOk() (*map[string]string, bool)`

GetConfigOk returns a tuple with the Config field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfig

`func (o *CreateHookOption) SetConfig(v map[string]string)`

SetConfig sets Config field to given value.


### GetEvents

`func (o *CreateHookOption) GetEvents() []string`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *CreateHookOption) GetEventsOk() (*[]string, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *CreateHookOption) SetEvents(v []string)`

SetEvents sets Events field to given value.

### HasEvents

`func (o *CreateHookOption) HasEvents() bool`

HasEvents returns a boolean if a field has been set.

### GetType

`func (o *CreateHookOption) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CreateHookOption) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CreateHookOption) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



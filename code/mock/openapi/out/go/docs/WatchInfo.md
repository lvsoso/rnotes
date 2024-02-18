# WatchInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**Ignored** | Pointer to **bool** |  | [optional] 
**Reason** | Pointer to **map[string]interface{}** |  | [optional] 
**RepositoryUrl** | Pointer to **string** |  | [optional] 
**Subscribed** | Pointer to **bool** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewWatchInfo

`func NewWatchInfo() *WatchInfo`

NewWatchInfo instantiates a new WatchInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWatchInfoWithDefaults

`func NewWatchInfoWithDefaults() *WatchInfo`

NewWatchInfoWithDefaults instantiates a new WatchInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *WatchInfo) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WatchInfo) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WatchInfo) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *WatchInfo) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetIgnored

`func (o *WatchInfo) GetIgnored() bool`

GetIgnored returns the Ignored field if non-nil, zero value otherwise.

### GetIgnoredOk

`func (o *WatchInfo) GetIgnoredOk() (*bool, bool)`

GetIgnoredOk returns a tuple with the Ignored field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIgnored

`func (o *WatchInfo) SetIgnored(v bool)`

SetIgnored sets Ignored field to given value.

### HasIgnored

`func (o *WatchInfo) HasIgnored() bool`

HasIgnored returns a boolean if a field has been set.

### GetReason

`func (o *WatchInfo) GetReason() map[string]interface{}`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *WatchInfo) GetReasonOk() (*map[string]interface{}, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *WatchInfo) SetReason(v map[string]interface{})`

SetReason sets Reason field to given value.

### HasReason

`func (o *WatchInfo) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetRepositoryUrl

`func (o *WatchInfo) GetRepositoryUrl() string`

GetRepositoryUrl returns the RepositoryUrl field if non-nil, zero value otherwise.

### GetRepositoryUrlOk

`func (o *WatchInfo) GetRepositoryUrlOk() (*string, bool)`

GetRepositoryUrlOk returns a tuple with the RepositoryUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepositoryUrl

`func (o *WatchInfo) SetRepositoryUrl(v string)`

SetRepositoryUrl sets RepositoryUrl field to given value.

### HasRepositoryUrl

`func (o *WatchInfo) HasRepositoryUrl() bool`

HasRepositoryUrl returns a boolean if a field has been set.

### GetSubscribed

`func (o *WatchInfo) GetSubscribed() bool`

GetSubscribed returns the Subscribed field if non-nil, zero value otherwise.

### GetSubscribedOk

`func (o *WatchInfo) GetSubscribedOk() (*bool, bool)`

GetSubscribedOk returns a tuple with the Subscribed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubscribed

`func (o *WatchInfo) SetSubscribed(v bool)`

SetSubscribed sets Subscribed field to given value.

### HasSubscribed

`func (o *WatchInfo) HasSubscribed() bool`

HasSubscribed returns a boolean if a field has been set.

### GetUrl

`func (o *WatchInfo) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *WatchInfo) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *WatchInfo) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *WatchInfo) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



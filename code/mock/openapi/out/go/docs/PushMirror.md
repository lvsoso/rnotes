# PushMirror

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | Pointer to **time.Time** |  | [optional] 
**Interval** | Pointer to **string** |  | [optional] 
**LastError** | Pointer to **string** |  | [optional] 
**LastUpdate** | Pointer to **time.Time** |  | [optional] 
**RemoteAddress** | Pointer to **string** |  | [optional] 
**RemoteName** | Pointer to **string** |  | [optional] 
**RepoName** | Pointer to **string** |  | [optional] 
**SyncOnCommit** | Pointer to **bool** |  | [optional] 

## Methods

### NewPushMirror

`func NewPushMirror() *PushMirror`

NewPushMirror instantiates a new PushMirror object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPushMirrorWithDefaults

`func NewPushMirrorWithDefaults() *PushMirror`

NewPushMirrorWithDefaults instantiates a new PushMirror object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *PushMirror) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *PushMirror) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *PushMirror) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *PushMirror) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetInterval

`func (o *PushMirror) GetInterval() string`

GetInterval returns the Interval field if non-nil, zero value otherwise.

### GetIntervalOk

`func (o *PushMirror) GetIntervalOk() (*string, bool)`

GetIntervalOk returns a tuple with the Interval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInterval

`func (o *PushMirror) SetInterval(v string)`

SetInterval sets Interval field to given value.

### HasInterval

`func (o *PushMirror) HasInterval() bool`

HasInterval returns a boolean if a field has been set.

### GetLastError

`func (o *PushMirror) GetLastError() string`

GetLastError returns the LastError field if non-nil, zero value otherwise.

### GetLastErrorOk

`func (o *PushMirror) GetLastErrorOk() (*string, bool)`

GetLastErrorOk returns a tuple with the LastError field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastError

`func (o *PushMirror) SetLastError(v string)`

SetLastError sets LastError field to given value.

### HasLastError

`func (o *PushMirror) HasLastError() bool`

HasLastError returns a boolean if a field has been set.

### GetLastUpdate

`func (o *PushMirror) GetLastUpdate() time.Time`

GetLastUpdate returns the LastUpdate field if non-nil, zero value otherwise.

### GetLastUpdateOk

`func (o *PushMirror) GetLastUpdateOk() (*time.Time, bool)`

GetLastUpdateOk returns a tuple with the LastUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdate

`func (o *PushMirror) SetLastUpdate(v time.Time)`

SetLastUpdate sets LastUpdate field to given value.

### HasLastUpdate

`func (o *PushMirror) HasLastUpdate() bool`

HasLastUpdate returns a boolean if a field has been set.

### GetRemoteAddress

`func (o *PushMirror) GetRemoteAddress() string`

GetRemoteAddress returns the RemoteAddress field if non-nil, zero value otherwise.

### GetRemoteAddressOk

`func (o *PushMirror) GetRemoteAddressOk() (*string, bool)`

GetRemoteAddressOk returns a tuple with the RemoteAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteAddress

`func (o *PushMirror) SetRemoteAddress(v string)`

SetRemoteAddress sets RemoteAddress field to given value.

### HasRemoteAddress

`func (o *PushMirror) HasRemoteAddress() bool`

HasRemoteAddress returns a boolean if a field has been set.

### GetRemoteName

`func (o *PushMirror) GetRemoteName() string`

GetRemoteName returns the RemoteName field if non-nil, zero value otherwise.

### GetRemoteNameOk

`func (o *PushMirror) GetRemoteNameOk() (*string, bool)`

GetRemoteNameOk returns a tuple with the RemoteName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteName

`func (o *PushMirror) SetRemoteName(v string)`

SetRemoteName sets RemoteName field to given value.

### HasRemoteName

`func (o *PushMirror) HasRemoteName() bool`

HasRemoteName returns a boolean if a field has been set.

### GetRepoName

`func (o *PushMirror) GetRepoName() string`

GetRepoName returns the RepoName field if non-nil, zero value otherwise.

### GetRepoNameOk

`func (o *PushMirror) GetRepoNameOk() (*string, bool)`

GetRepoNameOk returns a tuple with the RepoName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoName

`func (o *PushMirror) SetRepoName(v string)`

SetRepoName sets RepoName field to given value.

### HasRepoName

`func (o *PushMirror) HasRepoName() bool`

HasRepoName returns a boolean if a field has been set.

### GetSyncOnCommit

`func (o *PushMirror) GetSyncOnCommit() bool`

GetSyncOnCommit returns the SyncOnCommit field if non-nil, zero value otherwise.

### GetSyncOnCommitOk

`func (o *PushMirror) GetSyncOnCommitOk() (*bool, bool)`

GetSyncOnCommitOk returns a tuple with the SyncOnCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSyncOnCommit

`func (o *PushMirror) SetSyncOnCommit(v bool)`

SetSyncOnCommit sets SyncOnCommit field to given value.

### HasSyncOnCommit

`func (o *PushMirror) HasSyncOnCommit() bool`

HasSyncOnCommit returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TrackedTime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | Pointer to **time.Time** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**Issue** | Pointer to [**Issue**](Issue.md) |  | [optional] 
**IssueId** | Pointer to **int64** | deprecated (only for backwards compatibility) | [optional] 
**Time** | Pointer to **int64** | Time in seconds | [optional] 
**UserId** | Pointer to **int64** | deprecated (only for backwards compatibility) | [optional] 
**UserName** | Pointer to **string** |  | [optional] 

## Methods

### NewTrackedTime

`func NewTrackedTime() *TrackedTime`

NewTrackedTime instantiates a new TrackedTime object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedTimeWithDefaults

`func NewTrackedTimeWithDefaults() *TrackedTime`

NewTrackedTimeWithDefaults instantiates a new TrackedTime object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *TrackedTime) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *TrackedTime) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *TrackedTime) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *TrackedTime) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetId

`func (o *TrackedTime) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TrackedTime) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TrackedTime) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *TrackedTime) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIssue

`func (o *TrackedTime) GetIssue() Issue`

GetIssue returns the Issue field if non-nil, zero value otherwise.

### GetIssueOk

`func (o *TrackedTime) GetIssueOk() (*Issue, bool)`

GetIssueOk returns a tuple with the Issue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssue

`func (o *TrackedTime) SetIssue(v Issue)`

SetIssue sets Issue field to given value.

### HasIssue

`func (o *TrackedTime) HasIssue() bool`

HasIssue returns a boolean if a field has been set.

### GetIssueId

`func (o *TrackedTime) GetIssueId() int64`

GetIssueId returns the IssueId field if non-nil, zero value otherwise.

### GetIssueIdOk

`func (o *TrackedTime) GetIssueIdOk() (*int64, bool)`

GetIssueIdOk returns a tuple with the IssueId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueId

`func (o *TrackedTime) SetIssueId(v int64)`

SetIssueId sets IssueId field to given value.

### HasIssueId

`func (o *TrackedTime) HasIssueId() bool`

HasIssueId returns a boolean if a field has been set.

### GetTime

`func (o *TrackedTime) GetTime() int64`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *TrackedTime) GetTimeOk() (*int64, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTime

`func (o *TrackedTime) SetTime(v int64)`

SetTime sets Time field to given value.

### HasTime

`func (o *TrackedTime) HasTime() bool`

HasTime returns a boolean if a field has been set.

### GetUserId

`func (o *TrackedTime) GetUserId() int64`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *TrackedTime) GetUserIdOk() (*int64, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *TrackedTime) SetUserId(v int64)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *TrackedTime) HasUserId() bool`

HasUserId returns a boolean if a field has been set.

### GetUserName

`func (o *TrackedTime) GetUserName() string`

GetUserName returns the UserName field if non-nil, zero value otherwise.

### GetUserNameOk

`func (o *TrackedTime) GetUserNameOk() (*string, bool)`

GetUserNameOk returns a tuple with the UserName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserName

`func (o *TrackedTime) SetUserName(v string)`

SetUserName sets UserName field to given value.

### HasUserName

`func (o *TrackedTime) HasUserName() bool`

HasUserName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



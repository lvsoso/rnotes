# AddTimeOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | Pointer to **time.Time** |  | [optional] 
**Time** | **int64** | time in seconds | 
**UserName** | Pointer to **string** | User who spent the time (optional) | [optional] 

## Methods

### NewAddTimeOption

`func NewAddTimeOption(time int64, ) *AddTimeOption`

NewAddTimeOption instantiates a new AddTimeOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddTimeOptionWithDefaults

`func NewAddTimeOptionWithDefaults() *AddTimeOption`

NewAddTimeOptionWithDefaults instantiates a new AddTimeOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *AddTimeOption) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *AddTimeOption) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *AddTimeOption) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *AddTimeOption) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetTime

`func (o *AddTimeOption) GetTime() int64`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *AddTimeOption) GetTimeOk() (*int64, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTime

`func (o *AddTimeOption) SetTime(v int64)`

SetTime sets Time field to given value.


### GetUserName

`func (o *AddTimeOption) GetUserName() string`

GetUserName returns the UserName field if non-nil, zero value otherwise.

### GetUserNameOk

`func (o *AddTimeOption) GetUserNameOk() (*string, bool)`

GetUserNameOk returns a tuple with the UserName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserName

`func (o *AddTimeOption) SetUserName(v string)`

SetUserName sets UserName field to given value.

### HasUserName

`func (o *AddTimeOption) HasUserName() bool`

HasUserName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



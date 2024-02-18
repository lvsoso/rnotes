# Cron

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExecTimes** | Pointer to **int64** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Next** | Pointer to **time.Time** |  | [optional] 
**Prev** | Pointer to **time.Time** |  | [optional] 
**Schedule** | Pointer to **string** |  | [optional] 

## Methods

### NewCron

`func NewCron() *Cron`

NewCron instantiates a new Cron object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCronWithDefaults

`func NewCronWithDefaults() *Cron`

NewCronWithDefaults instantiates a new Cron object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExecTimes

`func (o *Cron) GetExecTimes() int64`

GetExecTimes returns the ExecTimes field if non-nil, zero value otherwise.

### GetExecTimesOk

`func (o *Cron) GetExecTimesOk() (*int64, bool)`

GetExecTimesOk returns a tuple with the ExecTimes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecTimes

`func (o *Cron) SetExecTimes(v int64)`

SetExecTimes sets ExecTimes field to given value.

### HasExecTimes

`func (o *Cron) HasExecTimes() bool`

HasExecTimes returns a boolean if a field has been set.

### GetName

`func (o *Cron) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Cron) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Cron) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Cron) HasName() bool`

HasName returns a boolean if a field has been set.

### GetNext

`func (o *Cron) GetNext() time.Time`

GetNext returns the Next field if non-nil, zero value otherwise.

### GetNextOk

`func (o *Cron) GetNextOk() (*time.Time, bool)`

GetNextOk returns a tuple with the Next field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNext

`func (o *Cron) SetNext(v time.Time)`

SetNext sets Next field to given value.

### HasNext

`func (o *Cron) HasNext() bool`

HasNext returns a boolean if a field has been set.

### GetPrev

`func (o *Cron) GetPrev() time.Time`

GetPrev returns the Prev field if non-nil, zero value otherwise.

### GetPrevOk

`func (o *Cron) GetPrevOk() (*time.Time, bool)`

GetPrevOk returns a tuple with the Prev field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrev

`func (o *Cron) SetPrev(v time.Time)`

SetPrev sets Prev field to given value.

### HasPrev

`func (o *Cron) HasPrev() bool`

HasPrev returns a boolean if a field has been set.

### GetSchedule

`func (o *Cron) GetSchedule() string`

GetSchedule returns the Schedule field if non-nil, zero value otherwise.

### GetScheduleOk

`func (o *Cron) GetScheduleOk() (*string, bool)`

GetScheduleOk returns a tuple with the Schedule field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSchedule

`func (o *Cron) SetSchedule(v string)`

SetSchedule sets Schedule field to given value.

### HasSchedule

`func (o *Cron) HasSchedule() bool`

HasSchedule returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



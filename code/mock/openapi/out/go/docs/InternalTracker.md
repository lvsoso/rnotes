# InternalTracker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AllowOnlyContributorsToTrackTime** | Pointer to **bool** | Let only contributors track time (Built-in issue tracker) | [optional] 
**EnableIssueDependencies** | Pointer to **bool** | Enable dependencies for issues and pull requests (Built-in issue tracker) | [optional] 
**EnableTimeTracker** | Pointer to **bool** | Enable time tracking (Built-in issue tracker) | [optional] 

## Methods

### NewInternalTracker

`func NewInternalTracker() *InternalTracker`

NewInternalTracker instantiates a new InternalTracker object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInternalTrackerWithDefaults

`func NewInternalTrackerWithDefaults() *InternalTracker`

NewInternalTrackerWithDefaults instantiates a new InternalTracker object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAllowOnlyContributorsToTrackTime

`func (o *InternalTracker) GetAllowOnlyContributorsToTrackTime() bool`

GetAllowOnlyContributorsToTrackTime returns the AllowOnlyContributorsToTrackTime field if non-nil, zero value otherwise.

### GetAllowOnlyContributorsToTrackTimeOk

`func (o *InternalTracker) GetAllowOnlyContributorsToTrackTimeOk() (*bool, bool)`

GetAllowOnlyContributorsToTrackTimeOk returns a tuple with the AllowOnlyContributorsToTrackTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowOnlyContributorsToTrackTime

`func (o *InternalTracker) SetAllowOnlyContributorsToTrackTime(v bool)`

SetAllowOnlyContributorsToTrackTime sets AllowOnlyContributorsToTrackTime field to given value.

### HasAllowOnlyContributorsToTrackTime

`func (o *InternalTracker) HasAllowOnlyContributorsToTrackTime() bool`

HasAllowOnlyContributorsToTrackTime returns a boolean if a field has been set.

### GetEnableIssueDependencies

`func (o *InternalTracker) GetEnableIssueDependencies() bool`

GetEnableIssueDependencies returns the EnableIssueDependencies field if non-nil, zero value otherwise.

### GetEnableIssueDependenciesOk

`func (o *InternalTracker) GetEnableIssueDependenciesOk() (*bool, bool)`

GetEnableIssueDependenciesOk returns a tuple with the EnableIssueDependencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableIssueDependencies

`func (o *InternalTracker) SetEnableIssueDependencies(v bool)`

SetEnableIssueDependencies sets EnableIssueDependencies field to given value.

### HasEnableIssueDependencies

`func (o *InternalTracker) HasEnableIssueDependencies() bool`

HasEnableIssueDependencies returns a boolean if a field has been set.

### GetEnableTimeTracker

`func (o *InternalTracker) GetEnableTimeTracker() bool`

GetEnableTimeTracker returns the EnableTimeTracker field if non-nil, zero value otherwise.

### GetEnableTimeTrackerOk

`func (o *InternalTracker) GetEnableTimeTrackerOk() (*bool, bool)`

GetEnableTimeTrackerOk returns a tuple with the EnableTimeTracker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableTimeTracker

`func (o *InternalTracker) SetEnableTimeTracker(v bool)`

SetEnableTimeTracker sets EnableTimeTracker field to given value.

### HasEnableTimeTracker

`func (o *InternalTracker) HasEnableTimeTracker() bool`

HasEnableTimeTracker returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



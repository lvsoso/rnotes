# StopWatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | Pointer to **time.Time** |  | [optional] 
**Duration** | Pointer to **string** |  | [optional] 
**IssueIndex** | Pointer to **int64** |  | [optional] 
**IssueTitle** | Pointer to **string** |  | [optional] 
**RepoName** | Pointer to **string** |  | [optional] 
**RepoOwnerName** | Pointer to **string** |  | [optional] 
**Seconds** | Pointer to **int64** |  | [optional] 

## Methods

### NewStopWatch

`func NewStopWatch() *StopWatch`

NewStopWatch instantiates a new StopWatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStopWatchWithDefaults

`func NewStopWatchWithDefaults() *StopWatch`

NewStopWatchWithDefaults instantiates a new StopWatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *StopWatch) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *StopWatch) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *StopWatch) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *StopWatch) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetDuration

`func (o *StopWatch) GetDuration() string`

GetDuration returns the Duration field if non-nil, zero value otherwise.

### GetDurationOk

`func (o *StopWatch) GetDurationOk() (*string, bool)`

GetDurationOk returns a tuple with the Duration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuration

`func (o *StopWatch) SetDuration(v string)`

SetDuration sets Duration field to given value.

### HasDuration

`func (o *StopWatch) HasDuration() bool`

HasDuration returns a boolean if a field has been set.

### GetIssueIndex

`func (o *StopWatch) GetIssueIndex() int64`

GetIssueIndex returns the IssueIndex field if non-nil, zero value otherwise.

### GetIssueIndexOk

`func (o *StopWatch) GetIssueIndexOk() (*int64, bool)`

GetIssueIndexOk returns a tuple with the IssueIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueIndex

`func (o *StopWatch) SetIssueIndex(v int64)`

SetIssueIndex sets IssueIndex field to given value.

### HasIssueIndex

`func (o *StopWatch) HasIssueIndex() bool`

HasIssueIndex returns a boolean if a field has been set.

### GetIssueTitle

`func (o *StopWatch) GetIssueTitle() string`

GetIssueTitle returns the IssueTitle field if non-nil, zero value otherwise.

### GetIssueTitleOk

`func (o *StopWatch) GetIssueTitleOk() (*string, bool)`

GetIssueTitleOk returns a tuple with the IssueTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueTitle

`func (o *StopWatch) SetIssueTitle(v string)`

SetIssueTitle sets IssueTitle field to given value.

### HasIssueTitle

`func (o *StopWatch) HasIssueTitle() bool`

HasIssueTitle returns a boolean if a field has been set.

### GetRepoName

`func (o *StopWatch) GetRepoName() string`

GetRepoName returns the RepoName field if non-nil, zero value otherwise.

### GetRepoNameOk

`func (o *StopWatch) GetRepoNameOk() (*string, bool)`

GetRepoNameOk returns a tuple with the RepoName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoName

`func (o *StopWatch) SetRepoName(v string)`

SetRepoName sets RepoName field to given value.

### HasRepoName

`func (o *StopWatch) HasRepoName() bool`

HasRepoName returns a boolean if a field has been set.

### GetRepoOwnerName

`func (o *StopWatch) GetRepoOwnerName() string`

GetRepoOwnerName returns the RepoOwnerName field if non-nil, zero value otherwise.

### GetRepoOwnerNameOk

`func (o *StopWatch) GetRepoOwnerNameOk() (*string, bool)`

GetRepoOwnerNameOk returns a tuple with the RepoOwnerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoOwnerName

`func (o *StopWatch) SetRepoOwnerName(v string)`

SetRepoOwnerName sets RepoOwnerName field to given value.

### HasRepoOwnerName

`func (o *StopWatch) HasRepoOwnerName() bool`

HasRepoOwnerName returns a boolean if a field has been set.

### GetSeconds

`func (o *StopWatch) GetSeconds() int64`

GetSeconds returns the Seconds field if non-nil, zero value otherwise.

### GetSecondsOk

`func (o *StopWatch) GetSecondsOk() (*int64, bool)`

GetSecondsOk returns a tuple with the Seconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeconds

`func (o *StopWatch) SetSeconds(v int64)`

SetSeconds sets Seconds field to given value.

### HasSeconds

`func (o *StopWatch) HasSeconds() bool`

HasSeconds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



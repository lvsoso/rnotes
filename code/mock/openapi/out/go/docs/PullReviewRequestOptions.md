# PullReviewRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reviewers** | Pointer to **[]string** |  | [optional] 
**TeamReviewers** | Pointer to **[]string** |  | [optional] 

## Methods

### NewPullReviewRequestOptions

`func NewPullReviewRequestOptions() *PullReviewRequestOptions`

NewPullReviewRequestOptions instantiates a new PullReviewRequestOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPullReviewRequestOptionsWithDefaults

`func NewPullReviewRequestOptionsWithDefaults() *PullReviewRequestOptions`

NewPullReviewRequestOptionsWithDefaults instantiates a new PullReviewRequestOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReviewers

`func (o *PullReviewRequestOptions) GetReviewers() []string`

GetReviewers returns the Reviewers field if non-nil, zero value otherwise.

### GetReviewersOk

`func (o *PullReviewRequestOptions) GetReviewersOk() (*[]string, bool)`

GetReviewersOk returns a tuple with the Reviewers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewers

`func (o *PullReviewRequestOptions) SetReviewers(v []string)`

SetReviewers sets Reviewers field to given value.

### HasReviewers

`func (o *PullReviewRequestOptions) HasReviewers() bool`

HasReviewers returns a boolean if a field has been set.

### GetTeamReviewers

`func (o *PullReviewRequestOptions) GetTeamReviewers() []string`

GetTeamReviewers returns the TeamReviewers field if non-nil, zero value otherwise.

### GetTeamReviewersOk

`func (o *PullReviewRequestOptions) GetTeamReviewersOk() (*[]string, bool)`

GetTeamReviewersOk returns a tuple with the TeamReviewers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamReviewers

`func (o *PullReviewRequestOptions) SetTeamReviewers(v []string)`

SetTeamReviewers sets TeamReviewers field to given value.

### HasTeamReviewers

`func (o *PullReviewRequestOptions) HasTeamReviewers() bool`

HasTeamReviewers returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



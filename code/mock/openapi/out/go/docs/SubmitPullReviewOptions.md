# SubmitPullReviewOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** |  | [optional] 
**Event** | Pointer to **string** | ReviewStateType review state type | [optional] 

## Methods

### NewSubmitPullReviewOptions

`func NewSubmitPullReviewOptions() *SubmitPullReviewOptions`

NewSubmitPullReviewOptions instantiates a new SubmitPullReviewOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubmitPullReviewOptionsWithDefaults

`func NewSubmitPullReviewOptionsWithDefaults() *SubmitPullReviewOptions`

NewSubmitPullReviewOptionsWithDefaults instantiates a new SubmitPullReviewOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBody

`func (o *SubmitPullReviewOptions) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *SubmitPullReviewOptions) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *SubmitPullReviewOptions) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *SubmitPullReviewOptions) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetEvent

`func (o *SubmitPullReviewOptions) GetEvent() string`

GetEvent returns the Event field if non-nil, zero value otherwise.

### GetEventOk

`func (o *SubmitPullReviewOptions) GetEventOk() (*string, bool)`

GetEventOk returns a tuple with the Event field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvent

`func (o *SubmitPullReviewOptions) SetEvent(v string)`

SetEvent sets Event field to given value.

### HasEvent

`func (o *SubmitPullReviewOptions) HasEvent() bool`

HasEvent returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



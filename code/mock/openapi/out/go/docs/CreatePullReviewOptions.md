# CreatePullReviewOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to [**[]CreatePullReviewComment**](CreatePullReviewComment.md) |  | [optional] 
**CommitId** | Pointer to **string** |  | [optional] 
**Event** | Pointer to **string** | ReviewStateType review state type | [optional] 

## Methods

### NewCreatePullReviewOptions

`func NewCreatePullReviewOptions() *CreatePullReviewOptions`

NewCreatePullReviewOptions instantiates a new CreatePullReviewOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreatePullReviewOptionsWithDefaults

`func NewCreatePullReviewOptionsWithDefaults() *CreatePullReviewOptions`

NewCreatePullReviewOptionsWithDefaults instantiates a new CreatePullReviewOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBody

`func (o *CreatePullReviewOptions) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *CreatePullReviewOptions) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *CreatePullReviewOptions) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *CreatePullReviewOptions) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetComments

`func (o *CreatePullReviewOptions) GetComments() []CreatePullReviewComment`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *CreatePullReviewOptions) GetCommentsOk() (*[]CreatePullReviewComment, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *CreatePullReviewOptions) SetComments(v []CreatePullReviewComment)`

SetComments sets Comments field to given value.

### HasComments

`func (o *CreatePullReviewOptions) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCommitId

`func (o *CreatePullReviewOptions) GetCommitId() string`

GetCommitId returns the CommitId field if non-nil, zero value otherwise.

### GetCommitIdOk

`func (o *CreatePullReviewOptions) GetCommitIdOk() (*string, bool)`

GetCommitIdOk returns a tuple with the CommitId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitId

`func (o *CreatePullReviewOptions) SetCommitId(v string)`

SetCommitId sets CommitId field to given value.

### HasCommitId

`func (o *CreatePullReviewOptions) HasCommitId() bool`

HasCommitId returns a boolean if a field has been set.

### GetEvent

`func (o *CreatePullReviewOptions) GetEvent() string`

GetEvent returns the Event field if non-nil, zero value otherwise.

### GetEventOk

`func (o *CreatePullReviewOptions) GetEventOk() (*string, bool)`

GetEventOk returns a tuple with the Event field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvent

`func (o *CreatePullReviewOptions) SetEvent(v string)`

SetEvent sets Event field to given value.

### HasEvent

`func (o *CreatePullReviewOptions) HasEvent() bool`

HasEvent returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



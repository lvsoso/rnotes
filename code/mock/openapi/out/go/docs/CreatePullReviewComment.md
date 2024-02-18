# CreatePullReviewComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** |  | [optional] 
**NewPosition** | Pointer to **int64** | if comment to new file line or 0 | [optional] 
**OldPosition** | Pointer to **int64** | if comment to old file line or 0 | [optional] 
**Path** | Pointer to **string** | the tree path | [optional] 

## Methods

### NewCreatePullReviewComment

`func NewCreatePullReviewComment() *CreatePullReviewComment`

NewCreatePullReviewComment instantiates a new CreatePullReviewComment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreatePullReviewCommentWithDefaults

`func NewCreatePullReviewCommentWithDefaults() *CreatePullReviewComment`

NewCreatePullReviewCommentWithDefaults instantiates a new CreatePullReviewComment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBody

`func (o *CreatePullReviewComment) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *CreatePullReviewComment) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *CreatePullReviewComment) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *CreatePullReviewComment) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetNewPosition

`func (o *CreatePullReviewComment) GetNewPosition() int64`

GetNewPosition returns the NewPosition field if non-nil, zero value otherwise.

### GetNewPositionOk

`func (o *CreatePullReviewComment) GetNewPositionOk() (*int64, bool)`

GetNewPositionOk returns a tuple with the NewPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewPosition

`func (o *CreatePullReviewComment) SetNewPosition(v int64)`

SetNewPosition sets NewPosition field to given value.

### HasNewPosition

`func (o *CreatePullReviewComment) HasNewPosition() bool`

HasNewPosition returns a boolean if a field has been set.

### GetOldPosition

`func (o *CreatePullReviewComment) GetOldPosition() int64`

GetOldPosition returns the OldPosition field if non-nil, zero value otherwise.

### GetOldPositionOk

`func (o *CreatePullReviewComment) GetOldPositionOk() (*int64, bool)`

GetOldPositionOk returns a tuple with the OldPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldPosition

`func (o *CreatePullReviewComment) SetOldPosition(v int64)`

SetOldPosition sets OldPosition field to given value.

### HasOldPosition

`func (o *CreatePullReviewComment) HasOldPosition() bool`

HasOldPosition returns a boolean if a field has been set.

### GetPath

`func (o *CreatePullReviewComment) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *CreatePullReviewComment) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *CreatePullReviewComment) SetPath(v string)`

SetPath sets Path field to given value.

### HasPath

`func (o *CreatePullReviewComment) HasPath() bool`

HasPath returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



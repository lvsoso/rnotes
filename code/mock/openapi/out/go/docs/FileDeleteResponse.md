# FileDeleteResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Commit** | Pointer to [**FileCommitResponse**](FileCommitResponse.md) |  | [optional] 
**Content** | Pointer to **map[string]interface{}** |  | [optional] 
**Verification** | Pointer to [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Methods

### NewFileDeleteResponse

`func NewFileDeleteResponse() *FileDeleteResponse`

NewFileDeleteResponse instantiates a new FileDeleteResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileDeleteResponseWithDefaults

`func NewFileDeleteResponseWithDefaults() *FileDeleteResponse`

NewFileDeleteResponseWithDefaults instantiates a new FileDeleteResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommit

`func (o *FileDeleteResponse) GetCommit() FileCommitResponse`

GetCommit returns the Commit field if non-nil, zero value otherwise.

### GetCommitOk

`func (o *FileDeleteResponse) GetCommitOk() (*FileCommitResponse, bool)`

GetCommitOk returns a tuple with the Commit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommit

`func (o *FileDeleteResponse) SetCommit(v FileCommitResponse)`

SetCommit sets Commit field to given value.

### HasCommit

`func (o *FileDeleteResponse) HasCommit() bool`

HasCommit returns a boolean if a field has been set.

### GetContent

`func (o *FileDeleteResponse) GetContent() map[string]interface{}`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *FileDeleteResponse) GetContentOk() (*map[string]interface{}, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *FileDeleteResponse) SetContent(v map[string]interface{})`

SetContent sets Content field to given value.

### HasContent

`func (o *FileDeleteResponse) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetVerification

`func (o *FileDeleteResponse) GetVerification() PayloadCommitVerification`

GetVerification returns the Verification field if non-nil, zero value otherwise.

### GetVerificationOk

`func (o *FileDeleteResponse) GetVerificationOk() (*PayloadCommitVerification, bool)`

GetVerificationOk returns a tuple with the Verification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerification

`func (o *FileDeleteResponse) SetVerification(v PayloadCommitVerification)`

SetVerification sets Verification field to given value.

### HasVerification

`func (o *FileDeleteResponse) HasVerification() bool`

HasVerification returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



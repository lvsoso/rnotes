# FileResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Commit** | Pointer to [**FileCommitResponse**](FileCommitResponse.md) |  | [optional] 
**Content** | Pointer to [**ContentsResponse**](ContentsResponse.md) |  | [optional] 
**Verification** | Pointer to [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Methods

### NewFileResponse

`func NewFileResponse() *FileResponse`

NewFileResponse instantiates a new FileResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileResponseWithDefaults

`func NewFileResponseWithDefaults() *FileResponse`

NewFileResponseWithDefaults instantiates a new FileResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommit

`func (o *FileResponse) GetCommit() FileCommitResponse`

GetCommit returns the Commit field if non-nil, zero value otherwise.

### GetCommitOk

`func (o *FileResponse) GetCommitOk() (*FileCommitResponse, bool)`

GetCommitOk returns a tuple with the Commit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommit

`func (o *FileResponse) SetCommit(v FileCommitResponse)`

SetCommit sets Commit field to given value.

### HasCommit

`func (o *FileResponse) HasCommit() bool`

HasCommit returns a boolean if a field has been set.

### GetContent

`func (o *FileResponse) GetContent() ContentsResponse`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *FileResponse) GetContentOk() (*ContentsResponse, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *FileResponse) SetContent(v ContentsResponse)`

SetContent sets Content field to given value.

### HasContent

`func (o *FileResponse) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetVerification

`func (o *FileResponse) GetVerification() PayloadCommitVerification`

GetVerification returns the Verification field if non-nil, zero value otherwise.

### GetVerificationOk

`func (o *FileResponse) GetVerificationOk() (*PayloadCommitVerification, bool)`

GetVerificationOk returns a tuple with the Verification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerification

`func (o *FileResponse) SetVerification(v PayloadCommitVerification)`

SetVerification sets Verification field to given value.

### HasVerification

`func (o *FileResponse) HasVerification() bool`

HasVerification returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



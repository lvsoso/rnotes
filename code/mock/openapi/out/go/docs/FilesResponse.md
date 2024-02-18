# FilesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Commit** | Pointer to [**FileCommitResponse**](FileCommitResponse.md) |  | [optional] 
**Files** | Pointer to [**[]ContentsResponse**](ContentsResponse.md) |  | [optional] 
**Verification** | Pointer to [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Methods

### NewFilesResponse

`func NewFilesResponse() *FilesResponse`

NewFilesResponse instantiates a new FilesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFilesResponseWithDefaults

`func NewFilesResponseWithDefaults() *FilesResponse`

NewFilesResponseWithDefaults instantiates a new FilesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommit

`func (o *FilesResponse) GetCommit() FileCommitResponse`

GetCommit returns the Commit field if non-nil, zero value otherwise.

### GetCommitOk

`func (o *FilesResponse) GetCommitOk() (*FileCommitResponse, bool)`

GetCommitOk returns a tuple with the Commit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommit

`func (o *FilesResponse) SetCommit(v FileCommitResponse)`

SetCommit sets Commit field to given value.

### HasCommit

`func (o *FilesResponse) HasCommit() bool`

HasCommit returns a boolean if a field has been set.

### GetFiles

`func (o *FilesResponse) GetFiles() []ContentsResponse`

GetFiles returns the Files field if non-nil, zero value otherwise.

### GetFilesOk

`func (o *FilesResponse) GetFilesOk() (*[]ContentsResponse, bool)`

GetFilesOk returns a tuple with the Files field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiles

`func (o *FilesResponse) SetFiles(v []ContentsResponse)`

SetFiles sets Files field to given value.

### HasFiles

`func (o *FilesResponse) HasFiles() bool`

HasFiles returns a boolean if a field has been set.

### GetVerification

`func (o *FilesResponse) GetVerification() PayloadCommitVerification`

GetVerification returns the Verification field if non-nil, zero value otherwise.

### GetVerificationOk

`func (o *FilesResponse) GetVerificationOk() (*PayloadCommitVerification, bool)`

GetVerificationOk returns a tuple with the Verification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerification

`func (o *FilesResponse) SetVerification(v PayloadCommitVerification)`

SetVerification sets Verification field to given value.

### HasVerification

`func (o *FilesResponse) HasVerification() bool`

HasVerification returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



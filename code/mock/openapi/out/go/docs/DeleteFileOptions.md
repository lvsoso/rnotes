# DeleteFileOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Branch** | Pointer to **string** | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**Committer** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Dates** | Pointer to [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**Message** | Pointer to **string** | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**NewBranch** | Pointer to **string** | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**Sha** | **string** | sha is the SHA for the file that already exists | 
**Signoff** | Pointer to **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Methods

### NewDeleteFileOptions

`func NewDeleteFileOptions(sha string, ) *DeleteFileOptions`

NewDeleteFileOptions instantiates a new DeleteFileOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeleteFileOptionsWithDefaults

`func NewDeleteFileOptionsWithDefaults() *DeleteFileOptions`

NewDeleteFileOptionsWithDefaults instantiates a new DeleteFileOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *DeleteFileOptions) GetAuthor() Identity`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *DeleteFileOptions) GetAuthorOk() (*Identity, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *DeleteFileOptions) SetAuthor(v Identity)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *DeleteFileOptions) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetBranch

`func (o *DeleteFileOptions) GetBranch() string`

GetBranch returns the Branch field if non-nil, zero value otherwise.

### GetBranchOk

`func (o *DeleteFileOptions) GetBranchOk() (*string, bool)`

GetBranchOk returns a tuple with the Branch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranch

`func (o *DeleteFileOptions) SetBranch(v string)`

SetBranch sets Branch field to given value.

### HasBranch

`func (o *DeleteFileOptions) HasBranch() bool`

HasBranch returns a boolean if a field has been set.

### GetCommitter

`func (o *DeleteFileOptions) GetCommitter() Identity`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *DeleteFileOptions) GetCommitterOk() (*Identity, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *DeleteFileOptions) SetCommitter(v Identity)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *DeleteFileOptions) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetDates

`func (o *DeleteFileOptions) GetDates() CommitDateOptions`

GetDates returns the Dates field if non-nil, zero value otherwise.

### GetDatesOk

`func (o *DeleteFileOptions) GetDatesOk() (*CommitDateOptions, bool)`

GetDatesOk returns a tuple with the Dates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDates

`func (o *DeleteFileOptions) SetDates(v CommitDateOptions)`

SetDates sets Dates field to given value.

### HasDates

`func (o *DeleteFileOptions) HasDates() bool`

HasDates returns a boolean if a field has been set.

### GetMessage

`func (o *DeleteFileOptions) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *DeleteFileOptions) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *DeleteFileOptions) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *DeleteFileOptions) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetNewBranch

`func (o *DeleteFileOptions) GetNewBranch() string`

GetNewBranch returns the NewBranch field if non-nil, zero value otherwise.

### GetNewBranchOk

`func (o *DeleteFileOptions) GetNewBranchOk() (*string, bool)`

GetNewBranchOk returns a tuple with the NewBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewBranch

`func (o *DeleteFileOptions) SetNewBranch(v string)`

SetNewBranch sets NewBranch field to given value.

### HasNewBranch

`func (o *DeleteFileOptions) HasNewBranch() bool`

HasNewBranch returns a boolean if a field has been set.

### GetSha

`func (o *DeleteFileOptions) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *DeleteFileOptions) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *DeleteFileOptions) SetSha(v string)`

SetSha sets Sha field to given value.


### GetSignoff

`func (o *DeleteFileOptions) GetSignoff() bool`

GetSignoff returns the Signoff field if non-nil, zero value otherwise.

### GetSignoffOk

`func (o *DeleteFileOptions) GetSignoffOk() (*bool, bool)`

GetSignoffOk returns a tuple with the Signoff field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignoff

`func (o *DeleteFileOptions) SetSignoff(v bool)`

SetSignoff sets Signoff field to given value.

### HasSignoff

`func (o *DeleteFileOptions) HasSignoff() bool`

HasSignoff returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



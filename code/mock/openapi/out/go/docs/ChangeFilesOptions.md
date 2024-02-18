# ChangeFilesOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Branch** | Pointer to **string** | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**Committer** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Dates** | Pointer to [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**Files** | [**[]ChangeFileOperation**](ChangeFileOperation.md) | list of file operations | 
**Message** | Pointer to **string** | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**NewBranch** | Pointer to **string** | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**Signoff** | Pointer to **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Methods

### NewChangeFilesOptions

`func NewChangeFilesOptions(files []ChangeFileOperation, ) *ChangeFilesOptions`

NewChangeFilesOptions instantiates a new ChangeFilesOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChangeFilesOptionsWithDefaults

`func NewChangeFilesOptionsWithDefaults() *ChangeFilesOptions`

NewChangeFilesOptionsWithDefaults instantiates a new ChangeFilesOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *ChangeFilesOptions) GetAuthor() Identity`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *ChangeFilesOptions) GetAuthorOk() (*Identity, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *ChangeFilesOptions) SetAuthor(v Identity)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *ChangeFilesOptions) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetBranch

`func (o *ChangeFilesOptions) GetBranch() string`

GetBranch returns the Branch field if non-nil, zero value otherwise.

### GetBranchOk

`func (o *ChangeFilesOptions) GetBranchOk() (*string, bool)`

GetBranchOk returns a tuple with the Branch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranch

`func (o *ChangeFilesOptions) SetBranch(v string)`

SetBranch sets Branch field to given value.

### HasBranch

`func (o *ChangeFilesOptions) HasBranch() bool`

HasBranch returns a boolean if a field has been set.

### GetCommitter

`func (o *ChangeFilesOptions) GetCommitter() Identity`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *ChangeFilesOptions) GetCommitterOk() (*Identity, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *ChangeFilesOptions) SetCommitter(v Identity)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *ChangeFilesOptions) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetDates

`func (o *ChangeFilesOptions) GetDates() CommitDateOptions`

GetDates returns the Dates field if non-nil, zero value otherwise.

### GetDatesOk

`func (o *ChangeFilesOptions) GetDatesOk() (*CommitDateOptions, bool)`

GetDatesOk returns a tuple with the Dates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDates

`func (o *ChangeFilesOptions) SetDates(v CommitDateOptions)`

SetDates sets Dates field to given value.

### HasDates

`func (o *ChangeFilesOptions) HasDates() bool`

HasDates returns a boolean if a field has been set.

### GetFiles

`func (o *ChangeFilesOptions) GetFiles() []ChangeFileOperation`

GetFiles returns the Files field if non-nil, zero value otherwise.

### GetFilesOk

`func (o *ChangeFilesOptions) GetFilesOk() (*[]ChangeFileOperation, bool)`

GetFilesOk returns a tuple with the Files field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiles

`func (o *ChangeFilesOptions) SetFiles(v []ChangeFileOperation)`

SetFiles sets Files field to given value.


### GetMessage

`func (o *ChangeFilesOptions) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ChangeFilesOptions) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ChangeFilesOptions) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *ChangeFilesOptions) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetNewBranch

`func (o *ChangeFilesOptions) GetNewBranch() string`

GetNewBranch returns the NewBranch field if non-nil, zero value otherwise.

### GetNewBranchOk

`func (o *ChangeFilesOptions) GetNewBranchOk() (*string, bool)`

GetNewBranchOk returns a tuple with the NewBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewBranch

`func (o *ChangeFilesOptions) SetNewBranch(v string)`

SetNewBranch sets NewBranch field to given value.

### HasNewBranch

`func (o *ChangeFilesOptions) HasNewBranch() bool`

HasNewBranch returns a boolean if a field has been set.

### GetSignoff

`func (o *ChangeFilesOptions) GetSignoff() bool`

GetSignoff returns the Signoff field if non-nil, zero value otherwise.

### GetSignoffOk

`func (o *ChangeFilesOptions) GetSignoffOk() (*bool, bool)`

GetSignoffOk returns a tuple with the Signoff field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignoff

`func (o *ChangeFilesOptions) SetSignoff(v bool)`

SetSignoff sets Signoff field to given value.

### HasSignoff

`func (o *ChangeFilesOptions) HasSignoff() bool`

HasSignoff returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



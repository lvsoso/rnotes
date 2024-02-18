# CreateFileOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Branch** | Pointer to **string** | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**Committer** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Content** | **string** | content must be base64 encoded | 
**Dates** | Pointer to [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**Message** | Pointer to **string** | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**NewBranch** | Pointer to **string** | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**Signoff** | Pointer to **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Methods

### NewCreateFileOptions

`func NewCreateFileOptions(content string, ) *CreateFileOptions`

NewCreateFileOptions instantiates a new CreateFileOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateFileOptionsWithDefaults

`func NewCreateFileOptionsWithDefaults() *CreateFileOptions`

NewCreateFileOptionsWithDefaults instantiates a new CreateFileOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *CreateFileOptions) GetAuthor() Identity`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *CreateFileOptions) GetAuthorOk() (*Identity, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *CreateFileOptions) SetAuthor(v Identity)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *CreateFileOptions) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetBranch

`func (o *CreateFileOptions) GetBranch() string`

GetBranch returns the Branch field if non-nil, zero value otherwise.

### GetBranchOk

`func (o *CreateFileOptions) GetBranchOk() (*string, bool)`

GetBranchOk returns a tuple with the Branch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranch

`func (o *CreateFileOptions) SetBranch(v string)`

SetBranch sets Branch field to given value.

### HasBranch

`func (o *CreateFileOptions) HasBranch() bool`

HasBranch returns a boolean if a field has been set.

### GetCommitter

`func (o *CreateFileOptions) GetCommitter() Identity`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *CreateFileOptions) GetCommitterOk() (*Identity, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *CreateFileOptions) SetCommitter(v Identity)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *CreateFileOptions) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetContent

`func (o *CreateFileOptions) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *CreateFileOptions) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *CreateFileOptions) SetContent(v string)`

SetContent sets Content field to given value.


### GetDates

`func (o *CreateFileOptions) GetDates() CommitDateOptions`

GetDates returns the Dates field if non-nil, zero value otherwise.

### GetDatesOk

`func (o *CreateFileOptions) GetDatesOk() (*CommitDateOptions, bool)`

GetDatesOk returns a tuple with the Dates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDates

`func (o *CreateFileOptions) SetDates(v CommitDateOptions)`

SetDates sets Dates field to given value.

### HasDates

`func (o *CreateFileOptions) HasDates() bool`

HasDates returns a boolean if a field has been set.

### GetMessage

`func (o *CreateFileOptions) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *CreateFileOptions) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *CreateFileOptions) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *CreateFileOptions) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetNewBranch

`func (o *CreateFileOptions) GetNewBranch() string`

GetNewBranch returns the NewBranch field if non-nil, zero value otherwise.

### GetNewBranchOk

`func (o *CreateFileOptions) GetNewBranchOk() (*string, bool)`

GetNewBranchOk returns a tuple with the NewBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewBranch

`func (o *CreateFileOptions) SetNewBranch(v string)`

SetNewBranch sets NewBranch field to given value.

### HasNewBranch

`func (o *CreateFileOptions) HasNewBranch() bool`

HasNewBranch returns a boolean if a field has been set.

### GetSignoff

`func (o *CreateFileOptions) GetSignoff() bool`

GetSignoff returns the Signoff field if non-nil, zero value otherwise.

### GetSignoffOk

`func (o *CreateFileOptions) GetSignoffOk() (*bool, bool)`

GetSignoffOk returns a tuple with the Signoff field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignoff

`func (o *CreateFileOptions) SetSignoff(v bool)`

SetSignoff sets Signoff field to given value.

### HasSignoff

`func (o *CreateFileOptions) HasSignoff() bool`

HasSignoff returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



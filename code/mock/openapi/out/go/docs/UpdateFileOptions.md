# UpdateFileOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Branch** | Pointer to **string** | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**Committer** | Pointer to [**Identity**](Identity.md) |  | [optional] 
**Content** | **string** | content must be base64 encoded | 
**Dates** | Pointer to [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**FromPath** | Pointer to **string** | from_path (optional) is the path of the original file which will be moved/renamed to the path in the URL | [optional] 
**Message** | Pointer to **string** | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**NewBranch** | Pointer to **string** | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**Sha** | **string** | sha is the SHA for the file that already exists | 
**Signoff** | Pointer to **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Methods

### NewUpdateFileOptions

`func NewUpdateFileOptions(content string, sha string, ) *UpdateFileOptions`

NewUpdateFileOptions instantiates a new UpdateFileOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateFileOptionsWithDefaults

`func NewUpdateFileOptionsWithDefaults() *UpdateFileOptions`

NewUpdateFileOptionsWithDefaults instantiates a new UpdateFileOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *UpdateFileOptions) GetAuthor() Identity`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *UpdateFileOptions) GetAuthorOk() (*Identity, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *UpdateFileOptions) SetAuthor(v Identity)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *UpdateFileOptions) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetBranch

`func (o *UpdateFileOptions) GetBranch() string`

GetBranch returns the Branch field if non-nil, zero value otherwise.

### GetBranchOk

`func (o *UpdateFileOptions) GetBranchOk() (*string, bool)`

GetBranchOk returns a tuple with the Branch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranch

`func (o *UpdateFileOptions) SetBranch(v string)`

SetBranch sets Branch field to given value.

### HasBranch

`func (o *UpdateFileOptions) HasBranch() bool`

HasBranch returns a boolean if a field has been set.

### GetCommitter

`func (o *UpdateFileOptions) GetCommitter() Identity`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *UpdateFileOptions) GetCommitterOk() (*Identity, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *UpdateFileOptions) SetCommitter(v Identity)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *UpdateFileOptions) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetContent

`func (o *UpdateFileOptions) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *UpdateFileOptions) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *UpdateFileOptions) SetContent(v string)`

SetContent sets Content field to given value.


### GetDates

`func (o *UpdateFileOptions) GetDates() CommitDateOptions`

GetDates returns the Dates field if non-nil, zero value otherwise.

### GetDatesOk

`func (o *UpdateFileOptions) GetDatesOk() (*CommitDateOptions, bool)`

GetDatesOk returns a tuple with the Dates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDates

`func (o *UpdateFileOptions) SetDates(v CommitDateOptions)`

SetDates sets Dates field to given value.

### HasDates

`func (o *UpdateFileOptions) HasDates() bool`

HasDates returns a boolean if a field has been set.

### GetFromPath

`func (o *UpdateFileOptions) GetFromPath() string`

GetFromPath returns the FromPath field if non-nil, zero value otherwise.

### GetFromPathOk

`func (o *UpdateFileOptions) GetFromPathOk() (*string, bool)`

GetFromPathOk returns a tuple with the FromPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromPath

`func (o *UpdateFileOptions) SetFromPath(v string)`

SetFromPath sets FromPath field to given value.

### HasFromPath

`func (o *UpdateFileOptions) HasFromPath() bool`

HasFromPath returns a boolean if a field has been set.

### GetMessage

`func (o *UpdateFileOptions) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *UpdateFileOptions) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *UpdateFileOptions) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *UpdateFileOptions) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetNewBranch

`func (o *UpdateFileOptions) GetNewBranch() string`

GetNewBranch returns the NewBranch field if non-nil, zero value otherwise.

### GetNewBranchOk

`func (o *UpdateFileOptions) GetNewBranchOk() (*string, bool)`

GetNewBranchOk returns a tuple with the NewBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewBranch

`func (o *UpdateFileOptions) SetNewBranch(v string)`

SetNewBranch sets NewBranch field to given value.

### HasNewBranch

`func (o *UpdateFileOptions) HasNewBranch() bool`

HasNewBranch returns a boolean if a field has been set.

### GetSha

`func (o *UpdateFileOptions) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *UpdateFileOptions) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *UpdateFileOptions) SetSha(v string)`

SetSha sets Sha field to given value.


### GetSignoff

`func (o *UpdateFileOptions) GetSignoff() bool`

GetSignoff returns the Signoff field if non-nil, zero value otherwise.

### GetSignoffOk

`func (o *UpdateFileOptions) GetSignoffOk() (*bool, bool)`

GetSignoffOk returns a tuple with the Signoff field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSignoff

`func (o *UpdateFileOptions) SetSignoff(v bool)`

SetSignoff sets Signoff field to given value.

### HasSignoff

`func (o *UpdateFileOptions) HasSignoff() bool`

HasSignoff returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



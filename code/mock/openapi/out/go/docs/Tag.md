# Tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Commit** | Pointer to [**CommitMeta**](CommitMeta.md) |  | [optional] 
**Id** | Pointer to **string** |  | [optional] 
**Message** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**TarballUrl** | Pointer to **string** |  | [optional] 
**ZipballUrl** | Pointer to **string** |  | [optional] 

## Methods

### NewTag

`func NewTag() *Tag`

NewTag instantiates a new Tag object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTagWithDefaults

`func NewTagWithDefaults() *Tag`

NewTagWithDefaults instantiates a new Tag object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommit

`func (o *Tag) GetCommit() CommitMeta`

GetCommit returns the Commit field if non-nil, zero value otherwise.

### GetCommitOk

`func (o *Tag) GetCommitOk() (*CommitMeta, bool)`

GetCommitOk returns a tuple with the Commit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommit

`func (o *Tag) SetCommit(v CommitMeta)`

SetCommit sets Commit field to given value.

### HasCommit

`func (o *Tag) HasCommit() bool`

HasCommit returns a boolean if a field has been set.

### GetId

`func (o *Tag) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Tag) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Tag) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Tag) HasId() bool`

HasId returns a boolean if a field has been set.

### GetMessage

`func (o *Tag) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *Tag) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *Tag) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *Tag) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetName

`func (o *Tag) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Tag) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Tag) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Tag) HasName() bool`

HasName returns a boolean if a field has been set.

### GetTarballUrl

`func (o *Tag) GetTarballUrl() string`

GetTarballUrl returns the TarballUrl field if non-nil, zero value otherwise.

### GetTarballUrlOk

`func (o *Tag) GetTarballUrlOk() (*string, bool)`

GetTarballUrlOk returns a tuple with the TarballUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarballUrl

`func (o *Tag) SetTarballUrl(v string)`

SetTarballUrl sets TarballUrl field to given value.

### HasTarballUrl

`func (o *Tag) HasTarballUrl() bool`

HasTarballUrl returns a boolean if a field has been set.

### GetZipballUrl

`func (o *Tag) GetZipballUrl() string`

GetZipballUrl returns the ZipballUrl field if non-nil, zero value otherwise.

### GetZipballUrlOk

`func (o *Tag) GetZipballUrlOk() (*string, bool)`

GetZipballUrlOk returns a tuple with the ZipballUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZipballUrl

`func (o *Tag) SetZipballUrl(v string)`

SetZipballUrl sets ZipballUrl field to given value.

### HasZipballUrl

`func (o *Tag) HasZipballUrl() bool`

HasZipballUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ChangeFileOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | Pointer to **string** | new or updated file content, must be base64 encoded | [optional] 
**FromPath** | Pointer to **string** | old path of the file to move | [optional] 
**Operation** | **string** | indicates what to do with the file | 
**Path** | **string** | path to the existing or new file | 
**Sha** | Pointer to **string** | sha is the SHA for the file that already exists, required for update or delete | [optional] 

## Methods

### NewChangeFileOperation

`func NewChangeFileOperation(operation string, path string, ) *ChangeFileOperation`

NewChangeFileOperation instantiates a new ChangeFileOperation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChangeFileOperationWithDefaults

`func NewChangeFileOperationWithDefaults() *ChangeFileOperation`

NewChangeFileOperationWithDefaults instantiates a new ChangeFileOperation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *ChangeFileOperation) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *ChangeFileOperation) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *ChangeFileOperation) SetContent(v string)`

SetContent sets Content field to given value.

### HasContent

`func (o *ChangeFileOperation) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetFromPath

`func (o *ChangeFileOperation) GetFromPath() string`

GetFromPath returns the FromPath field if non-nil, zero value otherwise.

### GetFromPathOk

`func (o *ChangeFileOperation) GetFromPathOk() (*string, bool)`

GetFromPathOk returns a tuple with the FromPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromPath

`func (o *ChangeFileOperation) SetFromPath(v string)`

SetFromPath sets FromPath field to given value.

### HasFromPath

`func (o *ChangeFileOperation) HasFromPath() bool`

HasFromPath returns a boolean if a field has been set.

### GetOperation

`func (o *ChangeFileOperation) GetOperation() string`

GetOperation returns the Operation field if non-nil, zero value otherwise.

### GetOperationOk

`func (o *ChangeFileOperation) GetOperationOk() (*string, bool)`

GetOperationOk returns a tuple with the Operation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperation

`func (o *ChangeFileOperation) SetOperation(v string)`

SetOperation sets Operation field to given value.


### GetPath

`func (o *ChangeFileOperation) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *ChangeFileOperation) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *ChangeFileOperation) SetPath(v string)`

SetPath sets Path field to given value.


### GetSha

`func (o *ChangeFileOperation) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *ChangeFileOperation) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *ChangeFileOperation) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *ChangeFileOperation) HasSha() bool`

HasSha returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



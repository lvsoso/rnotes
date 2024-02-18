# CreateWikiPageOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContentBase64** | Pointer to **string** | content must be base64 encoded | [optional] 
**Message** | Pointer to **string** | optional commit message summarizing the change | [optional] 
**Title** | Pointer to **string** | page title. leave empty to keep unchanged | [optional] 

## Methods

### NewCreateWikiPageOptions

`func NewCreateWikiPageOptions() *CreateWikiPageOptions`

NewCreateWikiPageOptions instantiates a new CreateWikiPageOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateWikiPageOptionsWithDefaults

`func NewCreateWikiPageOptionsWithDefaults() *CreateWikiPageOptions`

NewCreateWikiPageOptionsWithDefaults instantiates a new CreateWikiPageOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContentBase64

`func (o *CreateWikiPageOptions) GetContentBase64() string`

GetContentBase64 returns the ContentBase64 field if non-nil, zero value otherwise.

### GetContentBase64Ok

`func (o *CreateWikiPageOptions) GetContentBase64Ok() (*string, bool)`

GetContentBase64Ok returns a tuple with the ContentBase64 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentBase64

`func (o *CreateWikiPageOptions) SetContentBase64(v string)`

SetContentBase64 sets ContentBase64 field to given value.

### HasContentBase64

`func (o *CreateWikiPageOptions) HasContentBase64() bool`

HasContentBase64 returns a boolean if a field has been set.

### GetMessage

`func (o *CreateWikiPageOptions) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *CreateWikiPageOptions) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *CreateWikiPageOptions) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *CreateWikiPageOptions) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetTitle

`func (o *CreateWikiPageOptions) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CreateWikiPageOptions) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CreateWikiPageOptions) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *CreateWikiPageOptions) HasTitle() bool`

HasTitle returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MarkupOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Context** | Pointer to **string** | Context to render  in: body | [optional] 
**FilePath** | Pointer to **string** | File path for detecting extension in file mode  in: body | [optional] 
**Mode** | Pointer to **string** | Mode to render (comment, gfm, markdown, file)  in: body | [optional] 
**Text** | Pointer to **string** | Text markup to render  in: body | [optional] 
**Wiki** | Pointer to **bool** | Is it a wiki page ?  in: body | [optional] 

## Methods

### NewMarkupOption

`func NewMarkupOption() *MarkupOption`

NewMarkupOption instantiates a new MarkupOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMarkupOptionWithDefaults

`func NewMarkupOptionWithDefaults() *MarkupOption`

NewMarkupOptionWithDefaults instantiates a new MarkupOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContext

`func (o *MarkupOption) GetContext() string`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *MarkupOption) GetContextOk() (*string, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *MarkupOption) SetContext(v string)`

SetContext sets Context field to given value.

### HasContext

`func (o *MarkupOption) HasContext() bool`

HasContext returns a boolean if a field has been set.

### GetFilePath

`func (o *MarkupOption) GetFilePath() string`

GetFilePath returns the FilePath field if non-nil, zero value otherwise.

### GetFilePathOk

`func (o *MarkupOption) GetFilePathOk() (*string, bool)`

GetFilePathOk returns a tuple with the FilePath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilePath

`func (o *MarkupOption) SetFilePath(v string)`

SetFilePath sets FilePath field to given value.

### HasFilePath

`func (o *MarkupOption) HasFilePath() bool`

HasFilePath returns a boolean if a field has been set.

### GetMode

`func (o *MarkupOption) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *MarkupOption) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *MarkupOption) SetMode(v string)`

SetMode sets Mode field to given value.

### HasMode

`func (o *MarkupOption) HasMode() bool`

HasMode returns a boolean if a field has been set.

### GetText

`func (o *MarkupOption) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *MarkupOption) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *MarkupOption) SetText(v string)`

SetText sets Text field to given value.

### HasText

`func (o *MarkupOption) HasText() bool`

HasText returns a boolean if a field has been set.

### GetWiki

`func (o *MarkupOption) GetWiki() bool`

GetWiki returns the Wiki field if non-nil, zero value otherwise.

### GetWikiOk

`func (o *MarkupOption) GetWikiOk() (*bool, bool)`

GetWikiOk returns a tuple with the Wiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWiki

`func (o *MarkupOption) SetWiki(v bool)`

SetWiki sets Wiki field to given value.

### HasWiki

`func (o *MarkupOption) HasWiki() bool`

HasWiki returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



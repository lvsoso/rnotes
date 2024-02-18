# MarkdownOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Context** | Pointer to **string** | Context to render  in: body | [optional] 
**Mode** | Pointer to **string** | Mode to render (comment, gfm, markdown)  in: body | [optional] 
**Text** | Pointer to **string** | Text markdown to render  in: body | [optional] 
**Wiki** | Pointer to **bool** | Is it a wiki page ?  in: body | [optional] 

## Methods

### NewMarkdownOption

`func NewMarkdownOption() *MarkdownOption`

NewMarkdownOption instantiates a new MarkdownOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMarkdownOptionWithDefaults

`func NewMarkdownOptionWithDefaults() *MarkdownOption`

NewMarkdownOptionWithDefaults instantiates a new MarkdownOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContext

`func (o *MarkdownOption) GetContext() string`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *MarkdownOption) GetContextOk() (*string, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *MarkdownOption) SetContext(v string)`

SetContext sets Context field to given value.

### HasContext

`func (o *MarkdownOption) HasContext() bool`

HasContext returns a boolean if a field has been set.

### GetMode

`func (o *MarkdownOption) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *MarkdownOption) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *MarkdownOption) SetMode(v string)`

SetMode sets Mode field to given value.

### HasMode

`func (o *MarkdownOption) HasMode() bool`

HasMode returns a boolean if a field has been set.

### GetText

`func (o *MarkdownOption) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *MarkdownOption) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *MarkdownOption) SetText(v string)`

SetText sets Text field to given value.

### HasText

`func (o *MarkdownOption) HasText() bool`

HasText returns a boolean if a field has been set.

### GetWiki

`func (o *MarkdownOption) GetWiki() bool`

GetWiki returns the Wiki field if non-nil, zero value otherwise.

### GetWikiOk

`func (o *MarkdownOption) GetWikiOk() (*bool, bool)`

GetWikiOk returns a tuple with the Wiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWiki

`func (o *MarkdownOption) SetWiki(v bool)`

SetWiki sets Wiki field to given value.

### HasWiki

`func (o *MarkdownOption) HasWiki() bool`

HasWiki returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



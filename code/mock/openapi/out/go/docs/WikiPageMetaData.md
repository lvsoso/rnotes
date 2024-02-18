# WikiPageMetaData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HtmlUrl** | Pointer to **string** |  | [optional] 
**LastCommit** | Pointer to [**WikiCommit**](WikiCommit.md) |  | [optional] 
**SubUrl** | Pointer to **string** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 

## Methods

### NewWikiPageMetaData

`func NewWikiPageMetaData() *WikiPageMetaData`

NewWikiPageMetaData instantiates a new WikiPageMetaData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWikiPageMetaDataWithDefaults

`func NewWikiPageMetaDataWithDefaults() *WikiPageMetaData`

NewWikiPageMetaDataWithDefaults instantiates a new WikiPageMetaData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHtmlUrl

`func (o *WikiPageMetaData) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *WikiPageMetaData) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *WikiPageMetaData) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *WikiPageMetaData) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetLastCommit

`func (o *WikiPageMetaData) GetLastCommit() WikiCommit`

GetLastCommit returns the LastCommit field if non-nil, zero value otherwise.

### GetLastCommitOk

`func (o *WikiPageMetaData) GetLastCommitOk() (*WikiCommit, bool)`

GetLastCommitOk returns a tuple with the LastCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCommit

`func (o *WikiPageMetaData) SetLastCommit(v WikiCommit)`

SetLastCommit sets LastCommit field to given value.

### HasLastCommit

`func (o *WikiPageMetaData) HasLastCommit() bool`

HasLastCommit returns a boolean if a field has been set.

### GetSubUrl

`func (o *WikiPageMetaData) GetSubUrl() string`

GetSubUrl returns the SubUrl field if non-nil, zero value otherwise.

### GetSubUrlOk

`func (o *WikiPageMetaData) GetSubUrlOk() (*string, bool)`

GetSubUrlOk returns a tuple with the SubUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubUrl

`func (o *WikiPageMetaData) SetSubUrl(v string)`

SetSubUrl sets SubUrl field to given value.

### HasSubUrl

`func (o *WikiPageMetaData) HasSubUrl() bool`

HasSubUrl returns a boolean if a field has been set.

### GetTitle

`func (o *WikiPageMetaData) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *WikiPageMetaData) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *WikiPageMetaData) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *WikiPageMetaData) HasTitle() bool`

HasTitle returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



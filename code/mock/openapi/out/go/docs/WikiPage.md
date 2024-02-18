# WikiPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CommitCount** | Pointer to **int64** |  | [optional] 
**ContentBase64** | Pointer to **string** | Page content, base64 encoded | [optional] 
**Footer** | Pointer to **string** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**LastCommit** | Pointer to [**WikiCommit**](WikiCommit.md) |  | [optional] 
**Sidebar** | Pointer to **string** |  | [optional] 
**SubUrl** | Pointer to **string** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 

## Methods

### NewWikiPage

`func NewWikiPage() *WikiPage`

NewWikiPage instantiates a new WikiPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWikiPageWithDefaults

`func NewWikiPageWithDefaults() *WikiPage`

NewWikiPageWithDefaults instantiates a new WikiPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommitCount

`func (o *WikiPage) GetCommitCount() int64`

GetCommitCount returns the CommitCount field if non-nil, zero value otherwise.

### GetCommitCountOk

`func (o *WikiPage) GetCommitCountOk() (*int64, bool)`

GetCommitCountOk returns a tuple with the CommitCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitCount

`func (o *WikiPage) SetCommitCount(v int64)`

SetCommitCount sets CommitCount field to given value.

### HasCommitCount

`func (o *WikiPage) HasCommitCount() bool`

HasCommitCount returns a boolean if a field has been set.

### GetContentBase64

`func (o *WikiPage) GetContentBase64() string`

GetContentBase64 returns the ContentBase64 field if non-nil, zero value otherwise.

### GetContentBase64Ok

`func (o *WikiPage) GetContentBase64Ok() (*string, bool)`

GetContentBase64Ok returns a tuple with the ContentBase64 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentBase64

`func (o *WikiPage) SetContentBase64(v string)`

SetContentBase64 sets ContentBase64 field to given value.

### HasContentBase64

`func (o *WikiPage) HasContentBase64() bool`

HasContentBase64 returns a boolean if a field has been set.

### GetFooter

`func (o *WikiPage) GetFooter() string`

GetFooter returns the Footer field if non-nil, zero value otherwise.

### GetFooterOk

`func (o *WikiPage) GetFooterOk() (*string, bool)`

GetFooterOk returns a tuple with the Footer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFooter

`func (o *WikiPage) SetFooter(v string)`

SetFooter sets Footer field to given value.

### HasFooter

`func (o *WikiPage) HasFooter() bool`

HasFooter returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *WikiPage) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *WikiPage) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *WikiPage) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *WikiPage) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetLastCommit

`func (o *WikiPage) GetLastCommit() WikiCommit`

GetLastCommit returns the LastCommit field if non-nil, zero value otherwise.

### GetLastCommitOk

`func (o *WikiPage) GetLastCommitOk() (*WikiCommit, bool)`

GetLastCommitOk returns a tuple with the LastCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCommit

`func (o *WikiPage) SetLastCommit(v WikiCommit)`

SetLastCommit sets LastCommit field to given value.

### HasLastCommit

`func (o *WikiPage) HasLastCommit() bool`

HasLastCommit returns a boolean if a field has been set.

### GetSidebar

`func (o *WikiPage) GetSidebar() string`

GetSidebar returns the Sidebar field if non-nil, zero value otherwise.

### GetSidebarOk

`func (o *WikiPage) GetSidebarOk() (*string, bool)`

GetSidebarOk returns a tuple with the Sidebar field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSidebar

`func (o *WikiPage) SetSidebar(v string)`

SetSidebar sets Sidebar field to given value.

### HasSidebar

`func (o *WikiPage) HasSidebar() bool`

HasSidebar returns a boolean if a field has been set.

### GetSubUrl

`func (o *WikiPage) GetSubUrl() string`

GetSubUrl returns the SubUrl field if non-nil, zero value otherwise.

### GetSubUrlOk

`func (o *WikiPage) GetSubUrlOk() (*string, bool)`

GetSubUrlOk returns a tuple with the SubUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubUrl

`func (o *WikiPage) SetSubUrl(v string)`

SetSubUrl sets SubUrl field to given value.

### HasSubUrl

`func (o *WikiPage) HasSubUrl() bool`

HasSubUrl returns a boolean if a field has been set.

### GetTitle

`func (o *WikiPage) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *WikiPage) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *WikiPage) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *WikiPage) HasTitle() bool`

HasTitle returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Links** | Pointer to [**FileLinksResponse**](FileLinksResponse.md) |  | [optional] 
**Content** | Pointer to **string** | &#x60;content&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional] 
**DownloadUrl** | Pointer to **string** |  | [optional] 
**Encoding** | Pointer to **string** | &#x60;encoding&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional] 
**GitUrl** | Pointer to **string** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**LastCommitSha** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Path** | Pointer to **string** |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**Size** | Pointer to **int64** |  | [optional] 
**SubmoduleGitUrl** | Pointer to **string** | &#x60;submodule_git_url&#x60; is populated when &#x60;type&#x60; is &#x60;submodule&#x60;, otherwise null | [optional] 
**Target** | Pointer to **string** | &#x60;target&#x60; is populated when &#x60;type&#x60; is &#x60;symlink&#x60;, otherwise null | [optional] 
**Type** | Pointer to **string** | &#x60;type&#x60; will be &#x60;file&#x60;, &#x60;dir&#x60;, &#x60;symlink&#x60;, or &#x60;submodule&#x60; | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewContentsResponse

`func NewContentsResponse() *ContentsResponse`

NewContentsResponse instantiates a new ContentsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentsResponseWithDefaults

`func NewContentsResponseWithDefaults() *ContentsResponse`

NewContentsResponseWithDefaults instantiates a new ContentsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinks

`func (o *ContentsResponse) GetLinks() FileLinksResponse`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *ContentsResponse) GetLinksOk() (*FileLinksResponse, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *ContentsResponse) SetLinks(v FileLinksResponse)`

SetLinks sets Links field to given value.

### HasLinks

`func (o *ContentsResponse) HasLinks() bool`

HasLinks returns a boolean if a field has been set.

### GetContent

`func (o *ContentsResponse) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *ContentsResponse) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *ContentsResponse) SetContent(v string)`

SetContent sets Content field to given value.

### HasContent

`func (o *ContentsResponse) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetDownloadUrl

`func (o *ContentsResponse) GetDownloadUrl() string`

GetDownloadUrl returns the DownloadUrl field if non-nil, zero value otherwise.

### GetDownloadUrlOk

`func (o *ContentsResponse) GetDownloadUrlOk() (*string, bool)`

GetDownloadUrlOk returns a tuple with the DownloadUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDownloadUrl

`func (o *ContentsResponse) SetDownloadUrl(v string)`

SetDownloadUrl sets DownloadUrl field to given value.

### HasDownloadUrl

`func (o *ContentsResponse) HasDownloadUrl() bool`

HasDownloadUrl returns a boolean if a field has been set.

### GetEncoding

`func (o *ContentsResponse) GetEncoding() string`

GetEncoding returns the Encoding field if non-nil, zero value otherwise.

### GetEncodingOk

`func (o *ContentsResponse) GetEncodingOk() (*string, bool)`

GetEncodingOk returns a tuple with the Encoding field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEncoding

`func (o *ContentsResponse) SetEncoding(v string)`

SetEncoding sets Encoding field to given value.

### HasEncoding

`func (o *ContentsResponse) HasEncoding() bool`

HasEncoding returns a boolean if a field has been set.

### GetGitUrl

`func (o *ContentsResponse) GetGitUrl() string`

GetGitUrl returns the GitUrl field if non-nil, zero value otherwise.

### GetGitUrlOk

`func (o *ContentsResponse) GetGitUrlOk() (*string, bool)`

GetGitUrlOk returns a tuple with the GitUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGitUrl

`func (o *ContentsResponse) SetGitUrl(v string)`

SetGitUrl sets GitUrl field to given value.

### HasGitUrl

`func (o *ContentsResponse) HasGitUrl() bool`

HasGitUrl returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *ContentsResponse) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *ContentsResponse) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *ContentsResponse) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *ContentsResponse) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetLastCommitSha

`func (o *ContentsResponse) GetLastCommitSha() string`

GetLastCommitSha returns the LastCommitSha field if non-nil, zero value otherwise.

### GetLastCommitShaOk

`func (o *ContentsResponse) GetLastCommitShaOk() (*string, bool)`

GetLastCommitShaOk returns a tuple with the LastCommitSha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCommitSha

`func (o *ContentsResponse) SetLastCommitSha(v string)`

SetLastCommitSha sets LastCommitSha field to given value.

### HasLastCommitSha

`func (o *ContentsResponse) HasLastCommitSha() bool`

HasLastCommitSha returns a boolean if a field has been set.

### GetName

`func (o *ContentsResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ContentsResponse) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ContentsResponse) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *ContentsResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPath

`func (o *ContentsResponse) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *ContentsResponse) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *ContentsResponse) SetPath(v string)`

SetPath sets Path field to given value.

### HasPath

`func (o *ContentsResponse) HasPath() bool`

HasPath returns a boolean if a field has been set.

### GetSha

`func (o *ContentsResponse) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *ContentsResponse) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *ContentsResponse) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *ContentsResponse) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetSize

`func (o *ContentsResponse) GetSize() int64`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *ContentsResponse) GetSizeOk() (*int64, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *ContentsResponse) SetSize(v int64)`

SetSize sets Size field to given value.

### HasSize

`func (o *ContentsResponse) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetSubmoduleGitUrl

`func (o *ContentsResponse) GetSubmoduleGitUrl() string`

GetSubmoduleGitUrl returns the SubmoduleGitUrl field if non-nil, zero value otherwise.

### GetSubmoduleGitUrlOk

`func (o *ContentsResponse) GetSubmoduleGitUrlOk() (*string, bool)`

GetSubmoduleGitUrlOk returns a tuple with the SubmoduleGitUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubmoduleGitUrl

`func (o *ContentsResponse) SetSubmoduleGitUrl(v string)`

SetSubmoduleGitUrl sets SubmoduleGitUrl field to given value.

### HasSubmoduleGitUrl

`func (o *ContentsResponse) HasSubmoduleGitUrl() bool`

HasSubmoduleGitUrl returns a boolean if a field has been set.

### GetTarget

`func (o *ContentsResponse) GetTarget() string`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *ContentsResponse) GetTargetOk() (*string, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *ContentsResponse) SetTarget(v string)`

SetTarget sets Target field to given value.

### HasTarget

`func (o *ContentsResponse) HasTarget() bool`

HasTarget returns a boolean if a field has been set.

### GetType

`func (o *ContentsResponse) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ContentsResponse) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ContentsResponse) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *ContentsResponse) HasType() bool`

HasType returns a boolean if a field has been set.

### GetUrl

`func (o *ContentsResponse) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *ContentsResponse) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *ContentsResponse) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *ContentsResponse) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



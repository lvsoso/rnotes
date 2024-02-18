# GitTreeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Page** | Pointer to **int64** |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**TotalCount** | Pointer to **int64** |  | [optional] 
**Tree** | Pointer to [**[]GitEntry**](GitEntry.md) |  | [optional] 
**Truncated** | Pointer to **bool** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewGitTreeResponse

`func NewGitTreeResponse() *GitTreeResponse`

NewGitTreeResponse instantiates a new GitTreeResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGitTreeResponseWithDefaults

`func NewGitTreeResponseWithDefaults() *GitTreeResponse`

NewGitTreeResponseWithDefaults instantiates a new GitTreeResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPage

`func (o *GitTreeResponse) GetPage() int64`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *GitTreeResponse) GetPageOk() (*int64, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *GitTreeResponse) SetPage(v int64)`

SetPage sets Page field to given value.

### HasPage

`func (o *GitTreeResponse) HasPage() bool`

HasPage returns a boolean if a field has been set.

### GetSha

`func (o *GitTreeResponse) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *GitTreeResponse) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *GitTreeResponse) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *GitTreeResponse) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetTotalCount

`func (o *GitTreeResponse) GetTotalCount() int64`

GetTotalCount returns the TotalCount field if non-nil, zero value otherwise.

### GetTotalCountOk

`func (o *GitTreeResponse) GetTotalCountOk() (*int64, bool)`

GetTotalCountOk returns a tuple with the TotalCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCount

`func (o *GitTreeResponse) SetTotalCount(v int64)`

SetTotalCount sets TotalCount field to given value.

### HasTotalCount

`func (o *GitTreeResponse) HasTotalCount() bool`

HasTotalCount returns a boolean if a field has been set.

### GetTree

`func (o *GitTreeResponse) GetTree() []GitEntry`

GetTree returns the Tree field if non-nil, zero value otherwise.

### GetTreeOk

`func (o *GitTreeResponse) GetTreeOk() (*[]GitEntry, bool)`

GetTreeOk returns a tuple with the Tree field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTree

`func (o *GitTreeResponse) SetTree(v []GitEntry)`

SetTree sets Tree field to given value.

### HasTree

`func (o *GitTreeResponse) HasTree() bool`

HasTree returns a boolean if a field has been set.

### GetTruncated

`func (o *GitTreeResponse) GetTruncated() bool`

GetTruncated returns the Truncated field if non-nil, zero value otherwise.

### GetTruncatedOk

`func (o *GitTreeResponse) GetTruncatedOk() (*bool, bool)`

GetTruncatedOk returns a tuple with the Truncated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTruncated

`func (o *GitTreeResponse) SetTruncated(v bool)`

SetTruncated sets Truncated field to given value.

### HasTruncated

`func (o *GitTreeResponse) HasTruncated() bool`

HasTruncated returns a boolean if a field has been set.

### GetUrl

`func (o *GitTreeResponse) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *GitTreeResponse) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *GitTreeResponse) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *GitTreeResponse) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



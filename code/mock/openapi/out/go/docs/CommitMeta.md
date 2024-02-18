# CommitMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | Pointer to **time.Time** |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewCommitMeta

`func NewCommitMeta() *CommitMeta`

NewCommitMeta instantiates a new CommitMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCommitMetaWithDefaults

`func NewCommitMetaWithDefaults() *CommitMeta`

NewCommitMetaWithDefaults instantiates a new CommitMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *CommitMeta) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *CommitMeta) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *CommitMeta) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *CommitMeta) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetSha

`func (o *CommitMeta) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *CommitMeta) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *CommitMeta) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *CommitMeta) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetUrl

`func (o *CommitMeta) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *CommitMeta) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *CommitMeta) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *CommitMeta) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assets** | Pointer to [**[]Attachment**](Attachment.md) |  | [optional] 
**Author** | Pointer to [**User**](User.md) |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**Draft** | Pointer to **bool** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Prerelease** | Pointer to **bool** |  | [optional] 
**PublishedAt** | Pointer to **time.Time** |  | [optional] 
**TagName** | Pointer to **string** |  | [optional] 
**TarballUrl** | Pointer to **string** |  | [optional] 
**TargetCommitish** | Pointer to **string** |  | [optional] 
**UploadUrl** | Pointer to **string** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**ZipballUrl** | Pointer to **string** |  | [optional] 

## Methods

### NewRelease

`func NewRelease() *Release`

NewRelease instantiates a new Release object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewReleaseWithDefaults

`func NewReleaseWithDefaults() *Release`

NewReleaseWithDefaults instantiates a new Release object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssets

`func (o *Release) GetAssets() []Attachment`

GetAssets returns the Assets field if non-nil, zero value otherwise.

### GetAssetsOk

`func (o *Release) GetAssetsOk() (*[]Attachment, bool)`

GetAssetsOk returns a tuple with the Assets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssets

`func (o *Release) SetAssets(v []Attachment)`

SetAssets sets Assets field to given value.

### HasAssets

`func (o *Release) HasAssets() bool`

HasAssets returns a boolean if a field has been set.

### GetAuthor

`func (o *Release) GetAuthor() User`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *Release) GetAuthorOk() (*User, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *Release) SetAuthor(v User)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *Release) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetBody

`func (o *Release) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *Release) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *Release) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *Release) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Release) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Release) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Release) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Release) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDraft

`func (o *Release) GetDraft() bool`

GetDraft returns the Draft field if non-nil, zero value otherwise.

### GetDraftOk

`func (o *Release) GetDraftOk() (*bool, bool)`

GetDraftOk returns a tuple with the Draft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraft

`func (o *Release) SetDraft(v bool)`

SetDraft sets Draft field to given value.

### HasDraft

`func (o *Release) HasDraft() bool`

HasDraft returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *Release) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *Release) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *Release) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *Release) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *Release) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Release) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Release) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Release) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *Release) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Release) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Release) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Release) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrerelease

`func (o *Release) GetPrerelease() bool`

GetPrerelease returns the Prerelease field if non-nil, zero value otherwise.

### GetPrereleaseOk

`func (o *Release) GetPrereleaseOk() (*bool, bool)`

GetPrereleaseOk returns a tuple with the Prerelease field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrerelease

`func (o *Release) SetPrerelease(v bool)`

SetPrerelease sets Prerelease field to given value.

### HasPrerelease

`func (o *Release) HasPrerelease() bool`

HasPrerelease returns a boolean if a field has been set.

### GetPublishedAt

`func (o *Release) GetPublishedAt() time.Time`

GetPublishedAt returns the PublishedAt field if non-nil, zero value otherwise.

### GetPublishedAtOk

`func (o *Release) GetPublishedAtOk() (*time.Time, bool)`

GetPublishedAtOk returns a tuple with the PublishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublishedAt

`func (o *Release) SetPublishedAt(v time.Time)`

SetPublishedAt sets PublishedAt field to given value.

### HasPublishedAt

`func (o *Release) HasPublishedAt() bool`

HasPublishedAt returns a boolean if a field has been set.

### GetTagName

`func (o *Release) GetTagName() string`

GetTagName returns the TagName field if non-nil, zero value otherwise.

### GetTagNameOk

`func (o *Release) GetTagNameOk() (*string, bool)`

GetTagNameOk returns a tuple with the TagName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagName

`func (o *Release) SetTagName(v string)`

SetTagName sets TagName field to given value.

### HasTagName

`func (o *Release) HasTagName() bool`

HasTagName returns a boolean if a field has been set.

### GetTarballUrl

`func (o *Release) GetTarballUrl() string`

GetTarballUrl returns the TarballUrl field if non-nil, zero value otherwise.

### GetTarballUrlOk

`func (o *Release) GetTarballUrlOk() (*string, bool)`

GetTarballUrlOk returns a tuple with the TarballUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarballUrl

`func (o *Release) SetTarballUrl(v string)`

SetTarballUrl sets TarballUrl field to given value.

### HasTarballUrl

`func (o *Release) HasTarballUrl() bool`

HasTarballUrl returns a boolean if a field has been set.

### GetTargetCommitish

`func (o *Release) GetTargetCommitish() string`

GetTargetCommitish returns the TargetCommitish field if non-nil, zero value otherwise.

### GetTargetCommitishOk

`func (o *Release) GetTargetCommitishOk() (*string, bool)`

GetTargetCommitishOk returns a tuple with the TargetCommitish field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetCommitish

`func (o *Release) SetTargetCommitish(v string)`

SetTargetCommitish sets TargetCommitish field to given value.

### HasTargetCommitish

`func (o *Release) HasTargetCommitish() bool`

HasTargetCommitish returns a boolean if a field has been set.

### GetUploadUrl

`func (o *Release) GetUploadUrl() string`

GetUploadUrl returns the UploadUrl field if non-nil, zero value otherwise.

### GetUploadUrlOk

`func (o *Release) GetUploadUrlOk() (*string, bool)`

GetUploadUrlOk returns a tuple with the UploadUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadUrl

`func (o *Release) SetUploadUrl(v string)`

SetUploadUrl sets UploadUrl field to given value.

### HasUploadUrl

`func (o *Release) HasUploadUrl() bool`

HasUploadUrl returns a boolean if a field has been set.

### GetUrl

`func (o *Release) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Release) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Release) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *Release) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetZipballUrl

`func (o *Release) GetZipballUrl() string`

GetZipballUrl returns the ZipballUrl field if non-nil, zero value otherwise.

### GetZipballUrlOk

`func (o *Release) GetZipballUrlOk() (*string, bool)`

GetZipballUrlOk returns a tuple with the ZipballUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZipballUrl

`func (o *Release) SetZipballUrl(v string)`

SetZipballUrl sets ZipballUrl field to given value.

### HasZipballUrl

`func (o *Release) HasZipballUrl() bool`

HasZipballUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



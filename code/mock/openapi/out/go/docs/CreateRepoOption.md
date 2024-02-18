# CreateRepoOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AutoInit** | Pointer to **bool** | Whether the repository should be auto-initialized? | [optional] 
**DefaultBranch** | Pointer to **string** | DefaultBranch of the repository (used when initializes and in template) | [optional] 
**Description** | Pointer to **string** | Description of the repository to create | [optional] 
**Gitignores** | Pointer to **string** | Gitignores to use | [optional] 
**IssueLabels** | Pointer to **string** | Label-Set to use | [optional] 
**License** | Pointer to **string** | License to use | [optional] 
**Name** | **string** | Name of the repository to create | 
**ObjectFormatName** | Pointer to **string** | ObjectFormatName of the underlying git repository | [optional] 
**Private** | Pointer to **bool** | Whether the repository is private | [optional] 
**Readme** | Pointer to **string** | Readme of the repository to create | [optional] 
**Template** | Pointer to **bool** | Whether the repository is template | [optional] 
**TrustModel** | Pointer to **string** | TrustModel of the repository | [optional] 

## Methods

### NewCreateRepoOption

`func NewCreateRepoOption(name string, ) *CreateRepoOption`

NewCreateRepoOption instantiates a new CreateRepoOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateRepoOptionWithDefaults

`func NewCreateRepoOptionWithDefaults() *CreateRepoOption`

NewCreateRepoOptionWithDefaults instantiates a new CreateRepoOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAutoInit

`func (o *CreateRepoOption) GetAutoInit() bool`

GetAutoInit returns the AutoInit field if non-nil, zero value otherwise.

### GetAutoInitOk

`func (o *CreateRepoOption) GetAutoInitOk() (*bool, bool)`

GetAutoInitOk returns a tuple with the AutoInit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoInit

`func (o *CreateRepoOption) SetAutoInit(v bool)`

SetAutoInit sets AutoInit field to given value.

### HasAutoInit

`func (o *CreateRepoOption) HasAutoInit() bool`

HasAutoInit returns a boolean if a field has been set.

### GetDefaultBranch

`func (o *CreateRepoOption) GetDefaultBranch() string`

GetDefaultBranch returns the DefaultBranch field if non-nil, zero value otherwise.

### GetDefaultBranchOk

`func (o *CreateRepoOption) GetDefaultBranchOk() (*string, bool)`

GetDefaultBranchOk returns a tuple with the DefaultBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultBranch

`func (o *CreateRepoOption) SetDefaultBranch(v string)`

SetDefaultBranch sets DefaultBranch field to given value.

### HasDefaultBranch

`func (o *CreateRepoOption) HasDefaultBranch() bool`

HasDefaultBranch returns a boolean if a field has been set.

### GetDescription

`func (o *CreateRepoOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateRepoOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateRepoOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateRepoOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetGitignores

`func (o *CreateRepoOption) GetGitignores() string`

GetGitignores returns the Gitignores field if non-nil, zero value otherwise.

### GetGitignoresOk

`func (o *CreateRepoOption) GetGitignoresOk() (*string, bool)`

GetGitignoresOk returns a tuple with the Gitignores field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGitignores

`func (o *CreateRepoOption) SetGitignores(v string)`

SetGitignores sets Gitignores field to given value.

### HasGitignores

`func (o *CreateRepoOption) HasGitignores() bool`

HasGitignores returns a boolean if a field has been set.

### GetIssueLabels

`func (o *CreateRepoOption) GetIssueLabels() string`

GetIssueLabels returns the IssueLabels field if non-nil, zero value otherwise.

### GetIssueLabelsOk

`func (o *CreateRepoOption) GetIssueLabelsOk() (*string, bool)`

GetIssueLabelsOk returns a tuple with the IssueLabels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueLabels

`func (o *CreateRepoOption) SetIssueLabels(v string)`

SetIssueLabels sets IssueLabels field to given value.

### HasIssueLabels

`func (o *CreateRepoOption) HasIssueLabels() bool`

HasIssueLabels returns a boolean if a field has been set.

### GetLicense

`func (o *CreateRepoOption) GetLicense() string`

GetLicense returns the License field if non-nil, zero value otherwise.

### GetLicenseOk

`func (o *CreateRepoOption) GetLicenseOk() (*string, bool)`

GetLicenseOk returns a tuple with the License field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLicense

`func (o *CreateRepoOption) SetLicense(v string)`

SetLicense sets License field to given value.

### HasLicense

`func (o *CreateRepoOption) HasLicense() bool`

HasLicense returns a boolean if a field has been set.

### GetName

`func (o *CreateRepoOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateRepoOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateRepoOption) SetName(v string)`

SetName sets Name field to given value.


### GetObjectFormatName

`func (o *CreateRepoOption) GetObjectFormatName() string`

GetObjectFormatName returns the ObjectFormatName field if non-nil, zero value otherwise.

### GetObjectFormatNameOk

`func (o *CreateRepoOption) GetObjectFormatNameOk() (*string, bool)`

GetObjectFormatNameOk returns a tuple with the ObjectFormatName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectFormatName

`func (o *CreateRepoOption) SetObjectFormatName(v string)`

SetObjectFormatName sets ObjectFormatName field to given value.

### HasObjectFormatName

`func (o *CreateRepoOption) HasObjectFormatName() bool`

HasObjectFormatName returns a boolean if a field has been set.

### GetPrivate

`func (o *CreateRepoOption) GetPrivate() bool`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *CreateRepoOption) GetPrivateOk() (*bool, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *CreateRepoOption) SetPrivate(v bool)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *CreateRepoOption) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.

### GetReadme

`func (o *CreateRepoOption) GetReadme() string`

GetReadme returns the Readme field if non-nil, zero value otherwise.

### GetReadmeOk

`func (o *CreateRepoOption) GetReadmeOk() (*string, bool)`

GetReadmeOk returns a tuple with the Readme field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReadme

`func (o *CreateRepoOption) SetReadme(v string)`

SetReadme sets Readme field to given value.

### HasReadme

`func (o *CreateRepoOption) HasReadme() bool`

HasReadme returns a boolean if a field has been set.

### GetTemplate

`func (o *CreateRepoOption) GetTemplate() bool`

GetTemplate returns the Template field if non-nil, zero value otherwise.

### GetTemplateOk

`func (o *CreateRepoOption) GetTemplateOk() (*bool, bool)`

GetTemplateOk returns a tuple with the Template field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemplate

`func (o *CreateRepoOption) SetTemplate(v bool)`

SetTemplate sets Template field to given value.

### HasTemplate

`func (o *CreateRepoOption) HasTemplate() bool`

HasTemplate returns a boolean if a field has been set.

### GetTrustModel

`func (o *CreateRepoOption) GetTrustModel() string`

GetTrustModel returns the TrustModel field if non-nil, zero value otherwise.

### GetTrustModelOk

`func (o *CreateRepoOption) GetTrustModelOk() (*string, bool)`

GetTrustModelOk returns a tuple with the TrustModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrustModel

`func (o *CreateRepoOption) SetTrustModel(v string)`

SetTrustModel sets TrustModel field to given value.

### HasTrustModel

`func (o *CreateRepoOption) HasTrustModel() bool`

HasTrustModel returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



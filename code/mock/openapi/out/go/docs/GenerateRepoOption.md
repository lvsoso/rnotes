# GenerateRepoOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Avatar** | Pointer to **bool** | include avatar of the template repo | [optional] 
**DefaultBranch** | Pointer to **string** | Default branch of the new repository | [optional] 
**Description** | Pointer to **string** | Description of the repository to create | [optional] 
**GitContent** | Pointer to **bool** | include git content of default branch in template repo | [optional] 
**GitHooks** | Pointer to **bool** | include git hooks in template repo | [optional] 
**Labels** | Pointer to **bool** | include labels in template repo | [optional] 
**Name** | **string** | Name of the repository to create | 
**Owner** | **string** | The organization or person who will own the new repository | 
**Private** | Pointer to **bool** | Whether the repository is private | [optional] 
**ProtectedBranch** | Pointer to **bool** | include protected branches in template repo | [optional] 
**Topics** | Pointer to **bool** | include topics in template repo | [optional] 
**Webhooks** | Pointer to **bool** | include webhooks in template repo | [optional] 

## Methods

### NewGenerateRepoOption

`func NewGenerateRepoOption(name string, owner string, ) *GenerateRepoOption`

NewGenerateRepoOption instantiates a new GenerateRepoOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGenerateRepoOptionWithDefaults

`func NewGenerateRepoOptionWithDefaults() *GenerateRepoOption`

NewGenerateRepoOptionWithDefaults instantiates a new GenerateRepoOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvatar

`func (o *GenerateRepoOption) GetAvatar() bool`

GetAvatar returns the Avatar field if non-nil, zero value otherwise.

### GetAvatarOk

`func (o *GenerateRepoOption) GetAvatarOk() (*bool, bool)`

GetAvatarOk returns a tuple with the Avatar field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatar

`func (o *GenerateRepoOption) SetAvatar(v bool)`

SetAvatar sets Avatar field to given value.

### HasAvatar

`func (o *GenerateRepoOption) HasAvatar() bool`

HasAvatar returns a boolean if a field has been set.

### GetDefaultBranch

`func (o *GenerateRepoOption) GetDefaultBranch() string`

GetDefaultBranch returns the DefaultBranch field if non-nil, zero value otherwise.

### GetDefaultBranchOk

`func (o *GenerateRepoOption) GetDefaultBranchOk() (*string, bool)`

GetDefaultBranchOk returns a tuple with the DefaultBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultBranch

`func (o *GenerateRepoOption) SetDefaultBranch(v string)`

SetDefaultBranch sets DefaultBranch field to given value.

### HasDefaultBranch

`func (o *GenerateRepoOption) HasDefaultBranch() bool`

HasDefaultBranch returns a boolean if a field has been set.

### GetDescription

`func (o *GenerateRepoOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *GenerateRepoOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *GenerateRepoOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *GenerateRepoOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetGitContent

`func (o *GenerateRepoOption) GetGitContent() bool`

GetGitContent returns the GitContent field if non-nil, zero value otherwise.

### GetGitContentOk

`func (o *GenerateRepoOption) GetGitContentOk() (*bool, bool)`

GetGitContentOk returns a tuple with the GitContent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGitContent

`func (o *GenerateRepoOption) SetGitContent(v bool)`

SetGitContent sets GitContent field to given value.

### HasGitContent

`func (o *GenerateRepoOption) HasGitContent() bool`

HasGitContent returns a boolean if a field has been set.

### GetGitHooks

`func (o *GenerateRepoOption) GetGitHooks() bool`

GetGitHooks returns the GitHooks field if non-nil, zero value otherwise.

### GetGitHooksOk

`func (o *GenerateRepoOption) GetGitHooksOk() (*bool, bool)`

GetGitHooksOk returns a tuple with the GitHooks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGitHooks

`func (o *GenerateRepoOption) SetGitHooks(v bool)`

SetGitHooks sets GitHooks field to given value.

### HasGitHooks

`func (o *GenerateRepoOption) HasGitHooks() bool`

HasGitHooks returns a boolean if a field has been set.

### GetLabels

`func (o *GenerateRepoOption) GetLabels() bool`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *GenerateRepoOption) GetLabelsOk() (*bool, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *GenerateRepoOption) SetLabels(v bool)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *GenerateRepoOption) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetName

`func (o *GenerateRepoOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GenerateRepoOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GenerateRepoOption) SetName(v string)`

SetName sets Name field to given value.


### GetOwner

`func (o *GenerateRepoOption) GetOwner() string`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *GenerateRepoOption) GetOwnerOk() (*string, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *GenerateRepoOption) SetOwner(v string)`

SetOwner sets Owner field to given value.


### GetPrivate

`func (o *GenerateRepoOption) GetPrivate() bool`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *GenerateRepoOption) GetPrivateOk() (*bool, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *GenerateRepoOption) SetPrivate(v bool)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *GenerateRepoOption) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.

### GetProtectedBranch

`func (o *GenerateRepoOption) GetProtectedBranch() bool`

GetProtectedBranch returns the ProtectedBranch field if non-nil, zero value otherwise.

### GetProtectedBranchOk

`func (o *GenerateRepoOption) GetProtectedBranchOk() (*bool, bool)`

GetProtectedBranchOk returns a tuple with the ProtectedBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtectedBranch

`func (o *GenerateRepoOption) SetProtectedBranch(v bool)`

SetProtectedBranch sets ProtectedBranch field to given value.

### HasProtectedBranch

`func (o *GenerateRepoOption) HasProtectedBranch() bool`

HasProtectedBranch returns a boolean if a field has been set.

### GetTopics

`func (o *GenerateRepoOption) GetTopics() bool`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *GenerateRepoOption) GetTopicsOk() (*bool, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *GenerateRepoOption) SetTopics(v bool)`

SetTopics sets Topics field to given value.

### HasTopics

`func (o *GenerateRepoOption) HasTopics() bool`

HasTopics returns a boolean if a field has been set.

### GetWebhooks

`func (o *GenerateRepoOption) GetWebhooks() bool`

GetWebhooks returns the Webhooks field if non-nil, zero value otherwise.

### GetWebhooksOk

`func (o *GenerateRepoOption) GetWebhooksOk() (*bool, bool)`

GetWebhooksOk returns a tuple with the Webhooks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhooks

`func (o *GenerateRepoOption) SetWebhooks(v bool)`

SetWebhooks sets Webhooks field to given value.

### HasWebhooks

`func (o *GenerateRepoOption) HasWebhooks() bool`

HasWebhooks returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



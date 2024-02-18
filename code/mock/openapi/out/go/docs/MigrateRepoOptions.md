# MigrateRepoOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthPassword** | Pointer to **string** |  | [optional] 
**AuthToken** | Pointer to **string** |  | [optional] 
**AuthUsername** | Pointer to **string** |  | [optional] 
**CloneAddr** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Issues** | Pointer to **bool** |  | [optional] 
**Labels** | Pointer to **bool** |  | [optional] 
**Lfs** | Pointer to **bool** |  | [optional] 
**LfsEndpoint** | Pointer to **string** |  | [optional] 
**Milestones** | Pointer to **bool** |  | [optional] 
**Mirror** | Pointer to **bool** |  | [optional] 
**MirrorInterval** | Pointer to **string** |  | [optional] 
**Private** | Pointer to **bool** |  | [optional] 
**PullRequests** | Pointer to **bool** |  | [optional] 
**Releases** | Pointer to **bool** |  | [optional] 
**RepoName** | **string** |  | 
**RepoOwner** | Pointer to **string** | Name of User or Organisation who will own Repo after migration | [optional] 
**Service** | Pointer to **string** |  | [optional] 
**Uid** | Pointer to **int64** | deprecated (only for backwards compatibility) | [optional] 
**Wiki** | Pointer to **bool** |  | [optional] 

## Methods

### NewMigrateRepoOptions

`func NewMigrateRepoOptions(cloneAddr string, repoName string, ) *MigrateRepoOptions`

NewMigrateRepoOptions instantiates a new MigrateRepoOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMigrateRepoOptionsWithDefaults

`func NewMigrateRepoOptionsWithDefaults() *MigrateRepoOptions`

NewMigrateRepoOptionsWithDefaults instantiates a new MigrateRepoOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthPassword

`func (o *MigrateRepoOptions) GetAuthPassword() string`

GetAuthPassword returns the AuthPassword field if non-nil, zero value otherwise.

### GetAuthPasswordOk

`func (o *MigrateRepoOptions) GetAuthPasswordOk() (*string, bool)`

GetAuthPasswordOk returns a tuple with the AuthPassword field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthPassword

`func (o *MigrateRepoOptions) SetAuthPassword(v string)`

SetAuthPassword sets AuthPassword field to given value.

### HasAuthPassword

`func (o *MigrateRepoOptions) HasAuthPassword() bool`

HasAuthPassword returns a boolean if a field has been set.

### GetAuthToken

`func (o *MigrateRepoOptions) GetAuthToken() string`

GetAuthToken returns the AuthToken field if non-nil, zero value otherwise.

### GetAuthTokenOk

`func (o *MigrateRepoOptions) GetAuthTokenOk() (*string, bool)`

GetAuthTokenOk returns a tuple with the AuthToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthToken

`func (o *MigrateRepoOptions) SetAuthToken(v string)`

SetAuthToken sets AuthToken field to given value.

### HasAuthToken

`func (o *MigrateRepoOptions) HasAuthToken() bool`

HasAuthToken returns a boolean if a field has been set.

### GetAuthUsername

`func (o *MigrateRepoOptions) GetAuthUsername() string`

GetAuthUsername returns the AuthUsername field if non-nil, zero value otherwise.

### GetAuthUsernameOk

`func (o *MigrateRepoOptions) GetAuthUsernameOk() (*string, bool)`

GetAuthUsernameOk returns a tuple with the AuthUsername field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthUsername

`func (o *MigrateRepoOptions) SetAuthUsername(v string)`

SetAuthUsername sets AuthUsername field to given value.

### HasAuthUsername

`func (o *MigrateRepoOptions) HasAuthUsername() bool`

HasAuthUsername returns a boolean if a field has been set.

### GetCloneAddr

`func (o *MigrateRepoOptions) GetCloneAddr() string`

GetCloneAddr returns the CloneAddr field if non-nil, zero value otherwise.

### GetCloneAddrOk

`func (o *MigrateRepoOptions) GetCloneAddrOk() (*string, bool)`

GetCloneAddrOk returns a tuple with the CloneAddr field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloneAddr

`func (o *MigrateRepoOptions) SetCloneAddr(v string)`

SetCloneAddr sets CloneAddr field to given value.


### GetDescription

`func (o *MigrateRepoOptions) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *MigrateRepoOptions) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *MigrateRepoOptions) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *MigrateRepoOptions) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetIssues

`func (o *MigrateRepoOptions) GetIssues() bool`

GetIssues returns the Issues field if non-nil, zero value otherwise.

### GetIssuesOk

`func (o *MigrateRepoOptions) GetIssuesOk() (*bool, bool)`

GetIssuesOk returns a tuple with the Issues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssues

`func (o *MigrateRepoOptions) SetIssues(v bool)`

SetIssues sets Issues field to given value.

### HasIssues

`func (o *MigrateRepoOptions) HasIssues() bool`

HasIssues returns a boolean if a field has been set.

### GetLabels

`func (o *MigrateRepoOptions) GetLabels() bool`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *MigrateRepoOptions) GetLabelsOk() (*bool, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *MigrateRepoOptions) SetLabels(v bool)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *MigrateRepoOptions) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetLfs

`func (o *MigrateRepoOptions) GetLfs() bool`

GetLfs returns the Lfs field if non-nil, zero value otherwise.

### GetLfsOk

`func (o *MigrateRepoOptions) GetLfsOk() (*bool, bool)`

GetLfsOk returns a tuple with the Lfs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLfs

`func (o *MigrateRepoOptions) SetLfs(v bool)`

SetLfs sets Lfs field to given value.

### HasLfs

`func (o *MigrateRepoOptions) HasLfs() bool`

HasLfs returns a boolean if a field has been set.

### GetLfsEndpoint

`func (o *MigrateRepoOptions) GetLfsEndpoint() string`

GetLfsEndpoint returns the LfsEndpoint field if non-nil, zero value otherwise.

### GetLfsEndpointOk

`func (o *MigrateRepoOptions) GetLfsEndpointOk() (*string, bool)`

GetLfsEndpointOk returns a tuple with the LfsEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLfsEndpoint

`func (o *MigrateRepoOptions) SetLfsEndpoint(v string)`

SetLfsEndpoint sets LfsEndpoint field to given value.

### HasLfsEndpoint

`func (o *MigrateRepoOptions) HasLfsEndpoint() bool`

HasLfsEndpoint returns a boolean if a field has been set.

### GetMilestones

`func (o *MigrateRepoOptions) GetMilestones() bool`

GetMilestones returns the Milestones field if non-nil, zero value otherwise.

### GetMilestonesOk

`func (o *MigrateRepoOptions) GetMilestonesOk() (*bool, bool)`

GetMilestonesOk returns a tuple with the Milestones field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestones

`func (o *MigrateRepoOptions) SetMilestones(v bool)`

SetMilestones sets Milestones field to given value.

### HasMilestones

`func (o *MigrateRepoOptions) HasMilestones() bool`

HasMilestones returns a boolean if a field has been set.

### GetMirror

`func (o *MigrateRepoOptions) GetMirror() bool`

GetMirror returns the Mirror field if non-nil, zero value otherwise.

### GetMirrorOk

`func (o *MigrateRepoOptions) GetMirrorOk() (*bool, bool)`

GetMirrorOk returns a tuple with the Mirror field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMirror

`func (o *MigrateRepoOptions) SetMirror(v bool)`

SetMirror sets Mirror field to given value.

### HasMirror

`func (o *MigrateRepoOptions) HasMirror() bool`

HasMirror returns a boolean if a field has been set.

### GetMirrorInterval

`func (o *MigrateRepoOptions) GetMirrorInterval() string`

GetMirrorInterval returns the MirrorInterval field if non-nil, zero value otherwise.

### GetMirrorIntervalOk

`func (o *MigrateRepoOptions) GetMirrorIntervalOk() (*string, bool)`

GetMirrorIntervalOk returns a tuple with the MirrorInterval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMirrorInterval

`func (o *MigrateRepoOptions) SetMirrorInterval(v string)`

SetMirrorInterval sets MirrorInterval field to given value.

### HasMirrorInterval

`func (o *MigrateRepoOptions) HasMirrorInterval() bool`

HasMirrorInterval returns a boolean if a field has been set.

### GetPrivate

`func (o *MigrateRepoOptions) GetPrivate() bool`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *MigrateRepoOptions) GetPrivateOk() (*bool, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *MigrateRepoOptions) SetPrivate(v bool)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *MigrateRepoOptions) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.

### GetPullRequests

`func (o *MigrateRepoOptions) GetPullRequests() bool`

GetPullRequests returns the PullRequests field if non-nil, zero value otherwise.

### GetPullRequestsOk

`func (o *MigrateRepoOptions) GetPullRequestsOk() (*bool, bool)`

GetPullRequestsOk returns a tuple with the PullRequests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPullRequests

`func (o *MigrateRepoOptions) SetPullRequests(v bool)`

SetPullRequests sets PullRequests field to given value.

### HasPullRequests

`func (o *MigrateRepoOptions) HasPullRequests() bool`

HasPullRequests returns a boolean if a field has been set.

### GetReleases

`func (o *MigrateRepoOptions) GetReleases() bool`

GetReleases returns the Releases field if non-nil, zero value otherwise.

### GetReleasesOk

`func (o *MigrateRepoOptions) GetReleasesOk() (*bool, bool)`

GetReleasesOk returns a tuple with the Releases field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReleases

`func (o *MigrateRepoOptions) SetReleases(v bool)`

SetReleases sets Releases field to given value.

### HasReleases

`func (o *MigrateRepoOptions) HasReleases() bool`

HasReleases returns a boolean if a field has been set.

### GetRepoName

`func (o *MigrateRepoOptions) GetRepoName() string`

GetRepoName returns the RepoName field if non-nil, zero value otherwise.

### GetRepoNameOk

`func (o *MigrateRepoOptions) GetRepoNameOk() (*string, bool)`

GetRepoNameOk returns a tuple with the RepoName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoName

`func (o *MigrateRepoOptions) SetRepoName(v string)`

SetRepoName sets RepoName field to given value.


### GetRepoOwner

`func (o *MigrateRepoOptions) GetRepoOwner() string`

GetRepoOwner returns the RepoOwner field if non-nil, zero value otherwise.

### GetRepoOwnerOk

`func (o *MigrateRepoOptions) GetRepoOwnerOk() (*string, bool)`

GetRepoOwnerOk returns a tuple with the RepoOwner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoOwner

`func (o *MigrateRepoOptions) SetRepoOwner(v string)`

SetRepoOwner sets RepoOwner field to given value.

### HasRepoOwner

`func (o *MigrateRepoOptions) HasRepoOwner() bool`

HasRepoOwner returns a boolean if a field has been set.

### GetService

`func (o *MigrateRepoOptions) GetService() string`

GetService returns the Service field if non-nil, zero value otherwise.

### GetServiceOk

`func (o *MigrateRepoOptions) GetServiceOk() (*string, bool)`

GetServiceOk returns a tuple with the Service field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetService

`func (o *MigrateRepoOptions) SetService(v string)`

SetService sets Service field to given value.

### HasService

`func (o *MigrateRepoOptions) HasService() bool`

HasService returns a boolean if a field has been set.

### GetUid

`func (o *MigrateRepoOptions) GetUid() int64`

GetUid returns the Uid field if non-nil, zero value otherwise.

### GetUidOk

`func (o *MigrateRepoOptions) GetUidOk() (*int64, bool)`

GetUidOk returns a tuple with the Uid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUid

`func (o *MigrateRepoOptions) SetUid(v int64)`

SetUid sets Uid field to given value.

### HasUid

`func (o *MigrateRepoOptions) HasUid() bool`

HasUid returns a boolean if a field has been set.

### GetWiki

`func (o *MigrateRepoOptions) GetWiki() bool`

GetWiki returns the Wiki field if non-nil, zero value otherwise.

### GetWikiOk

`func (o *MigrateRepoOptions) GetWikiOk() (*bool, bool)`

GetWikiOk returns a tuple with the Wiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWiki

`func (o *MigrateRepoOptions) SetWiki(v bool)`

SetWiki sets Wiki field to given value.

### HasWiki

`func (o *MigrateRepoOptions) HasWiki() bool`

HasWiki returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



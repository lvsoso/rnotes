# Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AllowFastForwardOnlyMerge** | Pointer to **bool** |  | [optional] 
**AllowMergeCommits** | Pointer to **bool** |  | [optional] 
**AllowRebase** | Pointer to **bool** |  | [optional] 
**AllowRebaseExplicit** | Pointer to **bool** |  | [optional] 
**AllowRebaseUpdate** | Pointer to **bool** |  | [optional] 
**AllowSquashMerge** | Pointer to **bool** |  | [optional] 
**Archived** | Pointer to **bool** |  | [optional] 
**ArchivedAt** | Pointer to **time.Time** |  | [optional] 
**AvatarUrl** | Pointer to **string** |  | [optional] 
**CloneUrl** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**DefaultAllowMaintainerEdit** | Pointer to **bool** |  | [optional] 
**DefaultBranch** | Pointer to **string** |  | [optional] 
**DefaultDeleteBranchAfterMerge** | Pointer to **bool** |  | [optional] 
**DefaultMergeStyle** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Empty** | Pointer to **bool** |  | [optional] 
**ExternalTracker** | Pointer to [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**ExternalWiki** | Pointer to [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**Fork** | Pointer to **bool** |  | [optional] 
**ForksCount** | Pointer to **int64** |  | [optional] 
**FullName** | Pointer to **string** |  | [optional] 
**HasActions** | Pointer to **bool** |  | [optional] 
**HasIssues** | Pointer to **bool** |  | [optional] 
**HasPackages** | Pointer to **bool** |  | [optional] 
**HasProjects** | Pointer to **bool** |  | [optional] 
**HasPullRequests** | Pointer to **bool** |  | [optional] 
**HasReleases** | Pointer to **bool** |  | [optional] 
**HasWiki** | Pointer to **bool** |  | [optional] 
**HtmlUrl** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**IgnoreWhitespaceConflicts** | Pointer to **bool** |  | [optional] 
**Internal** | Pointer to **bool** |  | [optional] 
**InternalTracker** | Pointer to [**InternalTracker**](InternalTracker.md) |  | [optional] 
**Language** | Pointer to **string** |  | [optional] 
**LanguagesUrl** | Pointer to **string** |  | [optional] 
**Link** | Pointer to **string** |  | [optional] 
**Mirror** | Pointer to **bool** |  | [optional] 
**MirrorInterval** | Pointer to **string** |  | [optional] 
**MirrorUpdated** | Pointer to **time.Time** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**ObjectFormatName** | Pointer to **string** | ObjectFormatName of the underlying git repository | [optional] 
**OpenIssuesCount** | Pointer to **int64** |  | [optional] 
**OpenPrCounter** | Pointer to **int64** |  | [optional] 
**OriginalUrl** | Pointer to **string** |  | [optional] 
**Owner** | Pointer to [**User**](User.md) |  | [optional] 
**Parent** | Pointer to [**Repository**](Repository.md) |  | [optional] 
**Permissions** | Pointer to [**Permission**](Permission.md) |  | [optional] 
**Private** | Pointer to **bool** |  | [optional] 
**ReleaseCounter** | Pointer to **int64** |  | [optional] 
**RepoTransfer** | Pointer to [**RepoTransfer**](RepoTransfer.md) |  | [optional] 
**Size** | Pointer to **int64** |  | [optional] 
**SshUrl** | Pointer to **string** |  | [optional] 
**StarsCount** | Pointer to **int64** |  | [optional] 
**Template** | Pointer to **bool** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**WatchersCount** | Pointer to **int64** |  | [optional] 
**Website** | Pointer to **string** |  | [optional] 

## Methods

### NewRepository

`func NewRepository() *Repository`

NewRepository instantiates a new Repository object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepositoryWithDefaults

`func NewRepositoryWithDefaults() *Repository`

NewRepositoryWithDefaults instantiates a new Repository object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAllowFastForwardOnlyMerge

`func (o *Repository) GetAllowFastForwardOnlyMerge() bool`

GetAllowFastForwardOnlyMerge returns the AllowFastForwardOnlyMerge field if non-nil, zero value otherwise.

### GetAllowFastForwardOnlyMergeOk

`func (o *Repository) GetAllowFastForwardOnlyMergeOk() (*bool, bool)`

GetAllowFastForwardOnlyMergeOk returns a tuple with the AllowFastForwardOnlyMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowFastForwardOnlyMerge

`func (o *Repository) SetAllowFastForwardOnlyMerge(v bool)`

SetAllowFastForwardOnlyMerge sets AllowFastForwardOnlyMerge field to given value.

### HasAllowFastForwardOnlyMerge

`func (o *Repository) HasAllowFastForwardOnlyMerge() bool`

HasAllowFastForwardOnlyMerge returns a boolean if a field has been set.

### GetAllowMergeCommits

`func (o *Repository) GetAllowMergeCommits() bool`

GetAllowMergeCommits returns the AllowMergeCommits field if non-nil, zero value otherwise.

### GetAllowMergeCommitsOk

`func (o *Repository) GetAllowMergeCommitsOk() (*bool, bool)`

GetAllowMergeCommitsOk returns a tuple with the AllowMergeCommits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowMergeCommits

`func (o *Repository) SetAllowMergeCommits(v bool)`

SetAllowMergeCommits sets AllowMergeCommits field to given value.

### HasAllowMergeCommits

`func (o *Repository) HasAllowMergeCommits() bool`

HasAllowMergeCommits returns a boolean if a field has been set.

### GetAllowRebase

`func (o *Repository) GetAllowRebase() bool`

GetAllowRebase returns the AllowRebase field if non-nil, zero value otherwise.

### GetAllowRebaseOk

`func (o *Repository) GetAllowRebaseOk() (*bool, bool)`

GetAllowRebaseOk returns a tuple with the AllowRebase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowRebase

`func (o *Repository) SetAllowRebase(v bool)`

SetAllowRebase sets AllowRebase field to given value.

### HasAllowRebase

`func (o *Repository) HasAllowRebase() bool`

HasAllowRebase returns a boolean if a field has been set.

### GetAllowRebaseExplicit

`func (o *Repository) GetAllowRebaseExplicit() bool`

GetAllowRebaseExplicit returns the AllowRebaseExplicit field if non-nil, zero value otherwise.

### GetAllowRebaseExplicitOk

`func (o *Repository) GetAllowRebaseExplicitOk() (*bool, bool)`

GetAllowRebaseExplicitOk returns a tuple with the AllowRebaseExplicit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowRebaseExplicit

`func (o *Repository) SetAllowRebaseExplicit(v bool)`

SetAllowRebaseExplicit sets AllowRebaseExplicit field to given value.

### HasAllowRebaseExplicit

`func (o *Repository) HasAllowRebaseExplicit() bool`

HasAllowRebaseExplicit returns a boolean if a field has been set.

### GetAllowRebaseUpdate

`func (o *Repository) GetAllowRebaseUpdate() bool`

GetAllowRebaseUpdate returns the AllowRebaseUpdate field if non-nil, zero value otherwise.

### GetAllowRebaseUpdateOk

`func (o *Repository) GetAllowRebaseUpdateOk() (*bool, bool)`

GetAllowRebaseUpdateOk returns a tuple with the AllowRebaseUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowRebaseUpdate

`func (o *Repository) SetAllowRebaseUpdate(v bool)`

SetAllowRebaseUpdate sets AllowRebaseUpdate field to given value.

### HasAllowRebaseUpdate

`func (o *Repository) HasAllowRebaseUpdate() bool`

HasAllowRebaseUpdate returns a boolean if a field has been set.

### GetAllowSquashMerge

`func (o *Repository) GetAllowSquashMerge() bool`

GetAllowSquashMerge returns the AllowSquashMerge field if non-nil, zero value otherwise.

### GetAllowSquashMergeOk

`func (o *Repository) GetAllowSquashMergeOk() (*bool, bool)`

GetAllowSquashMergeOk returns a tuple with the AllowSquashMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowSquashMerge

`func (o *Repository) SetAllowSquashMerge(v bool)`

SetAllowSquashMerge sets AllowSquashMerge field to given value.

### HasAllowSquashMerge

`func (o *Repository) HasAllowSquashMerge() bool`

HasAllowSquashMerge returns a boolean if a field has been set.

### GetArchived

`func (o *Repository) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *Repository) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *Repository) SetArchived(v bool)`

SetArchived sets Archived field to given value.

### HasArchived

`func (o *Repository) HasArchived() bool`

HasArchived returns a boolean if a field has been set.

### GetArchivedAt

`func (o *Repository) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *Repository) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *Repository) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.

### HasArchivedAt

`func (o *Repository) HasArchivedAt() bool`

HasArchivedAt returns a boolean if a field has been set.

### GetAvatarUrl

`func (o *Repository) GetAvatarUrl() string`

GetAvatarUrl returns the AvatarUrl field if non-nil, zero value otherwise.

### GetAvatarUrlOk

`func (o *Repository) GetAvatarUrlOk() (*string, bool)`

GetAvatarUrlOk returns a tuple with the AvatarUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatarUrl

`func (o *Repository) SetAvatarUrl(v string)`

SetAvatarUrl sets AvatarUrl field to given value.

### HasAvatarUrl

`func (o *Repository) HasAvatarUrl() bool`

HasAvatarUrl returns a boolean if a field has been set.

### GetCloneUrl

`func (o *Repository) GetCloneUrl() string`

GetCloneUrl returns the CloneUrl field if non-nil, zero value otherwise.

### GetCloneUrlOk

`func (o *Repository) GetCloneUrlOk() (*string, bool)`

GetCloneUrlOk returns a tuple with the CloneUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloneUrl

`func (o *Repository) SetCloneUrl(v string)`

SetCloneUrl sets CloneUrl field to given value.

### HasCloneUrl

`func (o *Repository) HasCloneUrl() bool`

HasCloneUrl returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Repository) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Repository) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Repository) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Repository) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetDefaultAllowMaintainerEdit

`func (o *Repository) GetDefaultAllowMaintainerEdit() bool`

GetDefaultAllowMaintainerEdit returns the DefaultAllowMaintainerEdit field if non-nil, zero value otherwise.

### GetDefaultAllowMaintainerEditOk

`func (o *Repository) GetDefaultAllowMaintainerEditOk() (*bool, bool)`

GetDefaultAllowMaintainerEditOk returns a tuple with the DefaultAllowMaintainerEdit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultAllowMaintainerEdit

`func (o *Repository) SetDefaultAllowMaintainerEdit(v bool)`

SetDefaultAllowMaintainerEdit sets DefaultAllowMaintainerEdit field to given value.

### HasDefaultAllowMaintainerEdit

`func (o *Repository) HasDefaultAllowMaintainerEdit() bool`

HasDefaultAllowMaintainerEdit returns a boolean if a field has been set.

### GetDefaultBranch

`func (o *Repository) GetDefaultBranch() string`

GetDefaultBranch returns the DefaultBranch field if non-nil, zero value otherwise.

### GetDefaultBranchOk

`func (o *Repository) GetDefaultBranchOk() (*string, bool)`

GetDefaultBranchOk returns a tuple with the DefaultBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultBranch

`func (o *Repository) SetDefaultBranch(v string)`

SetDefaultBranch sets DefaultBranch field to given value.

### HasDefaultBranch

`func (o *Repository) HasDefaultBranch() bool`

HasDefaultBranch returns a boolean if a field has been set.

### GetDefaultDeleteBranchAfterMerge

`func (o *Repository) GetDefaultDeleteBranchAfterMerge() bool`

GetDefaultDeleteBranchAfterMerge returns the DefaultDeleteBranchAfterMerge field if non-nil, zero value otherwise.

### GetDefaultDeleteBranchAfterMergeOk

`func (o *Repository) GetDefaultDeleteBranchAfterMergeOk() (*bool, bool)`

GetDefaultDeleteBranchAfterMergeOk returns a tuple with the DefaultDeleteBranchAfterMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultDeleteBranchAfterMerge

`func (o *Repository) SetDefaultDeleteBranchAfterMerge(v bool)`

SetDefaultDeleteBranchAfterMerge sets DefaultDeleteBranchAfterMerge field to given value.

### HasDefaultDeleteBranchAfterMerge

`func (o *Repository) HasDefaultDeleteBranchAfterMerge() bool`

HasDefaultDeleteBranchAfterMerge returns a boolean if a field has been set.

### GetDefaultMergeStyle

`func (o *Repository) GetDefaultMergeStyle() string`

GetDefaultMergeStyle returns the DefaultMergeStyle field if non-nil, zero value otherwise.

### GetDefaultMergeStyleOk

`func (o *Repository) GetDefaultMergeStyleOk() (*string, bool)`

GetDefaultMergeStyleOk returns a tuple with the DefaultMergeStyle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultMergeStyle

`func (o *Repository) SetDefaultMergeStyle(v string)`

SetDefaultMergeStyle sets DefaultMergeStyle field to given value.

### HasDefaultMergeStyle

`func (o *Repository) HasDefaultMergeStyle() bool`

HasDefaultMergeStyle returns a boolean if a field has been set.

### GetDescription

`func (o *Repository) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Repository) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Repository) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Repository) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEmpty

`func (o *Repository) GetEmpty() bool`

GetEmpty returns the Empty field if non-nil, zero value otherwise.

### GetEmptyOk

`func (o *Repository) GetEmptyOk() (*bool, bool)`

GetEmptyOk returns a tuple with the Empty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmpty

`func (o *Repository) SetEmpty(v bool)`

SetEmpty sets Empty field to given value.

### HasEmpty

`func (o *Repository) HasEmpty() bool`

HasEmpty returns a boolean if a field has been set.

### GetExternalTracker

`func (o *Repository) GetExternalTracker() ExternalTracker`

GetExternalTracker returns the ExternalTracker field if non-nil, zero value otherwise.

### GetExternalTrackerOk

`func (o *Repository) GetExternalTrackerOk() (*ExternalTracker, bool)`

GetExternalTrackerOk returns a tuple with the ExternalTracker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalTracker

`func (o *Repository) SetExternalTracker(v ExternalTracker)`

SetExternalTracker sets ExternalTracker field to given value.

### HasExternalTracker

`func (o *Repository) HasExternalTracker() bool`

HasExternalTracker returns a boolean if a field has been set.

### GetExternalWiki

`func (o *Repository) GetExternalWiki() ExternalWiki`

GetExternalWiki returns the ExternalWiki field if non-nil, zero value otherwise.

### GetExternalWikiOk

`func (o *Repository) GetExternalWikiOk() (*ExternalWiki, bool)`

GetExternalWikiOk returns a tuple with the ExternalWiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalWiki

`func (o *Repository) SetExternalWiki(v ExternalWiki)`

SetExternalWiki sets ExternalWiki field to given value.

### HasExternalWiki

`func (o *Repository) HasExternalWiki() bool`

HasExternalWiki returns a boolean if a field has been set.

### GetFork

`func (o *Repository) GetFork() bool`

GetFork returns the Fork field if non-nil, zero value otherwise.

### GetForkOk

`func (o *Repository) GetForkOk() (*bool, bool)`

GetForkOk returns a tuple with the Fork field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFork

`func (o *Repository) SetFork(v bool)`

SetFork sets Fork field to given value.

### HasFork

`func (o *Repository) HasFork() bool`

HasFork returns a boolean if a field has been set.

### GetForksCount

`func (o *Repository) GetForksCount() int64`

GetForksCount returns the ForksCount field if non-nil, zero value otherwise.

### GetForksCountOk

`func (o *Repository) GetForksCountOk() (*int64, bool)`

GetForksCountOk returns a tuple with the ForksCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetForksCount

`func (o *Repository) SetForksCount(v int64)`

SetForksCount sets ForksCount field to given value.

### HasForksCount

`func (o *Repository) HasForksCount() bool`

HasForksCount returns a boolean if a field has been set.

### GetFullName

`func (o *Repository) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *Repository) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *Repository) SetFullName(v string)`

SetFullName sets FullName field to given value.

### HasFullName

`func (o *Repository) HasFullName() bool`

HasFullName returns a boolean if a field has been set.

### GetHasActions

`func (o *Repository) GetHasActions() bool`

GetHasActions returns the HasActions field if non-nil, zero value otherwise.

### GetHasActionsOk

`func (o *Repository) GetHasActionsOk() (*bool, bool)`

GetHasActionsOk returns a tuple with the HasActions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasActions

`func (o *Repository) SetHasActions(v bool)`

SetHasActions sets HasActions field to given value.

### HasHasActions

`func (o *Repository) HasHasActions() bool`

HasHasActions returns a boolean if a field has been set.

### GetHasIssues

`func (o *Repository) GetHasIssues() bool`

GetHasIssues returns the HasIssues field if non-nil, zero value otherwise.

### GetHasIssuesOk

`func (o *Repository) GetHasIssuesOk() (*bool, bool)`

GetHasIssuesOk returns a tuple with the HasIssues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasIssues

`func (o *Repository) SetHasIssues(v bool)`

SetHasIssues sets HasIssues field to given value.

### HasHasIssues

`func (o *Repository) HasHasIssues() bool`

HasHasIssues returns a boolean if a field has been set.

### GetHasPackages

`func (o *Repository) GetHasPackages() bool`

GetHasPackages returns the HasPackages field if non-nil, zero value otherwise.

### GetHasPackagesOk

`func (o *Repository) GetHasPackagesOk() (*bool, bool)`

GetHasPackagesOk returns a tuple with the HasPackages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPackages

`func (o *Repository) SetHasPackages(v bool)`

SetHasPackages sets HasPackages field to given value.

### HasHasPackages

`func (o *Repository) HasHasPackages() bool`

HasHasPackages returns a boolean if a field has been set.

### GetHasProjects

`func (o *Repository) GetHasProjects() bool`

GetHasProjects returns the HasProjects field if non-nil, zero value otherwise.

### GetHasProjectsOk

`func (o *Repository) GetHasProjectsOk() (*bool, bool)`

GetHasProjectsOk returns a tuple with the HasProjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasProjects

`func (o *Repository) SetHasProjects(v bool)`

SetHasProjects sets HasProjects field to given value.

### HasHasProjects

`func (o *Repository) HasHasProjects() bool`

HasHasProjects returns a boolean if a field has been set.

### GetHasPullRequests

`func (o *Repository) GetHasPullRequests() bool`

GetHasPullRequests returns the HasPullRequests field if non-nil, zero value otherwise.

### GetHasPullRequestsOk

`func (o *Repository) GetHasPullRequestsOk() (*bool, bool)`

GetHasPullRequestsOk returns a tuple with the HasPullRequests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPullRequests

`func (o *Repository) SetHasPullRequests(v bool)`

SetHasPullRequests sets HasPullRequests field to given value.

### HasHasPullRequests

`func (o *Repository) HasHasPullRequests() bool`

HasHasPullRequests returns a boolean if a field has been set.

### GetHasReleases

`func (o *Repository) GetHasReleases() bool`

GetHasReleases returns the HasReleases field if non-nil, zero value otherwise.

### GetHasReleasesOk

`func (o *Repository) GetHasReleasesOk() (*bool, bool)`

GetHasReleasesOk returns a tuple with the HasReleases field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasReleases

`func (o *Repository) SetHasReleases(v bool)`

SetHasReleases sets HasReleases field to given value.

### HasHasReleases

`func (o *Repository) HasHasReleases() bool`

HasHasReleases returns a boolean if a field has been set.

### GetHasWiki

`func (o *Repository) GetHasWiki() bool`

GetHasWiki returns the HasWiki field if non-nil, zero value otherwise.

### GetHasWikiOk

`func (o *Repository) GetHasWikiOk() (*bool, bool)`

GetHasWikiOk returns a tuple with the HasWiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasWiki

`func (o *Repository) SetHasWiki(v bool)`

SetHasWiki sets HasWiki field to given value.

### HasHasWiki

`func (o *Repository) HasHasWiki() bool`

HasHasWiki returns a boolean if a field has been set.

### GetHtmlUrl

`func (o *Repository) GetHtmlUrl() string`

GetHtmlUrl returns the HtmlUrl field if non-nil, zero value otherwise.

### GetHtmlUrlOk

`func (o *Repository) GetHtmlUrlOk() (*string, bool)`

GetHtmlUrlOk returns a tuple with the HtmlUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtmlUrl

`func (o *Repository) SetHtmlUrl(v string)`

SetHtmlUrl sets HtmlUrl field to given value.

### HasHtmlUrl

`func (o *Repository) HasHtmlUrl() bool`

HasHtmlUrl returns a boolean if a field has been set.

### GetId

`func (o *Repository) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Repository) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Repository) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Repository) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIgnoreWhitespaceConflicts

`func (o *Repository) GetIgnoreWhitespaceConflicts() bool`

GetIgnoreWhitespaceConflicts returns the IgnoreWhitespaceConflicts field if non-nil, zero value otherwise.

### GetIgnoreWhitespaceConflictsOk

`func (o *Repository) GetIgnoreWhitespaceConflictsOk() (*bool, bool)`

GetIgnoreWhitespaceConflictsOk returns a tuple with the IgnoreWhitespaceConflicts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIgnoreWhitespaceConflicts

`func (o *Repository) SetIgnoreWhitespaceConflicts(v bool)`

SetIgnoreWhitespaceConflicts sets IgnoreWhitespaceConflicts field to given value.

### HasIgnoreWhitespaceConflicts

`func (o *Repository) HasIgnoreWhitespaceConflicts() bool`

HasIgnoreWhitespaceConflicts returns a boolean if a field has been set.

### GetInternal

`func (o *Repository) GetInternal() bool`

GetInternal returns the Internal field if non-nil, zero value otherwise.

### GetInternalOk

`func (o *Repository) GetInternalOk() (*bool, bool)`

GetInternalOk returns a tuple with the Internal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternal

`func (o *Repository) SetInternal(v bool)`

SetInternal sets Internal field to given value.

### HasInternal

`func (o *Repository) HasInternal() bool`

HasInternal returns a boolean if a field has been set.

### GetInternalTracker

`func (o *Repository) GetInternalTracker() InternalTracker`

GetInternalTracker returns the InternalTracker field if non-nil, zero value otherwise.

### GetInternalTrackerOk

`func (o *Repository) GetInternalTrackerOk() (*InternalTracker, bool)`

GetInternalTrackerOk returns a tuple with the InternalTracker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternalTracker

`func (o *Repository) SetInternalTracker(v InternalTracker)`

SetInternalTracker sets InternalTracker field to given value.

### HasInternalTracker

`func (o *Repository) HasInternalTracker() bool`

HasInternalTracker returns a boolean if a field has been set.

### GetLanguage

`func (o *Repository) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *Repository) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *Repository) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *Repository) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### GetLanguagesUrl

`func (o *Repository) GetLanguagesUrl() string`

GetLanguagesUrl returns the LanguagesUrl field if non-nil, zero value otherwise.

### GetLanguagesUrlOk

`func (o *Repository) GetLanguagesUrlOk() (*string, bool)`

GetLanguagesUrlOk returns a tuple with the LanguagesUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguagesUrl

`func (o *Repository) SetLanguagesUrl(v string)`

SetLanguagesUrl sets LanguagesUrl field to given value.

### HasLanguagesUrl

`func (o *Repository) HasLanguagesUrl() bool`

HasLanguagesUrl returns a boolean if a field has been set.

### GetLink

`func (o *Repository) GetLink() string`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *Repository) GetLinkOk() (*string, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *Repository) SetLink(v string)`

SetLink sets Link field to given value.

### HasLink

`func (o *Repository) HasLink() bool`

HasLink returns a boolean if a field has been set.

### GetMirror

`func (o *Repository) GetMirror() bool`

GetMirror returns the Mirror field if non-nil, zero value otherwise.

### GetMirrorOk

`func (o *Repository) GetMirrorOk() (*bool, bool)`

GetMirrorOk returns a tuple with the Mirror field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMirror

`func (o *Repository) SetMirror(v bool)`

SetMirror sets Mirror field to given value.

### HasMirror

`func (o *Repository) HasMirror() bool`

HasMirror returns a boolean if a field has been set.

### GetMirrorInterval

`func (o *Repository) GetMirrorInterval() string`

GetMirrorInterval returns the MirrorInterval field if non-nil, zero value otherwise.

### GetMirrorIntervalOk

`func (o *Repository) GetMirrorIntervalOk() (*string, bool)`

GetMirrorIntervalOk returns a tuple with the MirrorInterval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMirrorInterval

`func (o *Repository) SetMirrorInterval(v string)`

SetMirrorInterval sets MirrorInterval field to given value.

### HasMirrorInterval

`func (o *Repository) HasMirrorInterval() bool`

HasMirrorInterval returns a boolean if a field has been set.

### GetMirrorUpdated

`func (o *Repository) GetMirrorUpdated() time.Time`

GetMirrorUpdated returns the MirrorUpdated field if non-nil, zero value otherwise.

### GetMirrorUpdatedOk

`func (o *Repository) GetMirrorUpdatedOk() (*time.Time, bool)`

GetMirrorUpdatedOk returns a tuple with the MirrorUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMirrorUpdated

`func (o *Repository) SetMirrorUpdated(v time.Time)`

SetMirrorUpdated sets MirrorUpdated field to given value.

### HasMirrorUpdated

`func (o *Repository) HasMirrorUpdated() bool`

HasMirrorUpdated returns a boolean if a field has been set.

### GetName

`func (o *Repository) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Repository) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Repository) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Repository) HasName() bool`

HasName returns a boolean if a field has been set.

### GetObjectFormatName

`func (o *Repository) GetObjectFormatName() string`

GetObjectFormatName returns the ObjectFormatName field if non-nil, zero value otherwise.

### GetObjectFormatNameOk

`func (o *Repository) GetObjectFormatNameOk() (*string, bool)`

GetObjectFormatNameOk returns a tuple with the ObjectFormatName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectFormatName

`func (o *Repository) SetObjectFormatName(v string)`

SetObjectFormatName sets ObjectFormatName field to given value.

### HasObjectFormatName

`func (o *Repository) HasObjectFormatName() bool`

HasObjectFormatName returns a boolean if a field has been set.

### GetOpenIssuesCount

`func (o *Repository) GetOpenIssuesCount() int64`

GetOpenIssuesCount returns the OpenIssuesCount field if non-nil, zero value otherwise.

### GetOpenIssuesCountOk

`func (o *Repository) GetOpenIssuesCountOk() (*int64, bool)`

GetOpenIssuesCountOk returns a tuple with the OpenIssuesCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenIssuesCount

`func (o *Repository) SetOpenIssuesCount(v int64)`

SetOpenIssuesCount sets OpenIssuesCount field to given value.

### HasOpenIssuesCount

`func (o *Repository) HasOpenIssuesCount() bool`

HasOpenIssuesCount returns a boolean if a field has been set.

### GetOpenPrCounter

`func (o *Repository) GetOpenPrCounter() int64`

GetOpenPrCounter returns the OpenPrCounter field if non-nil, zero value otherwise.

### GetOpenPrCounterOk

`func (o *Repository) GetOpenPrCounterOk() (*int64, bool)`

GetOpenPrCounterOk returns a tuple with the OpenPrCounter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenPrCounter

`func (o *Repository) SetOpenPrCounter(v int64)`

SetOpenPrCounter sets OpenPrCounter field to given value.

### HasOpenPrCounter

`func (o *Repository) HasOpenPrCounter() bool`

HasOpenPrCounter returns a boolean if a field has been set.

### GetOriginalUrl

`func (o *Repository) GetOriginalUrl() string`

GetOriginalUrl returns the OriginalUrl field if non-nil, zero value otherwise.

### GetOriginalUrlOk

`func (o *Repository) GetOriginalUrlOk() (*string, bool)`

GetOriginalUrlOk returns a tuple with the OriginalUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalUrl

`func (o *Repository) SetOriginalUrl(v string)`

SetOriginalUrl sets OriginalUrl field to given value.

### HasOriginalUrl

`func (o *Repository) HasOriginalUrl() bool`

HasOriginalUrl returns a boolean if a field has been set.

### GetOwner

`func (o *Repository) GetOwner() User`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *Repository) GetOwnerOk() (*User, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *Repository) SetOwner(v User)`

SetOwner sets Owner field to given value.

### HasOwner

`func (o *Repository) HasOwner() bool`

HasOwner returns a boolean if a field has been set.

### GetParent

`func (o *Repository) GetParent() Repository`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *Repository) GetParentOk() (*Repository, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *Repository) SetParent(v Repository)`

SetParent sets Parent field to given value.

### HasParent

`func (o *Repository) HasParent() bool`

HasParent returns a boolean if a field has been set.

### GetPermissions

`func (o *Repository) GetPermissions() Permission`

GetPermissions returns the Permissions field if non-nil, zero value otherwise.

### GetPermissionsOk

`func (o *Repository) GetPermissionsOk() (*Permission, bool)`

GetPermissionsOk returns a tuple with the Permissions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermissions

`func (o *Repository) SetPermissions(v Permission)`

SetPermissions sets Permissions field to given value.

### HasPermissions

`func (o *Repository) HasPermissions() bool`

HasPermissions returns a boolean if a field has been set.

### GetPrivate

`func (o *Repository) GetPrivate() bool`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *Repository) GetPrivateOk() (*bool, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *Repository) SetPrivate(v bool)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *Repository) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.

### GetReleaseCounter

`func (o *Repository) GetReleaseCounter() int64`

GetReleaseCounter returns the ReleaseCounter field if non-nil, zero value otherwise.

### GetReleaseCounterOk

`func (o *Repository) GetReleaseCounterOk() (*int64, bool)`

GetReleaseCounterOk returns a tuple with the ReleaseCounter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReleaseCounter

`func (o *Repository) SetReleaseCounter(v int64)`

SetReleaseCounter sets ReleaseCounter field to given value.

### HasReleaseCounter

`func (o *Repository) HasReleaseCounter() bool`

HasReleaseCounter returns a boolean if a field has been set.

### GetRepoTransfer

`func (o *Repository) GetRepoTransfer() RepoTransfer`

GetRepoTransfer returns the RepoTransfer field if non-nil, zero value otherwise.

### GetRepoTransferOk

`func (o *Repository) GetRepoTransferOk() (*RepoTransfer, bool)`

GetRepoTransferOk returns a tuple with the RepoTransfer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoTransfer

`func (o *Repository) SetRepoTransfer(v RepoTransfer)`

SetRepoTransfer sets RepoTransfer field to given value.

### HasRepoTransfer

`func (o *Repository) HasRepoTransfer() bool`

HasRepoTransfer returns a boolean if a field has been set.

### GetSize

`func (o *Repository) GetSize() int64`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *Repository) GetSizeOk() (*int64, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *Repository) SetSize(v int64)`

SetSize sets Size field to given value.

### HasSize

`func (o *Repository) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetSshUrl

`func (o *Repository) GetSshUrl() string`

GetSshUrl returns the SshUrl field if non-nil, zero value otherwise.

### GetSshUrlOk

`func (o *Repository) GetSshUrlOk() (*string, bool)`

GetSshUrlOk returns a tuple with the SshUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSshUrl

`func (o *Repository) SetSshUrl(v string)`

SetSshUrl sets SshUrl field to given value.

### HasSshUrl

`func (o *Repository) HasSshUrl() bool`

HasSshUrl returns a boolean if a field has been set.

### GetStarsCount

`func (o *Repository) GetStarsCount() int64`

GetStarsCount returns the StarsCount field if non-nil, zero value otherwise.

### GetStarsCountOk

`func (o *Repository) GetStarsCountOk() (*int64, bool)`

GetStarsCountOk returns a tuple with the StarsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStarsCount

`func (o *Repository) SetStarsCount(v int64)`

SetStarsCount sets StarsCount field to given value.

### HasStarsCount

`func (o *Repository) HasStarsCount() bool`

HasStarsCount returns a boolean if a field has been set.

### GetTemplate

`func (o *Repository) GetTemplate() bool`

GetTemplate returns the Template field if non-nil, zero value otherwise.

### GetTemplateOk

`func (o *Repository) GetTemplateOk() (*bool, bool)`

GetTemplateOk returns a tuple with the Template field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemplate

`func (o *Repository) SetTemplate(v bool)`

SetTemplate sets Template field to given value.

### HasTemplate

`func (o *Repository) HasTemplate() bool`

HasTemplate returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Repository) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Repository) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Repository) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Repository) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUrl

`func (o *Repository) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Repository) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Repository) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *Repository) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetWatchersCount

`func (o *Repository) GetWatchersCount() int64`

GetWatchersCount returns the WatchersCount field if non-nil, zero value otherwise.

### GetWatchersCountOk

`func (o *Repository) GetWatchersCountOk() (*int64, bool)`

GetWatchersCountOk returns a tuple with the WatchersCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWatchersCount

`func (o *Repository) SetWatchersCount(v int64)`

SetWatchersCount sets WatchersCount field to given value.

### HasWatchersCount

`func (o *Repository) HasWatchersCount() bool`

HasWatchersCount returns a boolean if a field has been set.

### GetWebsite

`func (o *Repository) GetWebsite() string`

GetWebsite returns the Website field if non-nil, zero value otherwise.

### GetWebsiteOk

`func (o *Repository) GetWebsiteOk() (*string, bool)`

GetWebsiteOk returns a tuple with the Website field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsite

`func (o *Repository) SetWebsite(v string)`

SetWebsite sets Website field to given value.

### HasWebsite

`func (o *Repository) HasWebsite() bool`

HasWebsite returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



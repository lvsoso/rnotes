# EditRepoOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AllowFastForwardOnlyMerge** | Pointer to **bool** | either &#x60;true&#x60; to allow fast-forward-only merging pull requests, or &#x60;false&#x60; to prevent fast-forward-only merging. | [optional] 
**AllowManualMerge** | Pointer to **bool** | either &#x60;true&#x60; to allow mark pr as merged manually, or &#x60;false&#x60; to prevent it. | [optional] 
**AllowMergeCommits** | Pointer to **bool** | either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. | [optional] 
**AllowRebase** | Pointer to **bool** | either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. | [optional] 
**AllowRebaseExplicit** | Pointer to **bool** | either &#x60;true&#x60; to allow rebase with explicit merge commits (--no-ff), or &#x60;false&#x60; to prevent rebase with explicit merge commits. | [optional] 
**AllowRebaseUpdate** | Pointer to **bool** | either &#x60;true&#x60; to allow updating pull request branch by rebase, or &#x60;false&#x60; to prevent it. | [optional] 
**AllowSquashMerge** | Pointer to **bool** | either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. | [optional] 
**Archived** | Pointer to **bool** | set to &#x60;true&#x60; to archive this repository. | [optional] 
**AutodetectManualMerge** | Pointer to **bool** | either &#x60;true&#x60; to enable AutodetectManualMerge, or &#x60;false&#x60; to prevent it. Note: In some special cases, misjudgments can occur. | [optional] 
**DefaultAllowMaintainerEdit** | Pointer to **bool** | set to &#x60;true&#x60; to allow edits from maintainers by default | [optional] 
**DefaultBranch** | Pointer to **string** | sets the default branch for this repository. | [optional] 
**DefaultDeleteBranchAfterMerge** | Pointer to **bool** | set to &#x60;true&#x60; to delete pr branch after merge by default | [optional] 
**DefaultMergeStyle** | Pointer to **string** | set to a merge style to be used by this repository: \&quot;merge\&quot;, \&quot;rebase\&quot;, \&quot;rebase-merge\&quot;, \&quot;squash\&quot;, or \&quot;fast-forward-only\&quot;. | [optional] 
**Description** | Pointer to **string** | a short description of the repository. | [optional] 
**EnablePrune** | Pointer to **bool** | enable prune - remove obsolete remote-tracking references | [optional] 
**ExternalTracker** | Pointer to [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**ExternalWiki** | Pointer to [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**HasActions** | Pointer to **bool** | either &#x60;true&#x60; to enable actions unit, or &#x60;false&#x60; to disable them. | [optional] 
**HasIssues** | Pointer to **bool** | either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. | [optional] 
**HasPackages** | Pointer to **bool** | either &#x60;true&#x60; to enable packages unit, or &#x60;false&#x60; to disable them. | [optional] 
**HasProjects** | Pointer to **bool** | either &#x60;true&#x60; to enable project unit, or &#x60;false&#x60; to disable them. | [optional] 
**HasPullRequests** | Pointer to **bool** | either &#x60;true&#x60; to allow pull requests, or &#x60;false&#x60; to prevent pull request. | [optional] 
**HasReleases** | Pointer to **bool** | either &#x60;true&#x60; to enable releases unit, or &#x60;false&#x60; to disable them. | [optional] 
**HasWiki** | Pointer to **bool** | either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. | [optional] 
**IgnoreWhitespaceConflicts** | Pointer to **bool** | either &#x60;true&#x60; to ignore whitespace for conflicts, or &#x60;false&#x60; to not ignore whitespace. | [optional] 
**InternalTracker** | Pointer to [**InternalTracker**](InternalTracker.md) |  | [optional] 
**MirrorInterval** | Pointer to **string** | set to a string like &#x60;8h30m0s&#x60; to set the mirror interval time | [optional] 
**Name** | Pointer to **string** | name of the repository | [optional] 
**Private** | Pointer to **bool** | either &#x60;true&#x60; to make the repository private or &#x60;false&#x60; to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private. | [optional] 
**Template** | Pointer to **bool** | either &#x60;true&#x60; to make this repository a template or &#x60;false&#x60; to make it a normal repository | [optional] 
**Website** | Pointer to **string** | a URL with more information about the repository. | [optional] 

## Methods

### NewEditRepoOption

`func NewEditRepoOption() *EditRepoOption`

NewEditRepoOption instantiates a new EditRepoOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditRepoOptionWithDefaults

`func NewEditRepoOptionWithDefaults() *EditRepoOption`

NewEditRepoOptionWithDefaults instantiates a new EditRepoOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAllowFastForwardOnlyMerge

`func (o *EditRepoOption) GetAllowFastForwardOnlyMerge() bool`

GetAllowFastForwardOnlyMerge returns the AllowFastForwardOnlyMerge field if non-nil, zero value otherwise.

### GetAllowFastForwardOnlyMergeOk

`func (o *EditRepoOption) GetAllowFastForwardOnlyMergeOk() (*bool, bool)`

GetAllowFastForwardOnlyMergeOk returns a tuple with the AllowFastForwardOnlyMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowFastForwardOnlyMerge

`func (o *EditRepoOption) SetAllowFastForwardOnlyMerge(v bool)`

SetAllowFastForwardOnlyMerge sets AllowFastForwardOnlyMerge field to given value.

### HasAllowFastForwardOnlyMerge

`func (o *EditRepoOption) HasAllowFastForwardOnlyMerge() bool`

HasAllowFastForwardOnlyMerge returns a boolean if a field has been set.

### GetAllowManualMerge

`func (o *EditRepoOption) GetAllowManualMerge() bool`

GetAllowManualMerge returns the AllowManualMerge field if non-nil, zero value otherwise.

### GetAllowManualMergeOk

`func (o *EditRepoOption) GetAllowManualMergeOk() (*bool, bool)`

GetAllowManualMergeOk returns a tuple with the AllowManualMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowManualMerge

`func (o *EditRepoOption) SetAllowManualMerge(v bool)`

SetAllowManualMerge sets AllowManualMerge field to given value.

### HasAllowManualMerge

`func (o *EditRepoOption) HasAllowManualMerge() bool`

HasAllowManualMerge returns a boolean if a field has been set.

### GetAllowMergeCommits

`func (o *EditRepoOption) GetAllowMergeCommits() bool`

GetAllowMergeCommits returns the AllowMergeCommits field if non-nil, zero value otherwise.

### GetAllowMergeCommitsOk

`func (o *EditRepoOption) GetAllowMergeCommitsOk() (*bool, bool)`

GetAllowMergeCommitsOk returns a tuple with the AllowMergeCommits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowMergeCommits

`func (o *EditRepoOption) SetAllowMergeCommits(v bool)`

SetAllowMergeCommits sets AllowMergeCommits field to given value.

### HasAllowMergeCommits

`func (o *EditRepoOption) HasAllowMergeCommits() bool`

HasAllowMergeCommits returns a boolean if a field has been set.

### GetAllowRebase

`func (o *EditRepoOption) GetAllowRebase() bool`

GetAllowRebase returns the AllowRebase field if non-nil, zero value otherwise.

### GetAllowRebaseOk

`func (o *EditRepoOption) GetAllowRebaseOk() (*bool, bool)`

GetAllowRebaseOk returns a tuple with the AllowRebase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowRebase

`func (o *EditRepoOption) SetAllowRebase(v bool)`

SetAllowRebase sets AllowRebase field to given value.

### HasAllowRebase

`func (o *EditRepoOption) HasAllowRebase() bool`

HasAllowRebase returns a boolean if a field has been set.

### GetAllowRebaseExplicit

`func (o *EditRepoOption) GetAllowRebaseExplicit() bool`

GetAllowRebaseExplicit returns the AllowRebaseExplicit field if non-nil, zero value otherwise.

### GetAllowRebaseExplicitOk

`func (o *EditRepoOption) GetAllowRebaseExplicitOk() (*bool, bool)`

GetAllowRebaseExplicitOk returns a tuple with the AllowRebaseExplicit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowRebaseExplicit

`func (o *EditRepoOption) SetAllowRebaseExplicit(v bool)`

SetAllowRebaseExplicit sets AllowRebaseExplicit field to given value.

### HasAllowRebaseExplicit

`func (o *EditRepoOption) HasAllowRebaseExplicit() bool`

HasAllowRebaseExplicit returns a boolean if a field has been set.

### GetAllowRebaseUpdate

`func (o *EditRepoOption) GetAllowRebaseUpdate() bool`

GetAllowRebaseUpdate returns the AllowRebaseUpdate field if non-nil, zero value otherwise.

### GetAllowRebaseUpdateOk

`func (o *EditRepoOption) GetAllowRebaseUpdateOk() (*bool, bool)`

GetAllowRebaseUpdateOk returns a tuple with the AllowRebaseUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowRebaseUpdate

`func (o *EditRepoOption) SetAllowRebaseUpdate(v bool)`

SetAllowRebaseUpdate sets AllowRebaseUpdate field to given value.

### HasAllowRebaseUpdate

`func (o *EditRepoOption) HasAllowRebaseUpdate() bool`

HasAllowRebaseUpdate returns a boolean if a field has been set.

### GetAllowSquashMerge

`func (o *EditRepoOption) GetAllowSquashMerge() bool`

GetAllowSquashMerge returns the AllowSquashMerge field if non-nil, zero value otherwise.

### GetAllowSquashMergeOk

`func (o *EditRepoOption) GetAllowSquashMergeOk() (*bool, bool)`

GetAllowSquashMergeOk returns a tuple with the AllowSquashMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowSquashMerge

`func (o *EditRepoOption) SetAllowSquashMerge(v bool)`

SetAllowSquashMerge sets AllowSquashMerge field to given value.

### HasAllowSquashMerge

`func (o *EditRepoOption) HasAllowSquashMerge() bool`

HasAllowSquashMerge returns a boolean if a field has been set.

### GetArchived

`func (o *EditRepoOption) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *EditRepoOption) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *EditRepoOption) SetArchived(v bool)`

SetArchived sets Archived field to given value.

### HasArchived

`func (o *EditRepoOption) HasArchived() bool`

HasArchived returns a boolean if a field has been set.

### GetAutodetectManualMerge

`func (o *EditRepoOption) GetAutodetectManualMerge() bool`

GetAutodetectManualMerge returns the AutodetectManualMerge field if non-nil, zero value otherwise.

### GetAutodetectManualMergeOk

`func (o *EditRepoOption) GetAutodetectManualMergeOk() (*bool, bool)`

GetAutodetectManualMergeOk returns a tuple with the AutodetectManualMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutodetectManualMerge

`func (o *EditRepoOption) SetAutodetectManualMerge(v bool)`

SetAutodetectManualMerge sets AutodetectManualMerge field to given value.

### HasAutodetectManualMerge

`func (o *EditRepoOption) HasAutodetectManualMerge() bool`

HasAutodetectManualMerge returns a boolean if a field has been set.

### GetDefaultAllowMaintainerEdit

`func (o *EditRepoOption) GetDefaultAllowMaintainerEdit() bool`

GetDefaultAllowMaintainerEdit returns the DefaultAllowMaintainerEdit field if non-nil, zero value otherwise.

### GetDefaultAllowMaintainerEditOk

`func (o *EditRepoOption) GetDefaultAllowMaintainerEditOk() (*bool, bool)`

GetDefaultAllowMaintainerEditOk returns a tuple with the DefaultAllowMaintainerEdit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultAllowMaintainerEdit

`func (o *EditRepoOption) SetDefaultAllowMaintainerEdit(v bool)`

SetDefaultAllowMaintainerEdit sets DefaultAllowMaintainerEdit field to given value.

### HasDefaultAllowMaintainerEdit

`func (o *EditRepoOption) HasDefaultAllowMaintainerEdit() bool`

HasDefaultAllowMaintainerEdit returns a boolean if a field has been set.

### GetDefaultBranch

`func (o *EditRepoOption) GetDefaultBranch() string`

GetDefaultBranch returns the DefaultBranch field if non-nil, zero value otherwise.

### GetDefaultBranchOk

`func (o *EditRepoOption) GetDefaultBranchOk() (*string, bool)`

GetDefaultBranchOk returns a tuple with the DefaultBranch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultBranch

`func (o *EditRepoOption) SetDefaultBranch(v string)`

SetDefaultBranch sets DefaultBranch field to given value.

### HasDefaultBranch

`func (o *EditRepoOption) HasDefaultBranch() bool`

HasDefaultBranch returns a boolean if a field has been set.

### GetDefaultDeleteBranchAfterMerge

`func (o *EditRepoOption) GetDefaultDeleteBranchAfterMerge() bool`

GetDefaultDeleteBranchAfterMerge returns the DefaultDeleteBranchAfterMerge field if non-nil, zero value otherwise.

### GetDefaultDeleteBranchAfterMergeOk

`func (o *EditRepoOption) GetDefaultDeleteBranchAfterMergeOk() (*bool, bool)`

GetDefaultDeleteBranchAfterMergeOk returns a tuple with the DefaultDeleteBranchAfterMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultDeleteBranchAfterMerge

`func (o *EditRepoOption) SetDefaultDeleteBranchAfterMerge(v bool)`

SetDefaultDeleteBranchAfterMerge sets DefaultDeleteBranchAfterMerge field to given value.

### HasDefaultDeleteBranchAfterMerge

`func (o *EditRepoOption) HasDefaultDeleteBranchAfterMerge() bool`

HasDefaultDeleteBranchAfterMerge returns a boolean if a field has been set.

### GetDefaultMergeStyle

`func (o *EditRepoOption) GetDefaultMergeStyle() string`

GetDefaultMergeStyle returns the DefaultMergeStyle field if non-nil, zero value otherwise.

### GetDefaultMergeStyleOk

`func (o *EditRepoOption) GetDefaultMergeStyleOk() (*string, bool)`

GetDefaultMergeStyleOk returns a tuple with the DefaultMergeStyle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultMergeStyle

`func (o *EditRepoOption) SetDefaultMergeStyle(v string)`

SetDefaultMergeStyle sets DefaultMergeStyle field to given value.

### HasDefaultMergeStyle

`func (o *EditRepoOption) HasDefaultMergeStyle() bool`

HasDefaultMergeStyle returns a boolean if a field has been set.

### GetDescription

`func (o *EditRepoOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *EditRepoOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *EditRepoOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *EditRepoOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEnablePrune

`func (o *EditRepoOption) GetEnablePrune() bool`

GetEnablePrune returns the EnablePrune field if non-nil, zero value otherwise.

### GetEnablePruneOk

`func (o *EditRepoOption) GetEnablePruneOk() (*bool, bool)`

GetEnablePruneOk returns a tuple with the EnablePrune field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnablePrune

`func (o *EditRepoOption) SetEnablePrune(v bool)`

SetEnablePrune sets EnablePrune field to given value.

### HasEnablePrune

`func (o *EditRepoOption) HasEnablePrune() bool`

HasEnablePrune returns a boolean if a field has been set.

### GetExternalTracker

`func (o *EditRepoOption) GetExternalTracker() ExternalTracker`

GetExternalTracker returns the ExternalTracker field if non-nil, zero value otherwise.

### GetExternalTrackerOk

`func (o *EditRepoOption) GetExternalTrackerOk() (*ExternalTracker, bool)`

GetExternalTrackerOk returns a tuple with the ExternalTracker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalTracker

`func (o *EditRepoOption) SetExternalTracker(v ExternalTracker)`

SetExternalTracker sets ExternalTracker field to given value.

### HasExternalTracker

`func (o *EditRepoOption) HasExternalTracker() bool`

HasExternalTracker returns a boolean if a field has been set.

### GetExternalWiki

`func (o *EditRepoOption) GetExternalWiki() ExternalWiki`

GetExternalWiki returns the ExternalWiki field if non-nil, zero value otherwise.

### GetExternalWikiOk

`func (o *EditRepoOption) GetExternalWikiOk() (*ExternalWiki, bool)`

GetExternalWikiOk returns a tuple with the ExternalWiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalWiki

`func (o *EditRepoOption) SetExternalWiki(v ExternalWiki)`

SetExternalWiki sets ExternalWiki field to given value.

### HasExternalWiki

`func (o *EditRepoOption) HasExternalWiki() bool`

HasExternalWiki returns a boolean if a field has been set.

### GetHasActions

`func (o *EditRepoOption) GetHasActions() bool`

GetHasActions returns the HasActions field if non-nil, zero value otherwise.

### GetHasActionsOk

`func (o *EditRepoOption) GetHasActionsOk() (*bool, bool)`

GetHasActionsOk returns a tuple with the HasActions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasActions

`func (o *EditRepoOption) SetHasActions(v bool)`

SetHasActions sets HasActions field to given value.

### HasHasActions

`func (o *EditRepoOption) HasHasActions() bool`

HasHasActions returns a boolean if a field has been set.

### GetHasIssues

`func (o *EditRepoOption) GetHasIssues() bool`

GetHasIssues returns the HasIssues field if non-nil, zero value otherwise.

### GetHasIssuesOk

`func (o *EditRepoOption) GetHasIssuesOk() (*bool, bool)`

GetHasIssuesOk returns a tuple with the HasIssues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasIssues

`func (o *EditRepoOption) SetHasIssues(v bool)`

SetHasIssues sets HasIssues field to given value.

### HasHasIssues

`func (o *EditRepoOption) HasHasIssues() bool`

HasHasIssues returns a boolean if a field has been set.

### GetHasPackages

`func (o *EditRepoOption) GetHasPackages() bool`

GetHasPackages returns the HasPackages field if non-nil, zero value otherwise.

### GetHasPackagesOk

`func (o *EditRepoOption) GetHasPackagesOk() (*bool, bool)`

GetHasPackagesOk returns a tuple with the HasPackages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPackages

`func (o *EditRepoOption) SetHasPackages(v bool)`

SetHasPackages sets HasPackages field to given value.

### HasHasPackages

`func (o *EditRepoOption) HasHasPackages() bool`

HasHasPackages returns a boolean if a field has been set.

### GetHasProjects

`func (o *EditRepoOption) GetHasProjects() bool`

GetHasProjects returns the HasProjects field if non-nil, zero value otherwise.

### GetHasProjectsOk

`func (o *EditRepoOption) GetHasProjectsOk() (*bool, bool)`

GetHasProjectsOk returns a tuple with the HasProjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasProjects

`func (o *EditRepoOption) SetHasProjects(v bool)`

SetHasProjects sets HasProjects field to given value.

### HasHasProjects

`func (o *EditRepoOption) HasHasProjects() bool`

HasHasProjects returns a boolean if a field has been set.

### GetHasPullRequests

`func (o *EditRepoOption) GetHasPullRequests() bool`

GetHasPullRequests returns the HasPullRequests field if non-nil, zero value otherwise.

### GetHasPullRequestsOk

`func (o *EditRepoOption) GetHasPullRequestsOk() (*bool, bool)`

GetHasPullRequestsOk returns a tuple with the HasPullRequests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPullRequests

`func (o *EditRepoOption) SetHasPullRequests(v bool)`

SetHasPullRequests sets HasPullRequests field to given value.

### HasHasPullRequests

`func (o *EditRepoOption) HasHasPullRequests() bool`

HasHasPullRequests returns a boolean if a field has been set.

### GetHasReleases

`func (o *EditRepoOption) GetHasReleases() bool`

GetHasReleases returns the HasReleases field if non-nil, zero value otherwise.

### GetHasReleasesOk

`func (o *EditRepoOption) GetHasReleasesOk() (*bool, bool)`

GetHasReleasesOk returns a tuple with the HasReleases field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasReleases

`func (o *EditRepoOption) SetHasReleases(v bool)`

SetHasReleases sets HasReleases field to given value.

### HasHasReleases

`func (o *EditRepoOption) HasHasReleases() bool`

HasHasReleases returns a boolean if a field has been set.

### GetHasWiki

`func (o *EditRepoOption) GetHasWiki() bool`

GetHasWiki returns the HasWiki field if non-nil, zero value otherwise.

### GetHasWikiOk

`func (o *EditRepoOption) GetHasWikiOk() (*bool, bool)`

GetHasWikiOk returns a tuple with the HasWiki field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasWiki

`func (o *EditRepoOption) SetHasWiki(v bool)`

SetHasWiki sets HasWiki field to given value.

### HasHasWiki

`func (o *EditRepoOption) HasHasWiki() bool`

HasHasWiki returns a boolean if a field has been set.

### GetIgnoreWhitespaceConflicts

`func (o *EditRepoOption) GetIgnoreWhitespaceConflicts() bool`

GetIgnoreWhitespaceConflicts returns the IgnoreWhitespaceConflicts field if non-nil, zero value otherwise.

### GetIgnoreWhitespaceConflictsOk

`func (o *EditRepoOption) GetIgnoreWhitespaceConflictsOk() (*bool, bool)`

GetIgnoreWhitespaceConflictsOk returns a tuple with the IgnoreWhitespaceConflicts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIgnoreWhitespaceConflicts

`func (o *EditRepoOption) SetIgnoreWhitespaceConflicts(v bool)`

SetIgnoreWhitespaceConflicts sets IgnoreWhitespaceConflicts field to given value.

### HasIgnoreWhitespaceConflicts

`func (o *EditRepoOption) HasIgnoreWhitespaceConflicts() bool`

HasIgnoreWhitespaceConflicts returns a boolean if a field has been set.

### GetInternalTracker

`func (o *EditRepoOption) GetInternalTracker() InternalTracker`

GetInternalTracker returns the InternalTracker field if non-nil, zero value otherwise.

### GetInternalTrackerOk

`func (o *EditRepoOption) GetInternalTrackerOk() (*InternalTracker, bool)`

GetInternalTrackerOk returns a tuple with the InternalTracker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternalTracker

`func (o *EditRepoOption) SetInternalTracker(v InternalTracker)`

SetInternalTracker sets InternalTracker field to given value.

### HasInternalTracker

`func (o *EditRepoOption) HasInternalTracker() bool`

HasInternalTracker returns a boolean if a field has been set.

### GetMirrorInterval

`func (o *EditRepoOption) GetMirrorInterval() string`

GetMirrorInterval returns the MirrorInterval field if non-nil, zero value otherwise.

### GetMirrorIntervalOk

`func (o *EditRepoOption) GetMirrorIntervalOk() (*string, bool)`

GetMirrorIntervalOk returns a tuple with the MirrorInterval field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMirrorInterval

`func (o *EditRepoOption) SetMirrorInterval(v string)`

SetMirrorInterval sets MirrorInterval field to given value.

### HasMirrorInterval

`func (o *EditRepoOption) HasMirrorInterval() bool`

HasMirrorInterval returns a boolean if a field has been set.

### GetName

`func (o *EditRepoOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EditRepoOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *EditRepoOption) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *EditRepoOption) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrivate

`func (o *EditRepoOption) GetPrivate() bool`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *EditRepoOption) GetPrivateOk() (*bool, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *EditRepoOption) SetPrivate(v bool)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *EditRepoOption) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.

### GetTemplate

`func (o *EditRepoOption) GetTemplate() bool`

GetTemplate returns the Template field if non-nil, zero value otherwise.

### GetTemplateOk

`func (o *EditRepoOption) GetTemplateOk() (*bool, bool)`

GetTemplateOk returns a tuple with the Template field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemplate

`func (o *EditRepoOption) SetTemplate(v bool)`

SetTemplate sets Template field to given value.

### HasTemplate

`func (o *EditRepoOption) HasTemplate() bool`

HasTemplate returns a boolean if a field has been set.

### GetWebsite

`func (o *EditRepoOption) GetWebsite() string`

GetWebsite returns the Website field if non-nil, zero value otherwise.

### GetWebsiteOk

`func (o *EditRepoOption) GetWebsiteOk() (*string, bool)`

GetWebsiteOk returns a tuple with the Website field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsite

`func (o *EditRepoOption) SetWebsite(v string)`

SetWebsite sets Website field to given value.

### HasWebsite

`func (o *EditRepoOption) HasWebsite() bool`

HasWebsite returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



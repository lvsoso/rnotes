# \RepositoryApi

All URIs are relative to *http://}/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AcceptRepoTransfer**](RepositoryApi.md#AcceptRepoTransfer) | **Post** /repos/{owner}/{repo}/transfer/accept | Accept a repo transfer
[**CreateCurrentUserRepo**](RepositoryApi.md#CreateCurrentUserRepo) | **Post** /user/repos | Create a repository
[**CreateFork**](RepositoryApi.md#CreateFork) | **Post** /repos/{owner}/{repo}/forks | Fork a repository
[**DeleteRepoSecret**](RepositoryApi.md#DeleteRepoSecret) | **Delete** /repos/{owner}/{repo}/actions/secrets/{secretname} | Delete a secret in a repository
[**GenerateRepo**](RepositoryApi.md#GenerateRepo) | **Post** /repos/{template_owner}/{template_repo}/generate | Create a repository using a template
[**GetAnnotatedTag**](RepositoryApi.md#GetAnnotatedTag) | **Get** /repos/{owner}/{repo}/git/tags/{sha} | Gets the tag object of an annotated tag (not lightweight tags)
[**GetBlob**](RepositoryApi.md#GetBlob) | **Get** /repos/{owner}/{repo}/git/blobs/{sha} | Gets the blob of a repository.
[**GetTree**](RepositoryApi.md#GetTree) | **Get** /repos/{owner}/{repo}/git/trees/{sha} | Gets the tree of a repository.
[**ListForks**](RepositoryApi.md#ListForks) | **Get** /repos/{owner}/{repo}/forks | List a repository&#39;s forks
[**RejectRepoTransfer**](RepositoryApi.md#RejectRepoTransfer) | **Post** /repos/{owner}/{repo}/transfer/reject | Reject a repo transfer
[**RepoAddCollaborator**](RepositoryApi.md#RepoAddCollaborator) | **Put** /repos/{owner}/{repo}/collaborators/{collaborator} | Add a collaborator to a repository
[**RepoAddPushMirror**](RepositoryApi.md#RepoAddPushMirror) | **Post** /repos/{owner}/{repo}/push_mirrors | add a push mirror to the repository
[**RepoAddTeam**](RepositoryApi.md#RepoAddTeam) | **Put** /repos/{owner}/{repo}/teams/{team} | Add a team to a repository
[**RepoAddTopic**](RepositoryApi.md#RepoAddTopic) | **Put** /repos/{owner}/{repo}/topics/{topic} | Add a topic to a repository
[**RepoApplyDiffPatch**](RepositoryApi.md#RepoApplyDiffPatch) | **Post** /repos/{owner}/{repo}/diffpatch | Apply diff patch to repository
[**RepoCancelScheduledAutoMerge**](RepositoryApi.md#RepoCancelScheduledAutoMerge) | **Delete** /repos/{owner}/{repo}/pulls/{index}/merge | Cancel the scheduled auto merge for the given pull request
[**RepoChangeFiles**](RepositoryApi.md#RepoChangeFiles) | **Post** /repos/{owner}/{repo}/contents | Modify multiple files in a repository
[**RepoCheckCollaborator**](RepositoryApi.md#RepoCheckCollaborator) | **Get** /repos/{owner}/{repo}/collaborators/{collaborator} | Check if a user is a collaborator of a repository
[**RepoCheckTeam**](RepositoryApi.md#RepoCheckTeam) | **Get** /repos/{owner}/{repo}/teams/{team} | Check if a team is assigned to a repository
[**RepoCreateBranch**](RepositoryApi.md#RepoCreateBranch) | **Post** /repos/{owner}/{repo}/branches | Create a branch
[**RepoCreateBranchProtection**](RepositoryApi.md#RepoCreateBranchProtection) | **Post** /repos/{owner}/{repo}/branch_protections | Create a branch protections for a repository
[**RepoCreateFile**](RepositoryApi.md#RepoCreateFile) | **Post** /repos/{owner}/{repo}/contents/{filepath} | Create a file in a repository
[**RepoCreateHook**](RepositoryApi.md#RepoCreateHook) | **Post** /repos/{owner}/{repo}/hooks | Create a hook
[**RepoCreateKey**](RepositoryApi.md#RepoCreateKey) | **Post** /repos/{owner}/{repo}/keys | Add a key to a repository
[**RepoCreatePullRequest**](RepositoryApi.md#RepoCreatePullRequest) | **Post** /repos/{owner}/{repo}/pulls | Create a pull request
[**RepoCreatePullReview**](RepositoryApi.md#RepoCreatePullReview) | **Post** /repos/{owner}/{repo}/pulls/{index}/reviews | Create a review to an pull request
[**RepoCreatePullReviewRequests**](RepositoryApi.md#RepoCreatePullReviewRequests) | **Post** /repos/{owner}/{repo}/pulls/{index}/requested_reviewers | create review requests for a pull request
[**RepoCreateRelease**](RepositoryApi.md#RepoCreateRelease) | **Post** /repos/{owner}/{repo}/releases | Create a release
[**RepoCreateReleaseAttachment**](RepositoryApi.md#RepoCreateReleaseAttachment) | **Post** /repos/{owner}/{repo}/releases/{id}/assets | Create a release attachment
[**RepoCreateStatus**](RepositoryApi.md#RepoCreateStatus) | **Post** /repos/{owner}/{repo}/statuses/{sha} | Create a commit status
[**RepoCreateTag**](RepositoryApi.md#RepoCreateTag) | **Post** /repos/{owner}/{repo}/tags | Create a new git tag in a repository
[**RepoCreateWikiPage**](RepositoryApi.md#RepoCreateWikiPage) | **Post** /repos/{owner}/{repo}/wiki/new | Create a wiki page
[**RepoDelete**](RepositoryApi.md#RepoDelete) | **Delete** /repos/{owner}/{repo} | Delete a repository
[**RepoDeleteAvatar**](RepositoryApi.md#RepoDeleteAvatar) | **Delete** /repos/{owner}/{repo}/avatar | Delete avatar
[**RepoDeleteBranch**](RepositoryApi.md#RepoDeleteBranch) | **Delete** /repos/{owner}/{repo}/branches/{branch} | Delete a specific branch from a repository
[**RepoDeleteBranchProtection**](RepositoryApi.md#RepoDeleteBranchProtection) | **Delete** /repos/{owner}/{repo}/branch_protections/{name} | Delete a specific branch protection for the repository
[**RepoDeleteCollaborator**](RepositoryApi.md#RepoDeleteCollaborator) | **Delete** /repos/{owner}/{repo}/collaborators/{collaborator} | Delete a collaborator from a repository
[**RepoDeleteFile**](RepositoryApi.md#RepoDeleteFile) | **Delete** /repos/{owner}/{repo}/contents/{filepath} | Delete a file in a repository
[**RepoDeleteGitHook**](RepositoryApi.md#RepoDeleteGitHook) | **Delete** /repos/{owner}/{repo}/hooks/git/{id} | Delete a Git hook in a repository
[**RepoDeleteHook**](RepositoryApi.md#RepoDeleteHook) | **Delete** /repos/{owner}/{repo}/hooks/{id} | Delete a hook in a repository
[**RepoDeleteKey**](RepositoryApi.md#RepoDeleteKey) | **Delete** /repos/{owner}/{repo}/keys/{id} | Delete a key from a repository
[**RepoDeletePullReview**](RepositoryApi.md#RepoDeletePullReview) | **Delete** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Delete a specific review from a pull request
[**RepoDeletePullReviewRequests**](RepositoryApi.md#RepoDeletePullReviewRequests) | **Delete** /repos/{owner}/{repo}/pulls/{index}/requested_reviewers | cancel review requests for a pull request
[**RepoDeletePushMirror**](RepositoryApi.md#RepoDeletePushMirror) | **Delete** /repos/{owner}/{repo}/push_mirrors/{name} | deletes a push mirror from a repository by remoteName
[**RepoDeleteRelease**](RepositoryApi.md#RepoDeleteRelease) | **Delete** /repos/{owner}/{repo}/releases/{id} | Delete a release
[**RepoDeleteReleaseAttachment**](RepositoryApi.md#RepoDeleteReleaseAttachment) | **Delete** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Delete a release attachment
[**RepoDeleteReleaseByTag**](RepositoryApi.md#RepoDeleteReleaseByTag) | **Delete** /repos/{owner}/{repo}/releases/tags/{tag} | Delete a release by tag name
[**RepoDeleteTag**](RepositoryApi.md#RepoDeleteTag) | **Delete** /repos/{owner}/{repo}/tags/{tag} | Delete a repository&#39;s tag by name
[**RepoDeleteTeam**](RepositoryApi.md#RepoDeleteTeam) | **Delete** /repos/{owner}/{repo}/teams/{team} | Delete a team from a repository
[**RepoDeleteTopic**](RepositoryApi.md#RepoDeleteTopic) | **Delete** /repos/{owner}/{repo}/topics/{topic} | Delete a topic from a repository
[**RepoDeleteWikiPage**](RepositoryApi.md#RepoDeleteWikiPage) | **Delete** /repos/{owner}/{repo}/wiki/page/{pageName} | Delete a wiki page
[**RepoDismissPullReview**](RepositoryApi.md#RepoDismissPullReview) | **Post** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals | Dismiss a review for a pull request
[**RepoDownloadCommitDiffOrPatch**](RepositoryApi.md#RepoDownloadCommitDiffOrPatch) | **Get** /repos/{owner}/{repo}/git/commits/{sha}.{diffType} | Get a commit&#39;s diff or patch
[**RepoDownloadPullDiffOrPatch**](RepositoryApi.md#RepoDownloadPullDiffOrPatch) | **Get** /repos/{owner}/{repo}/pulls/{index}.{diffType} | Get a pull request diff or patch
[**RepoEdit**](RepositoryApi.md#RepoEdit) | **Patch** /repos/{owner}/{repo} | Edit a repository&#39;s properties. Only fields that are set will be changed.
[**RepoEditBranchProtection**](RepositoryApi.md#RepoEditBranchProtection) | **Patch** /repos/{owner}/{repo}/branch_protections/{name} | Edit a branch protections for a repository. Only fields that are set will be changed
[**RepoEditGitHook**](RepositoryApi.md#RepoEditGitHook) | **Patch** /repos/{owner}/{repo}/hooks/git/{id} | Edit a Git hook in a repository
[**RepoEditHook**](RepositoryApi.md#RepoEditHook) | **Patch** /repos/{owner}/{repo}/hooks/{id} | Edit a hook in a repository
[**RepoEditPullRequest**](RepositoryApi.md#RepoEditPullRequest) | **Patch** /repos/{owner}/{repo}/pulls/{index} | Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
[**RepoEditRelease**](RepositoryApi.md#RepoEditRelease) | **Patch** /repos/{owner}/{repo}/releases/{id} | Update a release
[**RepoEditReleaseAttachment**](RepositoryApi.md#RepoEditReleaseAttachment) | **Patch** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Edit a release attachment
[**RepoEditWikiPage**](RepositoryApi.md#RepoEditWikiPage) | **Patch** /repos/{owner}/{repo}/wiki/page/{pageName} | Edit a wiki page
[**RepoGet**](RepositoryApi.md#RepoGet) | **Get** /repos/{owner}/{repo} | Get a repository
[**RepoGetAllCommits**](RepositoryApi.md#RepoGetAllCommits) | **Get** /repos/{owner}/{repo}/commits | Get a list of all commits from a repository
[**RepoGetArchive**](RepositoryApi.md#RepoGetArchive) | **Get** /repos/{owner}/{repo}/archive/{archive} | Get an archive of a repository
[**RepoGetAssignees**](RepositoryApi.md#RepoGetAssignees) | **Get** /repos/{owner}/{repo}/assignees | Return all users that have write access and can be assigned to issues
[**RepoGetBranch**](RepositoryApi.md#RepoGetBranch) | **Get** /repos/{owner}/{repo}/branches/{branch} | Retrieve a specific branch from a repository, including its effective branch protection
[**RepoGetBranchProtection**](RepositoryApi.md#RepoGetBranchProtection) | **Get** /repos/{owner}/{repo}/branch_protections/{name} | Get a specific branch protection for the repository
[**RepoGetByID**](RepositoryApi.md#RepoGetByID) | **Get** /repositories/{id} | Get a repository by id
[**RepoGetCombinedStatusByRef**](RepositoryApi.md#RepoGetCombinedStatusByRef) | **Get** /repos/{owner}/{repo}/commits/{ref}/status | Get a commit&#39;s combined status, by branch/tag/commit reference
[**RepoGetContents**](RepositoryApi.md#RepoGetContents) | **Get** /repos/{owner}/{repo}/contents/{filepath} | Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
[**RepoGetContentsList**](RepositoryApi.md#RepoGetContentsList) | **Get** /repos/{owner}/{repo}/contents | Gets the metadata of all the entries of the root dir
[**RepoGetEditorConfig**](RepositoryApi.md#RepoGetEditorConfig) | **Get** /repos/{owner}/{repo}/editorconfig/{filepath} | Get the EditorConfig definitions of a file in a repository
[**RepoGetGitHook**](RepositoryApi.md#RepoGetGitHook) | **Get** /repos/{owner}/{repo}/hooks/git/{id} | Get a Git hook
[**RepoGetHook**](RepositoryApi.md#RepoGetHook) | **Get** /repos/{owner}/{repo}/hooks/{id} | Get a hook
[**RepoGetIssueConfig**](RepositoryApi.md#RepoGetIssueConfig) | **Get** /repos/{owner}/{repo}/issue_config | Returns the issue config for a repo
[**RepoGetIssueTemplates**](RepositoryApi.md#RepoGetIssueTemplates) | **Get** /repos/{owner}/{repo}/issue_templates | Get available issue templates for a repository
[**RepoGetKey**](RepositoryApi.md#RepoGetKey) | **Get** /repos/{owner}/{repo}/keys/{id} | Get a repository&#39;s key by id
[**RepoGetLanguages**](RepositoryApi.md#RepoGetLanguages) | **Get** /repos/{owner}/{repo}/languages | Get languages and number of bytes of code written
[**RepoGetLatestRelease**](RepositoryApi.md#RepoGetLatestRelease) | **Get** /repos/{owner}/{repo}/releases/latest | Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at
[**RepoGetNote**](RepositoryApi.md#RepoGetNote) | **Get** /repos/{owner}/{repo}/git/notes/{sha} | Get a note corresponding to a single commit from a repository
[**RepoGetPullRequest**](RepositoryApi.md#RepoGetPullRequest) | **Get** /repos/{owner}/{repo}/pulls/{index} | Get a pull request
[**RepoGetPullRequestCommits**](RepositoryApi.md#RepoGetPullRequestCommits) | **Get** /repos/{owner}/{repo}/pulls/{index}/commits | Get commits for a pull request
[**RepoGetPullRequestFiles**](RepositoryApi.md#RepoGetPullRequestFiles) | **Get** /repos/{owner}/{repo}/pulls/{index}/files | Get changed files for a pull request
[**RepoGetPullReview**](RepositoryApi.md#RepoGetPullReview) | **Get** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Get a specific review for a pull request
[**RepoGetPullReviewComments**](RepositoryApi.md#RepoGetPullReviewComments) | **Get** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments | Get a specific review for a pull request
[**RepoGetPushMirrorByRemoteName**](RepositoryApi.md#RepoGetPushMirrorByRemoteName) | **Get** /repos/{owner}/{repo}/push_mirrors/{name} | Get push mirror of the repository by remoteName
[**RepoGetRawFile**](RepositoryApi.md#RepoGetRawFile) | **Get** /repos/{owner}/{repo}/raw/{filepath} | Get a file from a repository
[**RepoGetRawFileOrLFS**](RepositoryApi.md#RepoGetRawFileOrLFS) | **Get** /repos/{owner}/{repo}/media/{filepath} | Get a file or it&#39;s LFS object from a repository
[**RepoGetRelease**](RepositoryApi.md#RepoGetRelease) | **Get** /repos/{owner}/{repo}/releases/{id} | Get a release
[**RepoGetReleaseAttachment**](RepositoryApi.md#RepoGetReleaseAttachment) | **Get** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Get a release attachment
[**RepoGetReleaseByTag**](RepositoryApi.md#RepoGetReleaseByTag) | **Get** /repos/{owner}/{repo}/releases/tags/{tag} | Get a release by tag name
[**RepoGetRepoPermissions**](RepositoryApi.md#RepoGetRepoPermissions) | **Get** /repos/{owner}/{repo}/collaborators/{collaborator}/permission | Get repository permissions for a user
[**RepoGetReviewers**](RepositoryApi.md#RepoGetReviewers) | **Get** /repos/{owner}/{repo}/reviewers | Return all users that can be requested to review in this repo
[**RepoGetRunnerRegistrationToken**](RepositoryApi.md#RepoGetRunnerRegistrationToken) | **Get** /repos/{owner}/{repo}/runners/registration-token | Get a repository&#39;s actions runner registration token
[**RepoGetSingleCommit**](RepositoryApi.md#RepoGetSingleCommit) | **Get** /repos/{owner}/{repo}/git/commits/{sha} | Get a single commit from a repository
[**RepoGetTag**](RepositoryApi.md#RepoGetTag) | **Get** /repos/{owner}/{repo}/tags/{tag} | Get the tag of a repository by tag name
[**RepoGetWikiPage**](RepositoryApi.md#RepoGetWikiPage) | **Get** /repos/{owner}/{repo}/wiki/page/{pageName} | Get a wiki page
[**RepoGetWikiPageRevisions**](RepositoryApi.md#RepoGetWikiPageRevisions) | **Get** /repos/{owner}/{repo}/wiki/revisions/{pageName} | Get revisions of a wiki page
[**RepoGetWikiPages**](RepositoryApi.md#RepoGetWikiPages) | **Get** /repos/{owner}/{repo}/wiki/pages | Get all wiki pages
[**RepoListActivityFeeds**](RepositoryApi.md#RepoListActivityFeeds) | **Get** /repos/{owner}/{repo}/activities/feeds | List a repository&#39;s activity feeds
[**RepoListAllGitRefs**](RepositoryApi.md#RepoListAllGitRefs) | **Get** /repos/{owner}/{repo}/git/refs | Get specified ref or filtered repository&#39;s refs
[**RepoListBranchProtection**](RepositoryApi.md#RepoListBranchProtection) | **Get** /repos/{owner}/{repo}/branch_protections | List branch protections for a repository
[**RepoListBranches**](RepositoryApi.md#RepoListBranches) | **Get** /repos/{owner}/{repo}/branches | List a repository&#39;s branches
[**RepoListCollaborators**](RepositoryApi.md#RepoListCollaborators) | **Get** /repos/{owner}/{repo}/collaborators | List a repository&#39;s collaborators
[**RepoListGitHooks**](RepositoryApi.md#RepoListGitHooks) | **Get** /repos/{owner}/{repo}/hooks/git | List the Git hooks in a repository
[**RepoListGitRefs**](RepositoryApi.md#RepoListGitRefs) | **Get** /repos/{owner}/{repo}/git/refs/{ref} | Get specified ref or filtered repository&#39;s refs
[**RepoListHooks**](RepositoryApi.md#RepoListHooks) | **Get** /repos/{owner}/{repo}/hooks | List the hooks in a repository
[**RepoListKeys**](RepositoryApi.md#RepoListKeys) | **Get** /repos/{owner}/{repo}/keys | List a repository&#39;s keys
[**RepoListPinnedIssues**](RepositoryApi.md#RepoListPinnedIssues) | **Get** /repos/{owner}/{repo}/issues/pinned | List a repo&#39;s pinned issues
[**RepoListPinnedPullRequests**](RepositoryApi.md#RepoListPinnedPullRequests) | **Get** /repos/{owner}/{repo}/pulls/pinned | List a repo&#39;s pinned pull requests
[**RepoListPullRequests**](RepositoryApi.md#RepoListPullRequests) | **Get** /repos/{owner}/{repo}/pulls | List a repo&#39;s pull requests
[**RepoListPullReviews**](RepositoryApi.md#RepoListPullReviews) | **Get** /repos/{owner}/{repo}/pulls/{index}/reviews | List all reviews for a pull request
[**RepoListPushMirrors**](RepositoryApi.md#RepoListPushMirrors) | **Get** /repos/{owner}/{repo}/push_mirrors | Get all push mirrors of the repository
[**RepoListReleaseAttachments**](RepositoryApi.md#RepoListReleaseAttachments) | **Get** /repos/{owner}/{repo}/releases/{id}/assets | List release&#39;s attachments
[**RepoListReleases**](RepositoryApi.md#RepoListReleases) | **Get** /repos/{owner}/{repo}/releases | List a repo&#39;s releases
[**RepoListStargazers**](RepositoryApi.md#RepoListStargazers) | **Get** /repos/{owner}/{repo}/stargazers | List a repo&#39;s stargazers
[**RepoListStatuses**](RepositoryApi.md#RepoListStatuses) | **Get** /repos/{owner}/{repo}/statuses/{sha} | Get a commit&#39;s statuses
[**RepoListStatusesByRef**](RepositoryApi.md#RepoListStatusesByRef) | **Get** /repos/{owner}/{repo}/commits/{ref}/statuses | Get a commit&#39;s statuses, by branch/tag/commit reference
[**RepoListSubscribers**](RepositoryApi.md#RepoListSubscribers) | **Get** /repos/{owner}/{repo}/subscribers | List a repo&#39;s watchers
[**RepoListTags**](RepositoryApi.md#RepoListTags) | **Get** /repos/{owner}/{repo}/tags | List a repository&#39;s tags
[**RepoListTeams**](RepositoryApi.md#RepoListTeams) | **Get** /repos/{owner}/{repo}/teams | List a repository&#39;s teams
[**RepoListTopics**](RepositoryApi.md#RepoListTopics) | **Get** /repos/{owner}/{repo}/topics | Get list of topics that a repository has
[**RepoMergePullRequest**](RepositoryApi.md#RepoMergePullRequest) | **Post** /repos/{owner}/{repo}/pulls/{index}/merge | Merge a pull request
[**RepoMigrate**](RepositoryApi.md#RepoMigrate) | **Post** /repos/migrate | Migrate a remote git repository
[**RepoMirrorSync**](RepositoryApi.md#RepoMirrorSync) | **Post** /repos/{owner}/{repo}/mirror-sync | Sync a mirrored repository
[**RepoNewPinAllowed**](RepositoryApi.md#RepoNewPinAllowed) | **Get** /repos/{owner}/{repo}/new_pin_allowed | Returns if new Issue Pins are allowed
[**RepoPullRequestIsMerged**](RepositoryApi.md#RepoPullRequestIsMerged) | **Get** /repos/{owner}/{repo}/pulls/{index}/merge | Check if a pull request has been merged
[**RepoPushMirrorSync**](RepositoryApi.md#RepoPushMirrorSync) | **Post** /repos/{owner}/{repo}/push_mirrors-sync | Sync all push mirrored repository
[**RepoSearch**](RepositoryApi.md#RepoSearch) | **Get** /repos/search | Search for repositories
[**RepoSigningKey**](RepositoryApi.md#RepoSigningKey) | **Get** /repos/{owner}/{repo}/signing-key.gpg | Get signing-key.gpg for given repository
[**RepoSubmitPullReview**](RepositoryApi.md#RepoSubmitPullReview) | **Post** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Submit a pending review to an pull request
[**RepoTestHook**](RepositoryApi.md#RepoTestHook) | **Post** /repos/{owner}/{repo}/hooks/{id}/tests | Test a push webhook
[**RepoTrackedTimes**](RepositoryApi.md#RepoTrackedTimes) | **Get** /repos/{owner}/{repo}/times | List a repo&#39;s tracked times
[**RepoTransfer**](RepositoryApi.md#RepoTransfer) | **Post** /repos/{owner}/{repo}/transfer | Transfer a repo ownership
[**RepoUnDismissPullReview**](RepositoryApi.md#RepoUnDismissPullReview) | **Post** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals | Cancel to dismiss a review for a pull request
[**RepoUpdateAvatar**](RepositoryApi.md#RepoUpdateAvatar) | **Post** /repos/{owner}/{repo}/avatar | Update avatar
[**RepoUpdateFile**](RepositoryApi.md#RepoUpdateFile) | **Put** /repos/{owner}/{repo}/contents/{filepath} | Update a file in a repository
[**RepoUpdatePullRequest**](RepositoryApi.md#RepoUpdatePullRequest) | **Post** /repos/{owner}/{repo}/pulls/{index}/update | Merge PR&#39;s baseBranch into headBranch
[**RepoUpdateTopics**](RepositoryApi.md#RepoUpdateTopics) | **Put** /repos/{owner}/{repo}/topics | Replace list of topics for a repository
[**RepoValidateIssueConfig**](RepositoryApi.md#RepoValidateIssueConfig) | **Get** /repos/{owner}/{repo}/issue_config/validate | Returns the validation information for a issue config
[**TopicSearch**](RepositoryApi.md#TopicSearch) | **Get** /topics/search | search topics via keyword
[**UpdateRepoSecret**](RepositoryApi.md#UpdateRepoSecret) | **Put** /repos/{owner}/{repo}/actions/secrets/{secretname} | Create or Update a secret value in a repository
[**UserCurrentCheckSubscription**](RepositoryApi.md#UserCurrentCheckSubscription) | **Get** /repos/{owner}/{repo}/subscription | Check if the current user is watching a repo
[**UserCurrentDeleteSubscription**](RepositoryApi.md#UserCurrentDeleteSubscription) | **Delete** /repos/{owner}/{repo}/subscription | Unwatch a repo
[**UserCurrentPutSubscription**](RepositoryApi.md#UserCurrentPutSubscription) | **Put** /repos/{owner}/{repo}/subscription | Watch a repo
[**UserTrackedTimes**](RepositoryApi.md#UserTrackedTimes) | **Get** /repos/{owner}/{repo}/times/{user} | List a user&#39;s tracked times in a repo



## AcceptRepoTransfer

> Repository AcceptRepoTransfer(ctx, owner, repo).Execute()

Accept a repo transfer

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to transfer
    repo := "repo_example" // string | name of the repo to transfer

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.AcceptRepoTransfer(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.AcceptRepoTransfer``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AcceptRepoTransfer`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.AcceptRepoTransfer`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to transfer | 
**repo** | **string** | name of the repo to transfer | 

### Other Parameters

Other parameters are passed through a pointer to a apiAcceptRepoTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateCurrentUserRepo

> Repository CreateCurrentUserRepo(ctx).Body(body).Execute()

Create a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    body := *openapiclient.NewCreateRepoOption("Name_example") // CreateRepoOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.CreateCurrentUserRepo(context.Background()).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.CreateCurrentUserRepo``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `CreateCurrentUserRepo`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.CreateCurrentUserRepo`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCurrentUserRepoRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepoOption**](CreateRepoOption.md) |  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateFork

> Repository CreateFork(ctx, owner, repo).Body(body).Execute()

Fork a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to fork
    repo := "repo_example" // string | name of the repo to fork
    body := *openapiclient.NewCreateForkOption() // CreateForkOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.CreateFork(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.CreateFork``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `CreateFork`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.CreateFork`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to fork | 
**repo** | **string** | name of the repo to fork | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateForkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateForkOption**](CreateForkOption.md) |  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteRepoSecret

> DeleteRepoSecret(ctx, owner, repo, secretname).Execute()

Delete a secret in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repository
    repo := "repo_example" // string | name of the repository
    secretname := "secretname_example" // string | name of the secret

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.DeleteRepoSecret(context.Background(), owner, repo, secretname).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.DeleteRepoSecret``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repository | 
**repo** | **string** | name of the repository | 
**secretname** | **string** | name of the secret | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteRepoSecretRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GenerateRepo

> Repository GenerateRepo(ctx, templateOwner, templateRepo).Body(body).Execute()

Create a repository using a template

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    templateOwner := "templateOwner_example" // string | name of the template repository owner
    templateRepo := "templateRepo_example" // string | name of the template repository
    body := *openapiclient.NewGenerateRepoOption("Name_example", "Owner_example") // GenerateRepoOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.GenerateRepo(context.Background(), templateOwner, templateRepo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.GenerateRepo``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GenerateRepo`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.GenerateRepo`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**templateOwner** | **string** | name of the template repository owner | 
**templateRepo** | **string** | name of the template repository | 

### Other Parameters

Other parameters are passed through a pointer to a apiGenerateRepoRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**GenerateRepoOption**](GenerateRepoOption.md) |  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAnnotatedTag

> AnnotatedTag GetAnnotatedTag(ctx, owner, repo, sha).Execute()

Gets the tag object of an annotated tag (not lightweight tags)

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.GetAnnotatedTag(context.Background(), owner, repo, sha).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.GetAnnotatedTag``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetAnnotatedTag`: AnnotatedTag
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.GetAnnotatedTag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAnnotatedTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**AnnotatedTag**](AnnotatedTag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetBlob

> GitBlobResponse GetBlob(ctx, owner, repo, sha).Execute()

Gets the blob of a repository.

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | sha of the commit

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.GetBlob(context.Background(), owner, repo, sha).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.GetBlob``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetBlob`: GitBlobResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.GetBlob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | sha of the commit | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetBlobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**GitBlobResponse**](GitBlobResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTree

> GitTreeResponse GetTree(ctx, owner, repo, sha).Recursive(recursive).Page(page).PerPage(perPage).Execute()

Gets the tree of a repository.

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | sha of the commit
    recursive := true // bool | show all directories and files (optional)
    page := int32(56) // int32 | page number; the 'truncated' field in the response will be true if there are still more items after this page, false if the last page (optional)
    perPage := int32(56) // int32 | number of items per page (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.GetTree(context.Background(), owner, repo, sha).Recursive(recursive).Page(page).PerPage(perPage).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.GetTree``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetTree`: GitTreeResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.GetTree`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | sha of the commit | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTreeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **recursive** | **bool** | show all directories and files | 
 **page** | **int32** | page number; the &#39;truncated&#39; field in the response will be true if there are still more items after this page, false if the last page | 
 **perPage** | **int32** | number of items per page | 

### Return type

[**GitTreeResponse**](GitTreeResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListForks

> []Repository ListForks(ctx, owner, repo).Page(page).Limit(limit).Execute()

List a repository's forks

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.ListForks(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.ListForks``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `ListForks`: []Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.ListForks`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiListForksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RejectRepoTransfer

> Repository RejectRepoTransfer(ctx, owner, repo).Execute()

Reject a repo transfer

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to transfer
    repo := "repo_example" // string | name of the repo to transfer

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RejectRepoTransfer(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RejectRepoTransfer``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RejectRepoTransfer`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RejectRepoTransfer`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to transfer | 
**repo** | **string** | name of the repo to transfer | 

### Other Parameters

Other parameters are passed through a pointer to a apiRejectRepoTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoAddCollaborator

> RepoAddCollaborator(ctx, owner, repo, collaborator).Body(body).Execute()

Add a collaborator to a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    collaborator := "collaborator_example" // string | username of the collaborator to add
    body := *openapiclient.NewAddCollaboratorOption() // AddCollaboratorOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoAddCollaborator(context.Background(), owner, repo, collaborator).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoAddCollaborator``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**collaborator** | **string** | username of the collaborator to add | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoAddCollaboratorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**AddCollaboratorOption**](AddCollaboratorOption.md) |  | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoAddPushMirror

> PushMirror RepoAddPushMirror(ctx, owner, repo).Body(body).Execute()

add a push mirror to the repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreatePushMirrorOption() // CreatePushMirrorOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoAddPushMirror(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoAddPushMirror``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoAddPushMirror`: PushMirror
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoAddPushMirror`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoAddPushMirrorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreatePushMirrorOption**](CreatePushMirrorOption.md) |  | 

### Return type

[**PushMirror**](PushMirror.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoAddTeam

> RepoAddTeam(ctx, owner, repo, team).Execute()

Add a team to a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    team := "team_example" // string | team name

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoAddTeam(context.Background(), owner, repo, team).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoAddTeam``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**team** | **string** | team name | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoAddTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoAddTopic

> RepoAddTopic(ctx, owner, repo, topic).Execute()

Add a topic to a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    topic := "topic_example" // string | name of the topic to add

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoAddTopic(context.Background(), owner, repo, topic).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoAddTopic``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**topic** | **string** | name of the topic to add | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoAddTopicRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoApplyDiffPatch

> FileResponse RepoApplyDiffPatch(ctx, owner, repo).Body(body).Execute()

Apply diff patch to repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewUpdateFileOptions("Content_example", "Sha_example") // UpdateFileOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoApplyDiffPatch(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoApplyDiffPatch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoApplyDiffPatch`: FileResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoApplyDiffPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoApplyDiffPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**UpdateFileOptions**](UpdateFileOptions.md) |  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCancelScheduledAutoMerge

> RepoCancelScheduledAutoMerge(ctx, owner, repo, index).Execute()

Cancel the scheduled auto merge for the given pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to merge

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCancelScheduledAutoMerge(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCancelScheduledAutoMerge``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to merge | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCancelScheduledAutoMergeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoChangeFiles

> FilesResponse RepoChangeFiles(ctx, owner, repo).Body(body).Execute()

Modify multiple files in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewChangeFilesOptions([]openapiclient.ChangeFileOperation{*openapiclient.NewChangeFileOperation("Operation_example", "Path_example")}) // ChangeFilesOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoChangeFiles(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoChangeFiles``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoChangeFiles`: FilesResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoChangeFiles`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoChangeFilesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**ChangeFilesOptions**](ChangeFilesOptions.md) |  | 

### Return type

[**FilesResponse**](FilesResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCheckCollaborator

> RepoCheckCollaborator(ctx, owner, repo, collaborator).Execute()

Check if a user is a collaborator of a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    collaborator := "collaborator_example" // string | username of the collaborator

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCheckCollaborator(context.Background(), owner, repo, collaborator).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCheckCollaborator``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**collaborator** | **string** | username of the collaborator | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCheckCollaboratorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCheckTeam

> Team RepoCheckTeam(ctx, owner, repo, team).Execute()

Check if a team is assigned to a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    team := "team_example" // string | team name

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCheckTeam(context.Background(), owner, repo, team).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCheckTeam``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCheckTeam`: Team
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCheckTeam`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**team** | **string** | team name | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCheckTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateBranch

> Branch RepoCreateBranch(ctx, owner, repo).Body(body).Execute()

Create a branch

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateBranchRepoOption("NewBranchName_example") // CreateBranchRepoOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateBranch(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateBranch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateBranch`: Branch
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateBranch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateBranchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateBranchRepoOption**](CreateBranchRepoOption.md) |  | 

### Return type

[**Branch**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateBranchProtection

> BranchProtection RepoCreateBranchProtection(ctx, owner, repo).Body(body).Execute()

Create a branch protections for a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateBranchProtectionOption() // CreateBranchProtectionOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateBranchProtection(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateBranchProtection``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateBranchProtection`: BranchProtection
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateBranchProtection`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateBranchProtectionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateBranchProtectionOption**](CreateBranchProtectionOption.md) |  | 

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateFile

> FileResponse RepoCreateFile(ctx, owner, repo, filepath).Body(body).Execute()

Create a file in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | path of the file to create
    body := *openapiclient.NewCreateFileOptions("Content_example") // CreateFileOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateFile(context.Background(), owner, repo, filepath).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateFile``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateFile`: FileResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateFile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | path of the file to create | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**CreateFileOptions**](CreateFileOptions.md) |  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateHook

> Hook RepoCreateHook(ctx, owner, repo).Body(body).Execute()

Create a hook

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateHookOption(map[string]string{"key": "Inner_example"}, "Type_example") // CreateHookOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateHook(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateHook`: Hook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateHook`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateHookOption**](CreateHookOption.md) |  | 

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateKey

> DeployKey RepoCreateKey(ctx, owner, repo).Body(body).Execute()

Add a key to a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateKeyOption("Key_example", "Title_example") // CreateKeyOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateKey(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateKey``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateKey`: DeployKey
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateKeyOption**](CreateKeyOption.md) |  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreatePullRequest

> PullRequest RepoCreatePullRequest(ctx, owner, repo).Body(body).Execute()

Create a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreatePullRequestOption() // CreatePullRequestOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreatePullRequest(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreatePullRequest``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreatePullRequest`: PullRequest
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreatePullRequest`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreatePullRequestRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreatePullRequestOption**](CreatePullRequestOption.md) |  | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreatePullReview

> PullReview RepoCreatePullReview(ctx, owner, repo, index).Body(body).Execute()

Create a review to an pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    body := *openapiclient.NewCreatePullReviewOptions() // CreatePullReviewOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreatePullReview(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreatePullReview``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreatePullReview`: PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreatePullReview`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreatePullReviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**CreatePullReviewOptions**](CreatePullReviewOptions.md) |  | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreatePullReviewRequests

> []PullReview RepoCreatePullReviewRequests(ctx, owner, repo, index).Body(body).Execute()

create review requests for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    body := *openapiclient.NewPullReviewRequestOptions() // PullReviewRequestOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreatePullReviewRequests(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreatePullReviewRequests``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreatePullReviewRequests`: []PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreatePullReviewRequests`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreatePullReviewRequestsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**PullReviewRequestOptions**](PullReviewRequestOptions.md) |  | 

### Return type

[**[]PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateRelease

> Release RepoCreateRelease(ctx, owner, repo).Body(body).Execute()

Create a release

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateReleaseOption("TagName_example") // CreateReleaseOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateRelease(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateRelease``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateRelease`: Release
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateRelease`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateReleaseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateReleaseOption**](CreateReleaseOption.md) |  | 

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateReleaseAttachment

> Attachment RepoCreateReleaseAttachment(ctx, owner, repo, id).Attachment(attachment).Name(name).Execute()

Create a release attachment

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release
    attachment := os.NewFile(1234, "some_file") // *os.File | attachment to upload
    name := "name_example" // string | name of the attachment (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateReleaseAttachment(context.Background(), owner, repo, id).Attachment(attachment).Name(name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateReleaseAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateReleaseAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateReleaseAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateReleaseAttachmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **attachment** | ***os.File** | attachment to upload | 
 **name** | **string** | name of the attachment | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateStatus

> CommitStatus RepoCreateStatus(ctx, owner, repo, sha).Body(body).Execute()

Create a commit status

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | sha of the commit
    body := *openapiclient.NewCreateStatusOption() // CreateStatusOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateStatus(context.Background(), owner, repo, sha).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateStatus``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateStatus`: CommitStatus
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateStatus`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | sha of the commit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**CreateStatusOption**](CreateStatusOption.md) |  | 

### Return type

[**CommitStatus**](CommitStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateTag

> Tag RepoCreateTag(ctx, owner, repo).Body(body).Execute()

Create a new git tag in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateTagOption("TagName_example") // CreateTagOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateTag(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateTag``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateTag`: Tag
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateTag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateTagOption**](CreateTagOption.md) |  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoCreateWikiPage

> WikiPage RepoCreateWikiPage(ctx, owner, repo).Body(body).Execute()

Create a wiki page

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewCreateWikiPageOptions() // CreateWikiPageOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoCreateWikiPage(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoCreateWikiPage``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoCreateWikiPage`: WikiPage
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoCreateWikiPage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoCreateWikiPageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateWikiPageOptions**](CreateWikiPageOptions.md) |  | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDelete

> RepoDelete(ctx, owner, repo).Execute()

Delete a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to delete
    repo := "repo_example" // string | name of the repo to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDelete(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDelete``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to delete | 
**repo** | **string** | name of the repo to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteAvatar

> RepoDeleteAvatar(ctx, owner, repo).Execute()

Delete avatar

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteAvatar(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteAvatar``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteAvatarRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteBranch

> RepoDeleteBranch(ctx, owner, repo, branch).Execute()

Delete a specific branch from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    branch := "branch_example" // string | branch to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteBranch(context.Background(), owner, repo, branch).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteBranch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**branch** | **string** | branch to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteBranchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteBranchProtection

> RepoDeleteBranchProtection(ctx, owner, repo, name).Execute()

Delete a specific branch protection for the repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    name := "name_example" // string | name of protected branch

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteBranchProtection(context.Background(), owner, repo, name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteBranchProtection``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**name** | **string** | name of protected branch | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteBranchProtectionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteCollaborator

> RepoDeleteCollaborator(ctx, owner, repo, collaborator).Execute()

Delete a collaborator from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    collaborator := "collaborator_example" // string | username of the collaborator to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteCollaborator(context.Background(), owner, repo, collaborator).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteCollaborator``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**collaborator** | **string** | username of the collaborator to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteCollaboratorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteFile

> FileDeleteResponse RepoDeleteFile(ctx, owner, repo, filepath).Body(body).Execute()

Delete a file in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | path of the file to delete
    body := *openapiclient.NewDeleteFileOptions("Sha_example") // DeleteFileOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteFile(context.Background(), owner, repo, filepath).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteFile``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoDeleteFile`: FileDeleteResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoDeleteFile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | path of the file to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**DeleteFileOptions**](DeleteFileOptions.md) |  | 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteGitHook

> RepoDeleteGitHook(ctx, owner, repo, id).Execute()

Delete a Git hook in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := "id_example" // string | id of the hook to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteGitHook(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteGitHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **string** | id of the hook to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteGitHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteHook

> RepoDeleteHook(ctx, owner, repo, id).Execute()

Delete a hook in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the hook to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteHook(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the hook to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteKey

> RepoDeleteKey(ctx, owner, repo, id).Execute()

Delete a key from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the key to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteKey(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteKey``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the key to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeletePullReview

> RepoDeletePullReview(ctx, owner, repo, index, id).Execute()

Delete a specific review from a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    id := int64(789) // int64 | id of the review

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeletePullReview(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeletePullReview``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 
**id** | **int64** | id of the review | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeletePullReviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeletePullReviewRequests

> RepoDeletePullReviewRequests(ctx, owner, repo, index).Body(body).Execute()

cancel review requests for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    body := *openapiclient.NewPullReviewRequestOptions() // PullReviewRequestOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeletePullReviewRequests(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeletePullReviewRequests``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeletePullReviewRequestsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**PullReviewRequestOptions**](PullReviewRequestOptions.md) |  | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeletePushMirror

> RepoDeletePushMirror(ctx, owner, repo, name).Execute()

deletes a push mirror from a repository by remoteName

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    name := "name_example" // string | remote name of the pushMirror

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeletePushMirror(context.Background(), owner, repo, name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeletePushMirror``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**name** | **string** | remote name of the pushMirror | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeletePushMirrorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteRelease

> RepoDeleteRelease(ctx, owner, repo, id).Execute()

Delete a release

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteRelease(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteRelease``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteReleaseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteReleaseAttachment

> RepoDeleteReleaseAttachment(ctx, owner, repo, id, attachmentId).Execute()

Delete a release attachment

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release
    attachmentId := int64(789) // int64 | id of the attachment to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteReleaseAttachment(context.Background(), owner, repo, id, attachmentId).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteReleaseAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release | 
**attachmentId** | **int64** | id of the attachment to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteReleaseAttachmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteReleaseByTag

> RepoDeleteReleaseByTag(ctx, owner, repo, tag).Execute()

Delete a release by tag name

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    tag := "tag_example" // string | tag name of the release to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteReleaseByTag(context.Background(), owner, repo, tag).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteReleaseByTag``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**tag** | **string** | tag name of the release to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteReleaseByTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteTag

> RepoDeleteTag(ctx, owner, repo, tag).Execute()

Delete a repository's tag by name

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    tag := "tag_example" // string | name of tag to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteTag(context.Background(), owner, repo, tag).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteTag``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**tag** | **string** | name of tag to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteTeam

> RepoDeleteTeam(ctx, owner, repo, team).Execute()

Delete a team from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    team := "team_example" // string | team name

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteTeam(context.Background(), owner, repo, team).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteTeam``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**team** | **string** | team name | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteTopic

> RepoDeleteTopic(ctx, owner, repo, topic).Execute()

Delete a topic from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    topic := "topic_example" // string | name of the topic to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteTopic(context.Background(), owner, repo, topic).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteTopic``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**topic** | **string** | name of the topic to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteTopicRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDeleteWikiPage

> RepoDeleteWikiPage(ctx, owner, repo, pageName).Execute()

Delete a wiki page

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    pageName := "pageName_example" // string | name of the page

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDeleteWikiPage(context.Background(), owner, repo, pageName).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDeleteWikiPage``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**pageName** | **string** | name of the page | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDeleteWikiPageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDismissPullReview

> PullReview RepoDismissPullReview(ctx, owner, repo, index, id).Body(body).Execute()

Dismiss a review for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    id := int64(789) // int64 | id of the review
    body := *openapiclient.NewDismissPullReviewOptions() // DismissPullReviewOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDismissPullReview(context.Background(), owner, repo, index, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDismissPullReview``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoDismissPullReview`: PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoDismissPullReview`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 
**id** | **int64** | id of the review | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDismissPullReviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **body** | [**DismissPullReviewOptions**](DismissPullReviewOptions.md) |  | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDownloadCommitDiffOrPatch

> string RepoDownloadCommitDiffOrPatch(ctx, owner, repo, sha, diffType).Execute()

Get a commit's diff or patch

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | SHA of the commit to get
    diffType := "diffType_example" // string | whether the output is diff or patch

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDownloadCommitDiffOrPatch(context.Background(), owner, repo, sha, diffType).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDownloadCommitDiffOrPatch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoDownloadCommitDiffOrPatch`: string
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoDownloadCommitDiffOrPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | SHA of the commit to get | 
**diffType** | **string** | whether the output is diff or patch | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDownloadCommitDiffOrPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

**string**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoDownloadPullDiffOrPatch

> string RepoDownloadPullDiffOrPatch(ctx, owner, repo, index, diffType).Binary(binary).Execute()

Get a pull request diff or patch

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to get
    diffType := "diffType_example" // string | whether the output is diff or patch
    binary := true // bool | whether to include binary file changes. if true, the diff is applicable with `git apply` (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoDownloadPullDiffOrPatch(context.Background(), owner, repo, index, diffType).Binary(binary).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoDownloadPullDiffOrPatch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoDownloadPullDiffOrPatch`: string
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoDownloadPullDiffOrPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to get | 
**diffType** | **string** | whether the output is diff or patch | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoDownloadPullDiffOrPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **binary** | **bool** | whether to include binary file changes. if true, the diff is applicable with &#x60;git apply&#x60; | 

### Return type

**string**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEdit

> Repository RepoEdit(ctx, owner, repo).Body(body).Execute()

Edit a repository's properties. Only fields that are set will be changed.

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to edit
    repo := "repo_example" // string | name of the repo to edit
    body := *openapiclient.NewEditRepoOption() // EditRepoOption | Properties of a repo that you can edit (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEdit(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEdit``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEdit`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEdit`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to edit | 
**repo** | **string** | name of the repo to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**EditRepoOption**](EditRepoOption.md) | Properties of a repo that you can edit | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditBranchProtection

> BranchProtection RepoEditBranchProtection(ctx, owner, repo, name).Body(body).Execute()

Edit a branch protections for a repository. Only fields that are set will be changed

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    name := "name_example" // string | name of protected branch
    body := *openapiclient.NewEditBranchProtectionOption() // EditBranchProtectionOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditBranchProtection(context.Background(), owner, repo, name).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditBranchProtection``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditBranchProtection`: BranchProtection
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditBranchProtection`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**name** | **string** | name of protected branch | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditBranchProtectionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditBranchProtectionOption**](EditBranchProtectionOption.md) |  | 

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditGitHook

> GitHook RepoEditGitHook(ctx, owner, repo, id).Body(body).Execute()

Edit a Git hook in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := "id_example" // string | id of the hook to get
    body := *openapiclient.NewEditGitHookOption() // EditGitHookOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditGitHook(context.Background(), owner, repo, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditGitHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditGitHook`: GitHook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditGitHook`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **string** | id of the hook to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditGitHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditGitHookOption**](EditGitHookOption.md) |  | 

### Return type

[**GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditHook

> Hook RepoEditHook(ctx, owner, repo, id).Body(body).Execute()

Edit a hook in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | index of the hook
    body := *openapiclient.NewEditHookOption() // EditHookOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditHook(context.Background(), owner, repo, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditHook`: Hook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditHook`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | index of the hook | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditHookOption**](EditHookOption.md) |  | 

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditPullRequest

> PullRequest RepoEditPullRequest(ctx, owner, repo, index).Body(body).Execute()

Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to edit
    body := *openapiclient.NewEditPullRequestOption() // EditPullRequestOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditPullRequest(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditPullRequest``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditPullRequest`: PullRequest
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditPullRequest`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditPullRequestRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditPullRequestOption**](EditPullRequestOption.md) |  | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditRelease

> Release RepoEditRelease(ctx, owner, repo, id).Body(body).Execute()

Update a release

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release to edit
    body := *openapiclient.NewEditReleaseOption() // EditReleaseOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditRelease(context.Background(), owner, repo, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditRelease``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditRelease`: Release
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditRelease`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditReleaseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditReleaseOption**](EditReleaseOption.md) |  | 

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditReleaseAttachment

> Attachment RepoEditReleaseAttachment(ctx, owner, repo, id, attachmentId).Body(body).Execute()

Edit a release attachment

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release
    attachmentId := int64(789) // int64 | id of the attachment to edit
    body := *openapiclient.NewEditAttachmentOptions() // EditAttachmentOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditReleaseAttachment(context.Background(), owner, repo, id, attachmentId).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditReleaseAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditReleaseAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditReleaseAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release | 
**attachmentId** | **int64** | id of the attachment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditReleaseAttachmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **body** | [**EditAttachmentOptions**](EditAttachmentOptions.md) |  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoEditWikiPage

> WikiPage RepoEditWikiPage(ctx, owner, repo, pageName).Body(body).Execute()

Edit a wiki page

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    pageName := "pageName_example" // string | name of the page
    body := *openapiclient.NewCreateWikiPageOptions() // CreateWikiPageOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoEditWikiPage(context.Background(), owner, repo, pageName).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoEditWikiPage``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoEditWikiPage`: WikiPage
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoEditWikiPage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**pageName** | **string** | name of the page | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoEditWikiPageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**CreateWikiPageOptions**](CreateWikiPageOptions.md) |  | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGet

> Repository RepoGet(ctx, owner, repo).Execute()

Get a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGet(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGet`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetAllCommits

> []Commit RepoGetAllCommits(ctx, owner, repo).Sha(sha).Path(path).Stat(stat).Verification(verification).Files(files).Page(page).Limit(limit).Not(not).Execute()

Get a list of all commits from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | SHA or branch to start listing commits from (usually 'master') (optional)
    path := "path_example" // string | filepath of a file/dir (optional)
    stat := true // bool | include diff stats for every commit (disable for speedup, default 'true') (optional)
    verification := true // bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files := true // bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (ignored if used with 'path') (optional)
    not := "not_example" // string | commits that match the given specifier will not be listed. (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetAllCommits(context.Background(), owner, repo).Sha(sha).Path(path).Stat(stat).Verification(verification).Files(files).Page(page).Limit(limit).Not(not).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetAllCommits``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetAllCommits`: []Commit
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetAllCommits`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetAllCommitsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **sha** | **string** | SHA or branch to start listing commits from (usually &#39;master&#39;) | 
 **path** | **string** | filepath of a file/dir | 
 **stat** | **bool** | include diff stats for every commit (disable for speedup, default &#39;true&#39;) | 
 **verification** | **bool** | include verification for every commit (disable for speedup, default &#39;true&#39;) | 
 **files** | **bool** | include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results (ignored if used with &#39;path&#39;) | 
 **not** | **string** | commits that match the given specifier will not be listed. | 

### Return type

[**[]Commit**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetArchive

> RepoGetArchive(ctx, owner, repo, archive).Execute()

Get an archive of a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    archive := "archive_example" // string | the git reference for download with attached archive format (e.g. master.zip)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetArchive(context.Background(), owner, repo, archive).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetArchive``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**archive** | **string** | the git reference for download with attached archive format (e.g. master.zip) | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetArchiveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetAssignees

> []User RepoGetAssignees(ctx, owner, repo).Execute()

Return all users that have write access and can be assigned to issues

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetAssignees(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetAssignees``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetAssignees`: []User
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetAssignees`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetAssigneesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetBranch

> Branch RepoGetBranch(ctx, owner, repo, branch).Execute()

Retrieve a specific branch from a repository, including its effective branch protection

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    branch := "branch_example" // string | branch to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetBranch(context.Background(), owner, repo, branch).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetBranch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetBranch`: Branch
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetBranch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**branch** | **string** | branch to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetBranchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Branch**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetBranchProtection

> BranchProtection RepoGetBranchProtection(ctx, owner, repo, name).Execute()

Get a specific branch protection for the repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    name := "name_example" // string | name of protected branch

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetBranchProtection(context.Background(), owner, repo, name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetBranchProtection``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetBranchProtection`: BranchProtection
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetBranchProtection`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**name** | **string** | name of protected branch | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetBranchProtectionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetByID

> Repository RepoGetByID(ctx, id).Execute()

Get a repository by id

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    id := int64(789) // int64 | id of the repo to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetByID(context.Background(), id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetByID``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetByID`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetByID`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int64** | id of the repo to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetByIDRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetCombinedStatusByRef

> CombinedStatus RepoGetCombinedStatusByRef(ctx, owner, repo, ref).Page(page).Limit(limit).Execute()

Get a commit's combined status, by branch/tag/commit reference

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    ref := "ref_example" // string | name of branch/tag/commit
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetCombinedStatusByRef(context.Background(), owner, repo, ref).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetCombinedStatusByRef``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetCombinedStatusByRef`: CombinedStatus
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetCombinedStatusByRef`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**ref** | **string** | name of branch/tag/commit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetCombinedStatusByRefRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**CombinedStatus**](CombinedStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetContents

> ContentsResponse RepoGetContents(ctx, owner, repo, filepath).Ref(ref).Execute()

Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | path of the dir, file, symlink or submodule in the repo
    ref := "ref_example" // string | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetContents(context.Background(), owner, repo, filepath).Ref(ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetContents``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetContents`: ContentsResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetContents`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | path of the dir, file, symlink or submodule in the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetContentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ref** | **string** | The name of the commit/branch/tag. Default the repository’s default branch (usually master) | 

### Return type

[**ContentsResponse**](ContentsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetContentsList

> []ContentsResponse RepoGetContentsList(ctx, owner, repo).Ref(ref).Execute()

Gets the metadata of all the entries of the root dir

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    ref := "ref_example" // string | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetContentsList(context.Background(), owner, repo).Ref(ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetContentsList``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetContentsList`: []ContentsResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetContentsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetContentsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ref** | **string** | The name of the commit/branch/tag. Default the repository’s default branch (usually master) | 

### Return type

[**[]ContentsResponse**](ContentsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetEditorConfig

> RepoGetEditorConfig(ctx, owner, repo, filepath).Ref(ref).Execute()

Get the EditorConfig definitions of a file in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | filepath of file to get
    ref := "ref_example" // string | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetEditorConfig(context.Background(), owner, repo, filepath).Ref(ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetEditorConfig``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | filepath of file to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetEditorConfigRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ref** | **string** | The name of the commit/branch/tag. Default the repository’s default branch (usually master) | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetGitHook

> GitHook RepoGetGitHook(ctx, owner, repo, id).Execute()

Get a Git hook

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := "id_example" // string | id of the hook to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetGitHook(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetGitHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetGitHook`: GitHook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetGitHook`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **string** | id of the hook to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetGitHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetHook

> Hook RepoGetHook(ctx, owner, repo, id).Execute()

Get a hook

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the hook to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetHook(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetHook`: Hook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetHook`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the hook to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetIssueConfig

> IssueConfig RepoGetIssueConfig(ctx, owner, repo).Execute()

Returns the issue config for a repo

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetIssueConfig(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetIssueConfig``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetIssueConfig`: IssueConfig
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetIssueConfig`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetIssueConfigRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**IssueConfig**](IssueConfig.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetIssueTemplates

> []IssueTemplate RepoGetIssueTemplates(ctx, owner, repo).Execute()

Get available issue templates for a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetIssueTemplates(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetIssueTemplates``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetIssueTemplates`: []IssueTemplate
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetIssueTemplates`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetIssueTemplatesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]IssueTemplate**](IssueTemplate.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetKey

> DeployKey RepoGetKey(ctx, owner, repo, id).Execute()

Get a repository's key by id

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the key to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetKey(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetKey``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetKey`: DeployKey
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the key to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetLanguages

> map[string]int64 RepoGetLanguages(ctx, owner, repo).Execute()

Get languages and number of bytes of code written

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetLanguages(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetLanguages``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetLanguages`: map[string]int64
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetLanguages`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetLanguagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

**map[string]int64**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetLatestRelease

> Release RepoGetLatestRelease(ctx, owner, repo).Execute()

Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetLatestRelease(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetLatestRelease``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetLatestRelease`: Release
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetLatestRelease`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetLatestReleaseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetNote

> Note RepoGetNote(ctx, owner, repo, sha).Verification(verification).Files(files).Execute()

Get a note corresponding to a single commit from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | a git ref or commit sha
    verification := true // bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files := true // bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetNote(context.Background(), owner, repo, sha).Verification(verification).Files(files).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetNote``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetNote`: Note
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | a git ref or commit sha | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **verification** | **bool** | include verification for every commit (disable for speedup, default &#39;true&#39;) | 
 **files** | **bool** | include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | 

### Return type

[**Note**](Note.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetPullRequest

> PullRequest RepoGetPullRequest(ctx, owner, repo, index).Execute()

Get a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetPullRequest(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetPullRequest``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetPullRequest`: PullRequest
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetPullRequest`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetPullRequestRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetPullRequestCommits

> []Commit RepoGetPullRequestCommits(ctx, owner, repo, index).Page(page).Limit(limit).Verification(verification).Files(files).Execute()

Get commits for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to get
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)
    verification := true // bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files := true // bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetPullRequestCommits(context.Background(), owner, repo, index).Page(page).Limit(limit).Verification(verification).Files(files).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetPullRequestCommits``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetPullRequestCommits`: []Commit
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetPullRequestCommits`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetPullRequestCommitsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 
 **verification** | **bool** | include verification for every commit (disable for speedup, default &#39;true&#39;) | 
 **files** | **bool** | include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | 

### Return type

[**[]Commit**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetPullRequestFiles

> []ChangedFile RepoGetPullRequestFiles(ctx, owner, repo, index).SkipTo(skipTo).Whitespace(whitespace).Page(page).Limit(limit).Execute()

Get changed files for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to get
    skipTo := "skipTo_example" // string | skip to given file (optional)
    whitespace := "whitespace_example" // string | whitespace behavior (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetPullRequestFiles(context.Background(), owner, repo, index).SkipTo(skipTo).Whitespace(whitespace).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetPullRequestFiles``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetPullRequestFiles`: []ChangedFile
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetPullRequestFiles`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetPullRequestFilesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **skipTo** | **string** | skip to given file | 
 **whitespace** | **string** | whitespace behavior | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]ChangedFile**](ChangedFile.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetPullReview

> PullReview RepoGetPullReview(ctx, owner, repo, index, id).Execute()

Get a specific review for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    id := int64(789) // int64 | id of the review

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetPullReview(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetPullReview``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetPullReview`: PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetPullReview`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 
**id** | **int64** | id of the review | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetPullReviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetPullReviewComments

> []PullReviewComment RepoGetPullReviewComments(ctx, owner, repo, index, id).Execute()

Get a specific review for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    id := int64(789) // int64 | id of the review

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetPullReviewComments(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetPullReviewComments``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetPullReviewComments`: []PullReviewComment
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetPullReviewComments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 
**id** | **int64** | id of the review | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetPullReviewCommentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**[]PullReviewComment**](PullReviewComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetPushMirrorByRemoteName

> PushMirror RepoGetPushMirrorByRemoteName(ctx, owner, repo, name).Execute()

Get push mirror of the repository by remoteName

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    name := "name_example" // string | remote name of push mirror

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetPushMirrorByRemoteName(context.Background(), owner, repo, name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetPushMirrorByRemoteName``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetPushMirrorByRemoteName`: PushMirror
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetPushMirrorByRemoteName`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**name** | **string** | remote name of push mirror | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetPushMirrorByRemoteNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**PushMirror**](PushMirror.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetRawFile

> RepoGetRawFile(ctx, owner, repo, filepath).Ref(ref).Execute()

Get a file from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | filepath of the file to get
    ref := "ref_example" // string | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetRawFile(context.Background(), owner, repo, filepath).Ref(ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetRawFile``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | filepath of the file to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetRawFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ref** | **string** | The name of the commit/branch/tag. Default the repository’s default branch (usually master) | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetRawFileOrLFS

> RepoGetRawFileOrLFS(ctx, owner, repo, filepath).Ref(ref).Execute()

Get a file or it's LFS object from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | filepath of the file to get
    ref := "ref_example" // string | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetRawFileOrLFS(context.Background(), owner, repo, filepath).Ref(ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetRawFileOrLFS``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | filepath of the file to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetRawFileOrLFSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ref** | **string** | The name of the commit/branch/tag. Default the repository’s default branch (usually master) | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetRelease

> Release RepoGetRelease(ctx, owner, repo, id).Execute()

Get a release

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetRelease(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetRelease``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetRelease`: Release
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetRelease`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetReleaseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetReleaseAttachment

> Attachment RepoGetReleaseAttachment(ctx, owner, repo, id, attachmentId).Execute()

Get a release attachment

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release
    attachmentId := int64(789) // int64 | id of the attachment to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetReleaseAttachment(context.Background(), owner, repo, id, attachmentId).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetReleaseAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetReleaseAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetReleaseAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release | 
**attachmentId** | **int64** | id of the attachment to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetReleaseAttachmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetReleaseByTag

> Release RepoGetReleaseByTag(ctx, owner, repo, tag).Execute()

Get a release by tag name

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    tag := "tag_example" // string | tag name of the release to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetReleaseByTag(context.Background(), owner, repo, tag).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetReleaseByTag``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetReleaseByTag`: Release
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetReleaseByTag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**tag** | **string** | tag name of the release to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetReleaseByTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetRepoPermissions

> RepoCollaboratorPermission RepoGetRepoPermissions(ctx, owner, repo, collaborator).Execute()

Get repository permissions for a user

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    collaborator := "collaborator_example" // string | username of the collaborator

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetRepoPermissions(context.Background(), owner, repo, collaborator).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetRepoPermissions``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetRepoPermissions`: RepoCollaboratorPermission
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetRepoPermissions`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**collaborator** | **string** | username of the collaborator | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetRepoPermissionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**RepoCollaboratorPermission**](RepoCollaboratorPermission.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetReviewers

> []User RepoGetReviewers(ctx, owner, repo).Execute()

Return all users that can be requested to review in this repo

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetReviewers(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetReviewers``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetReviewers`: []User
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetReviewers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetReviewersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetRunnerRegistrationToken

> RepoGetRunnerRegistrationToken(ctx, owner, repo).Execute()

Get a repository's actions runner registration token

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetRunnerRegistrationToken(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetRunnerRegistrationToken``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetRunnerRegistrationTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetSingleCommit

> Commit RepoGetSingleCommit(ctx, owner, repo, sha).Stat(stat).Verification(verification).Files(files).Execute()

Get a single commit from a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | a git ref or commit sha
    stat := true // bool | include diff stats for every commit (disable for speedup, default 'true') (optional)
    verification := true // bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files := true // bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetSingleCommit(context.Background(), owner, repo, sha).Stat(stat).Verification(verification).Files(files).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetSingleCommit``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetSingleCommit`: Commit
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetSingleCommit`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | a git ref or commit sha | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetSingleCommitRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **stat** | **bool** | include diff stats for every commit (disable for speedup, default &#39;true&#39;) | 
 **verification** | **bool** | include verification for every commit (disable for speedup, default &#39;true&#39;) | 
 **files** | **bool** | include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | 

### Return type

[**Commit**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetTag

> Tag RepoGetTag(ctx, owner, repo, tag).Execute()

Get the tag of a repository by tag name

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    tag := "tag_example" // string | name of tag

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetTag(context.Background(), owner, repo, tag).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetTag``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetTag`: Tag
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetTag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**tag** | **string** | name of tag | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Tag**](Tag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetWikiPage

> WikiPage RepoGetWikiPage(ctx, owner, repo, pageName).Execute()

Get a wiki page

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    pageName := "pageName_example" // string | name of the page

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetWikiPage(context.Background(), owner, repo, pageName).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetWikiPage``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetWikiPage`: WikiPage
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetWikiPage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**pageName** | **string** | name of the page | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetWikiPageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetWikiPageRevisions

> WikiCommitList RepoGetWikiPageRevisions(ctx, owner, repo, pageName).Page(page).Execute()

Get revisions of a wiki page

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    pageName := "pageName_example" // string | name of the page
    page := int32(56) // int32 | page number of results to return (1-based) (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetWikiPageRevisions(context.Background(), owner, repo, pageName).Page(page).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetWikiPageRevisions``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetWikiPageRevisions`: WikiCommitList
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetWikiPageRevisions`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**pageName** | **string** | name of the page | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetWikiPageRevisionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 

### Return type

[**WikiCommitList**](WikiCommitList.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoGetWikiPages

> []WikiPageMetaData RepoGetWikiPages(ctx, owner, repo).Page(page).Limit(limit).Execute()

Get all wiki pages

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoGetWikiPages(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoGetWikiPages``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoGetWikiPages`: []WikiPageMetaData
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoGetWikiPages`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoGetWikiPagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]WikiPageMetaData**](WikiPageMetaData.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListActivityFeeds

> []Activity RepoListActivityFeeds(ctx, owner, repo).Date(date).Page(page).Limit(limit).Execute()

List a repository's activity feeds

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    "time"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    date := time.Now() // string | the date of the activities to be found (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListActivityFeeds(context.Background(), owner, repo).Date(date).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListActivityFeeds``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListActivityFeeds`: []Activity
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListActivityFeeds`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListActivityFeedsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **date** | **string** | the date of the activities to be found | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Activity**](Activity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListAllGitRefs

> []Reference RepoListAllGitRefs(ctx, owner, repo).Execute()

Get specified ref or filtered repository's refs

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListAllGitRefs(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListAllGitRefs``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListAllGitRefs`: []Reference
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListAllGitRefs`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListAllGitRefsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]Reference**](Reference.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListBranchProtection

> []BranchProtection RepoListBranchProtection(ctx, owner, repo).Execute()

List branch protections for a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListBranchProtection(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListBranchProtection``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListBranchProtection`: []BranchProtection
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListBranchProtection`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListBranchProtectionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListBranches

> []Branch RepoListBranches(ctx, owner, repo).Page(page).Limit(limit).Execute()

List a repository's branches

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListBranches(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListBranches``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListBranches`: []Branch
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListBranches`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListBranchesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Branch**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListCollaborators

> []User RepoListCollaborators(ctx, owner, repo).Page(page).Limit(limit).Execute()

List a repository's collaborators

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListCollaborators(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListCollaborators``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListCollaborators`: []User
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListCollaborators`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListCollaboratorsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListGitHooks

> []GitHook RepoListGitHooks(ctx, owner, repo).Execute()

List the Git hooks in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListGitHooks(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListGitHooks``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListGitHooks`: []GitHook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListGitHooks`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListGitHooksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListGitRefs

> []Reference RepoListGitRefs(ctx, owner, repo, ref).Execute()

Get specified ref or filtered repository's refs

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    ref := "ref_example" // string | part or full name of the ref

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListGitRefs(context.Background(), owner, repo, ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListGitRefs``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListGitRefs`: []Reference
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListGitRefs`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**ref** | **string** | part or full name of the ref | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListGitRefsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**[]Reference**](Reference.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListHooks

> []Hook RepoListHooks(ctx, owner, repo).Page(page).Limit(limit).Execute()

List the hooks in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListHooks(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListHooks``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListHooks`: []Hook
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListHooks`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListHooksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListKeys

> []DeployKey RepoListKeys(ctx, owner, repo).KeyId(keyId).Fingerprint(fingerprint).Page(page).Limit(limit).Execute()

List a repository's keys

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    keyId := int32(56) // int32 | the key_id to search for (optional)
    fingerprint := "fingerprint_example" // string | fingerprint of the key (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListKeys(context.Background(), owner, repo).KeyId(keyId).Fingerprint(fingerprint).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListKeys``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListKeys`: []DeployKey
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListKeys`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListKeysRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **keyId** | **int32** | the key_id to search for | 
 **fingerprint** | **string** | fingerprint of the key | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListPinnedIssues

> []Issue RepoListPinnedIssues(ctx, owner, repo).Execute()

List a repo's pinned issues

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListPinnedIssues(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListPinnedIssues``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListPinnedIssues`: []Issue
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListPinnedIssues`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListPinnedIssuesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListPinnedPullRequests

> []PullRequest RepoListPinnedPullRequests(ctx, owner, repo).Execute()

List a repo's pinned pull requests

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListPinnedPullRequests(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListPinnedPullRequests``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListPinnedPullRequests`: []PullRequest
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListPinnedPullRequests`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListPinnedPullRequestsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListPullRequests

> []PullRequest RepoListPullRequests(ctx, owner, repo).State(state).Sort(sort).Milestone(milestone).Labels(labels).Page(page).Limit(limit).Execute()

List a repo's pull requests

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    state := "state_example" // string | State of pull request: open or closed (optional) (optional)
    sort := "sort_example" // string | Type of sort (optional)
    milestone := int64(789) // int64 | ID of the milestone (optional)
    labels := []int64{int64(123)} // []int64 | Label IDs (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListPullRequests(context.Background(), owner, repo).State(state).Sort(sort).Milestone(milestone).Labels(labels).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListPullRequests``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListPullRequests`: []PullRequest
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListPullRequests`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListPullRequestsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **state** | **string** | State of pull request: open or closed (optional) | 
 **sort** | **string** | Type of sort | 
 **milestone** | **int64** | ID of the milestone | 
 **labels** | **[]int64** | Label IDs | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListPullReviews

> []PullReview RepoListPullReviews(ctx, owner, repo, index).Page(page).Limit(limit).Execute()

List all reviews for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListPullReviews(context.Background(), owner, repo, index).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListPullReviews``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListPullReviews`: []PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListPullReviews`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListPullReviewsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListPushMirrors

> []PushMirror RepoListPushMirrors(ctx, owner, repo).Page(page).Limit(limit).Execute()

Get all push mirrors of the repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListPushMirrors(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListPushMirrors``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListPushMirrors`: []PushMirror
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListPushMirrors`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListPushMirrorsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]PushMirror**](PushMirror.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListReleaseAttachments

> []Attachment RepoListReleaseAttachments(ctx, owner, repo, id).Execute()

List release's attachments

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the release

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListReleaseAttachments(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListReleaseAttachments``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListReleaseAttachments`: []Attachment
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListReleaseAttachments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the release | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListReleaseAttachmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**[]Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListReleases

> []Release RepoListReleases(ctx, owner, repo).Draft(draft).PreRelease(preRelease).Page(page).Limit(limit).Execute()

List a repo's releases

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    draft := true // bool | filter (exclude / include) drafts, if you dont have repo write access none will show (optional)
    preRelease := true // bool | filter (exclude / include) pre-releases (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListReleases(context.Background(), owner, repo).Draft(draft).PreRelease(preRelease).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListReleases``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListReleases`: []Release
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListReleases`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListReleasesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **draft** | **bool** | filter (exclude / include) drafts, if you dont have repo write access none will show | 
 **preRelease** | **bool** | filter (exclude / include) pre-releases | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListStargazers

> []User RepoListStargazers(ctx, owner, repo).Page(page).Limit(limit).Execute()

List a repo's stargazers

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListStargazers(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListStargazers``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListStargazers`: []User
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListStargazers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListStargazersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListStatuses

> []CommitStatus RepoListStatuses(ctx, owner, repo, sha).Sort(sort).State(state).Page(page).Limit(limit).Execute()

Get a commit's statuses

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    sha := "sha_example" // string | sha of the commit
    sort := "sort_example" // string | type of sort (optional)
    state := "state_example" // string | type of state (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListStatuses(context.Background(), owner, repo, sha).Sort(sort).State(state).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListStatuses``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListStatuses`: []CommitStatus
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListStatuses`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**sha** | **string** | sha of the commit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListStatusesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **sort** | **string** | type of sort | 
 **state** | **string** | type of state | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]CommitStatus**](CommitStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListStatusesByRef

> []CommitStatus RepoListStatusesByRef(ctx, owner, repo, ref).Sort(sort).State(state).Page(page).Limit(limit).Execute()

Get a commit's statuses, by branch/tag/commit reference

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    ref := "ref_example" // string | name of branch/tag/commit
    sort := "sort_example" // string | type of sort (optional)
    state := "state_example" // string | type of state (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListStatusesByRef(context.Background(), owner, repo, ref).Sort(sort).State(state).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListStatusesByRef``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListStatusesByRef`: []CommitStatus
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListStatusesByRef`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**ref** | **string** | name of branch/tag/commit | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListStatusesByRefRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **sort** | **string** | type of sort | 
 **state** | **string** | type of state | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]CommitStatus**](CommitStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListSubscribers

> []User RepoListSubscribers(ctx, owner, repo).Page(page).Limit(limit).Execute()

List a repo's watchers

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListSubscribers(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListSubscribers``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListSubscribers`: []User
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListSubscribers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListSubscribersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListTags

> []Tag RepoListTags(ctx, owner, repo).Page(page).Limit(limit).Execute()

List a repository's tags

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results, default maximum page size is 50 (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListTags(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListTags``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListTags`: []Tag
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListTags`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListTagsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results, default maximum page size is 50 | 

### Return type

[**[]Tag**](Tag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListTeams

> []Team RepoListTeams(ctx, owner, repo).Execute()

List a repository's teams

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListTeams(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListTeams``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListTeams`: []Team
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListTeams`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListTeamsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoListTopics

> TopicName RepoListTopics(ctx, owner, repo).Page(page).Limit(limit).Execute()

Get list of topics that a repository has

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoListTopics(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoListTopics``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoListTopics`: TopicName
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoListTopics`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoListTopicsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**TopicName**](TopicName.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoMergePullRequest

> RepoMergePullRequest(ctx, owner, repo, index).Body(body).Execute()

Merge a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to merge
    body := *openapiclient.NewMergePullRequestOption("Do_example") // MergePullRequestOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoMergePullRequest(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoMergePullRequest``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to merge | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoMergePullRequestRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**MergePullRequestOption**](MergePullRequestOption.md) |  | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoMigrate

> Repository RepoMigrate(ctx).Body(body).Execute()

Migrate a remote git repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    body := *openapiclient.NewMigrateRepoOptions("CloneAddr_example", "RepoName_example") // MigrateRepoOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoMigrate(context.Background()).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoMigrate``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoMigrate`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoMigrate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRepoMigrateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateRepoOptions**](MigrateRepoOptions.md) |  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoMirrorSync

> RepoMirrorSync(ctx, owner, repo).Execute()

Sync a mirrored repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to sync
    repo := "repo_example" // string | name of the repo to sync

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoMirrorSync(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoMirrorSync``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to sync | 
**repo** | **string** | name of the repo to sync | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoMirrorSyncRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoNewPinAllowed

> NewIssuePinsAllowed RepoNewPinAllowed(ctx, owner, repo).Execute()

Returns if new Issue Pins are allowed

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoNewPinAllowed(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoNewPinAllowed``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoNewPinAllowed`: NewIssuePinsAllowed
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoNewPinAllowed`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoNewPinAllowedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**NewIssuePinsAllowed**](NewIssuePinsAllowed.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoPullRequestIsMerged

> RepoPullRequestIsMerged(ctx, owner, repo, index).Execute()

Check if a pull request has been merged

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoPullRequestIsMerged(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoPullRequestIsMerged``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoPullRequestIsMergedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoPushMirrorSync

> RepoPushMirrorSync(ctx, owner, repo).Execute()

Sync all push mirrored repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to sync
    repo := "repo_example" // string | name of the repo to sync

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoPushMirrorSync(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoPushMirrorSync``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to sync | 
**repo** | **string** | name of the repo to sync | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoPushMirrorSyncRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoSearch

> SearchResults RepoSearch(ctx).Q(q).Topic(topic).IncludeDesc(includeDesc).Uid(uid).PriorityOwnerId(priorityOwnerId).TeamId(teamId).StarredBy(starredBy).Private(private).IsPrivate(isPrivate).Template(template).Archived(archived).Mode(mode).Exclusive(exclusive).Sort(sort).Order(order).Page(page).Limit(limit).Execute()

Search for repositories

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    q := "q_example" // string | keyword (optional)
    topic := true // bool | Limit search to repositories with keyword as topic (optional)
    includeDesc := true // bool | include search of keyword within repository description (optional)
    uid := int64(789) // int64 | search only for repos that the user with the given id owns or contributes to (optional)
    priorityOwnerId := int64(789) // int64 | repo owner to prioritize in the results (optional)
    teamId := int64(789) // int64 | search only for repos that belong to the given team id (optional)
    starredBy := int64(789) // int64 | search only for repos that the user with the given id has starred (optional)
    private := true // bool | include private repositories this user has access to (defaults to true) (optional)
    isPrivate := true // bool | show only pubic, private or all repositories (defaults to all) (optional)
    template := true // bool | include template repositories this user has access to (defaults to true) (optional)
    archived := true // bool | show only archived, non-archived or all repositories (defaults to all) (optional)
    mode := "mode_example" // string | type of repository to search for. Supported values are \"fork\", \"source\", \"mirror\" and \"collaborative\" (optional)
    exclusive := true // bool | if `uid` is given, search only for repos that the user owns (optional)
    sort := "sort_example" // string | sort repos by attribute. Supported values are \"alpha\", \"created\", \"updated\", \"size\", and \"id\". Default is \"alpha\" (optional)
    order := "order_example" // string | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoSearch(context.Background()).Q(q).Topic(topic).IncludeDesc(includeDesc).Uid(uid).PriorityOwnerId(priorityOwnerId).TeamId(teamId).StarredBy(starredBy).Private(private).IsPrivate(isPrivate).Template(template).Archived(archived).Mode(mode).Exclusive(exclusive).Sort(sort).Order(order).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoSearch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoSearch`: SearchResults
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoSearch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRepoSearchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **string** | keyword | 
 **topic** | **bool** | Limit search to repositories with keyword as topic | 
 **includeDesc** | **bool** | include search of keyword within repository description | 
 **uid** | **int64** | search only for repos that the user with the given id owns or contributes to | 
 **priorityOwnerId** | **int64** | repo owner to prioritize in the results | 
 **teamId** | **int64** | search only for repos that belong to the given team id | 
 **starredBy** | **int64** | search only for repos that the user with the given id has starred | 
 **private** | **bool** | include private repositories this user has access to (defaults to true) | 
 **isPrivate** | **bool** | show only pubic, private or all repositories (defaults to all) | 
 **template** | **bool** | include template repositories this user has access to (defaults to true) | 
 **archived** | **bool** | show only archived, non-archived or all repositories (defaults to all) | 
 **mode** | **string** | type of repository to search for. Supported values are \&quot;fork\&quot;, \&quot;source\&quot;, \&quot;mirror\&quot; and \&quot;collaborative\&quot; | 
 **exclusive** | **bool** | if &#x60;uid&#x60; is given, search only for repos that the user owns | 
 **sort** | **string** | sort repos by attribute. Supported values are \&quot;alpha\&quot;, \&quot;created\&quot;, \&quot;updated\&quot;, \&quot;size\&quot;, and \&quot;id\&quot;. Default is \&quot;alpha\&quot; | 
 **order** | **string** | sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoSigningKey

> string RepoSigningKey(ctx, owner, repo).Execute()

Get signing-key.gpg for given repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoSigningKey(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoSigningKey``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoSigningKey`: string
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoSigningKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoSigningKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

**string**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoSubmitPullReview

> PullReview RepoSubmitPullReview(ctx, owner, repo, index, id).Body(body).Execute()

Submit a pending review to an pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    id := int64(789) // int64 | id of the review
    body := *openapiclient.NewSubmitPullReviewOptions() // SubmitPullReviewOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoSubmitPullReview(context.Background(), owner, repo, index, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoSubmitPullReview``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoSubmitPullReview`: PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoSubmitPullReview`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 
**id** | **int64** | id of the review | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoSubmitPullReviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **body** | [**SubmitPullReviewOptions**](SubmitPullReviewOptions.md) |  | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoTestHook

> RepoTestHook(ctx, owner, repo, id).Ref(ref).Execute()

Test a push webhook

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    id := int64(789) // int64 | id of the hook to test
    ref := "ref_example" // string | The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload. (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoTestHook(context.Background(), owner, repo, id).Ref(ref).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoTestHook``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the hook to test | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoTestHookRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ref** | **string** | The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload. | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoTrackedTimes

> []TrackedTime RepoTrackedTimes(ctx, owner, repo).User(user).Since(since).Before(before).Page(page).Limit(limit).Execute()

List a repo's tracked times

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    "time"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    user := "user_example" // string | optional filter by user (available for issue managers) (optional)
    since := time.Now() // time.Time | Only show times updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before := time.Now() // time.Time | Only show times updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoTrackedTimes(context.Background(), owner, repo).User(user).Since(since).Before(before).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoTrackedTimes``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoTrackedTimes`: []TrackedTime
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoTrackedTimes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoTrackedTimesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **user** | **string** | optional filter by user (available for issue managers) | 
 **since** | **time.Time** | Only show times updated after the given time. This is a timestamp in RFC 3339 format | 
 **before** | **time.Time** | Only show times updated before the given time. This is a timestamp in RFC 3339 format | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]TrackedTime**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoTransfer

> Repository RepoTransfer(ctx, owner, repo).Body(body).Execute()

Transfer a repo ownership

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo to transfer
    repo := "repo_example" // string | name of the repo to transfer
    body := *openapiclient.NewTransferRepoOption("NewOwner_example") // TransferRepoOption | Transfer Options

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoTransfer(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoTransfer``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoTransfer`: Repository
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoTransfer`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo to transfer | 
**repo** | **string** | name of the repo to transfer | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoTransferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**TransferRepoOption**](TransferRepoOption.md) | Transfer Options | 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoUnDismissPullReview

> PullReview RepoUnDismissPullReview(ctx, owner, repo, index, id).Execute()

Cancel to dismiss a review for a pull request

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request
    id := int64(789) // int64 | id of the review

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoUnDismissPullReview(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoUnDismissPullReview``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoUnDismissPullReview`: PullReview
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoUnDismissPullReview`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request | 
**id** | **int64** | id of the review | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoUnDismissPullReviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoUpdateAvatar

> RepoUpdateAvatar(ctx, owner, repo).Body(body).Execute()

Update avatar

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewUpdateRepoAvatarOption() // UpdateRepoAvatarOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoUpdateAvatar(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoUpdateAvatar``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoUpdateAvatarRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**UpdateRepoAvatarOption**](UpdateRepoAvatarOption.md) |  | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoUpdateFile

> FileResponse RepoUpdateFile(ctx, owner, repo, filepath).Body(body).Execute()

Update a file in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    filepath := "filepath_example" // string | path of the file to update
    body := *openapiclient.NewUpdateFileOptions("Content_example", "Sha_example") // UpdateFileOptions | 

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoUpdateFile(context.Background(), owner, repo, filepath).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoUpdateFile``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoUpdateFile`: FileResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoUpdateFile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**filepath** | **string** | path of the file to update | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoUpdateFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**UpdateFileOptions**](UpdateFileOptions.md) |  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoUpdatePullRequest

> RepoUpdatePullRequest(ctx, owner, repo, index).Style(style).Execute()

Merge PR's baseBranch into headBranch

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    index := int64(789) // int64 | index of the pull request to get
    style := "style_example" // string | how to update pull request (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoUpdatePullRequest(context.Background(), owner, repo, index).Style(style).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoUpdatePullRequest``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the pull request to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoUpdatePullRequestRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **style** | **string** | how to update pull request | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoUpdateTopics

> RepoUpdateTopics(ctx, owner, repo).Body(body).Execute()

Replace list of topics for a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    body := *openapiclient.NewRepoTopicOptions() // RepoTopicOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoUpdateTopics(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoUpdateTopics``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoUpdateTopicsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**RepoTopicOptions**](RepoTopicOptions.md) |  | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RepoValidateIssueConfig

> IssueConfigValidation RepoValidateIssueConfig(ctx, owner, repo).Execute()

Returns the validation information for a issue config

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.RepoValidateIssueConfig(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.RepoValidateIssueConfig``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `RepoValidateIssueConfig`: IssueConfigValidation
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.RepoValidateIssueConfig`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiRepoValidateIssueConfigRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**IssueConfigValidation**](IssueConfigValidation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TopicSearch

> []TopicResponse TopicSearch(ctx).Q(q).Page(page).Limit(limit).Execute()

search topics via keyword

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    q := "q_example" // string | keywords to search
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.TopicSearch(context.Background()).Q(q).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.TopicSearch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TopicSearch`: []TopicResponse
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.TopicSearch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTopicSearchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **string** | keywords to search | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]TopicResponse**](TopicResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateRepoSecret

> UpdateRepoSecret(ctx, owner, repo, secretname).Body(body).Execute()

Create or Update a secret value in a repository

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repository
    repo := "repo_example" // string | name of the repository
    secretname := "secretname_example" // string | name of the secret
    body := *openapiclient.NewCreateOrUpdateSecretOption("Data_example") // CreateOrUpdateSecretOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.UpdateRepoSecret(context.Background(), owner, repo, secretname).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.UpdateRepoSecret``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repository | 
**repo** | **string** | name of the repository | 
**secretname** | **string** | name of the secret | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateRepoSecretRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**CreateOrUpdateSecretOption**](CreateOrUpdateSecretOption.md) |  | 

### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UserCurrentCheckSubscription

> WatchInfo UserCurrentCheckSubscription(ctx, owner, repo).Execute()

Check if the current user is watching a repo

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.UserCurrentCheckSubscription(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.UserCurrentCheckSubscription``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `UserCurrentCheckSubscription`: WatchInfo
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.UserCurrentCheckSubscription`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiUserCurrentCheckSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UserCurrentDeleteSubscription

> UserCurrentDeleteSubscription(ctx, owner, repo).Execute()

Unwatch a repo

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.UserCurrentDeleteSubscription(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.UserCurrentDeleteSubscription``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiUserCurrentDeleteSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UserCurrentPutSubscription

> WatchInfo UserCurrentPutSubscription(ctx, owner, repo).Execute()

Watch a repo

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.UserCurrentPutSubscription(context.Background(), owner, repo).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.UserCurrentPutSubscription``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `UserCurrentPutSubscription`: WatchInfo
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.UserCurrentPutSubscription`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiUserCurrentPutSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UserTrackedTimes

> []TrackedTime UserTrackedTimes(ctx, owner, repo, user).Execute()

List a user's tracked times in a repo

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    owner := "owner_example" // string | owner of the repo
    repo := "repo_example" // string | name of the repo
    user := "user_example" // string | username of user

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.RepositoryApi.UserTrackedTimes(context.Background(), owner, repo, user).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RepositoryApi.UserTrackedTimes``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `UserTrackedTimes`: []TrackedTime
    fmt.Fprintf(os.Stdout, "Response from `RepositoryApi.UserTrackedTimes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**user** | **string** | username of user | 

### Other Parameters

Other parameters are passed through a pointer to a apiUserTrackedTimesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**[]TrackedTime**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


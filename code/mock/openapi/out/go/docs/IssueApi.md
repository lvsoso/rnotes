# \IssueApi

All URIs are relative to *http://}/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**IssueAddLabel**](IssueApi.md#IssueAddLabel) | **Post** /repos/{owner}/{repo}/issues/{index}/labels | Add a label to an issue
[**IssueAddSubscription**](IssueApi.md#IssueAddSubscription) | **Put** /repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | Subscribe user to issue
[**IssueAddTime**](IssueApi.md#IssueAddTime) | **Post** /repos/{owner}/{repo}/issues/{index}/times | Add tracked time to a issue
[**IssueCheckSubscription**](IssueApi.md#IssueCheckSubscription) | **Get** /repos/{owner}/{repo}/issues/{index}/subscriptions/check | Check if user is subscribed to an issue
[**IssueClearLabels**](IssueApi.md#IssueClearLabels) | **Delete** /repos/{owner}/{repo}/issues/{index}/labels | Remove all labels from an issue
[**IssueCreateComment**](IssueApi.md#IssueCreateComment) | **Post** /repos/{owner}/{repo}/issues/{index}/comments | Add a comment to an issue
[**IssueCreateIssue**](IssueApi.md#IssueCreateIssue) | **Post** /repos/{owner}/{repo}/issues | Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**IssueCreateIssueAttachment**](IssueApi.md#IssueCreateIssueAttachment) | **Post** /repos/{owner}/{repo}/issues/{index}/assets | Create an issue attachment
[**IssueCreateIssueBlocking**](IssueApi.md#IssueCreateIssueBlocking) | **Post** /repos/{owner}/{repo}/issues/{index}/blocks | Block the issue given in the body by the issue in path
[**IssueCreateIssueCommentAttachment**](IssueApi.md#IssueCreateIssueCommentAttachment) | **Post** /repos/{owner}/{repo}/issues/comments/{id}/assets | Create a comment attachment
[**IssueCreateIssueDependencies**](IssueApi.md#IssueCreateIssueDependencies) | **Post** /repos/{owner}/{repo}/issues/{index}/dependencies | Make the issue in the url depend on the issue in the form.
[**IssueCreateLabel**](IssueApi.md#IssueCreateLabel) | **Post** /repos/{owner}/{repo}/labels | Create a label
[**IssueCreateMilestone**](IssueApi.md#IssueCreateMilestone) | **Post** /repos/{owner}/{repo}/milestones | Create a milestone
[**IssueDelete**](IssueApi.md#IssueDelete) | **Delete** /repos/{owner}/{repo}/issues/{index} | Delete an issue
[**IssueDeleteComment**](IssueApi.md#IssueDeleteComment) | **Delete** /repos/{owner}/{repo}/issues/comments/{id} | Delete a comment
[**IssueDeleteCommentDeprecated**](IssueApi.md#IssueDeleteCommentDeprecated) | **Delete** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Delete a comment
[**IssueDeleteCommentReaction**](IssueApi.md#IssueDeleteCommentReaction) | **Delete** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Remove a reaction from a comment of an issue
[**IssueDeleteIssueAttachment**](IssueApi.md#IssueDeleteIssueAttachment) | **Delete** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Delete an issue attachment
[**IssueDeleteIssueCommentAttachment**](IssueApi.md#IssueDeleteIssueCommentAttachment) | **Delete** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Delete a comment attachment
[**IssueDeleteIssueReaction**](IssueApi.md#IssueDeleteIssueReaction) | **Delete** /repos/{owner}/{repo}/issues/{index}/reactions | Remove a reaction from an issue
[**IssueDeleteLabel**](IssueApi.md#IssueDeleteLabel) | **Delete** /repos/{owner}/{repo}/labels/{id} | Delete a label
[**IssueDeleteMilestone**](IssueApi.md#IssueDeleteMilestone) | **Delete** /repos/{owner}/{repo}/milestones/{id} | Delete a milestone
[**IssueDeleteStopWatch**](IssueApi.md#IssueDeleteStopWatch) | **Delete** /repos/{owner}/{repo}/issues/{index}/stopwatch/delete | Delete an issue&#39;s existing stopwatch.
[**IssueDeleteSubscription**](IssueApi.md#IssueDeleteSubscription) | **Delete** /repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | Unsubscribe user from issue
[**IssueDeleteTime**](IssueApi.md#IssueDeleteTime) | **Delete** /repos/{owner}/{repo}/issues/{index}/times/{id} | Delete specific tracked time
[**IssueEditComment**](IssueApi.md#IssueEditComment) | **Patch** /repos/{owner}/{repo}/issues/comments/{id} | Edit a comment
[**IssueEditCommentDeprecated**](IssueApi.md#IssueEditCommentDeprecated) | **Patch** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Edit a comment
[**IssueEditIssue**](IssueApi.md#IssueEditIssue) | **Patch** /repos/{owner}/{repo}/issues/{index} | Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**IssueEditIssueAttachment**](IssueApi.md#IssueEditIssueAttachment) | **Patch** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Edit an issue attachment
[**IssueEditIssueCommentAttachment**](IssueApi.md#IssueEditIssueCommentAttachment) | **Patch** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Edit a comment attachment
[**IssueEditIssueDeadline**](IssueApi.md#IssueEditIssueDeadline) | **Post** /repos/{owner}/{repo}/issues/{index}/deadline | Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
[**IssueEditLabel**](IssueApi.md#IssueEditLabel) | **Patch** /repos/{owner}/{repo}/labels/{id} | Update a label
[**IssueEditMilestone**](IssueApi.md#IssueEditMilestone) | **Patch** /repos/{owner}/{repo}/milestones/{id} | Update a milestone
[**IssueGetComment**](IssueApi.md#IssueGetComment) | **Get** /repos/{owner}/{repo}/issues/comments/{id} | Get a comment
[**IssueGetCommentReactions**](IssueApi.md#IssueGetCommentReactions) | **Get** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Get a list of reactions from a comment of an issue
[**IssueGetComments**](IssueApi.md#IssueGetComments) | **Get** /repos/{owner}/{repo}/issues/{index}/comments | List all comments on an issue
[**IssueGetCommentsAndTimeline**](IssueApi.md#IssueGetCommentsAndTimeline) | **Get** /repos/{owner}/{repo}/issues/{index}/timeline | List all comments and events on an issue
[**IssueGetIssue**](IssueApi.md#IssueGetIssue) | **Get** /repos/{owner}/{repo}/issues/{index} | Get an issue
[**IssueGetIssueAttachment**](IssueApi.md#IssueGetIssueAttachment) | **Get** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Get an issue attachment
[**IssueGetIssueCommentAttachment**](IssueApi.md#IssueGetIssueCommentAttachment) | **Get** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Get a comment attachment
[**IssueGetIssueReactions**](IssueApi.md#IssueGetIssueReactions) | **Get** /repos/{owner}/{repo}/issues/{index}/reactions | Get a list reactions of an issue
[**IssueGetLabel**](IssueApi.md#IssueGetLabel) | **Get** /repos/{owner}/{repo}/labels/{id} | Get a single label
[**IssueGetLabels**](IssueApi.md#IssueGetLabels) | **Get** /repos/{owner}/{repo}/issues/{index}/labels | Get an issue&#39;s labels
[**IssueGetMilestone**](IssueApi.md#IssueGetMilestone) | **Get** /repos/{owner}/{repo}/milestones/{id} | Get a milestone
[**IssueGetMilestonesList**](IssueApi.md#IssueGetMilestonesList) | **Get** /repos/{owner}/{repo}/milestones | Get all of a repository&#39;s opened milestones
[**IssueGetRepoComments**](IssueApi.md#IssueGetRepoComments) | **Get** /repos/{owner}/{repo}/issues/comments | List all comments in a repository
[**IssueListBlocks**](IssueApi.md#IssueListBlocks) | **Get** /repos/{owner}/{repo}/issues/{index}/blocks | List issues that are blocked by this issue
[**IssueListIssueAttachments**](IssueApi.md#IssueListIssueAttachments) | **Get** /repos/{owner}/{repo}/issues/{index}/assets | List issue&#39;s attachments
[**IssueListIssueCommentAttachments**](IssueApi.md#IssueListIssueCommentAttachments) | **Get** /repos/{owner}/{repo}/issues/comments/{id}/assets | List comment&#39;s attachments
[**IssueListIssueDependencies**](IssueApi.md#IssueListIssueDependencies) | **Get** /repos/{owner}/{repo}/issues/{index}/dependencies | List an issue&#39;s dependencies, i.e all issues that block this issue.
[**IssueListIssues**](IssueApi.md#IssueListIssues) | **Get** /repos/{owner}/{repo}/issues | List a repository&#39;s issues
[**IssueListLabels**](IssueApi.md#IssueListLabels) | **Get** /repos/{owner}/{repo}/labels | Get all of a repository&#39;s labels
[**IssuePostCommentReaction**](IssueApi.md#IssuePostCommentReaction) | **Post** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Add a reaction to a comment of an issue
[**IssuePostIssueReaction**](IssueApi.md#IssuePostIssueReaction) | **Post** /repos/{owner}/{repo}/issues/{index}/reactions | Add a reaction to an issue
[**IssueRemoveIssueBlocking**](IssueApi.md#IssueRemoveIssueBlocking) | **Delete** /repos/{owner}/{repo}/issues/{index}/blocks | Unblock the issue given in the body by the issue in path
[**IssueRemoveIssueDependencies**](IssueApi.md#IssueRemoveIssueDependencies) | **Delete** /repos/{owner}/{repo}/issues/{index}/dependencies | Remove an issue dependency
[**IssueRemoveLabel**](IssueApi.md#IssueRemoveLabel) | **Delete** /repos/{owner}/{repo}/issues/{index}/labels/{id} | Remove a label from an issue
[**IssueReplaceLabels**](IssueApi.md#IssueReplaceLabels) | **Put** /repos/{owner}/{repo}/issues/{index}/labels | Replace an issue&#39;s labels
[**IssueResetTime**](IssueApi.md#IssueResetTime) | **Delete** /repos/{owner}/{repo}/issues/{index}/times | Reset a tracked time of an issue
[**IssueSearchIssues**](IssueApi.md#IssueSearchIssues) | **Get** /repos/issues/search | Search for issues across the repositories that the user has access to
[**IssueStartStopWatch**](IssueApi.md#IssueStartStopWatch) | **Post** /repos/{owner}/{repo}/issues/{index}/stopwatch/start | Start stopwatch on an issue.
[**IssueStopStopWatch**](IssueApi.md#IssueStopStopWatch) | **Post** /repos/{owner}/{repo}/issues/{index}/stopwatch/stop | Stop an issue&#39;s existing stopwatch.
[**IssueSubscriptions**](IssueApi.md#IssueSubscriptions) | **Get** /repos/{owner}/{repo}/issues/{index}/subscriptions | Get users who subscribed on an issue.
[**IssueTrackedTimes**](IssueApi.md#IssueTrackedTimes) | **Get** /repos/{owner}/{repo}/issues/{index}/times | List an issue&#39;s tracked times
[**MoveIssuePin**](IssueApi.md#MoveIssuePin) | **Patch** /repos/{owner}/{repo}/issues/{index}/pin/{position} | Moves the Pin to the given Position
[**PinIssue**](IssueApi.md#PinIssue) | **Post** /repos/{owner}/{repo}/issues/{index}/pin | Pin an Issue
[**UnpinIssue**](IssueApi.md#UnpinIssue) | **Delete** /repos/{owner}/{repo}/issues/{index}/pin | Unpin an Issue



## IssueAddLabel

> []Label IssueAddLabel(ctx, owner, repo, index).Body(body).Execute()

Add a label to an issue

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
    index := int64(789) // int64 | index of the issue
    body := *openapiclient.NewIssueLabelsOption() // IssueLabelsOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueAddLabel(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueAddLabel``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueAddLabel`: []Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueAddLabel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueAddLabelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**IssueLabelsOption**](IssueLabelsOption.md) |  | 

### Return type

[**[]Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueAddSubscription

> IssueAddSubscription(ctx, owner, repo, index, user).Execute()

Subscribe user to issue

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
    index := int64(789) // int64 | index of the issue
    user := "user_example" // string | user to subscribe

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueAddSubscription(context.Background(), owner, repo, index, user).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueAddSubscription``: %v\n", err)
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
**index** | **int64** | index of the issue | 
**user** | **string** | user to subscribe | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueAddSubscriptionRequest struct via the builder pattern


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


## IssueAddTime

> TrackedTime IssueAddTime(ctx, owner, repo, index).Body(body).Execute()

Add tracked time to a issue

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
    index := int64(789) // int64 | index of the issue
    body := *openapiclient.NewAddTimeOption(int64(123)) // AddTimeOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueAddTime(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueAddTime``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueAddTime`: TrackedTime
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueAddTime`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueAddTimeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**AddTimeOption**](AddTimeOption.md) |  | 

### Return type

[**TrackedTime**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueCheckSubscription

> WatchInfo IssueCheckSubscription(ctx, owner, repo, index).Execute()

Check if user is subscribed to an issue

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
    index := int64(789) // int64 | index of the issue

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCheckSubscription(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCheckSubscription``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCheckSubscription`: WatchInfo
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCheckSubscription`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCheckSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueClearLabels

> IssueClearLabels(ctx, owner, repo, index).Execute()

Remove all labels from an issue

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
    index := int64(789) // int64 | index of the issue

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueClearLabels(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueClearLabels``: %v\n", err)
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
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueClearLabelsRequest struct via the builder pattern


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


## IssueCreateComment

> Comment IssueCreateComment(ctx, owner, repo, index).Body(body).Execute()

Add a comment to an issue

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
    index := int64(789) // int64 | index of the issue
    body := *openapiclient.NewCreateIssueCommentOption("Body_example") // CreateIssueCommentOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateComment(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateComment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateComment`: Comment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateComment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateCommentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**CreateIssueCommentOption**](CreateIssueCommentOption.md) |  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueCreateIssue

> Issue IssueCreateIssue(ctx, owner, repo).Body(body).Execute()

Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

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
    body := *openapiclient.NewCreateIssueOption("Title_example") // CreateIssueOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateIssue(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateIssue``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateIssue`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateIssue`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateIssueRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateIssueOption**](CreateIssueOption.md) |  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueCreateIssueAttachment

> Attachment IssueCreateIssueAttachment(ctx, owner, repo, index).Attachment(attachment).Name(name).Execute()

Create an issue attachment

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
    index := int64(789) // int64 | index of the issue
    attachment := os.NewFile(1234, "some_file") // *os.File | attachment to upload
    name := "name_example" // string | name of the attachment (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateIssueAttachment(context.Background(), owner, repo, index).Attachment(attachment).Name(name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateIssueAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateIssueAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateIssueAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateIssueAttachmentRequest struct via the builder pattern


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


## IssueCreateIssueBlocking

> Issue IssueCreateIssueBlocking(ctx, owner, repo, index).Body(body).Execute()

Block the issue given in the body by the issue in path

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
    index := "index_example" // string | index of the issue
    body := *openapiclient.NewIssueMeta() // IssueMeta |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateIssueBlocking(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateIssueBlocking``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateIssueBlocking`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateIssueBlocking`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **string** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateIssueBlockingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**IssueMeta**](IssueMeta.md) |  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueCreateIssueCommentAttachment

> Attachment IssueCreateIssueCommentAttachment(ctx, owner, repo, id).Attachment(attachment).Name(name).Execute()

Create a comment attachment

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
    id := int64(789) // int64 | id of the comment
    attachment := os.NewFile(1234, "some_file") // *os.File | attachment to upload
    name := "name_example" // string | name of the attachment (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateIssueCommentAttachment(context.Background(), owner, repo, id).Attachment(attachment).Name(name).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateIssueCommentAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateIssueCommentAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateIssueCommentAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateIssueCommentAttachmentRequest struct via the builder pattern


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


## IssueCreateIssueDependencies

> Issue IssueCreateIssueDependencies(ctx, owner, repo, index).Body(body).Execute()

Make the issue in the url depend on the issue in the form.

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
    index := "index_example" // string | index of the issue
    body := *openapiclient.NewIssueMeta() // IssueMeta |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateIssueDependencies(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateIssueDependencies``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateIssueDependencies`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateIssueDependencies`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **string** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateIssueDependenciesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**IssueMeta**](IssueMeta.md) |  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueCreateLabel

> Label IssueCreateLabel(ctx, owner, repo).Body(body).Execute()

Create a label

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
    body := *openapiclient.NewCreateLabelOption("#00aabb", "Name_example") // CreateLabelOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateLabel(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateLabel``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateLabel`: Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateLabel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateLabelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateLabelOption**](CreateLabelOption.md) |  | 

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueCreateMilestone

> Milestone IssueCreateMilestone(ctx, owner, repo).Body(body).Execute()

Create a milestone

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
    body := *openapiclient.NewCreateMilestoneOption() // CreateMilestoneOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueCreateMilestone(context.Background(), owner, repo).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueCreateMilestone``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueCreateMilestone`: Milestone
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueCreateMilestone`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueCreateMilestoneRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**CreateMilestoneOption**](CreateMilestoneOption.md) |  | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueDelete

> IssueDelete(ctx, owner, repo, index).Execute()

Delete an issue

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
    index := int64(789) // int64 | index of issue to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDelete(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDelete``: %v\n", err)
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
**index** | **int64** | index of issue to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteRequest struct via the builder pattern


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


## IssueDeleteComment

> IssueDeleteComment(ctx, owner, repo, id).Execute()

Delete a comment

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
    id := int64(789) // int64 | id of comment to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteComment(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteComment``: %v\n", err)
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
**id** | **int64** | id of comment to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteCommentRequest struct via the builder pattern


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


## IssueDeleteCommentDeprecated

> IssueDeleteCommentDeprecated(ctx, owner, repo, index, id).Execute()

Delete a comment

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
    index := int32(56) // int32 | this parameter is ignored
    id := int64(789) // int64 | id of comment to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteCommentDeprecated(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteCommentDeprecated``: %v\n", err)
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
**index** | **int32** | this parameter is ignored | 
**id** | **int64** | id of comment to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteCommentDeprecatedRequest struct via the builder pattern


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


## IssueDeleteCommentReaction

> IssueDeleteCommentReaction(ctx, owner, repo, id).Content(content).Execute()

Remove a reaction from a comment of an issue

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
    id := int64(789) // int64 | id of the comment to edit
    content := *openapiclient.NewEditReactionOption() // EditReactionOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteCommentReaction(context.Background(), owner, repo, id).Content(content).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteCommentReaction``: %v\n", err)
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
**id** | **int64** | id of the comment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteCommentReactionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **content** | [**EditReactionOption**](EditReactionOption.md) |  | 

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


## IssueDeleteIssueAttachment

> IssueDeleteIssueAttachment(ctx, owner, repo, index, attachmentId).Execute()

Delete an issue attachment

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
    index := int64(789) // int64 | index of the issue
    attachmentId := int64(789) // int64 | id of the attachment to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteIssueAttachment(context.Background(), owner, repo, index, attachmentId).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteIssueAttachment``: %v\n", err)
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
**index** | **int64** | index of the issue | 
**attachmentId** | **int64** | id of the attachment to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteIssueAttachmentRequest struct via the builder pattern


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


## IssueDeleteIssueCommentAttachment

> IssueDeleteIssueCommentAttachment(ctx, owner, repo, id, attachmentId).Execute()

Delete a comment attachment

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
    id := int64(789) // int64 | id of the comment
    attachmentId := int64(789) // int64 | id of the attachment to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteIssueCommentAttachment(context.Background(), owner, repo, id, attachmentId).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteIssueCommentAttachment``: %v\n", err)
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
**id** | **int64** | id of the comment | 
**attachmentId** | **int64** | id of the attachment to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteIssueCommentAttachmentRequest struct via the builder pattern


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


## IssueDeleteIssueReaction

> IssueDeleteIssueReaction(ctx, owner, repo, index).Content(content).Execute()

Remove a reaction from an issue

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
    index := int64(789) // int64 | index of the issue
    content := *openapiclient.NewEditReactionOption() // EditReactionOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteIssueReaction(context.Background(), owner, repo, index).Content(content).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteIssueReaction``: %v\n", err)
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
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteIssueReactionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **content** | [**EditReactionOption**](EditReactionOption.md) |  | 

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


## IssueDeleteLabel

> IssueDeleteLabel(ctx, owner, repo, id).Execute()

Delete a label

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
    id := int64(789) // int64 | id of the label to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteLabel(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteLabel``: %v\n", err)
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
**id** | **int64** | id of the label to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteLabelRequest struct via the builder pattern


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


## IssueDeleteMilestone

> IssueDeleteMilestone(ctx, owner, repo, id).Execute()

Delete a milestone

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
    id := "id_example" // string | the milestone to delete, identified by ID and if not available by name

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteMilestone(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteMilestone``: %v\n", err)
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
**id** | **string** | the milestone to delete, identified by ID and if not available by name | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteMilestoneRequest struct via the builder pattern


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


## IssueDeleteStopWatch

> IssueDeleteStopWatch(ctx, owner, repo, index).Execute()

Delete an issue's existing stopwatch.

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
    index := int64(789) // int64 | index of the issue to stop the stopwatch on

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteStopWatch(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteStopWatch``: %v\n", err)
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
**index** | **int64** | index of the issue to stop the stopwatch on | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteStopWatchRequest struct via the builder pattern


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


## IssueDeleteSubscription

> IssueDeleteSubscription(ctx, owner, repo, index, user).Execute()

Unsubscribe user from issue

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
    index := int64(789) // int64 | index of the issue
    user := "user_example" // string | user witch unsubscribe

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteSubscription(context.Background(), owner, repo, index, user).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteSubscription``: %v\n", err)
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
**index** | **int64** | index of the issue | 
**user** | **string** | user witch unsubscribe | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteSubscriptionRequest struct via the builder pattern


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


## IssueDeleteTime

> IssueDeleteTime(ctx, owner, repo, index, id).Execute()

Delete specific tracked time

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
    index := int64(789) // int64 | index of the issue
    id := int64(789) // int64 | id of time to delete

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueDeleteTime(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueDeleteTime``: %v\n", err)
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
**index** | **int64** | index of the issue | 
**id** | **int64** | id of time to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueDeleteTimeRequest struct via the builder pattern


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


## IssueEditComment

> Comment IssueEditComment(ctx, owner, repo, id).Body(body).Execute()

Edit a comment

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
    id := int64(789) // int64 | id of the comment to edit
    body := *openapiclient.NewEditIssueCommentOption("Body_example") // EditIssueCommentOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditComment(context.Background(), owner, repo, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditComment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditComment`: Comment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditComment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditCommentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditIssueCommentOption**](EditIssueCommentOption.md) |  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueEditCommentDeprecated

> Comment IssueEditCommentDeprecated(ctx, owner, repo, index, id).Body(body).Execute()

Edit a comment

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
    index := int32(56) // int32 | this parameter is ignored
    id := int64(789) // int64 | id of the comment to edit
    body := *openapiclient.NewEditIssueCommentOption("Body_example") // EditIssueCommentOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditCommentDeprecated(context.Background(), owner, repo, index, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditCommentDeprecated``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditCommentDeprecated`: Comment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditCommentDeprecated`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int32** | this parameter is ignored | 
**id** | **int64** | id of the comment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditCommentDeprecatedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **body** | [**EditIssueCommentOption**](EditIssueCommentOption.md) |  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueEditIssue

> Issue IssueEditIssue(ctx, owner, repo, index).Body(body).Execute()

Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

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
    index := int64(789) // int64 | index of the issue to edit
    body := *openapiclient.NewEditIssueOption() // EditIssueOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditIssue(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditIssue``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditIssue`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditIssue`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditIssueRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditIssueOption**](EditIssueOption.md) |  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueEditIssueAttachment

> Attachment IssueEditIssueAttachment(ctx, owner, repo, index, attachmentId).Body(body).Execute()

Edit an issue attachment

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
    index := int64(789) // int64 | index of the issue
    attachmentId := int64(789) // int64 | id of the attachment to edit
    body := *openapiclient.NewEditAttachmentOptions() // EditAttachmentOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditIssueAttachment(context.Background(), owner, repo, index, attachmentId).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditIssueAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditIssueAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditIssueAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 
**attachmentId** | **int64** | id of the attachment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditIssueAttachmentRequest struct via the builder pattern


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


## IssueEditIssueCommentAttachment

> Attachment IssueEditIssueCommentAttachment(ctx, owner, repo, id, attachmentId).Body(body).Execute()

Edit a comment attachment

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
    id := int64(789) // int64 | id of the comment
    attachmentId := int64(789) // int64 | id of the attachment to edit
    body := *openapiclient.NewEditAttachmentOptions() // EditAttachmentOptions |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditIssueCommentAttachment(context.Background(), owner, repo, id, attachmentId).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditIssueCommentAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditIssueCommentAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditIssueCommentAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment | 
**attachmentId** | **int64** | id of the attachment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditIssueCommentAttachmentRequest struct via the builder pattern


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


## IssueEditIssueDeadline

> IssueDeadline IssueEditIssueDeadline(ctx, owner, repo, index).Body(body).Execute()

Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.

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
    index := int64(789) // int64 | index of the issue to create or update a deadline on
    body := *openapiclient.NewEditDeadlineOption(time.Now()) // EditDeadlineOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditIssueDeadline(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditIssueDeadline``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditIssueDeadline`: IssueDeadline
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditIssueDeadline`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue to create or update a deadline on | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditIssueDeadlineRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditDeadlineOption**](EditDeadlineOption.md) |  | 

### Return type

[**IssueDeadline**](IssueDeadline.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueEditLabel

> Label IssueEditLabel(ctx, owner, repo, id).Body(body).Execute()

Update a label

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
    id := int64(789) // int64 | id of the label to edit
    body := *openapiclient.NewEditLabelOption() // EditLabelOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditLabel(context.Background(), owner, repo, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditLabel``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditLabel`: Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditLabel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the label to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditLabelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditLabelOption**](EditLabelOption.md) |  | 

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueEditMilestone

> Milestone IssueEditMilestone(ctx, owner, repo, id).Body(body).Execute()

Update a milestone

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
    id := "id_example" // string | the milestone to edit, identified by ID and if not available by name
    body := *openapiclient.NewEditMilestoneOption() // EditMilestoneOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueEditMilestone(context.Background(), owner, repo, id).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueEditMilestone``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueEditMilestone`: Milestone
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueEditMilestone`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **string** | the milestone to edit, identified by ID and if not available by name | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueEditMilestoneRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**EditMilestoneOption**](EditMilestoneOption.md) |  | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetComment

> Comment IssueGetComment(ctx, owner, repo, id).Execute()

Get a comment

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
    id := int64(789) // int64 | id of the comment

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetComment(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetComment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetComment`: Comment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetComment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetCommentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetCommentReactions

> []Reaction IssueGetCommentReactions(ctx, owner, repo, id).Execute()

Get a list of reactions from a comment of an issue

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
    id := int64(789) // int64 | id of the comment to edit

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetCommentReactions(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetCommentReactions``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetCommentReactions`: []Reaction
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetCommentReactions`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetCommentReactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**[]Reaction**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetComments

> []Comment IssueGetComments(ctx, owner, repo, index).Since(since).Before(before).Execute()

List all comments on an issue

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
    index := int64(789) // int64 | index of the issue
    since := time.Now() // time.Time | if provided, only comments updated since the specified time are returned. (optional)
    before := time.Now() // time.Time | if provided, only comments updated before the provided time are returned. (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetComments(context.Background(), owner, repo, index).Since(since).Before(before).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetComments``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetComments`: []Comment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetComments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetCommentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **since** | **time.Time** | if provided, only comments updated since the specified time are returned. | 
 **before** | **time.Time** | if provided, only comments updated before the provided time are returned. | 

### Return type

[**[]Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetCommentsAndTimeline

> []TimelineComment IssueGetCommentsAndTimeline(ctx, owner, repo, index).Since(since).Page(page).Limit(limit).Before(before).Execute()

List all comments and events on an issue

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
    index := int64(789) // int64 | index of the issue
    since := time.Now() // time.Time | if provided, only comments updated since the specified time are returned. (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)
    before := time.Now() // time.Time | if provided, only comments updated before the provided time are returned. (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetCommentsAndTimeline(context.Background(), owner, repo, index).Since(since).Page(page).Limit(limit).Before(before).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetCommentsAndTimeline``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetCommentsAndTimeline`: []TimelineComment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetCommentsAndTimeline`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetCommentsAndTimelineRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **since** | **time.Time** | if provided, only comments updated since the specified time are returned. | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 
 **before** | **time.Time** | if provided, only comments updated before the provided time are returned. | 

### Return type

[**[]TimelineComment**](TimelineComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetIssue

> Issue IssueGetIssue(ctx, owner, repo, index).Execute()

Get an issue

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
    index := int64(789) // int64 | index of the issue to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetIssue(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetIssue``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetIssue`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetIssue`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetIssueRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetIssueAttachment

> Attachment IssueGetIssueAttachment(ctx, owner, repo, index, attachmentId).Execute()

Get an issue attachment

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
    index := int64(789) // int64 | index of the issue
    attachmentId := int64(789) // int64 | id of the attachment to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetIssueAttachment(context.Background(), owner, repo, index, attachmentId).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetIssueAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetIssueAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetIssueAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 
**attachmentId** | **int64** | id of the attachment to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetIssueAttachmentRequest struct via the builder pattern


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


## IssueGetIssueCommentAttachment

> Attachment IssueGetIssueCommentAttachment(ctx, owner, repo, id, attachmentId).Execute()

Get a comment attachment

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
    id := int64(789) // int64 | id of the comment
    attachmentId := int64(789) // int64 | id of the attachment to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetIssueCommentAttachment(context.Background(), owner, repo, id, attachmentId).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetIssueCommentAttachment``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetIssueCommentAttachment`: Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetIssueCommentAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment | 
**attachmentId** | **int64** | id of the attachment to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetIssueCommentAttachmentRequest struct via the builder pattern


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


## IssueGetIssueReactions

> []Reaction IssueGetIssueReactions(ctx, owner, repo, index).Page(page).Limit(limit).Execute()

Get a list reactions of an issue

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
    index := int64(789) // int64 | index of the issue
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetIssueReactions(context.Background(), owner, repo, index).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetIssueReactions``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetIssueReactions`: []Reaction
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetIssueReactions`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetIssueReactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Reaction**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetLabel

> Label IssueGetLabel(ctx, owner, repo, id).Execute()

Get a single label

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
    id := int64(789) // int64 | id of the label to get

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetLabel(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetLabel``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetLabel`: Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetLabel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the label to get | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetLabelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetLabels

> []Label IssueGetLabels(ctx, owner, repo, index).Execute()

Get an issue's labels

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
    index := int64(789) // int64 | index of the issue

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetLabels(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetLabels``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetLabels`: []Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetLabels`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetLabelsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**[]Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetMilestone

> Milestone IssueGetMilestone(ctx, owner, repo, id).Execute()

Get a milestone

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
    id := "id_example" // string | the milestone to get, identified by ID and if not available by name

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetMilestone(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetMilestone``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetMilestone`: Milestone
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetMilestone`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **string** | the milestone to get, identified by ID and if not available by name | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetMilestoneRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetMilestonesList

> []Milestone IssueGetMilestonesList(ctx, owner, repo).State(state).Name(name).Page(page).Limit(limit).Execute()

Get all of a repository's opened milestones

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
    state := "state_example" // string | Milestone state, Recognized values are open, closed and all. Defaults to \"open\" (optional)
    name := "name_example" // string | filter by milestone name (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetMilestonesList(context.Background(), owner, repo).State(state).Name(name).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetMilestonesList``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetMilestonesList`: []Milestone
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetMilestonesList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetMilestonesListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **state** | **string** | Milestone state, Recognized values are open, closed and all. Defaults to \&quot;open\&quot; | 
 **name** | **string** | filter by milestone name | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueGetRepoComments

> []Comment IssueGetRepoComments(ctx, owner, repo).Since(since).Before(before).Page(page).Limit(limit).Execute()

List all comments in a repository

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
    since := time.Now() // time.Time | if provided, only comments updated since the provided time are returned. (optional)
    before := time.Now() // time.Time | if provided, only comments updated before the provided time are returned. (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueGetRepoComments(context.Background(), owner, repo).Since(since).Before(before).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueGetRepoComments``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueGetRepoComments`: []Comment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueGetRepoComments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueGetRepoCommentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **since** | **time.Time** | if provided, only comments updated since the provided time are returned. | 
 **before** | **time.Time** | if provided, only comments updated before the provided time are returned. | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueListBlocks

> []Issue IssueListBlocks(ctx, owner, repo, index).Page(page).Limit(limit).Execute()

List issues that are blocked by this issue

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
    index := "index_example" // string | index of the issue
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueListBlocks(context.Background(), owner, repo, index).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueListBlocks``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueListBlocks`: []Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueListBlocks`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **string** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueListBlocksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

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


## IssueListIssueAttachments

> []Attachment IssueListIssueAttachments(ctx, owner, repo, index).Execute()

List issue's attachments

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
    index := int64(789) // int64 | index of the issue

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueListIssueAttachments(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueListIssueAttachments``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueListIssueAttachments`: []Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueListIssueAttachments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueListIssueAttachmentsRequest struct via the builder pattern


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


## IssueListIssueCommentAttachments

> []Attachment IssueListIssueCommentAttachments(ctx, owner, repo, id).Execute()

List comment's attachments

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
    id := int64(789) // int64 | id of the comment

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueListIssueCommentAttachments(context.Background(), owner, repo, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueListIssueCommentAttachments``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueListIssueCommentAttachments`: []Attachment
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueListIssueCommentAttachments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueListIssueCommentAttachmentsRequest struct via the builder pattern


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


## IssueListIssueDependencies

> []Issue IssueListIssueDependencies(ctx, owner, repo, index).Page(page).Limit(limit).Execute()

List an issue's dependencies, i.e all issues that block this issue.

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
    index := "index_example" // string | index of the issue
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueListIssueDependencies(context.Background(), owner, repo, index).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueListIssueDependencies``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueListIssueDependencies`: []Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueListIssueDependencies`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **string** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueListIssueDependenciesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

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


## IssueListIssues

> []Issue IssueListIssues(ctx, owner, repo).State(state).Labels(labels).Q(q).Type_(type_).Milestones(milestones).Since(since).Before(before).CreatedBy(createdBy).AssignedBy(assignedBy).MentionedBy(mentionedBy).Page(page).Limit(limit).Execute()

List a repository's issues

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
    state := "state_example" // string | whether issue is open or closed (optional)
    labels := "labels_example" // string | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded (optional)
    q := "q_example" // string | search string (optional)
    type_ := "type__example" // string | filter by type (issues / pulls) if set (optional)
    milestones := "milestones_example" // string | comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded (optional)
    since := time.Now() // time.Time | Only show items updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before := time.Now() // time.Time | Only show items updated before the given time. This is a timestamp in RFC 3339 format (optional)
    createdBy := "createdBy_example" // string | Only show items which were created by the the given user (optional)
    assignedBy := "assignedBy_example" // string | Only show items for which the given user is assigned (optional)
    mentionedBy := "mentionedBy_example" // string | Only show items in which the given user was mentioned (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueListIssues(context.Background(), owner, repo).State(state).Labels(labels).Q(q).Type_(type_).Milestones(milestones).Since(since).Before(before).CreatedBy(createdBy).AssignedBy(assignedBy).MentionedBy(mentionedBy).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueListIssues``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueListIssues`: []Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueListIssues`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueListIssuesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **state** | **string** | whether issue is open or closed | 
 **labels** | **string** | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded | 
 **q** | **string** | search string | 
 **type_** | **string** | filter by type (issues / pulls) if set | 
 **milestones** | **string** | comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded | 
 **since** | **time.Time** | Only show items updated after the given time. This is a timestamp in RFC 3339 format | 
 **before** | **time.Time** | Only show items updated before the given time. This is a timestamp in RFC 3339 format | 
 **createdBy** | **string** | Only show items which were created by the the given user | 
 **assignedBy** | **string** | Only show items for which the given user is assigned | 
 **mentionedBy** | **string** | Only show items in which the given user was mentioned | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

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


## IssueListLabels

> []Label IssueListLabels(ctx, owner, repo).Page(page).Limit(limit).Execute()

Get all of a repository's labels

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
    resp, r, err := api_client.IssueApi.IssueListLabels(context.Background(), owner, repo).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueListLabels``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueListLabels`: []Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueListLabels`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueListLabelsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssuePostCommentReaction

> Reaction IssuePostCommentReaction(ctx, owner, repo, id).Content(content).Execute()

Add a reaction to a comment of an issue

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
    id := int64(789) // int64 | id of the comment to edit
    content := *openapiclient.NewEditReactionOption() // EditReactionOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssuePostCommentReaction(context.Background(), owner, repo, id).Content(content).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssuePostCommentReaction``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssuePostCommentReaction`: Reaction
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssuePostCommentReaction`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**id** | **int64** | id of the comment to edit | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssuePostCommentReactionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **content** | [**EditReactionOption**](EditReactionOption.md) |  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssuePostIssueReaction

> Reaction IssuePostIssueReaction(ctx, owner, repo, index).Content(content).Execute()

Add a reaction to an issue

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
    index := int64(789) // int64 | index of the issue
    content := *openapiclient.NewEditReactionOption() // EditReactionOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssuePostIssueReaction(context.Background(), owner, repo, index).Content(content).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssuePostIssueReaction``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssuePostIssueReaction`: Reaction
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssuePostIssueReaction`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssuePostIssueReactionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **content** | [**EditReactionOption**](EditReactionOption.md) |  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueRemoveIssueBlocking

> Issue IssueRemoveIssueBlocking(ctx, owner, repo, index).Body(body).Execute()

Unblock the issue given in the body by the issue in path

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
    index := "index_example" // string | index of the issue
    body := *openapiclient.NewIssueMeta() // IssueMeta |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueRemoveIssueBlocking(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueRemoveIssueBlocking``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueRemoveIssueBlocking`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueRemoveIssueBlocking`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **string** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueRemoveIssueBlockingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**IssueMeta**](IssueMeta.md) |  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueRemoveIssueDependencies

> Issue IssueRemoveIssueDependencies(ctx, owner, repo, index).Body(body).Execute()

Remove an issue dependency

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
    index := "index_example" // string | index of the issue
    body := *openapiclient.NewIssueMeta() // IssueMeta |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueRemoveIssueDependencies(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueRemoveIssueDependencies``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueRemoveIssueDependencies`: Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueRemoveIssueDependencies`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **string** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueRemoveIssueDependenciesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**IssueMeta**](IssueMeta.md) |  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueRemoveLabel

> IssueRemoveLabel(ctx, owner, repo, index, id).Execute()

Remove a label from an issue

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
    index := int64(789) // int64 | index of the issue
    id := int64(789) // int64 | id of the label to remove

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueRemoveLabel(context.Background(), owner, repo, index, id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueRemoveLabel``: %v\n", err)
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
**index** | **int64** | index of the issue | 
**id** | **int64** | id of the label to remove | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueRemoveLabelRequest struct via the builder pattern


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


## IssueReplaceLabels

> []Label IssueReplaceLabels(ctx, owner, repo, index).Body(body).Execute()

Replace an issue's labels

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
    index := int64(789) // int64 | index of the issue
    body := *openapiclient.NewIssueLabelsOption() // IssueLabelsOption |  (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueReplaceLabels(context.Background(), owner, repo, index).Body(body).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueReplaceLabels``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueReplaceLabels`: []Label
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueReplaceLabels`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueReplaceLabelsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **body** | [**IssueLabelsOption**](IssueLabelsOption.md) |  | 

### Return type

[**[]Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IssueResetTime

> IssueResetTime(ctx, owner, repo, index).Execute()

Reset a tracked time of an issue

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
    index := int64(789) // int64 | index of the issue to add tracked time to

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueResetTime(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueResetTime``: %v\n", err)
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
**index** | **int64** | index of the issue to add tracked time to | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueResetTimeRequest struct via the builder pattern


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


## IssueSearchIssues

> []Issue IssueSearchIssues(ctx).State(state).Labels(labels).Milestones(milestones).Q(q).PriorityRepoId(priorityRepoId).Type_(type_).Since(since).Before(before).Assigned(assigned).Created(created).Mentioned(mentioned).ReviewRequested(reviewRequested).Reviewed(reviewed).Owner(owner).Team(team).Page(page).Limit(limit).Execute()

Search for issues across the repositories that the user has access to

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
    state := "state_example" // string | whether issue is open or closed (optional)
    labels := "labels_example" // string | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded (optional)
    milestones := "milestones_example" // string | comma separated list of milestone names. Fetch only issues that have any of this milestones. Non existent are discarded (optional)
    q := "q_example" // string | search string (optional)
    priorityRepoId := int64(789) // int64 | repository to prioritize in the results (optional)
    type_ := "type__example" // string | filter by type (issues / pulls) if set (optional)
    since := time.Now() // time.Time | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before := time.Now() // time.Time | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format (optional)
    assigned := true // bool | filter (issues / pulls) assigned to you, default is false (optional)
    created := true // bool | filter (issues / pulls) created by you, default is false (optional)
    mentioned := true // bool | filter (issues / pulls) mentioning you, default is false (optional)
    reviewRequested := true // bool | filter pulls requesting your review, default is false (optional)
    reviewed := true // bool | filter pulls reviewed by you, default is false (optional)
    owner := "owner_example" // string | filter by owner (optional)
    team := "team_example" // string | filter by team (requires organization owner parameter to be provided) (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueSearchIssues(context.Background()).State(state).Labels(labels).Milestones(milestones).Q(q).PriorityRepoId(priorityRepoId).Type_(type_).Since(since).Before(before).Assigned(assigned).Created(created).Mentioned(mentioned).ReviewRequested(reviewRequested).Reviewed(reviewed).Owner(owner).Team(team).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueSearchIssues``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueSearchIssues`: []Issue
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueSearchIssues`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiIssueSearchIssuesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **string** | whether issue is open or closed | 
 **labels** | **string** | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded | 
 **milestones** | **string** | comma separated list of milestone names. Fetch only issues that have any of this milestones. Non existent are discarded | 
 **q** | **string** | search string | 
 **priorityRepoId** | **int64** | repository to prioritize in the results | 
 **type_** | **string** | filter by type (issues / pulls) if set | 
 **since** | **time.Time** | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format | 
 **before** | **time.Time** | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format | 
 **assigned** | **bool** | filter (issues / pulls) assigned to you, default is false | 
 **created** | **bool** | filter (issues / pulls) created by you, default is false | 
 **mentioned** | **bool** | filter (issues / pulls) mentioning you, default is false | 
 **reviewRequested** | **bool** | filter pulls requesting your review, default is false | 
 **reviewed** | **bool** | filter pulls reviewed by you, default is false | 
 **owner** | **string** | filter by owner | 
 **team** | **string** | filter by team (requires organization owner parameter to be provided) | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

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


## IssueStartStopWatch

> IssueStartStopWatch(ctx, owner, repo, index).Execute()

Start stopwatch on an issue.

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
    index := int64(789) // int64 | index of the issue to create the stopwatch on

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueStartStopWatch(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueStartStopWatch``: %v\n", err)
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
**index** | **int64** | index of the issue to create the stopwatch on | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueStartStopWatchRequest struct via the builder pattern


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


## IssueStopStopWatch

> IssueStopStopWatch(ctx, owner, repo, index).Execute()

Stop an issue's existing stopwatch.

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
    index := int64(789) // int64 | index of the issue to stop the stopwatch on

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueStopStopWatch(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueStopStopWatch``: %v\n", err)
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
**index** | **int64** | index of the issue to stop the stopwatch on | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueStopStopWatchRequest struct via the builder pattern


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


## IssueSubscriptions

> []User IssueSubscriptions(ctx, owner, repo, index).Page(page).Limit(limit).Execute()

Get users who subscribed on an issue.

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
    index := int64(789) // int64 | index of the issue
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueSubscriptions(context.Background(), owner, repo, index).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueSubscriptions``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueSubscriptions`: []User
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueSubscriptions`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueSubscriptionsRequest struct via the builder pattern


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


## IssueTrackedTimes

> []TrackedTime IssueTrackedTimes(ctx, owner, repo, index).User(user).Since(since).Before(before).Page(page).Limit(limit).Execute()

List an issue's tracked times

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
    index := int64(789) // int64 | index of the issue
    user := "user_example" // string | optional filter by user (available for issue managers) (optional)
    since := time.Now() // time.Time | Only show times updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before := time.Now() // time.Time | Only show times updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.IssueTrackedTimes(context.Background(), owner, repo, index).User(user).Since(since).Before(before).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.IssueTrackedTimes``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `IssueTrackedTimes`: []TrackedTime
    fmt.Fprintf(os.Stdout, "Response from `IssueApi.IssueTrackedTimes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 
**index** | **int64** | index of the issue | 

### Other Parameters

Other parameters are passed through a pointer to a apiIssueTrackedTimesRequest struct via the builder pattern


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


## MoveIssuePin

> MoveIssuePin(ctx, owner, repo, index, position).Execute()

Moves the Pin to the given Position

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
    index := int64(789) // int64 | index of issue
    position := int64(789) // int64 | the new position

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.MoveIssuePin(context.Background(), owner, repo, index, position).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.MoveIssuePin``: %v\n", err)
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
**index** | **int64** | index of issue | 
**position** | **int64** | the new position | 

### Other Parameters

Other parameters are passed through a pointer to a apiMoveIssuePinRequest struct via the builder pattern


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


## PinIssue

> PinIssue(ctx, owner, repo, index).Execute()

Pin an Issue

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
    index := int64(789) // int64 | index of issue to pin

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.PinIssue(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.PinIssue``: %v\n", err)
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
**index** | **int64** | index of issue to pin | 

### Other Parameters

Other parameters are passed through a pointer to a apiPinIssueRequest struct via the builder pattern


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


## UnpinIssue

> UnpinIssue(ctx, owner, repo, index).Execute()

Unpin an Issue

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
    index := int64(789) // int64 | index of issue to unpin

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.IssueApi.UnpinIssue(context.Background(), owner, repo, index).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IssueApi.UnpinIssue``: %v\n", err)
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
**index** | **int64** | index of issue to unpin | 

### Other Parameters

Other parameters are passed through a pointer to a apiUnpinIssueRequest struct via the builder pattern


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


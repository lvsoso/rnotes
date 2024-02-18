# \NotificationApi

All URIs are relative to *http://}/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**NotifyGetList**](NotificationApi.md#NotifyGetList) | **Get** /notifications | List users&#39;s notification threads
[**NotifyGetRepoList**](NotificationApi.md#NotifyGetRepoList) | **Get** /repos/{owner}/{repo}/notifications | List users&#39;s notification threads on a specific repo
[**NotifyGetThread**](NotificationApi.md#NotifyGetThread) | **Get** /notifications/threads/{id} | Get notification thread by ID
[**NotifyNewAvailable**](NotificationApi.md#NotifyNewAvailable) | **Get** /notifications/new | Check if unread notifications exist
[**NotifyReadList**](NotificationApi.md#NotifyReadList) | **Put** /notifications | Mark notification threads as read, pinned or unread
[**NotifyReadRepoList**](NotificationApi.md#NotifyReadRepoList) | **Put** /repos/{owner}/{repo}/notifications | Mark notification threads as read, pinned or unread on a specific repo
[**NotifyReadThread**](NotificationApi.md#NotifyReadThread) | **Patch** /notifications/threads/{id} | Mark notification thread as read by ID



## NotifyGetList

> []NotificationThread NotifyGetList(ctx).All(all).StatusTypes(statusTypes).SubjectType(subjectType).Since(since).Before(before).Page(page).Limit(limit).Execute()

List users's notification threads

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
    all := true // bool | If true, show notifications marked as read. Default value is false (optional)
    statusTypes := []string{"Inner_example"} // []string | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned. (optional)
    subjectType := []string{"SubjectType_example"} // []string | filter notifications by subject type (optional)
    since := time.Now() // time.Time | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before := time.Now() // time.Time | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyGetList(context.Background()).All(all).StatusTypes(statusTypes).SubjectType(subjectType).Since(since).Before(before).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyGetList``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyGetList`: []NotificationThread
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyGetList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiNotifyGetListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool** | If true, show notifications marked as read. Default value is false | 
 **statusTypes** | **[]string** | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread &amp; pinned. | 
 **subjectType** | **[]string** | filter notifications by subject type | 
 **since** | **time.Time** | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format | 
 **before** | **time.Time** | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NotifyGetRepoList

> []NotificationThread NotifyGetRepoList(ctx, owner, repo).All(all).StatusTypes(statusTypes).SubjectType(subjectType).Since(since).Before(before).Page(page).Limit(limit).Execute()

List users's notification threads on a specific repo

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
    all := true // bool | If true, show notifications marked as read. Default value is false (optional)
    statusTypes := []string{"Inner_example"} // []string | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned (optional)
    subjectType := []string{"SubjectType_example"} // []string | filter notifications by subject type (optional)
    since := time.Now() // time.Time | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before := time.Now() // time.Time | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyGetRepoList(context.Background(), owner, repo).All(all).StatusTypes(statusTypes).SubjectType(subjectType).Since(since).Before(before).Page(page).Limit(limit).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyGetRepoList``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyGetRepoList`: []NotificationThread
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyGetRepoList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiNotifyGetRepoListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **all** | **bool** | If true, show notifications marked as read. Default value is false | 
 **statusTypes** | **[]string** | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread &amp; pinned | 
 **subjectType** | **[]string** | filter notifications by subject type | 
 **since** | **time.Time** | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format | 
 **before** | **time.Time** | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format | 
 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 

### Return type

[**[]NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NotifyGetThread

> NotificationThread NotifyGetThread(ctx, id).Execute()

Get notification thread by ID

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
    id := "id_example" // string | id of notification thread

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyGetThread(context.Background(), id).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyGetThread``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyGetThread`: NotificationThread
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyGetThread`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | id of notification thread | 

### Other Parameters

Other parameters are passed through a pointer to a apiNotifyGetThreadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NotifyNewAvailable

> NotificationCount NotifyNewAvailable(ctx).Execute()

Check if unread notifications exist

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

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyNewAvailable(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyNewAvailable``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyNewAvailable`: NotificationCount
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyNewAvailable`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiNotifyNewAvailableRequest struct via the builder pattern


### Return type

[**NotificationCount**](NotificationCount.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NotifyReadList

> []NotificationThread NotifyReadList(ctx).LastReadAt(lastReadAt).All(all).StatusTypes(statusTypes).ToStatus(toStatus).Execute()

Mark notification threads as read, pinned or unread

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
    lastReadAt := time.Now() // time.Time | Describes the last point that notifications were checked. Anything updated since this time will not be updated. (optional)
    all := "all_example" // string | If true, mark all notifications on this repo. Default value is false (optional)
    statusTypes := []string{"Inner_example"} // []string | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. (optional)
    toStatus := "toStatus_example" // string | Status to mark notifications as, Defaults to read. (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyReadList(context.Background()).LastReadAt(lastReadAt).All(all).StatusTypes(statusTypes).ToStatus(toStatus).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyReadList``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyReadList`: []NotificationThread
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyReadList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiNotifyReadListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lastReadAt** | **time.Time** | Describes the last point that notifications were checked. Anything updated since this time will not be updated. | 
 **all** | **string** | If true, mark all notifications on this repo. Default value is false | 
 **statusTypes** | **[]string** | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. | 
 **toStatus** | **string** | Status to mark notifications as, Defaults to read. | 

### Return type

[**[]NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NotifyReadRepoList

> []NotificationThread NotifyReadRepoList(ctx, owner, repo).All(all).StatusTypes(statusTypes).ToStatus(toStatus).LastReadAt(lastReadAt).Execute()

Mark notification threads as read, pinned or unread on a specific repo

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
    all := "all_example" // string | If true, mark all notifications on this repo. Default value is false (optional)
    statusTypes := []string{"Inner_example"} // []string | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. (optional)
    toStatus := "toStatus_example" // string | Status to mark notifications as. Defaults to read. (optional)
    lastReadAt := time.Now() // time.Time | Describes the last point that notifications were checked. Anything updated since this time will not be updated. (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyReadRepoList(context.Background(), owner, repo).All(all).StatusTypes(statusTypes).ToStatus(toStatus).LastReadAt(lastReadAt).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyReadRepoList``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyReadRepoList`: []NotificationThread
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyReadRepoList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the repo | 
**repo** | **string** | name of the repo | 

### Other Parameters

Other parameters are passed through a pointer to a apiNotifyReadRepoListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **all** | **string** | If true, mark all notifications on this repo. Default value is false | 
 **statusTypes** | **[]string** | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. | 
 **toStatus** | **string** | Status to mark notifications as. Defaults to read. | 
 **lastReadAt** | **time.Time** | Describes the last point that notifications were checked. Anything updated since this time will not be updated. | 

### Return type

[**[]NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## NotifyReadThread

> NotificationThread NotifyReadThread(ctx, id).ToStatus(toStatus).Execute()

Mark notification thread as read by ID

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
    id := "id_example" // string | id of notification thread
    toStatus := "toStatus_example" // string | Status to mark notifications as (optional) (default to "read")

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.NotificationApi.NotifyReadThread(context.Background(), id).ToStatus(toStatus).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `NotificationApi.NotifyReadThread``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `NotifyReadThread`: NotificationThread
    fmt.Fprintf(os.Stdout, "Response from `NotificationApi.NotifyReadThread`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | id of notification thread | 

### Other Parameters

Other parameters are passed through a pointer to a apiNotifyReadThreadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **toStatus** | **string** | Status to mark notifications as | [default to &quot;read&quot;]

### Return type

[**NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


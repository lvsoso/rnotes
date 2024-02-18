# \SettingsApi

All URIs are relative to *http://}/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetGeneralAPISettings**](SettingsApi.md#GetGeneralAPISettings) | **Get** /settings/api | Get instance&#39;s global settings for api
[**GetGeneralAttachmentSettings**](SettingsApi.md#GetGeneralAttachmentSettings) | **Get** /settings/attachment | Get instance&#39;s global settings for Attachment
[**GetGeneralRepositorySettings**](SettingsApi.md#GetGeneralRepositorySettings) | **Get** /settings/repository | Get instance&#39;s global settings for repositories
[**GetGeneralUISettings**](SettingsApi.md#GetGeneralUISettings) | **Get** /settings/ui | Get instance&#39;s global settings for ui



## GetGeneralAPISettings

> GeneralAPISettings GetGeneralAPISettings(ctx).Execute()

Get instance's global settings for api

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
    resp, r, err := api_client.SettingsApi.GetGeneralAPISettings(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SettingsApi.GetGeneralAPISettings``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetGeneralAPISettings`: GeneralAPISettings
    fmt.Fprintf(os.Stdout, "Response from `SettingsApi.GetGeneralAPISettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetGeneralAPISettingsRequest struct via the builder pattern


### Return type

[**GeneralAPISettings**](GeneralAPISettings.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGeneralAttachmentSettings

> GeneralAttachmentSettings GetGeneralAttachmentSettings(ctx).Execute()

Get instance's global settings for Attachment

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
    resp, r, err := api_client.SettingsApi.GetGeneralAttachmentSettings(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SettingsApi.GetGeneralAttachmentSettings``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetGeneralAttachmentSettings`: GeneralAttachmentSettings
    fmt.Fprintf(os.Stdout, "Response from `SettingsApi.GetGeneralAttachmentSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetGeneralAttachmentSettingsRequest struct via the builder pattern


### Return type

[**GeneralAttachmentSettings**](GeneralAttachmentSettings.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGeneralRepositorySettings

> GeneralRepoSettings GetGeneralRepositorySettings(ctx).Execute()

Get instance's global settings for repositories

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
    resp, r, err := api_client.SettingsApi.GetGeneralRepositorySettings(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SettingsApi.GetGeneralRepositorySettings``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetGeneralRepositorySettings`: GeneralRepoSettings
    fmt.Fprintf(os.Stdout, "Response from `SettingsApi.GetGeneralRepositorySettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetGeneralRepositorySettingsRequest struct via the builder pattern


### Return type

[**GeneralRepoSettings**](GeneralRepoSettings.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGeneralUISettings

> GeneralUISettings GetGeneralUISettings(ctx).Execute()

Get instance's global settings for ui

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
    resp, r, err := api_client.SettingsApi.GetGeneralUISettings(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SettingsApi.GetGeneralUISettings``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetGeneralUISettings`: GeneralUISettings
    fmt.Fprintf(os.Stdout, "Response from `SettingsApi.GetGeneralUISettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetGeneralUISettingsRequest struct via the builder pattern


### Return type

[**GeneralUISettings**](GeneralUISettings.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


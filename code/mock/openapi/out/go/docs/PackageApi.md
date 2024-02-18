# \PackageApi

All URIs are relative to *http://}/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeletePackage**](PackageApi.md#DeletePackage) | **Delete** /packages/{owner}/{type}/{name}/{version} | Delete a package
[**GetPackage**](PackageApi.md#GetPackage) | **Get** /packages/{owner}/{type}/{name}/{version} | Gets a package
[**ListPackageFiles**](PackageApi.md#ListPackageFiles) | **Get** /packages/{owner}/{type}/{name}/{version}/files | Gets all files of a package
[**ListPackages**](PackageApi.md#ListPackages) | **Get** /packages/{owner} | Gets all packages of an owner



## DeletePackage

> DeletePackage(ctx, owner, type_, name, version).Execute()

Delete a package

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
    owner := "owner_example" // string | owner of the package
    type_ := "type__example" // string | type of the package
    name := "name_example" // string | name of the package
    version := "version_example" // string | version of the package

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.PackageApi.DeletePackage(context.Background(), owner, type_, name, version).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PackageApi.DeletePackage``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the package | 
**type_** | **string** | type of the package | 
**name** | **string** | name of the package | 
**version** | **string** | version of the package | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeletePackageRequest struct via the builder pattern


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


## GetPackage

> Package GetPackage(ctx, owner, type_, name, version).Execute()

Gets a package

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
    owner := "owner_example" // string | owner of the package
    type_ := "type__example" // string | type of the package
    name := "name_example" // string | name of the package
    version := "version_example" // string | version of the package

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.PackageApi.GetPackage(context.Background(), owner, type_, name, version).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PackageApi.GetPackage``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GetPackage`: Package
    fmt.Fprintf(os.Stdout, "Response from `PackageApi.GetPackage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the package | 
**type_** | **string** | type of the package | 
**name** | **string** | name of the package | 
**version** | **string** | version of the package | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetPackageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**Package**](Package.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListPackageFiles

> []PackageFile ListPackageFiles(ctx, owner, type_, name, version).Execute()

Gets all files of a package

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
    owner := "owner_example" // string | owner of the package
    type_ := "type__example" // string | type of the package
    name := "name_example" // string | name of the package
    version := "version_example" // string | version of the package

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.PackageApi.ListPackageFiles(context.Background(), owner, type_, name, version).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PackageApi.ListPackageFiles``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `ListPackageFiles`: []PackageFile
    fmt.Fprintf(os.Stdout, "Response from `PackageApi.ListPackageFiles`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the package | 
**type_** | **string** | type of the package | 
**name** | **string** | name of the package | 
**version** | **string** | version of the package | 

### Other Parameters

Other parameters are passed through a pointer to a apiListPackageFilesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**[]PackageFile**](PackageFile.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListPackages

> []Package ListPackages(ctx, owner).Page(page).Limit(limit).Type_(type_).Q(q).Execute()

Gets all packages of an owner

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
    owner := "owner_example" // string | owner of the packages
    page := int32(56) // int32 | page number of results to return (1-based) (optional)
    limit := int32(56) // int32 | page size of results (optional)
    type_ := "type__example" // string | package type filter (optional)
    q := "q_example" // string | name filter (optional)

    configuration := openapiclient.NewConfiguration()
    api_client := openapiclient.NewAPIClient(configuration)
    resp, r, err := api_client.PackageApi.ListPackages(context.Background(), owner).Page(page).Limit(limit).Type_(type_).Q(q).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `PackageApi.ListPackages``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `ListPackages`: []Package
    fmt.Fprintf(os.Stdout, "Response from `PackageApi.ListPackages`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**owner** | **string** | owner of the packages | 

### Other Parameters

Other parameters are passed through a pointer to a apiListPackagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | page number of results to return (1-based) | 
 **limit** | **int32** | page size of results | 
 **type_** | **string** | package type filter | 
 **q** | **string** | name filter | 

### Return type

[**[]Package**](Package.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


# IssueConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BlankIssuesEnabled** | Pointer to **bool** |  | [optional] 
**ContactLinks** | Pointer to [**[]IssueConfigContactLink**](IssueConfigContactLink.md) |  | [optional] 

## Methods

### NewIssueConfig

`func NewIssueConfig() *IssueConfig`

NewIssueConfig instantiates a new IssueConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIssueConfigWithDefaults

`func NewIssueConfigWithDefaults() *IssueConfig`

NewIssueConfigWithDefaults instantiates a new IssueConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBlankIssuesEnabled

`func (o *IssueConfig) GetBlankIssuesEnabled() bool`

GetBlankIssuesEnabled returns the BlankIssuesEnabled field if non-nil, zero value otherwise.

### GetBlankIssuesEnabledOk

`func (o *IssueConfig) GetBlankIssuesEnabledOk() (*bool, bool)`

GetBlankIssuesEnabledOk returns a tuple with the BlankIssuesEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBlankIssuesEnabled

`func (o *IssueConfig) SetBlankIssuesEnabled(v bool)`

SetBlankIssuesEnabled sets BlankIssuesEnabled field to given value.

### HasBlankIssuesEnabled

`func (o *IssueConfig) HasBlankIssuesEnabled() bool`

HasBlankIssuesEnabled returns a boolean if a field has been set.

### GetContactLinks

`func (o *IssueConfig) GetContactLinks() []IssueConfigContactLink`

GetContactLinks returns the ContactLinks field if non-nil, zero value otherwise.

### GetContactLinksOk

`func (o *IssueConfig) GetContactLinksOk() (*[]IssueConfigContactLink, bool)`

GetContactLinksOk returns a tuple with the ContactLinks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContactLinks

`func (o *IssueConfig) SetContactLinks(v []IssueConfigContactLink)`

SetContactLinks sets ContactLinks field to given value.

### HasContactLinks

`func (o *IssueConfig) HasContactLinks() bool`

HasContactLinks returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



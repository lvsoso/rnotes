# ExternalTracker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExternalTrackerFormat** | Pointer to **string** | External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index. | [optional] 
**ExternalTrackerRegexpPattern** | Pointer to **string** | External Issue Tracker issue regular expression | [optional] 
**ExternalTrackerStyle** | Pointer to **string** | External Issue Tracker Number Format, either &#x60;numeric&#x60;, &#x60;alphanumeric&#x60;, or &#x60;regexp&#x60; | [optional] 
**ExternalTrackerUrl** | Pointer to **string** | URL of external issue tracker. | [optional] 

## Methods

### NewExternalTracker

`func NewExternalTracker() *ExternalTracker`

NewExternalTracker instantiates a new ExternalTracker object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExternalTrackerWithDefaults

`func NewExternalTrackerWithDefaults() *ExternalTracker`

NewExternalTrackerWithDefaults instantiates a new ExternalTracker object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExternalTrackerFormat

`func (o *ExternalTracker) GetExternalTrackerFormat() string`

GetExternalTrackerFormat returns the ExternalTrackerFormat field if non-nil, zero value otherwise.

### GetExternalTrackerFormatOk

`func (o *ExternalTracker) GetExternalTrackerFormatOk() (*string, bool)`

GetExternalTrackerFormatOk returns a tuple with the ExternalTrackerFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalTrackerFormat

`func (o *ExternalTracker) SetExternalTrackerFormat(v string)`

SetExternalTrackerFormat sets ExternalTrackerFormat field to given value.

### HasExternalTrackerFormat

`func (o *ExternalTracker) HasExternalTrackerFormat() bool`

HasExternalTrackerFormat returns a boolean if a field has been set.

### GetExternalTrackerRegexpPattern

`func (o *ExternalTracker) GetExternalTrackerRegexpPattern() string`

GetExternalTrackerRegexpPattern returns the ExternalTrackerRegexpPattern field if non-nil, zero value otherwise.

### GetExternalTrackerRegexpPatternOk

`func (o *ExternalTracker) GetExternalTrackerRegexpPatternOk() (*string, bool)`

GetExternalTrackerRegexpPatternOk returns a tuple with the ExternalTrackerRegexpPattern field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalTrackerRegexpPattern

`func (o *ExternalTracker) SetExternalTrackerRegexpPattern(v string)`

SetExternalTrackerRegexpPattern sets ExternalTrackerRegexpPattern field to given value.

### HasExternalTrackerRegexpPattern

`func (o *ExternalTracker) HasExternalTrackerRegexpPattern() bool`

HasExternalTrackerRegexpPattern returns a boolean if a field has been set.

### GetExternalTrackerStyle

`func (o *ExternalTracker) GetExternalTrackerStyle() string`

GetExternalTrackerStyle returns the ExternalTrackerStyle field if non-nil, zero value otherwise.

### GetExternalTrackerStyleOk

`func (o *ExternalTracker) GetExternalTrackerStyleOk() (*string, bool)`

GetExternalTrackerStyleOk returns a tuple with the ExternalTrackerStyle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalTrackerStyle

`func (o *ExternalTracker) SetExternalTrackerStyle(v string)`

SetExternalTrackerStyle sets ExternalTrackerStyle field to given value.

### HasExternalTrackerStyle

`func (o *ExternalTracker) HasExternalTrackerStyle() bool`

HasExternalTrackerStyle returns a boolean if a field has been set.

### GetExternalTrackerUrl

`func (o *ExternalTracker) GetExternalTrackerUrl() string`

GetExternalTrackerUrl returns the ExternalTrackerUrl field if non-nil, zero value otherwise.

### GetExternalTrackerUrlOk

`func (o *ExternalTracker) GetExternalTrackerUrlOk() (*string, bool)`

GetExternalTrackerUrlOk returns a tuple with the ExternalTrackerUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalTrackerUrl

`func (o *ExternalTracker) SetExternalTrackerUrl(v string)`

SetExternalTrackerUrl sets ExternalTrackerUrl field to given value.

### HasExternalTrackerUrl

`func (o *ExternalTracker) HasExternalTrackerUrl() bool`

HasExternalTrackerUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PullRequestMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Draft** | Pointer to **bool** |  | [optional] 
**Merged** | Pointer to **bool** |  | [optional] 
**MergedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewPullRequestMeta

`func NewPullRequestMeta() *PullRequestMeta`

NewPullRequestMeta instantiates a new PullRequestMeta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPullRequestMetaWithDefaults

`func NewPullRequestMetaWithDefaults() *PullRequestMeta`

NewPullRequestMetaWithDefaults instantiates a new PullRequestMeta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDraft

`func (o *PullRequestMeta) GetDraft() bool`

GetDraft returns the Draft field if non-nil, zero value otherwise.

### GetDraftOk

`func (o *PullRequestMeta) GetDraftOk() (*bool, bool)`

GetDraftOk returns a tuple with the Draft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraft

`func (o *PullRequestMeta) SetDraft(v bool)`

SetDraft sets Draft field to given value.

### HasDraft

`func (o *PullRequestMeta) HasDraft() bool`

HasDraft returns a boolean if a field has been set.

### GetMerged

`func (o *PullRequestMeta) GetMerged() bool`

GetMerged returns the Merged field if non-nil, zero value otherwise.

### GetMergedOk

`func (o *PullRequestMeta) GetMergedOk() (*bool, bool)`

GetMergedOk returns a tuple with the Merged field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMerged

`func (o *PullRequestMeta) SetMerged(v bool)`

SetMerged sets Merged field to given value.

### HasMerged

`func (o *PullRequestMeta) HasMerged() bool`

HasMerged returns a boolean if a field has been set.

### GetMergedAt

`func (o *PullRequestMeta) GetMergedAt() time.Time`

GetMergedAt returns the MergedAt field if non-nil, zero value otherwise.

### GetMergedAtOk

`func (o *PullRequestMeta) GetMergedAtOk() (*time.Time, bool)`

GetMergedAtOk returns a tuple with the MergedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergedAt

`func (o *PullRequestMeta) SetMergedAt(v time.Time)`

SetMergedAt sets MergedAt field to given value.

### HasMergedAt

`func (o *PullRequestMeta) HasMergedAt() bool`

HasMergedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



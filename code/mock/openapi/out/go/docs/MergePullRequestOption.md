# MergePullRequestOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Do** | **string** |  | 
**MergeCommitID** | Pointer to **string** |  | [optional] 
**MergeMessageField** | Pointer to **string** |  | [optional] 
**MergeTitleField** | Pointer to **string** |  | [optional] 
**DeleteBranchAfterMerge** | Pointer to **bool** |  | [optional] 
**ForceMerge** | Pointer to **bool** |  | [optional] 
**HeadCommitId** | Pointer to **string** |  | [optional] 
**MergeWhenChecksSucceed** | Pointer to **bool** |  | [optional] 

## Methods

### NewMergePullRequestOption

`func NewMergePullRequestOption(do string, ) *MergePullRequestOption`

NewMergePullRequestOption instantiates a new MergePullRequestOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMergePullRequestOptionWithDefaults

`func NewMergePullRequestOptionWithDefaults() *MergePullRequestOption`

NewMergePullRequestOptionWithDefaults instantiates a new MergePullRequestOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDo

`func (o *MergePullRequestOption) GetDo() string`

GetDo returns the Do field if non-nil, zero value otherwise.

### GetDoOk

`func (o *MergePullRequestOption) GetDoOk() (*string, bool)`

GetDoOk returns a tuple with the Do field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDo

`func (o *MergePullRequestOption) SetDo(v string)`

SetDo sets Do field to given value.


### GetMergeCommitID

`func (o *MergePullRequestOption) GetMergeCommitID() string`

GetMergeCommitID returns the MergeCommitID field if non-nil, zero value otherwise.

### GetMergeCommitIDOk

`func (o *MergePullRequestOption) GetMergeCommitIDOk() (*string, bool)`

GetMergeCommitIDOk returns a tuple with the MergeCommitID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeCommitID

`func (o *MergePullRequestOption) SetMergeCommitID(v string)`

SetMergeCommitID sets MergeCommitID field to given value.

### HasMergeCommitID

`func (o *MergePullRequestOption) HasMergeCommitID() bool`

HasMergeCommitID returns a boolean if a field has been set.

### GetMergeMessageField

`func (o *MergePullRequestOption) GetMergeMessageField() string`

GetMergeMessageField returns the MergeMessageField field if non-nil, zero value otherwise.

### GetMergeMessageFieldOk

`func (o *MergePullRequestOption) GetMergeMessageFieldOk() (*string, bool)`

GetMergeMessageFieldOk returns a tuple with the MergeMessageField field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeMessageField

`func (o *MergePullRequestOption) SetMergeMessageField(v string)`

SetMergeMessageField sets MergeMessageField field to given value.

### HasMergeMessageField

`func (o *MergePullRequestOption) HasMergeMessageField() bool`

HasMergeMessageField returns a boolean if a field has been set.

### GetMergeTitleField

`func (o *MergePullRequestOption) GetMergeTitleField() string`

GetMergeTitleField returns the MergeTitleField field if non-nil, zero value otherwise.

### GetMergeTitleFieldOk

`func (o *MergePullRequestOption) GetMergeTitleFieldOk() (*string, bool)`

GetMergeTitleFieldOk returns a tuple with the MergeTitleField field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeTitleField

`func (o *MergePullRequestOption) SetMergeTitleField(v string)`

SetMergeTitleField sets MergeTitleField field to given value.

### HasMergeTitleField

`func (o *MergePullRequestOption) HasMergeTitleField() bool`

HasMergeTitleField returns a boolean if a field has been set.

### GetDeleteBranchAfterMerge

`func (o *MergePullRequestOption) GetDeleteBranchAfterMerge() bool`

GetDeleteBranchAfterMerge returns the DeleteBranchAfterMerge field if non-nil, zero value otherwise.

### GetDeleteBranchAfterMergeOk

`func (o *MergePullRequestOption) GetDeleteBranchAfterMergeOk() (*bool, bool)`

GetDeleteBranchAfterMergeOk returns a tuple with the DeleteBranchAfterMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeleteBranchAfterMerge

`func (o *MergePullRequestOption) SetDeleteBranchAfterMerge(v bool)`

SetDeleteBranchAfterMerge sets DeleteBranchAfterMerge field to given value.

### HasDeleteBranchAfterMerge

`func (o *MergePullRequestOption) HasDeleteBranchAfterMerge() bool`

HasDeleteBranchAfterMerge returns a boolean if a field has been set.

### GetForceMerge

`func (o *MergePullRequestOption) GetForceMerge() bool`

GetForceMerge returns the ForceMerge field if non-nil, zero value otherwise.

### GetForceMergeOk

`func (o *MergePullRequestOption) GetForceMergeOk() (*bool, bool)`

GetForceMergeOk returns a tuple with the ForceMerge field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetForceMerge

`func (o *MergePullRequestOption) SetForceMerge(v bool)`

SetForceMerge sets ForceMerge field to given value.

### HasForceMerge

`func (o *MergePullRequestOption) HasForceMerge() bool`

HasForceMerge returns a boolean if a field has been set.

### GetHeadCommitId

`func (o *MergePullRequestOption) GetHeadCommitId() string`

GetHeadCommitId returns the HeadCommitId field if non-nil, zero value otherwise.

### GetHeadCommitIdOk

`func (o *MergePullRequestOption) GetHeadCommitIdOk() (*string, bool)`

GetHeadCommitIdOk returns a tuple with the HeadCommitId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeadCommitId

`func (o *MergePullRequestOption) SetHeadCommitId(v string)`

SetHeadCommitId sets HeadCommitId field to given value.

### HasHeadCommitId

`func (o *MergePullRequestOption) HasHeadCommitId() bool`

HasHeadCommitId returns a boolean if a field has been set.

### GetMergeWhenChecksSucceed

`func (o *MergePullRequestOption) GetMergeWhenChecksSucceed() bool`

GetMergeWhenChecksSucceed returns the MergeWhenChecksSucceed field if non-nil, zero value otherwise.

### GetMergeWhenChecksSucceedOk

`func (o *MergePullRequestOption) GetMergeWhenChecksSucceedOk() (*bool, bool)`

GetMergeWhenChecksSucceedOk returns a tuple with the MergeWhenChecksSucceed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMergeWhenChecksSucceed

`func (o *MergePullRequestOption) SetMergeWhenChecksSucceed(v bool)`

SetMergeWhenChecksSucceed sets MergeWhenChecksSucceed field to given value.

### HasMergeWhenChecksSucceed

`func (o *MergePullRequestOption) HasMergeWhenChecksSucceed() bool`

HasMergeWhenChecksSucceed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



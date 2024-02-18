# EditPullRequestOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AllowMaintainerEdit** | Pointer to **bool** |  | [optional] 
**Assignee** | Pointer to **string** |  | [optional] 
**Assignees** | Pointer to **[]string** |  | [optional] 
**Base** | Pointer to **string** |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**DueDate** | Pointer to **time.Time** |  | [optional] 
**Labels** | Pointer to **[]int64** |  | [optional] 
**Milestone** | Pointer to **int64** |  | [optional] 
**State** | Pointer to **string** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**UnsetDueDate** | Pointer to **bool** |  | [optional] 

## Methods

### NewEditPullRequestOption

`func NewEditPullRequestOption() *EditPullRequestOption`

NewEditPullRequestOption instantiates a new EditPullRequestOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditPullRequestOptionWithDefaults

`func NewEditPullRequestOptionWithDefaults() *EditPullRequestOption`

NewEditPullRequestOptionWithDefaults instantiates a new EditPullRequestOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAllowMaintainerEdit

`func (o *EditPullRequestOption) GetAllowMaintainerEdit() bool`

GetAllowMaintainerEdit returns the AllowMaintainerEdit field if non-nil, zero value otherwise.

### GetAllowMaintainerEditOk

`func (o *EditPullRequestOption) GetAllowMaintainerEditOk() (*bool, bool)`

GetAllowMaintainerEditOk returns a tuple with the AllowMaintainerEdit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowMaintainerEdit

`func (o *EditPullRequestOption) SetAllowMaintainerEdit(v bool)`

SetAllowMaintainerEdit sets AllowMaintainerEdit field to given value.

### HasAllowMaintainerEdit

`func (o *EditPullRequestOption) HasAllowMaintainerEdit() bool`

HasAllowMaintainerEdit returns a boolean if a field has been set.

### GetAssignee

`func (o *EditPullRequestOption) GetAssignee() string`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *EditPullRequestOption) GetAssigneeOk() (*string, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *EditPullRequestOption) SetAssignee(v string)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *EditPullRequestOption) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssignees

`func (o *EditPullRequestOption) GetAssignees() []string`

GetAssignees returns the Assignees field if non-nil, zero value otherwise.

### GetAssigneesOk

`func (o *EditPullRequestOption) GetAssigneesOk() (*[]string, bool)`

GetAssigneesOk returns a tuple with the Assignees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignees

`func (o *EditPullRequestOption) SetAssignees(v []string)`

SetAssignees sets Assignees field to given value.

### HasAssignees

`func (o *EditPullRequestOption) HasAssignees() bool`

HasAssignees returns a boolean if a field has been set.

### GetBase

`func (o *EditPullRequestOption) GetBase() string`

GetBase returns the Base field if non-nil, zero value otherwise.

### GetBaseOk

`func (o *EditPullRequestOption) GetBaseOk() (*string, bool)`

GetBaseOk returns a tuple with the Base field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBase

`func (o *EditPullRequestOption) SetBase(v string)`

SetBase sets Base field to given value.

### HasBase

`func (o *EditPullRequestOption) HasBase() bool`

HasBase returns a boolean if a field has been set.

### GetBody

`func (o *EditPullRequestOption) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *EditPullRequestOption) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *EditPullRequestOption) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *EditPullRequestOption) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetDueDate

`func (o *EditPullRequestOption) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *EditPullRequestOption) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *EditPullRequestOption) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.

### HasDueDate

`func (o *EditPullRequestOption) HasDueDate() bool`

HasDueDate returns a boolean if a field has been set.

### GetLabels

`func (o *EditPullRequestOption) GetLabels() []int64`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *EditPullRequestOption) GetLabelsOk() (*[]int64, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *EditPullRequestOption) SetLabels(v []int64)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *EditPullRequestOption) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetMilestone

`func (o *EditPullRequestOption) GetMilestone() int64`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *EditPullRequestOption) GetMilestoneOk() (*int64, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *EditPullRequestOption) SetMilestone(v int64)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *EditPullRequestOption) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetState

`func (o *EditPullRequestOption) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *EditPullRequestOption) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *EditPullRequestOption) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *EditPullRequestOption) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *EditPullRequestOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *EditPullRequestOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *EditPullRequestOption) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *EditPullRequestOption) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetUnsetDueDate

`func (o *EditPullRequestOption) GetUnsetDueDate() bool`

GetUnsetDueDate returns the UnsetDueDate field if non-nil, zero value otherwise.

### GetUnsetDueDateOk

`func (o *EditPullRequestOption) GetUnsetDueDateOk() (*bool, bool)`

GetUnsetDueDateOk returns a tuple with the UnsetDueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnsetDueDate

`func (o *EditPullRequestOption) SetUnsetDueDate(v bool)`

SetUnsetDueDate sets UnsetDueDate field to given value.

### HasUnsetDueDate

`func (o *EditPullRequestOption) HasUnsetDueDate() bool`

HasUnsetDueDate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



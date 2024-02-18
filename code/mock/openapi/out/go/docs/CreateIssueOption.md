# CreateIssueOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assignee** | Pointer to **string** | deprecated | [optional] 
**Assignees** | Pointer to **[]string** |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**Closed** | Pointer to **bool** |  | [optional] 
**DueDate** | Pointer to **time.Time** |  | [optional] 
**Labels** | Pointer to **[]int64** | list of label ids | [optional] 
**Milestone** | Pointer to **int64** | milestone id | [optional] 
**Ref** | Pointer to **string** |  | [optional] 
**Title** | **string** |  | 

## Methods

### NewCreateIssueOption

`func NewCreateIssueOption(title string, ) *CreateIssueOption`

NewCreateIssueOption instantiates a new CreateIssueOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateIssueOptionWithDefaults

`func NewCreateIssueOptionWithDefaults() *CreateIssueOption`

NewCreateIssueOptionWithDefaults instantiates a new CreateIssueOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignee

`func (o *CreateIssueOption) GetAssignee() string`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *CreateIssueOption) GetAssigneeOk() (*string, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *CreateIssueOption) SetAssignee(v string)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *CreateIssueOption) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssignees

`func (o *CreateIssueOption) GetAssignees() []string`

GetAssignees returns the Assignees field if non-nil, zero value otherwise.

### GetAssigneesOk

`func (o *CreateIssueOption) GetAssigneesOk() (*[]string, bool)`

GetAssigneesOk returns a tuple with the Assignees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignees

`func (o *CreateIssueOption) SetAssignees(v []string)`

SetAssignees sets Assignees field to given value.

### HasAssignees

`func (o *CreateIssueOption) HasAssignees() bool`

HasAssignees returns a boolean if a field has been set.

### GetBody

`func (o *CreateIssueOption) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *CreateIssueOption) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *CreateIssueOption) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *CreateIssueOption) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetClosed

`func (o *CreateIssueOption) GetClosed() bool`

GetClosed returns the Closed field if non-nil, zero value otherwise.

### GetClosedOk

`func (o *CreateIssueOption) GetClosedOk() (*bool, bool)`

GetClosedOk returns a tuple with the Closed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosed

`func (o *CreateIssueOption) SetClosed(v bool)`

SetClosed sets Closed field to given value.

### HasClosed

`func (o *CreateIssueOption) HasClosed() bool`

HasClosed returns a boolean if a field has been set.

### GetDueDate

`func (o *CreateIssueOption) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *CreateIssueOption) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *CreateIssueOption) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.

### HasDueDate

`func (o *CreateIssueOption) HasDueDate() bool`

HasDueDate returns a boolean if a field has been set.

### GetLabels

`func (o *CreateIssueOption) GetLabels() []int64`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *CreateIssueOption) GetLabelsOk() (*[]int64, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *CreateIssueOption) SetLabels(v []int64)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *CreateIssueOption) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetMilestone

`func (o *CreateIssueOption) GetMilestone() int64`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *CreateIssueOption) GetMilestoneOk() (*int64, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *CreateIssueOption) SetMilestone(v int64)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *CreateIssueOption) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetRef

`func (o *CreateIssueOption) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *CreateIssueOption) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *CreateIssueOption) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *CreateIssueOption) HasRef() bool`

HasRef returns a boolean if a field has been set.

### GetTitle

`func (o *CreateIssueOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CreateIssueOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CreateIssueOption) SetTitle(v string)`

SetTitle sets Title field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



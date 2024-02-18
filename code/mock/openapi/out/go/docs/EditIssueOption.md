# EditIssueOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assignee** | Pointer to **string** | deprecated | [optional] 
**Assignees** | Pointer to **[]string** |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**DueDate** | Pointer to **time.Time** |  | [optional] 
**Milestone** | Pointer to **int64** |  | [optional] 
**Ref** | Pointer to **string** |  | [optional] 
**State** | Pointer to **string** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**UnsetDueDate** | Pointer to **bool** |  | [optional] 

## Methods

### NewEditIssueOption

`func NewEditIssueOption() *EditIssueOption`

NewEditIssueOption instantiates a new EditIssueOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditIssueOptionWithDefaults

`func NewEditIssueOptionWithDefaults() *EditIssueOption`

NewEditIssueOptionWithDefaults instantiates a new EditIssueOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignee

`func (o *EditIssueOption) GetAssignee() string`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *EditIssueOption) GetAssigneeOk() (*string, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *EditIssueOption) SetAssignee(v string)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *EditIssueOption) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssignees

`func (o *EditIssueOption) GetAssignees() []string`

GetAssignees returns the Assignees field if non-nil, zero value otherwise.

### GetAssigneesOk

`func (o *EditIssueOption) GetAssigneesOk() (*[]string, bool)`

GetAssigneesOk returns a tuple with the Assignees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignees

`func (o *EditIssueOption) SetAssignees(v []string)`

SetAssignees sets Assignees field to given value.

### HasAssignees

`func (o *EditIssueOption) HasAssignees() bool`

HasAssignees returns a boolean if a field has been set.

### GetBody

`func (o *EditIssueOption) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *EditIssueOption) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *EditIssueOption) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *EditIssueOption) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetDueDate

`func (o *EditIssueOption) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *EditIssueOption) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *EditIssueOption) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.

### HasDueDate

`func (o *EditIssueOption) HasDueDate() bool`

HasDueDate returns a boolean if a field has been set.

### GetMilestone

`func (o *EditIssueOption) GetMilestone() int64`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *EditIssueOption) GetMilestoneOk() (*int64, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *EditIssueOption) SetMilestone(v int64)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *EditIssueOption) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetRef

`func (o *EditIssueOption) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *EditIssueOption) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *EditIssueOption) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *EditIssueOption) HasRef() bool`

HasRef returns a boolean if a field has been set.

### GetState

`func (o *EditIssueOption) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *EditIssueOption) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *EditIssueOption) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *EditIssueOption) HasState() bool`

HasState returns a boolean if a field has been set.

### GetTitle

`func (o *EditIssueOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *EditIssueOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *EditIssueOption) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *EditIssueOption) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetUnsetDueDate

`func (o *EditIssueOption) GetUnsetDueDate() bool`

GetUnsetDueDate returns the UnsetDueDate field if non-nil, zero value otherwise.

### GetUnsetDueDateOk

`func (o *EditIssueOption) GetUnsetDueDateOk() (*bool, bool)`

GetUnsetDueDateOk returns a tuple with the UnsetDueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnsetDueDate

`func (o *EditIssueOption) SetUnsetDueDate(v bool)`

SetUnsetDueDate sets UnsetDueDate field to given value.

### HasUnsetDueDate

`func (o *EditIssueOption) HasUnsetDueDate() bool`

HasUnsetDueDate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



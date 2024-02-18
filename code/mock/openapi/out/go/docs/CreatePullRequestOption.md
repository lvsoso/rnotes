# CreatePullRequestOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assignee** | Pointer to **string** |  | [optional] 
**Assignees** | Pointer to **[]string** |  | [optional] 
**Base** | Pointer to **string** |  | [optional] 
**Body** | Pointer to **string** |  | [optional] 
**DueDate** | Pointer to **time.Time** |  | [optional] 
**Head** | Pointer to **string** |  | [optional] 
**Labels** | Pointer to **[]int64** |  | [optional] 
**Milestone** | Pointer to **int64** |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 

## Methods

### NewCreatePullRequestOption

`func NewCreatePullRequestOption() *CreatePullRequestOption`

NewCreatePullRequestOption instantiates a new CreatePullRequestOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreatePullRequestOptionWithDefaults

`func NewCreatePullRequestOptionWithDefaults() *CreatePullRequestOption`

NewCreatePullRequestOptionWithDefaults instantiates a new CreatePullRequestOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignee

`func (o *CreatePullRequestOption) GetAssignee() string`

GetAssignee returns the Assignee field if non-nil, zero value otherwise.

### GetAssigneeOk

`func (o *CreatePullRequestOption) GetAssigneeOk() (*string, bool)`

GetAssigneeOk returns a tuple with the Assignee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignee

`func (o *CreatePullRequestOption) SetAssignee(v string)`

SetAssignee sets Assignee field to given value.

### HasAssignee

`func (o *CreatePullRequestOption) HasAssignee() bool`

HasAssignee returns a boolean if a field has been set.

### GetAssignees

`func (o *CreatePullRequestOption) GetAssignees() []string`

GetAssignees returns the Assignees field if non-nil, zero value otherwise.

### GetAssigneesOk

`func (o *CreatePullRequestOption) GetAssigneesOk() (*[]string, bool)`

GetAssigneesOk returns a tuple with the Assignees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignees

`func (o *CreatePullRequestOption) SetAssignees(v []string)`

SetAssignees sets Assignees field to given value.

### HasAssignees

`func (o *CreatePullRequestOption) HasAssignees() bool`

HasAssignees returns a boolean if a field has been set.

### GetBase

`func (o *CreatePullRequestOption) GetBase() string`

GetBase returns the Base field if non-nil, zero value otherwise.

### GetBaseOk

`func (o *CreatePullRequestOption) GetBaseOk() (*string, bool)`

GetBaseOk returns a tuple with the Base field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBase

`func (o *CreatePullRequestOption) SetBase(v string)`

SetBase sets Base field to given value.

### HasBase

`func (o *CreatePullRequestOption) HasBase() bool`

HasBase returns a boolean if a field has been set.

### GetBody

`func (o *CreatePullRequestOption) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *CreatePullRequestOption) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *CreatePullRequestOption) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *CreatePullRequestOption) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetDueDate

`func (o *CreatePullRequestOption) GetDueDate() time.Time`

GetDueDate returns the DueDate field if non-nil, zero value otherwise.

### GetDueDateOk

`func (o *CreatePullRequestOption) GetDueDateOk() (*time.Time, bool)`

GetDueDateOk returns a tuple with the DueDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDueDate

`func (o *CreatePullRequestOption) SetDueDate(v time.Time)`

SetDueDate sets DueDate field to given value.

### HasDueDate

`func (o *CreatePullRequestOption) HasDueDate() bool`

HasDueDate returns a boolean if a field has been set.

### GetHead

`func (o *CreatePullRequestOption) GetHead() string`

GetHead returns the Head field if non-nil, zero value otherwise.

### GetHeadOk

`func (o *CreatePullRequestOption) GetHeadOk() (*string, bool)`

GetHeadOk returns a tuple with the Head field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHead

`func (o *CreatePullRequestOption) SetHead(v string)`

SetHead sets Head field to given value.

### HasHead

`func (o *CreatePullRequestOption) HasHead() bool`

HasHead returns a boolean if a field has been set.

### GetLabels

`func (o *CreatePullRequestOption) GetLabels() []int64`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *CreatePullRequestOption) GetLabelsOk() (*[]int64, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *CreatePullRequestOption) SetLabels(v []int64)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *CreatePullRequestOption) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetMilestone

`func (o *CreatePullRequestOption) GetMilestone() int64`

GetMilestone returns the Milestone field if non-nil, zero value otherwise.

### GetMilestoneOk

`func (o *CreatePullRequestOption) GetMilestoneOk() (*int64, bool)`

GetMilestoneOk returns a tuple with the Milestone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMilestone

`func (o *CreatePullRequestOption) SetMilestone(v int64)`

SetMilestone sets Milestone field to given value.

### HasMilestone

`func (o *CreatePullRequestOption) HasMilestone() bool`

HasMilestone returns a boolean if a field has been set.

### GetTitle

`func (o *CreatePullRequestOption) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CreatePullRequestOption) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CreatePullRequestOption) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *CreatePullRequestOption) HasTitle() bool`

HasTitle returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



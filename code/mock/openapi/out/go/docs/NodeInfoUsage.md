# NodeInfoUsage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LocalComments** | Pointer to **int64** |  | [optional] 
**LocalPosts** | Pointer to **int64** |  | [optional] 
**Users** | Pointer to [**NodeInfoUsageUsers**](NodeInfoUsageUsers.md) |  | [optional] 

## Methods

### NewNodeInfoUsage

`func NewNodeInfoUsage() *NodeInfoUsage`

NewNodeInfoUsage instantiates a new NodeInfoUsage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNodeInfoUsageWithDefaults

`func NewNodeInfoUsageWithDefaults() *NodeInfoUsage`

NewNodeInfoUsageWithDefaults instantiates a new NodeInfoUsage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLocalComments

`func (o *NodeInfoUsage) GetLocalComments() int64`

GetLocalComments returns the LocalComments field if non-nil, zero value otherwise.

### GetLocalCommentsOk

`func (o *NodeInfoUsage) GetLocalCommentsOk() (*int64, bool)`

GetLocalCommentsOk returns a tuple with the LocalComments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocalComments

`func (o *NodeInfoUsage) SetLocalComments(v int64)`

SetLocalComments sets LocalComments field to given value.

### HasLocalComments

`func (o *NodeInfoUsage) HasLocalComments() bool`

HasLocalComments returns a boolean if a field has been set.

### GetLocalPosts

`func (o *NodeInfoUsage) GetLocalPosts() int64`

GetLocalPosts returns the LocalPosts field if non-nil, zero value otherwise.

### GetLocalPostsOk

`func (o *NodeInfoUsage) GetLocalPostsOk() (*int64, bool)`

GetLocalPostsOk returns a tuple with the LocalPosts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocalPosts

`func (o *NodeInfoUsage) SetLocalPosts(v int64)`

SetLocalPosts sets LocalPosts field to given value.

### HasLocalPosts

`func (o *NodeInfoUsage) HasLocalPosts() bool`

HasLocalPosts returns a boolean if a field has been set.

### GetUsers

`func (o *NodeInfoUsage) GetUsers() NodeInfoUsageUsers`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *NodeInfoUsage) GetUsersOk() (*NodeInfoUsageUsers, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *NodeInfoUsage) SetUsers(v NodeInfoUsageUsers)`

SetUsers sets Users field to given value.

### HasUsers

`func (o *NodeInfoUsage) HasUsers() bool`

HasUsers returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



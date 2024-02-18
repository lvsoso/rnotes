# NotificationThread

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** |  | [optional] 
**Pinned** | Pointer to **bool** |  | [optional] 
**Repository** | Pointer to [**Repository**](Repository.md) |  | [optional] 
**Subject** | Pointer to [**NotificationSubject**](NotificationSubject.md) |  | [optional] 
**Unread** | Pointer to **bool** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewNotificationThread

`func NewNotificationThread() *NotificationThread`

NewNotificationThread instantiates a new NotificationThread object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNotificationThreadWithDefaults

`func NewNotificationThreadWithDefaults() *NotificationThread`

NewNotificationThreadWithDefaults instantiates a new NotificationThread object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *NotificationThread) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NotificationThread) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NotificationThread) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *NotificationThread) HasId() bool`

HasId returns a boolean if a field has been set.

### GetPinned

`func (o *NotificationThread) GetPinned() bool`

GetPinned returns the Pinned field if non-nil, zero value otherwise.

### GetPinnedOk

`func (o *NotificationThread) GetPinnedOk() (*bool, bool)`

GetPinnedOk returns a tuple with the Pinned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPinned

`func (o *NotificationThread) SetPinned(v bool)`

SetPinned sets Pinned field to given value.

### HasPinned

`func (o *NotificationThread) HasPinned() bool`

HasPinned returns a boolean if a field has been set.

### GetRepository

`func (o *NotificationThread) GetRepository() Repository`

GetRepository returns the Repository field if non-nil, zero value otherwise.

### GetRepositoryOk

`func (o *NotificationThread) GetRepositoryOk() (*Repository, bool)`

GetRepositoryOk returns a tuple with the Repository field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepository

`func (o *NotificationThread) SetRepository(v Repository)`

SetRepository sets Repository field to given value.

### HasRepository

`func (o *NotificationThread) HasRepository() bool`

HasRepository returns a boolean if a field has been set.

### GetSubject

`func (o *NotificationThread) GetSubject() NotificationSubject`

GetSubject returns the Subject field if non-nil, zero value otherwise.

### GetSubjectOk

`func (o *NotificationThread) GetSubjectOk() (*NotificationSubject, bool)`

GetSubjectOk returns a tuple with the Subject field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubject

`func (o *NotificationThread) SetSubject(v NotificationSubject)`

SetSubject sets Subject field to given value.

### HasSubject

`func (o *NotificationThread) HasSubject() bool`

HasSubject returns a boolean if a field has been set.

### GetUnread

`func (o *NotificationThread) GetUnread() bool`

GetUnread returns the Unread field if non-nil, zero value otherwise.

### GetUnreadOk

`func (o *NotificationThread) GetUnreadOk() (*bool, bool)`

GetUnreadOk returns a tuple with the Unread field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnread

`func (o *NotificationThread) SetUnread(v bool)`

SetUnread sets Unread field to given value.

### HasUnread

`func (o *NotificationThread) HasUnread() bool`

HasUnread returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *NotificationThread) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *NotificationThread) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *NotificationThread) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *NotificationThread) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetUrl

`func (o *NotificationThread) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *NotificationThread) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *NotificationThread) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *NotificationThread) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



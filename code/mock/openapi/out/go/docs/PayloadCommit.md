# PayloadCommit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Added** | Pointer to **[]string** |  | [optional] 
**Author** | Pointer to [**PayloadUser**](PayloadUser.md) |  | [optional] 
**Committer** | Pointer to [**PayloadUser**](PayloadUser.md) |  | [optional] 
**Id** | Pointer to **string** | sha1 hash of the commit | [optional] 
**Message** | Pointer to **string** |  | [optional] 
**Modified** | Pointer to **[]string** |  | [optional] 
**Removed** | Pointer to **[]string** |  | [optional] 
**Timestamp** | Pointer to **time.Time** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**Verification** | Pointer to [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Methods

### NewPayloadCommit

`func NewPayloadCommit() *PayloadCommit`

NewPayloadCommit instantiates a new PayloadCommit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPayloadCommitWithDefaults

`func NewPayloadCommitWithDefaults() *PayloadCommit`

NewPayloadCommitWithDefaults instantiates a new PayloadCommit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAdded

`func (o *PayloadCommit) GetAdded() []string`

GetAdded returns the Added field if non-nil, zero value otherwise.

### GetAddedOk

`func (o *PayloadCommit) GetAddedOk() (*[]string, bool)`

GetAddedOk returns a tuple with the Added field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdded

`func (o *PayloadCommit) SetAdded(v []string)`

SetAdded sets Added field to given value.

### HasAdded

`func (o *PayloadCommit) HasAdded() bool`

HasAdded returns a boolean if a field has been set.

### GetAuthor

`func (o *PayloadCommit) GetAuthor() PayloadUser`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *PayloadCommit) GetAuthorOk() (*PayloadUser, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *PayloadCommit) SetAuthor(v PayloadUser)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *PayloadCommit) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetCommitter

`func (o *PayloadCommit) GetCommitter() PayloadUser`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *PayloadCommit) GetCommitterOk() (*PayloadUser, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *PayloadCommit) SetCommitter(v PayloadUser)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *PayloadCommit) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.

### GetId

`func (o *PayloadCommit) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PayloadCommit) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PayloadCommit) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *PayloadCommit) HasId() bool`

HasId returns a boolean if a field has been set.

### GetMessage

`func (o *PayloadCommit) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *PayloadCommit) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *PayloadCommit) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *PayloadCommit) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetModified

`func (o *PayloadCommit) GetModified() []string`

GetModified returns the Modified field if non-nil, zero value otherwise.

### GetModifiedOk

`func (o *PayloadCommit) GetModifiedOk() (*[]string, bool)`

GetModifiedOk returns a tuple with the Modified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModified

`func (o *PayloadCommit) SetModified(v []string)`

SetModified sets Modified field to given value.

### HasModified

`func (o *PayloadCommit) HasModified() bool`

HasModified returns a boolean if a field has been set.

### GetRemoved

`func (o *PayloadCommit) GetRemoved() []string`

GetRemoved returns the Removed field if non-nil, zero value otherwise.

### GetRemovedOk

`func (o *PayloadCommit) GetRemovedOk() (*[]string, bool)`

GetRemovedOk returns a tuple with the Removed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoved

`func (o *PayloadCommit) SetRemoved(v []string)`

SetRemoved sets Removed field to given value.

### HasRemoved

`func (o *PayloadCommit) HasRemoved() bool`

HasRemoved returns a boolean if a field has been set.

### GetTimestamp

`func (o *PayloadCommit) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *PayloadCommit) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *PayloadCommit) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.

### HasTimestamp

`func (o *PayloadCommit) HasTimestamp() bool`

HasTimestamp returns a boolean if a field has been set.

### GetUrl

`func (o *PayloadCommit) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *PayloadCommit) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *PayloadCommit) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *PayloadCommit) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetVerification

`func (o *PayloadCommit) GetVerification() PayloadCommitVerification`

GetVerification returns the Verification field if non-nil, zero value otherwise.

### GetVerificationOk

`func (o *PayloadCommit) GetVerificationOk() (*PayloadCommitVerification, bool)`

GetVerificationOk returns a tuple with the Verification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerification

`func (o *PayloadCommit) SetVerification(v PayloadCommitVerification)`

SetVerification sets Verification field to given value.

### HasVerification

`func (o *PayloadCommit) HasVerification() bool`

HasVerification returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



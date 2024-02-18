# CommitDateOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | Pointer to **time.Time** |  | [optional] 
**Committer** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewCommitDateOptions

`func NewCommitDateOptions() *CommitDateOptions`

NewCommitDateOptions instantiates a new CommitDateOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCommitDateOptionsWithDefaults

`func NewCommitDateOptionsWithDefaults() *CommitDateOptions`

NewCommitDateOptionsWithDefaults instantiates a new CommitDateOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *CommitDateOptions) GetAuthor() time.Time`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *CommitDateOptions) GetAuthorOk() (*time.Time, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *CommitDateOptions) SetAuthor(v time.Time)`

SetAuthor sets Author field to given value.

### HasAuthor

`func (o *CommitDateOptions) HasAuthor() bool`

HasAuthor returns a boolean if a field has been set.

### GetCommitter

`func (o *CommitDateOptions) GetCommitter() time.Time`

GetCommitter returns the Committer field if non-nil, zero value otherwise.

### GetCommitterOk

`func (o *CommitDateOptions) GetCommitterOk() (*time.Time, bool)`

GetCommitterOk returns a tuple with the Committer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitter

`func (o *CommitDateOptions) SetCommitter(v time.Time)`

SetCommitter sets Committer field to given value.

### HasCommitter

`func (o *CommitDateOptions) HasCommitter() bool`

HasCommitter returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



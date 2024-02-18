# RepoTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Doer** | Pointer to [**User**](User.md) |  | [optional] 
**Recipient** | Pointer to [**User**](User.md) |  | [optional] 
**Teams** | Pointer to [**[]Team**](Team.md) |  | [optional] 

## Methods

### NewRepoTransfer

`func NewRepoTransfer() *RepoTransfer`

NewRepoTransfer instantiates a new RepoTransfer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepoTransferWithDefaults

`func NewRepoTransferWithDefaults() *RepoTransfer`

NewRepoTransferWithDefaults instantiates a new RepoTransfer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDoer

`func (o *RepoTransfer) GetDoer() User`

GetDoer returns the Doer field if non-nil, zero value otherwise.

### GetDoerOk

`func (o *RepoTransfer) GetDoerOk() (*User, bool)`

GetDoerOk returns a tuple with the Doer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDoer

`func (o *RepoTransfer) SetDoer(v User)`

SetDoer sets Doer field to given value.

### HasDoer

`func (o *RepoTransfer) HasDoer() bool`

HasDoer returns a boolean if a field has been set.

### GetRecipient

`func (o *RepoTransfer) GetRecipient() User`

GetRecipient returns the Recipient field if non-nil, zero value otherwise.

### GetRecipientOk

`func (o *RepoTransfer) GetRecipientOk() (*User, bool)`

GetRecipientOk returns a tuple with the Recipient field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecipient

`func (o *RepoTransfer) SetRecipient(v User)`

SetRecipient sets Recipient field to given value.

### HasRecipient

`func (o *RepoTransfer) HasRecipient() bool`

HasRecipient returns a boolean if a field has been set.

### GetTeams

`func (o *RepoTransfer) GetTeams() []Team`

GetTeams returns the Teams field if non-nil, zero value otherwise.

### GetTeamsOk

`func (o *RepoTransfer) GetTeamsOk() (*[]Team, bool)`

GetTeamsOk returns a tuple with the Teams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeams

`func (o *RepoTransfer) SetTeams(v []Team)`

SetTeams sets Teams field to given value.

### HasTeams

`func (o *RepoTransfer) HasTeams() bool`

HasTeams returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateUserOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | Pointer to **time.Time** | For explicitly setting the user creation timestamp. Useful when users are migrated from other systems. When omitted, the user&#39;s creation timestamp will be set to \&quot;now\&quot;. | [optional] 
**Email** | **string** |  | 
**FullName** | Pointer to **string** |  | [optional] 
**LoginName** | Pointer to **string** |  | [optional] 
**MustChangePassword** | Pointer to **bool** |  | [optional] 
**Password** | Pointer to **string** |  | [optional] 
**Restricted** | Pointer to **bool** |  | [optional] 
**SendNotify** | Pointer to **bool** |  | [optional] 
**SourceId** | Pointer to **int64** |  | [optional] 
**Username** | **string** |  | 
**Visibility** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateUserOption

`func NewCreateUserOption(email string, username string, ) *CreateUserOption`

NewCreateUserOption instantiates a new CreateUserOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateUserOptionWithDefaults

`func NewCreateUserOptionWithDefaults() *CreateUserOption`

NewCreateUserOptionWithDefaults instantiates a new CreateUserOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *CreateUserOption) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CreateUserOption) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CreateUserOption) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *CreateUserOption) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetEmail

`func (o *CreateUserOption) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateUserOption) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateUserOption) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetFullName

`func (o *CreateUserOption) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *CreateUserOption) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *CreateUserOption) SetFullName(v string)`

SetFullName sets FullName field to given value.

### HasFullName

`func (o *CreateUserOption) HasFullName() bool`

HasFullName returns a boolean if a field has been set.

### GetLoginName

`func (o *CreateUserOption) GetLoginName() string`

GetLoginName returns the LoginName field if non-nil, zero value otherwise.

### GetLoginNameOk

`func (o *CreateUserOption) GetLoginNameOk() (*string, bool)`

GetLoginNameOk returns a tuple with the LoginName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoginName

`func (o *CreateUserOption) SetLoginName(v string)`

SetLoginName sets LoginName field to given value.

### HasLoginName

`func (o *CreateUserOption) HasLoginName() bool`

HasLoginName returns a boolean if a field has been set.

### GetMustChangePassword

`func (o *CreateUserOption) GetMustChangePassword() bool`

GetMustChangePassword returns the MustChangePassword field if non-nil, zero value otherwise.

### GetMustChangePasswordOk

`func (o *CreateUserOption) GetMustChangePasswordOk() (*bool, bool)`

GetMustChangePasswordOk returns a tuple with the MustChangePassword field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMustChangePassword

`func (o *CreateUserOption) SetMustChangePassword(v bool)`

SetMustChangePassword sets MustChangePassword field to given value.

### HasMustChangePassword

`func (o *CreateUserOption) HasMustChangePassword() bool`

HasMustChangePassword returns a boolean if a field has been set.

### GetPassword

`func (o *CreateUserOption) GetPassword() string`

GetPassword returns the Password field if non-nil, zero value otherwise.

### GetPasswordOk

`func (o *CreateUserOption) GetPasswordOk() (*string, bool)`

GetPasswordOk returns a tuple with the Password field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassword

`func (o *CreateUserOption) SetPassword(v string)`

SetPassword sets Password field to given value.

### HasPassword

`func (o *CreateUserOption) HasPassword() bool`

HasPassword returns a boolean if a field has been set.

### GetRestricted

`func (o *CreateUserOption) GetRestricted() bool`

GetRestricted returns the Restricted field if non-nil, zero value otherwise.

### GetRestrictedOk

`func (o *CreateUserOption) GetRestrictedOk() (*bool, bool)`

GetRestrictedOk returns a tuple with the Restricted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestricted

`func (o *CreateUserOption) SetRestricted(v bool)`

SetRestricted sets Restricted field to given value.

### HasRestricted

`func (o *CreateUserOption) HasRestricted() bool`

HasRestricted returns a boolean if a field has been set.

### GetSendNotify

`func (o *CreateUserOption) GetSendNotify() bool`

GetSendNotify returns the SendNotify field if non-nil, zero value otherwise.

### GetSendNotifyOk

`func (o *CreateUserOption) GetSendNotifyOk() (*bool, bool)`

GetSendNotifyOk returns a tuple with the SendNotify field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSendNotify

`func (o *CreateUserOption) SetSendNotify(v bool)`

SetSendNotify sets SendNotify field to given value.

### HasSendNotify

`func (o *CreateUserOption) HasSendNotify() bool`

HasSendNotify returns a boolean if a field has been set.

### GetSourceId

`func (o *CreateUserOption) GetSourceId() int64`

GetSourceId returns the SourceId field if non-nil, zero value otherwise.

### GetSourceIdOk

`func (o *CreateUserOption) GetSourceIdOk() (*int64, bool)`

GetSourceIdOk returns a tuple with the SourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceId

`func (o *CreateUserOption) SetSourceId(v int64)`

SetSourceId sets SourceId field to given value.

### HasSourceId

`func (o *CreateUserOption) HasSourceId() bool`

HasSourceId returns a boolean if a field has been set.

### GetUsername

`func (o *CreateUserOption) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *CreateUserOption) GetUsernameOk() (*string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsername

`func (o *CreateUserOption) SetUsername(v string)`

SetUsername sets Username field to given value.


### GetVisibility

`func (o *CreateUserOption) GetVisibility() string`

GetVisibility returns the Visibility field if non-nil, zero value otherwise.

### GetVisibilityOk

`func (o *CreateUserOption) GetVisibilityOk() (*string, bool)`

GetVisibilityOk returns a tuple with the Visibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisibility

`func (o *CreateUserOption) SetVisibility(v string)`

SetVisibility sets Visibility field to given value.

### HasVisibility

`func (o *CreateUserOption) HasVisibility() bool`

HasVisibility returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



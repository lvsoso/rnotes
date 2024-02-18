# EditUserOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Active** | Pointer to **bool** |  | [optional] 
**Admin** | Pointer to **bool** |  | [optional] 
**AllowCreateOrganization** | Pointer to **bool** |  | [optional] 
**AllowGitHook** | Pointer to **bool** |  | [optional] 
**AllowImportLocal** | Pointer to **bool** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Email** | Pointer to **string** |  | [optional] 
**FullName** | Pointer to **string** |  | [optional] 
**Location** | Pointer to **string** |  | [optional] 
**LoginName** | **string** |  | 
**MaxRepoCreation** | Pointer to **int64** |  | [optional] 
**MustChangePassword** | Pointer to **bool** |  | [optional] 
**Password** | Pointer to **string** |  | [optional] 
**ProhibitLogin** | Pointer to **bool** |  | [optional] 
**Restricted** | Pointer to **bool** |  | [optional] 
**SourceId** | **int64** |  | 
**Visibility** | Pointer to **string** |  | [optional] 
**Website** | Pointer to **string** |  | [optional] 

## Methods

### NewEditUserOption

`func NewEditUserOption(loginName string, sourceId int64, ) *EditUserOption`

NewEditUserOption instantiates a new EditUserOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditUserOptionWithDefaults

`func NewEditUserOptionWithDefaults() *EditUserOption`

NewEditUserOptionWithDefaults instantiates a new EditUserOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActive

`func (o *EditUserOption) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *EditUserOption) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *EditUserOption) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *EditUserOption) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetAdmin

`func (o *EditUserOption) GetAdmin() bool`

GetAdmin returns the Admin field if non-nil, zero value otherwise.

### GetAdminOk

`func (o *EditUserOption) GetAdminOk() (*bool, bool)`

GetAdminOk returns a tuple with the Admin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdmin

`func (o *EditUserOption) SetAdmin(v bool)`

SetAdmin sets Admin field to given value.

### HasAdmin

`func (o *EditUserOption) HasAdmin() bool`

HasAdmin returns a boolean if a field has been set.

### GetAllowCreateOrganization

`func (o *EditUserOption) GetAllowCreateOrganization() bool`

GetAllowCreateOrganization returns the AllowCreateOrganization field if non-nil, zero value otherwise.

### GetAllowCreateOrganizationOk

`func (o *EditUserOption) GetAllowCreateOrganizationOk() (*bool, bool)`

GetAllowCreateOrganizationOk returns a tuple with the AllowCreateOrganization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowCreateOrganization

`func (o *EditUserOption) SetAllowCreateOrganization(v bool)`

SetAllowCreateOrganization sets AllowCreateOrganization field to given value.

### HasAllowCreateOrganization

`func (o *EditUserOption) HasAllowCreateOrganization() bool`

HasAllowCreateOrganization returns a boolean if a field has been set.

### GetAllowGitHook

`func (o *EditUserOption) GetAllowGitHook() bool`

GetAllowGitHook returns the AllowGitHook field if non-nil, zero value otherwise.

### GetAllowGitHookOk

`func (o *EditUserOption) GetAllowGitHookOk() (*bool, bool)`

GetAllowGitHookOk returns a tuple with the AllowGitHook field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowGitHook

`func (o *EditUserOption) SetAllowGitHook(v bool)`

SetAllowGitHook sets AllowGitHook field to given value.

### HasAllowGitHook

`func (o *EditUserOption) HasAllowGitHook() bool`

HasAllowGitHook returns a boolean if a field has been set.

### GetAllowImportLocal

`func (o *EditUserOption) GetAllowImportLocal() bool`

GetAllowImportLocal returns the AllowImportLocal field if non-nil, zero value otherwise.

### GetAllowImportLocalOk

`func (o *EditUserOption) GetAllowImportLocalOk() (*bool, bool)`

GetAllowImportLocalOk returns a tuple with the AllowImportLocal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowImportLocal

`func (o *EditUserOption) SetAllowImportLocal(v bool)`

SetAllowImportLocal sets AllowImportLocal field to given value.

### HasAllowImportLocal

`func (o *EditUserOption) HasAllowImportLocal() bool`

HasAllowImportLocal returns a boolean if a field has been set.

### GetDescription

`func (o *EditUserOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *EditUserOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *EditUserOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *EditUserOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEmail

`func (o *EditUserOption) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *EditUserOption) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *EditUserOption) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *EditUserOption) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetFullName

`func (o *EditUserOption) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *EditUserOption) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *EditUserOption) SetFullName(v string)`

SetFullName sets FullName field to given value.

### HasFullName

`func (o *EditUserOption) HasFullName() bool`

HasFullName returns a boolean if a field has been set.

### GetLocation

`func (o *EditUserOption) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *EditUserOption) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *EditUserOption) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *EditUserOption) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### GetLoginName

`func (o *EditUserOption) GetLoginName() string`

GetLoginName returns the LoginName field if non-nil, zero value otherwise.

### GetLoginNameOk

`func (o *EditUserOption) GetLoginNameOk() (*string, bool)`

GetLoginNameOk returns a tuple with the LoginName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoginName

`func (o *EditUserOption) SetLoginName(v string)`

SetLoginName sets LoginName field to given value.


### GetMaxRepoCreation

`func (o *EditUserOption) GetMaxRepoCreation() int64`

GetMaxRepoCreation returns the MaxRepoCreation field if non-nil, zero value otherwise.

### GetMaxRepoCreationOk

`func (o *EditUserOption) GetMaxRepoCreationOk() (*int64, bool)`

GetMaxRepoCreationOk returns a tuple with the MaxRepoCreation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRepoCreation

`func (o *EditUserOption) SetMaxRepoCreation(v int64)`

SetMaxRepoCreation sets MaxRepoCreation field to given value.

### HasMaxRepoCreation

`func (o *EditUserOption) HasMaxRepoCreation() bool`

HasMaxRepoCreation returns a boolean if a field has been set.

### GetMustChangePassword

`func (o *EditUserOption) GetMustChangePassword() bool`

GetMustChangePassword returns the MustChangePassword field if non-nil, zero value otherwise.

### GetMustChangePasswordOk

`func (o *EditUserOption) GetMustChangePasswordOk() (*bool, bool)`

GetMustChangePasswordOk returns a tuple with the MustChangePassword field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMustChangePassword

`func (o *EditUserOption) SetMustChangePassword(v bool)`

SetMustChangePassword sets MustChangePassword field to given value.

### HasMustChangePassword

`func (o *EditUserOption) HasMustChangePassword() bool`

HasMustChangePassword returns a boolean if a field has been set.

### GetPassword

`func (o *EditUserOption) GetPassword() string`

GetPassword returns the Password field if non-nil, zero value otherwise.

### GetPasswordOk

`func (o *EditUserOption) GetPasswordOk() (*string, bool)`

GetPasswordOk returns a tuple with the Password field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassword

`func (o *EditUserOption) SetPassword(v string)`

SetPassword sets Password field to given value.

### HasPassword

`func (o *EditUserOption) HasPassword() bool`

HasPassword returns a boolean if a field has been set.

### GetProhibitLogin

`func (o *EditUserOption) GetProhibitLogin() bool`

GetProhibitLogin returns the ProhibitLogin field if non-nil, zero value otherwise.

### GetProhibitLoginOk

`func (o *EditUserOption) GetProhibitLoginOk() (*bool, bool)`

GetProhibitLoginOk returns a tuple with the ProhibitLogin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProhibitLogin

`func (o *EditUserOption) SetProhibitLogin(v bool)`

SetProhibitLogin sets ProhibitLogin field to given value.

### HasProhibitLogin

`func (o *EditUserOption) HasProhibitLogin() bool`

HasProhibitLogin returns a boolean if a field has been set.

### GetRestricted

`func (o *EditUserOption) GetRestricted() bool`

GetRestricted returns the Restricted field if non-nil, zero value otherwise.

### GetRestrictedOk

`func (o *EditUserOption) GetRestrictedOk() (*bool, bool)`

GetRestrictedOk returns a tuple with the Restricted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestricted

`func (o *EditUserOption) SetRestricted(v bool)`

SetRestricted sets Restricted field to given value.

### HasRestricted

`func (o *EditUserOption) HasRestricted() bool`

HasRestricted returns a boolean if a field has been set.

### GetSourceId

`func (o *EditUserOption) GetSourceId() int64`

GetSourceId returns the SourceId field if non-nil, zero value otherwise.

### GetSourceIdOk

`func (o *EditUserOption) GetSourceIdOk() (*int64, bool)`

GetSourceIdOk returns a tuple with the SourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceId

`func (o *EditUserOption) SetSourceId(v int64)`

SetSourceId sets SourceId field to given value.


### GetVisibility

`func (o *EditUserOption) GetVisibility() string`

GetVisibility returns the Visibility field if non-nil, zero value otherwise.

### GetVisibilityOk

`func (o *EditUserOption) GetVisibilityOk() (*string, bool)`

GetVisibilityOk returns a tuple with the Visibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisibility

`func (o *EditUserOption) SetVisibility(v string)`

SetVisibility sets Visibility field to given value.

### HasVisibility

`func (o *EditUserOption) HasVisibility() bool`

HasVisibility returns a boolean if a field has been set.

### GetWebsite

`func (o *EditUserOption) GetWebsite() string`

GetWebsite returns the Website field if non-nil, zero value otherwise.

### GetWebsiteOk

`func (o *EditUserOption) GetWebsiteOk() (*string, bool)`

GetWebsiteOk returns a tuple with the Website field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsite

`func (o *EditUserOption) SetWebsite(v string)`

SetWebsite sets Website field to given value.

### HasWebsite

`func (o *EditUserOption) HasWebsite() bool`

HasWebsite returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



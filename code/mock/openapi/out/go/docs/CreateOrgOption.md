# CreateOrgOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | Pointer to **string** |  | [optional] 
**Email** | Pointer to **string** |  | [optional] 
**FullName** | Pointer to **string** |  | [optional] 
**Location** | Pointer to **string** |  | [optional] 
**RepoAdminChangeTeamAccess** | Pointer to **bool** |  | [optional] 
**Username** | **string** |  | 
**Visibility** | Pointer to **string** | possible values are &#x60;public&#x60; (default), &#x60;limited&#x60; or &#x60;private&#x60; | [optional] 
**Website** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateOrgOption

`func NewCreateOrgOption(username string, ) *CreateOrgOption`

NewCreateOrgOption instantiates a new CreateOrgOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateOrgOptionWithDefaults

`func NewCreateOrgOptionWithDefaults() *CreateOrgOption`

NewCreateOrgOptionWithDefaults instantiates a new CreateOrgOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *CreateOrgOption) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateOrgOption) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateOrgOption) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateOrgOption) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEmail

`func (o *CreateOrgOption) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateOrgOption) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateOrgOption) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *CreateOrgOption) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetFullName

`func (o *CreateOrgOption) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *CreateOrgOption) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *CreateOrgOption) SetFullName(v string)`

SetFullName sets FullName field to given value.

### HasFullName

`func (o *CreateOrgOption) HasFullName() bool`

HasFullName returns a boolean if a field has been set.

### GetLocation

`func (o *CreateOrgOption) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *CreateOrgOption) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *CreateOrgOption) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *CreateOrgOption) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### GetRepoAdminChangeTeamAccess

`func (o *CreateOrgOption) GetRepoAdminChangeTeamAccess() bool`

GetRepoAdminChangeTeamAccess returns the RepoAdminChangeTeamAccess field if non-nil, zero value otherwise.

### GetRepoAdminChangeTeamAccessOk

`func (o *CreateOrgOption) GetRepoAdminChangeTeamAccessOk() (*bool, bool)`

GetRepoAdminChangeTeamAccessOk returns a tuple with the RepoAdminChangeTeamAccess field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoAdminChangeTeamAccess

`func (o *CreateOrgOption) SetRepoAdminChangeTeamAccess(v bool)`

SetRepoAdminChangeTeamAccess sets RepoAdminChangeTeamAccess field to given value.

### HasRepoAdminChangeTeamAccess

`func (o *CreateOrgOption) HasRepoAdminChangeTeamAccess() bool`

HasRepoAdminChangeTeamAccess returns a boolean if a field has been set.

### GetUsername

`func (o *CreateOrgOption) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *CreateOrgOption) GetUsernameOk() (*string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsername

`func (o *CreateOrgOption) SetUsername(v string)`

SetUsername sets Username field to given value.


### GetVisibility

`func (o *CreateOrgOption) GetVisibility() string`

GetVisibility returns the Visibility field if non-nil, zero value otherwise.

### GetVisibilityOk

`func (o *CreateOrgOption) GetVisibilityOk() (*string, bool)`

GetVisibilityOk returns a tuple with the Visibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisibility

`func (o *CreateOrgOption) SetVisibility(v string)`

SetVisibility sets Visibility field to given value.

### HasVisibility

`func (o *CreateOrgOption) HasVisibility() bool`

HasVisibility returns a boolean if a field has been set.

### GetWebsite

`func (o *CreateOrgOption) GetWebsite() string`

GetWebsite returns the Website field if non-nil, zero value otherwise.

### GetWebsiteOk

`func (o *CreateOrgOption) GetWebsiteOk() (*string, bool)`

GetWebsiteOk returns a tuple with the Website field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsite

`func (o *CreateOrgOption) SetWebsite(v string)`

SetWebsite sets Website field to given value.

### HasWebsite

`func (o *CreateOrgOption) HasWebsite() bool`

HasWebsite returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



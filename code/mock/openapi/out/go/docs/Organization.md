# Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvatarUrl** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Email** | Pointer to **string** |  | [optional] 
**FullName** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**Location** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**RepoAdminChangeTeamAccess** | Pointer to **bool** |  | [optional] 
**Username** | Pointer to **string** | deprecated | [optional] 
**Visibility** | Pointer to **string** |  | [optional] 
**Website** | Pointer to **string** |  | [optional] 

## Methods

### NewOrganization

`func NewOrganization() *Organization`

NewOrganization instantiates a new Organization object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrganizationWithDefaults

`func NewOrganizationWithDefaults() *Organization`

NewOrganizationWithDefaults instantiates a new Organization object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvatarUrl

`func (o *Organization) GetAvatarUrl() string`

GetAvatarUrl returns the AvatarUrl field if non-nil, zero value otherwise.

### GetAvatarUrlOk

`func (o *Organization) GetAvatarUrlOk() (*string, bool)`

GetAvatarUrlOk returns a tuple with the AvatarUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatarUrl

`func (o *Organization) SetAvatarUrl(v string)`

SetAvatarUrl sets AvatarUrl field to given value.

### HasAvatarUrl

`func (o *Organization) HasAvatarUrl() bool`

HasAvatarUrl returns a boolean if a field has been set.

### GetDescription

`func (o *Organization) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Organization) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Organization) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Organization) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEmail

`func (o *Organization) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *Organization) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *Organization) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *Organization) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetFullName

`func (o *Organization) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *Organization) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *Organization) SetFullName(v string)`

SetFullName sets FullName field to given value.

### HasFullName

`func (o *Organization) HasFullName() bool`

HasFullName returns a boolean if a field has been set.

### GetId

`func (o *Organization) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Organization) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Organization) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *Organization) HasId() bool`

HasId returns a boolean if a field has been set.

### GetLocation

`func (o *Organization) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *Organization) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *Organization) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *Organization) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### GetName

`func (o *Organization) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Organization) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Organization) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Organization) HasName() bool`

HasName returns a boolean if a field has been set.

### GetRepoAdminChangeTeamAccess

`func (o *Organization) GetRepoAdminChangeTeamAccess() bool`

GetRepoAdminChangeTeamAccess returns the RepoAdminChangeTeamAccess field if non-nil, zero value otherwise.

### GetRepoAdminChangeTeamAccessOk

`func (o *Organization) GetRepoAdminChangeTeamAccessOk() (*bool, bool)`

GetRepoAdminChangeTeamAccessOk returns a tuple with the RepoAdminChangeTeamAccess field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepoAdminChangeTeamAccess

`func (o *Organization) SetRepoAdminChangeTeamAccess(v bool)`

SetRepoAdminChangeTeamAccess sets RepoAdminChangeTeamAccess field to given value.

### HasRepoAdminChangeTeamAccess

`func (o *Organization) HasRepoAdminChangeTeamAccess() bool`

HasRepoAdminChangeTeamAccess returns a boolean if a field has been set.

### GetUsername

`func (o *Organization) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *Organization) GetUsernameOk() (*string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsername

`func (o *Organization) SetUsername(v string)`

SetUsername sets Username field to given value.

### HasUsername

`func (o *Organization) HasUsername() bool`

HasUsername returns a boolean if a field has been set.

### GetVisibility

`func (o *Organization) GetVisibility() string`

GetVisibility returns the Visibility field if non-nil, zero value otherwise.

### GetVisibilityOk

`func (o *Organization) GetVisibilityOk() (*string, bool)`

GetVisibilityOk returns a tuple with the Visibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisibility

`func (o *Organization) SetVisibility(v string)`

SetVisibility sets Visibility field to given value.

### HasVisibility

`func (o *Organization) HasVisibility() bool`

HasVisibility returns a boolean if a field has been set.

### GetWebsite

`func (o *Organization) GetWebsite() string`

GetWebsite returns the Website field if non-nil, zero value otherwise.

### GetWebsiteOk

`func (o *Organization) GetWebsiteOk() (*string, bool)`

GetWebsiteOk returns a tuple with the Website field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsite

`func (o *Organization) SetWebsite(v string)`

SetWebsite sets Website field to given value.

### HasWebsite

`func (o *Organization) HasWebsite() bool`

HasWebsite returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Active** | Pointer to **bool** | Is user active | [optional] 
**AvatarUrl** | Pointer to **string** | URL to the user&#39;s avatar | [optional] 
**Created** | Pointer to **time.Time** |  | [optional] 
**Description** | Pointer to **string** | the user&#39;s description | [optional] 
**Email** | Pointer to **string** |  | [optional] 
**FollowersCount** | Pointer to **int64** | user counts | [optional] 
**FollowingCount** | Pointer to **int64** |  | [optional] 
**FullName** | Pointer to **string** | the user&#39;s full name | [optional] 
**Id** | Pointer to **int64** | the user&#39;s id | [optional] 
**IsAdmin** | Pointer to **bool** | Is the user an administrator | [optional] 
**Language** | Pointer to **string** | User locale | [optional] 
**LastLogin** | Pointer to **time.Time** |  | [optional] 
**Location** | Pointer to **string** | the user&#39;s location | [optional] 
**Login** | Pointer to **string** | the user&#39;s username | [optional] 
**LoginName** | Pointer to **string** | the user&#39;s authentication sign-in name. | [optional] [default to "empty"]
**ProhibitLogin** | Pointer to **bool** | Is user login prohibited | [optional] 
**Restricted** | Pointer to **bool** | Is user restricted | [optional] 
**StarredReposCount** | Pointer to **int64** |  | [optional] 
**Visibility** | Pointer to **string** | User visibility level option: public, limited, private | [optional] 
**Website** | Pointer to **string** | the user&#39;s website | [optional] 

## Methods

### NewUser

`func NewUser() *User`

NewUser instantiates a new User object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserWithDefaults

`func NewUserWithDefaults() *User`

NewUserWithDefaults instantiates a new User object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActive

`func (o *User) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *User) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *User) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *User) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetAvatarUrl

`func (o *User) GetAvatarUrl() string`

GetAvatarUrl returns the AvatarUrl field if non-nil, zero value otherwise.

### GetAvatarUrlOk

`func (o *User) GetAvatarUrlOk() (*string, bool)`

GetAvatarUrlOk returns a tuple with the AvatarUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvatarUrl

`func (o *User) SetAvatarUrl(v string)`

SetAvatarUrl sets AvatarUrl field to given value.

### HasAvatarUrl

`func (o *User) HasAvatarUrl() bool`

HasAvatarUrl returns a boolean if a field has been set.

### GetCreated

`func (o *User) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *User) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *User) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *User) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetDescription

`func (o *User) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *User) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *User) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *User) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEmail

`func (o *User) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *User) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *User) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *User) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetFollowersCount

`func (o *User) GetFollowersCount() int64`

GetFollowersCount returns the FollowersCount field if non-nil, zero value otherwise.

### GetFollowersCountOk

`func (o *User) GetFollowersCountOk() (*int64, bool)`

GetFollowersCountOk returns a tuple with the FollowersCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFollowersCount

`func (o *User) SetFollowersCount(v int64)`

SetFollowersCount sets FollowersCount field to given value.

### HasFollowersCount

`func (o *User) HasFollowersCount() bool`

HasFollowersCount returns a boolean if a field has been set.

### GetFollowingCount

`func (o *User) GetFollowingCount() int64`

GetFollowingCount returns the FollowingCount field if non-nil, zero value otherwise.

### GetFollowingCountOk

`func (o *User) GetFollowingCountOk() (*int64, bool)`

GetFollowingCountOk returns a tuple with the FollowingCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFollowingCount

`func (o *User) SetFollowingCount(v int64)`

SetFollowingCount sets FollowingCount field to given value.

### HasFollowingCount

`func (o *User) HasFollowingCount() bool`

HasFollowingCount returns a boolean if a field has been set.

### GetFullName

`func (o *User) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *User) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *User) SetFullName(v string)`

SetFullName sets FullName field to given value.

### HasFullName

`func (o *User) HasFullName() bool`

HasFullName returns a boolean if a field has been set.

### GetId

`func (o *User) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *User) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *User) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *User) HasId() bool`

HasId returns a boolean if a field has been set.

### GetIsAdmin

`func (o *User) GetIsAdmin() bool`

GetIsAdmin returns the IsAdmin field if non-nil, zero value otherwise.

### GetIsAdminOk

`func (o *User) GetIsAdminOk() (*bool, bool)`

GetIsAdminOk returns a tuple with the IsAdmin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsAdmin

`func (o *User) SetIsAdmin(v bool)`

SetIsAdmin sets IsAdmin field to given value.

### HasIsAdmin

`func (o *User) HasIsAdmin() bool`

HasIsAdmin returns a boolean if a field has been set.

### GetLanguage

`func (o *User) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *User) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *User) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *User) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### GetLastLogin

`func (o *User) GetLastLogin() time.Time`

GetLastLogin returns the LastLogin field if non-nil, zero value otherwise.

### GetLastLoginOk

`func (o *User) GetLastLoginOk() (*time.Time, bool)`

GetLastLoginOk returns a tuple with the LastLogin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastLogin

`func (o *User) SetLastLogin(v time.Time)`

SetLastLogin sets LastLogin field to given value.

### HasLastLogin

`func (o *User) HasLastLogin() bool`

HasLastLogin returns a boolean if a field has been set.

### GetLocation

`func (o *User) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *User) GetLocationOk() (*string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *User) SetLocation(v string)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *User) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### GetLogin

`func (o *User) GetLogin() string`

GetLogin returns the Login field if non-nil, zero value otherwise.

### GetLoginOk

`func (o *User) GetLoginOk() (*string, bool)`

GetLoginOk returns a tuple with the Login field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogin

`func (o *User) SetLogin(v string)`

SetLogin sets Login field to given value.

### HasLogin

`func (o *User) HasLogin() bool`

HasLogin returns a boolean if a field has been set.

### GetLoginName

`func (o *User) GetLoginName() string`

GetLoginName returns the LoginName field if non-nil, zero value otherwise.

### GetLoginNameOk

`func (o *User) GetLoginNameOk() (*string, bool)`

GetLoginNameOk returns a tuple with the LoginName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoginName

`func (o *User) SetLoginName(v string)`

SetLoginName sets LoginName field to given value.

### HasLoginName

`func (o *User) HasLoginName() bool`

HasLoginName returns a boolean if a field has been set.

### GetProhibitLogin

`func (o *User) GetProhibitLogin() bool`

GetProhibitLogin returns the ProhibitLogin field if non-nil, zero value otherwise.

### GetProhibitLoginOk

`func (o *User) GetProhibitLoginOk() (*bool, bool)`

GetProhibitLoginOk returns a tuple with the ProhibitLogin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProhibitLogin

`func (o *User) SetProhibitLogin(v bool)`

SetProhibitLogin sets ProhibitLogin field to given value.

### HasProhibitLogin

`func (o *User) HasProhibitLogin() bool`

HasProhibitLogin returns a boolean if a field has been set.

### GetRestricted

`func (o *User) GetRestricted() bool`

GetRestricted returns the Restricted field if non-nil, zero value otherwise.

### GetRestrictedOk

`func (o *User) GetRestrictedOk() (*bool, bool)`

GetRestrictedOk returns a tuple with the Restricted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestricted

`func (o *User) SetRestricted(v bool)`

SetRestricted sets Restricted field to given value.

### HasRestricted

`func (o *User) HasRestricted() bool`

HasRestricted returns a boolean if a field has been set.

### GetStarredReposCount

`func (o *User) GetStarredReposCount() int64`

GetStarredReposCount returns the StarredReposCount field if non-nil, zero value otherwise.

### GetStarredReposCountOk

`func (o *User) GetStarredReposCountOk() (*int64, bool)`

GetStarredReposCountOk returns a tuple with the StarredReposCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStarredReposCount

`func (o *User) SetStarredReposCount(v int64)`

SetStarredReposCount sets StarredReposCount field to given value.

### HasStarredReposCount

`func (o *User) HasStarredReposCount() bool`

HasStarredReposCount returns a boolean if a field has been set.

### GetVisibility

`func (o *User) GetVisibility() string`

GetVisibility returns the Visibility field if non-nil, zero value otherwise.

### GetVisibilityOk

`func (o *User) GetVisibilityOk() (*string, bool)`

GetVisibilityOk returns a tuple with the Visibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisibility

`func (o *User) SetVisibility(v string)`

SetVisibility sets Visibility field to given value.

### HasVisibility

`func (o *User) HasVisibility() bool`

HasVisibility returns a boolean if a field has been set.

### GetWebsite

`func (o *User) GetWebsite() string`

GetWebsite returns the Website field if non-nil, zero value otherwise.

### GetWebsiteOk

`func (o *User) GetWebsiteOk() (*string, bool)`

GetWebsiteOk returns a tuple with the Website field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsite

`func (o *User) SetWebsite(v string)`

SetWebsite sets Website field to given value.

### HasWebsite

`func (o *User) HasWebsite() bool`

HasWebsite returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



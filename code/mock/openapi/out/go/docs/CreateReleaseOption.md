# CreateReleaseOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** |  | [optional] 
**Draft** | Pointer to **bool** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Prerelease** | Pointer to **bool** |  | [optional] 
**TagName** | **string** |  | 
**TargetCommitish** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateReleaseOption

`func NewCreateReleaseOption(tagName string, ) *CreateReleaseOption`

NewCreateReleaseOption instantiates a new CreateReleaseOption object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateReleaseOptionWithDefaults

`func NewCreateReleaseOptionWithDefaults() *CreateReleaseOption`

NewCreateReleaseOptionWithDefaults instantiates a new CreateReleaseOption object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBody

`func (o *CreateReleaseOption) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *CreateReleaseOption) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *CreateReleaseOption) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *CreateReleaseOption) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetDraft

`func (o *CreateReleaseOption) GetDraft() bool`

GetDraft returns the Draft field if non-nil, zero value otherwise.

### GetDraftOk

`func (o *CreateReleaseOption) GetDraftOk() (*bool, bool)`

GetDraftOk returns a tuple with the Draft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraft

`func (o *CreateReleaseOption) SetDraft(v bool)`

SetDraft sets Draft field to given value.

### HasDraft

`func (o *CreateReleaseOption) HasDraft() bool`

HasDraft returns a boolean if a field has been set.

### GetName

`func (o *CreateReleaseOption) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateReleaseOption) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateReleaseOption) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CreateReleaseOption) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrerelease

`func (o *CreateReleaseOption) GetPrerelease() bool`

GetPrerelease returns the Prerelease field if non-nil, zero value otherwise.

### GetPrereleaseOk

`func (o *CreateReleaseOption) GetPrereleaseOk() (*bool, bool)`

GetPrereleaseOk returns a tuple with the Prerelease field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrerelease

`func (o *CreateReleaseOption) SetPrerelease(v bool)`

SetPrerelease sets Prerelease field to given value.

### HasPrerelease

`func (o *CreateReleaseOption) HasPrerelease() bool`

HasPrerelease returns a boolean if a field has been set.

### GetTagName

`func (o *CreateReleaseOption) GetTagName() string`

GetTagName returns the TagName field if non-nil, zero value otherwise.

### GetTagNameOk

`func (o *CreateReleaseOption) GetTagNameOk() (*string, bool)`

GetTagNameOk returns a tuple with the TagName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagName

`func (o *CreateReleaseOption) SetTagName(v string)`

SetTagName sets TagName field to given value.


### GetTargetCommitish

`func (o *CreateReleaseOption) GetTargetCommitish() string`

GetTargetCommitish returns the TargetCommitish field if non-nil, zero value otherwise.

### GetTargetCommitishOk

`func (o *CreateReleaseOption) GetTargetCommitishOk() (*string, bool)`

GetTargetCommitishOk returns a tuple with the TargetCommitish field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetCommitish

`func (o *CreateReleaseOption) SetTargetCommitish(v string)`

SetTargetCommitish sets TargetCommitish field to given value.

### HasTargetCommitish

`func (o *CreateReleaseOption) HasTargetCommitish() bool`

HasTargetCommitish returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



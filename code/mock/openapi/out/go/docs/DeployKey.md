# DeployKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**Fingerprint** | Pointer to **string** |  | [optional] 
**Id** | Pointer to **int64** |  | [optional] 
**Key** | Pointer to **string** |  | [optional] 
**KeyId** | Pointer to **int64** |  | [optional] 
**ReadOnly** | Pointer to **bool** |  | [optional] 
**Repository** | Pointer to [**Repository**](Repository.md) |  | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewDeployKey

`func NewDeployKey() *DeployKey`

NewDeployKey instantiates a new DeployKey object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeployKeyWithDefaults

`func NewDeployKeyWithDefaults() *DeployKey`

NewDeployKeyWithDefaults instantiates a new DeployKey object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *DeployKey) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DeployKey) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DeployKey) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *DeployKey) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetFingerprint

`func (o *DeployKey) GetFingerprint() string`

GetFingerprint returns the Fingerprint field if non-nil, zero value otherwise.

### GetFingerprintOk

`func (o *DeployKey) GetFingerprintOk() (*string, bool)`

GetFingerprintOk returns a tuple with the Fingerprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFingerprint

`func (o *DeployKey) SetFingerprint(v string)`

SetFingerprint sets Fingerprint field to given value.

### HasFingerprint

`func (o *DeployKey) HasFingerprint() bool`

HasFingerprint returns a boolean if a field has been set.

### GetId

`func (o *DeployKey) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DeployKey) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DeployKey) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *DeployKey) HasId() bool`

HasId returns a boolean if a field has been set.

### GetKey

`func (o *DeployKey) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *DeployKey) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *DeployKey) SetKey(v string)`

SetKey sets Key field to given value.

### HasKey

`func (o *DeployKey) HasKey() bool`

HasKey returns a boolean if a field has been set.

### GetKeyId

`func (o *DeployKey) GetKeyId() int64`

GetKeyId returns the KeyId field if non-nil, zero value otherwise.

### GetKeyIdOk

`func (o *DeployKey) GetKeyIdOk() (*int64, bool)`

GetKeyIdOk returns a tuple with the KeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeyId

`func (o *DeployKey) SetKeyId(v int64)`

SetKeyId sets KeyId field to given value.

### HasKeyId

`func (o *DeployKey) HasKeyId() bool`

HasKeyId returns a boolean if a field has been set.

### GetReadOnly

`func (o *DeployKey) GetReadOnly() bool`

GetReadOnly returns the ReadOnly field if non-nil, zero value otherwise.

### GetReadOnlyOk

`func (o *DeployKey) GetReadOnlyOk() (*bool, bool)`

GetReadOnlyOk returns a tuple with the ReadOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReadOnly

`func (o *DeployKey) SetReadOnly(v bool)`

SetReadOnly sets ReadOnly field to given value.

### HasReadOnly

`func (o *DeployKey) HasReadOnly() bool`

HasReadOnly returns a boolean if a field has been set.

### GetRepository

`func (o *DeployKey) GetRepository() Repository`

GetRepository returns the Repository field if non-nil, zero value otherwise.

### GetRepositoryOk

`func (o *DeployKey) GetRepositoryOk() (*Repository, bool)`

GetRepositoryOk returns a tuple with the Repository field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepository

`func (o *DeployKey) SetRepository(v Repository)`

SetRepository sets Repository field to given value.

### HasRepository

`func (o *DeployKey) HasRepository() bool`

HasRepository returns a boolean if a field has been set.

### GetTitle

`func (o *DeployKey) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *DeployKey) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *DeployKey) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *DeployKey) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetUrl

`func (o *DeployKey) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *DeployKey) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *DeployKey) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *DeployKey) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | Pointer to [**GitObject**](GitObject.md) |  | [optional] 
**Ref** | Pointer to **string** |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 

## Methods

### NewReference

`func NewReference() *Reference`

NewReference instantiates a new Reference object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewReferenceWithDefaults

`func NewReferenceWithDefaults() *Reference`

NewReferenceWithDefaults instantiates a new Reference object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *Reference) GetObject() GitObject`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *Reference) GetObjectOk() (*GitObject, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *Reference) SetObject(v GitObject)`

SetObject sets Object field to given value.

### HasObject

`func (o *Reference) HasObject() bool`

HasObject returns a boolean if a field has been set.

### GetRef

`func (o *Reference) GetRef() string`

GetRef returns the Ref field if non-nil, zero value otherwise.

### GetRefOk

`func (o *Reference) GetRefOk() (*string, bool)`

GetRefOk returns a tuple with the Ref field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRef

`func (o *Reference) SetRef(v string)`

SetRef sets Ref field to given value.

### HasRef

`func (o *Reference) HasRef() bool`

HasRef returns a boolean if a field has been set.

### GetUrl

`func (o *Reference) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Reference) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Reference) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *Reference) HasUrl() bool`

HasUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



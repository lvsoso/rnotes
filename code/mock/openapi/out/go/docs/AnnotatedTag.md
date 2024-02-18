# AnnotatedTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | Pointer to **string** |  | [optional] 
**Object** | Pointer to [**AnnotatedTagObject**](AnnotatedTagObject.md) |  | [optional] 
**Sha** | Pointer to **string** |  | [optional] 
**Tag** | Pointer to **string** |  | [optional] 
**Tagger** | Pointer to [**CommitUser**](CommitUser.md) |  | [optional] 
**Url** | Pointer to **string** |  | [optional] 
**Verification** | Pointer to [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Methods

### NewAnnotatedTag

`func NewAnnotatedTag() *AnnotatedTag`

NewAnnotatedTag instantiates a new AnnotatedTag object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnnotatedTagWithDefaults

`func NewAnnotatedTagWithDefaults() *AnnotatedTag`

NewAnnotatedTagWithDefaults instantiates a new AnnotatedTag object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *AnnotatedTag) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *AnnotatedTag) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *AnnotatedTag) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *AnnotatedTag) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetObject

`func (o *AnnotatedTag) GetObject() AnnotatedTagObject`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *AnnotatedTag) GetObjectOk() (*AnnotatedTagObject, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *AnnotatedTag) SetObject(v AnnotatedTagObject)`

SetObject sets Object field to given value.

### HasObject

`func (o *AnnotatedTag) HasObject() bool`

HasObject returns a boolean if a field has been set.

### GetSha

`func (o *AnnotatedTag) GetSha() string`

GetSha returns the Sha field if non-nil, zero value otherwise.

### GetShaOk

`func (o *AnnotatedTag) GetShaOk() (*string, bool)`

GetShaOk returns a tuple with the Sha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha

`func (o *AnnotatedTag) SetSha(v string)`

SetSha sets Sha field to given value.

### HasSha

`func (o *AnnotatedTag) HasSha() bool`

HasSha returns a boolean if a field has been set.

### GetTag

`func (o *AnnotatedTag) GetTag() string`

GetTag returns the Tag field if non-nil, zero value otherwise.

### GetTagOk

`func (o *AnnotatedTag) GetTagOk() (*string, bool)`

GetTagOk returns a tuple with the Tag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTag

`func (o *AnnotatedTag) SetTag(v string)`

SetTag sets Tag field to given value.

### HasTag

`func (o *AnnotatedTag) HasTag() bool`

HasTag returns a boolean if a field has been set.

### GetTagger

`func (o *AnnotatedTag) GetTagger() CommitUser`

GetTagger returns the Tagger field if non-nil, zero value otherwise.

### GetTaggerOk

`func (o *AnnotatedTag) GetTaggerOk() (*CommitUser, bool)`

GetTaggerOk returns a tuple with the Tagger field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagger

`func (o *AnnotatedTag) SetTagger(v CommitUser)`

SetTagger sets Tagger field to given value.

### HasTagger

`func (o *AnnotatedTag) HasTagger() bool`

HasTagger returns a boolean if a field has been set.

### GetUrl

`func (o *AnnotatedTag) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *AnnotatedTag) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *AnnotatedTag) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *AnnotatedTag) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetVerification

`func (o *AnnotatedTag) GetVerification() PayloadCommitVerification`

GetVerification returns the Verification field if non-nil, zero value otherwise.

### GetVerificationOk

`func (o *AnnotatedTag) GetVerificationOk() (*PayloadCommitVerification, bool)`

GetVerificationOk returns a tuple with the Verification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerification

`func (o *AnnotatedTag) SetVerification(v PayloadCommitVerification)`

SetVerification sets Verification field to given value.

### HasVerification

`func (o *AnnotatedTag) HasVerification() bool`

HasVerification returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



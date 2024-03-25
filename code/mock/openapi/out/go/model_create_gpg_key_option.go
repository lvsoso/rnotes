/*
Gitea API

This documentation describes the Gitea API.

API version: {{AppVer | JSEscape | Safe}}
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// CreateGPGKeyOption CreateGPGKeyOption options create user GPG key
type CreateGPGKeyOption struct {
	// An armored GPG key to add
	ArmoredPublicKey string `json:"armored_public_key"`
	ArmoredSignature *string `json:"armored_signature,omitempty"`
}

// NewCreateGPGKeyOption instantiates a new CreateGPGKeyOption object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCreateGPGKeyOption(armoredPublicKey string) *CreateGPGKeyOption {
	this := CreateGPGKeyOption{}
	this.ArmoredPublicKey = armoredPublicKey
	return &this
}

// NewCreateGPGKeyOptionWithDefaults instantiates a new CreateGPGKeyOption object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCreateGPGKeyOptionWithDefaults() *CreateGPGKeyOption {
	this := CreateGPGKeyOption{}
	return &this
}

// GetArmoredPublicKey returns the ArmoredPublicKey field value
func (o *CreateGPGKeyOption) GetArmoredPublicKey() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.ArmoredPublicKey
}

// GetArmoredPublicKeyOk returns a tuple with the ArmoredPublicKey field value
// and a boolean to check if the value has been set.
func (o *CreateGPGKeyOption) GetArmoredPublicKeyOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.ArmoredPublicKey, true
}

// SetArmoredPublicKey sets field value
func (o *CreateGPGKeyOption) SetArmoredPublicKey(v string) {
	o.ArmoredPublicKey = v
}

// GetArmoredSignature returns the ArmoredSignature field value if set, zero value otherwise.
func (o *CreateGPGKeyOption) GetArmoredSignature() string {
	if o == nil || o.ArmoredSignature == nil {
		var ret string
		return ret
	}
	return *o.ArmoredSignature
}

// GetArmoredSignatureOk returns a tuple with the ArmoredSignature field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *CreateGPGKeyOption) GetArmoredSignatureOk() (*string, bool) {
	if o == nil || o.ArmoredSignature == nil {
		return nil, false
	}
	return o.ArmoredSignature, true
}

// HasArmoredSignature returns a boolean if a field has been set.
func (o *CreateGPGKeyOption) HasArmoredSignature() bool {
	if o != nil && o.ArmoredSignature != nil {
		return true
	}

	return false
}

// SetArmoredSignature gets a reference to the given string and assigns it to the ArmoredSignature field.
func (o *CreateGPGKeyOption) SetArmoredSignature(v string) {
	o.ArmoredSignature = &v
}

func (o CreateGPGKeyOption) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["armored_public_key"] = o.ArmoredPublicKey
	}
	if o.ArmoredSignature != nil {
		toSerialize["armored_signature"] = o.ArmoredSignature
	}
	return json.Marshal(toSerialize)
}

type NullableCreateGPGKeyOption struct {
	value *CreateGPGKeyOption
	isSet bool
}

func (v NullableCreateGPGKeyOption) Get() *CreateGPGKeyOption {
	return v.value
}

func (v *NullableCreateGPGKeyOption) Set(val *CreateGPGKeyOption) {
	v.value = val
	v.isSet = true
}

func (v NullableCreateGPGKeyOption) IsSet() bool {
	return v.isSet
}

func (v *NullableCreateGPGKeyOption) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCreateGPGKeyOption(val *CreateGPGKeyOption) *NullableCreateGPGKeyOption {
	return &NullableCreateGPGKeyOption{value: val, isSet: true}
}

func (v NullableCreateGPGKeyOption) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCreateGPGKeyOption) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


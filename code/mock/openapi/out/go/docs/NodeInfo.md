# NodeInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metadata** | Pointer to **map[string]interface{}** |  | [optional] 
**OpenRegistrations** | Pointer to **bool** |  | [optional] 
**Protocols** | Pointer to **[]string** |  | [optional] 
**Services** | Pointer to [**NodeInfoServices**](NodeInfoServices.md) |  | [optional] 
**Software** | Pointer to [**NodeInfoSoftware**](NodeInfoSoftware.md) |  | [optional] 
**Usage** | Pointer to [**NodeInfoUsage**](NodeInfoUsage.md) |  | [optional] 
**Version** | Pointer to **string** |  | [optional] 

## Methods

### NewNodeInfo

`func NewNodeInfo() *NodeInfo`

NewNodeInfo instantiates a new NodeInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNodeInfoWithDefaults

`func NewNodeInfoWithDefaults() *NodeInfo`

NewNodeInfoWithDefaults instantiates a new NodeInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetadata

`func (o *NodeInfo) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *NodeInfo) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *NodeInfo) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *NodeInfo) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetOpenRegistrations

`func (o *NodeInfo) GetOpenRegistrations() bool`

GetOpenRegistrations returns the OpenRegistrations field if non-nil, zero value otherwise.

### GetOpenRegistrationsOk

`func (o *NodeInfo) GetOpenRegistrationsOk() (*bool, bool)`

GetOpenRegistrationsOk returns a tuple with the OpenRegistrations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenRegistrations

`func (o *NodeInfo) SetOpenRegistrations(v bool)`

SetOpenRegistrations sets OpenRegistrations field to given value.

### HasOpenRegistrations

`func (o *NodeInfo) HasOpenRegistrations() bool`

HasOpenRegistrations returns a boolean if a field has been set.

### GetProtocols

`func (o *NodeInfo) GetProtocols() []string`

GetProtocols returns the Protocols field if non-nil, zero value otherwise.

### GetProtocolsOk

`func (o *NodeInfo) GetProtocolsOk() (*[]string, bool)`

GetProtocolsOk returns a tuple with the Protocols field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtocols

`func (o *NodeInfo) SetProtocols(v []string)`

SetProtocols sets Protocols field to given value.

### HasProtocols

`func (o *NodeInfo) HasProtocols() bool`

HasProtocols returns a boolean if a field has been set.

### GetServices

`func (o *NodeInfo) GetServices() NodeInfoServices`

GetServices returns the Services field if non-nil, zero value otherwise.

### GetServicesOk

`func (o *NodeInfo) GetServicesOk() (*NodeInfoServices, bool)`

GetServicesOk returns a tuple with the Services field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServices

`func (o *NodeInfo) SetServices(v NodeInfoServices)`

SetServices sets Services field to given value.

### HasServices

`func (o *NodeInfo) HasServices() bool`

HasServices returns a boolean if a field has been set.

### GetSoftware

`func (o *NodeInfo) GetSoftware() NodeInfoSoftware`

GetSoftware returns the Software field if non-nil, zero value otherwise.

### GetSoftwareOk

`func (o *NodeInfo) GetSoftwareOk() (*NodeInfoSoftware, bool)`

GetSoftwareOk returns a tuple with the Software field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSoftware

`func (o *NodeInfo) SetSoftware(v NodeInfoSoftware)`

SetSoftware sets Software field to given value.

### HasSoftware

`func (o *NodeInfo) HasSoftware() bool`

HasSoftware returns a boolean if a field has been set.

### GetUsage

`func (o *NodeInfo) GetUsage() NodeInfoUsage`

GetUsage returns the Usage field if non-nil, zero value otherwise.

### GetUsageOk

`func (o *NodeInfo) GetUsageOk() (*NodeInfoUsage, bool)`

GetUsageOk returns a tuple with the Usage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsage

`func (o *NodeInfo) SetUsage(v NodeInfoUsage)`

SetUsage sets Usage field to given value.

### HasUsage

`func (o *NodeInfo) HasUsage() bool`

HasUsage returns a boolean if a field has been set.

### GetVersion

`func (o *NodeInfo) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *NodeInfo) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *NodeInfo) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *NodeInfo) HasVersion() bool`

HasVersion returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



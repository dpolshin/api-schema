// Code generated by protoc-gen-go. DO NOT EDIT.
// source: definitions.proto

package dialog

import (
	fmt "fmt"
	_ "github.com/gogo/protobuf/types"
	proto "github.com/golang/protobuf/proto"
	descriptor "github.com/golang/protobuf/protoc-gen-go/descriptor"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type UUIDValue struct {
	Msb                  int64    `protobuf:"varint,1,opt,name=msb,proto3" json:"msb,omitempty"`
	Lsb                  int64    `protobuf:"varint,2,opt,name=lsb,proto3" json:"lsb,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *UUIDValue) Reset()         { *m = UUIDValue{} }
func (m *UUIDValue) String() string { return proto.CompactTextString(m) }
func (*UUIDValue) ProtoMessage()    {}
func (*UUIDValue) Descriptor() ([]byte, []int) {
	return fileDescriptor_bef01fe2be18d2f0, []int{0}
}

func (m *UUIDValue) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UUIDValue.Unmarshal(m, b)
}
func (m *UUIDValue) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UUIDValue.Marshal(b, m, deterministic)
}
func (m *UUIDValue) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UUIDValue.Merge(m, src)
}
func (m *UUIDValue) XXX_Size() int {
	return xxx_messageInfo_UUIDValue.Size(m)
}
func (m *UUIDValue) XXX_DiscardUnknown() {
	xxx_messageInfo_UUIDValue.DiscardUnknown(m)
}

var xxx_messageInfo_UUIDValue proto.InternalMessageInfo

func (m *UUIDValue) GetMsb() int64 {
	if m != nil {
		return m.Msb
	}
	return 0
}

func (m *UUIDValue) GetLsb() int64 {
	if m != nil {
		return m.Lsb
	}
	return 0
}

type DialogOptions struct {
	Log                  string   `protobuf:"bytes,1,opt,name=log,proto3" json:"log,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DialogOptions) Reset()         { *m = DialogOptions{} }
func (m *DialogOptions) String() string { return proto.CompactTextString(m) }
func (*DialogOptions) ProtoMessage()    {}
func (*DialogOptions) Descriptor() ([]byte, []int) {
	return fileDescriptor_bef01fe2be18d2f0, []int{1}
}

func (m *DialogOptions) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DialogOptions.Unmarshal(m, b)
}
func (m *DialogOptions) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DialogOptions.Marshal(b, m, deterministic)
}
func (m *DialogOptions) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DialogOptions.Merge(m, src)
}
func (m *DialogOptions) XXX_Size() int {
	return xxx_messageInfo_DialogOptions.Size(m)
}
func (m *DialogOptions) XXX_DiscardUnknown() {
	xxx_messageInfo_DialogOptions.DiscardUnknown(m)
}

var xxx_messageInfo_DialogOptions proto.InternalMessageInfo

func (m *DialogOptions) GetLog() string {
	if m != nil {
		return m.Log
	}
	return ""
}

/// server timestamp when state was created or modified
type DataClock struct {
	Clock                int64    `protobuf:"varint,1,opt,name=clock,proto3" json:"clock,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DataClock) Reset()         { *m = DataClock{} }
func (m *DataClock) String() string { return proto.CompactTextString(m) }
func (*DataClock) ProtoMessage()    {}
func (*DataClock) Descriptor() ([]byte, []int) {
	return fileDescriptor_bef01fe2be18d2f0, []int{2}
}

func (m *DataClock) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DataClock.Unmarshal(m, b)
}
func (m *DataClock) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DataClock.Marshal(b, m, deterministic)
}
func (m *DataClock) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DataClock.Merge(m, src)
}
func (m *DataClock) XXX_Size() int {
	return xxx_messageInfo_DataClock.Size(m)
}
func (m *DataClock) XXX_DiscardUnknown() {
	xxx_messageInfo_DataClock.DiscardUnknown(m)
}

var xxx_messageInfo_DataClock proto.InternalMessageInfo

func (m *DataClock) GetClock() int64 {
	if m != nil {
		return m.Clock
	}
	return 0
}

var E_Dlg = &proto.ExtensionDesc{
	ExtendedType:  (*descriptor.FieldOptions)(nil),
	ExtensionType: (*DialogOptions)(nil),
	Field:         100001,
	Name:          "dialog.dlg",
	Tag:           "bytes,100001,opt,name=dlg",
	Filename:      "definitions.proto",
}

func init() {
	proto.RegisterType((*UUIDValue)(nil), "dialog.UUIDValue")
	proto.RegisterType((*DialogOptions)(nil), "dialog.DialogOptions")
	proto.RegisterType((*DataClock)(nil), "dialog.DataClock")
	proto.RegisterExtension(E_Dlg)
}

func init() { proto.RegisterFile("definitions.proto", fileDescriptor_bef01fe2be18d2f0) }

var fileDescriptor_bef01fe2be18d2f0 = []byte{
	// 248 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x54, 0x8f, 0xcd, 0x4a, 0xc4, 0x30,
	0x14, 0x85, 0xa9, 0xc5, 0x42, 0x23, 0x82, 0x96, 0x19, 0xa9, 0x03, 0x42, 0xa7, 0xab, 0x59, 0xdd,
	0x82, 0xee, 0xdc, 0x08, 0x5a, 0x44, 0x57, 0x42, 0x61, 0xdc, 0xe7, 0x6f, 0x42, 0xf0, 0xce, 0xdc,
	0x92, 0x74, 0x7c, 0x0b, 0x1f, 0xc2, 0x57, 0xf3, 0x49, 0x24, 0x49, 0x5d, 0xb8, 0xca, 0xb9, 0x37,
	0x27, 0xdf, 0x39, 0x61, 0x97, 0x4a, 0xef, 0xec, 0xc1, 0x4e, 0x96, 0x0e, 0x1e, 0x46, 0x47, 0x13,
	0x55, 0x85, 0xb2, 0x1c, 0xc9, 0xac, 0x96, 0x5e, 0x72, 0xe4, 0xa3, 0xe8, 0xe6, 0x33, 0x5d, 0xaf,
	0x1a, 0x43, 0x64, 0x50, 0x77, 0x71, 0x12, 0xc7, 0x5d, 0xa7, 0xb4, 0x97, 0xce, 0x8e, 0x13, 0xb9,
	0xe4, 0x68, 0x3b, 0x56, 0x6e, 0xb7, 0xaf, 0xfd, 0x3b, 0xc7, 0xa3, 0xae, 0x2e, 0x58, 0xbe, 0xf7,
	0xa2, 0xce, 0x9a, 0x6c, 0x93, 0x0f, 0x41, 0x86, 0x0d, 0x7a, 0x51, 0x9f, 0xa4, 0x0d, 0x7a, 0xd1,
	0xae, 0xd9, 0x79, 0x1f, 0x33, 0xdf, 0xc6, 0x58, 0x24, 0x5a, 0xc8, 0xc4, 0x47, 0xe5, 0x10, 0x64,
	0xbb, 0x66, 0x65, 0xcf, 0x27, 0xfe, 0x84, 0x24, 0x3f, 0xaa, 0x05, 0x3b, 0x95, 0x41, 0xcc, 0xd4,
	0x34, 0xdc, 0xbf, 0xb0, 0x5c, 0xa1, 0xa9, 0x6e, 0x20, 0x15, 0x84, 0xbf, 0x82, 0xf0, 0x6c, 0x35,
	0xaa, 0x19, 0x5d, 0x7f, 0x7f, 0x15, 0x4d, 0xb6, 0x39, 0xbb, 0x5d, 0x42, 0xfa, 0x26, 0xfc, 0x4b,
	0x1e, 0x02, 0xe2, 0xf1, 0xfa, 0xe7, 0xe1, 0x8a, 0x2d, 0xec, 0x1e, 0x14, 0x1a, 0x30, 0x6e, 0x94,
	0xe0, 0xb5, 0xfb, 0xb4, 0x52, 0x7b, 0x51, 0x44, 0xea, 0xdd, 0x6f, 0x00, 0x00, 0x00, 0xff, 0xff,
	0xbb, 0xf0, 0x14, 0x7c, 0x38, 0x01, 0x00, 0x00,
}
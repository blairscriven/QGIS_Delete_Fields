# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xf9\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x16\x00\x00\x00\x16\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\
\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\
\x04\x67\x41\x4d\x41\x00\x00\xb1\x8f\x0b\xfc\x61\x05\x00\x00\x00\
\x09\x70\x48\x59\x73\x00\x00\x12\x74\x00\x00\x12\x74\x01\xde\x66\
\x1f\x78\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\
\xa0\xbd\xa7\x93\x00\x00\x00\x07\x74\x49\x4d\x45\x07\xd9\x02\x15\
\x16\x11\x2c\x9d\x48\x83\xbb\x00\x00\x00\x69\x49\x44\x41\x54\x48\
\x4b\x63\x64\x60\x60\xf8\x0f\xc4\x54\x07\x60\x83\x7f\x66\xd4\x42\
\x78\x68\x80\x7d\x46\x33\xc3\xcc\x9b\xaf\xa0\x3c\x54\x90\xae\x2e\
\xc6\x80\x4f\x1f\x13\x94\x4d\x75\xc0\x02\xa5\x19\xfa\x67\xcc\x80\
\xb2\x20\xa0\x30\x23\x03\xca\x62\x60\x58\x96\xff\x08\xca\x82\x80\
\xa8\x89\x72\x50\x16\x6e\x7d\x34\x0b\x8a\xa1\x17\x79\xa3\x2e\x86\
\x83\x51\x17\x83\xc1\xa8\x8b\x51\xc0\xa8\x8b\xc1\x60\xd4\xc5\x48\
\x80\x81\x01\x00\xe7\x4a\x77\x07\x16\xdf\x7a\x81\x00\x00\x00\x00\
\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x07\
\x07\x3b\xe0\xb3\
\x00\x70\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x73\
\x00\x11\
\x06\xb5\xf9\x03\
\x00\x44\
\x00\x65\x00\x6c\x00\x65\x00\x74\x00\x65\x00\x5f\x00\x44\x00\x75\x00\x70\x00\x6c\x00\x69\x00\x63\x00\x61\x00\x74\x00\x65\x00\x73\
\
\x00\x08\
\x0a\x61\x5a\xa7\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x3c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x3c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x88\x8b\x7b\xcc\xb6\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

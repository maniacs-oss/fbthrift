#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from thrift.lib.py3.thrift_server cimport cServerInterface

cdef extern from "src/gen-cpp2/SimpleService.h" namespace "py3::simple":
    cdef cppclass cSimpleServiceSvAsyncIf "py3::simple::SimpleServiceSvAsyncIf":
      pass

    cdef cppclass cSimpleServiceSvIf "py3::simple::SimpleServiceSvIf"(cSimpleServiceSvAsyncIf, cServerInterface):
      pass


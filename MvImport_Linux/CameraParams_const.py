#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Don't change this file, it was auto generated by Const_file_Generater.py.

# ch: 设备类型定义 | en: Device Type Definition
MV_UNKNOW_DEVICE                             = 0x00000000  # ch:未知设备类型，保留意义 | en:Unknown Device Type, Reserved
MV_GIGE_DEVICE                               = 0x00000001  # ch:GigE设备 | en:GigE Device
MV_1394_DEVICE                               = 0x00000002  # ch:1394-a/b 设备 | en:1394-a/b Device
MV_USB_DEVICE                                = 0x00000004  # ch:USB3.0 设备 | en:USB3.0 Device
MV_CAMERALINK_DEVICE                         = 0x00000008  # ch:CameraLink设备 | en:CameraLink Device
MV_VIR_GIGE_DEVICE                           = 0x00000010  # ch:虚拟GigE设备 | en:Virtual GigE Device
MV_VIR_USB_DEVICE                            = 0x00000020  # ch:虚拟USB设备  | en:Virtual USB Device
MV_GENTL_GIGE_DEVICE                         = 0x00000040  # ch:自研网卡下GigE设备 | en:GenTL GigE Device
MV_GENTL_CAMERALINK_DEVICE                   = 0x00000080  # ch:CameraLink设备 | en:GenTL CameraLink Device
MV_GENTL_CXP_DEVICE                          = 0x00000100  # ch:CoaXPress设备 | en:GenTL CoaXPress Device
MV_GENTL_XOF_DEVICE                          = 0x00000200  # ch:XoF设备 | en:GenTL XoF Device

# ch:采集卡类型 | en:Interface type
MV_GIGE_INTERFACE                    = 0x00000001          # ch:GigE Vision采集卡 | en:GigE Vision interface
MV_CAMERALINK_INTERFACE              = 0x00000004          # ch:Camera Link采集卡 | eh:Camera Link interface
MV_CXP_INTERFACE                     = 0x00000008          # ch:CoaXPress采集卡 | en:CoaXPress interface
MV_XOF_INTERFACE                     = 0x00000010          # ch:XoFLink采集卡 | en:XoFLink interface

INFO_MAX_BUFFER_SIZE                         = 64          # ch:最大的数据信息大小 | eh:Maximum data information size
MV_MAX_TLS_NUM                               = 8           # ch:最多支持的传输层实例个数 | eh:The maximum number of supported transport layer instances
MV_MAX_DEVICE_NUM                            = 256         # ch:最大支持的设备个数 | eh:The maximum number of supported devices

MV_MAX_INTERFACE_NUM                         = 64          # ch:最大支持的采集卡数量 | eh:The maximum number of Frame Grabber interface supported

MV_MAX_SERIAL_PORT_NUM                       = 64          # ch:最大支持的串口数量 | eh:The maximum number of serial port supported

MV_MAX_GENTL_IF_NUM                          = 256         # ch:最大支持的GenTL数量 | eh:The maximum number of GenTL supported
MV_MAX_GENTL_DEV_NUM                         = 256         # ch:最大支持的GenTL设备数量 | eh:The maximum number of GenTL devices supported

MAX_EVENT_NAME_SIZE                          = 128  # 相机Event事件名称最大长度 | en:Max length of event name
MV_MAX_SPLIT_NUM                             = 8    # ch: 分时曝光时最多将源图像拆分的个数 | en:The maximum number of source image to be split in time-division exposure

# ch: GigEVision IP配置 | en: GigEVision IP Configuration
MV_IP_CFG_STATIC                             = 0x05000000  # ch: 静态 | en: Static
MV_IP_CFG_DHCP                               = 0x06000000  # ch: DHCP | en: DHCP
MV_IP_CFG_LLA                                = 0x04000000  # ch: LLA | en: LLA

# ch: GigEVision网络传输模式 | en: GigEVision Net Transfer Mode
MV_NET_TRANS_DRIVER                          = 0x00000001  # ch: 驱动 | en: Driver
MV_NET_TRANS_SOCKET                          = 0x00000002  # ch: Socket | en: Socket

MV_MATCH_TYPE_NET_DETECT                     = 0x00000001  # ch:网络流量和丢包信息 | en:Network traffic and packet loss information
MV_MATCH_TYPE_USB_DETECT                     = 0x00000002  # ch:host接收到来自U3V设备的字节总数 | en:The total number of bytes host received from U3V device

MV_MAX_XML_NODE_NUM_C                        = 128  # ch: 某个节点对应的子节点个数最大值 | en: The maximum number of child nodes corresponding to a node
MV_MAX_XML_NODE_STRLEN_C                     = 64   # ch: 节点名称字符串最大长度 | en: The maximum length of node name string
MV_MAX_XML_STRVALUE_STRLEN_C                 = 64   # ch: 节点String值最大长度 | en: The maximum length of Node String
MV_MAX_XML_DISC_STRLEN_C                     = 512  # ch: 节点描述字段最大长度 | en: The maximum length of the node description field
MV_MAX_XML_ENTRY_NUM                         = 10   # ch: 最多的单元数 | en: The maximum number of units
MV_MAX_XML_PARENTS_NUM                       = 8    # ch: 父节点个数上限 | en: The maximum number of parent nodes
MV_MAX_XML_SYMBOLIC_STRLEN_C                 = 64   # ch: 每个已经实现单元的名称长度 | en: The length of the name of each unit that has been implemented
MV_MAX_XML_SYMBOLIC_NUM                      = 64   # ch: 最大XML符号数 | en: Max XML Symbolic Number
MV_MAX_SYMBOLIC_LEN                          = 64   # ch:最大枚举条目对应的符号长度 | en:Max Enum Entry Symbolic Number

# ch: 异常消息类型 | en: Exception message type
MV_EXCEPTION_DEV_DISCONNECT                  = 0x00008001  # ch:设备断开连接 | en:The device is disconnected
MV_EXCEPTION_VERSION_CHECK                   = 0x00008002  # ch:SDK与驱动版本不匹配 | en:SDK does not match the driver version

# ch:设备的访问模式 | en:Device Access Mode
# ch:独占权限，其他APP只允许读CCP寄存器| en:Exclusive authority, other APP is only allowed to read the CCP register
MV_ACCESS_Exclusive                          = 1
# ch:可以从5模式下抢占权限，然后以独占权限打开| en:You can seize the authority from the 5 mode, and then open with exclusive authority
MV_ACCESS_ExclusiveWithSwitch                = 2
# ch:控制权限，其他APP允许读所有寄存器| en:Control authority, allows other APP reading all registers
MV_ACCESS_Control                            = 3
# ch:可以从5的模式下抢占权限，然后以控制权限打开| en:You can seize the authority from the 5 mode, and then open with control authority
MV_ACCESS_ControlWithSwitch                  = 4
# ch:以可被抢占的控制权限打开| en:Open with seized control authority
MV_ACCESS_ControlSwitchEnable                = 5
# ch:可以从5的模式下抢占权限，然后以可被抢占的控制权限打开| en:You can seize the authority from the 5 mode, and then open with seized control authority
MV_ACCESS_ControlSwitchEnableWithKey         = 6
# ch:读模式打开设备，适用于控制权限下| en:Open with read mode and is available under control authority
MV_ACCESS_Monitor                            = 7

# ch: 波特率 | en: CameraLink Baud Rates (CLUINT32)
MV_CAML_BAUDRATE_9600                        = 0x00000001  # ch: 9600 | en: 9600
MV_CAML_BAUDRATE_19200                       = 0x00000002  # ch: 19200 | en: 19200
MV_CAML_BAUDRATE_38400                       = 0x00000004  # ch: 38400 | en: 38400
MV_CAML_BAUDRATE_57600                       = 0x00000008  # ch: 57600 | en: 57600
MV_CAML_BAUDRATE_115200                      = 0x00000010  # ch: 115200 | en: 115200
MV_CAML_BAUDRATE_230400                      = 0x00000020  # ch: 230400 | en: 230400
MV_CAML_BAUDRATE_460800                      = 0x00000040  # ch: 460800 | en: 460800
MV_CAML_BAUDRATE_921600                      = 0x00000080  # ch: 921600 | en: 921600
MV_CAML_BAUDRATE_AUTOMAX                     = 0x40000000  # ch: 最大值 | en: Auto Max
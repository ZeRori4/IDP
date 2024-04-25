# -*- coding: utf-8 -*-
# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 5</title>
	<version>1.0</version>
<parameter>
    <type>string_from_list</type>
    <id>TYPE_OBJ</id>
    <name>Тип объекта</name>
    <value>ip_cameras</value>
    <string_list>ip_cameras,channels</string_list>
</parameter>
</parameters>
'''

import host

GLOBALS = globals()

TYPE_OBJ = GLOBALS.get("TYPE_OBJ", "ip_cameras")


def get_data_from_ip_device():
    device_info_list = []
    device_info = {}
    for sett in host.settings("ip_cameras").ls():
        if sett.type == "Grabber":
            device_info["name"] = sett.name
            device_info["guid"] = sett.guid
            device_info_list.append(device_info)
    return device_info_list


def get_data_from_channel():
    channel_info_list = []
    channel_info = {}
    for sett in host.settings("channels").ls():
        if sett.type == "Channel":
            channel_info["guid"] = sett.guid
            channel_info["name"] = sett.name
            channel_info_list.append(channel_info)
    return channel_info_list


if TYPE_OBJ == "ip_cameras":
    host.message(get_data_from_ip_device(), 10 * 1e3)
else:
    host.message(get_data_from_channel(), 10 * 1e3)

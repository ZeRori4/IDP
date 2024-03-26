# -*- coding: utf-8 -*-
# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 6</title>
	<version>1.0</version>
</parameters>
'''
import host


def get_data_from_ip_device():
    device_info_list = []
    device_info = {}
    for sett in host.settings("/{}/ip_cameras".format(host.settings("").guid)).ls():
        if sett.type == "Grabber":
            if sett["grabber_enabled"]:
                device_info["name"] = sett["name"]
                device_info["guid"] = sett.guid
                device_info["channel00_audio_codec"] = sett["channel00_audio_codec"]
                device_info["channel00_resolution"] = sett["channel00_resolution"]
                device_info["channel00_fps"] = sett["channel00_fps"]
                device_info_list.append(device_info)
                device_info = {}
    return device_info_list


host.message(get_data_from_ip_device())

# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 9</title>
	<version>1.0</version>
</parameters>
'''
import os
import json

import host

shots_path = host.settings("system_wide_options")["screenshots_folder"]
new_folder = "new_folder_name"
new_path = os.path.join(shots_path, new_folder)
if not os.path.exists(new_path):
    os.makedirs(new_path)
name_file = "ip_cameras.json"
file_path = os.path.join(new_path, name_file)

def get_data_from_ip_device():
    device_info_list = []
    device_info = {}
    for sett in host.settings("ip_cameras").ls():
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


with open(file_path, 'w') as f:
    json.dump(get_data_from_ip_device(), f)

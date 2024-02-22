import host
import os
import json

shots_path = host.settings("system_wide_options")["screenshots_folder"]
name_file = "ip_cameras.json"
full_path = shots_path + "/" + name_file

server_guid = host.settings("").guid
ip_cameras = objects_list("IP Device")
guid_camers = [info[1] for info in ip_cameras]
result = []
for camera in guid_camers:
    data = {}
    data["name"] = host.settings("/%s/ip_cameras/%s" % (server_guid, camera))["name"]
    data["guid"] = camera
    data["channel00_audio_codec"] = host.settings("/%s/ip_cameras/%s" % (server_guid, camera))["channel00_audio_codec"]
    data["channel00_resolution"] = host.settings("/%s/ip_cameras/%s" % (server_guid, camera))["channel00_resolution"]
    data["channel00_fps"] = host.settings("/%s/ip_cameras/%s" % (server_guid, camera))["channel00_fps"]
    result.append(data)

with open(full_path, 'w') as f:
    json.dump(result, f)


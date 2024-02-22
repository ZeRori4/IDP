# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 6</title>
	<version>1.0</version>
</parameters>
'''
import host
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

message(result)
raise Exception(result)
# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 34</title>
	<version>1.0</version>
    <parameter>
        <type>string</type>
        <name>token</name>
        <id>token</id>
        <value></value>
    </parameter>
</parameters>
'''

import os
import time
import base64

import host

GLOBALS = globals()

TOKEN = GLOBALS.get("TOKEN", "MOTION")


def handler(ev):
    channel_id = "jNKP0Kkf_LJ4ppdNR"
    date = int(time.time())
    file_name = "1223.jpg"
    full_path = "C:\DSSL\Trassir-4.5.10.0-1207057-64-Release\shots"
    new_path = os.path.join(full_path, file_name)
    host.screenshot_v2(channel_id, file_name, full_path, str(date))

    with open(new_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    channel = {
        "type": "trassir_channel",
        "channel_guid": "jNKP0Kkf",
        "name": "My channel Name",
        "server_guid": "LJ4ppdNR"
    }
    image = {
        "type": "image",
        "format": "JPEG",
        "image_base64": image_base64
    }
    alarm = {
        "type_token": TOKEN,
        "contents": [channel, image]
    }
    host.fire_alarm(alarm)


host.activate_on_events("Motion Start", "", handler)

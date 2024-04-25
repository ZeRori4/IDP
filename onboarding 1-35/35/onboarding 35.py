# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 35</title>
	<version>1.0</version>
    <parameter>
        <type>string</type>
        <name>token</name>
        <id>token</id>
        <value></value>
    </parameter>
</parameters>
'''

import host


GLOBALS = globals()

TOKEN = GLOBALS.get("TOKEN", "MOTION")
channel = {
   "type": "trassir_channel",
   "channel_guid": "eVEbBqWn",
   "name": "My channel Name",
   "server_guid": "LJ4ppdNR"
}
image = {
  "type": "image",
  "format": "JPEG",
  "image_base64": "c29tZSBkYXRhIGhlcmU="
}
alarm = {
  "type_token": TOKEN,
  "contents": [channel, image]
}
host.fire_alarm(alarm)


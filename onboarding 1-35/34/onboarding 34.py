# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 34</title>
	<version>1.0</version>
    <parameter>
        <type>string</type>
        <name>token</name>
        <id>TOKEN</id>
        <value></value>
    </parameter>
</parameters>
'''

import host
GLOBALS = globals()

TOKEN = GLOBALS.get("TOKEN", "MOTION")

alarm = {
  "token": TOKEN
}
res = host.fire_alarm(alarm)
if res:
  print("OK")
else:
  print("FAIL")

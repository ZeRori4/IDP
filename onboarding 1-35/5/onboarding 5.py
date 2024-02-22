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
    <string_list>IP Device,Channel</string_list>
</parameter>
</parameters>
'''

import host

GLOBALS = globals()

TYPE_OBJ = GLOBALS.get("TYPE_OBJ", "IP Device")

result = [(x[0], x[1]) for x in objects_list(TYPE_OBJ)]
message(result, 10*1e3)

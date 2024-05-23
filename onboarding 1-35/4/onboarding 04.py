# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 4</title>
	<version>1.0</version>
<parameter>
    <type>date</type>
    <id>DATA</id>
    <name>Дата для вывода</name>
    <value>12-03-01</value>
</parameter>
</parameters>
'''

import datetime
import time

GLOBALS = globals()

DATA = GLOBALS.get("DATA", "")

element = datetime.datetime.strptime(DATA, "%d.%m.%Y")
tuple = element.timetuple()
timestamp = time.mktime(tuple)
raise Exception(timestamp)

# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 10</title>
	<version>1.0</version>
    <parameter>
        <type>string_from_list</type>
        <id>user_function</id>
        <name>Тип скриншота</name>
        <value>с фигурами</value>
    <string_list>с фигурами,без фигур</string_list>
    </parameter>
    <parameter>
        <type>channel</type>
        <id>channel_id</id>
        <name>Канал</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Имя файла:</name>
        <id>file_name</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Путь сохранения файла:</name>
        <id>full_path</id>
        <value></value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>date_start</id>
        <name>Дата, за которую будет сохраняться скриншот</name>
        <value>2014-03-01</value>
    </parameter>
</parameters>
'''

import host
import time
import datetime

GLOBALS = globals()

USER_FUNCTION = GLOBALS.get("USER_FUNCTION", "с фигурами")
CHANNEL_ID = GLOBALS.get("CHANNEL_ID", "")
FILE_NAME = GLOBALS.get("FILE_NAME", "")
FULL_PATH = GLOBALS.get("FULL_PATH", "")
DATE_START = GLOBALS.get("DATE_START", "21.04.2024")

date = int(
    time.mktime(datetime.datetime.strptime(DATE_START, '%d.%m.%Y').timetuple())
)


def screenshot_mode(user_function, channel_id, file_name, full_path, date):
    return (
        host.screenshot_v2_figures(channel_id, file_name, full_path, str(date))
        if user_function == "с фигурами"
        else host.screenshot_v2(channel_id, file_name, full_path, str(date))
    )

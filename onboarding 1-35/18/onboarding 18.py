# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 18</title>
	<version>1.0</version>
    <parameter>
        <type>channel</type>
        <id>CHANNEL_FULL_GUID</id>
        <name>Канал</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>COLOR</id>
        <name>color</name>
        <value>1FC619</value>
    </parameter>
</parameters>
'''

import host

GLOBALS = globals()

COLOR = GLOBALS.get("COLOR", "")
CHANNEL_FULL_GUID = GLOBALS.get("CHANNEL_FULL_GUID", "")

channel_guid = CHANNEL_FULL_GUID.split("_")[0]

rect = "rect {x1} {y1} {x2} {y2} {color}"

figures = [
    rect.format(x1=30, y1=30, x2=50, y2=50, color=COLOR),
]

host.figure_set(channel_guid, figures)


def clear():
    host.figure_remove(channel_guid)


host.timeout(2000, clear)
# как почистить фигуры во време выключения скрипта в этом же скрипте так и не понял
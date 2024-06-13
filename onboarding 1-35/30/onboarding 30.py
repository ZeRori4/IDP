# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 30</title>
	<version>1.0</version>
    <parameter>
        <type>channel</type>
        <id>channel_id</id>
        <name>Канал</name>
        <value></value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>date_start</id>
        <name>даты начала экспорта</name>
        <value>2014-03-01</value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>date_end</id>
        <name>даты окончания экспорта</name>
        <value>2014-03-01</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Путь сохранения файла</name>
        <id>full_path</id>
        <value></value>
    </parameter>

</parameters>
'''

import host


GLOBALS = globals()

channel_id = GLOBALS.get("channel_id", "")
full_path = GLOBALS.get("full_path", "")
date_start = GLOBALS.get("date_start", "07.02.2024")
date_end = GLOBALS.get("date_end", "08.02.2024")

channel_guid, server_guid = channel_id.split("_")


def callback(task_status):
    # 0 - задача отменена; 1 - задача выполняется; 2 - задача провалилась; 3 - задача успешно завершилась

    if task_status == 0:
        status_string = "CANCELED";
    elif task_status == 1:
        status_string = "IN PROGRESS";
    elif task_status == 2:
        status_string = "FAILED";
    elif task_status == 3:
        status_string = "SUCCEEDED";
    else:
        status_string = "Unknown status " + str(task_status);

    host.alert("export status updated: " + status_string)


host.archive_export(
    server_guid,
    channel_guid,
    full_path,
    date_start,
    date_end,
    {},
    callback
)

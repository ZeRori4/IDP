# -*- coding: utf-8 -*-
# Напишите здесь описание скрипта
"""
<parameters>
	<title>onboarding 32</title>
	<version>1.0</version>
    <parameter>
        <type>integer</type>
        <name>Количество строк</name>
        <id>DB_ROW</id>
        <value></value>
    </parameter>

    <resources>
        <resource>database/base.py</resource>
        <resource>database/schema.py</resource>
        <resource>database/__init__.py</resource>
    </resources>

</parameters>
"""

import os
import csv
from schema import init_db
import sqlalchemy as sa

GLOBALS = globals()

DB_ROW = GLOBALS.get("DB_ROW", "")

db = init_db()
shots_path = os.path.expanduser(host.settings("system_wide_options")["screenshots_folder"])
name_file = "last_events.csv"
csv_filename = os.path.join(shots_path, name_file)

events = db.query(EventLog).order_by(EventLog.id.desc()).limit(DB_ROW)

with open(csv_filename, 'w') as csvfile:
    fieldnames = ['id', 'event_type', 'ts', 'origin', 'p1', 'p2', 'p3', 'flags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for event in events:
        writer.writerow(
            [
                event.id,
                event.event_type,
                event.ts,
                event.origin,
                event.p1,
                event.p2,
                event.p3,
                event.flags
            ]
        )

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
        <resource>schema.py</resource>
    </resources>

</parameters>
"""

resources = {
    "schema.py": """
        eNqVU01r3DAQvRv8H4RPWlgMbaCHgqFs00Cg9JLcShGyPdaK6MPRyKH+95VWltdssqHRyZ55
        781oNG9wVpPOKgWdl9YgkXq0zhPDNfR+GhWURVksQXxWXHVH0DPhSJCXxRDp53ANf33dQ6e4
        416+QFbbhFjLEV4TrdMZjIAYWtH8Cdym+NGij7+HwCfNK0m6i8mHxA35rUrM4ZpZMJRP3g5q
        wmNzxxXCnsRAZ7WWPkVOimUR6iCSHy9g/E8raKy/+1oWJBzGPG8VxGExFqQriCimrKgSQPax
        FV5/t2rShoave+NBgNuT0UnN3cyeYG4e3RTqm0mpKLdWjwpJ0c8jXFV6k+fxEn+Q4n2KdVJI
        c0l78E4aQW++7K7Qxk+XlMewBtfAnz8CvvkAeFBc4P/PKJG+nR5Xgz/aPkV6GMjzBG6mncL8
        zvE48JMzea/qMyZtyS0Pq5BW8+wdWt0eqj35XeXtqf4s8FhGGulZ31IwYezQ/LJmXSyhbMtV
        Lpa7lQNJWCKRRPimvSXRnHxSCwjKS0ess8Yke9P14osJ6pAbpJgc0Faavkkqy0TftszWIckz
        GxOt+su08lRoHkAA/ANuUXBN
    """,
}
t1utils.resources_check(script_path, resources)

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

# -*- coding: utf-8 -*-
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

resources = {
    "database/base.py": """
        eNqNVE1v2zAMvRvwfxC8ix0kPg8BDKxFu1M3bMhuw2DIFu0KsaWUktPm34+ypMZJg2E+ie/x
        44mk/IltVhvWaiFVv2WT7TafHZImHeqR8GGA1kqtDJPjQaNlio8g7HQY4N1HWXizg2yiS0BG
        rngPmCZpEgjzMvChfYbxxLhhht8gSo3jTOqQfkHBWxtL7H4+3Xn0EVHjLV9bCmgHjtzKI8S4
        BVQ33MBC3LM21plpMoLlglvOKtJYfiPrgay8SJMdGEPNcIQuTasPIGrjsdwh/jjyPWBenP1r
        BC4A/zssTe5JG7lfy82jtCoeZu8v1x0X0LFYoB20geoXTrBmCKM+QvWVD4as1Wr/yrE3xTZN
        GH1Zlv1AfZQCGGcWuTJ8nj0f2CyacdSTEkQaQAmG6Y4R7PTRgpQU7vMoeI3XozuEHuTv1byT
        xVMo676ThEEsA8/UAixbPY7S5iEF7QMcPuyC2x5A3N7OgLTRDW/3MYf7kEvqNsV4qJN042Gp
        TnZs7uIC+qDM8cukFOO7fRW0i0JmMi/8yrkFa/zMzw8sD2N5uM/W7Hf2eARln3RPRhbKLo71
        ywR4yv6kSUjpdkAqaWvR5KB6qaD6rhWNnZalk/1sxMmTWO/CpGGOWIgORDU/kLIHShjE1pRJ
        +d+Dv8fcPfcQaclpHjy+uqg8+kS79FIotz94dvc+bIdNCHkjlai8juLCJzysf7rGl1I6ikp5
        0nMXvTvvakibX2doCbdQ03ac74tgJ1QsDjCPd1vH5OvLKsVfdDm/bg==
    """,
    "database/schema.py": """
        eNqVVE2L2zAQvRv8H4RzUcAY2oUeCoaSbguFtpfdWylCtseKWH14JXmp/331YTnZkJSuyEGe
        mffeePwmOzQaLVGvhYDeca0s4nLSxiFFJQxungSUxc7/ctw+Cyr6I8gFUYssDanIcUo08Mc1
        A/SCGur4C2ToWYh01MI1qDZyUwJrfUeSPoF53cNRW7dGJDg6UEdR63tpfvine/+E92v64GV8
        6lIZZ1ibLxnwkEQD3Zl85MsRn1urMJ2dHsVsj+1XKizUKAR6LSV3KbLSlkVZ3JxfWcQhNKGx
        /Iah7zrLhBLfv7Xoywso910zHPL7j2WB/CHE0U5A+GCE+OYqCFVEaFalAj6k6XzWYpYK+9s3
        5YCBqdFkuKRmIU+wtI9m9ppqFiLQbf0HhsTolgluMl3FOXtZf+Ds3xBtOOPqEvbgDFcM333Y
        34BN7y4hj96Ft4rfv6X47g3Fo6DM/v+MEuhT/LjeiUc9pMgAI3qewSy4FzZ/53AMuNmobIzm
        VBO4ooGD/bvk+tMK4+r+UNXoV5UNVP3enLmLalxxR4YOg/LTh/anVtFfu6jKhO6oyP5fUdFZ
        I0oAxC0KmA0SXZNSbdzXhoEXWJsjvVYq/eFsqxpOfi+fHjmbDeCOq6FNRPtcdX0Pz9cuLeLZ
        Zp6LrDPMg8J5JnUm3i4kztdj/wLaMKMH
    """,
    "database/__init__.py": """
        eNpLK8rPVdBLSixOVcjMLcgvKlHIzMssiU9J4uUCAIlsCWk=
    """,
}
t1utils.resources_check(script_path, resources)

import os
import csv
from database import init_db
from database.schema import EventLog

GLOBALS = globals()

DB_ROW = GLOBALS.get("DB_ROW", "")

db = init_db()
shots_path = os.path.expanduser(host.settings("system_wide_options")["screenshots_folder"])
name_file = "last_events.csv"
csv_filename = os.path.join(shots_path, name_file)

with db.session() as session:
    events = session.query(EventLog).order_by(EventLog.id.desc()).limit(DB_ROW)

with open(csv_filename, 'w') as csvfile:
    fieldnames = ['id', 'event_type', 'ts', 'origin', 'p1', 'p2', 'p3', 'flags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for event in events:
        writer.writerow(
            {
        'id': event.id,
        'event_type': event.event_type,
        'ts': event.ts,
        'origin': event.origin,
        'p1': event.p1,
        'p2': event.p2,
        'p3': event.p3,
        'flags': event.flags
    }
        )

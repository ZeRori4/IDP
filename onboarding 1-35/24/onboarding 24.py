# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 24</title>
	<version>1.0</version>
</parameters>
'''
import host
import json
import os


screenshots_folder = host.settings("system_wide_options")["screenshots_folder"]


def fr_event(ev):
    ev.data = json.loads(ev.data)
    file_path = os.path.join(screenshots_folder, "last_fr_event.json")
    with open(file_path, "w") as json_file:
        json.dump(ev.data, json_file, ensure_ascii=False, indent=4)


host.activate_on_events("Face Recognized", "", fr_event)

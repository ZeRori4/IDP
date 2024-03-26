# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 23</title>
	<version>1.0</version>
</parameters>
'''
import host
import json
import os

screenshots_folder = host.settings("system_wide_options")["screenshots_folder"]


def lpr_event(event):
    dict_data_lpr_event = vars(event)
    for key, value in dict_data_lpr_event.items():
        if isinstance(value, long):
            dict_data_lpr_event[key] = int(value)

    dict_data_lpr_event['matched_embrecords_history'] = []
    dict_data_lpr_event['track_points'] = json.loads(
        dict_data_lpr_event['track_points']
    )

    file_path = os.path.join(screenshots_folder, "last_lpr_event.json")
    with open(file_path, "w") as json_file:
        json.dump(dict_data_lpr_event, json_file, ensure_ascii=False, indent=4)


host.activate_on_lpr_events(lpr_event)

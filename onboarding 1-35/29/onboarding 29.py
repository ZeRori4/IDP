# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 29</title>
	<version>1.0</version>
</parameters>
'''


import os
import xlsxwriter

import host


def save_data_to_xlsx(file_path, data_list):
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    headers = ['Name', 'Audio Codec', 'Resolution', 'FPS Limit']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    row_num = 1
    for item in data_list:
        worksheet.write(row_num, 0, item['name'])
        worksheet.write(row_num, 1, item['channel00_audio_codec'])
        worksheet.write(row_num, 2, item['channel00_resolution'])
        worksheet.write(row_num, 3, item['channel00_fps'])
        row_num += 1

    workbook.close()


def get_data_from_ip_device():
    device_info_list = []
    device_info = {}
    for sett in host.settings("ip_cameras").ls():
        if sett.type == "Grabber":
            if sett["grabber_enabled"]:
                device_info["name"] = sett["name"]
                device_info["channel00_audio_codec"] = sett["channel00_audio_codec"]
                device_info["channel00_resolution"] = sett["channel00_resolution"]
                device_info["channel00_fps"] = sett["channel00_fps"]
                device_info_list.append(device_info)
                device_info = {}
    return device_info_list


shots_path = os.path.expanduser(host.settings("system_wide_options")["screenshots_folder"])
name_file = "ip_cameras.xlsx"
file_path = os.path.join(shots_path, name_file)

device_data = get_data_from_ip_device()
save_data_to_xlsx(file_path, device_data)
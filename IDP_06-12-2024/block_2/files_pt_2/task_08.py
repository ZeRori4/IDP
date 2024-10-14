# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход данные (формат в Приложении 2), папку для сохранения отчёта и генерирует
отчет. Реализуйте отчет в формате xlsx по всем данным.
Заголовки для отчета: Дата и время, Имя сервера, Имя канала, Номер авто, Направление, Имя списка.
Приложение 2
Имя отчета: "entry_exit_report_<дата/время>."
Данные:
[
  {
    "number": "a678mp",
    "direction": "up", "list": "black",
    "channel_name": "Entry", "server_name": "MSK-1",
    "datetime": 1713071347
  },
  {
    "number": "a678mp",
    "direction": "down", "list": "black",
    "channel_name": "Exit", "server_name": "MSK-1",
    "datetime": 1713082147
  },
  {
    "number": "a123mp",
    "direction": "up", "list": "white",
    "channel_name": "Entry", "server_name": "MSK-2",
    "datetime": 1713067421
  },
  {
    "number": "a123mp",
    "direction": "down", "list": "white",
    "channel_name": "Exit", "server_name": "MSK-2",
    "datetime": 1713085421
  },
  {
    "number": "a777mp",
    "direction": "up", "list": "white",
    "channel_name": "Entry", "server_name": "MSK-1",
    "datetime": 1713179202
  }
]
"""

import os
import xlsxwriter
from datetime import datetime


def generate_report(data, path):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = u"entry_exit_report_{}.xlsx".format(current_time)
    report_path = os.path.join(path, report_name)

    workbook = xlsxwriter.Workbook(report_path)
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, u"Дата и время")
    worksheet.write(0, 1, u"Имя сервера")
    worksheet.write(0, 2, u"Имя канала")
    worksheet.write(0, 3, u"Номер авто")
    worksheet.write(0, 4, u"Направление")
    worksheet.write(0, 5, u"Имя списка")

    row = 1
    for row_data in data:

        datetime_str = datetime.fromtimestamp(row_data["datetime"]).strftime("%Y-%m-%d %H:%M:%S")
        worksheet.write(row, 0, datetime_str)
        worksheet.write(row, 1, row_data["server_name"])
        worksheet.write(row, 2, row_data["channel_name"])
        worksheet.write(row, 3, row_data["number"])
        worksheet.write(row, 4, row_data["direction"])
        worksheet.write(row, 5, row_data["list"])
        row += 1

    workbook.close()


data_application = [
    {
        "number": "a678mp",
        "direction": "up", "list": "black",
        "channel_name": "Entry", "server_name": "MSK-1",
        "datetime": 1713071347
    },
    {
        "number": "a678mp",
        "direction": "down", "list": "black",
        "channel_name": "Exit", "server_name": "MSK-1",
        "datetime": 1713082147
    },
    {
        "number": "a123mp",
        "direction": "up", "list": "white",
        "channel_name": "Entry", "server_name": "MSK-2",
        "datetime": 1713067421
    },
    {
        "number": "a123mp",
        "direction": "down", "list": "white",
        "channel_name": "Exit", "server_name": "MSK-2",
        "datetime": 1713085421
    },
    {
        "number": "a777mp",
        "direction": "up", "list": "white",
        "channel_name": "Entry", "server_name": "MSK-1",
        "datetime": 1713179202
    }
]

folder_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_2"
generate_report(data_application, folder_path)

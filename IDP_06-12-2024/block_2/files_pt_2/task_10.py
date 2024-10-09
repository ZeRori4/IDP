# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход данные (формат в Приложении 2), папку для сохранения отчёта и генерирует
отчет. Реализуйте отчет в формате xlsx. Закрасьте проезды в соответствии со списками
(белый список - зеленым, черный список - красным).
Заголовки для отчета:
Дата и время, Имя сервера, Имя канала, Номер авто, Направление, Имя списка, Время на парковке (в формате ЧЧ:ММ:СС).
Если авто не выехало, поле Время на парковке оставить пустым. Добавить последней строкой "Всего проездов:" с подсчетом
общего числа проездов.
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
'''


import os
import xlsxwriter
from datetime import datetime


def generate_report(data, path):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = u"entry_exit_report_{}.xlsx".format(current_time)
    report_path = os.path.join(path, report_name)

    workbook = xlsxwriter.Workbook(report_path)
    worksheet = workbook.add_worksheet()

    green_cell = workbook.add_format({'bg_color': '#00FF00'})
    red_cell = workbook.add_format({'bg_color': '#FF0000'})

    worksheet.write(0, 0, u"Дата и время")
    worksheet.write(0, 1, u"Имя сервера")
    worksheet.write(0, 2, u"Имя канала")
    worksheet.write(0, 3, u"Номер авто")
    worksheet.write(0, 4, u"Направление")
    worksheet.write(0, 5, u"Имя списка")
    worksheet.write(0, 6, u"Время на парковке")

    row = 1
    total_entries = 0
    entry_times = {}
    for row_data in data:
        cell_format = green_cell if row_data["list"] == "white" else red_cell

        time_stamp = datetime.fromtimestamp(row_data["datetime"])
        parking_time = ""
        if row_data["direction"] == "up":
            entry_times[row_data["number"]] = time_stamp
        elif row_data["direction"] == "down":
            entry_time = entry_times.pop(row_data["number"], None)
            if entry_time:
                parking_time = time_stamp - entry_time

        worksheet.write(row, 0, time_stamp.strftime('%Y-%m-%d %H:%M:%S'), cell_format)
        worksheet.write(row, 1, row_data["server_name"], cell_format)
        worksheet.write(row, 2, row_data["channel_name"], cell_format)
        worksheet.write(row, 3, row_data["number"], cell_format)
        worksheet.write(row, 4, row_data["direction"], cell_format)
        worksheet.write(row, 5, row_data["list"], cell_format)
        worksheet.write(row, 6, str(parking_time), cell_format)
        row += 1
        total_entries += 1

    worksheet.write(row, 0, u"Всего проездов:", workbook.add_format({'bold': True}))
    worksheet.write(row, 1, total_entries, workbook.add_format({'bold': True}))

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

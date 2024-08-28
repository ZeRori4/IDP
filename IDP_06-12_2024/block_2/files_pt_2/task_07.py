# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход данные (формат в Приложении 2), папку для сохранения отчёта и генерирует
отчет. Реализуйте отчет в формате csv по всем данным.
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


import csv
import os
from datetime import datetime


def generate_report(data, path):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = "entry_exit_report_{}.csv".format(current_time)
    report_path = os.path.join(path, report_filename)

    headers = ["Дата и время", "Имя сервера", "Имя канала", "Номер авто", "Направление", "Имя списка"]

    with open(report_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            datetime_str = datetime.fromtimestamp(row["datetime"]).strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([
                datetime_str,
                row["server_name"],
                row["channel_name"],
                row["number"],
                row["direction"],
                row["list"]
            ])


data_application = [
    {
        "number": "a678mp",
        "direction": "up",
        "list": "black",
        "channel_name": "Entry",
        "server_name": "MSK-1",
        "datetime": 1713071347
    },
    {
        "number": "a678mp",
        "direction": "down",
        "list": "black",
        "channel_name": "Exit",
        "server_name": "MSK-1",
        "datetime": 1713082147
    },
    {
        "number": "a123mp",
        "direction": "up",
        "list": "white",
        "channel_name": "Entry",
        "server_name": "MSK-2",
        "datetime": 1713067421
    },
    {
        "number": "a123mp",
        "direction": "down",
        "list": "white",
        "channel_name": "Exit",
        "server_name": "MSK-2",
        "datetime": 1713085421
    },
    {
        "number": "a777mp",
        "direction": "up",
        "list": "white",
        "channel_name": "Entry",
        "server_name": "MSK-1",
        "datetime": 1713179202
    }
]

folder_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_2"
generate_report(data_application, folder_path)

import os
import host
folder = host.settings("system_wide_options")["screenshots_folder"]
content = os.listdir(folder)
# нужно содержимое script_path / имелось в виду папка скриншотов где есть логи скриптов?
file_list = '\n'.join(content)
alert(file_list)

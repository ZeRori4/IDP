import os
content = os.listdir(script_path)
file_list = '\n'.join(content)
alert(file_list)

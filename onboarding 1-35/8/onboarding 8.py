import os
import host
content = os.listdir("C:/DSSL/")
file_list = '\n'.join(content)
host.alert(file_list)

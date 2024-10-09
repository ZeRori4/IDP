# -*- coding: utf-8 -*-

'''
Создайте функцию, которая принимает на вход путь до директории, создает в рабочем каталоге файл
file_sizes_in_<имя каталога>.txt и записывает в него информацию по анализируемой директории в формате
'Относительный путь до файла - размер файла в байтах'. Нужно пройти по всем файлам анализируемой и всех вложенных
директорий. В случае вложенных файлов путь указывается относительно анализируемой директории. Пример результата:
/path/to/directory/abc -> file_sizes_in_abc.txt
1.txt - 12
2.txt - 34
sub_folder_1/3.txt - 500
sub_folder_2/4.txt - 345
'''


import os


def get_file_sizes_to_dir(dir_path):
    output_file = 'file_sizes_in_{}.txt'.format(os.path.basename(os.path.normpath(dir_path)))
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_size = os.path.getsize(file_path)
                relative_path = os.path.relpath(file_path, dir_path)
                f.write('{} - {}\n'.format(relative_path, file_size))


get_file_sizes_to_dir('C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1')

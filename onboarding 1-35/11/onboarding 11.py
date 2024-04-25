# -*- coding: utf-8 -*-
# Напишите здесь описание скрипта
"""
<parameters>
	<title>onboarding 11</title>
	<version>1.0</version>
	<parameter>
        <type>integer</type>
        <name>Параметр 1</name>
        <id>param_1</id>
        <value>100</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Параметр 2</name>
        <id>param_2</id>
        <value>100</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>user_function</id>
        <name>Функция</name>
        <value>+</value>
        <string_list>/,*,+,-</string_list>
    </parameter>
<resources>
        <resource>func.py</resource>
    </resources>

</parameters>
"""

resources = {
	"func.py": '''
		eAGN0MsKgCAQBdB90D8MrXoStQza9hsRNUYgBj7+PycJC0IcF6Lcexaz8kUpmIxYhzRJE7Cz
		IQNmP3KFnNVGoZzpqY9T1LDIfe7c1Re2QgWag8EnCeMIWZW9EjQStZHCIVA5xSeQ/ypNUGki
		lTKolJFKG1TaR6Hje/d68+ICrgVhSg==
	'''
}
t1utils.resources_check(script_path, resources)

from func import сalculator

result = сalculator.calculate(user_function, param_1, param_2)
raise Exception(result)

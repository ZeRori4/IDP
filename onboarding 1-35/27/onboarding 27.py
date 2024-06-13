
'''
<parameters>
	<title>onboarding 27</title>
	<version>1.0</version>
</parameters>
'''
import host


def get_local_templates():
    templates_list = []
    for tpl in host.settings("templates").ls():
        tpl_string = 'name: {}, guid: {}'.format(tpl.name, tpl.guid)
        templates_list.append(tpl_string)
        str_tpl = '\n'.join(templates_list)
    return host.alert(str_tpl)


get_local_templates()

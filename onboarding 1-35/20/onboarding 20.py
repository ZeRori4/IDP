# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 20</title>
	<version>1.0</version>
    <parameter>
        <type>string_from_list</type>
        <id>object_detection</id>
        <name>object of detection</name>
        <value>person</value>
        <string_list>person,vehicle,animal</string_list>
    </parameter>
</parameters>

'''

import host


def counting_objects_in_zone(ev):
    for zone in ev.zones:
        if zone.objects_inside[0].class_id == object_detection:
            host.message("Зона: %s, объект: %s = %s" % (
                zone.zone_name,
                zone.objects_inside[0].class_id,
                len(zone.objects_inside)
            ))


host.activate_on_deep_detection_events(counting_objects_in_zone)

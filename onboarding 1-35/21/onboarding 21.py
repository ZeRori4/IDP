# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 21</title>
	<version>1.0</version>
</parameters>
'''
import host


def count_hardhat(event):
    dict_count = {
        "with_hardhat": 0,
        "without_hardhat": 0
    }
    list_with_hardhat = []
    list_without_hardhat = []

    if event.server_guid == host.settings("").guid:
        for zone in event.zones:
            if zone.zone_type == 1:
                continue
            for obj_inside in zone.objects_inside:
                if hasattr(obj_inside, "specifications_name"):
                    specifications_name = obj_inside.specifications_name
                    if specifications_name[0] == "with_hardhat":
                        list_with_hardhat.append(specifications_name[0])
                        dict_count["with_hardhat"] = len(list_with_hardhat)
                    else:
                        list_without_hardhat.append(specifications_name[0])
                        dict_count["without_hardhat"] = len(
                            list_without_hardhat)
            host.alert(dict_count)


host.activate_on_deep_detection_events(count_hardhat)

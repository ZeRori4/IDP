import os

import host

from exthttp.auth import User
from exthttp.constant import SCRIPT_PATH

script = host.stats().parent()


def _get_icon(icon_path):
    if icon_path:
        if not os.path.isfile(icon_path):
            icon_path = os.path.join(SCRIPT_PATH, icon_path)

        if os.path.isfile(icon_path):
            with open(icon_path, "rb") as f:
                return f.read()
    return ""


def create_module(guid, name=None, lang=None, icon_path=None, check_rights=None, allow_multiple=False, idx=0):
    if allow_multiple is True:
        name = script["name"]
    else:
        name = name or script["name"]
    lang = lang or script["language"] or host.settings("system_wide_options")["i18n_language"]

    if idx:
        guid_ = "%s%s" % (guid, idx)
    else:
        guid_ = guid
    name_ = name
    tmod = host.TrassirModule(guid_)
    tmod.set_name(name_)
    tmod.set_lang(lang)

    tmod.set_icon_data(_get_icon(icon_path))

    def _mod_check_rights(userid, username):
        return User(userid, cog_guid=guid_).has_view_rights

    tmod.set_check_rights(check_rights or _mod_check_rights)
    tmod.set_url(guid_)

    try:
        host.trassir_module_add(tmod)
    except RuntimeError as err:
        if allow_multiple is True:
            return create_module(
                guid,
                name=name,
                lang=lang,
                icon_path=icon_path,
                check_rights=check_rights,
                allow_multiple=allow_multiple,
                idx=idx+1
            )
        raise err
    host.cog_create_or_update(guid_, name, None)

    tmod.name = name_
    tmod.guid = guid_
    tmod.lang = lang
    tmod.allow_multiple = allow_multiple

    return tmod

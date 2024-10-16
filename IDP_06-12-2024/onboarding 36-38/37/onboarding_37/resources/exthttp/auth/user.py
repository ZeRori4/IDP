import host

from exthttp.utils import logger

USER_SETTINGS = host.settings("users")


class User(object):
    name = "Anonymous"
    guid = ""
    base_rights = rights = 0
    settings = None

    def __init__(self, guid, cog_guid=None):
        self.guid = guid
        self.settings = USER_SETTINGS.cd(guid)
        if self.settings:
            self.name = self.settings.name
            self.base_rights = self.settings["base_rights"]

            if cog_guid:
                self.rights = host.cog_rights(guid, cog_guid)
            else:
                self.rights = self.base_rights

        logger.debug(self)

    def __repr__(self):
        return "<User({self.name!r}, {self.guid!r}, {self.rights!r})>".format(self=self)

    def __getitem__(self, item):
        if self.settings:
            logger.debug("__getitem__ settings(%r)[%r]", self.settings.path, item)
            return self.settings[item]
        else:
            logger.warning("No user settings: %s", self)

    def __setitem__(self, key, value):
        if self.settings:
            logger.debug("__getitem__ settings(%r)[%r] = %r", self.settings.path, key, value)
            self.settings[key] = value
        else:
            logger.warning("No user settings: %s", self)

    @property
    def is_superuser(self):
        return self.guid == "Admin"

    @property
    def has_view_rights(self):
        return bool(self.rights & host.RIGHTS_VIEW)

    @property
    def has_modify_rights(self):
        return bool(self.rights & host.RIGHTS_MODIFY)

    @property
    def has_setup_rights(self):
        return bool(self.rights & host.RIGHTS_SETUP)

    @property
    def icon(self):
        if self.settings:
            try:
                return self.settings["icon"].split("/")[-1]
            except (KeyError, IndexError):
                pass

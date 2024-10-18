# -*- coding: utf-8 -*-

import os
import host

SERVER_NAME = host.settings("").name or "Client"
SERVER_GUID = host.settings("").guid
SCRIPT_NAME = host.stats().parent().name
SCRIPT_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
LANGUAGE_ID = host.stats().parent()["language"] or host.settings("system_wide_options")["i18n_language"]

# -*- coding: utf-8 -*-
'''
<parameters>
    
    <title>onboarding_37</title>
    <version>1.0.2</version>

    <resources>
        <resource>helpers.py</resource>
        <resource>exthttp/constant.py</resource>
        <resource>exthttp/utils.py</resource>
        <resource>exthttp/__init__.py</resource>
        <resource>exthttp/__version__.py</resource>
        <resource>exthttp/auth/login.py</resource>
        <resource>exthttp/auth/user.py</resource>
        <resource>exthttp/auth/__init__.py</resource>
        <resource>exthttp/core/app.py</resource>
        <resource>exthttp/core/handlers.py</resource>
        <resource>exthttp/core/module.py</resource>
        <resource>exthttp/core/__init__.py</resource>
        <resource>exthttp/http/request.py</resource>
        <resource>exthttp/http/response.py</resource>
        <resource>exthttp/http/__init__.py</resource>
        <resource>static/img/trassir.png</resource>
        <resource>templates/index.html</resource>
    </resources>

</parameters>
'''


import json

import host
from exthttp import create_app, BaseHandler
from exthttp import http

APP_NAME = host.stats().parent().name
app = create_app("onboarding_37")
app.create_module(name=APP_NAME, icon_path="static/img/trassir.png")


def get_info_scripts():
    list_info_scr = []
    for sett in host.settings("scripts").ls():
        stats = host.stats()
        script = stats.parent()
        if sett.type == "Script":
            dict_info = {
                "name": sett["name"].decode('utf-8'),
                "guid": script.guid,
                "already_running": sett["enable"],
                "last_error": stats["last_error"],
            }
            list_info_scr.append(dict_info)
    return list_info_scr

@app.route("index")
class IndexHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        return http.HttpResponse("Hello world")


@app.route("scripts")  # https://localhost:8080/s/onboarding_37/scripts
class ScreenshotHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        return http.JsonResponse(json.loads(json.dumps({"message": get_info_scripts()})))

# -*- coding: utf-8 -*-
'''
<parameters>
    
    <title>onboarding_37</title>
    <version>1.0.3</version>

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

import host
from exthttp import create_app, BaseHandler
from exthttp import http

APP_NAME = host.stats().parent().name
app = create_app("onboarding_38")
app.create_module(name=APP_NAME, icon_path="static/img/trassir.png")
app.need_auth = False


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
                "last_error": sett.cd("stats")["last_error"],
            }
            list_info_scr.append(dict_info)
    return list_info_scr


@app.route("index")
class IndexHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        return http.HttpResponse("Hello world")


@app.route("scripts")
class ScreenshotHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        if request.user.has_view_rights:
            return http.JsonResponse({"message": get_info_scripts()})
        return http.JsonResponse({"error": "Forbidden"}, status=403)
    get.need_auth = True

# https://localhost:8080/login?username=ptz&password=ptz  - получаем sid
# https://localhost:8080/s/onboarding_38/scripts?sid=I9dsFPQM  - доступ к данным
# -*- coding: utf-8 -*-
'''
<parameters>
    
    <title>onboarding_37</title>
    <version>1.0.1</version>

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


import os
from datetime import datetime

import host
from exthttp import create_app, BaseHandler
from exthttp import http

SCREENSHOT_PATH = host.settings("system_wide_options")["screenshots_folder"]
SERVER_GUID = host.settings("").guid

APP_NAME = host.stats().parent().name
app = create_app("onboarding_37")
app.create_module(name=APP_NAME, icon_path="static/img/trassir.png")


@app.route("index")
class IndexHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        return http.HttpResponse("Hello world")


@app.route("screenshot")  # https://localhost:8080/s/onboarding_36/screenshot?channel_guid=A02zwoe0
class ScreenshotHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        channel_guid = request.GET.get("channel_guid")
        try:
            obj = host.object(channel_guid)
            if not hasattr(obj, "screenshot_v2"):
                return http.JsonResponse({"message": "Screenshot with {} not found".format(channel_guid)})
            dt = datetime.now()
            screenshot_time = dt.strftime("%Y%m%d_%H%M%S")
            screenshot_name = "{}_{}_{}.jpg".format(channel_guid, host.random_guid(), screenshot_time)
            screenshot_path = os.path.join(SCREENSHOT_PATH, screenshot_name)
            host.screenshot_v2(
                "{}_{}".format(channel_guid, SERVER_GUID), screenshot_name, SCREENSHOT_PATH, screenshot_time
            )
            with open(screenshot_path, "rb") as image_file:
                image_data = image_file.read()
                return http.HttpResponse(data=image_data, headers={"Content-Type": "image/jpeg"})
        except Exception as err:
            return http.JsonResponse({"message": "Error when creating a screenshot, error: {}".format(err)})

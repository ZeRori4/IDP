import re
import json
import requests

import host

from exthttp.core.handlers import BaseHandler
from exthttp.http import HttpResponseRedirect, JsonResponse
from exthttp.constant import SERVER_GUID
from exthttp.utils import logger

LOGIN_URL = "https://localhost:{sdk_port}/login".format(
    sdk_port=host.settings("webserver")["http_port"]
)
LOGIN_RES_REGEXP = re.compile(r"\/\*.*\*\/", flags=re.S)


class LoginHandler(BaseHandler):

    def __init__(self, basename):
        self.basename = basename
        super(LoginHandler, self).__init__()

    def post(self, request, *args, **kwargs):
        logger.debug("request.POST (%s) = %s", type(request.POST).__name__, request.POST)
        username = request.POST.get("username")
        if not username:
            data = {"success": 0, "error_code": "Empty username"}
        else:
            if SERVER_GUID == "client":
                data = {"success": 0, "error_code": "Authentication is not available for Trassir Client"}
            else:
                response = requests.post(
                    LOGIN_URL,
                    data={"username": username, "password": request.POST.get("password", "")},
                    verify=False,
                )
                if response.status_code == 200:
                    try:
                        data = json.loads(LOGIN_RES_REGEXP.sub("", response.text))
                    except ValueError:
                        data = {"success": 0, "error_code": response.text}

                    if data["success"]:
                        return JsonResponse(data)
                else:
                    data = {"success": 0, "error_code": "[{r.status_code}] {r.text}".format(r=response)}

        return JsonResponse(data, status=400)

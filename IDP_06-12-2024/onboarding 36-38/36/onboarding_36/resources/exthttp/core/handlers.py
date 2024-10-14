import os
import traceback

from mako.lookup import TemplateLookup
from mako.exceptions import html_error_template

from exthttp.http import (
    HttpResponse,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    HttpResponseUnknownError,
    HttpResponseServerError,
    JsonResponse,
)
from exthttp.constant import SCRIPT_NAME, SERVER_NAME
from exthttp.utils import tr, logger

BASE_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))
directories = [BASE_PATH]

templates_path = os.path.join(BASE_PATH, "templates")
if os.path.exists(templates_path):
    directories.append(templates_path)

lookup = TemplateLookup(
    directories=directories,
    default_filters=["decode.utf8"],
    input_encoding="utf-8",
    output_encoding="utf-8",
    encoding_errors="replace",
)

is_dev = os.getenv("EXTHTTP_ENV", "prod") == "dev"

_redirect_html = """<!DOCTYPE html><html><head>
<script>
    // This script needs for right relative link to static folder
    String.prototype.endsWith = function (suffix) {{
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    }};
    const href = window.location.href.split("?")[0];
    if (href.endsWith('{basename}')) {{
        if (!href.endsWith('{basename}/{basename}')) {{
            window.location.replace(href + "/index{sid}");
        }}
    }} else if (href.endsWith('{basename}/')) {{
        window.location.replace(href + "index{sid}");
    }}
</script>
</head>
<body><p>Redirecting...</p></body></html>"""

_index_html = """<!doctype html><head><meta charset='utf-8'></head><body>
Please, add <span style="background-color: #fff0f0">&quot;index&quot;</span> handler to your app. For example:<br>
<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
<pre style="margin: 0; line-height: 125%">
<span style="color: #555555; font-weight: bold">@app.route</span>(<span style="background-color: #fff0f0">&quot;index&quot;</span>)
<span style="color: #008800; font-weight: bold">class</span> <span style="color: #BB0066; font-weight: bold">IndexHandler</span>(BaseHandler):
    <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get</span>(<span style="color: #007020">self</span>, request, <span style="color: #333333">*</span>args, <span style="color: #333333">**</span>kwargs):
        <span style="color: #008800; font-weight: bold">return</span> http<span style="color: #333333">.</span>HttpResponse(<span style="background-color: #fff0f0">&quot;Hello world&quot;</span>)
</pre>
</div></body></html>"""


class BaseHandler(object):
    __template__ = None
    __mako_template__ = None

    title = None
    rights = ""

    def __init__(self):
        self.app = None
        self.url = ""
        self.menu = []
        self.__load_template()
        self.request = None

    def __load_template(self):
        if self.__template__:
            self.__mako_template__ = lookup.get_template(self.__template__)

    def get_sid(self):
        sid = ""
        if self.request:
            sid = self.request.GET.get("sid", "")
        return sid

    def _add_defaults_context(self, context):
        __default_context = {
            "app": self.app,
            "title": SCRIPT_NAME,
            "server_name": SERVER_NAME,
            "request": self.request,
            "sid": self.get_sid(),
        }

        __default_context.update(context)

        return __default_context

    def _add_menu(self, context):
        context["menu"] = []
        if self.request:
            sid = self.get_sid()
            for item in self.menu:
                item = dict(item)
                if item.get("rights"):
                    if getattr(self.request.user, item["rights"], False) is False:
                        continue
                item["is_active"] = self.request.path == item["link"]
                if not getattr(self.request, "is_trassir", False) and sid:
                    item["link"] += "?sid=%s" % sid
                context["menu"].append(item)

    def render(self, **context):
        if is_dev:
            self.__load_template()

        if self.__mako_template__:
            context = self._add_defaults_context(context)
            self._add_menu(context)
            try:
                return HttpResponse(self.__mako_template__.render(**context))
            except:
                return HttpResponseServerError(html_error_template().render())

    def get(self, *args, **kwargs):
        return HttpResponseNotAllowed("GET")

    def post(self, *args, **kwargs):
        return HttpResponseNotAllowed("POST")

    def delete(self, *args, **kwargs):
        return HttpResponseNotAllowed("DELETE")


class PageNotFoundHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound("Sorry, %s not found" % request.url)


class IndexHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        return HttpResponse(_index_html)


class RedirectHandler(BaseHandler):
    def __init__(self, basename):
        super(RedirectHandler, self).__init__()
        self.basename = basename
        self.page_not_found_handler = PageNotFoundHandler()

    def get(self, request, *args, **kwargs):
        sid = request.GET.get("sid", "")
        if sid:
            sid = "?sid=%s" % sid

        if not request.path or request.path == self.basename:
            location = "{}/index".format(self.basename)
            logger.info("Path: %s, redirecting to %s", request.path, location)
            return HttpResponse(_redirect_html.format(basename=self.basename, sid=sid))

        elif request.path.endswith("/"):
            location = "index"
            logger.info("Path: %s, redirecting to %s", request.path, location)
            return HttpResponse(_redirect_html.format(basename=self.basename, sid=sid))
        else:
            logger.info("Redirect to 404")

            try:
                context = self._add_defaults_context({})
                self._add_menu(context)
                response = HttpResponse(self.page_not_found_handler.get(request, *args, **kwargs))
            except:
                response = HttpResponseServerError(html_error_template().render())

            return response


def error_handler(request, error, *args, **kwargs):
    return HttpResponseUnknownError("{}\n {}".format(request, traceback.format_exc()))

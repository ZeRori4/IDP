import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.1"
logger.debug("%s version: %s", __name__, __version__)

server_guid = host.settings("").guid

gui = host.object("operatorgui_%s" % server_guid)
try:
    logger.info("gui %s loaded success", gui.name)
except EnvironmentError:
    gui = None
    logger.warning("gui object not found")

templates_settings = host.settings("templates")
templates = host.object("%sT" % server_guid)


class TemplateError(Exception):
    pass


class CreateTemplateError(TemplateError):
    pass


class TemplateNotFound(TemplateError):
    pass


class GUITemplate(object):
    def __init__(self, settings):
        if settings.type != "Template":
            raise TypeError("Expected Template settings, got %s" % settings.type)
        self.settings = settings
        self.obj = None
        self.__load_object()

    def __repr__(self):
        return "<GUITemplate(settings({s.path}))>".format(s=self.settings)

    def __load_object(self, tries=3):
        self.obj = host.object(self.settings.guid)
        try:
            logger.info("Loaded template object %s", self.obj.name)
        except EnvironmentError:
            self.obj = None
            if tries:
                logger.warning(
                    "Template object not found: %s (%s): %s", self.settings.name, self.settings.guid, tries
                )
                host.timeout(500, lambda: self.__load_object(tries-1))
            else:
                logger.error(
                    "Template object not found: %s (%s)", self.settings.name, self.settings.guid
                )

    @classmethod
    def create_template(cls, name, content=""):
        """Create new template

        Args:
            name (str): Template name
            content (str): Template default content

        Returns:
            GUITemplate: Template object

        Raises:
            CreateTemplateError: if can't find template after creating
        """
        templates.create_template(name, content)
        try:
            template = cls.find_template_by_name(name)
        except TemplateNotFound:
            raise CreateTemplateError("Failed to create template {}".format(name))
        return template

    @classmethod
    def find_template_by_name(cls, name):
        """Find template guid by name

        Args:
            name (str) : Template name

        Returns:
            GUITemplate: Template object

        Raises:
            TemplateNotFound: if can't find template
        """
        for settings in templates_settings.ls():
            if settings.type == "Template" and settings.name == name:
                return cls(settings)

        raise TemplateNotFound(name)

    @property
    def guid(self):
        return self.settings.guid

    @property
    def name(self):
        return self.settings.name

    @name.setter
    def name(self, value):
        value = str(value)
        logger.debug("Set new name: %s", value)
        self.settings["name"] = value

    @property
    def content(self):
        return self.settings["content"]

    @content.setter
    def content(self, value):
        value = str(value)
        logger.debug("Set new content: %s", value)
        self.settings["content"] = value

    @property
    def shared(self):
        if self.obj:
            return self.obj.state("shared") == "Shared to Cloud"

    def channels_content(self, *channels):
        self.content = "gui7(DEWARP_SETTINGS,,,-1,%s)" % ",".join(
            str(ch) for ch in channels
        )

    def show(self, monitor=1):
        if gui:
            logger.debug("Show template %s", self.name)
            gui.show(self.guid, monitor)
        else:
            logger.warning("GUI object not loaded")

    def delete(self):
        if self.obj:
            logger.info("Remove template (%s")
            self.obj.delete_template()


def create(name, content=""):
    """Create new template

    Args:
        name (str): Template name
        content (str): Template default content

    Returns:
        GUITemplate: Template object

    Raises:
        CreateTemplateError: if can't find template after creating
    """
    return GUITemplate.create_template(name, content=content)


def get(name):
    """Find template by name

    Args:
        name (str) : Template name

    Returns:
        GUITemplate: Template object

    Raises:
        TemplateNotFound: if can't find template
    """
    return GUITemplate.find_template_by_name(name)


def get_or_create(name, content=""):
    """Create new template

    Args:
        name (str): Template name
        content (str): Template default content

    Returns:
        GUITemplate: Template object

    Raises:
        CreateTemplateError: if can't find template after creating
    """
    try:
        return get(name)
    except TemplateNotFound:
        return create(name, content=content)

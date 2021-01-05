from ._version import __version__
from .handlers import setup_handlers


def _jupyter_server_extension_paths():
    return [{"module": "notebook_static_image_handler"}]


def load_jupyter_server_extension(lab_app):
    setup_handlers(lab_app.web_app)

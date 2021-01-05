import os

from notebook.utils import url_path_join
from tornado.web import StaticFileHandler
import logging

logger = logging.getLogger(__name__)

def setup_handlers(web_app):
    base_url = web_app.settings["base_url"]

    target_path = os.getenv(
        "NOTEBOOK_STATIC_IMAGE_HANDLER_REPLACE_RULE",
        "static/base/images/(.*)",
    )
    target_url = url_path_join(base_url, target_path)

    replaced_dir = os.getenv(
        "NOTEBOOK_STATIC_IMAGE_HANDLER_TARGET_DIR",
        "/static/images",
    )
    logger.info("[NotebookApp: notebook_static_image_hanlder] Replace %s to %s" % (target_url, replaced_dir))

    handlers = [(target_url, StaticFileHandler, {"path": replaced_dir})]
    web_app.add_handlers(".*$", handlers)
    
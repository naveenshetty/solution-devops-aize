from flask import Flask
from .routes import blueprint
from .config import Config
import logging
def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.config.from_object(Config)
    # Set up logging
    logging_level = app.config.get('LOGGING_LEVEL', 'INFO').upper()
    logging.basicConfig(level=logging_level)
    logger = logging.getLogger(__name__)
    logger.info("Application starting with logging level: %s", logging_level)

    return app

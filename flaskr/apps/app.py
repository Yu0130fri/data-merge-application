from flask import Flask

from .config import config


def create_app(config_key: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    from flaskr.apps.data_merge_app import views

    app.register_blueprint(views.data_merge_app, url_prefix="")

    return app

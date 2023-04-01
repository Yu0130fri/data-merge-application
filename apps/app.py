from flask import Flask

from .config import config


def create_app(config_key: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    from apps.data_merge_app import views

    app.register_blueprint(views.data_merge_app, url_prefix="")

    from apps.data_visualization import views as visualize_view

    app.register_blueprint(
        visualize_view.data_visualization_app, url_prefix="/data_visualization"
    )

    return app

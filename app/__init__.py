from flask import Flask

from instance.config import APP_CONFIG


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[config_name])

    from app.api.v1 import VERSION_1 as v1
    app.register_blueprint(v1)

    return app

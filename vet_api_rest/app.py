from flask import Flask
from vet_api_rest import api
from vet_api_rest import auth
from vet_api_rest import manage
from vet_api_rest.extensions import db
from vet_api_rest.extensions import jwt


def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("vet_api_rest")
    app.config.from_object("vet_api_rest.config")

    app.config['MYSQL_DATABASE_USER'] = "root"
    app.config['MYSQL_DATABASE_PASSWORD'] = "tryhard.python"
    app.config['MYSQL_DATABASE_DB'] = "vet_petshop_db"
    app.config['MYSQL_DATABASE_HOST'] = "localhost"

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)
    configure_cli(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """Configure flask extensions"""
    db.init_app(app)
    jwt.init_app(app)


def configure_cli(app):
    """Configure Flask 2.0's cli for easy entity management"""
    app.cli.add_command(manage.init)


def register_blueprints(app):
    """Register all blueprints for application"""
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)

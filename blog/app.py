from flask import Flask, render_template
from flask_migrate import Migrate

from blog import commands


def create_app() -> Flask:
    from blog.models.database import db
    from blog.auth.views import login_manager

    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_blueprints(app)
    register_commands(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    return app


def register_blueprints(app: Flask):
    from blog.user.views import users_app
    from blog.article.views import articles_app
    from blog.homepage.views import homepage
    from blog.auth.views import auth_app

    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(homepage, url_prefix="/")
    app.register_blueprint(auth_app, url_prefix="/auth")


def register_commands(app: Flask):
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.init_db)

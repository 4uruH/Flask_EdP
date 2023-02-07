from flask import Flask

from blog.commands import create_admin, create_tags
from blog.models import User
from blog.security import flask_bcrypt
from blog.extensions import db, login_manager, migrate, csrf, admin


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    flask_bcrypt.init_app(app)
    register_blueprints(app)
    register_commands(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    from blog.user.views import users_app
    from blog.article.views import articles_app
    from blog.homepage.views import homepage
    from blog.auth.views import auth_app
    from blog.author.views import authors_app
    from blog import admin

    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(homepage, url_prefix="/")
    app.register_blueprint(auth_app, url_prefix="/auth")
    app.register_blueprint(authors_app, url_prefix="/authors")

    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(create_admin)
    app.cli.add_command(create_tags)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth_app.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

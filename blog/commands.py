import click

from blog.models.database import db


@click.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User()
    james = User()
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User
    with app.app_context():
        db.create_all(app=app)


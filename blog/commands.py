import os

import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


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


@click.command('create-admin')
def create_admin():
    from blog.models.user import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(username="admin1", is_staff=True, email='name1@example.com', password=('test123'))
        )
        db.session.commit()

    print("admin created")





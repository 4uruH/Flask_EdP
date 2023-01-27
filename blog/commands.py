
import click

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
            User(username="admin1123", is_staff=True, email='name1123@example.com', password=('test123'))
        )
        db.session.commit()

    print("admin created")


@click.command('create-tags')
def create_tags():
    from blog.models import Tag
    from wsgi import app
    """
    Run in your terminal:
    ➜ flask create-tags
    """

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')

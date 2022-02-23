import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from vet_api_rest.extensions import db
    from vet_api_rest.models import Usuario

    click.echo("create user")
    user = Usuario(username="admin", email="admin@mail.com", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")

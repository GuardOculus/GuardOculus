import os
import click
from app import db
from app.models import User


def register(app):
    @app.cli.group()
    def user():
        """User profiles interaction"""
        pass

    @user.command()
    @click.option("-u", "--username")
    @click.option("-p", "--password")
    @click.option("-r", "--role", type=click.IntRange(0, 1))
    def create(username, password, role):
        new_user = User(username=username, role=int(role))
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        click.echo('User created')

    @user.command()
    def list():
        click.echo("Username\t│Role")
        click.echo("────────────────┼─────")
        for user in User.query.all():
            click.echo(user.username + "\t\t│" + ("admin" if user.role == 0 else "guard"))

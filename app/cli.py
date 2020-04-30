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
    @click.argument("username")
    @click.argument("password")
    @click.argument("role")
    def create(username, password, role):
        new_user = User(username=username, role=int(role))
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        click.echo('User created', color='green')

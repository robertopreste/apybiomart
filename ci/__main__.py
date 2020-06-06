#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import shutil
import subprocess

import click

from .create_suite import create_all


@click.group()
def cli():
    """ Main entry point for the CI infrastructure. """
    pass


@cli.command(name="create-suite")
def create_suite():
    """ Update all files used for testing. """
    click.echo("Updating test files...")
    create_all()
    click.echo("Done.")


@cli.command(name="build")
def build():
    """ Build the package to be uploaded to PyPI. """
    build_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             "build")
    dist_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            "dist")
    eggs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            ".eggs")
    egg_info_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "apybiomart.egg-info")

    if os.path.isdir(build_dir):
        click.echo("Removing build directory... ", nl=False)
        shutil.rmtree(build_dir)
        click.echo("Done.")

    if os.path.isdir(eggs_dir):
        click.echo("Removing .eggs directory... ", nl=False)
        shutil.rmtree(eggs_dir)
        click.echo("Done.")

    if os.path.isdir(egg_info_dir):
        click.echo("Removing .egg-info directory... ", nl=False)
        shutil.rmtree(egg_info_dir)
        click.echo("Done.")

    if os.path.isdir(dist_dir):
        click.echo("Removing dist directory... ", nl=False)
        shutil.rmtree(dist_dir)
        click.echo("Done.")

    click.echo("Building package...")
    subprocess.check_call(["python", "setup.py", "sdist", "bdist_wheel"])
    click.echo("Done.")


@cli.command(name="docs")
def docs():
    """ Create documentation. """
    click.echo("Creating documentation with Sphinx...")
    subprocess.check_call(
        ["sphinx-build", "-b", "html", "docs", "docs/_build"]
    )
    click.echo("Done.")


@cli.command(name="flake8")
def flake8():
    """ Perform flake8 checks on the code. """
    click.echo("Performing flake8 linting...")
    subprocess.check_call(["flake8", "apybiomart"])
    click.echo("Done.")


@cli.command(name="install")
def install():
    """ Install the package (in development mode). """
    click.echo("Installing apybiomart...")
    subprocess.check_call(["pip", "install", "-e", "."])
    click.echo("Done.")


@cli.command(name="install-reqs")
def install_reqs():
    """ Install all requirements needed for the package. """
    click.echo("Installing requirements for apybiomart...")
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    click.echo("Done.")


@cli.command(name="check")
def twine_check():
    """ Check the package using Twine. """
    click.echo("Checking package...")
    subprocess.check_call(["twine", "check", "dist/*"])
    click.echo("Done.")


@cli.command(name="upload")
@click.option("-u", "--username", default=None, help="PyPI username.")
@click.option("-p", "--password", default=None, help="PyPI password.")
def twine_upload(username, password):
    """ Upload the package to PyPI using Twine.

    Args:
        username: PyPI username (if not provided, twine will ask for it)
        password: PyPI password (if not provided, twine will ask for it)
    """
    cmd = ["twine", "upload"]
    if username:
        cmd.extend(["-u", username])
        if password:
            cmd.extend(["-p", password])
    cmd.append("dist/*")

    click.echo("Uploading package...")
    subprocess.check_call(cmd)
    click.echo("Done.")


if __name__ == '__main__':
    cli()

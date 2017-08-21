'''
Golem - run commands in an automatically discovered and captured environment.
'''

import click

@click.command()
def cli():
    click.echo('Hello world!')

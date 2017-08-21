'''
Golem - run commands in an automatically discovered and captured environment.
'''

import click
import logging

@click.group()
@click.option('-v', '--verbose', count=True, help='Increase logging verbosity.')
@click.option('-q', '--quiet', count=True, help='Decrease logging verbosity')
def cli(verbose, quiet):
    logging_level = logging.WARN - (verbose * 10) + (quiet * 10)
    logging.basicConfig(level=logging_level)
    log = logging.getLogger("golem.main")
    pass

@cli.command()
def init():
    log = logging.getLogger("golem.init")
    log.info("Starting Golem")
    click.echo("Stub for init")
    log.info("Stopping Golem")
    pass

@cli.command()
def format():
    log = logging.getLogger("golem.format")
    log.info("Starting Golem")
    click.echo("Stub for format")
    log.info("Stopping Golem")
    pass

@cli.command()
def run():
    log = logging.getLogger("golem.run")
    log.info("Starting Golem")
    click.echo("Stub for run")
    log.info("Stopping Golem")
    pass

@cli.command()
def alias():
    log = logging.getLogger("golem.alias")
    log.info("Starting Golem")
    click.echo("Stub for alias")
    log.info("Stopping Golem")

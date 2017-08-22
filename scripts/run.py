'''
Golem - run commands in an automatically discovered and captured environment.
'''

import click
import logging
import commands as cmds

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
    cmds.init()
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
@click.option('-t','--target', default='run', type=click.Choice(['run','init','format']), help='One of: "run", "init", or "format". Specify the context in which this alias is run. [default: run]')
@click.option('-l','--location', type=click.Path(exists=True), default='.', help='Specify the location in which this alias shall be run.')
@click.option('-e','--environment', multiple=True, help='Specify a series of format-type alias names to use as environment variables in the evaluation of this alias.')
@click.option('-H','--set-help', default="", help='Specify the help string for this alias.')
@click.argument('name')
@click.argument('command', nargs=-1, required=True)
def alias(target, location, environment, set_help, name, command):
    log = logging.getLogger("golem.alias")
    log.info("Starting Golem")
    cmds.alias(target=target, location=location, environment=environment, help=set_help, name=name, command=' '.join(command))
    click.echo("Stub for alias")
    log.info("Stopping Golem")

@cli.command()
@click.argument('target')
@click.argument('name')
def format(target, name):
    log = logging.getLogger("golem.format")
    log.info("Starting Golem")
    cmds.format(target=target, name=name)
    log.info("Stopping Golem")

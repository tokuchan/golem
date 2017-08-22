from pathlib import Path
from subprocess import check_output

import click
import logging

# SQLAlchemy libraries
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Alias(Base):
    __tablename__ = 'Alias'
    target = Column(String)
    location = Column(String)
    environment = Column(String)
    name = Column(String, primary_key=True)
    command = Column(String)
    help = Column(String)
    def __repr__(self):
        return f"Alias(target='{self.target}', location='{self.location}', environment='{self.environment}', name='{self.name}', command='{self.command}, help='{self.help}')"
    pass

class GolemDB:
    def __init__(self):
        self.engine = create_engine('sqlite:///.golem.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)
        pass
    def get(self, target, name):
        return self.session.query(Alias).filter(Alias.target == target, Alias.name == name).first()
    def set(self, alias):
        self.session.merge(alias)
        self.session.commit()
        pass
    def session(self):
        return self.session
    pass

def init():
    log = logging.getLogger("golem.commands.init")
    log.info("Initializing Golem Project")
    db = GolemDB()
    db.set(Alias(target="init", name="test", command="echo foo"))
    log.debug(db.get("init", "test"))
    click.echo("Stub for actual init function")
    log.info("Golem project intialized")
    pass

def alias(*, name, command, target="run", location=Path('.'), environment=None, help=None):
    log = logging.getLogger("golem.commands.alias")
    log.info("Adding/updating an alias")
    db = GolemDB()
    alias = Alias(target=target, location=str(location), name=name, command=command, help=help)
    db.set(alias)
    click.echo("Stub for alias function")
    log.info("Alias updated.")
    pass

def format(target, name):
    log = logging.getLogger("golem.format")
    log.info("Formatting alias")
    db = GolemDB()
    alias = db.get(target, name)
    log.debug(alias)
    click.echo(check_output(alias.command, encoding='utf-8', shell=True))
    pass

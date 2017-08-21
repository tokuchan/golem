import click
import logging

# SQLAlchemy libraries
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Aliases(Base):
    run_scope = Column(String)
    name = Column(String, primary_key=True)
    command = Column(String)
    pass

class GolemDB:
    def __init__(self):
        self.engine = create_engine('sqlite:///.golem.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(engine)
        pass
    def get(self, run_scope, name):
        return self.session.query(Aliases).filter(Aliases.run_scope == run_scope, Aliases.name == name).first()
    def set(self, run_scope, name, command):
        alias = Aliases(run_scope = run_scope, name = name, command = command)
        self.session.add(alias)
        self.session.commit()
        pass
    def session(self):
        return self.session
    pass

def init():
    log = logging.getLogger("golem.commands.init")
    log.info("Initializing Golem Project")
    click.echo("Stub for actual init function")
    log.info("Golem project intialized")
    pass

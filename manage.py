#!/usr/bin/env python

from flask_script import Server, Manager
from fstat import app, db
from fstat.parser import get_summary


manager = Manager(app)
manager.add_command('runserver', Server())


@manager.command
def db_init():
    db.create_all()


@manager.option('-n', dest='num_days')
@manager.option('-j', '--job', dest='job_name')
def process_jobs(job_name, num_days):
    get_summary(job_name, int(num_days))


if __name__ == '__main__':
    manager.run()

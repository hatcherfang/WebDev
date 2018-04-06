# -*- coding: utf-8 -*-
# from flask.ext.script import Manager, Server
# Importing flask.ext.script is deprecated, use flask_script instead
#usage:
# python manage.py runserver
from flask_script import Manager, Server
from app import app


manager = Manager(app)


manager.add_command("runserver", Server(host='0.0.0.0', port=5000, use_debugger=True)) 
if __name__ == '__main__':
    manager.run()

#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/BlogApp/")
#from BlogApp import app as application
from App import app as application
application.secret_key = 'djfg'

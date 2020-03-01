#!/usr/bin/python
import sys
sys.path.insert(0, 'xxx/.local/lib/python2.6/site-packages')
from wsgiref.handlers import CGIHandler
from myapp import app
CGIHandler().run(app)

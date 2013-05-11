#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
main.py

This file is part of example app for Google AppEngine Test Starter project

Code downloaded from: http://github.com/rzajac/gaeteststarter
@author: Rafal Zajac rzajac<at>gmail<dot>com
@copyright: Copyright 2007-2013 Rafal Zajac rzajac<at>gmail<dot>com. All rights reserved.
@license: Licensed under the MIT license
'''

# Python imports

# GAE imports
import webapp2
from webapp2_extras import routes

url_mapping = [
    routes.RedirectRoute(r'/', handler='webhandlers.TestHandler1'),
    routes.RedirectRoute(r'/postInBody', handler='webhandlers.TestHandler2'),
    routes.RedirectRoute(r'/testTaskQueue', handler='webhandlers.TestTaskQueue', methods=['POST']),
    routes.RedirectRoute(r'/testTaskQueue/<param1:[^/]+>', handler='webhandlers.TestTaskQueue', methods=['GET']),
    routes.RedirectRoute(r'/<param1:[^/]+>', handler='webhandlers.TestHandler2'),
]

app = webapp2.WSGIApplication(url_mapping)

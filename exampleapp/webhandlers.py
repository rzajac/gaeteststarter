#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
webhandlers.py

This file is part of example app for Google AppEngine Test Starter project

Code downloaded from: http://github.com/rzajac/gaeteststarter
@author: Rafal Zajac rzajac<at>gmail<dot>com
@copyright: Copyright 2007-2013 Rafal Zajac rzajac<at>gmail<dot>com. All rights reserved.
@license: Licensed under the MIT license
"""

# GAE imports
import webapp2
from google.appengine.api import taskqueue


class TestHandler1(webapp2.RequestHandler):

    def get(self):

        respMsg = 'Hello World'

        param1 = self.request.get('param1', '')
        param2 = self.request.get('param2', '')

        if param1:
            respMsg += ' ' + param1

        if param2:
            respMsg += ' ' + param2

        self.response.write(respMsg)

    def post(self):

        param1 = self.request.get('paramPost1', '')
        param2 = self.request.get('paramPost2', '')

        self.response.write(param1 + param2)


class TestHandler2(webapp2.RequestHandler):

    def get(self, param1):
        self.response.write(param1)

    def post(self):
        self.response.write(self.request.body)


class TestTaskQueue(webapp2.RequestHandler):

    def get(self, param1):
        taskqueue.add(url='/testTaskQueue', params={'param': param1})
        self.response.write('Task Added')

    def post(self):
        # This is our task runner
        self.response.write('Task Finished')

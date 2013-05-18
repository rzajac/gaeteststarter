#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_example_app.py

Example tests for exampleapp that is part of this package.

Code downloaded from: http://github.com/rzajac/gaeteststarter
@author: Rafal Zajac rzajac<at>gmail<dot>com
@copyright: Copyright 2007-2013 Rafal Zajac rzajac<at>gmail<dot>com. All rights reserved.
@license: Licensed under the MIT license
"""

from __future__ import with_statement

# Python imports
from webtest.app import AppError

# GAE imports
from google.appengine.ext import ndb

# Test imports
from teststarter import BaseTestCase
from exampleapp.main import app as tst_app


class ExampleAppTestHandlers(BaseTestCase):
    """Test app handlers"""

    def setUp(self):

        # Setup application
        self.set_application(tst_app)

        # Create testbed
        self.setup_testbed()

    def tearDown(self):
        self.clear_application()
        self.testbed.deactivate()

    def testGet(self):
        resp = self.get('/')
        self.assertOK(resp)
        self.assertEquals('Hello World', resp.body)

    def testGetWithParamsInUrl(self):
        resp = self.get('/?param1=aaa&param2=bbb')
        self.assertOK(resp)
        self.assertEquals('Hello World aaa bbb', resp.body)

    def testGetWithParamsAsDictionary(self):
        params = {'param1': 'aaa2', 'param2': 'bbb2'}
        resp = self.get('/', params)
        self.assertOK(resp)
        self.assertEquals('Hello World aaa2 bbb2', resp.body)

    def testPostInBody(self):
        resp = self.post('/postInBody', 'postTest')
        self.assertOK(resp)
        self.assertEquals('postTest', resp.body)

    def testPostWithDataAsDictionary(self):
        params = {'paramPost1': 'post1', 'paramPost2': 'post2'}
        resp = self.post('/', params)
        self.assertOK(resp)
        self.assertEquals('post1post2', resp.body)

    def test404(self):

        with self.assertRaises(AppError) as ex:
            self.get('/not/Existing/Route')

        self.assertTrue(ex.exception.message.startswith('Bad response: 404 Not Found'))


class ExampleAppTestQueues(BaseTestCase):
    """Test task queues"""

    def setUp(self):

        # Setup application
        self.set_application(tst_app)

        # Create testbed
        self.setup_testbed()
        self.init_taskqueue_stub()

    def tearDown(self):
        self.clear_application()
        self.testbed.deactivate()

    def testOneTaskPutOnTheQueue(self):

        # Add task
        resp = self.get('/testTaskQueue/paramForTask')

        # Test handler
        self.assertOK(resp)
        self.assertEquals('Task Added', resp.body)

        # See if we have 1 task added to the default queue
        self.assertTasksInQueue(1)

        # Get our task
        task = self.get_tasks()[0]

        # Test task properties
        self.assertEquals('/testTaskQueue', task['url'])
        self.assertEquals('default', task['queue_name'])
        self.assertEquals({'param': 'paramForTask'}, task['params'])
        self.assertEquals('param=paramForTask', task['decoded_body'])
        self.assertEquals('POST', task['method'])

        # Execute task
        count = self.execute_tasks_until_empty()

        # We should have run only one task
        self.assertEquals(1, count)


class Car(ndb.Model):
    """Example model"""

    name = ndb.StringProperty()
    some_value = ndb.IntegerProperty(default=0)


class ExampleAppTestDatastore(BaseTestCase):
    """Test datastore"""

    def setUp(self):

        # Setup application
        self.set_application(tst_app)

        # Create testbed
        self.setup_testbed()
        self.init_datastore_stub()
        self.init_memcache_stub()

    def tearDown(self):
        self.clear_application()
        self.testbed.deactivate()

    def testPersistance(self):

        cars_count = Car.query().count()
        self.assertEqual(0, cars_count)

        car = Car()
        car.name = 'Bittle'
        car.some_value = 10
        car.put()

        cars_count = Car.query().count()
        self.assertEqual(1, cars_count)

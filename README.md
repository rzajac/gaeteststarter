## AppEngine Test Starter

Purpose of this project is to bootstrap writing tests for Google AppEngine applications. It provides **BaseTestCase** class loaded with helper methods to _initialize stubs_, _test task queues_, _test request handlers_ and more...

With the package you also get **testrunner.py** that will help you run tests:

* run all the tests in the test package
* run only one test file
* run only tests form specific TestCase class
* run only one test case from specific class

Part of this package is example application and example tests. Please see the files for usage examples. [exampletests/test_example_app.py](https://github.com/rzajac/gaeteststarter/blob/master/exampletests/test_example_app.py)

## Test runner usage:

<pre>
Usage: testrunner.py SDK_PATH TEST_PATH [TEST_METHOD]

Run unit tests for App Engine apps.

SDK_PATH    Path to the AppEngine SDK
TEST_PATH   Path to module / class containing tests
TEST_METHOD The name of the method to run

Examples:
  testrunner.py /sdk/path exampletests - run all tests in module
  testrunner.py /sdk/path exampletests.test_example_app - run all tests in a specific file
  testrunner.py /sdk/path exampletests.test_example_app.ExampleAppTestHandlers - run all rests in a class
  testrunner.py /sdk/path exampletests.test_example_app.ExampleAppTestHandlers testGet - run one test
</pre>

To make things even easier there is a **Makefile** that you can customize and use it to run tests without typing long options :) Just type *make test*.

## Run example tests

Either use:
    $ make test
or
    $ ./testrunner.py /usr/local/google_appengine exampletests

## Using Test Starter in your project

The easiest way to add Test Starter to your applications is to copy **testrunner.py**, **teststarter.py** and **Makefile** to your app test folder.

You can also add Test Starter as git submodule and take advantage of updates to this project.

    $ git submodule add http://github.com/rzajac/gaeteststarter tests
    $ git submodule init
    $ git submodule update

## License

Code is licensed under MIT license.

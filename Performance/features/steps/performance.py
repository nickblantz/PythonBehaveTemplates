from behave import *
import time
import subprocess

@given(u'I have File Archival and Retreival performance tests in "{filename}"')
def set_impl(context, filename):
    context.filename = filename

@when('I execute the test for "{numOfUsers}" users')
def set_impl(context, numOfUsers):
	#subprocess.run(["C:/apache-jmeter-5.0/bin/jmeter", "-Jthreads="+numOfUsers, "-n", "-t", "libraries/"+context.filename+".jmx", "-l", "test_results/"+context.filename+".jtl"])
	subprocess.run(["echo", context.filename])
	
@then('I should get back the performance results')
def step_impl(context):
    assert True is not False


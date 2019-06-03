# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from fixtures.exampleFixture import test_fixture
import os
import yaml
	
def before_all(context):
	context.word = os.environ.get('TEST_ENV')
	if context.word == None:
		context.word = "QA1"	#default value if no environments selected
	context.config = yaml.load(open("features/config/"+context.word+".yml"), Loader=yaml.FullLoader)
	

def before_tag(context, tag):
    if tag == "Fixture":
	    use_fixture(test_fixture, context)

# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from fixtures.exampleFixture import test_fixture
import os
import yaml
	
def before_all(context):
	context.word = os.environ['TEST_ENV']
	context.config = yaml.load(open("features/config/"+context.word+".yml"), Loader=yaml.FullLoader)
	

def before_tag(context, tag):
    if tag == "Fixture":
	    use_fixture(test_fixture, context)

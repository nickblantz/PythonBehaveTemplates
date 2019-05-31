from behave import *
import requests
import json


@given('I am attempting to use an example API')
def set_impl(context):
    context.url = context.config.get("api_url")

@when('I request valid information from the API')
def set_impl(context):
	context.response = requests.get(context.url)
	
@then('I must get a reponse with status code 200 and a JSON object with token')
def step_impl(context):
    assert context.response.status_code == 200
	
	
	
@given('I am attempting to use an example API with the coordinates of San Francisco')
def set_impl(context):
	context.parameters = {"lat": 37.78, "lon": -122.41}
	context.url = context.config.get("api_url2")


@when('I request valid information from the API regarding those parameters')
def set_impl(context):
	context.response = requests.get(context.url, params=context.parameters)

@then('I receive the requested data and find that the ISS passes San Francisco five times')
def step_impl(context):
	assert context.response.status_code == 200
	assert context.response.json().get("request").get("passes") is 5
	
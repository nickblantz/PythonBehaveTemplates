@APIExample @QA
Feature: API and JSON Example Tests
  @API
  Scenario: Attempting to retrieve JSON data from API
    Given I am attempting to use an example API
    When I request valid information from the API
    Then I must get a reponse with status code 200 and a JSON object with token
  @API @Fixture
  Scenario: Retrieving API data using parameters
    Given I am attempting to use an example API with the coordinates of San Francisco
    When I request valid information from the API regarding those parameters
    Then I receive the requested data and find that the ISS passes San Francisco five times
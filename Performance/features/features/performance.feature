@PerformanceExample @UAT
Feature: DMS File archival and search Performance

  @Performance @Fixture
  Scenario: Measure time take to archive a file, folder and document and then retrieve it
    Given I have File Archival and Retreival performance tests in "DMS-Billing"
    When I execute the test for "2" users
    Then I should get back the performance results
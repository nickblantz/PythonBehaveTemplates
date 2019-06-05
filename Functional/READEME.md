## Directory Structure

- **specs:** Holds all of the feature files (.feature) which act as instructions/documentation for the tests
	
- **steps:** Holds all step definitions which act as code behind the feature files
	
- **config:** Holds any configuration files for the project (.yml)
	
- **fixtures:** Holds any fixture files (.py) which operate in conjunction with the environment file (environment.py) to setup the environment for each test
			  
		  
## Other Documents

- **behave.ini:** Configuration file for running behave.  Normally, behave is set to capture standard out, we have disabled the capture here.
	
- **environment.py:** File used to setup the environment in which the tests are run.  Uses hooks like 'before_all' or 'after_tag' or fixtures to 
	specify the environments for each specific test.
	
	
## Environment Config
To configure environment specific data, create a new <ENV_NAME>.yml file.  These represent an environment that you can specify at run time through TEST_ENV.  The default environment config file is QA1.yml

	
## Setup Instructions
Setup this example project by first installing python and behave.  Clone the repo and then behave can be ran in either the 'Functional' or 'Performance' folder.

	
## Support 
[https://cucumber.io/docs/gherkin/reference](https://cucumber.io/docs/gherkin/reference)
	


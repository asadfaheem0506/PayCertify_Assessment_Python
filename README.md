# Python-Behave-Selenium

## Test Cases Included

Test Case #1: Orbitz Search Results 

##Framework-Page Object Model Overview
I am using Cucumber BDD framework with Page Object Model. Language used for this framework is python. Behave is the python library used for implementing this BDD framework.
It is a common language syntax which can be used to define steps for end to end tests.

Overview of the Page Object Model 

1)Feature file includes all the test cases setup as individual scenarios. 
2)Logic behind each step is inside the step definition file. 
3)All the common functions used in the project are driverUtil file
4)config file includes the url and basic information for common variables. 
5)pageUtils includes all the elements and their xpaths that are being used for automation. 
6)environment files includes the before and after methods for all the tests
7)All the reports are generated and kept in the reports folder. 
   

## Installations for environment setup
1) First of move root project directory execute `pip install -r requirements.txt` which will install the all needed python dependencies to your computer

2) Install the chromedriver using: `brew cask install chromedriver`
 
3) Install the geckodriver(firefox) using: `brew install geckodriver`
 
4) Install allure using `brew install allure` & `pip install allure_behave`(OR `npm install -g allure-commandline --save-dev`)

#Test Execution

1) In the root project directory execute: `behave`and it will start executing tests

2) In the root project directory execute: run `behave -f plain --no-capture features/GoogleSearch_UI.feature` to print logs from print statements.

3) In the root project directory execute: run `behave -f plain --no-capture --tags=@<tagName> features/GoogleSearch_UI.feature` to print logs and run specific test by providing tag.

4) To execute tests with multiple browsers and generate report, execute below three commands in different command prompts
  --Follow steps below. 
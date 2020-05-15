from behave import *
from utilities.driverUtil import driver
import utilities.config as sconfig
from pageUtils.elements import *
import re

use_step_matcher("re")

@given("I go to Orbitz")
def step_impl(context):
    driver.navigateToMaps(sconfig.orbitzUrl)

@when("I select flight tab and multi city option")
def step_impl(context):
    driver.waitOnElement(flightsBtn)
    driver.elementClick(flightsBtn)
    driver.waitOnElement(multiCityBtn)
    driver.elementClick(multiCityBtn)
    try:
        driver.elementClick(notifCloseBtn)
    except:
        pass

@when("I Search for 2 adults and 2 children with ages")
def step_impl(context):
    driver.waitFor(1)
    driver.elementClick(adultAgeBtn)
    driver.waitOnElement(adultAgeSelectBtn)
    driver.elementClick(adultAgeSelectBtn)
    driver.elementClick(childrenBtn)
    driver.waitOnElement(childrenNumBtn)
    driver.elementClick(childrenNumBtn)
    driver.elementClick(children1AgeBtn)
    driver.waitOnElement(children1AgeSelectBtn)
    driver.elementClick(children1AgeSelectBtn)
    driver.elementClick(children2AgeBtn)
    driver.waitOnElement(children2AgeSelectBtn)
    driver.elementClick(children2AgeSelectBtn)
    driver.waitFor(1)
    driver.elementClick(child1AgeLabel)

@when("I select route using three flight destinations")
def step_impl(context):
    driver.waitFor(2)
    driver.elementClick(addFlightBtn)
    driver.enterValues(source1Btn, sconfig.DFW)
    driver.waitOnElement(loc1And3Select)
    driver.elementClick(loc1And3Select)
    driver.enterValues(destination1Btn, sconfig.SFO)
    driver.waitOnElement(loc2Select)
    driver.elementClick(loc2Select)
    driver.enterValues(source2Btn, sconfig.SFO)
    driver.waitOnElement(loc2Select)
    driver.elementClick(loc2Select)
    driver.enterValues(destination2Btn, sconfig.NYC)
    driver.waitOnElement(loc1And3Select)
    driver.elementClick(loc1And3Select)
    driver.enterValues(source3Btn, sconfig.NYC)
    driver.waitOnElement(loc1And3Select)
    driver.elementClick(loc1And3Select)
    driver.enterValues(destination3Btn, sconfig.DFW)
    driver.waitOnElement(loc1And3Select)
    driver.elementClick(loc1And3Select)

@when("I select travel dates for each flight")
def step_impl(context):
    flight1Date = "[2]"
    flight2Date = "[6]"
    flight3Date = "[10]"
    driver.elementClick(flight1DateBtn)
    driver.waitOnElement(datesPicker)
    availDates = len(driver.getElements(datesPicker))
    print("Available Dates are: "+str(availDates))
    driver.elementClick(datesPicker+flight1Date)
    driver.waitFor(1)
    driver.elementClick(flight2DateBtn)
    driver.elementClick(datesPicker+flight2Date)
    driver.waitFor(1)
    driver.elementClick(flight3DateBtn)
    driver.elementClick(datesPicker+flight3Date)

@when("I search with the selected criteria")
def step_impl(context):
    driver.waitFor(1)
    driver.elementClick(searchBtn)

@then("I verify results select flights and validate itinerary")
def step_impl(context):
    driver.waitOnElement(flightsResult)
    numOfFlights = len(driver.getElements(flightsResult))
    print("Number of Results from the Search Criteria: "+str(numOfFlights))
    try:
        driver.elementClick(nonstopFlightSelect)
    except:
        driver.elementClick(onestopFlightSelect)
    print("Selecting the Lowest Price Flight with Least Stops")
    driver.waitFor(5)
    driver.elementClick(lowestPriceFlight)
    driver.waitFor(5)
    driver.elementClick(lowestPriceFlight)
    print("Waiting on Selecting Second Flight")
    driver.waitOnElement(noExtraCostFlight)
    print("Selecting Flight with No Extra Cost")
    driver.waitFor(5)
    driver.elementClick(lowestPriceFlight)
    driver.waitOnElement(selectFareBtn)
    driver.elementClick(lowestPriceFlight)
    print("Waiting on Selecting Third Flight")
    driver.waitOnElement(noExtraCostFlight)
    print("Selecting Flight with No Extra Cost")
    driver.waitFor(5)
    driver.elementClick(lowestPriceFlight)
    driver.waitOnElement(selectFareBtn)
    driver.elementClick(lowestPriceFlight)
    driver.waitFor(3)
    driver.switchWindow()
    print("Validating Confirmation of First Flight")
    flight1Source = driver.getTextForElement(flight1Sourceconfirmation)
    flight1Dest = driver.getTextForElement(flight1DestConfirmation)
    print("Flight 1 Source: "+str(flight1Source))
    print("Flight 1 Dest: "+str(flight1Dest))
    assert sconfig.Dallas in flight1Source
    assert sconfig.sanFran in flight1Dest
    print("Validating Confirmation of Second Flight")
    flight2Source = driver.getTextForElement(flight2Sourceconfirmation)
    flight2Dest = driver.getTextForElement(flight2DestConfirmation)
    print("Flight 2 Source: "+str(flight2Source))
    print("Flight 2 Dest: "+str(flight2Dest))
    assert sconfig.sanFran in flight2Source
    assert sconfig.newYork in flight2Dest
    print("Validating Confirmation of Third Flight")
    flight3Source = driver.getTextForElement(flight3Sourceconfirmation)
    flight3Dest = driver.getTextForElement(flight3DestConfirmation)
    print("Flight 3 Source: "+str(flight3Source))
    print("Flight 3 Dest: "+str(flight3Dest))
    assert sconfig.newYork in flight3Source
    assert sconfig.Dallas in flight3Dest
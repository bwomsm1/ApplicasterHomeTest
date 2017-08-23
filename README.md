# Applicaster Home Test
Home test for Mobile Automation position in Applicaster

## Prerequisites
* Test should be running under Mac OS (requesting this since I haven't tested it under Windows only)
* Appium client v1.6.6-beta.4 is installed on your machine (for installation follow instructions below)
* The application original Bundle ID has not changed from SMWarren.e-Where
* Appium server is running in background, from Mac terminal run 'appium' command.

## Running the tests
* Install our application on "iPhone 6 Simulator" via xCode (remember keeping SMWarren.e-Where as our bundle id) <br />
    (you can choose other simulator such as iPhone 7, just update this in configuration.json file under device_name field, by default its iPhone 6)
* From terminal enter the following:
    * cd ApplicasterHomeTest/ <br >
    * python test.py

## Tests description
The project contains the following 3 tests:<br />
    test_navigate_to_all_screens - This test perform basic navigation between all screens of the application and verify on each screen the elements<br />
    test_stress_test_launch_application - This test perform stress test for by launching the application 5 times in a row <br />
    test_background_to_forground - This test verifies that the application returns to same state (=screen) after returning from background

## How to install Appium v1.6.6-beta4
    1. brew install node           # get node.js
    2. npm install -g appium@beta  # get appium
    3. npm install wd              # get appium client

## Candidate personal details
Name: Boaz Warshawsky<br />
Phone: 054-566-4876<br />
LinkedIn: https://www.linkedin.com/in/boaz-warshawsky/


iOS app:
https://mandrillapp.com/track/click/30101449/github.com?p=eyJzIjoiMnh4cFJ0VFFPbDFlWlZaY0Y4c2FFaVJiNHVRIiwidiI6MSwicCI6IntcInVcIjozMDEwMTQ0OSxcInZcIjoxLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL2dpdGh1Yi5jb21cXFwvU01XQVJSRU5cXFwvU1dFdmVudHNQcm90b3R5cGVBcHBcIixcImlkXCI6XCI1MmQ3MzVlNzdhOWY0MWI3OTZkOWVkMzA2YjkxOGUwMFwiLFwidXJsX2lkc1wiOltcIjk4ODY5NWI2YWM5OWI1Yjg3OGVmMGM0ODgxMzRlZGI4ZDBiYWEzNWRcIl19In0

Android app:
https://github.com/erikcaffrey/RecyclerView-Examples

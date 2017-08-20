## Applicaster Home Test
Home test for Mobile Automation position in Applicaster

## Candidate personal details
Name: Boaz Warshawsky<br />
Phone: 054-566-4876<br />
LinkedIn: https://www.linkedin.com/in/boaz-warshawsky/

## Prerequisites
* Test should be running under Mac OS (requesting this since I haven't tested it under Windows only)
* Appium client v1.6.6-beta.4 is installed on your machine (for installation follow instructions below)
* The application original Bundle ID has not changed from SMWarren.e-Where
* Appium server is running in background, from Mac terminal run 'appium' command.

## Running the tests
* Install our application on "iPhone 6 Simulator" via xCode (remember keeping SMWarren.e-Where as our bundle id) <br >
* From terminal enter the following:
    * cd ApplicasterHomeTest/ <br >
    * python test.py


## How to install Appium v1.6.6-beta4
    1. brew install node           # get node.js
    2. npm install -g appium@beta  # get appium
    3. npm install wd              # get appium client



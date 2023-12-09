*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.4 seconds
${HOME_URL}  http://${SERVER}
${ADD_BOOK_URL}  http://${SERVER}/addbook
${ADD_MANUAL_URL}  http://${SERVER}/addmanual
${ALL_REFERENCES_URL}  http://${SERVER}/all_references

*** Keywords ***
Open And Configure Browser
    # jos käytät Firefoxia ja Geckodriveriä käytä seuraavaa riviä sitä alemman sijaan
    # ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # seuraava rivi on kommentoitu pois tässä vaiheessa
    # Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

#Open And Configure Browser
#    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
#    Call Method    ${options}    add_argument    --no-sandbox
#    Call Method  ${options}  add_argument  --headless
#    Open Browser  browser=chrome  options=${options}
#    Set Selenium Speed  ${DELAY}

Addbook Page Should Be Open 
    SeleniumLibrary.Title Should be  Add a book

Addmanual Page Should Be Open
    SeleniumLibrary.Title Should be  Add a manual

All_references Page Should Be Open
    SeleniumLibrary.Title Should be  All references


Go To Addbook Page
    Go To  ${ADD_BOOK_URL}

Go To Addmanual Page
    Go To  ${ADD_MANUAL_URL}

Go To All_references Page
    Go To  ${ALL_REFERENCES_URL}

Go To Starting Page
    SeleniumLibrary.Go To  ${HOME_URL} 

Home Page Is Open
    SeleniumLibrary.Title Should Be  Home

Submit A Book
    Click Button  Add    

Submit A Manual
    Click Button  Add

Delete A reference
    Click Button  Delete

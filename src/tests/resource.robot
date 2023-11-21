*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${ADD_BOOK_URL}  http://${SERVER}/addbook
${ALL_REFERENCES_URL}  http://${SERVER}/all_references

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Addbook Page Should Be Open 
    SeleniumLibrary.Title Should be  Add a book

All_references Page Should Be Open
    SeleniumLibrary.Title Should be  All references


Go To Addbook Page
    Go To  ${ADD_BOOK_URL}

Go To All_references Page
    Go To  ${ALL_REFERENCES_URL}

Go To Starting Page
    SeleniumLibrary.Go To  ${HOME_URL} 

Set author
    [Arguments]  ${author}  
    Input Text  author  ${author}

Set title
    [Arguments]  ${title}  
    Input Text  title  ${title}

Set publisher
    [Arguments]  ${publisher}  
    Input Text  publisher  ${publisher}

Set year
    [Arguments]  ${year}  
    Input Text  year  ${year}

Set volume
    [Arguments]  ${volume}  
    Input Text  volume  ${volume}

Set series
    [Arguments]  ${series}  
    Input Text  series  ${series}

Set address
    [Arguments]  ${address}  
    Input Text  address  ${address}

Set edition
    [Arguments]  ${edition}  
    Input Text  author  ${edition}

Set month
    [Arguments]  ${month}  
    Input Text  author  ${month}

Set note
    [Arguments]  ${note}  
    Input Text  author  ${note}





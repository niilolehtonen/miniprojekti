*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Addmanual Page

*** Test Cases ***
Add A Manual With Only Necessary Attributes
    Set title  Test
    
    Submit A Manual
    Home Page Is Open

Add A Manual With Optional Attributes
    Set title  Test
    Set author  Tom
    Set year  2000
    Set organization  Test
    Set address  Helsinki
    Set edition  4
    Set month  8
    Set note  testnote

    Submit A Manual
    Home Page Is Open
    
Add A Manual With Invalid Author
    Set title  Test
    Set author  34

    Submit A Manual
    Addmanual Should Fail With Message  Author should contain only letters

Add A Manual With Invalid Year
    Set title  Test
    Set year  test

    Submit A Manual
    Addmanual Should Fail With Message  Year should contain only numbers

Add A Manual With Invalid Month
    Set title  Test
    Set month  41

    Submit A Manual
    Addmanual Should Fail With Message  Month should contain only numbers 1 to 12

Add A Manual With Invalid Author, Year And Month
    Set title  Test
    Set Author  34
    Set year  test
    Set month  41

    Submit A Manual
    Addmanual Should Fail With Message  Author should contain only letters
    Addmanual Should Fail With Message  Year should contain only numbers
    Addmanual Should Fail With Message  Month should contain only numbers 1 to 12
    
*** Keywords ***
Set title
    [Arguments]  ${title}  
    Input Text  title  ${title}

Set author
    [Arguments]  ${author}  
    Input Text  author  ${author}

Set year
    [Arguments]  ${year}  
    Input Text  year  ${year}

Set Organization
    [Arguments]  ${organization}
    Input Text  organization  ${organization}

Set address
    [Arguments]  ${address}  
    Input Text  address  ${address}

Set edition
    [Arguments]  ${edition}  
    Input Text  edition  ${edition}

Set month
    [Arguments]  ${month}  
    Input Text  month  ${month}

Set note
    [Arguments]  ${note}  
    Input Text  note  ${note}

Addmanual Should Fail With Message
    [Arguments]  ${message}
    Addmanual Page Should Be Open
    Page Should Contain  ${message}
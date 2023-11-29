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
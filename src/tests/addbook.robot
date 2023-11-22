*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Addbook Page

*** Test Cases ***
Add A Book With Correctly
    Set author  Tom
    Set title  Test
    Set publisher  Test
    Set year  2000
    Set volume  2
    Set series  3
    Set address  Helsinki
    Set edition  4
    Set month  8
    Set note  testnote
    Submit A Book 
    Home Page Is Open

*** Keywords ***

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
    Input Text  edition  ${edition}

Set month
    [Arguments]  ${month}  
    Input Text  month  ${month}

Set note
    [Arguments]  ${note}  
    Input Text  note  ${note}

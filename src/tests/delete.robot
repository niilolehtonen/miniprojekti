*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Check That Delete Button Work
    Go To Addmanual Page
    Set title  Test    
    Submit A Manual
    Go To All_references Page
    Delete A reference  Test

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

Set publisher
    [Arguments]  ${publisher}  
    Input Text  publisher  ${publisher}

Set volume
    [Arguments]  ${volume}  
    Input Text  volume  ${volume}

Set series
    [Arguments]  ${series}  
    Input Text  series  ${series}

Allreferences Should Contain
    [Arguments]  ${message}
    All_references Page Should Be Open
    Page Should Contain  ${message}

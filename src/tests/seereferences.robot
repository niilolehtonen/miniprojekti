*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Add A Manual Correctly And See That From Allreferences
    Go To Addmanual Page
    Set title  Test    
    Submit A Manual
    Go To All_references Page
    Allreferences Should Contain  title: Test

Add A Book Correctly And See That From Allreferences
    Go To Addbook Page
    Set author  Tom
    Set title  test
    Set publisher  Test
    Set year  2000
    Submit A Book
    Go To All_references Page
    Allreferences Should Contain  author: Tom
    Allreferences Should Contain  title: test
    Allreferences Should Contain  publisher: Test
    Allreferences Should Contain  year: 2000

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
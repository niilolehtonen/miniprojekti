*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Addarticle Page

*** Test Cases ***
Add An Article With Only Necessary Attributes
    Set author  Tom
    Set title  Test
    Set journal  Test_journal
    Set year  2000
    
    Submit An Article
    Home Page Is Open

Add An Article With Optional Attributes
    Set author  Tom
    Set title  Test
    Set journal  Test
    Set year  2000
    Set volume  2
    Set number  3
    Set pages  45
    Set month  8
    Set note  testnote
    Submit An Article
    Home Page Is Open

Add An Article With Invalid Author, Year, Volume And Month
    Set author  34
    Set title  Test
    Set journal  Test
    Set year  Invalid
    Set volume  testvolume
    Set number  test
    Set pages  34
    Set month  41
    Set note  test

    Submit An Article
    Addarticle Should Fail With Message  Author should contain only letters
    Addarticle Should Fail With Message  Year should contain only numbers
    Addarticle Should Fail With Message  Month should contain only numbers 1 to 12
*** Keywords ***

Set author
    [Arguments]  ${author}  
    Input Text  author  ${author}

Set title
    [Arguments]  ${title}  
    Input Text  title  ${title}

Set journal
    [Arguments]  ${journal}  
    Input Text  journal  ${journal}

Set year
    [Arguments]  ${year}  
    Input Text  year  ${year}

Set volume
    [Arguments]  ${volume}  
    Input Text  volume  ${volume}

Set number
    [Arguments]  ${number}
    Input Text  number  ${number}

Set pages
    [Arguments]  ${pages}  
    Input Text  pages  ${pages}

Set month
    [Arguments]  ${month}  
    Input Text  month  ${month}

Set note
    [Arguments]  ${note}  
    Input Text  note  ${note}

Addarticle Should Fail With Message
    [Arguments]  ${message}
    Addarticle Page Should Be Open
    Page Should Contain  ${message}
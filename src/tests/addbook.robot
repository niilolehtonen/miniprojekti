*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Addbook Page

*** Test Cases ***
Add A Book With Only Necessary Attributes
    Set author  Tom
    Set title  Test
    Set publisher  Test
    Set year  2000
    
    Submit A Book
    Home Page Is Open

Add A Book With Optional Attributes
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
    
Add A Book With Invalid Author
    Set author  45
    Set title  Test
    Set publisher  test
    Set year  2019

    Submit A Book
    Addbook Should Fail With Message  Author should contain only letters

Add A Book With Invalid Year
    Set author  Test
    Set title  Test
    Set publisher  test
    Set year  kk

    Submit A Book    

    Submit A Manual
    Addbook Should Fail With Message  Year should contain only numbers

Add A Book With Invalid Volume
    Set author  test
    Set title  Test
    Set publisher  test
    Set year  2019
    Set volume  kk

    Submit A Book
    Addbook Should Fail With Message  Volume should contain only numbers


Add A Book With Invalid Month
    Set author  test
    Set title  Test
    Set publisher  test
    Set year  1900
    Set month  41

    Submit A Book
    Addbook Should Fail With Message  Month should contain only numbers 1 to 12

Add A Book With Invalid Author, Year, Volume And Month
    Set Author  34
    Set title  Test
    Set publisher  test
    Set year  test
    Set volume  kk
    Set month  41

    Submit A Book
    Addbook Should Fail With Message  Author should contain only letters
    Addbook Should Fail With Message  Year should contain only numbers
    Addbook Should Fail With Message  Volume should contain only numbers
    Addbook Should Fail With Message  Month should contain only numbers 1 to 12

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

Addbook Should Fail With Message
    [Arguments]  ${message}
    Addbook Page Should Be Open
    Page Should Contain  ${message}

*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Click Addbook Link
    Click Link  Add a book
    Addbook Page Should Be Open 

Click All_references Link
    Click Link  See all references
    All_references Page Should Be Open
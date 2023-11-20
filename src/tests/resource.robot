*** Settings ***


*** Variables ***


*** Keywords ***

Input Book
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  Input  ${volume}  ${series}  ${address}  ${edition}  ${month}  ${note}
    Input  ${author}
    Input  ${title}
    Input  ${publisher}
    Input  ${year}
    Input  ${volume}
    Input  ${series}
    Input  ${address}
    Input  ${edition}
    Input  ${month}
    Input  ${note}
    Run Application
*** Settings ***
Library     ../AppLibrary.py


*** Keywords ***
Input Login Command
    Input    login

Input Credentials
    [Arguments]    ${username}    ${password}
    Input    ${username}
    Input    ${password}
    Run Application

Username ${username}
    Set Test Variable    ${USERNAME}    ${username}
Password ${password}
    Set Test Variable    ${PASSWORD}    ${password}

User Registers To The App
    Input    new
    Input    ${USERNAME}
    Input    ${PASSWORD}
    Run Application

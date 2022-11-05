*** Settings ***
Library     SeleniumLibrary
Library     ../AppLibrary.py


*** Variables ***
${SERVER}               localhost:5000
${BROWSER}              headlesschrome
${DELAY}                0.0 seconds
${HOME_URL}             http://${SERVER}
${LOGIN_URL}            http://${SERVER}/login
${REGISTER_URL}         http://${SERVER}/register
${VALID_USERNAME}       arhippa
${VALID_PASSWORD}       Qwerty1234


*** Keywords ***
Open And Configure Browser
    Open Browser    browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Login Page Should Be Open
    Title Should Be    Login

Main Page Should Be Open
    Title Should Be    Ohtu Application main page

Go To Login Page
    Go To    ${LOGIN_URL}

Go To Main Page
    Go To    ${HOME_URL}

Go To Register Page
    Go To    ${REGISTER_URL}

Register Page Should Be Open
    Title Should Be    Register

Welcome Page Should Be Open
    Title Should Be    Welcome to Ohtu Application!

Username ${username}, Password ${password} And Confirmation ${confirmation}
    Set Test Variable    ${USERNAME}    ${username}
    Set Test Variable    ${PASSWORD}    ${password}
    Set Test Variable    ${PASSWORD_CONFIRMATION}    ${confirmation}

User Registers To The Application
    Go To Register Page
    Input Text    username    ${USERNAME}
    Input Password    password    ${PASSWORD}
    Input Password    password_confirmation    ${PASSWORD_CONFIRMATION}
    Click Button    Register

User Has Registered Succesfully
    Username ${VALID_USERNAME}, Password ${VALID_PASSWORD} And Confirmation ${VALID_PASSWORD}
    User Registers To The Application

User Logs In
    Go To Login Page
    Input Text    username    ${VALID_USERNAME}
    Input Password    password    ${VALID_PASSWORD}
    Click Button    Login

User Has Registered Unsuccesfully
    Username ${VALID_USERNAME}, Password 13:37 And Confirmation 13:37
    User Registers To The Application

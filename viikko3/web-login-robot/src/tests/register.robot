*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close All Browsers
Test Setup          Reset Application


*** Test Cases ***
Register With Valid Username And Password
    Given Username arhippa, Password Qwerty1234 And Confirmation Qwerty1234
    When User Registers To The Application
    Then Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Given Username ye, Password Qwerty1234 And Confirmation Qwerty1234
    When User Registers To The Application
    Then Register Page Should Be Open
    And Page Should Contain
    ...    Username must contain at least 3 characters a-z

Register With Valid Username And Too Short Password
    Given Username arhippa, Password 13:37 And Confirmation 13:37
    When User Registers To The Application
    Then Register Page Should Be Open
    And Page Should Contain
    ...    Password must contain at least 8 characters with some non-letters

Register With Nonmatching Password And Password Confirmation
    Given Username arhippa, Password Qwerty1234 And Confirmation Qwerty12345
    When User Registers To The Application
    Then Register Page Should Be Open
    And Page Should Contain
    ...    Password confirmation does not match

Login After Successful Registration
    Given User Has Registered Succesfully
    When User Logs In
    Then Main Page Should Be Open

Login After Failed Registration
    Given User Has Registered Unsuccesfully
    When User Logs In
    Then Login Page Should Be Open
    And Page Should Contain
    ...    Invalid username or password

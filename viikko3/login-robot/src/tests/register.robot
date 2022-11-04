*** Settings ***
Resource      resource.robot
Force Tags    register

*** Test Cases ***
Register With Valid Username And Password
    Given Username arhippa
    And Password Qwerty12345
    When User Registers To The App
    Then Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    [Setup]    Create User    arhippa    Qwerty98765
    Given Username arhippa
    And Password Qwerty12345
    When User Registers To The App
    Then Output Should Contain
    ...    User with username arhippa already exists

Register With Too Short Username And Valid Password
    Given Username ye
    And Password Qwerty12345
    When User Registers To The App
    Then Output Should Contain
    ...    Username must contain at least 3 characters a-z

Register With Valid Username And Too Short Password
    Given Username arhippa
    And Password Qwer345
    When User Registers To The App
    Then Output Should Contain
    ...    Password must contain at least 8 characters with some non-letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Given Username arhippa
    And Password QwertyASDF
    When User Registers To The App
    Then Output Should Contain
    ...    Password must contain at least 8 characters with some non-letters

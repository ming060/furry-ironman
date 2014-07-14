*** Settings ***
Documentation     This demo project is aim to help you start with uiautomatorlibrary.
Library           uiautomatorlibrary

*** Test Cases ***
test
    # Install F-Droid
    Install    ${CURDIR}${/}FDroid.apk
    # Open the Application through adb command
    Execute Adb Shell Command    am start -W org.fdroid.fdroid/org.fdroid.fdroid.FDroid
    # Wait loading over
    ${is_loading_over}    Wait Until Gone    30000    text=Please Wait
    Should Be True    ${is_loading_over}    Loading over 10 seconds.
    # Check F-Droid text
    ${is_text_exist}    Wait For Exists    3000    text=F-Droid
    Should Be True    ${is_text_exist}    Text does not exist.
    [Teardown]    Run keywords    Run Keyword If Test Failed    Screenshot    AND    Uninstall

*** Keywords ***
Uninstall
    #Uninstall the Application
    uiautomatorlibrary.Uninstall    org.fdroid.fdroid

*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
At start there are no references
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Page Should Contain  things still unfinished: 0

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  Create new reference
    Input Text  content  Buy milk
    Click Button  Create
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk

After adding two references and marking one done, there is one unfinished
    Go To  ${HOME_URL}
    Click Link  Create new reference
    Input Text  content  Buy milk
    Click Button  Create
    Click Link  Create new reference
    Input Text  content  Clean house
    Click Button  Create
    Click Button  //li[div[contains(text(), 'Buy milk')]]/form/button
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk, done
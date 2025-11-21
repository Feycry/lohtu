*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Reset database
    Reset References

Saving a reference shows on index
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Click Link  Create new reference
    Input Text  name:author     Test Author
    Input Text  name:title      Test Title
    Input Text  name:booktitle  Test Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Reference app
    Page Should Contain  Test Title
    Page Should Contain  Test Author

Deleting a reference removes it from index
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Click Button  Delete reference
    Alert Should Be Present  Confrim deletion of reference
    Page Should Not Contain  Author


Saving a reference with too short title
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Click Link  Create new reference
    Input Text  name:author     Test Author
    Input Text  name:title      a
    Input Text  name:booktitle  Test Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Create a new reference
    Page Should Contain  Reference title length must be greater than 1


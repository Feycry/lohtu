*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Search filters references by query
    Reset References
    Go To  ${HOME_URL}
    Title Should Be  Reference app


    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Input Text  name:author     Test Author
    Input Text  name:title      Test Title
    Input Text  name:booktitle  Test
    Input Text  name:year       2024
    Click Button  Create
    Page Should Contain  Test Title
    Page Should Contain  Test Author

    Select From List By Label    name:reference_type    @article
    Click Button  Create new reference
    Input Text  name:author     Do not appear in search
    Input Text  name:title      Should not appear in filter search
    Input Text  name:journal    Journal
    Input Text  name:year       2023
    Click Button  Create
    Page Should Contain  Should not appear in filter search
    Page Should Contain  Do not appear in search


    Input Text    name:q    Test
    Click Button  xpath=//form[contains(@class,'search')]//button

    Page Should Contain    Test Title
    Page Should Contain    Test Author
    Page Should Not Contain    Should not appear in filter search
    Page Should Not Contain    Do not appear in search

    Click Link    Clear
    Page Should Contain    Test Title
    Page Should Contain    Should not appear in filter search

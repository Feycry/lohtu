*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Delete Reference Removes It From List
    Reset References
    Go To    ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @article
    Click Button  Create new reference
    Wait Until Page Contains    Create a new reference
    Input Text    id=author    Delete Author
    Input Text    id=title     To Be Deleted
    Input Text    id=journal   Del Journal
    Input Text    id=year      2023
    Click Button    Create
    Go To    ${HOME_URL}/
    Wait Until Page Contains    To Be Deleted
    Click Element    xpath=//li[.//text()[contains(.,'To Be Deleted')]]//button[contains(.,'Delete')]
    Run Keyword And Ignore Error    Handle Alert    ACCEPT
    Wait Until Page Does Not Contain    To Be Deleted

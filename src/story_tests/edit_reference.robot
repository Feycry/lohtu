*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Edit Existing Reference Updates Year
    Reset References
    Go To    ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Wait Until Page Contains    Create a new reference
    Input Text    id=author    Edit Author
    Input Text    id=title     Editable Title
    Input Text    id=booktitle    Edit Book
    Input Text    id=year      2024
    Click Button    Create
    Go To    ${HOME_URL}/
    Wait Until Page Contains    Editable Title
    Click Element    xpath=//li[.//text()[contains(.,'Editable Title')]]//button[contains(.,'Edit')]
    Wait Until Page Contains    Edit reference
    Clear Element Text    id=year
    Input Text    id=year    2025
    Click Button    Update
    Wait Until Page Contains    Editable Title
    Click Element    xpath=//li[.//text()[contains(.,'Editable Title')]]//div[contains(@class,'frontpage-references')]
    Wait Until Page Contains    year = {2025}

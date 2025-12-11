*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Export Selected Produces BibTeX For Checked Items
    Reset References
    Go To    ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button     Create new reference
    Wait Until Page Contains    Create a new reference
    Input Text    id=author    Sel Author
    Input Text    id=title     Selected Paper
    Input Text    id=booktitle    SelConf
    Input Text    id=year      2024
    Click Button  Create 
    Go To    ${HOME_URL}
    Title Should Be      Reference app
    Select From List By Label    name:reference_type    @article
    Click Button    Create new reference
    Wait Until Page Contains    Create a new reference
    Input Text    id=author    Other Author
    Input Text    id=title     Other Paper
    Input Text    id=journal    Other Journal
    Input Text    id=year      2023
    Click Button    Create
    Go To    ${HOME_URL}/
    Wait Until Page Contains    Selected Paper
    Wait Until Page Contains    Other Paper
    Click Element    xpath=//li[.//text()[contains(.,'Selected Paper')]]//input[@type='checkbox' and @name='reference_id']
    ${is_checked}=    Run Keyword And Return Status    Element Should Be Selected    xpath=//li[.//text()[contains(.,'Other Paper')]]//input[@type='checkbox' and @name='reference_id']
    Run Keyword If    ${is_checked}    Click Element    xpath=//li[.//text()[contains(.,'Other Paper')]]//input[@type='checkbox' and @name='reference_id']
    Click Button    Export selected to bibtex
    Wait Until Page Contains    @
    Page Should Contain    @inproceedings{
    Page Should Contain    author = {Sel Author}
    Page Should Contain    title = {Selected Paper}
    Page Should Not Contain    title = {Other Paper}

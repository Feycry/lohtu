*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Reset database
    Reset References

Export all to BibTeX
    Go To  ${HOME_URL}
    Title Should Be    Reference app
    Click Button    Export all to bibtex
    Wait Until Page Contains    @


    
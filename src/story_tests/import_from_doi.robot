*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Importing reference from DOI populates required fields and creates reference
    Reset References
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    
    Input Text  id:doi_lookup    10.1002/j.1538-7305.1948.tb01338.x
    Click Button  Import from DOI
    
    Title Should Be  Create a new reference
    
    Textfield Value Should Be  name:author     Shannon, C. E.
    Textfield Value Should Be  name:title      A Mathematical Theory of Communication
    Textfield Value Should Be  name:journal    Bell System Technical Journal
    Textfield Value Should Be  name:year       1948
    
    Click Button  Create
    
    Title Should Be  Reference app
    Page Should Contain  A Mathematical Theory of Communication
    Page Should Contain  Shannon, C. E.

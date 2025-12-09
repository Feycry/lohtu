*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Importing reference from DOI populates required fields and creates reference
    Reset References
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    
    Input Text  id:doi_lookup    10.1007/s13187-020-01751-z
    Click Button  Import from DOI
    
    Title Should Be  Create a new reference
    
    Textfield Value Should Be  name:author     Busse, Clara and August, Ella
    Textfield Value Should Be  name:title      How to Write and Publish a Research Paper for a Peer-Reviewed Journal
    Textfield Value Should Be  name:journal    Journal of Cancer Education
    Textfield Value Should Be  name:year       2020
    
    Click Button  Create
    
    Title Should Be  Reference app
    Page Should Contain  How to Write and Publish a Research Paper for a Peer-Reviewed Journal
    Page Should Contain  Busse, Clara and August, Ella

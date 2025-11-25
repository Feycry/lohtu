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
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
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
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Input Text  name:author     Test Author
    Input Text  name:title      a
    Input Text  name:booktitle  Test Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Create a new reference
    Page Should Contain  Reference title length must be greater than 1

Saving a reference with too long title
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Input Text  name:author     Long Author
    Input Text  name:title      ${long_title}
    Input Text  name:booktitle  Long Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Create a new reference
    Page Should Contain  Reference title length must be less than 100

Saving a reference after editing works
    Go To  ${HOME_URL}
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Input Text  name:author     Test Author
    Input Text  name:title      Test Title
    Input Text  name:booktitle  Test Book
    Input Text  name:year       2024
    Click Button  Create
    Click Button  Edit reference
    Title Should Be  Edit reference
    Input Text  name:year  2025
    Click Button  Update
    Page Should Contain  Year: 2025

Canceling changes works
    Reset References
    Go To  ${HOME_URL}
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Input Text  name:author     Test Author
    Input Text  name:title      Test Title
    Input Text  name:booktitle  Test Book
    Input Text  name:year       2024
    Click Button  Create
    Click Button  Edit reference
    Title Should Be  Edit reference
    Input Text  name:year  2025
    Click Link  Cancel
    Page Should Not Contain  Year: 2025
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
    # Ensure hidden reference_type is set to avoid timing issues in CI
    Execute JavaScript    document.querySelector('input[name="reference_type"]').value = 'inproceedings';
    Click Button  Create
    Title Should Be  Reference app
    Page Should Contain  Test Title
    Page Should Contain  Test Author

Deleting a reference removes it from index
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Click Button  Delete 
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
    Click Button  Edit
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
    Click Button  Edit
    Title Should Be  Edit reference
    Input Text  name:year  2025
    Click Link  Cancel
    Page Should Not Contain  Year: 2025

Creating inproceedings without author (required)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:title      Missing Author Title
    Input Text  name:booktitle  Conf Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Create a new reference

Creating inproceedings without booktitle (required)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:author     Missing Book Author
    Input Text  name:title      Missing Book Title
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Create a new reference

Creating inproceedings without year (required)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:author     Missing Year Author
    Input Text  name:title      Missing Year Title
    Input Text  name:booktitle  Conf Book
    Click Button  Create
    Title Should Be  Create a new reference

Creating article without journal (required)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @article
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:author     Article Author
    Input Text  name:title      Article Title
    Input Text  name:year       2025
    Click Button  Create
    Title Should Be  Create a new reference

Creating book without publisher (required)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @book
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:author     Book Author
    Input Text  name:title      Book Title
    Input Text  name:year       2022
    Click Button  Create
    Title Should Be  Create a new reference

Creating mastersthesis without school (required)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @mastersthesis
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:author     Thesis Author
    Input Text  name:title      Thesis Title
    Input Text  name:year       2021
    Click Button  Create
    Title Should Be  Create a new reference

Creating inproceedings with spaces-only title (invalid)
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Title Should Be  Create a new reference
    Input Text  name:author     Author
    Input Text  name:title      ${SPACE}
    Input Text  name:booktitle  Conf Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Create a new reference
    Page Should Contain  Title cannot be empty or whitespace only

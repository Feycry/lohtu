*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Copy Bibtex to Clipboard
    Reset References
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Select From List By Label    name:reference_type    @inproceedings
    Click Button  Create new reference
    Input Text  name:author     Clipboard Author
    Input Text  name:title      Clipboard Title
    Input Text  name:booktitle  Clipboard Book
    Input Text  name:year       2024
    Click Button  Create
    Title Should Be  Reference app
    Execute JavaScript    window.__copied = null; const orig = navigator.clipboard.writeText; navigator.clipboard.writeText = (t) => { window.__copied = t; return Promise.resolve(); };
    Click Button  Copy bibtex
    ${clipboard_content}=    Execute JavaScript    return window.__copied
    Should Contain    ${clipboard_content}    author = {Clipboard Author}



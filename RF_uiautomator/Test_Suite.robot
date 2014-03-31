*** Test Cases ***
Test_Case
    print_info
    ${obj}    get_object    Chrome
    Call Method    ${obj}    info
    Example Keyword    a=A    b=B

# robotframework-netaddr
[![PyPi license](https://img.shields.io/pypi/l/robotframework-netaddr.svg)](https://pypi.python.org/pypi/robotframework-netaddr)
[![PyPi downloads](https://img.shields.io/pypi/dm/robotframework-netaddr.svg)](https://pypi.python.org/pypi/robotframework-netaddr)
[![Latest Version](https://img.shields.io/pypi/v/robotframework-netaddr.svg)](https://pypi.python.org/pypi/robotframework-netaddr)

### Description
Provides a class which wraps much of the netaddr (https://netaddr.readthedocs.io/en/latest/introduction.html) library functionality.

The wrapped functions are accesible within Robot Framework and can be used there as keywords.

### Documentation
Keyword documentation can be found here: https://github.com/nkeulen/robotframework-netaddr/blob/master/documentation.md

### How to install
The package can be installed using pip:
```bash
pip install robotframework-netaddr
```

### How to use in robotframework
A quick demonstration of how this library can be used in robotframework:
```robotframework
*** Settings ***
Library    RobotFrameworkNetAddr

*** Test Cases ***
My Test Case
    # Check if an IP address is part of a subnet:
    ${subnet}    Set Variable    10.10.10.0/24
    ${ip}    Set Variable    10.10.10.123
    ${ip_in_subnet}    IPAddress In Network    ${ip}    ${subnet}
    Run Keyword If    ${ip_in_subnet}
    ...    Log To Console    \n${ip} is in ${subnet}    ELSE
    ...    Log To Console    \n${ip} is not in ${subnet}
    # Check a subnet mask:
    ${netmask}    IPNetwork Netmask    ${subnet}
    Should Be Equal As Strings    ${netmask}    255.255.255.0
```
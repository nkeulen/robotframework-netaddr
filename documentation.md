# robotframework-netaddr

## Importing the library
```robotframework
*** Settings ***
Library    RobotFrameworkNetAddr
```

## Keyword documentation
### ipnetwork broadcast
Returns the broadcast address of the given subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork cidr
Returns the network in cidr format.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask) |  10.0.0.0/255.255.255.0   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork hostmask
Returns the hostmask.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork info
Returns a dict with info about the network.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork ip
Returns the ip part the IPNetwork object.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is link local
Check if the address is a link local address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is loopback
Check if the address is a loopback address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is multicast
Check if the address is a multicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is private
Check if the address is a private address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is reserved
Check if the address is a reserved address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is unicast
Check if the address is a unicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork netmask
Returns the subnetmask of the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork network
Returns the network address of the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork prefixlen
Returns the prefix length of the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork size
Returns the number of addresses in the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork version
Returns the IP version of the network (4 or 6).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is network addr
Returns if the provided addr is the network address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork is valid ipv4
Returns if the provided addr is valid for IPv4.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options, should not contain the version keyword  |  - |  -   |



### ipnetwork is valid ipv6
Returns if the provided addr is valid for IPv6.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  fe80::1/48   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options, should not contain the version keyword  |  - |  -   |



### ipnetwork previous
Returns subnet one lower than the one provided with addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork next
Returns subnet one higher than the one provided with addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork in network
Checks if network addr2 overlaps with in addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| addr2 | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs_addr1 | passed to IPNetwork constructor for addr1, see netaddr docs for options  |  - |  -   |
| kwargs_addr2 | passed to IPNetwork constructor for addr2, see netaddr docs for options  |  - |  -   |


### ipaddress bin
Returns ip in binary.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress bits
Returns ip series of bits grouped together in octets (ipv4) or hextets (ipv6).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress info
Returns a dict with info about the IP address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is hostmask
Checks if the IP address is a hostmask.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is link local
Checks if the IP address is a link local address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is loopback
Checks if the IP address is a loopback address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is multicast
Checks if the IP address is a multicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is netmask
Checks if the IP address is a netmask.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is private
Checks if the IP address is a private address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is reserved
Checks if the IP address is a reserved address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is unicast
Checks if the IP address is a unicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress reverse dns
Returns a reverse dns notation of the IP address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress version
Returns the IP version of the IP address (4 or 6).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress words
Returns a octets (IPv4) or hextets (IPv6) set of decimal values.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress add
Add a number to an IP address to get a higher or lower (if provided with a negative amount) IP.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| amount | the amount to add |  10   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is valid ipv4
Checks if addr is a valid IPv4 address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress is valid ipv6
Checks if addr is a valid IPv6 address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  fe80::1   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress in network
Checks if addr is in subnet netw.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.200   |  -   |
| netw | the network |  10.0.0.0/24   |  -   |


### eui bin
Returns addr in binary.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui bits
Returns addr in grouped bits.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui ei
Returns the addr's EI part.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui eui64
Returns the addr's EUI64.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui iab
Returns the addr's IAB (if available).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui info
Returns a dict with info on the addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui ipv6
Returns an IPv6 address by combining a provided IPv6 prefix with this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| prefix | ipv6 prefix in hex |  0xfc000000000000000000000000000000  |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui ipv6 link local
Returns an IPv6 link local address based on this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui is iab
Check if the addr is IAB.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui modified eui64
Returns modified eui64 of this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui oui
Returns the OUI of this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui packed
Returns the addr in packed format.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui value
Returns the value of the addr in decimal.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui version
Returns the version of the addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui words
Returns addr in a set of decimal values.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui is valid
Returns if addr is a valid MAC address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |


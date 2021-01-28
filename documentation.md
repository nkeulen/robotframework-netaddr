# robotframework-netaddr
### keyword documentation
#  
#  
---
#  
#  
### ipnetwork_broadcast
Returns the broadcast address of the given subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_cidr
Returns the network in cidr format.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask) |  10.0.0.0/255.255.255.0   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_hostmask
Returns the hostmask.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_info
Returns a dict with info about the network.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_ip
Returns the ip part the IPNetwork object.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_link_local
Check if the address is a link local address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_loopback
Check if the address is a loopback address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_multicast
Check if the address is a multicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_private
Check if the address is a private address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_reserved
Check if the address is a reserved address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_unicast
Check if the address is a unicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_netmask
Returns the subnetmask of the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_network
Returns the network address of the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_prefixlen
Returns the prefix length of the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_size
Returns the number of addresses in the subnet.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_version
Returns the IP version of the network (4 or 6).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_network_addr
Returns if the provided addr is the network address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_is_valid_ipv4
Returns if the provided addr is valid for IPv4.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options, should not contain the version keyword  |  - |  -   |



### ipnetwork_is_valid_ipv6
Returns if the provided addr is valid for IPv6.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  fe80::1/48   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options, should not contain the version keyword  |  - |  -   |



### ipnetwork_previous
Returns subnet one lower than the one provided with addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_next
Returns subnet one higher than the one provided with addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs | passed to IPNetwork constructor, see netaddr docs for options  |  - |  -   |


### ipnetwork_in_network
Checks if network addr2 overlaps with in addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| addr2 | address (ip/mask or prefixlen) |  10.0.0.0/24   |  -   |
| kwargs_addr1 | passed to IPNetwork constructor for addr1, see netaddr docs for options  |  - |  -   |
| kwargs_addr2 | passed to IPNetwork constructor for addr2, see netaddr docs for options  |  - |  -   |


### ipaddress_bin
Returns ip in binary.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_bits
Returns ip series of bits grouped together in octets (ipv4) or hextets (ipv6).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_info
Returns a dict with info about the IP address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_hostmask
Checks if the IP address is a hostmask.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_link_local
Checks if the IP address is a link local address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_loopback
Checks if the IP address is a loopback address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_multicast
Checks if the IP address is a multicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_netmask
Checks if the IP address is a netmask.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_private
Checks if the IP address is a private address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_reserved
Checks if the IP address is a reserved address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_unicast
Checks if the IP address is a unicast address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_reverse_dns
Returns a reverse dns notation of the IP address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_version
Returns the IP version of the IP address (4 or 6).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_words
Returns a octets (IPv4) or hextets (IPv6) set of decimal values.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_add
Add a number to an IP address to get a higher or lower (if provided with a negative amount) IP.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| amount | the amount to add |  10   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_valid_ipv4
Checks if addr is a valid IPv4 address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.0   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_is_valid_ipv6
Checks if addr is a valid IPv6 address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  fe80::1   |  -   |
| kwargs | passed to IPAddress constructor, see netaddr docs for options  |  - |  -   |


### ipaddress_in_network
Checks if addr is in subnet netw.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the IP address |  10.0.0.200   |  -   |
| netw | the network |  10.0.0.0/24   |  -   |


### eui_bin
Returns addr in binary.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_bits
Returns addr in grouped bits.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_ei
Returns the addr's EI part.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_eui64
Returns the addr's EUI64.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_iab
Returns the addr's IAB (if available).

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_info
Returns a dict with info on the addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_ipv6
Returns an IPv6 address by combining a provided IPv6 prefix with this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| prefix | ipv6 prefix in hex |  0xfc000000000000000000000000000000  |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_ipv6_link_local
Returns an IPv6 link local address based on this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_is_iab
Check if the addr is IAB.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_modified_eui64
Returns modified eui64 of this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_oui
Returns the OUI of this addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_packed
Returns the addr in packed format.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_value
Returns the value of the addr in decimal.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_version
Returns the version of the addr.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_words
Returns addr in a set of decimal values.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |
| kwargs | passed to EUI constructor, see netaddr docs for options  |  - |  -   |


### eui_is_valid
Returns if addr is a valid MAC address.

*Arguments*
| argument | Description |  Example  |  Default value
| :------------- | :----------: | -----------: | -----------: |
| addr | the mac address |  00-01-02-AA-BB-CC   |  -   |


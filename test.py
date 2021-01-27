from robotframework_netaddr import RobotFrameworkNetAddr

def main():

    print("\n=== IPNetwork ===\n")

    addr = '10.20.30.40/24'
    addr6 = '2001:2:3::400/48'

    print('broadcast')
    print(RobotFrameworkNetAddr.ipnetwork_broadcast(addr))
    print(RobotFrameworkNetAddr.ipnetwork_broadcast(addr6))
    print('')

    print('cidr')
    print(RobotFrameworkNetAddr.ipnetwork_cidr(addr))
    print(RobotFrameworkNetAddr.ipnetwork_cidr(addr6))
    print('')

    print('hostmask')
    print(RobotFrameworkNetAddr.ipnetwork_hostmask(addr))
    print(RobotFrameworkNetAddr.ipnetwork_hostmask(addr6))
    print('')

    print('info')
    print(RobotFrameworkNetAddr.ipnetwork_info(addr))
    print(RobotFrameworkNetAddr.ipnetwork_info(addr6))
    print('')

    print('ip')
    print(RobotFrameworkNetAddr.ipnetwork_ip(addr))
    print(RobotFrameworkNetAddr.ipnetwork_ip(addr6))
    print('')

    print('is_link_local')
    print(RobotFrameworkNetAddr.ipnetwork_is_link_local(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_link_local(addr6))
    print('')

    print('is_loopback')
    print(RobotFrameworkNetAddr.ipnetwork_is_loopback(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_loopback(addr6))
    print('')

    print('is_multicast')
    print(RobotFrameworkNetAddr.ipnetwork_is_multicast(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_multicast(addr6))
    print('')

    print('is_private')
    print(RobotFrameworkNetAddr.ipnetwork_is_private(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_private(addr6))
    print('')

    print('is_reserved')
    print(RobotFrameworkNetAddr.ipnetwork_is_reserved(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_reserved(addr6))
    print('')

    print('is_unicast')
    print(RobotFrameworkNetAddr.ipnetwork_is_unicast(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_unicast(addr6))
    print('')

    print('netmask')
    print(RobotFrameworkNetAddr.ipnetwork_netmask(addr))
    print(RobotFrameworkNetAddr.ipnetwork_netmask(addr6))
    print('')

    print('network')
    print(RobotFrameworkNetAddr.ipnetwork_network(addr))
    print(RobotFrameworkNetAddr.ipnetwork_network(addr6))
    print('')

    print('prefixlen')
    print(RobotFrameworkNetAddr.ipnetwork_prefixlen(addr))
    print(RobotFrameworkNetAddr.ipnetwork_prefixlen(addr6))
    print('')

    print('size')
    print(RobotFrameworkNetAddr.ipnetwork_size(addr))
    print(RobotFrameworkNetAddr.ipnetwork_size(addr6))
    print('')

    print('version')
    print(RobotFrameworkNetAddr.ipnetwork_version(addr))
    print(RobotFrameworkNetAddr.ipnetwork_version(addr6))
    print('')

    print('is_network_addr')
    print(RobotFrameworkNetAddr.ipnetwork_is_network_addr(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_network_addr(addr6))
    print('')

    print('is_valid_ipv4')
    print(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv4(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv4(addr6))
    print('')

    print('is_valid_ipv6')
    print(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv6(addr))
    print(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv6(addr6))
    print('')

    print("\n=== IPAddress ===\n")

    addr = '10.20.30.40'
    addr6 = '2001:2:3::400'

    print('bin')
    print(RobotFrameworkNetAddr.ipaddress_bin(addr))
    print(RobotFrameworkNetAddr.ipaddress_bin(addr6))
    print('')

    print('bits')
    print(RobotFrameworkNetAddr.ipaddress_bits(addr))
    print(RobotFrameworkNetAddr.ipaddress_bits(addr6))
    print('')

    print('info')
    print(RobotFrameworkNetAddr.ipaddress_info(addr))
    print(RobotFrameworkNetAddr.ipaddress_info(addr6))
    print('')

    print('is_hostmask')
    print(RobotFrameworkNetAddr.ipaddress_is_hostmask(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_hostmask(addr6))
    print('')

    print('is_link_local')
    print(RobotFrameworkNetAddr.ipaddress_is_link_local(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_link_local(addr6))
    print('')

    print('is_loopback')
    print(RobotFrameworkNetAddr.ipaddress_is_loopback(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_loopback(addr6))
    print('')

    print('is_multicast')
    print(RobotFrameworkNetAddr.ipaddress_is_multicast(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_multicast(addr6))
    print('')

    print('is_netmask')
    print(RobotFrameworkNetAddr.ipaddress_is_netmask(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_netmask(addr6))
    print('')

    print('is_private')
    print(RobotFrameworkNetAddr.ipaddress_is_private(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_private(addr6))
    print('')

    print('is_reserved')
    print(RobotFrameworkNetAddr.ipaddress_is_reserved(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_reserved(addr6))
    print('')

    print('is_unicast')
    print(RobotFrameworkNetAddr.ipaddress_is_unicast(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_unicast(addr6))
    print('')

    print('reverse_dns')
    print(RobotFrameworkNetAddr.ipaddress_reverse_dns(addr))
    print(RobotFrameworkNetAddr.ipaddress_reverse_dns(addr6))
    print('')

    print('version')
    print(RobotFrameworkNetAddr.ipaddress_version(addr))
    print(RobotFrameworkNetAddr.ipaddress_version(addr6))
    print('')

    print('add')
    print(RobotFrameworkNetAddr.ipaddress_add(addr, 10))
    print(RobotFrameworkNetAddr.ipaddress_add(addr6, 10))
    print('')

    print('words')
    print(RobotFrameworkNetAddr.ipaddress_words(addr))
    print(RobotFrameworkNetAddr.ipaddress_words(addr6))
    print('')

    print('is_valid_ipv4')
    print(RobotFrameworkNetAddr.ipaddress_is_valid_ipv4(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_valid_ipv4(addr6))
    print('')

    print('is_valid_ipv6')
    print(RobotFrameworkNetAddr.ipaddress_is_valid_ipv6(addr))
    print(RobotFrameworkNetAddr.ipaddress_is_valid_ipv6(addr6))
    print('')

    print("\n=== EUI ===\n")

    addr = '00-1B-77-49-54-FD'

    print('bin')
    print(RobotFrameworkNetAddr.eui_bin(addr))
    print('')

    print('bits')
    print(RobotFrameworkNetAddr.eui_bits(addr))
    print('')

    print('ei')
    print(RobotFrameworkNetAddr.eui_ei(addr))
    print('')

    print('eui64')
    print(RobotFrameworkNetAddr.eui_eui64(addr))
    print('')

    print('iab')
    print(RobotFrameworkNetAddr.eui_iab(addr))
    print('')

    print('info')
    print(RobotFrameworkNetAddr.eui_info(addr))
    print('')

    print('ipv6')
    print(RobotFrameworkNetAddr.eui_ipv6(addr, 0x20010000000000000000000000000000))
    print('')

    print('ipv6_link_local')
    print(RobotFrameworkNetAddr.eui_ipv6_link_local(addr))
    print('')

    print('is_iab')
    print(RobotFrameworkNetAddr.eui_is_iab(addr))
    print('')

    print('modified_eui64')
    print(RobotFrameworkNetAddr.eui_modified_eui64(addr))
    print('')

    print('oui')
    print(RobotFrameworkNetAddr.eui_oui(addr))
    print('')

    print('packed')
    print(RobotFrameworkNetAddr.eui_packed(addr))
    print('')

    print('value')
    print(RobotFrameworkNetAddr.eui_value(addr))
    print('')

    print('version')
    print(RobotFrameworkNetAddr.eui_version(addr))
    print('')

    print('words')
    print(RobotFrameworkNetAddr.eui_words(addr))
    print('')

    print('is_valid')
    print(RobotFrameworkNetAddr.is_valid(addr))
    print(RobotFrameworkNetAddr.is_valid('totallynotvalid'))
    print('')


if __name__ == '__main__':
    main()

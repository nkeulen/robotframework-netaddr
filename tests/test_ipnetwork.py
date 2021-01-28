import unittest
import sys
import os

sys.path.append(os.path.abspath("../src/RobotFrameworkNetAddr"))
from robotframeworknetaddr import RobotFrameworkNetAddr


class TestIPNetwork(unittest.TestCase):

    def test_ipnetwork_ipv4(self):
        # setup variables used in testing:
        priv_ipv4_ip = '10.20.30.40'
        priv_ipv4_cidr = '10.20.30.40/22'
        priv_ipv4_netmask = '255.255.252.0'
        priv_ipv4_hostmask = '0.0.3.255'
        priv_ipv4_netmask_form = '10.20.30.40/255.255.252.0'
        priv_ipv4_net = '10.20.28.0'
        priv_ipv4_net_cidr = '10.20.28.0/22'
        priv_ipv4_bc = '10.20.31.255'
        priv_ipv4_prefixlen = '22'
        priv_ipv4_size = '1024'
        ipv4_version = '4'
        pub_ipv4_cidr = '8.8.8.8/24'
        reserved_ipv4 = '240.0.0.1/24'
        link_local_ipv4 = '169.254.0.0/16'
        multicast_ipv4 = '239.0.0.0/8'
        loopback_ipv4 = '127.0.0.0/8'
        invalid_ipv4 = ['300.400.500.600/33', '10.20.30.40/33', 'abcd']

        # run the actual tests:
        bc = RobotFrameworkNetAddr.ipnetwork_broadcast(priv_ipv4_cidr)
        self.assertEqual(str(bc), priv_ipv4_bc)

        cidr = RobotFrameworkNetAddr.ipnetwork_cidr(priv_ipv4_netmask_form)
        self.assertEqual(str(cidr), priv_ipv4_net_cidr)

        hostmask = RobotFrameworkNetAddr.ipnetwork_hostmask(priv_ipv4_netmask_form)
        self.assertEqual(str(hostmask), priv_ipv4_hostmask)

        ip = RobotFrameworkNetAddr.ipnetwork_ip(priv_ipv4_cidr)
        self.assertEqual(str(ip), priv_ipv4_ip)

        net = RobotFrameworkNetAddr.ipnetwork_network(priv_ipv4_cidr)
        self.assertEqual(str(net), priv_ipv4_net)

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_link_local(priv_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_link_local(link_local_ipv4))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_loopback(priv_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_loopback(loopback_ipv4))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_multicast(priv_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_multicast(multicast_ipv4))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_network_addr(priv_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_network_addr(priv_ipv4_net_cidr))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_private(pub_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_private(priv_ipv4_cidr))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_reserved(pub_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_reserved(reserved_ipv4))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_unicast(multicast_ipv4))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_unicast(priv_ipv4_cidr))

        for invalid in invalid_ipv4:
            self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv4(invalid))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv4(priv_ipv4_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv4(pub_ipv4_cidr))

        netmask = RobotFrameworkNetAddr.ipnetwork_netmask(priv_ipv4_cidr)
        self.assertEqual(str(netmask), priv_ipv4_netmask)

        prefixlen = RobotFrameworkNetAddr.ipnetwork_prefixlen(priv_ipv4_cidr)
        self.assertEqual(str(prefixlen), priv_ipv4_prefixlen)

        size = RobotFrameworkNetAddr.ipnetwork_size(priv_ipv4_cidr)
        self.assertEqual(str(size), priv_ipv4_size)

        version = RobotFrameworkNetAddr.ipnetwork_version(pub_ipv4_cidr)
        self.assertEqual(str(version), ipv4_version)

    def test_ipnetwork_ipv6(self):
        # setup variables used in testing:
        priv_ipv6_ip = 'fc00:1:2:3::400'
        priv_ipv6_cidr = 'fc00:1:2:3::400/54'
        priv_ipv6_netmask = 'ffff:ffff:ffff:fc00::'
        priv_ipv6_hostmask = '::3ff:ffff:ffff:ffff:ffff'
        priv_ipv6_netmask_form = 'fc00:1:2:3::400/ffff:ffff:ffff:fc00::'
        priv_ipv6_net = 'fc00:1:2::'
        priv_ipv6_net_cidr = 'fc00:1:2::/54'
        priv_ipv6_bc = 'fc00:1:2:3ff:ffff:ffff:ffff:ffff'
        priv_ipv6_prefixlen = '54'
        priv_ipv6_size = '18889465931478580854784'
        ipv6_version = '6'
        pub_ipv6_cidr = '2001:4860:4860::8888/48'
        reserved_ipv6 = '0::/48'
        link_local_ipv6 = 'fe80::/10'
        multicast_ipv6 = 'ff00::/8'
        invalid_ipv6 = ['fc00::1/210', '10.20.30.40/33', 'abcdefghjk']

        # run the actual tests:
        bc = RobotFrameworkNetAddr.ipnetwork_broadcast(priv_ipv6_cidr)
        self.assertEqual(str(bc), priv_ipv6_bc)

        cidr = RobotFrameworkNetAddr.ipnetwork_cidr(priv_ipv6_netmask_form)
        self.assertEqual(str(cidr), priv_ipv6_net_cidr)

        hostmask = RobotFrameworkNetAddr.ipnetwork_hostmask(priv_ipv6_netmask_form)
        self.assertEqual(str(hostmask), priv_ipv6_hostmask)

        ip = RobotFrameworkNetAddr.ipnetwork_ip(priv_ipv6_cidr)
        self.assertEqual(str(ip), priv_ipv6_ip)

        net = RobotFrameworkNetAddr.ipnetwork_network(priv_ipv6_cidr)
        self.assertEqual(str(net), priv_ipv6_net)

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_link_local(priv_ipv6_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_link_local(link_local_ipv6))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_multicast(priv_ipv6_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_multicast(multicast_ipv6))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_network_addr(priv_ipv6_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_network_addr(priv_ipv6_net_cidr))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_private(pub_ipv6_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_private(priv_ipv6_cidr))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_reserved(pub_ipv6_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_reserved(reserved_ipv6))

        self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_unicast(multicast_ipv6))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_unicast(priv_ipv6_cidr))

        for invalid in invalid_ipv6:
            self.assertFalse(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv6(invalid))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv6(priv_ipv6_cidr))
        self.assertTrue(RobotFrameworkNetAddr.ipnetwork_is_valid_ipv6(pub_ipv6_cidr))

        netmask = RobotFrameworkNetAddr.ipnetwork_netmask(priv_ipv6_cidr)
        self.assertEqual(str(netmask), priv_ipv6_netmask)

        prefixlen = RobotFrameworkNetAddr.ipnetwork_prefixlen(priv_ipv6_cidr)
        self.assertEqual(str(prefixlen), priv_ipv6_prefixlen)

        size = RobotFrameworkNetAddr.ipnetwork_size(priv_ipv6_cidr)
        self.assertEqual(str(size), priv_ipv6_size)

        version = RobotFrameworkNetAddr.ipnetwork_version(pub_ipv6_cidr)
        self.assertEqual(str(version), ipv6_version)

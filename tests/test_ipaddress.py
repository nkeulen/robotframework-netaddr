import unittest
import sys
import os

sys.path.append(os.path.abspath("../src/RobotFrameworkNetAddr"))
from robotframeworknetaddr import RobotFrameworkNetAddr


class TestIPAddress(unittest.TestCase):

    def test_ipaddress_ipv4(self):
        priv_ipv4_ip = '10.20.30.40'
        priv_ipv4_ip_plus_512 = '10.20.32.40'
        priv_ipv4_ip_min_1 = '10.20.30.39'
        priv_ipv4_reverse_dns = '40.30.20.10.in-addr.arpa.'
        pub_ipv4_ip = '8.8.8.8'
        reserved_ipv4 = '240.0.0.1'
        link_local_ipv4 = '169.254.0.1'
        multicast_ipv4 = '239.0.0.1'
        loopback_ipv4 = '127.0.0.1'
        invalid_ipv4 = ['300.400.500.600', 'abcd']

        ip_plus_512 = RobotFrameworkNetAddr.ipaddress_add(priv_ipv4_ip, 512)
        self.assertEqual(str(ip_plus_512), priv_ipv4_ip_plus_512)
        ip_min_1 = RobotFrameworkNetAddr.ipaddress_add(priv_ipv4_ip, -1)
        self.assertEqual(str(ip_min_1), priv_ipv4_ip_min_1)

        self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_link_local(priv_ipv4_ip))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_link_local(link_local_ipv4))

        self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_multicast(priv_ipv4_ip))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_multicast(multicast_ipv4))

        self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_loopback(priv_ipv4_ip))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_loopback(loopback_ipv4))

        rev_dns = RobotFrameworkNetAddr.ipaddress_reverse_dns(priv_ipv4_ip)
        self.assertEqual(str(rev_dns), priv_ipv4_reverse_dns)

        for invalid in invalid_ipv4:
            self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_valid_ipv4(invalid))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_valid_ipv4(pub_ipv4_ip))

    def test_ipaddress_ipv6(self):
        priv_ipv6_ip = 'fc00:1:2:3::400'
        priv_ipv6_ip_plus_1 = 'fc00:1:2:3::401'
        priv_ipv6_ip_min_1 = 'fc00:1:2:3::3ff'
        priv_ipv6_reverse_dns = '0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.3.0.0.0.2.0.0.0.1.0.0.0.0.0.c.f.ip6.arpa.'
        ipv6_version = '6'
        link_local_ipv6 = 'fe80::1'
        multicast_ipv6 = 'ff00::1'
        loopback_ipv6 = "::1"

        ip_plus_1 = RobotFrameworkNetAddr.ipaddress_add(priv_ipv6_ip, 1)
        self.assertEqual(str(ip_plus_1), priv_ipv6_ip_plus_1)
        ip_min_1 = RobotFrameworkNetAddr.ipaddress_add(priv_ipv6_ip, -1)
        self.assertEqual(str(ip_min_1), priv_ipv6_ip_min_1)

        self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_link_local(priv_ipv6_ip))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_link_local(link_local_ipv6))

        self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_multicast(priv_ipv6_ip))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_multicast(multicast_ipv6))

        self.assertFalse(RobotFrameworkNetAddr.ipaddress_is_loopback(priv_ipv6_ip))
        self.assertTrue(RobotFrameworkNetAddr.ipaddress_is_loopback(loopback_ipv6))

        rev_dns = RobotFrameworkNetAddr.ipaddress_reverse_dns(priv_ipv6_ip)
        self.assertEqual(str(rev_dns), priv_ipv6_reverse_dns)

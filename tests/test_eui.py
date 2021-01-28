import unittest
import sys
import os

sys.path.append(os.path.abspath("../src/RobotFrameworkNetAddr"))
from robotframeworknetaddr import RobotFrameworkNetAddr


class TestEUI(unittest.TestCase):

    def test_eui(self):
        addr = '00-2B-67-11-22-33'
        oui = '00-2B-67'
        ei = '11-22-33'
        eui64 = '00-2B-67-FF-FE-11-22-33'
        ipv6_prefix = 0xfc000000000000000000000000000000
        ipv6 = 'fc00::22b:67ff:fe11:2233'
        ipv6_link_local = 'fe80::22b:67ff:fe11:2233'
        invalid_addr = 'abcd'

        self.assertEqual(RobotFrameworkNetAddr.eui_oui(addr), oui)
        self.assertEqual(RobotFrameworkNetAddr.eui_ei(addr), ei)
        self.assertEqual(RobotFrameworkNetAddr.eui_eui64(addr), eui64)
        self.assertEqual(str(RobotFrameworkNetAddr.eui_ipv6(addr, ipv6_prefix)), ipv6)
        self.assertEqual(str(RobotFrameworkNetAddr.eui_ipv6_link_local(addr)), ipv6_link_local)
        self.assertFalse(RobotFrameworkNetAddr.eui_is_valid(invalid_addr))
        self.assertTrue(RobotFrameworkNetAddr.eui_is_valid(addr))

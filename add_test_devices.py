
"""
Python program to find out unittest of number of devices used in network
"""

import unittest

def add_network_devices_to_network(router_list):
    if len(router_list) > 27:
        raise ValueError("Number of Routers has to be less than 27")
    return {"router_list":router_list}

class TestAddDevices(unittest.TestCase):
    def test_add_network_devices_to_network(self):
        actual = add_network_devices_to_network(router_list=["ciscoxe-2380","cisco-xe-5493"])
        expected = {"router_list":["ciscoxe-2380","cisco-xe-5493"]}
        self.assertEqual(actual,expected)

# coding: utf-8

"""
    DFC

    DFC is a scalable object-storage based caching system with Amazon and Google Cloud backends.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: dfcdev@exchange.nvidia.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.daemon_api import DaemonApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDaemonApi(unittest.TestCase):
    """DaemonApi unit test stubs"""

    def setUp(self):
        configuration = openapi_client.Configuration()
        configuration.debug = False
        api_client = openapi_client.ApiClient(configuration)
        self.daemon = openapi_client.api.daemon_api.DaemonApi(api_client)
        self.models = openapi_client.models

    def tearDown(self):
        pass

    def test_get_config(self):
        """
        1. Get config
        2. Validate
        """
        input_params = self.models.InputParameters(
            self.models.Actions.SETCONFIG,
            "loglevel", "4")
        self.daemon.perform_operation(input_params)

        config = DictParser.parse(self.daemon.get(
            self.models.GetWhat.CONFIG))
        self.assertTrue(config.log.loglevel == "4",
                        "Set config value not getting reflected.")

        input_params = self.models.InputParameters(
            self.models.Actions.SETCONFIG,
            "loglevel", "3")
        self.daemon.perform_operation(input_params)

    def test_shutdown_target(self):
        smap = DictParser.parse(self.daemon.get(self.models.GetWhat.SMAP))
        target_id = smap.tmap.keys()[0]
        target_port = target_id[-4:]
        primary_proxy_port = smap.proxy_si.daemon_port
        print target_port, target_id
        self.daemon.api_client.configuration.host = (
                "http://localhost:%s/v1" % target_port)
        input_params = self.models.InputParameters(self.models.Actions.SHUTDOWN)
        self.daemon.perform_operation(input_params)
        self.daemon.api_client.configuration.host = (
                "http://localhost:%s/v1" % primary_proxy_port)
        updated_smap = DictParser.parse(
            self.daemon.get(self.models.GetWhat.SMAP))
        self.assertTrue(target_id not in updated_smap.tmap.keys(),
                        "Shutdown target returned in SMAP")


    def test_get_stats(self):
        smap = DictParser.parse(self.daemon.get(self.models.GetWhat.SMAP))
        target_port = smap.tmap.keys()[0][-4:]
        primary_proxy_port = smap.proxy_si.daemon_port
        self.daemon.api_client.configuration.host = (
                "http://localhost:%s/v1" % target_port)
        stats = DictParser.parse(self.daemon.get(self.models.GetWhat.STATS))
        self.assertTrue(stats.capacity.values()[0].avail != 0,
                        "Available disk space is returned as 0")
        self.daemon.api_client.configuration.host = (
                "http://localhost:%s/v1" % primary_proxy_port)

    def test_perform_operation(self):
        """Test case for perform_operation

        Perform operations such as setting config value, shutting down proxy/target etc. on a DFC daemon  # noqa: E501
        """
        pass


class DictParser(dict):
    __getattr__= dict.__getitem__

    def __init__(self, d):
        self.update(**dict((k, self.parse(v))
                           for k, v in d.iteritems()))

    @classmethod
    def parse(cls, v):
        if isinstance(v, dict):
            return cls(v)
        elif isinstance(v, list):
            return [cls.parse(i) for i in v]
        else:
            return v

if __name__ == '__main__':
    unittest.main()

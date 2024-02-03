#!/usr/bin/env python3
"""Module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Func that tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Func that tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)

        gh_org_client = GithubOrgClient(org)
        result = gh_org_client.org()

        mocked_fxn.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org)
                )
        self.assertEqual(result, resp)


if __name__ == '__main__':
    unittest.main()

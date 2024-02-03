#!/usr/bin/env python3
"""Module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch, PropertyMock
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

    def test_public_repos_url(self):
        """Tests the `_public_repos_url` property."""
        mock_payload = {
                "repos_url": "https://api.github.com/orgs/example/repos"
                }

        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock,
                return_value=mock_payload
                ):
            gh_org_client = GithubOrgClient("example")
            expected_url = "https://api.github.com/orgs/example/repos"

            result = gh_org_client._public_repos_url

            self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()

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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Func to test the public_repos method.
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697549,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 4342003,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2023-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566974,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1332004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2023-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()

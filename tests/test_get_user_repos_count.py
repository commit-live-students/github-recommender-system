from unittest import TestCase
import pandas as pd


class TestGet_user_repos_count(TestCase):
    def test_get_user_repos_count(self):
        from build import get_user_repos_count

        repos_count = get_user_repos_count("someonewhoisnotpresent")
        self.assertEqual(-1, repos_count)

        repos_count = get_user_repos_count("karpathy")
        self.assertGreaterEqual(repos_count, 16)

    def test_get_user_liked_repos_count(self):
        from build import get_user_liked_repos_count

        repos_count = get_user_liked_repos_count("someonewhoisnotpresent")
        self.assertEqual(-1, repos_count)

        repos_count = get_user_liked_repos_count("karpathy")
        self.assertGreaterEqual(repos_count, 23)

    def test_get_user_liked_repos(self):
        from build import get_user_liked_repos

        repos = get_user_liked_repos("someonewhoisnotpresent")
        self.assertEqual(None, repos)

        repos = get_user_liked_repos("karpathy")
        self.assertTrue(isinstance(repos, pd.DataFrame))

    def test_get_user_liked_repos_owners(self):
        from build import get_user_liked_repos_owners

        repos = get_user_liked_repos_owners("someonewhoisnotpresent")
        self.assertEqual(None, repos)

        repos = get_user_liked_repos_owners("karpathy")
        self.assertTrue(isinstance(repos, pd.DataFrame))


    def test_get_owners_liked_repos(self):
        from build import get_owners_liked_repos

        repos = get_owners_liked_repos("someonewhoisnotpresent")
        self.assertEqual(None, repos)

        repos = get_owners_liked_repos("karpathy")
        self.assertTrue(isinstance(repos, pd.DataFrame))

    def test_get_owners_liked_repos_summary(self):
        from build import get_owners_liked_repos_summary

        repos = get_owners_liked_repos_summary("someonewhoisnotpresent")
        self.assertEqual(None, repos)

        repos = get_owners_liked_repos_summary("karpathy")
        self.assertTrue(isinstance(repos, list))
        self.assertTrue(isinstance(repos[0], tuple))
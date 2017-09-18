import pandas as pd
import numpy as np
import requests

def get_user_repos_count(username):
    url = "https://api.github.com/users/{}/repos?access_token=716ae4c6076c25088ba6eeabe6e2909b918beb54".format(username)
    req = requests.get(url)
    if req.status_code == 200:
        repositories = req.json()
        return len(repositories)
    #if req.status_code == 404 and req.json()['message'] == "Not Found":
    #    return -1
    return -1


def get_user_liked_repos_count(username):
    url = u'https://api.github.com/users/{}/starred?access_token=716ae4c6076c25088ba6eeabe6e2909b918beb54'.format(username)
    req = requests.get(url)
    if req.status_code == 200:
        starred_repos = req.json()
        return len(starred_repos)
    return -1


def get_user_liked_repos(username):
    url = u'https://api.github.com/users/{}/starred?access_token=716ae4c6076c25088ba6eeabe6e2909b918beb54'.format(username)
    req = requests.get(url)
    starred_repos = req.json()
    if req.status_code == 200:
        df = pd.DataFrame(starred_repos)
        return df[["name", "html_url"]]
    return None


def get_user_liked_repos_owners(username):
    url = u'https://api.github.com/users/{}/starred?access_token=716ae4c6076c25088ba6eeabe6e2909b918beb54'.format(username)
    req = requests.get(url)
    starred_repos = req.json()
    if req.status_code == 200:
        starred_list = []
        for item in starred_repos:
            starred_list.append({"name" : item.get("owner").get("login"), "urls" : item.get("owner").get("html_url")})
        return pd.DataFrame(starred_list)
    return None # Default return in None

def get_owners_liked_repos(username):
    url = u'https://api.github.com/users/{}/starred?access_token=716ae4c6076c25088ba6eeabe6e2909b918beb54'.format(username)
    req = requests.get(url)
    starred_repos = req.json()
    if req.status_code != 200:
        return None
    final_results = []
    for item in starred_repos:
        repo_name = item.get("name")
        repo_url = item.get("html_url")
        owner_name = item.get("owner").get("login")
        owner_profile_url = item.get("owner").get("html_url")

        owners_starred_url = 'https://api.github.com/users/{}/starred?access_token=716ae4c6076c25088ba6eeabe6e2909b918beb54'.format(owner_name)
        owner_req = requests.get(owners_starred_url)
        if owner_req.status_code == 200:
            owner_starred_repos = owner_req.json()
            for repo in owner_starred_repos:
                repo_liked_by_owner = repo.get("name")
                repo_url_liked_by_owner = repo.get("html_url")
                final_results.append({"repo_name" :repo_name, "repo_url" : repo_url, "owner_name" : owner_name , "owner_profile_url" : owner_profile_url, "repo_liked_by_owner" : repo_liked_by_owner, "repo_url_liked_by_owner" : repo_url_liked_by_owner})

    df = pd.DataFrame(final_results)
    return df


def get_owners_liked_repos_summary(username):
    df = get_owners_liked_repos(username)
    if type(df) != pd.core.frame.DataFrame: # or df.empty:
        return None
    grp = df.groupby(["repo_url"], sort=True, as_index=False).size()
    top_5 = grp.sort_values(ascending=False).head(5)
    results = []
    for url in top_5.index:
        repo_name =  df.loc[df['repo_url'] == url, 'repo_name'].head(1)
        results.append((repo_name.values[0], url))

    return results

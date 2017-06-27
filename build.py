import requests
import pandas as pd
from collections import defaultdict

def get_user_repos_count(username):
    url = "https://api.github.com/users/%s/repos"%username
    request = requests.get(url)

    if request.status_code != 200:
        return -1

    repositories = request.json()
    return len(repositories)


def get_user_liked_repos_count(username):
    url = "https://api.github.com/users/%s/starred"%username
    request = requests.get(url)

    if request.status_code != 200:
        return -1

    starred = request.json()
    return len(starred) # Getting 30 whereas actual count is 71 !!!
    # solution seen here
    # https://stackoverflow.com/questions/30636798/get-user-total-starred-count-using-github-api-v3

def get_user_liked_repos(username):
    liked_repos = []

    url = "https://api.github.com/users/%s/starred"%username
    request = requests.get(url)

    if request.status_code != 200:
        return None

    starred = request.json()

    for data in starred:
        liked_repos.append(data["name"]+data["html_url"])

    liked_repo_df = pd.DataFrame(data=liked_repos,columns=['name+url'])
    return liked_repo_df

def get_user_liked_repos_owners(username):
        liked_repo_owners = []

        url = "https://api.github.com/users/%s/starred"%username
        request = requests.get(url)

        if request.status_code != 200:
            return None

        starred = request.json()

        for data in starred:
            owner_data = data['owner']
            liked_repo_owners.append(owner_data['login']+owner_data['html_url'])

        liked_repo_owners_df = pd.DataFrame(data=liked_repo_owners,columns=['github_name+github_url'])

        return liked_repo_owners_df

def get_owners_liked_repos(username):
    lis = []

    url = "https://api.github.com/users/%s/starred"%username
    request = requests.get(url)

    #print "status_code ",request.status_code
    if request.status_code != 200:
        return None

    starred = request.json()

    for data in starred:
        lis.append(('repo_name',data['name']))
        lis.append(('repo_url',data['html_url']))

        owner_data = data['owner']
        lis.append(('owner_name',owner_data['login']))
        lis.append(('owner_profile_url',owner_data['html_url']))

        sub_url = "https://api.github.com/users/%s/starred"%owner_data['login']
        sub_request = requests.get(url)

        sub_starred = request.json()

        for sub_data in sub_starred:
                lis.append(('repo_liked_by_owner',sub_data['name']))
                lis.append(('repo_url_liked_by_owner',sub_data['html_url']))

    dic = defaultdict(list)
    for keys,values in lis:
        dic[keys].append(values)

    dataframe = pd.DataFrame.from_dict(dic,orient='index')
    #print dataframe.head()
    transposed = dataframe.transpose()
    #print transposed.head()
    transposed.to_csv('git.csv',index=False)

    return dataframe.transpose()

def get_owners_liked_repos_summary(username):
    url = "https://api.github.com/users/%s/starred"%username
    request = requests.get(url)

    #print "status_code ",request.status_code
    if request.status_code != 200:
        return None

    lis1 = []
    lis2 = []
    return_list = []
    df = pd.read_csv('git.csv')
    df2 = df.groupby(['repo_url_liked_by_owner','repo_name']).count().head().reset_index()
    df2 = df2[['repo_url_liked_by_owner','repo_name']]
    lis1 = df2['repo_url_liked_by_owner'].tolist()
    lis2 = df2['repo_name'].tolist()
    for i in range(len(lis1)):  # or lis, both will have same length due to head()
        return_list.append((lis1[i],lis2[i]))

    return return_list

#get_user_repos_count("karpathy")
#get_user_liked_repos_count("karpathy")
#get_user_liked_repos("karpathy")
#get_user_liked_repos_owners("karpathy")
#get_owners_liked_repos("karpathy")
#get_owners_liked_repos_summary("karpathy")

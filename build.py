import requests
import pandas as pd
def get_user_repos_count(username):
    url = "https://api.github.com/users/"+username
    request = requests.get(url)
    status = request.status_code
    if status == 200:
        repo = request.json()
        return repo["public_repos"]
    else:
        return -1


def get_user_liked_repos_count(username):
    url = "https://api.github.com/users/"+username+"/starred"
    request = requests.get(url)
    status = request.status_code
    if status == 200:
        repo = request.json()
        return len(repo)
    else:
        return -1


def get_user_liked_repos(username):
    url = "https://api.github.com/users/"+username+"/starred"
    request = requests.get(url)
    status = request.status_code
    data = []
    data_1 = []
    columns = ['name+urls']
    if status == 200:
        repo = request.json()
        for i in repo:
            data.append(i["name"]+i["html_url"])

        liked_repo = pd.DataFrame(data,columns=columns)
        return liked_repo

    else:
        return None


def get_user_liked_repos_owners(username):
        url = "https://api.github.com/users/"+username+"/starred"
        request = requests.get(url)
        status = request.status_code
        data = []
        data_1 = []
        columns = ['name+urls']
        if status == 200:
            repo = request.json()
            for i in repo:
                owner = i['owner']
                data.append(owner['login']+owner['html_url'])

            liked_repo = pd.DataFrame(data,columns=columns)
            return liked_repo
        else:
            return None

def get_owners_liked_repos(username):
    url = "https://api.github.com/users/"+username+"/starred"
    request = requests.get(url)
    status = request.status_code
    repo_name = []
    repo_url = []
    liked_repo = []
    owner_name = []
    owner_profile_url = []
    repo_liked_by_owner = []
    repo_url_liked_by_owner = []
    columns = ['repo_name','repo_url']
    if status == 200:
        repo = request.json()
        for i in repo:
            repo_name.append(i['name'])
            repo_url.append(i['html_url'])
            owner = i['owner']
            owner_name.append(owner['login'])
            owner_profile_url.append(owner['html_url'])
            url_2 = "https://api.github.com/users/"+owner['login']+"/starred"
            request = requests.get(url_2)
            status = request.status_code
            if status == 200:
                repo_owner = request.json()
                for j in repo_owner:
                    repo_liked_by_owner.append(j['name'])
                    repo_url_liked_by_owner.append(j['html_url'])
        dic = dict(repo_name = repo_name, repo_url = repo_url,owner_name = owner_name, owner_profile_url = owner_profile_url, repo_liked_by_owner = repo_liked_by_owner, repo_url_liked_by_owner = repo_url_liked_by_owner)
        df = pd.DataFrame({k : pd.Series(v) for k, v in dic.iteritems()})
        return df.head()
    else:
        return None


def get_owners_liked_repos_summary(username):
    url = "https://api.github.com/users/"+username+"/starred"
    request = requests.get(url)
    status = request.status_code
    data = []
    #print status
    columns = ['name+urls']
    if status == 200:
        repo = request.json()
        for i in repo:
            t = (i["name"],i["html_url"])
            data.append(t)
        return data
    else:
        return None



get_owners_liked_repos_summary("ankanroy007")
#sget_owners_liked_repos("ankanroy007")

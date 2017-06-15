# GitHub Recommender System

For this [GH user](https://api.github.com/users/karpathy/repos), answer the following questions.

__Question 1__

Write a function that gives the number of GitHub repos the user has

* Define function with name get_user_repos_count which should accept git hub username as parameter.
* Function should return count of repos this user has.
* As we require count it should be numeric value i.e. type of return variable should be numeric.
* In case if we pass username which does not belongs to gihub, function should return count -1 to indicate that user not found.


__Question 2__

Write a function that gives the number of GitHub repos has the user liked.

* Define function with name get_user_liked_repos_count which should accept git hub username as parameter.
* Function should return count of repos this user has liked.
* As we require count it should be numeric value i.e. type of return variable should be numeric.
* In case if we pass username which does not belongs to gihub, function should return count -1 to indicate that user not found.


__Question 3__

Write a function that gives the dataframe of repos (name+urls) liked by the user.

* Define function with name get_user_liked_repos which should accept git hub username as parameter.
* Function should return name and urls of repos in form of dataframe with name + urls.
* Return type must be dataframe.
* An empty dataframe should indicate none repos are liked and None object should indicate user is not found.


__Question 4__

Write a function that gives the dataframe of repos username (github name + github urls) liked by the user.

* Define function with name get_user_liked_repos_owners which should accept git hub username as parameter.
* Function should return github name and github url of repos owner in form of dataframe with name + urls.
* Return type must be dataframe.
* An empty dataframe should indicate none repos are liked and None object should indicate user is not found.


__Question 5__

Write a function that gives the dataframe of repos liked by owner of repos liked bu user. First get repos liked by user then get owner of repos and then get repos liked by these owners.

* Define function with name get_owners_liked_repos which should accept git hub username as parameter.
* Function should return dataframe with following columns.
    * repo_name,
    * repo_url,
    * owner_name,
    * owner_profile_url
    * repo_liked_by_owner
    * repo_url_liked_by_owner
* Return type must be dataframe.
* An empty dataframe should indicate none repos are liked and None object should indicate user is not found.


__Question 6__

Write a function that groups by and sorts the column repo_url of the dataframe obtained in the last task by frequency (highest number frequency first) and return the top 5 repos (name+url) as a list of tuples [(name1, url1), (name2, url2),...]

* Define function with name get_owners_liked_repos_summary which should accept git hub username as parameter.
* Function should return list with following columns.
    * repo_name,
    * repo_url,
* Return type must be list of tuples.
* An empty list should indicate none repos and None object should indicate user is not found.
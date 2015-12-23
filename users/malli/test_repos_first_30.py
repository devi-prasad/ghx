from github import Github
import json

g = Github()

for repo in g.search_repositories('https://api.github.com/repos','updated','asc'):
    print(repo.name)

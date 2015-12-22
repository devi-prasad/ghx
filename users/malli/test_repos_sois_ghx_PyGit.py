from github import Github
import json

g=Github('sois','sois#manipal123')

for repo in g.get_user().get_repos():
    print(repo.name)

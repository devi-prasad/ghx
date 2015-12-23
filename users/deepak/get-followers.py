
# script that gives count of repos and followers of sois
# it also list the followers url


from github import Github

g = Github("sois", "put password")

print('No of public repos: %d' % g.get_user().public_repos)
print('No of followers: %d' % g.get_user().followers)

for fol in g.get_user().get_followers():
	print(fol.followers_url)

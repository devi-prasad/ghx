# This script pulls github user name and their repositories
# I noticed problem with script is that there is a rate limiting ie.
# for unauthenticated requests, rate limit allows to make up to 60 requests
# per hour. Unauthenticated requests are associated with users IP address,
# and not the user making requests. 
# After exceeding limit, we get a error message like 
# API rate limit exceeded for 14.139.155.243 (IP address) 

from github import Github

g = Github()

for use in g.get_users():
	print()
	print(use.name)	
	print('repos of %s' % use.name)
	for repos in use.get_repos():
		print(repos.name)

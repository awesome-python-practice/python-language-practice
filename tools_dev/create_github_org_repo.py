import os

from github import Github

"""
deprecated
"""

access_token = os.environ.get('GITHUB_ACCESSTOKEN_BUILD_PRACTICE_GROUP')
g = Github(access_token)

user=g.get_user()

org = g.get_organization(login='awesome-practice')

# org.create_repo(name="test_create_by_python")  # error 401

print(org)

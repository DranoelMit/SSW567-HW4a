#Tim Leonard
#I pledge my honor that I have abided by the Stevens Honor System
import requests
import json

def fetchUserInfo(uid=None):
    if uid is None:
      return 'Error: missing parameter uid (User ID)'
    if not isinstance(uid, str):
      return 'User Id must be a string'
    r = requests.get(url='https://api.github.com/users/'+uid+'/repos')
    repos = r.json()
    if not isinstance(repos, list):
        return []
    strings = []
    for repo in repos:
        cr = requests.get(url='https://api.github.com/repos/'+uid+'/'+repo['name']+'/commits')
        commits = cr.json()
        temp = 'Repo: ' + repo['name'] + ' Number of commits: ' + str(len(commits))
        strings.append(temp)
    return strings
    


if __name__ == '__main__':
  repoList = fetchUserInfo('DranoelMit')
  for s in repoList:
    print(s)



import unittest
from unittest import mock

import GithubApi

@mock.patch('GithubApi.fetchUserInfo')
def mock_fetchUserInfo(mock_fetch_fun):
    mock_fetch_fun.return_value = ['Repo: AlexaDemo Number of commits: 1']

class TestApi(unittest.TestCase):

  def testMissingParam(self):
      self.assertEqual(GithubApi.fetchUserInfo(), 'Error: missing parameter uid (User ID)', 'User id is required')
  def testFirstRepo(self):
      self.assertEqual(GithubApi.fetchUserInfo('DranoelMit')[0], 'Repo: AlexaDemo Number of commits: 1', 'First repo of user DranoelMit')
  def testInvalidUser(self):
      self.assertEqual(GithubApi.fetchUserInfo('sdasdgasdjasdgjhasdgasdasgdasdascdasfcashd'), [], 'No repos for invalid user')
  def testBadParam(self):
      self.assertEqual(GithubApi.fetchUserInfo(5), 'User Id must be a string', 'Must pass function a string userId')    


if __name__ == '__main__':
  print('Running unit tests')
  unittest.main()

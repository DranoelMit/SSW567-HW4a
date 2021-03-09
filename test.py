import unittest

from GithubApi import fetchUserInfo

class TestApi(unittest.TestCase):

  def testMissingParam(self):
      self.assertEqual(fetchUserInfo(), 'Error: missing parameter uid (User ID)', 'User id is required')
  def testFirstRepo(self):
      self.assertEqual(fetchUserInfo('DranoelMit')[0], 'Repo: AlexaDemo Number of commits: 1', 'First repo of user DranoelMit')
  def testInvalidUser(self):
      self.assertEqual(fetchUserInfo('sdasdgasdjasdgjhasdgasdasgdasdascdasfcashd'), [], 'No repos for invalid user')
  def testBadParam(self):
      self.assertEqual(fetchUserInfo(5), 'User Id must be a string', 'Must pass function a string userId')    


if __name__ == '__main__':
  print('Running unit tests')
  unittest.main()

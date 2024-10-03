import unittest

from main import to_upper

class MyTestCase(unittest.TestCase):

  def test_to_upper(self):

    name="Practical"

    up=to_upper(name)

    self.assertEqual(up, "PRACTICAL")

if __name__=='__main__':

  unittest.main()
  
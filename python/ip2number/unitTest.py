import unittest
from python.ip2number.ip2number import Solution

class Test(unittest.TestCase):
    def test_init(self):
        s = Solution()
        self.assertEquals(s.ip2number('172.168.5.1'), 2896692481)
        self.assertEquals(s.ip2number('172 . 168.5.1'), 2896692481)
        self.assertEquals(s.ip2number('1 72.168.5.1'), 'ip address is not valid!')


if __name__ == "__main__":
    unittest.main()
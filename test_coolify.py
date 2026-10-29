import unittest
import coolify as cl

#test
class TestCoolify(unittest.TestCase):
    def test_name(self):
        name = "kev test"
        self.assertTrue(cl.coolify(name) == "kev is cool")
        self.assertFalse(cl.coolify(name) == "kev")

if __name__ == '__main__':
    unittest.main()
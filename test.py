try:
    from main import app
    import unittest
except Exception as e:
    print("Some Modules are Missing {} ".format(e))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

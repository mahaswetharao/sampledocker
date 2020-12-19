import unittest

import app
import redis

class BasicTests(unittest.TestCase):
    """Sample unit test case"""

    def setUp(self) -> None:
        """Initialize the redis and flask app"""

        app.r = redis.Redis(
                    host='redis-server',
                    port=6379)
        self.app = app.app.test_client()
        app.r.set("count", "0")
        self.r = app.r

    def tearDown(self) -> None:
        """shutdown redis server"""
        self.r.close()

    def test_number_of_visits(self):
        """test if number of visits increments on every screen load"""
        initial_visit_count = int(self.r.get("count"))
        res = self.app.get('/')
        next_visit_count = int(self.r.get("count"))

        self.assertEqual(res.status_code, 200)
        self.assertIn(str(initial_visit_count), str(res.data))
        self.assertEqual(initial_visit_count+1, next_visit_count)



if __name__ == '__main__':
    unittest.main()




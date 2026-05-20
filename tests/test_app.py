import unittest

from oracle_ai_lab.app import create_app
from oracle_ai_lab.config import AppConfig


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app(AppConfig(project_name="Test Project"))
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Test Project", response.data)

    def test_health(self):
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()

import unittest
from app import app, collection  # Import your Flask application and MongoDB collection
from flask import json
from datetime import datetime

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_health_check(self):
        response = self.app.get('/')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Service is healthy.')

    def test_db_check(self):
        response = self.app.get('/db')
        data = json.loads(response.get_data(as_text=True))

        # Assuming your DB is running and healthy
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Database is healthy.')

    def test_create_route(self):
        route_data = {
            "route_id": "test_route",
            "timestamp": datetime.now()
        }

        response = self.app.post('/routes', json=route_data)
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Route created successfully.')

    # Add tests for other endpoints as well

if __name__ == '__main__':
    unittest.main()

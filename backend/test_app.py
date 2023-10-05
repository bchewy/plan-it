import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from flask import json
from app import app  # Assuming your Flask app is named app.py

class FlaskAppTestCase(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()

	def test_health_check(self):
		response = self.app.get('/')
		data = json.loads(response.get_data(as_text=True))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['message'], 'Service is healthy.')

	@patch('pymongo.MongoClient')
	def test_db_check(self, MockClient):
		MockClient().admin.command.return_value = True
		response = self.app.get('/db')
		data = json.loads(response.get_data(as_text=True))
		print(f"Debug: Response Data: {data}")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['message'], 'Database is healthy.')


	@patch('app.collection')
	def test_create_route(self, MockCollection):
		new_route = {
			"route_id": "test_route",
			"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}
		MockCollection.insert_one.return_value = MagicMock()
		response = self.app.post('/routes', json=new_route)
		data = json.loads(response.get_data(as_text=True))
		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['message'], 'Route created successfully.')

	@patch('app.collection')
	def test_read_all_routes(self, MockCollection):
		MockCollection.find.return_value = []
		response = self.app.get('/routes')
		self.assertEqual(response.status_code, 200)

	@patch('app.collection')
	def test_read_one_route(self, MockCollection):
		MockCollection.find_one.return_value = {"_id": "some_fake_id", "route_id": "some_id"}
		response = self.app.get('/routes/some_id')
		self.assertEqual(response.status_code, 200)


	@patch('app.collection')
	def test_update_route(self, MockCollection):
		updated_data = {"some_field": "new_value"}
		MockCollection.find_one_and_update.return_value = {"route_id": "some_id"}
		response = self.app.put('/routes/some_id', json=updated_data)
		data = json.loads(response.get_data(as_text=True))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['message'], 'Route updated successfully.')

	@patch('app.collection')
	def test_delete_route(self, MockCollection):
		MockCollection.find_one_and_delete.return_value = {"route_id": "some_id"}
		response = self.app.delete('/routes/some_id')
		data = json.loads(response.get_data(as_text=True))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['message'], 'Route deleted successfully.')

if __name__ == '__main__':
		unittest.main()

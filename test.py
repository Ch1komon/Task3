import unittest
import json
from app import app

class ToDoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_todo(self):
        response = self.app.post('/todos', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Task')

    def test_get_todos(self):
        self.app.post('/todos', json={'title': 'Test Task'})
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(len(data) > 0)

    def test_update_todo(self):
        self.app.post('/todos', json={'title': 'Test Task'})
        response = self.app.put('/todos/1', json={'completed': True})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['completed'])

if __name__ == '__main__':
    unittest.main()
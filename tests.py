import unittest
from peewee import *
from datetime import datetime

from app import app
from models import Todo


class ViewTests(unittest.TestCase):
	def test_homepage(self):
		app.config['TESTING'] = True
		self.app = app.test_client()
		homeview = self.app.get('/')
		self.assertEqual(homeview.status_code, 200)
		
class TodoModel(unittest.TestCase):
	def test_todo_model(self):
		dt = datetime(2000, 1, 1, 0, 0)
		Todo.create(name='RANDOM', created_at='2000-01-01')
		self.assertEqual(Todo.get(Todo.name=='RANDOM').name, 'RANDOM')
		self.assertEqual(Todo.get(Todo.created_at=='2000-01-01').created_at, dt)
		
class TodoClass(unittest.TestCase):
	def test_get_todo_list(self):
		app.config['TESTING'] = True
		self.app = app.test_client()
		Todo.create(name='TODO')
		listview = self.app.get('/')
		self.assertEqual(listview.status_code, 200)
		
if __name__ == '__main__':
	unittest.main()
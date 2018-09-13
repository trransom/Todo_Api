import unittest

from app import app
from models import Todo


class ViewTests(unittest.TestCase):
	def test_homepage(self):
		view = self.app.get('/')
		self.assertEqual(view.status_code, 200)
		
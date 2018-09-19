from flask import jsonify, Blueprint

from flask_restful import (Resource, Api, reqparse, inputs, fields,
							marshal, marshal_with, url_for, abort)

import models

todo_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'url': fields.String,
	'todos': fields.List(fields.String)
}

def todo_or_404(todo_id):
	try:
		todo_obj = models.Todo.get(models.Todo.id==todo_id)
	except models.Todo.DoesNotExist:
		abort(404)
	else:
		return todo_obj

class TodoList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			help='No task name provided',
			location=['form', 'json']
		)
		super().__init__()
		
	def get(self):
		todos = [marshal(todo, todo_fields) 
				for todo in models.Todo.select()]
		return todos
		
	@marshal_with(todo_fields)
	def post(self):
		args = self.reqparse.parse_args()
		todo = models.Todo.create(**args)
		return (todo, 201, 
				{'Location': url_for('resources.todos.todo', id=todo.id)})
		
class Todo(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			help='No task title provided',
			location=['form', 'json']
		)
		super().__init__()
		
	@marshal_with(todo_fields)
	def get(self, id):
		return add_todos(todo_or_404(id))
		
	@marshal_with(todo_fields)
	def put(self, id):
		args = self.reqparse.parse_args()
		query = models.Todo.update(**args).where(models.Todo.id==id)
		query.execute()
		return (models.Todo.get(models.Todo.id==id), 200,
				{'Location': url_for('resources.todos.todo', id=id)})
		
	def delete(self, id):
		query = models.Todo.delete().where(models.Todo.id==id)
		query.execute()
		return ('', 204, {'Location': url_for('resources.todos.todos')})
		
todos_api = Blueprint('resources.todos', __name__)
api = Api(todos_api)
api.add_resource(
	TodoList,
	'/todos',
	endpoint='todos'
)
api.add_resource(
	Todo,
	'/todos/<int:id>',
	endpoint='todo'
)
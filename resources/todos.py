from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse, inputs, fields

import models

todo_fields = {
	'id': fields.Integer,
	'name': fields.String
}

class TodoList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			help='No task title provided',
			location=['form', 'json']
		)
		super().__init__()
		
	def get(self):
		return jsonify({'todos': [{'name': 'Get Milk'}]})
		
	def post(self):
		args = self.reqparse.parse_args()
		models.Todo.create(**args)
		return jsonify({'todos': [{'name': 'Get Milk'}]})
		
class Todo(Resource):
	def get(self, id):
		return jsonify({'name': [{'Get Milk'}]})
		
	def put(self, id):
		return jsonify({'name': [{'Get Milk'}]})
		
	def delete(self, id):
		return jsonify({'name': [{'Get Milk'}]})
		
todos_api = Blueprint('resources.courses', __name__)
api = Api(todos_api)
api.add_resource(
	TodoList,
	'/api/v1/todos',
	endpoint='todos'
)
api.add_resource(
	Todo,
	'/api/v1/todos/<int:id>',
	endpoint='todo'
)
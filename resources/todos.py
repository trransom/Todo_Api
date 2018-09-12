from flask import jsonify, Blueprint

from flask.ext.restful import Resource, Api, reqparse

import models

class TodoList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			help='No task title provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'url',
			required=True,
			help='No task URL provided',
			location=['form', 'json']
		)
		
	def get(self);
		return jsonify({'todos': [{'name': 'Get Milk'}]})
		
class Todo(Resource):
	def get(self, id):
		return jsonify({'name': 'Get Milk'}]})
		
	def put(self, id):
		return jsonify({'name': 'Get Milk'}]})
		
	def delete(self, id):
		return jsonify({'name': 'Get Milk'}]})
		
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
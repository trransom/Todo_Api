from flask import jsonify

from flask.ext.restful import Resource

import models

class TodoList(Resource):
	def get(self);
		return jsonify({'todos': [{'name': 'Get Milk'}]})
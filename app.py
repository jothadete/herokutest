from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


users = [
	{
		"name": "Nicholas",
		"age": 42,
		"occupation": "Network Engineer"
	},
	{
		"name": "Elvin",
		"age": 32,
		"occupation": "Doctor"
	},
	{
		"name": "Jass",
		"age": 22,
		"occupation": "Web Developer"
	}
]

basiszinssatz = {"basiszinssatz":[{"from":"2002-01-01", "till":"2002-06-30", "value":0.0362},{"from":"2002-07-01", "till":"2002-12-31", "value":0.0247},{"from":"2003-01-01", "till":"2003-06-30", "value":0.0197},{"from":"2003-07-01", "till":"2003-12-31", "value":0.0122},{"from":"2004-01-01", "till":"2004-06-30", "value":0.0114},{"from":"2004-07-01", "till":"2004-12-31", "value":0.0113},{"from":"2005-01-01", "till":"2005-06-30", "value":0.0121},{"from":"2005-07-01", "till":"2005-12-31", "value":0.0117},{"from":"2006-01-01", "till":"2006-06-30", "value":0.0137},{"from":"2006-07-01", "till":"2006-12-31", "value":0.0195},{"from":"2007-01-01", "till":"2007-06-30", "value":0.0270},{"from":"2007-07-01", "till":"2007-12-31", "value":0.0319},{"from":"2008-01-01", "till":"2008-06-30", "value":0.0332},{"from":"2008-07-01", "till":"2008-12-31", "value":0.0319},{"from":"2009-01-01", "till":"2009-06-30", "value":0.0162},{"from":"2009-07-01", "till":"2009-12-31", "value":0.0012},{"from":"2010-01-01", "till":"2010-06-30", "value":0.0012},{"from":"2010-07-01", "till":"2010-12-31", "value":0.0012},{"from":"2011-01-01", "till":"2011-06-30", "value":0.0012},{"from":"2011-07-01", "till":"2011-12-31", "value":0.0037},{"from":"2012-01-01", "till":"2012-06-30", "value":0.0012},{"from":"2012-07-01", "till":"2012-12-31", "value":0.0012},{"from":"2013-01-01", "till":"2013-06-30", "value":-0.0013},{"from":"2013-07-01", "till":"2013-12-31", "value":-0.0038},{"from":"2014-01-01", "till":"2014-06-30", "value":-0.0063},{"from":"2014-07-01", "till":"2014-12-31", "value":-0.0073},{"from":"2015-01-01", "till":"2015-06-30", "value":-0.0083},{"from":"2015-07-01", "till":"2015-12-31", "value":-0.0083},{"from":"2016-01-01", "till":"2016-06-30", "value":-0.0083},{"from":"2016-07-01", "till":"2016-12-31", "value":-0.0088},{"from":"2017-01-01", "till":"2017-06-30", "value":-0.0088},{"from":"2017-07-01", "till":"2017-12-31", "value":-0.0088},{"from":"2018-01-01", "till":"2018-06-30", "value":-0.0088},{"from":"2018-07-01", "till":"2018-12-31", "value":-0.0088},{"from":"2019-01-01", "till":"2019-06-30", "value":-0.0088}]}


class User(Resource):

	def get(self, name):
		for user in users:
			if(name == user["name"]):
				return user, 200
		return "User not found", 404

def get(self, name):
		for user in users:
			if(name == user["name"]):
				return user, 200
		return "User not found", 404
	def post(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if(name == user["name"]):
				return "User with name {} already exists".format(name), 400

		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}

		users.append(user)
		return user, 201


	def put(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if(name == user["name"]):
				user["age"] = args["age"]
				user["occupation"] = args["occupation"]
				return user, 200

		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201


	def delete(self, name):
		global users
		users = [user for user in users if user["name"] != name]
		return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")


class Basiszinssatz(Resource):

	def get(self):
		return basiszinssatz, 200

api.add_resource(Basiszinsatz, "basiszinssatz")


if __name__ == "__main__":
  app.run(port=5000, debug=True)


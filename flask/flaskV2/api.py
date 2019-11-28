from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello_world(Resource):
    def get(self):
         return {'about' : 'hello_world'}

    def post(self):
        some_json = request.get_json()
        return {'you send' : some_json}, 201

class Add(Resource):
    def get(self, num):
        return {'result' : num + 100}

api.add_resource(Hello_world,'/')
api.add_resource(Add, '/add/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)

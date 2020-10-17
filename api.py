from flask import Flask, jsonify,request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from query import query

app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

searchtext = ''

class HelloWorld(Resource):
    def get(self):
        return {"answer" : query(searchtext,10)}
    def post(self):
        searchtext = request.json['data']
        return {'answer': query(searchtext,15)}

api.add_resource(HelloWorld, '/',methods=['GET', 'POST','PUT'])

if __name__ == '__main__':
    app.run(debug=True)

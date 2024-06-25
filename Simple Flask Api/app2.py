"""
Method 2: Using the flask_restful library 
Create a new python file named ‘main.py’.
Import Flask from the flask framework.
Import API and Resource from the ‘flask_restful’ library.
Register the web app into a app variable using the following syntax.

"""




from flask import Flask 
from flask_restful import Api, Resource 

app = Flask(__name__) 

api = Api(app) 

class HelloWorld(Resource): 
	def get(self): 
		data={"data":"Hello World"} 
		return data 

api.add_resource(HelloWorld,'/hello') 


if __name__=='__main__': 
	app.run(debug=True)

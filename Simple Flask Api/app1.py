"""
Method 1: Using Flask ‘jsonify’ object
Create a new python file named ‘main.py’.
import Flask, jsonify and request from the flask framework.
Register the web app into an app variable using the following synt
"""



from flask import Flask, jsonify, request 

app = Flask(__name__) 


@app.route('/', methods=['GET']) 
def helloworld(): 
	if(request.method == 'GET'): 
		data = {"data": "Hello World"} 
		return jsonify(data) 


if __name__ == '__main__': 
	app.run(debug=True) 

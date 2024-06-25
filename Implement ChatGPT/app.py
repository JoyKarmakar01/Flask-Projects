from flask import Flask, render_template, request, jsonify 
from openai import OpenAI
import os
import openai

app = Flask(__name__) 

# OpenAI API Key 
client = OpenAI(
    api_key = 'sk-...UuyK'
)

def get_completion(prompt): 
	print(prompt) 
	query = openai.chat.Completion.create( 
		engine="gpt-3.5-turbo", 
		prompt=prompt, 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 

	response = query.choices[0].text 
	return response 

@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
	if request.method == 'POST': 
		print('step1') 
		prompt = request.form['prompt'] 
		response = get_completion(prompt) 
		print(response) 

		return jsonify({'response': response}) 
	return render_template('index.html') 


if __name__ == "__main__": 
	app.run(debug=True) 

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import config
import requests
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

app = Flask(__name__)
CORS(app)

## Define the API endpoint
# Version v2
@app.route('/api/v2/message', methods=['POST'])
def generate_response():
    data = request.get_json()
    prompt = f"Conversation:\nUser: {data['text']}\nAI:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

# Version v3
@app.route('/api/v3/message', methods=['POST'])
def message():
   data = request.get_json()
   prompt = data['prompt']
   response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[
           {"role": "system", "content": "You are a helpful assistant."},
           {"role": "user", "content": prompt}
       ]
   )
   message = response.choices[0].text.strip()
   return jsonify({'message': message})

# Versoin v4
@app.route('/api/v4/message', methods=['POST'])
def text():
   data = request.get_json()
   prompt = data['prompt']
   response = openai.ChatCompletion.create(
       model="text-davinci-002",
       messages=[
           {"role": "system", "content": "You are a helpful assistant."},
           {"role": "user", "content": prompt}
       ]
   )
   message = response.choices[0].message.content.strip()
   return jsonify({'message': message})

# Version v5
@app.route('/')
def hello_world():
    return 'Hello World! V1.0.2'


# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)


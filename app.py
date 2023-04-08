from dotenv import load_dotenv
from flask import Flask, request, jsonify, redirect, render_template, url_for
from flask_cors import CORS
import config
import requests
import openai
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv('OPENAI_KEY')


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/image", methods=("GET", "POST"))
def image():
    if request.method == "POST":
        image = request.form["image"]
        response = openai.Image.create(
            prompt=image,
            n=1,
            size="1024x1024"
        )
        return redirect(url_for("image", result=response['data'][0]['url']))

    result = request.args.get("result")
    return render_template("image.html", result=result)



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



# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)


from flask import Flask, request, jsonify
import config
import requests
import openai

# config.py config.DevelopmentConfig.OPENAI_KEY
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello World! V1.0.2'

#@app.route('/api/v1/message', methods=['POST'])
#def message():
#    # Obtém a mensagem do cliente do corpo da solicitação
#    data = request.json
#    prompt = data['prompt']
#    # Chama o modelo ChatGPT da OpenAI para gerar uma resposta
#    response = openai.ChatCompletion.create(
#        model="gpt-3.5-turbo",
#        messages=[
#            {"role": "system", "content": "You are a helpful assistant."},
#            {"role": "user", "content": prompt}
#        ]
#    )
#    # Obtém a resposta gerada pelo modelo e retorna ao cliente
#    message = response.choices[0].text.strip()
#    return jsonify({'message': message})



# Define the API endpoint
@app.route('/api/v1/message', methods=['POST'])
def generate_response():
    # Parse the request data
    data = request.get_json()

    # Generate the response using the OpenAI API
    prompt = f"Conversation:\nUser: {data['text']}\nAI:"
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the response from the OpenAI API and return it as JSON
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)


# sudo nohup python3 -u /home/monga/monga-applications-lab/app.py
#response = openai.ChatCompletion.create(
#    model="text-davinci-002",
#    messages=[
#        {"role": "system", "content": "You are a helpful assistant."},
#        {"role": "user", "content": prompt}
#    ]
#)
#message = response.choices[0].message.content.strip()


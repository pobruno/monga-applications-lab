from flask import Flask, request, jsonify
import config
import openai

app = Flask(__name__)
# config.py config.DevelopmentConfig.OPENAI_KEY
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

#@app.route('/')
#def hello_world():
#    return 'Hello World! V1.0.2'

@app.route('/api/chat', methods=['POST'])
def chat():
    # Obtém a mensagem do cliente do corpo da solicitação
    data = request.json
    prompt = data['prompt']
    # Chama o modelo ChatGPT da OpenAI para gerar uma resposta
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Obtém a resposta gerada pelo modelo e retorna ao cliente
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

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


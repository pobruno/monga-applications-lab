from flask import Flask, request, jsonify
import config
import openai

app = Flask(__name__)
# config.py config.DevelopmentConfig.OPENAI_KEY
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

@app.route('/')
def hello_world():
    return 'Hello World! V1.0.2'

@app.route('/api/chat', methods=['POST'])
def chat():
    # Obtém a mensagem do cliente do corpo da solicitação
    data = request.json
    prompt = data['prompt']
    # Chama o modelo ChatGPT da OpenAI para gerar uma resposta
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Obtém a resposta gerada pelo modelo e retorna ao cliente
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)

# sudo nohup python3 -u /home/monga/monga-applications-lab/app.py

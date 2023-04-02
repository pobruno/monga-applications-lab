from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST', 'GET'])
def chat():
    # seu código aqui
    response = {
        'message': 'Hello, ChatGPT!'
    }
    if request.method == 'POST':
        data = request.get_json()
        # código para processar o JSON aqui
        response['message'] = chatgpt_response
    return jsonify(response)

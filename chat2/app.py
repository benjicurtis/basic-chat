from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    name = data['name']
    message = data['msg']
    date = data['date']
    messages.append(f"{name}: {message}: {date}")
    return jsonify({'status': 'success', 'message': message})

@app.route('/response')
def get_messages():
    return jsonify({'messages': messages})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

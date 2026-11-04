from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/sendMsg", methods=["POST"])
def sendMsg():
    data = request.get_json()
    messages.append(data)
    return jsonify({"status": "success", "message": "Message received."})
@app.route("/getMsg", methods=["GET"])
def getMsg():
    return jsonify(messages)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

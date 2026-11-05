\from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

global active_users
active_users = 0

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
@app.route("/resetMsg", methods=["POST"])
def resetMsg():
    messages.clear()
    return jsonify({"status": "success", "message": "Messages reset."})
@app.route("/increaseActiveUsers", methods=["POST"])
def increaseActiveUsers():
    active_users += 1
    return jsonify({"status": "success", "message": "Active users increased."})
@app.route("/decreaseActiveUsers", methods=["POST"])
def decreaseActiveUsers():
    active_users -= 1
    return jsonify({"status": "success", "message": "Active users decreased."})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

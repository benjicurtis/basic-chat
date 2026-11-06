from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

messages = []

usersActive = []

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/messageSent", methods=["POST"])
def messageSent():
    data = request.get_json()
    messages.append(data)
    if len(messages) > 70:
        messages.pop(0)
    return jsonify({"status": "success", "message": "Message received successfully."}), 200
@app.route("/getMsg", methods=["GET"])
def getMsg():
    return jsonify(messages[::-1])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask on Vercel working!"})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)
    
    print("Webhook Received:", data)

    return jsonify({
        "status": "success",
        "received": data
    }), 200

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)   # 👈 THIS LINE FIXES YOUR ERROR

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    payload = {
        "contents": [
            {"parts": [{"text": user_message}]}
        ]
    }

    response = requests.post(GEMINI_URL, json=payload)
    data = response.json()

    try:
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        reply = "Sorry, I couldn't understand."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


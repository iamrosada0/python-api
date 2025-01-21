from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello, Flask on Vercel!"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    direction = data.get("direction", "")

    # Dummy response for testing
    if direction == "Portuguese to English":
        translated_text = f"Translated '{text}' to English"
    elif direction == "English to Portuguese":
        translated_text = f"Translated '{text}' to Portuguese"
    else:
        translated_text = "Invalid direction"

    return jsonify({"translated_text": translated_text})

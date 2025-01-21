from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello, Flask on Vercel!"

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    
    # Validate the incoming data
    if not data or 'text' not in data or 'direction' not in data:
        return jsonify({"error": "Both 'text' and 'direction' fields are required."}), 400

    input_text = data['text']
    direction = data['direction']

    # Set up translation based on direction
    try:
        if direction == "Portuguese to English":
            translator = Translator(to_lang="en", from_lang="pt")
        elif direction == "English to Portuguese":
            translator = Translator(to_lang="pt", from_lang="en")
        else:
            return jsonify({"error": "Invalid translation direction. Use 'Portuguese to English' or 'English to Portuguese'."}), 400

        # Perform the translation
        translated_text = translator.translate(input_text)

        # Return the translated text as a JSON response
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
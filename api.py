from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    # Obter os dados do corpo da requisição
    data = request.get_json()
    
    # Validar os dados recebidos
    if not data or 'text' not in data or 'direction' not in data:
        return jsonify({"error": "Both 'text' and 'direction' fields are required."}), 400

    input_text = data['text']
    direction = data['direction']

    # Configurar a tradução com base na direção selecionada
    try:
        if direction == "Portuguese to English":
            translator = Translator(to_lang="en", from_lang="pt")
        elif direction == "English to Portuguese":
            translator = Translator(to_lang="pt", from_lang="en")
        else:
            return jsonify({"error": "Invalid translation direction. Use 'Portuguese to English' or 'English to Portuguese'."}), 400

        # Realizar a tradução
        translated_text = translator.translate(input_text)

        # Retornar o texto traduzido como resposta JSON
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

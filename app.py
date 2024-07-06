from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Dictionary to map language codes to full names
language_names = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'gu': 'Gujarati',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'or': 'Odia',
    'pa': 'Punjabi',
    'sd': 'Sindhi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ur': 'Urdu'
}

@app.route('/')
def index():
    return render_template('index.html', languages=language_names)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text_to_translate = data.get('text')
    source_lang = data.get('source', 'en')
    target_lang = data.get('target', 'hi')

    # Check if target language is in the list of supported languages
    supported_languages = language_names.keys()

    if target_lang not in supported_languages:
        return jsonify({'error': 'Target language not supported'}), 400

    translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text
    response = {
        'translated_text': translated_text,
        'source_language_full_name': language_names.get(source_lang, source_lang),
        'target_language_full_name': language_names.get(target_lang, target_lang)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
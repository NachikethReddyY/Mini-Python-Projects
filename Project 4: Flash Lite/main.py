"""
Flash-Learn: AI-Powered Study Cards
This app lets users paste a long paragraph of text, and the app uses an AI model (via Ollama or an API) to generate 5 flashcards (Question/Answer pairs) automatically.
"""
import requests
from flask import Flask, render_template, request, url_for, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flash.db'
db = SQLAlchemy(app)

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    date = db.Column(db.DateTime)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'))
    deck = db.relationship('Deck', backref='cards')

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)

def call_ollama(user_input):
    # Using 127.0.0.1 instead of localhost to avoid IPv6 issues on macOS
    url = "http://127.0.0.1:11434/api/generate"
    prompt = f"Create flashcards(any number of them) based on the following text: {user_input}. Return ONLY a JSON list of objects with 'q' and 'a' keys. Even if the text is short, find enough detail to make 5 distinct question/answer pairs. Do not include any other text."
    payload = {
        "model": "llama3:latest",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
    try:
        # Increase timeout to 90s for slower local LLMs
        response = requests.post(url, json=payload, timeout=90)
        response.raise_for_status()
        raw_response = response.json().get('response', '')
        
        # Clean the response in case the AI added markdown backticks
        clean_json = raw_response.strip()
        if clean_json.startswith("```json"):
            clean_json = clean_json[7:].strip()
        if clean_json.endswith("```"):
            clean_json = clean_json[:-3].strip()
        
        return json.loads(clean_json)
    except Exception as e:
        print(f"DEBUG: Ollama Error: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    return render_template('loading.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    content = data.get('content', '')
    
    if not content or not content.strip():
        return jsonify({"status": "error", "message": "No content provided"}), 400
        
    cards_data = call_ollama(content)
    
    if not cards_data:
        return jsonify({"status": "error", "message": "AI failed to generate flashcards. Check terminal for details."}), 500
    
    print(f"DEBUG: Received cards_data type: {type(cards_data)}")
    print(f"DEBUG: cards_data content: {cards_data}")

    # DEFENSIVE LOGIC: Ensure cards_data is a list
    final_list = []
    if isinstance(cards_data, list):
        final_list = cards_data
    elif isinstance(cards_data, dict):
        # Case: AI returned {"cards": [...]} or {"flashcards": [...]}
        for value in cards_data.values():
            if isinstance(value, list):
                final_list = value
                break
        # Case: AI returned a single object {"q": "...", "a": "..."}
        if not final_list and ('q' in cards_data or 'question' in cards_data):
            final_list = [cards_data]

    if not final_list:
        return jsonify({"status": "error", "message": "AI response format was invalid. Expected a list of cards."}), 500

    try:
        # Clear old cards and add new ones
        db.session.query(Cards).delete()
        for item in final_list:
            # Another safety check: ensure item is a dictionary
            if not isinstance(item, dict):
                continue
                
            q = item.get('q') or item.get('question') or 'No Question'
            a = item.get('a') or item.get('answer') or 'No Answer'
            new_card = Cards(
                question=q,
                answer=a,
                date=datetime.datetime.now()
            )
            db.session.add(new_card)
        db.session.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        db.session.rollback()
        print(f"DEBUG: Database Error: {e}")
        return jsonify({"status": "error", "message": f"Database error: {str(e)}"}), 500

@app.route('/api/cards')
def api_get_cards():
    try:
        cards = Cards.query.all()
        return jsonify([{"question": c.question, "answer": c.answer} for c in cards])
    except Exception as e:
        return jsonify([])

@app.route('/error')
def error_page():
    # Use 500 for server/AI errors
    error_code = request.args.get('code', '500')
    error_title = request.args.get('title', 'AI Error')
    error_message = request.args.get('message', 'An unexpected error occurred.')
    return render_template('error.html',
                         error_code=error_code,
                         error_title=error_title,
                         error_message=error_message)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html',
                         error_code='404',
                         error_title='Page Not Found',
                         error_message='Sorry, we couldn\'t find the page you\'re looking for.'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html',
                         error_code='500',
                         error_title='Something Went Wrong',
                         error_message='An unexpected error occurred.'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001, debug=True)

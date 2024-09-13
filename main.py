import os
from flask import Flask, render_template, jsonify, request
from models import Theme, Game, db
from sqlalchemy.sql.expression import func
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/new-game', methods=['GET'])
def new_game():
    theme = Theme.query.order_by(func.random()).first()
    words = random.sample(theme.words.split(','), 9)
    game = Game(theme=theme.name, words=','.join(words), attempts=0, hint_points=9)
    db.session.add(game)
    db.session.commit()
    return jsonify({
        'game_id': game.id,
        'theme': game.theme,
        'words': words,
        'attempts': game.attempts,
        'hint_points': game.hint_points
    })

@app.route('/api/check-word', methods=['POST'])
def check_word():
    data = request.json
    game = Game.query.get(data['game_id'])
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    word = data['word'].lower()
    game_words = game.words.split(',')
    
    if word in game_words:
        game.attempts += 1
        db.session.commit()
        return jsonify({'correct': True, 'attempts': game.attempts})
    else:
        game.attempts += 1
        db.session.commit()
        return jsonify({'correct': False, 'attempts': game.attempts})

@app.route('/api/get-hint', methods=['POST'])
def get_hint():
    data = request.json
    game = Game.query.get(data['game_id'])
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    if game.hint_points < 3:
        return jsonify({'error': 'Not enough hint points'}), 400
    
    word_index = data['word_index']
    game_words = game.words.split(',')
    if word_index < 0 or word_index >= len(game_words):
        return jsonify({'error': 'Invalid word index'}), 400
    
    hint = game_words[word_index][:2]
    game.hint_points -= 3
    db.session.commit()
    
    return jsonify({'hint': hint, 'hint_points': game.hint_points})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

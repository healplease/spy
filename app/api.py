from string import ascii_letters, digits

from flask import request, url_for

from app import app, db
from app.api_utils import success, error


@app.route('/api/v1', methods=['GET'])
def api():
    routes = [ 
        {
            'methods': list(rule.methods - {'HEAD', 'OPTIONS'}),    # removing methods we do not interested in
            'url': str(rule)  # print all endpoints
        }
        for rule in app.url_map.iter_rules()
        if str(rule).startswith('/api/v1') 
    ]
    return success(routes)


@app.route('/api/v1/games', methods=['GET'])
def api_get_games_list():
    query = {}
    projection = { '_id': 0 }
    games = list(db.games.find(query, projection, limit=100))

    return success(games)


@app.route('/api/v1/game/<game>', methods=['GET'])
def api_get_game(game):
    query = { 'gameId': game }
    projection = { '_id': 0 }
    game = db.games.find_one(query, projection)

    return success(game)


@app.route('/api/v1/game/<game_id>/create', methods=['POST'])
def api_create_game(game_id):
    query = { 'gameId': game_id } 
    projection = { '_id': 0 }
    game = db.games.find_one(query, projection)

    if game:
        return error(403, 'Game already exists.')

    new_game_id = game_id
    if not 4 <= len(new_game_id) <= 32:
        return error(403, f'Game ID length should be between {4} and {32}.')

    if not new_game_id.isidentifier():
        return error(403, f'Game ID can only contain letters, numbers, underscore ("_") and should not start with number.')

    document = { 
        'gameId': new_game_id 
    }
    db.games.insert_one(document)

    query = { 'gameId': game_id }
    projection = { '_id': 0 }
    game = db.games.find_one(query, projection)

    return success(game)


@app.route('/api/v1/game/<game>/join', methods=['POST'])
def api_join_game(game):
    query = { 'gameId': game }
    projection = { '_id': 0 }
    game = db.games.find_one(query, projection)

    if game:
        return error(404, 'This game does not exist.')

    return success({})


@app.route('/api/v1/game/<game>/start', methods=['POST'])
def api_start_game(game):
    return success({})
from string import ascii_letters, digits

from flask import request, url_for

from app import app, db, models
from app.models import User, Game
from utils.api import success, error


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


@app.route('/api/v1/game/<game_id>', methods=['GET'])
def api_get_game(game_id:str):
    try:
        game = Game(game_id)
        return success(game)
    except Exception as e:
        return error(404, str(e))


@app.route('/api/v1/game/<game_id>/create', methods=['POST'])
def api_create_game(game_id:str):
    try:
        game = Game.create(game_id)
        return success(game)
    except Exception as e:
        return error(403, str(e))


@app.route('/api/v1/game/<game_id>/join', methods=['POST'])
def api_join_game(game_id:str):
    return success({})


@app.route('/api/v1/game/<game_id>/start', methods=['POST'])
def api_start_game(game_id:str):
    return success({})
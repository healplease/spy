from flask import request, jsonify, url_for

from app import app, db

@app.route('/api', methods=['GET'])
def api():
    routes = [
        {
            'methods': list(rule.methods - {'HEAD', 'OPTIONS'}),    # removing methods we do not interested in
            'url': url_for(rule.endpoint, **(rule.defaults or {}))  # print all endpoints
        }
        for rule in app.url_map.iter_rules()
        if rule.endpoint.startswith('api') 
    ]
    return jsonify(
        status=True, 
        result=routes
    )

@app.route('/api/v1/games/', methods=['GET'])
def api_get_games_list():
    query = {}
    projection = { '_id': 0 }
    games = list(db.games.find(query, projection, limit=100))

    return jsonify(
        status=True,
        result=games
    )  


@app.route('/api/v1/game/<game>', methods=['GET'])
def api_get_game(game):
    query = { 'gameId': game }
    projection = { '_id': 0 }
    game = db.games.find_one(query, projection)

    return jsonify(
        status=bool(game),
        result=game
    )


@app.route('/api/v1/game/<game>/create', methods=['POST'])
def api_create_game(game):
    return jsonify()


@app.route('/api/v1/game/<game>/join', methods=['POST'])
def api_join_game(game):
    return jsonify()


@app.route('/api/v1/game/<game>/start', methods=['POST'])
def api_start_game(game):
    return jsonify()
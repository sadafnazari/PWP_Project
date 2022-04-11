from flask import (
    Blueprint, jsonify
)

from flask_jwt_extended import (jwt_required)

from api.db import get_game_by_name_or_id
from api.db import get_list_of_all_games


bp = Blueprint("game", __name__)


@bp.route("/games/<string:name_or_id>", methods=["GET"])
@jwt_required()
def get_game(name_or_id):
    """Returns the game by name or id.
    :parameters:
        name_or_id: string
            The name or id of the game to get.
    :returns:
        json:
            A json object containing the status of the request and the payload.
    """
    response = {
        "status": "",
        "payload": {},
    }
    game_to_return = get_game_by_name_or_id(name_or_id)
    if game_to_return:
        response["status"] = "ok"
        response["payload"] = game_to_return.__dict__
        return jsonify(response), 200
    response["status"] = "not found"
    return jsonify(response), 404


@bp.route("/games", methods=["GET"])
@jwt_required()
def get_all_games():
    """Returns all games.
    :parameters:
        None
    :returns:
        json:
            A json object containing the status of the request and the payload.
    """
    response = {
        "status": "",
        "payload": {},
    }
    
    response["status"] = "ok"
    response["payload"] = [game.__dict__ for game in get_list_of_all_games()]
    return jsonify(response), 200

from flask import Blueprint, jsonify, abort, request
from ..models import User, Post, Mypage, Like, Following, Comment, db
import hashlib
import secrets

bp = Blueprint('followings', __name__, url_prefix='/followings')


@bp.route('', methods=['GET'])
def index():
    followings = Following.query.all()
    result = []
    for f in followings:
        result.append(f.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    f = Following.query.get_or_404(id)
    return jsonify(f.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'following_id' not in request.json:
        return abort(400)

    f = Following(
        user_id=request.json['user_id'],
        following_id=request.json['following_id']
    )
    db.session.add(f)
    db.session.commit()
    return jsonify(f.serialize())


@bp.route('/<int:id>/<int:following_id>', methods=['DELETE'])
def delete(id: int, following_id: int):
    f = Following.query.get_or_404((id, following_id))
    try:
        db.session.delete(f)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

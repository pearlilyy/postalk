from flask import Blueprint, jsonify, abort, request
from ..models import User, Post, Mypage, Like, Following, Comment, db
import hashlib
import secrets

bp = Blueprint('likes', __name__, url_prefix='/likes')


@bp.route('', methods=['GET'])
def index():
    likes = Like.query.all()
    result = []
    for l in likes:
        result.append(l.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    l = Like.query.get_or_404(id)
    return jsonify(l.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'post_id' not in request.json:
        return abort(400)

    l = Like(
        user_id=request.json['user_id'],
        post_id=request.json['post_id']
    )
    db.session.add(l)
    db.session.commit()
    return jsonify(l.serialize())


@bp.route('/<int:id>/posts/<int:post_id>', methods=['DELETE'])
def delete(id: int, post_id: int):
    l = Like.query.get_or_404((id, post_id))
    try:
        db.session.delete(l)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

from flask import Blueprint, jsonify, abort, request
from ..models import User, Post, Mypage, Like, Following, Comment, db
import hashlib
import secrets

bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('', methods=['GET'])
def index():
    posts = Post.query.all()
    result = []
    for p in posts:
        result.append(p.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Post.query.get_or_404(id)
    return jsonify(p.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'note' not in request.json:
        return abort(400)

    p = Post(
        user_id=request.json['user_id'],
        note=request.json['note'],
        photo=request.json['photo'],
        location=request.json['location']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(p.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    p = Post.query.get_or_404(id)

    if 'user_id' in request.json:
        p.user_id = request.json['user_id']
    if 'note' in request.json:
        p.note = request.json['note']
    if 'photo' in request.json:
        p.photo = request.json['photo']
    if 'location' in request.json:
        p.location = request.json['location']

    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Post.query.get_or_404(id)
    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

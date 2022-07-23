from flask import Blueprint, jsonify, abort, request
from ..models import User, Post, Mypage, Like, Following, Comment, db
import hashlib
import secrets

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('', methods=['GET'])
def index():
    comments = Comment.query.all()
    result = []
    for c in comments:
        result.append(c.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Comment.query.get_or_404(id)
    return jsonify(c.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'content' not in request.json or 'commenter_id' not in request.json or 'post_id' not in request.json:
        return abort(400)

    c = Comment(
        content=request.json['content'],
        commenter_id=request.json['commenter_id'],
        post_id=request.json['post_id']
    )
    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    c = Comment.query.get_or_404(id)

    if 'content' in request.json:
        c.content = request.json['content']
    if 'commenter_id' in request.json:
        c.commenter_id = request.json['commenter_id']
    if 'post_id' in request.json:
        c.post_id = request.json['post_id']

    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    c = Comment.query.get_or_404(id)
    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

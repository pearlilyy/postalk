from flask import Blueprint, jsonify, abort, request
from ..models import User, Post, Mypage, Like, Following, Comment, db
import hashlib
import secrets

bp = Blueprint('mypages', __name__, url_prefix='/mypages')


@bp.route('', methods=['GET'])
def index():
    mypages = Mypage.query.all()
    result = []
    for m in mypages:
        result.append(m.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    m = Mypage.query.get_or_404(id)
    return jsonify(m.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json:
        return abort(400)

    m = Mypage(
        user_id=request.json['user_id'],
        introduction=request.json['introduction']
    )
    db.session.add(m)
    db.session.commit()
    return jsonify(m.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    m = Mypage.query.get_or_404(id)

    if 'user_id' in request.json:
        m.user_id = request.json['user_id']
    if 'introduction' in request.json:
        m.introduction = request.json['introduction']

    try:
        db.session.commit()
        return jsonify(m.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    m = Mypage.query.get_or_404(id)
    try:
        db.session.delete(m)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

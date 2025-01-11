from flask import Blueprint,request
from comment_app.controller.comment_controller import commentController

comment_bp = Blueprint('comment_bp',__name__)

@comment_bp.route('/api/add_comment',methods=['POST'])
def add_comment():
    data = request.get_json()
    return commentController.create_comment(data=data)

@comment_bp.route('/api/add_reply',methods=['POST'])
def add_reply():
    data = request.get_json()
    return commentController.reply_to_comment(data=data)

@comment_bp.route('/api/get_all_comments',method=['POST'])
def get_comments():
    post_id = request.get_json().post_id
    return commentController.get_comments(post_id=post_id)

from flask import jsonify
from comment_app.service.comment_service import commentService
from comment_app.views.comment_view import commentView

class commentController:

    @staticmethod
    def create_comment(data):
        user_id = data.get('user_id')
        post_id = data.get('post_id')
        content = data.get('content')
        result = commentService.add_comment(user_id, post_id, content)
        if result:
            return commentView.render_comment(),201


    @staticmethod   
    def reply_to_comment(data):
        user_id = data.get('user_id')
        comment_id = data.get('comment_id')
        content = data.get('content')

        result = commentService.add_reply(user_id, comment_id, content)
        if result:
            return commentView.render_reply(),201

    @staticmethod
    def get_comments(post_id):
        comments = commentService.fetch_comments(post_id)
        return commentView.render_comments(comments) , 200

from flask import jsonify
class commentView:
    @staticmethod
    def render_comment():
        return jsonify({'message':"Comment added successfully"})
    
    @staticmethod
    def render_reply():
        return jsonify({'message': "Reply added successfully"})
    
    @staticmethod
    def render_comments(comments):
        return jsonify(commentView.get_comment_json(comments))
    
    @staticmethod
    def get_comment_json(comments):
        return [{
            "comment_id": comment.comment_id,
                "user_id": comment.user_id,
                "post_id": comment.post_id,
                "content": comment.content,
                "created_at": comment.created_at.isoformat(),
        } for comment in comments ]
    

    
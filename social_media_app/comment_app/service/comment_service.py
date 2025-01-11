from shared.utils.db_utils import db
from shared.models.comment_model import Comment, Reply

class CommentService:
    @staticmethod
    def add_comment(user_id, post_id, content):
        new_comment = Comment(
            user_id=user_id,
            post_id=post_id,
            content=content
        )
        db.session.add(new_comment)
        db.session.commit()
        return True

    @staticmethod
    def add_reply(user_id, comment_id, content):
        new_reply = Reply (user_id=user_id,comment_id=comment_id,content=content)
        db.session.add(new_reply)
        db.session.commit()
        return True

    @staticmethod
    def fetch_comments(post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments

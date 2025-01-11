from shared.utils.db_utils import db
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, func

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Reply(db.Model):

    __tablename__ = 'replies'

    reply_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    comment_id = Column(Integer, ForeignKey('comments.comment_id', ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


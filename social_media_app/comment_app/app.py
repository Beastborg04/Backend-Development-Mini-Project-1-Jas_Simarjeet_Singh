import sys, os
sys.path.append(os.getcwd())

from comment_app.routes.comment_routes import comment_bp
from flask import Flask
from shared.utils.db_utils import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:coco_1234@localhost/social_media_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(comment_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

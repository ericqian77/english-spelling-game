from models import db, Theme
from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def init_db():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()

        # Check if themes already exist
        if Theme.query.first() is None:
            # Add initial themes and words
            themes = [
                ('Animals', 'cat,dog,bird,fish,lion,bear,tiger,elephant,monkey'),
                ('Colors', 'red,blue,green,yellow,purple,orange,pink,brown,white'),
                ('Fruits', 'apple,banana,orange,grape,mango,pear,cherry,lemon,kiwi'),
            ]

            for name, words in themes:
                theme = Theme(name=name, words=words)
                db.session.add(theme)

            db.session.commit()
            print("Database initialized with sample themes and words.")
        else:
            print("Database already contains themes. Skipping initialization.")

if __name__ == '__main__':
    init_db()

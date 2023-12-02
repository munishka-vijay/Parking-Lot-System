from flask import Flask
from database import db
from sqlalchemy import text

from utils.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app

app = create_app()

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def greeting():
    try:
        return 'Hello This is Parking Lot System'
    except Exception as err:
        return f'Error: {str(err)}'
    
@app.route("/test-db", methods = ["GET"])
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return 'Connected to DB Successfully'
    except Exception as err:
        return f'Error connected to DB: {str(err)}'
    
if __name__ == "__main__":
    app.run(debug = True)
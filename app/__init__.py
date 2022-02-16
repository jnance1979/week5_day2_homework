from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main.routes import main
    from app.pairs.routes import pairs
    

    app.register_blueprint(main)

    app.register_blueprint(pairs)

    return app


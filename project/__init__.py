from flask import Flask
from flask_login import LoginManager
import secrets
from extensions import db



def create_app():

    app = Flask(__name__)
    
    secret = secrets.token_hex(16)
    app.config['SECRET_KEY'] = secret

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    return app


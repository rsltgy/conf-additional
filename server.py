from flask import Flask
from sign_in import sign_in
from sign_up import sign_up
from log_out import log_out
from home import home
from flask_login.login_manager import LoginManager
from User import get_user
from upload import upload


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(sign_in)
    app.register_blueprint(log_out)
    app.register_blueprint(upload)
    app.register_blueprint(sign_up)
    app.config.from_object('settings')
    return app
login_manager = LoginManager()

def main():
    app = create_app()
    login_manager.init_app(app)
    login_manager.login_view = 'sign_in.sign_in_page'
    app.run(host='0.0.0.0', port=80, debug=True)

@login_manager.user_loader
def load_user(email):
    return get_user(email)
        
if __name__ == '__main__':
    main()
    
    

    
    
from config.config import Config

def authenticate_admin(login, password):
    return login == Config.ADMIN_LOGIN and password == Config.ADMIN_PASSWORD

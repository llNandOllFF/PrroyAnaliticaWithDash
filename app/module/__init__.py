from app.utils.constant.general import PORT
from .appDash import app
import os

def iniciar_dash():
    print("Iniciando App Dash")
    host = os.environ.get('DASH_HOST', '127.0.0.1')#variable for Docker
    app.run_server(host=host,debug=False, port=PORT)
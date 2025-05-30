from app.utils.constant.general import PORT
from .appDash import app

def iniciar_dash():
    print("Iniciando App Dash")
    app.run_server(debug=False, port=PORT)
import dash_bootstrap_components as dbc
from dash import Dash
from flask import Flask
from app.layout.appLayout import LayoutPage
import app.routers.router

server = Flask(__name__)
app = Dash(__name__,server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Proyecto Final - FLORES F"
app._favicon = "dev.ico"
app.layout = LayoutPage()

import dash_bootstrap_components as dbc
from dash import html

def appFooter():
    return dbc.Navbar(
        dbc.Container(
            [
                html.Span("© 2025 - Fernando Flores Fernandez",className="text-white"),
            ],
            fluid=True,
            style={"justifyContent":"center"}
        ),
        color="dark",
        dark=True,
        fixed="bottom",
        style={"height": "56px"},
    )
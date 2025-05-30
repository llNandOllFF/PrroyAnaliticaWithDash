import dash_bootstrap_components as dbc
from dash import html

def get_card_component(title,data):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4(title),
                            html.H4(data)
                        ]),
                        color="dark",
                        outline=True,
                        className= "text-dark",
                        style={"textAlign":"Center","margin-botton":"20px"}
                    ),
                    )
    return component
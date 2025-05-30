import dash_bootstrap_components as dbc

def appHeader():
    return dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("Proyecto Final con Dash")
            ],
            fluid=True,
        ),
        color="dark",
        dark=True,
        fixed="top",
        style={"height": "56px"},
    )
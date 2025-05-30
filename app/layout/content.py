from dash import html,dcc

def appContainer():
    return html.Div(
        [
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content'),
        ],
        className="content_style",
    )

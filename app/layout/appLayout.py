from dash import html

from app.layout.content import appContainer
from app.layout.footer import appFooter
from app.layout.header import appHeader
from app.layout.sidebar import appSidebar

def LayoutPage():
    return html.Div(
    [appHeader(), appSidebar(), appContainer(), appFooter()]
)
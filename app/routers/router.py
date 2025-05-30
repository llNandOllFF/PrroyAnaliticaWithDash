
from dash import callback, Output, Input

from app.module.dashBoard.pages.claseFinal import dashboardPage
from app.module.dashBoard.pages.trabajoFinalPercapita import trabajoFinalPercapitaPage
from app.module.dashBoard.pages.trabajoFinalPoblacional import trabajoFinalPoblacionalPage
from app.module.home.pages.home import homePage
from app.module.security.pages.notfound import NotFoundPage

@callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(link):
    switch = {
        '/': homePage,
        '/dashboard/clase6': dashboardPage,
        '/dashboard/trabajoFinal/poblacion': trabajoFinalPoblacionalPage,
        '/dashboard/trabajoFinal/percapita': trabajoFinalPercapitaPage,
    }
    return switch.get(link, NotFoundPage)()

@callback(
    Output("sidebar-accordion", "active_item"),
    Input("url", "pathname"),
)
def update_accordion(pathname):
    if "/dashboard" in pathname:
        return "Dashboard"
    return None

@callback(
    Output("sidebar-trabajoFinal-accordion", "active_item"),
    Input("url", "pathname"),
)
def update_accordion(pathname):
    if "/trabajoFinal" in pathname:
        return "TrabajoFinal"
    return None
import dash_bootstrap_components as dbc
from dash import html

def appSidebar():
    return html.Div(
        [
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact", className="navlink-style"),
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Clase 6", href="/dashboard/clase6", active="exact", className="navlink-style"),
                                    dbc.Accordion(
                                        [
                                            dbc.AccordionItem(
                                                [
                                                    dbc.NavLink("Poblacional", href="/dashboard/trabajoFinal/poblacion", active="exact", className="navlink-style"),
                                                    dbc.NavLink("Percapita", href="/dashboard/trabajoFinal/percapita", active="exact", className="navlink-style"),
                                                ],
                                                title="Trabajo Final",
                                                item_id="TrabajoFinal", 
                                            ),
                                        ],
                                        start_collapsed=True,
                                        flush=True,
                                        className="accordion-style",
                                        id="sidebar-trabajoFinal-accordion",
                                    ),
                                ],
                                title="Dashboard",
                                item_id="Dashboard", 
                            ),
                        ],
                        start_collapsed=True,
                        flush=True,
                        className="accordion-style",
                        id="sidebar-accordion",
                    ),
                    dbc.NavLink("Security", href="/security", active="exact", className="navlink-style"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="sidebar_style",
    )
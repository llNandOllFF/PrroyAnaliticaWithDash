import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

def selectControl(label, dropdown_id, lst_data, multiple=True, width=3):
    return dbc.Col(
        [
            html.Label(f'{label}:'),
            dcc.Dropdown(
                id=dropdown_id,
                options=[
                    {'label': 'Todos', 'value': -1},
                    *[{'label': value_Data, 'value': value_Data} for value_Data in lst_data]
                ],
                value=[-1] if multiple else -1,
                multi=multiple
            ),
        ],
        width=width
    )

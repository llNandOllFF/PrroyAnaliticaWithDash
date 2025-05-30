from dash import html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from app.components.select import selectControl
import copy
import json

data_global =  px.data.gapminder()
data_anual = px.data.gapminder()
lst_anios = sorted(data_global["year"].unique())
lst_continentes = sorted(data_global["continent"].unique())
lst_paises = sorted(data_global["country"].unique())
select_anios = []
select_continent = []
col_data = ["Pais","Continente","Año","Esperanza de Vida","Percapita","PIB per cápita"]

#print(sorted(geodata["continent"].unique()))

# if 2018 in data_g["year"].values:
#     gapminder_2018 = data_g.query("year == 2018")
# else:
#     gapminder_2018 = data_g

with open('app/utils/mock/continents.json') as f:
        geojson_continentes = json.load(f)

def GetPercapitaPorContinente(anios,continentes,paises):
    global select_continent, select_anios, select_pais

    select_anios = copy.deepcopy(lst_anios) if -1 in anios else anios
    select_continent = copy.deepcopy(lst_continentes) if -1 in continentes else continentes
    select_pais = copy.deepcopy(lst_paises) if -1 in paises else paises

    data_anual = data_global[data_global['year'].isin(select_anios) & data_global['continent'].isin(select_continent) & data_global['country'].isin(select_pais)]

    df_grouppercapita = data_anual.groupby("continent", as_index=False)["gdpPercap"].mean()
    df_percapita = data_global[data_global['year'].isin(select_anios) & data_global['continent'].isin(select_continent) & data_global['country'].isin(select_pais)]
    df_table = data_global[data_global["year"].isin(select_anios) &
                              data_global["continent"].isin(select_continent) &
                              data_global["country"].isin(select_pais)].sort_values(by=["continent", "country",'gdpPercap'],ascending=[True, True, False] )

    return df_grouppercapita,df_percapita,df_table.to_dict("records")

def GrafPercapitaPorContinente(df_grouppercapita,df_percapita):
    
    fig_bar = px.bar(df_grouppercapita, 
                     x="continent", 
                     y="gdpPercap",
                     title="Percapita Total por Continente",
                     labels={"gdpPercap": "Percapita", "continent": "Continente"},
                     color="continent")
    
    fig_map = px.choropleth(df_grouppercapita, 
                            geojson = geojson_continentes,
                            locations="continent",
                            featureidkey='properties.CONTINENT',
                            color="gdpPercap",
                            projection='natural earth',
                            labels={"gdpPercap": "Percapita", "continent": "Continente"},
                            title="Percapita Total por cada Continente",
                            )
    fig_box = px.box(df_percapita,
                     x="continent",
                     y='gdpPercap',
                     color="continent",
                     log_y=True,
                     title="Nivel de Percapita por Continente",
                     labels={"gdpPercap": "Percapita", "continent": "Continente"})
    return fig_bar,fig_map,fig_box

def trabajoFinalPercapitaPage():
    return dbc.Container(
        [
            html.H3(f"GAPMINDER DATA PERCAPITA",className='text-center text-success'),
            html.Hr(),
            dbc.Row([
                selectControl("Año","select-percapita-anio",lst_anios,True,3),
                selectControl("Continente","select-percapita-continente",lst_continentes,True,3),
                selectControl("Pais","select-percapita-pais",lst_paises,True,3),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure={},id="gdpPercap-anio-bar-percapita"), width=6,className="style-graf"),
                dbc.Col(dcc.Graph(figure={},id="continent-anio-choropleth-percapita"), width=6,className="style-graf"),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure={},id="gdpPercap-continent-box-percapita"),className="style-graf"),
            ]),
            html.Div([
                 html.H3("Datos"),
                 dash_table.DataTable(
                    columns=[{"name": col, "id": col} for col in data_global.columns],
                    data=data_global.to_dict("records"),
                    page_size=10,
                    style_table={"overflowX": "auto"},
                    id="table-gapminder-percapita"
                )
            ])
        ]
    )

@callback(
        Output("gdpPercap-anio-bar-percapita", "figure"),
        Output("continent-anio-choropleth-percapita", "figure"),
        Output("gdpPercap-continent-box-percapita", "figure"),
        Output("table-gapminder-percapita", "data"),
        [Input("select-percapita-anio", "value"), Input("select-percapita-continente", "value"),Input("select-percapita-pais", "value")]
    )
def UpdatePercapitaPorContinente(selected_anio, selected_continente,selected_pais):
    df_grouppercapita,df_percapita,df_table = GetPercapitaPorContinente(selected_anio,selected_continente,selected_pais)
    fig_bar,fig_map, fix_box = GrafPercapitaPorContinente(df_grouppercapita,df_percapita)
    return fig_bar,fig_map,fix_box,df_table


@callback(
        Output("select-percapita-pais", "options"),
        Output("select-percapita-pais", "value"),
        [Input("select-percapita-continente", "value")]
    )
def UpdateDataSelectControlPais(selected_continente):
    lst_filter = None
    val_data = [-1]
    if ((-1 in selected_continente) | (selected_continente is None) | (len(selected_continente) == 0 )):
         val_data = [-1]
         lst_filter = copy.deepcopy(lst_paises)
    else:
         val_data = []
         lst_filter = sorted(data_global[data_global["continent"].isin(selected_continente)]["country"].unique())

    lst_options = [{'label': 'Todos', 'value': -1}] + [{'label': valueData, 'value': valueData} for valueData in lst_filter]
    
    return lst_options,val_data
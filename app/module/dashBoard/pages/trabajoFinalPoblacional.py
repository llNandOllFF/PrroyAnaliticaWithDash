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
col_data = ["Pais","Continente","Año","Esperanza de Vida","Población","PIB per cápita"]

#print(sorted(geodata["continent"].unique()))

# if 2018 in data_g["year"].values:
#     gapminder_2018 = data_g.query("year == 2018")
# else:
#     gapminder_2018 = data_g

with open('app/utils/mock/continents.json') as f:
        geojson_continentes = json.load(f)

#features = geojson_continentes["features"]
#df_continentes = pd.json_normalize(features)

#print(sorted(df_continentes["properties.CONTINENT"].unique()))
#print(lst_continentes)

# df_continentes["properties.CONTINENT"] = df_continentes["properties.CONTINENT"].replace({
#     "North America": "Americas",
#     "South America": "Americas",
#     "Australia": "Oceania",
# })

# geojson_continentes["features"] = df_continentes.to_dict(orient="records")
# geojson = json.dumps(geojson_continentes, indent=2)

# with open("app/utils/mock/continentsMod.json", "w") as f:
#     f.write(geojson)

def GetPoblacionPorContinente(anios,continentes,paises):
    global select_continent, select_anios, select_pais

    select_anios = copy.deepcopy(lst_anios) if -1 in anios else anios
    select_continent = copy.deepcopy(lst_continentes) if -1 in continentes else continentes
    select_pais = copy.deepcopy(lst_paises) if -1 in paises else paises

    data_anual = data_global[data_global['year'].isin(select_anios) & data_global['continent'].isin(select_continent) & data_global['country'].isin(select_pais)]

    df_grouppoblacion = data_anual.groupby("continent", as_index=False)["pop"].sum()
    df_poblacion = data_global[data_global['year'].isin(select_anios) & data_global['continent'].isin(select_continent) & data_global['country'].isin(select_pais)]
    df_table = data_global[data_global["year"].isin(select_anios) &
                              data_global["continent"].isin(select_continent) &
                              data_global["country"].isin(select_pais)].sort_values(by=["continent", "country",'pop'],ascending=[True, True, False] )

    return df_grouppoblacion,df_poblacion,df_table.to_dict("records")

def GrafPoblacionPorContinente(df_grouppoblacion,df_poblacion):
    
    fig_bar = px.bar(df_grouppoblacion, 
                     x="continent", 
                     y="pop",
                     title="Población Total por Continente",
                     labels={"pop": "Población", "continent": "Continente"},
                     color="continent")
    
    fig_map = px.choropleth(df_grouppoblacion, 
                            geojson = geojson_continentes,
                            locations="continent",
                            featureidkey='properties.CONTINENT',
                            color="pop",
                            projection='natural earth',
                            labels={"pop": "Población", "continent": "Continente"},
                            title="Población Total por cada Continente",
                            )
    fig_box = px.box(df_poblacion,
                     x="continent",
                     y='pop',
                     color="continent",
                     log_y=True,
                     title="Nivel de Población por Continente",
                     labels={"pop": "Población", "continent": "Continente"})
    return fig_bar,fig_map,fig_box

def trabajoFinalPoblacionalPage():
    return dbc.Container(
        [
            html.H3(f"GAPMINDER DATA POBLACIONAL",className='text-center text-success'),
            html.Hr(),
            dbc.Row([
                selectControl("Año","select-anio",lst_anios,True,3),
                selectControl("Continente","select-continente",lst_continentes,True,3),
                selectControl("Pais","select-pais",lst_paises,True,3),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure={},id="pop-anio-bar"), width=6,className="style-graf"),
                dbc.Col(dcc.Graph(figure={},id="continent-anio-choropleth"), width=6,className="style-graf"),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure={},id="pop-continent-box"),className="style-graf"),
            ]),
            html.Div([
                 html.H3("Datos"),
                 dash_table.DataTable(
                    columns=[{"name": col, "id": col} for col in data_global.columns],
                    data=data_global.to_dict("records"),
                    page_size=10,
                    style_table={"overflowX": "auto"},
                    id="table-gapminder"
                )
            ])
        ]
    )

@callback(
        Output("pop-anio-bar", "figure"),
        Output("continent-anio-choropleth", "figure"),
        Output("pop-continent-box", "figure"),
        Output("table-gapminder", "data"),
        [Input("select-anio", "value"), Input("select-continente", "value"),Input("select-pais", "value")]
    )
def UpdatePoblacionPorContinente(selected_anio, selected_continente,selected_pais):
    df_grouppoblacion,df_poblacion,df_table = GetPoblacionPorContinente(selected_anio,selected_continente,selected_pais)
    fig_bar,fig_map, fix_box = GrafPoblacionPorContinente(df_grouppoblacion,df_poblacion)
    return fig_bar,fig_map,fix_box,df_table


@callback(
        Output("select-pais", "options"),
        Output("select-pais", "value"),
        [Input("select-continente", "value")]
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
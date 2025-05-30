from dash import html, dcc
import dash_bootstrap_components as dbc

def homePage():
   return dbc.Container([
      html.H3('DESARROLLO DE UNA APLICACION DASH',className='text-center text-success'),
      html.Hr(), 
      html.Div(
         [
            html.H5("📌 Descripción"),
            html.Div([
               html.H6("Esta es una aplicacion web interactiva desarrollada en Dash, una libreria de python para creacion de Dashboards"),
               html.H6('Su proposito es mostrar de una manera estructura datos y graficos que satisfagan las necesidades de la organización.'),
            ]),
            html.Br(),
            html.H5("🚀 Tecnologías utilizadas"),
            html.Div([
               html.Ul([
                  html.Li("Python"),
                  html.Li("Dash"),
                  html.Li("Plotly"),
                  html.Li("Pandas"),
                  html.Li("dash-bootstrap-components"),
                  html.Li("geopandas")
               ])
            ]),
            html.Br(),
            html.H5("📂 Estructura del proyecto"),
            html.Div([
               html.Ul(
                  [
                     html.Li(html.B("📂 proyecto")),
                     html.Li([html.B("│── 📄 app.py")," # Código principal de la aplicación Dash"]),
                     html.Li([html.B("│── 📄 requirements.txt")," # Lista de dependencias"]),
                     html.Li([html.B("│── 📄 README.md")," # Documentación del proyecto"]),
                     html.Li(html.B("│── 📂 app")),
                     html.Ul(
                        [
                           html.Li([html.B("│── 📁 components"), " # componentes reutilizables"]),
                           html.Li([html.B("│── 📁 layout"), " # estructura visual y diseño"]),
                           html.Li([html.B("│── 📁 modules"), " # módulos funcionales"]),
                           html.Ul([
                              html.Li([html.B("│── 📁 assets"), " # archivos estaticos"])
                           ],style= {'listStyle': 'none'}),
                           html.Li([html.B("│── 📁 routers"), " # rutas de navegación"]),
                           html.Li([html.B("│── 📁 utils"), " #  funciones auxiliares y herramientas de soporte"]),
                        ],style= {'listStyle': 'none'}),
                  ],
                  style= {'listStyle': 'none'}
               )
            ]),
            html.Br(),
            html.H5("🔧 Instalación y ejecución"),
            html.Div([
               html.Ul([
                  html.Li(html.H6("# Crear un entorno virtual")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "python -m venv .venv \n"
                        "```"
                     )],
                     className='markdown-style'
                  )),
                  html.Li(html.H6("# Activar entorno virtual")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        ".\.venv\Scripts\\activate \n"
                        "```"
                     )],
                     className='markdown-style'
                  )),
                  html.Li(html.H6("# Ejecutar la aplicación")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "python main.py \n"
                        "```"
                     ),
                     html.P("*Al ejecutar la aplicación, se instalaran las dependencias automaticamente*")],
                     className='markdown-style'
                  )),
                  html.Li(html.H6("# App disponible en:")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "http://127.0.0.1:8050/ \n"
                        "```"
                     )],
                     className='markdown-style'
                  ))
               ],style= {'listStyle': 'none'})
            ]),
            html.Br(),
            html.H5("🐳 Dockerización"),
            html.Div([
               html.Ul([
                  html.Li(html.P("*Ya existe el archivo Dockerfile*")),
                  html.Li(html.H6("# Generar el docker build")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "docker build -t @{user}/@{nameImage}:@{version} . \n"
                     ),
                     html.P('ejem: docker build -t llnandollff90/reporte-dash:1 .')
                     ],
                     className='markdown-style'
                  )),
                  html.Li(html.H6("# Correr el docker build")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "docker run -p {hostLocal}:{contenedorHost} @{user}/@{nameImage}:@{version} \n"
                     ),
                     html.P('ejem: docker run -p 8050:8050 llnandollff90/reporte-dash:1')
                     ],
                     className='markdown-style'
                  )),
                  html.Li(html.H6("# App disponible en Local:")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "http://127.0.0.1:8050/ \n"
                        "```"
                     )],
                     className='markdown-style'
                  )),
                  html.Li(html.H6("# App disponible internamente del Contenedor:")),
                  html.Ul(html.Div([
                     dcc.Markdown(
                        "```python\n"
                        "http://172.17.0.2:8050/ \n"
                        "```"
                     )],
                     className='markdown-style'
                  ))
               ],style= {'listStyle': 'none'})
            ]),
            html.Br(),
            html.H5("✍️ Autor"),
            html.Div([
               html.Ul([
                  html.Li(html.B("Fernando Flores Fernandez")),
                  html.Li([html.B("📅 Año:")," 2025"]),
                  html.Li([html.B("📧 Contacto:"), " ''"]),
                  html.Li([html.B("📂 GitHub:")," ''"])
               ],style= {'listStyle': 'none'})
            ])
         ]
      )
   ])
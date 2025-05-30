📌 Descripción
    
    Esta es una aplicacion web interactiva desarrollada en Dash, una libreria de python para creacion de Dashboards
    Su proposito es mostrar de una manera estructura datos y graficos que satisfagan las necesidades de la organización.

🚀 Tecnologías utilizadas
    
    Python
    Dash
    Plotly
    Pandas
    dash-bootstrap-components
    geopandas

📂 Estructura del proyecto
    
    📂 proyecto
    │── 📄 app.py # Código principal de la aplicación Dash
    │── 📄 requirements.txt # Lista de dependencias
    │── 📄 README.md # Documentación del proyecto
    │── 📂 app
        │── 📁 components # componentes reutilizables
        │── 📁 layout # estructura visual y diseño
        │── 📁 modules # módulos funcionales
            │── 📁 assets # archivos estaticos
        │── 📁 routers # rutas de navegación
        │── 📁 utils # funciones auxiliares y herramientas de soporte

🔧 Instalación y ejecución
    
    # Crear un entorno virtual
    python -m venv .venv 
    
    # Activar entorno virtual
    .\.venv\Scripts\activate 
    
    # Ejecutar la aplicación
    python main.py 
    
    *Al ejecutar la aplicación, se instalaran las dependencias automaticamente*

    # App disponible en:
    http://127.0.0.1:8050/ 

🐳 Dockerización
    
    *Ya existe el archivo Dockerfile*
    
    # Generar la build
    docker build -t @{user}/@{nameImage}:@{version} .
    
    # Correr el docker build
    docker run -p 8050:8050 @{user}/@{nameImage}:@{version}
    
    # Acceder a la web (localmente)
    http://localhost:8050/
    
    # Acceder a la web (internamente - docker)
    http://172.17.0.2:8050

✍️ Autor
    
    🧑‍💻Fernando Flores Fernandez
        📅 Año: 2025
        📧 Contacto: ''
        📂 GitHub: ''
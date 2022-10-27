# _PROYECTO JAHAPY_

# Descripcion
Proyecto presentado en la Hackathon de octubre en Penguin Academy. El tema fue "Generar herramientas tecnologicas que fomenten o mejoren la experiencia turistica en Paraguay". Abordamos la problematica de la desinformacion, y nuestra solucion propone el conocimiento y geolocalizacion de lugares culturales para fomentar que la gente conozca nuestro pais a traves de nuestra cultura. 

El proyecto cuenta con dos ejes principale, el mapa que permite localizar en donde quedan los museos y espacios historicos de nuestro pais, y una seccion infromativa que nos habla de la riqueza cultural de cada uno de los departamentos, asi como la descripcion de los lugares disponibles en el mapa. 

# Tecnologias 

- Python
- Folium 
- SQL Alchemy 
- HTML
- Tailwind CSS

# Instalacion

1. Crear un entorno virtual
   `python3 -m venv venv `
2. Activar el entorno virtual
   `source ./venv/bin/activate `
3. Instalar los requisitos
   ` pip install -r requirements.txt`
4. Ejecutar el archivo `app.py`

# Archivos.

## Archivos HTML.
`index.html` Pagina principal del proyecto. 

`form_categorias.html`
Contiene el formulario para filtrar los lugares culturales por categorias y el iframe al mapa con la vista filtrada, que se genero en `vista_filtrada.html` .

`lista_lugar.html`
Genera una lista de todos los lugares culturales guardados en la base de datos.

`mapa_registro.html`
Contiene un formulario para cargar los lugares culturales a la base de datos.

`mapa.html`
Genera un mapa con marcadores en todas las posiciones guardadas en la base de datos.

## Endpoints.

- `/` Renderiza `index.html`
- `/mapa` Renderiza `mapa.html`
- `/registro` Renderiza `mapa_registro.html`
- `/lista-lugares` Renderiza
- `/filtro` Renderiza `form_categorias.html`

# Grupo.

## Integrantes

- Laura Acosta
- Cynthia
- Wendy Solis
- Natalia Muñoz
- Ivonne Livieres
- Alana

## Mentoras

- Tamara Cantero
- Jazmin Gamarra

Asuncion, Paraguay - 26/10/22

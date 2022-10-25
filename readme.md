# _PROYECTO JAHAPY_

# Descripcion

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

`form_categorias.html`
Contiene el formulario para filtrar los lugares culturales por categorias y el iframe al mapa con la vista filtrada, que se genero en `vista_filtrada.html` .

`lista_lugar.html`
Genera una lista de todos los lugares culturales guardados en la base de datos.

`mapa_registro.html`
Contiene un formulario para cargar los lugares culturales a la base de datos.

`mapa.html`
Genera el mapa con marcadores en todas las posiciones guardadas en la base de datos.

## Endpoints.

- `/` Renderiza `mapa.html`
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

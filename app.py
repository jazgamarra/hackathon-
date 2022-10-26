from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import folium
from geopy.geocoders import Nominatim

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db=SQLAlchemy(app)

class LugaresCulturales(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100), nullable=False)
    descripcion=db.Column(db.String(200), nullable=False)
    imagen=db.Column(db.String, nullable=False)
    categoria=db.Column(db.String(50), nullable=False)
    latitud=db.Column(db.Float, nullable=False)
    longitud=db.Column(db.Float, nullable=False)
    departamento=db.Column(db.String(80))

    def __init__(self, nombre, descripcion, imagen, categoria, latitud, longitud, departamento):
        self.nombre=nombre
        self.descripcion=descripcion
        self.imagen=imagen
        self.categoria=categoria
        self.latitud=latitud
        self.longitud=longitud
        self.departamento=departamento


@app.route('/mapa')
def crear_mapa():
    mapa=folium.Map(location=[-23.765547, -57.475052], zoom_start=6)
    lista=LugaresCulturales.query.all()
    for lugar in lista:
        folium.Marker(
            location=[lugar.latitud,lugar.longitud], 
            popup=f'''
            <img src="{lugar.imagen}" width="300" height="200" class="center">
            <h2>{lugar.nombre}</h2>
            <p>{lugar.descripcion}</p>
            ''', 
                icon=folium.Icon(color="red", icon="heart-empty"),
            ).add_to(mapa)
        folium.Circle(
            location=[lugar.latitud,lugar.longitud],
            radius=120, 
            fill_color='darkred', 
            fill_opacity=0.1, 
            color='none'
        ).add_to(mapa)
    mapa.save('templates/mapa.html')
    return render_template('mapa.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method=='POST':
        nombre=request.form['nombre']
        descripcion=request.form['descripcion']
        imagen=request.form['imagen']
        categoria=request.form['categoria']
        latitud=request.form['latitud']
        longitud=request.form['longitud']
        departamento=request.form['departamento']
    

        lugar=LugaresCulturales(nombre, descripcion, imagen, categoria, latitud, longitud, departamento)
        print(lugar.nombre, lugar.descripcion)
        db.session.add(lugar)
        db.session.commit()

    return render_template('mapa_registro.html')

@app.route('/borrar/<int:id>')
def borrar(id):
    lugar = LugaresCulturales.query.get(id)
    db.session.delete(lugar)
    db.session.commit()
    return redirect(url_for('listar'))

@app.route('/filtro', methods=['GET','POST'])
def filtrar():
    #definir en que parte del mapa el zoom
    mapa=folium.Map(location=[-23.765547, -57.475052], zoom_start=6)
    #post es que le llega algo del front al back
    if request.method=='POST':
        #crear una variable con lo que llego del front
        categoria_form=request.form['categoria']
        #consultar los lugares culturales
        consultar_lugar=db.session.query(LugaresCulturales)
        #definimos que variables deben coincidir
        filtro_por_categoria=LugaresCulturales.categoria==categoria_form
        #filtrar con el filtro que definimos arriba
        lista_lugares=consultar_lugar.filter(filtro_por_categoria).all()

        for lugar in lista_lugares:
            coor_marcador=[lugar.latitud, lugar.longitud]
            folium.Marker(
            location=coor_marcador, 
            popup=f'''
            <img src="{lugar.imagen}" width="300" height="200" class="center">
            <h2>{lugar.nombre}</h2>
            <p>{lugar.descripcion}</p>
            ''', 
                icon=folium.Icon(color="red", icon="heart-empty"),
            ).add_to(mapa)
        folium.Circle(
            location=[lugar.latitud,lugar.longitud],
            radius=120, 
            fill_color='darkred', 
            fill_opacity=0.1, 
            color='none'
        ).add_to(mapa)

    #guardamos en un html distinto
    mapa.save('templates/vista_filtrada.html')
    return render_template('form_categorias.html')

@app.route('/vista-filtrada')
def vista_filtrada():
    return render_template('vista_filtrada.html')

@app.route('/', methods=['GET','POST'])
def index():
    #definir en que parte del mapa el zoom
    mapa=folium.Map(location=[-23.765547, -57.475052], zoom_start=7)
    #post es que le llega algo del front al back
    if request.method=='POST':
        #crear una variable con lo que llego del front
        categoria_form=request.form['categoria']
        #consultar los lugares culturales
        consultar_lugar=db.session.query(LugaresCulturales)
        #definimos que variables deben coincidir
        filtro_por_categoria=LugaresCulturales.categoria==categoria_form
        #filtrar con el filtro que definimos arriba
        lista_lugares=consultar_lugar.filter(filtro_por_categoria).all()

        for lugar in lista_lugares:
            coor_marcador=[lugar.latitud, lugar.longitud]
            folium.Marker(
            location=coor_marcador, 
            popup=f'''
            <img src="{lugar.imagen}" width="300" height="200" class="center">
            <h2>{lugar.nombre}</h2>
            <p>{lugar.descripcion}</p>
            ''', 
                icon=folium.Icon(color="red", icon="heart-empty"),
            ).add_to(mapa)
        folium.Circle(
            location=[lugar.latitud,lugar.longitud],
            radius=120, 
            fill_color='darkred', 
            fill_opacity=0.1, 
            color='none'
        ).add_to(mapa)
    else: 
        lista=LugaresCulturales.query.all()
        for lugar in lista:
            folium.Marker(
                location=[lugar.latitud,lugar.longitud], 
                popup=f'''
                <img src="{lugar.imagen}" width="300" height="200" class="center">
                <h2>{lugar.nombre}</h2>
                <p>{lugar.descripcion}</p>
                ''', 
                    icon=folium.Icon(color="red", icon="heart-empty"),
                ).add_to(mapa)
            folium.Circle(
                location=[lugar.latitud,lugar.longitud],
                radius=120, 
                fill_color='darkred', 
                fill_opacity=0.1, 
                color='none'
            ).add_to(mapa)
        mapa.save('templates/mapa.html')
    #guardamos en un html distinto
    mapa.save('templates/vista_filtrada.html')
    
    # crear una lista con todos los lugares 
    lista=LugaresCulturales.query.all()
        
    # retornamos el index 
    return render_template('index.html', lista=lista)
 
@app.route('/lista-lugares')
def listar():
    lista =  LugaresCulturales.query.all() 
    return render_template('lista_lugar.html', lista=lista)

    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    
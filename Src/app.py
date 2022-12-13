from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyectocrud'
# desde el objeto app configuro la URI de la BBDD    user:clave@localhost/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 
db= SQLAlchemy(app)
ma=Marshmallow(app)
 
# defino la tabla
class Receta(db.Model):       
    id=db.Column(db.Integer, primary_key=True)  
    imagen=db.Column(db.String(900))
    nombre=db.Column(db.String(100))
    descripcion=db.Column(db.String(800))
    def __init__(self,imagen,nombre,descripcion):
        self.imagen=imagen 
        self.nombre=nombre   
        self.descripcion=descripcion
        
with app.app_context():
    db.create_all() 
#  ************************************************************
class RecetaSchema(ma.Schema):
    class Meta:
        fields=('id','imagen','nombre','descripcion')
receta_schema=RecetaSchema()          
recetas_schema=RecetaSchema(many=True)  
 
@app.route('/recetas',methods=['GET'])
def get_recetas():
    all_recetas=Receta.query.all()   
    result=recetas_schema.dump(all_recetas) 
    return jsonify(result)
 
@app.route('/recetas/<id>',methods=['GET'])
def get_receta(id):
    receta=Receta.query.get(id)
    return receta_schema.jsonify(receta)
 
@app.route('/recetas/<id>',methods=['DELETE'])
def delete_receta(id):
    receta=Receta.query.get(id)
    db.session.delete(receta)
    db.session.commit()
    return receta_schema.jsonify(receta)

@app.route('/recetas', methods=['POST']) # crea ruta o endpoint
def create_receta():
    print(request.json)  # request.json contiene el json que envio el cliente
    imagen=request.json['imagen']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    new_receta=Receta(imagen,nombre,descripcion)
    db.session.add(new_receta)
    db.session.commit()
    return receta_schema.jsonify(new_receta)

 
@app.route('/recetas/<id>' ,methods=['PUT'])
def update_receta(id):
    receta=Receta.query.get(id)
   
    imagen=request.json['imagen']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
 
    receta.imagen=imagen
    receta.nombre=nombre
    receta.descripcion=descripcion
    db.session.commit()
    return receta_schema.jsonify(receta)




# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)  

from config.config import crearbd
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship

class Marca(crearbd):
    __tablename__="Marca"
    id=Column(Integer,primary_key=True,index=True)
    descripcion=Column(String(20),nullable=False)

class Vehiculo(crearbd):
    __tablename__="Vehículo"
    id=Column(Integer,primary_key=True,index=True)
    modelo=Column(String(40),nullable=False)
    año_fabricacion=Column(Integer,nullable=False)
    peso=Column(Float,nullable=False)
    capacidad_motor=Column(Integer,nullable=False)
    id_marca=Column(Integer,ForeignKey('Marca.id'),nullable=False)


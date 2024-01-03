from config.config import ls
from models.models import Marca,Vehiculo
from schemas.schemas import MarcaOut,VehOut,MarcaIn,VehIn
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List

taller = APIRouter()

def get_db():
    db=ls()
    try:
        yield db
    finally:
        db.close()

@taller.get('/taller/marca/{id}', response_model=MarcaOut, status_code=status.HTTP_200_OK)
def get_marca(id: int, db: Session = Depends(get_db)):
    with db.begin():
        marca = db.query(Marca).filter(Marca.id == id).first()
        if marca is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Modelo no encontrado')
        marca_out = MarcaOut(id=marca.id, descripcion=marca.descripcion)
        return marca_out

@taller.get('/taller/vehiculo/{id}', response_model=VehOut, status_code=status.HTTP_200_OK)
def get_veh(id: int, db: Session = Depends(get_db)):
    with db.begin():
        vehiculo = db.query(Vehiculo).filter(Vehiculo.id == id).first()
        if vehiculo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Modelo no encontrado')
        vehiculo_out = VehOut(
            id=vehiculo.id,
            modelo=vehiculo.modelo,
            año_fabricacion=vehiculo.año_fabricacion,
            peso=vehiculo.peso,
            capacidad_motor=vehiculo.capacidad_motor,
            id_marca=vehiculo.id_marca
        )
        return vehiculo_out

@taller.get('/taller/marca', response_model=List[MarcaOut], status_code=status.HTTP_200_OK)
def getmarcas(db: Session = Depends(get_db)):
    with db.begin():
        marcas = db.query(Marca).all()
        if len(marcas) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Modelo no encontrado')
        marcas_out = [MarcaOut(id=marca.id, descripcion=marca.descripcion) for marca in marcas]
        return marcas_out

@taller.get('/taller/vehiculo', response_model=List[VehOut], status_code=status.HTTP_200_OK)
def getvehs(db: Session = Depends(get_db)):
    with db.begin():
        vehiculos = db.query(Vehiculo).all()
        if len(vehiculos) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Modelo no encontrado')
        vehiculos_out = [
            VehOut(
                id=vehiculo.id,
                modelo=vehiculo.modelo,
                año_fabricacion=vehiculo.año_fabricacion,
                peso=vehiculo.peso,
                capacidad_motor=vehiculo.capacidad_motor,
                id_marca=vehiculo.id_marca
            ) for vehiculo in vehiculos
        ]
        return vehiculos_out

@taller.post('/taller/marca', response_model=MarcaIn, status_code=status.HTTP_201_CREATED)
def addmarca(marca: MarcaIn, db: Session = Depends(get_db)):
    nmarca = Marca(descripcion=marca.descripcion)
    db.add(nmarca)
    db.commit()
    db.refresh(nmarca)
    return nmarca

@taller.post('/taller/vehiculo',response_model=VehIn,status_code=status.HTTP_201_CREATED)
def addveh(vehiculo:VehIn,db:Session=Depends(get_db)):
    nvehiculo=Vehiculo(
                modelo=vehiculo.modelo,
                año_fabricacion=vehiculo.año_fabricacion,
                peso=vehiculo.peso,
                capacidad_motor=vehiculo.capacidad_motor,
                id_marca=vehiculo.id_marca)
    db.add(nvehiculo)
    db.commit()
    db.refresh(nvehiculo)
    return nvehiculo

@taller.delete('/taller/marca/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_marca(id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == id).first()
    if marca is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Marca no encontrada')
    db.delete(marca)
    db.commit()
    return


@taller.delete('/taller/vehiculo/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_marca(id: int, db: Session = Depends(get_db)):
    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == id).first()
    if vehiculo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Marca no encontrada')
    db.delete(vehiculo)
    db.commit()
    return

@taller.put('/taller/marca/{id}', response_model=MarcaIn, status_code=status.HTTP_200_OK)
def update_marca(id: int, marca_in: MarcaIn, db: Session = Depends(get_db)):
    existing_marca = db.query(Marca).filter(Marca.id == id).first()
    if existing_marca is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Marca no encontrada')
    existing_marca.descripcion = marca_in.descripcion
    db.commit()
    return existing_marca

@taller.put('/taller/vehiculo/{id}', response_model=VehIn, status_code=status.HTTP_200_OK)
def update_vehiculo(id: int, vehiculo_in: VehIn, db: Session = Depends(get_db)):
    existing_vehiculo = db.query(Vehiculo).filter(Vehiculo.id == id).first()
    if existing_vehiculo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vehículo no encontrado')
    existing_vehiculo.modelo = vehiculo_in.modelo
    existing_vehiculo.año_fabricacion = vehiculo_in.año_fabricacion
    existing_vehiculo.peso = vehiculo_in.peso
    existing_vehiculo.capacidad_motor = vehiculo_in.capacidad_motor
    existing_vehiculo.id_marca = vehiculo_in.id_marca
    db.commit()
    return existing_vehiculo
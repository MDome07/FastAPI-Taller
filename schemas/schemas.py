from pydantic import BaseModel
from typing import Optional

class MarcaOut(BaseModel):
    id: Optional[int]=None
    descripcion: str

class VehOut(BaseModel):
    id: Optional[int]=None
    modelo: str
    año_fabricacion: int
    peso: float
    capacidad_motor: int
    id_marca: int

class MarcaIn(BaseModel):
    id: int
    descripcion: str

class VehIn(BaseModel):
    id: int
    modelo: str
    año_fabricacion: int
    peso: float
    capacidad_motor: int
    id_marca: int
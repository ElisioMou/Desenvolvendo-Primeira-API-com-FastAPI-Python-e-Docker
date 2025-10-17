from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float, Column, CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from workout_api.contrib.models import BaseModel
import uuid

Base = declarative_base()

class CategoriaModel(Base):
    __tablename__ = 'categorias'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), unique=True, nullable=False)
    id = Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
     # Relacionamento 1:1 com Atleta
    atleta = relationship(
        "AtletaModel", 
        back_populates="categoria", 
        lazy='selectin',
        uselist=False  # ← IMPORTANTE para 1:1
    )
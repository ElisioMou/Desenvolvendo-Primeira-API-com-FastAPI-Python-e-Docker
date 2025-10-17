from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float, Column, CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from workout_api.contrib.models import BaseModel
import uuid

Base = declarative_base()

class AtletaModel(Base):
    __tablename__ = 'atletas'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    idade = Column(Integer, nullable=False)
    id = Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Foreign Keys para os relacionamentos 1:1
    categoria_id = Column(Integer, ForeignKey('categorias.pk_id'), unique=True, nullable=False)
    centro_treinamento_id = Column(Integer, ForeignKey('centros_treinamento.pk_id'), unique=True, nullable=False)
    
    # Relacionamentos 1:1
    categoria = relationship(
        "CategoriaModel", 
        back_populates="atleta", 
        lazy='selectin',
        uselist=False  # ← IMPORTANTE para 1:1
    )

    centro_treinamento = relationship(
        "CentroTreinamentoModel", 
        back_populates="atleta", 
        lazy='selectin',
        uselist=False  # ← IMPORTANTE para 1:1
    )
       
  
    
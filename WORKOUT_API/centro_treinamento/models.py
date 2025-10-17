from datetime import datetime
from lib2to3.pytree import Base
import uuid
from sqlalchemy import CHAR, Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(Base):
    __tablename__ = 'centros_treinamento'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)
    id = Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relacionamento 1:1 com Atleta
    atleta = relationship(
        "AtletaModel", 
        back_populates="centro_treinamento", 
        lazy='selectin',
        uselist=False  # ← IMPORTANTE para 1:1
    )
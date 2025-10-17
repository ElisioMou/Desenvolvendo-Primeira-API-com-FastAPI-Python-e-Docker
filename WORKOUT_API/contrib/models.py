from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class CategoriaModel(Base):
    __tablename__ = 'categorias'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relacionamento 1:1
    atleta = relationship(
        "AtletaModel", 
        back_populates="categoria", 
        uselist=False
    )

class CentroTreinamentoModel(Base):
    __tablename__ = 'centros_treinamento'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relacionamento 1:1
    atleta = relationship(
        "AtletaModel", 
        back_populates="centro_treinamento", 
        uselist=False
    )

class AtletaModel(Base):
    __tablename__ = 'atletas'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    idade = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Foreign Keys para relacionamentos 1:1
    categoria_id = Column(Integer, ForeignKey('categorias.pk_id'), unique=True, nullable=False)
    centro_treinamento_id = Column(Integer, ForeignKey('centros_treinamento.pk_id'), unique=True, nullable=False)
    
    # Relacionamentos 1:1
    categoria = relationship(
        "CategoriaModel", 
        back_populates="atleta", 
        uselist=False
    )
    
    centro_treinamento = relationship(
        "CentroTreinamentoModel", 
        back_populates="atleta", 
        uselist=False
    )
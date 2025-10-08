from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    # Use string reference
    atleta: Mapped['AtletaModel'] = relationship( # pyright: ignore[reportUndefinedVariable]
        'AtletaModel',
        back_populates="categoria",
        lazy='selectin'
    )
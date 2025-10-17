from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys

# Adiciona o diretório raiz ao Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import base model
from workout_api.contrib.models import BaseModel

# Importe os módulos para registrar os modelos
import workout_api.atleta.models
import workout_api.categorias.models
import workout_api.centro_treinamento.models

config = context.config
target_metadata = BaseModel.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
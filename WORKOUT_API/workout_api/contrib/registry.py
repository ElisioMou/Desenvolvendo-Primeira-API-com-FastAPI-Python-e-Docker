"""
Registry para centralizar imports dos modelos e evitar circular imports
"""
from workout_api.contrib.models import BaseModel

# Esta importação garante que todos os modelos sejam registrados
def import_all_models():
    # Importe todos os módulos de modelos aqui
    from workout_api import atleta
    from workout_api import centro_treinamento
    from workout_api import categorias
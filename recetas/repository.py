from .db import get_database
from .models import Receta


def obtener_receta() -> Receta | None:
    db = get_database()
    coleccion = db["recetas_examen"]
    documento = coleccion.find_one()
    if documento is None:
        return None
    return Receta.from_document(documento)

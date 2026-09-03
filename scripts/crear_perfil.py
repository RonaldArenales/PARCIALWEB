import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from recetas.db import get_database


def crear_perfil():
    db = get_database()
    coleccion = db["asistencias"]

    documento = {
        "nombre": "Ronald Arenales Peña",
        "idUniversidad": "000524580",
        "lenguajeFavorito": "Python",
    }

    resultado = coleccion.insert_one(documento)
    print(f"Documento creado en 'asistencias' con _id: {resultado.inserted_id}")


if __name__ == "__main__":
    crear_perfil()

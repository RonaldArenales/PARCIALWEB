from dataclasses import dataclass, field


@dataclass
class Ingrediente:
    nombre: str
    cantidad: float
    unidad: str


@dataclass
class Origen:
    region: str
    pais: str


@dataclass
class Receta:
    nombre: str
    tipo_cocina: str
    tiempo_preparacion: str
    ingredientes: list[Ingrediente] = field(default_factory=list)
    origen: Origen | None = None

    @classmethod
    def from_document(cls, doc: dict) -> "Receta":
        ingredientes = [
            Ingrediente(
                nombre=i.get("nombre", ""),
                cantidad=i.get("cantidad", 0),
                unidad=i.get("unidad", ""),
            )
            for i in doc.get("ingredientes", [])
        ]

        origen_doc = doc.get("origen") or {}
        origen = Origen(
            region=origen_doc.get("region", ""),
            pais=origen_doc.get("pais", ""),
        )

        return cls(
            nombre=doc.get("nombre", ""),
            tipo_cocina=doc.get("tipoCocina", ""),
            tiempo_preparacion=doc.get("tiempoPreparacion", ""),
            ingredientes=ingredientes,
            origen=origen,
        )

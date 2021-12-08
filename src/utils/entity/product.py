from dataclasses import dataclass, field

from nova_api.entity import Entity


@dataclass
class Product(Entity):
    cotas: int = field(default=1, metadata={"default": "NOT NULL"})
    cota_price: int = field(default=100, metadata={"default": "NOT NULL"})
    remaining_cotas: int = field(default=None,
                                 metadata={"default": "NOT NULL"})
    name: str = field(default="Awesome gift")
    description: str = field(default="This is an awesome gift to give us.",
                             metadata={"type": "TEXT"})
    picture_url: str = field(default=None, metadata={"type": "TEXT"})

    def __post_init__(self):
        if self.remaining_cotas is None:
            self.remaining_cotas = self.cotas

    def simple_visualization(self):
        return {"id_": self.id_,
                "cota_price": self.cota_price,
                "remaining_cotas": self.remaining_cotas,
                "name": self.name,
                "picture_url": self.picture_url}

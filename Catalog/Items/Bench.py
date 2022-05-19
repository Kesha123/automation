from Catalog.Items.Item import Item

class Bench(Item):

    bench_count: int = 1

    def __init__(self, x: float = 500, y: float = 1500, rotation: float = 45, name: str = "bench") -> None:
        super().__init__(x, y, name, rotation)
        self.link =  "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(10)" if self.id == 2 else "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(10)"

    def __str__(self) -> str:
        return str(dict([("X", self.x), ("Y", self.y), ("Rotation", self.rotation), ("Id", self.id)]))
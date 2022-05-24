from enum import Enum
from Catalog.Catalogue import Catalogue
from Catalog.Items.Item import Item
from Catalog.Lines.Line import Line
from Palette.Properties import LengthProperty


class Bench(Item):

    bench_count: int = 1

    def __init__(self, x: float = 500, y: float = 1500, rotation: float = 45, name: str = "bench", **kwargs) -> None:
        super().__init__(x, y, name, rotation)
        self.extra_properties = kwargs
        self.link =  f"{Catalogue.CATALOG.value} > {Catalogue.BENCH.value}" if (Item.count_items == 1 or Line.count_lines == 1) else f"{Catalogue.CATALOG_ALTER.value} > {Catalogue.BENCH.value}"

    def set_properties(self, driver) -> None:
        super().set_properties(driver)
        if self.extra_properties.get("altitude"):
            property = LengthProperty("altitude",".PropertyLengthMeasure", self.extra_properties.get("altitude")).set_property(driver)

    def place_item(self, driver):
        super().place_item(driver)
        self.set_properties(driver)

    def __str__(self) -> str:
        return str(dict([("X", self.x), ("Y", self.y), ("Rotation", self.rotation), ("Id", self.id), self.extra_properties]))

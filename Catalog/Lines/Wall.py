from Catalog.Catalogue import Catalogue
from Catalog.Lines.Line import Line
from Catalog.Items.Item import Item

class Wall(Line):
    def __init__(self, name: str, x1: float, y1: float, x2: float, y2: float, length: dict) -> None:
        super().__init__(name, x1, y1, x2, y2, length)
        self.link = f"{Catalogue.CATALOG.value} > {Catalogue.WALL.value}" if (Item.count_Ids == 2 or Line.count_Ids == 2) else f"{Catalogue.CATALOG_ALTER.value} > {Catalogue.WALL.value}"

    def set_properties(self, driver):
        super().set_properties(driver)

    def place_line(self, driver):
        super().place_line(driver)
        self.set_properties(driver)

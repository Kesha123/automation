from enum import Enum
from Catalog.Catalogue import Catalogue
from Catalog.Lines.Line import Line
from Catalog.Items.Item import Item
from Palette.Properties import LengthProperty, SelectProperty

from Logger.Logger import Logger

class Wall(Line):
    def __init__(self, name: str, x1: float, y1: float, x2: float, y2: float, length: dict, **kwargs) -> None:
        super().__init__(name, x1, y1, x2, y2, length)
        self.extra_properties = kwargs
        self.link = f"{Catalogue.CATALOG.value} > {Catalogue.WALL.value}" if ((Item.count_items + Line.count_lines == 1)) else f"{Catalogue.CATALOG_ALTER.value} > {Catalogue.WALL.value}"

    def set_properties(self, driver):
        super().set_properties(driver)
        if self.extra_properties:
            if self.extra_properties.get("height"):
                height = LengthProperty("height", ExtraProperties.HEIGHT.value, self.extra_properties.get("height")).set_property(driver)

            if self.extra_properties.get("thickness"):
                thickness = LengthProperty("thickness", ExtraProperties.THICKNESS.value, self.extra_properties.get("thickness")).set_property(driver)

            if self.extra_properties.get("textureA"):
                textureA = SelectProperty("textureA", ExtraProperties.TEXTURE_A.value, self.extra_properties.get("textureA")).set_property(driver)
                
            if self.extra_properties.get("textureB"):
                textureB = SelectProperty("textureB", ExtraProperties.TEXTURE_B.value, self.extra_properties.get("textureB")).set_property(driver)           


    def place_line(self, driver):
        super().place_line(driver)
        self.set_properties(driver)
        Logger.info(f"{self.name} is \033[1mready\033[0m")

    def __str__(self) -> str:
        return super().__str__() + str(self.extra_properties)


class ExtraProperties(Enum):
    HEIGHT = "table.PropertyLengthMeasure:nth-child(3)"
    THICKNESS = "table.PropertyLengthMeasure:nth-child(4)"
    TEXTURE_A = "table.PropertyEnum:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    TEXTURE_B = "table.PropertyEnum:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
from enum import Enum
from Catalog.Catalogue import Catalogue
from Catalog.Lines.Line import Line
from Catalog.Items.Item import Item
from selenium.webdriver.support.ui import Select

class Wall(Line):
    def __init__(self, name: str, x1: float, y1: float, x2: float, y2: float, length: dict, **kwargs) -> None:
        super().__init__(name, x1, y1, x2, y2, length)
        self.extra_properties = kwargs
        self.link = f"{Catalogue.CATALOG.value} > {Catalogue.WALL.value}" if (Item.count_items == 1 or Line.count_lines == 1) else f"{Catalogue.CATALOG_ALTER.value} > {Catalogue.WALL.value}"

    def set_properties(self, driver):
        super().set_properties(driver)
        if self.extra_properties:
            if self.extra_properties.get("height"):
                length = self.extra_properties.get("height").get("length")
                unit = self.extra_properties.get("height").get("_unit")
                field = driver.find_element_by_css_selector(ExtraProperties.HEIGHT.value)
                field.clear()
                field.send_keys(length)

                measurement = Select(driver.find_element_by_css_selector(ExtraProperties.HEIGHT_UNITS.value))
                measurement.select_by_visible_text(unit)

                button = driver.find_element_by_css_selector(ExtraProperties.HEIGHT_BUTTON.value)
                button.click()

            if self.extra_properties.get("thickness"):
                length = self.extra_properties.get("thickness").get("length")
                unit = self.extra_properties.get("thickness").get("_unit")
                field = driver.find_element_by_css_selector(ExtraProperties.THICKNESS.value)
                field.clear()
                field.send_keys(length)

                measurement = Select(driver.find_element_by_css_selector(ExtraProperties.THICKNESS_UNITS.value))
                measurement.select_by_visible_text(unit)

                button = driver.find_element_by_css_selector(ExtraProperties.THICKNESS_BUTTON.value)
                button.click()

            if self.extra_properties.get("textureA"):
                textureA = self.extra_properties.get("textureA")
                field = Select(driver.find_element_by_css_selector(ExtraProperties.TEXTURE_A.value))
                field.select_by_visible_text(textureA)
                
            if self.extra_properties.get("textureB"):
                textureB = self.extra_properties.get("textureB")
                field = Select(driver.find_element_by_css_selector(ExtraProperties.TEXTURE_B.value))
                field.select_by_visible_text(textureB)
            


    def place_line(self, driver):
        super().place_line(driver)
        self.set_properties(driver)


class ExtraProperties(Enum):
    HEIGHT = "table.PropertyLengthMeasure:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    HEIGHT_UNITS = "table.PropertyLengthMeasure:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    HEIGHT_BUTTON = "table.PropertyLengthMeasure:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    THICKNESS = "table.PropertyLengthMeasure:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    THICKNESS_UNITS = "table.PropertyLengthMeasure:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    THICKNESS_BUTTON = "table.PropertyLengthMeasure:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    TEXTURE_A = "table.PropertyEnum:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    TEXTURE_B = "table.PropertyEnum:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
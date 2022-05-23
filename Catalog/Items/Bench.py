from enum import Enum
from Catalogue import Catalogue
from Catalog.Items.Item import Item
from selenium.webdriver.support.ui import Select


class Bench(Item):

    bench_count: int = 1

    def __init__(self, x: float = 500, y: float = 1500, rotation: float = 45, name: str = "bench", **kwargs) -> None:
        super().__init__(x, y, name, rotation)
        self.extra_properties = kwargs
        self.link =  f"{Catalogue.CATALOG.value} > {Catalogue.BENCH.value}" if self.id == 2 else f"{Catalogue.CATALOG_ALTER.value} > {Catalogue.BENCH.value}"

    def set_properties(self, driver) -> None:
        super().set_properties(driver)
        if self.extra_properties.get(ExtraProperties.ALTITUDE.value):
            input_field = driver.find_element_by_css_selector(ExtraProperties.ALTITUDE_INPUT.value)
            input_field.clear()
            input_field.send_keys(self.extra_properties.get(ExtraProperties.ALTITUDE.value).get("length"))

            measurement = Select(driver.find_element_by_css_selector(ExtraProperties.MEASUREMENT.value))
            measurement.select_by_visible_text(self.extra_properties.get(ExtraProperties.ALTITUDE.value).get("unit"))

            button = driver.find_element_by_css_selector(ExtraProperties.BUTTON.value)
            button.click()

    def place_item(self, driver):
        super().place_item(driver)
        self.set_properties(driver)


    def __str__(self) -> str:
        return str(dict([("X", self.x), ("Y", self.y), ("Rotation", self.rotation), ("Id", self.id), self.extra_properties]))


class ExtraProperties(Enum):
    ALTITUDE = "Altitude"
    ALTITUDE_INPUT = ".PropertyLengthMeasure > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    MEASUREMENT = ".PropertyLengthMeasure > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON = ".PropertyLengthMeasure > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"
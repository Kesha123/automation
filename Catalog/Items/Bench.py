from Catalog.Items.Item import Item
from selenium.webdriver.support.ui import Select


class Bench(Item):

    bench_count: int = 1

    def __init__(self, x: float = 500, y: float = 1500, rotation: float = 45, name: str = "bench", **kwargs) -> None:
        super().__init__(x, y, name, rotation)
        self.extra_properties = kwargs
        self.link =  "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(10)" if self.id == 2 else "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(10)"
        
    def set_properties(self, driver) -> None:
        super().set_properties(driver)
        if self.extra_properties.get('Altitude'):
            input_field = driver.find_element_by_css_selector(".PropertyLengthMeasure > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
            input_field.clear()
            input_field.send_keys(self.extra_properties.get("Altitude").get("length"))

            measurement = Select(driver.find_element_by_css_selector(".PropertyLengthMeasure > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"))
            measurement.select_by_visible_text(self.extra_properties.get("Altitude").get("unit"))

            button = driver.find_element_by_css_selector(".PropertyLengthMeasure > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
            button.click()

    def place_item(self, driver):
        super().place_item(driver)
        self.set_properties(driver)


    def __str__(self) -> str:
        return str(dict([("X", self.x), ("Y", self.y), ("Rotation", self.rotation), ("Id", self.id), self.extra_properties]))
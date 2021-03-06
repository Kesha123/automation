from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Property:
    def __init__(self, name: str, link: str, property) -> None:
        self.name = name
        self.link = link
        self.property = property

    def set_property(self, driver: webdriver.Firefox):
        pass


class FieldProperty(Property):
    def __init__(self, name: str, input_field_link: str, property) -> None:
        super().__init__(name, input_field_link, property)

    def set_property(self, driver: webdriver.Firefox) -> None:
        field = driver.find_element_by_css_selector(self.link)
        field.clear()
        field.send_keys(self.property)


class LengthProperty(Property):
    def __init__(self, name: str, link: str, property) -> None:
        super().__init__(name, link, property)

    def set_property(self, driver: webdriver.Firefox):
        super().set_property(driver)

        line = driver.find_element_by_css_selector(self.link)
        input_field = line.find_element_by_tag_name("input")
        input_field.clear()
        input_field.send_keys(self.property.get("length"))

        units = Select(line.find_element_by_tag_name("select"))
        units.select_by_visible_text(self.property.get("unit"))

        button = line.find_element_by_css_selector("td:nth-child(1) > div:nth-child(1) > div:nth-child(2)")

        if button.is_displayed():
            button.click()


class SelectProperty(Property):
    def __init__(self, name: str, link: str, property) -> None:
        super().__init__(name, link, property)

    def set_property(self, driver: webdriver.Firefox):
        super().set_property(driver)
        line = Select(driver.find_element_by_css_selector(self.link))
        line.select_by_visible_text(self.property)


class SubbmitProperty(Property):
    def __init__(self, name: str, link: str, property) -> None:
        super().__init__(name, link, property)

    def set_property(self, driver: webdriver.Firefox):
        super().set_property(driver)

        line = driver.find_element_by_css_selector(self.link)
        input_field = line.find_element_by_tag_name("input")
        input_field.clear()
        input_field.send_keys(self.property)

        button = line.find_element_by_css_selector("td:nth-child(2) > div:nth-child(1) > div:nth-child(2)") 

        if button.is_displayed():
            button.click()
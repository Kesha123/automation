

class Item:
    @staticmethod
    def insert_object_on_layer(driver) -> None:
        element = driver.find_element_by_css_selector("#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)")
        element.click()

    @staticmethod
    def add_object(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()
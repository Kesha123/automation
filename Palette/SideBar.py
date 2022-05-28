from enum import Enum
from Logger.Logger import Logger
from Palette.Properties import FieldProperty, SubbmitProperty
from selenium import webdriver

class SideBarList(Enum):
    GUIDES = ".sidebar > div:nth-child(1)"
    LAYERS = ".sidebar > div:nth-child(2)"
    LAYOUT_ELEMENTS = ".sidebar > div:nth-child(3)"
    GROUPS = ".sidebar > div:nth-child(4)"
    PROPERTIES = ".sidebar > div:nth-child(5)"

    PROPERTIES_BODY = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)"
    ITEM_MAIN_PROPERTIES_BODY = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)"
    LINE_MAIN_PROPERTIES_BODY = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)"
    LAYER_PROPERTY_BODY = "div:nth-child(2) > table:nth-child(3) > tbody:nth-child(1)"


class LayerList(Enum):
    NAME = "tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"
    OPACITY = "tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
    HEIGHT = "tr:nth-child(3) > td:nth-child(2) > div:nth-child(1)"
    ORDER = "tr:nth-child(4) > td:nth-child(2) > div:nth-child(1)"
    SAVE = "tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > button:nth-child(1)"
   

class SideBar:
    @staticmethod
    def open_elements_on_layer(driver) -> None:
        properties = driver.find_element_by_css_selector(SideBarList.LAYOUT_ELEMENTS.value)
        properties.click()    

    @staticmethod
    def count_sidebar_groups_rows(driver) -> int:
        elements_list = driver.find_element_by_css_selector(SideBarList.LAYOUT_ELEMENTS.value).find_elements_by_tag_name("div")

        for index, element in enumerate(elements_list):
            if not element.get_attribute("user-select"):
                elements_list.pop(index)

        return len(elements_list)

    @staticmethod
    def count_layers(driver: webdriver.Firefox):
        layer_table = driver.find_element_by_css_selector(f"{SideBarList.LAYERS.value} > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2)").find_elements_by_tag_name("tr")
        return len(layer_table)

    @staticmethod
    def add_layer(driver: webdriver.Firefox, **kwargs) -> None:
        layers = driver.find_element_by_css_selector(SideBarList.LAYERS.value).click()
        button = driver.find_element_by_css_selector(f"{SideBarList.LAYERS.value} > div:nth-child(2) > p:nth-child(2)").click()
        layer_properties_button = driver.find_element_by_css_selector(f"{SideBarList.LAYERS.value} > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({SideBar.count_layers(driver)}) > td:nth-child(2) > svg:nth-child(1)").click()

        if kwargs.get("name"):
            name = FieldProperty("name",f"{SideBarList.LAYERS.value} > {SideBarList.LAYER_PROPERTY_BODY.value} > {LayerList.NAME.value}",kwargs.get("name")).set_property(driver)
        if kwargs.get("opacity"):
            opacity = FieldProperty("opacity",f"{SideBarList.LAYERS.value} > {SideBarList.LAYER_PROPERTY_BODY.value} > {LayerList.OPACITY.value}",int(kwargs.get("opacity"))).set_property(driver)
        if kwargs.get("height"):
            height = SubbmitProperty("height",f"{SideBarList.LAYERS.value} > {SideBarList.LAYER_PROPERTY_BODY.value} > {LayerList.HEIGHT.value}",kwargs.get("height")).set_property(driver)
        if kwargs.get("order"):
            order = SubbmitProperty("order",f"{SideBarList.LAYERS.value} > {SideBarList.LAYER_PROPERTY_BODY.value} > {LayerList.ORDER.value}",kwargs.get("order")).set_property(driver)

        save = driver.find_element_by_css_selector(f"{SideBarList.LAYERS.value} > {SideBarList.LAYER_PROPERTY_BODY.value} > {LayerList.SAVE.value}").click()

        Logger.info("Layer added successully!!!")

    @staticmethod
    def get_lines_row() -> int:
        return 2

    @staticmethod
    def get_holes_row() -> int:
        return 3

    @staticmethod
    def get_items_row(driver) -> int:
        if SideBar.count_sidebar_groups_rows(driver) >= 4:
            return 4
        else:
            return SideBar.count_sidebar_groups_rows(driver)
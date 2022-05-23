from Palette.ToolBar import ToolBar, ToolBarList
from enum import Enum
from Palette.Layer import Layer
from Palette.SideBar import SideBar, SideBarList


class Item:
    __count_items: int = 0
    count_Ids: int = 1

    def __init__(self, x, y, name, rotation) -> None:
        Item.__count_items += 1
        Item.count_Ids += 1
        self.id = Item.count_Ids
        self.x = x
        self.y = y
        self.rotation = rotation
        self.name = name
        self.link = ""

    def self_choose(self, driver) -> None:
        SideBar.open_elements_on_layer(driver)
        link = f"{SideBarList.LAYOUT_ELEMENTS.value} > div:nth-child(2) > div:nth-child(1) > div:nth-child({SideBar.get_items_row(driver)}) > div:nth-child({self.id})"
        button = driver.find_element_by_css_selector(link)
        button.click()
    
    def set_properties(self, driver) -> None:
        name = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.NAME_SELCTOR.value}")
        name.clear()
        name.send_keys(self.name)

        x = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.X_SELECTOR.value}")
        x.clear()                             
        x.send_keys(0)                    

        y = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.Y_SELECTOR.value}")
        y.clear()
        y.send_keys(0)

        rotation = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.ROTATION_SELECTOR.value}")
        rotation.clear()
        rotation.send_keys(self.rotation)

        button_x = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.BUTTON_X_SELECTOR.value}")
        if button_x.is_displayed():
            button_x.click()
        
        button_y = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.BUTTON_Y_SELECTOR.value}")
        if button_y.is_displayed():
            button_y.click()
        
        button_rotation = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.BUTTON_ROTATION_SELECTOR.value}")
        if button_rotation.is_displayed():
            button_rotation.click()


    def place_item(self, driver):
        ToolBar.open_catalog(driver)
        Item.add_object(driver, self.link)
        Item.insert_object_on_layer(driver)
        self.self_choose(driver)

    @staticmethod
    def insert_object_on_layer(driver) -> None:
        element = driver.find_element_by_css_selector(Layer().link)
        element.click()

    @staticmethod
    def add_object(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()

    @staticmethod
    def open_catalog(driver) -> None:
        catalog = driver.find_element_by_css_selector(ToolBarList.CATALOG.value)
        catalog.click()


class ItemSelectorList(Enum):
    NAME_SELCTOR = "tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"
    X_SELECTOR = "tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    Y_SELECTOR = "tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    ROTATION_SELECTOR = "tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    BUTTON_X_SELECTOR = "tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    BUTTON_Y_SELECTOR = "tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    BUTTON_ROTATION_SELECTOR = "tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"

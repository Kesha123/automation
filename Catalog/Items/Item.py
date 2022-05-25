from Palette.ToolBar import ToolBar
from enum import Enum
from Palette.Layer import Layer
from Palette.SideBar import SideBar, SideBarList
from Palette.Properties import FieldProperty, SubbmitProperty
from Catalog.Counter import Counter
from Logger.Logger import Logger

class Item:
    count_items: int = 0
    count_Ids: int = 1

    def __init__(self, x, y, name, rotation) -> None:
        Logger.info(f"{type(self)} object has been cteated")
        Item.count_items += 1
        Item.count_Ids += 1
        Counter.count += 1
        self.id = Item.count_Ids
        self.number = Item.count_items
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
        name = FieldProperty("name",f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.NAME_SELCTOR.value}",self.name).set_property(driver)
        x = SubbmitProperty("x",f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.X.value}",self.x).set_property(driver)
        y = SubbmitProperty("y",f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.Y.value}",self.y).set_property(driver)
        rotation = SubbmitProperty("rotation",f"{SideBarList.PROPERTIES.value} > {SideBarList.ITEM_MAIN_PROPERTIES_BODY.value} > {ItemSelectorList.ROTATION.value}",self.rotation).set_property(driver)

        Logger.info(f"Main properties for {type(self)} object with \033[1m{self.name}\033[0m name were set")

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


class ItemSelectorList(Enum):
    NAME_SELCTOR = "tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"
    X = "tr:nth-child(2)"
    Y = "tr:nth-child(3)"
    ROTATION = "tr:nth-child(4)"


#.sidebar > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)
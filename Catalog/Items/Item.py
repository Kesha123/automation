from Palette.Palette import ToolBar
from Palette.Layer import Layer
from Palette.Palette import SideBar, SideBarList

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
        link = f"{SideBarList.LAYOUT_ELEMENTS.value} > div:nth-child(2) > div:nth-child(1) > div:nth-child({SideBar.count_sidebar_groups_rows(driver)}) > div:nth-child({self.id})"
        button = driver.find_element_by_css_selector(link)
        button.click()

    
    def set_properties(self, driver) -> None:
        name = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)")
        name.clear()
        name.send_keys(self.name)

        x = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        x.clear()                              
        x.send_keys(self.x)                    

        y = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        y.clear()
        y.send_keys(self.y)

        rotation = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        rotation.clear()
        rotation.send_keys(self.rotation)

        button_x = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
        button_x.click()
        
        button_y = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
        button_y.click()
        
        button_rotation = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
        button_rotation.click()

    def place_bench(self, driver):
        ToolBar.open_catalog(driver)
        Item.add_object(driver, self.link)
        Item.insert_object_on_layer(driver)
        self.self_choose(driver)
        self.set_properties(driver)


    @staticmethod
    def insert_object_on_layer(driver) -> None:
        element = driver.find_element_by_css_selector(Layer().link)
        element.click()

    @staticmethod
    def add_object(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()
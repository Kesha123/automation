from enum import Enum
from Palette.SideBar import SideBar, SideBarList
from Palette.ToolBar import ToolBar, ToolBarList
from Catalog.Lines.Line import Line
from Palette.Properties import FieldProperty, LengthProperty
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from Logger.Logger import Logger
from Catalog.Counter import Counter

class Hole:
    count_holes: int = 0
    count_Ids: int = 1

    def __init__(self, parent: Line, name: str, offset1: dict, offset2: dict, 
                width: dict = {"length":80, "unit":"cm"}, height: dict = {"length":215, "unit":"cm"}, altitude: dict = {"length":0, "unit":"cm"}, thickness: dict = {"length":30, "unit":"cm"}) -> None:
        Logger.info(f"{type(self)} object has been cteated")
        Hole.count_holes += 1
        Hole.count_Ids += 1
        Counter.count += 1
        self.id = Hole.count_Ids
        self.number = Hole.count_holes
        self.parent = parent
        self.name = name
        self.offset1 = offset1
        self.offset2 = offset2
        self.width = width
        self.height = height
        self.altitude = altitude
        self.thickness = thickness
        self.link = ""

    def self_choose(self, driver):
        SideBar.open_elements_on_layer(driver)
        link = f"{SideBarList.LAYOUT_ELEMENTS.value} > div:nth-child(2) > div:nth-child(1) > div:nth-child({SideBar.get_holes_row()}) > div:nth-child({self.id})"
        button = driver.find_element_by_css_selector(link)
        button.click()

    def place_hole(self, driver: webdriver.Firefox):
        ToolBar.open_catalog(driver)
        Hole.add_hole(driver,self.link)
        self.insert_hole_on_layer(driver)
        self.self_choose(driver)

    def set_properties(self, driver: webdriver.Firefox):
        name = FieldProperty("name",HoleSelectorList.NAME.value,self.name).set_property(driver)
        offset1 = LengthProperty("offset1",HoleSelectorList.OFFSET1.value,self.offset1).set_property(driver)
        offset2 = LengthProperty("offset2",f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > {HoleSelectorList.OFFSET2.value}",self.offset2).set_property(driver)
        width = LengthProperty("width",f"{SideBarList.PROPERTIES.value} > {SideBarList.PROPERTIES_BODY.value} > {HoleSelectorList.WIDTH.value}",self.width).set_property(driver)
        height = LengthProperty("height",HoleSelectorList.HEIGHT.value,self.height).set_property(driver)
        altitude = LengthProperty("altitude",HoleSelectorList.ALTITUDE.value,self.altitude).set_property(driver)
        thickness = LengthProperty("thickness",HoleSelectorList.THICKNESS.value,self.thickness).set_property(driver)
        Logger.info(f"Main properties for {type(self)} object with \033[1m{self.name}\033[0m name were set")

    def insert_hole_on_layer(self, driver: webdriver.Firefox) -> None:
        if Line.count_lines == 0:
            return
        else:
            ActionChains(driver).move_to_element(driver.find_element_by_css_selector(f"#svg-drawing-paper > g:nth-child(1) > g:nth-child(3) > g:nth-child({self.parent.number})")).click().send_keys(Keys.ESCAPE).perform()     

    @staticmethod
    def add_hole(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()
    

class HoleSelectorList(Enum):
    NAME = ".PropertyString > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"
    OFFSET1 = "table.PropertyLengthMeasure:nth-child(2)"
    OFFSET2 = "div:nth-child(1) > table:nth-child(3)"  
    WIDTH = "table:nth-child(3)"
    HEIGHT = "table.PropertyLengthMeasure:nth-child(4)"
    ALTITUDE = "table.PropertyLengthMeasure:nth-child(5)"
    THICKNESS = "table.PropertyLengthMeasure:nth-child(6)"

from enum import Enum
import math
from Palette.SideBar import SideBar, SideBarList
from Palette.ToolBar import ToolBar, ToolBarList
from Palette.Layer import Layer
from Palette.Properties import FieldProperty, SubbmitProperty, LengthProperty
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


from Logger.Logger import Logger

class Line:

    count_lines: int = 0
    count_Ids: int = 1

    def __init__(self, name: str, x1: float, y1: float, x2: float, y2: float) -> None:
        Logger.info(f"{type(self)} object has been cteated")
        Line.count_lines += 1
        Line.count_Ids += 1
        self.id = Line.count_Ids
        self.number = Line.count_lines
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = {"length":math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 ), "unit":"cm"}
        self.link = ""

    def self_choose(self, driver):
        SideBar.open_elements_on_layer(driver)
        link = f"{SideBarList.LAYOUT_ELEMENTS.value} > div:nth-child(2) > div:nth-child(1) > div:nth-child({SideBar.get_lines_row()}) > div:nth-child({self.id})"
        button = driver.find_element_by_css_selector(link)
        button.click()

    def place_line(self, driver):
        ToolBar.open_catalog(driver)
        Line.add_line(driver,self.link)
        Line.insert_line_on_layer(driver)
        self.self_choose(driver)

    def set_properties(self, driver):
        name = FieldProperty("name",f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.NAME.value}",self.name).set_property(driver)
        x1 = SubbmitProperty("x1",f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.X1.value}",self.x1).set_property(driver)
        y1 = SubbmitProperty("y1",f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.Y1.value}",self.y1).set_property(driver)
        x2 = SubbmitProperty("x2",f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.X2.value}",self.x2).set_property(driver)
        y2 = SubbmitProperty("y2",f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.Y2.value}",self.y2).set_property(driver)
        length = LengthProperty("length",f"{LineSelectorList.LENGTH.value}",self.length).set_property(driver)
        Logger.info(f"Main properties for {type(self)} object with \033[1m{self.name}\033[0m name were set")

    @staticmethod
    def insert_line_on_layer(driver: webdriver.Firefox) -> None:
        Logger.warning("Line inserting SHOULD me implemented in another way due to harcoding!!! \n\t ***Reminder for me")
        cell1 = driver.find_element_by_css_selector("#svg-drawing-paper > g:nth-child(1) > g:nth-child(1) > g:nth-child(2) > line:nth-child(2)")
        cell2 = driver.find_element_by_css_selector("#svg-drawing-paper > g:nth-child(1) > g:nth-child(1) > g:nth-child(2) > line:nth-child(4)")
        cell1.click()
        ActionChains(driver).move_to_element(cell2).click().send_keys(Keys.ESCAPE).perform()

    @staticmethod
    def add_line(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()

    def __str__(self) -> str:
        return str({"name":self.name,"x1":self.x1,"y1":self.y1,"x2":self.x2,"y2":self.y2,"length":self.length})


class LineSelectorList(Enum):
    NAME = "tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"
    X1 = "tr:nth-child(2)"
    Y1 = "tr:nth-child(3)"
    X2 = "tr:nth-child(4)"
    Y2 = "tr:nth-child(5)"
    LENGTH = "table.PropertyLengthMeasure:nth-child(2)"

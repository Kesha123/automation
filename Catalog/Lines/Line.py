from enum import Enum
from Palette.SideBar import SideBar, SideBarList
from Palette.ToolBar import ToolBar, ToolBarList
from Palette.Layer import Layer
from Palette.Properties import FieldProperty, SubbmitProperty, LengthProperty
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class Line:

    count_lines: int = 0
    count_Ids: int = 1

    def __init__(self, name: str, x1: float, y1: float, x2: float, y2: float, length: dict) -> None:
        Line.count_lines += 1
        Line.count_Ids += 1
        self.id = Line.count_Ids
        self.number = Line.count_lines
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = length
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

    @staticmethod
    def insert_line_on_layer(driver: webdriver.Firefox) -> None:
        element = driver.find_element_by_css_selector(Layer().link)
        element.click()
        ActionChains(driver).move_by_offset(100,100).click().perform()        

    @staticmethod
    def add_line(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()

    @staticmethod
    def open_catalog(driver) -> None:
        catalog = driver.find_element_by_css_selector(ToolBarList.CATALOG.value)
        catalog.click()


class LineSelectorList(Enum):
    NAME = "tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"
    X1 = "tr:nth-child(2)"
    Y1 = "tr:nth-child(3)"
    X2 = "tr:nth-child(4)"
    Y2 = "tr:nth-child(5)"
    LENGTH = "table.PropertyLengthMeasure:nth-child(2)"

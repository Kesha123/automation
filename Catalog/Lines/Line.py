from enum import Enum
from Palette.SideBar import SideBar, SideBarList
from Palette.ToolBar import ToolBar, ToolBarList
from Palette.Layer import Layer

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class Line:

    __count_lines: int = 0
    count_Ids: int = 1

    def __init__(self, name: str, x1: float, y1: float, x2: float, y2: float, length: dict) -> None:
        Line.__count_lines += 1
        Line.count_Ids += 1
        self.id = Line.count_Ids
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
        name = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.NAME.value}")
        name.clear()
        name.send_keys(self.name)

        x1 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.X1.value}")
        x1.clear()
        x1.send_keys(self.x1)
        
        y1 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.Y1.value}")
        y1.clear()
        y1.send_keys(self.y1)
        
        x2 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.X2.value}")
        x2.clear()
        x2.send_keys(self.x2)
        
        y2 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.Y2.value}")
        y2.clear()
        y2.send_keys(self.y2)
        
        length = driver.find_element_by_css_selector(LineSelectorList.LENGTH.value)
        length.clear()
        length.send_keys(self.length.get("length"))

        measurement = Select(driver.find_element_by_css_selector(LineSelectorList.MEASUREMENT.value))
        measurement.select_by_visible_text(self.length.get("unit"))

        button_x1 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.BUTTON_X1.value}")
        if button_x1.is_displayed():
            button_x1.click()

        button_y1 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.BUTTON_Y1.value}")
        if button_y1.is_displayed():
            button_y1.click()

        button_x2 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.BUTTON_X2.value}")
        if button_x2.is_displayed():
            button_x2.click()

        button_y2 = driver.find_element_by_css_selector(f"{SideBarList.PROPERTIES.value} > {SideBarList.LINE_MAIN_PROPERTIES_BODY.value} > {LineSelectorList.BUTTON_Y2.value}")
        if button_y2.is_displayed():
            button_y2.click()

        button_length = driver.find_element_by_css_selector(LineSelectorList.BUTTON_LENGTH.value)
        if button_length.is_displayed():
            button_length.click()


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
    X1 = "tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    Y1 = "tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    X2 = "tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    Y2 = "tr:nth-child(5) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    LENGTH = "table.PropertyLengthMeasure:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    MEASUREMENT = "table.PropertyLengthMeasure:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"

    BUTTON_X1 = "tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    BUTTON_Y1 = "tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    BUTTON_X2 = "tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    BUTTON_Y2 = "tr:nth-child(5) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    BUTTON_LENGTH = "table.PropertyLengthMeasure:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

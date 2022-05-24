from enum import Enum
from Palette.SideBar import SideBar, SideBarList
from Palette.ToolBar import ToolBar, ToolBarList
from Palette.Layer import Layer
from Catalog.Lines.Line import Line

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class Hole:
    count_holes: int = 0
    count_Ids: int = 1

    def __init__(self, parent: Line, name: str, offset1: dict, offset2: dict, 
                width: dict = {"length":80, "unit":"cm"}, height: dict = {"length":215, "unit":"cm"}, altitude: dict = {"length":0, "unit":"cm"}, thickness: dict = {"length":30, "unit":"cm"}) -> None:
        Hole.count_holes += 1
        Hole.count_Ids += 1
        self.id = Hole.count_Ids
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
        name = driver.find_element_by_css_selector(f"{HoleSelectorList.NAME.value}")
        name.clear()
        name.send_keys(self.name)

        offset1 = driver.find_element_by_css_selector(HoleSelectorList.OFFSET1.value)
        offset1.clear()
        offset1.send_keys(self.offset1.get("length"))
        offset1_unit = Select(driver.find_element_by_css_selector(HoleSelectorList.UNIT_OFFSET1.value))
        offset1_unit.select_by_visible_text(self.offset1.get("unit"))        

        offset2 = driver.find_element_by_css_selector(HoleSelectorList.OFFSET2.value)
        offset2.clear()
        offset2.send_keys(self.offset2.get("length"))
        offset2_unit = Select(driver.find_element_by_css_selector(HoleSelectorList.UNIT_OFFSET2.value))
        offset2_unit.select_by_visible_text(self.offset2.get("unit"))

        width = driver.find_element_by_css_selector(HoleSelectorList.WIDTH.value)
        width.clear()
        width.send_keys(self.width.get("length"))
        width_unit = Select(driver.find_element_by_css_selector(HoleSelectorList.UNIT_WIDTH.value))
        width_unit.select_by_visible_text(self.width.get("unit"))

        height = driver.find_element_by_css_selector(HoleSelectorList.HEIGHT.value)
        height.clear()
        height.send_keys(self.height.get("length"))
        height_unit = Select(driver.find_element_by_css_selector(HoleSelectorList.UNIT_HEIGHT.value))
        height_unit.select_by_visible_text(self.height.get("unit"))

        altitude = driver.find_element_by_css_selector(HoleSelectorList.ALTITUDE.value)
        altitude.clear()
        altitude.send_keys(self.altitude.get("length"))
        altitude_unit = Select(driver.find_element_by_css_selector(HoleSelectorList.UNIT_ALTITUDE.value))
        altitude_unit.select_by_visible_text(self.altitude.get("unit"))

        thickness = driver.find_element_by_css_selector(HoleSelectorList.THICKNESS.value)
        thickness.clear()
        thickness.send_keys(self.thickness.get("length"))
        thickness_unit = Select(driver.find_element_by_css_selector(HoleSelectorList.UNIT_THICKNESS.value))
        thickness_unit.select_by_visible_text(self.thickness.get("unit"))

        button_offset1 = driver.find_element_by_css_selector(HoleSelectorList.BUTTON_OFFSET1.value)
        if button_offset1.is_displayed():
            button_offset1.click()

        button_offset2 = driver.find_element_by_css_selector(HoleSelectorList.BUTTON_OFFSET2.value)
        if button_offset2.is_displayed():
            button_offset2.click()

        button_width = driver.find_element_by_css_selector(HoleSelectorList.BUTTON_WIDTH.value)
        if button_width.is_displayed():
            button_width.click()

        button_height = driver.find_element_by_css_selector(HoleSelectorList.BUTTON_HEIGHT.value)
        if button_height.is_displayed():
            button_height.click()

        button_altitude = driver.find_element_by_css_selector(HoleSelectorList.BUTTON_ALTITUDE.value)
        if button_altitude.is_displayed():
            button_altitude.click()

        button_thickness = driver.find_element_by_css_selector(HoleSelectorList.BUTTON_THICKNESS.value)
        if button_thickness.is_displayed():
            button_thickness.click()

    def insert_hole_on_layer(self, driver: webdriver.Firefox) -> None:
        if Line.count_lines == 0:
            return
        else:
            ActionChains(driver).move_to_element(driver.find_element_by_css_selector(f"#svg-drawing-paper > g:nth-child(1) > g:nth-child(3) > g:nth-child({self.parent.number})")).click().perform()     

    @staticmethod
    def add_hole(driver, link) -> None:
        object = driver.find_element_by_css_selector(link)
        object.click()

    @staticmethod
    def open_catalog(driver) -> None:
        catalog = driver.find_element_by_css_selector(ToolBarList.CATALOG.value)
        catalog.click()
    

class HoleSelectorList(Enum):
    NAME = ".PropertyString > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"

    OFFSET1 = "table.PropertyLengthMeasure:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    UNIT_OFFSET1 = "table.PropertyLengthMeasure:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON_OFFSET1 = "table.PropertyLengthMeasure:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    OFFSET2 = ".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    UNIT_OFFSET2 = ".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON_OFFSET2 = ".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    WIDTH = ".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    UNIT_WIDTH = ".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON_WIDTH = ".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    HEIGHT = "table.PropertyLengthMeasure:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    UNIT_HEIGHT = "table.PropertyLengthMeasure:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON_HEIGHT = "table.PropertyLengthMeasure:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    ALTITUDE = "table.PropertyLengthMeasure:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    UNIT_ALTITUDE = "table.PropertyLengthMeasure:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON_ALTITUDE = "table.PropertyLengthMeasure:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"

    THICKNESS = "table.PropertyLengthMeasure:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    UNIT_THICKNESS = "table.PropertyLengthMeasure:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)"
    BUTTON_THICKNESS = "table.PropertyLengthMeasure:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)"


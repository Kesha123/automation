from Catalog.Holes.Hole import Hole
from Catalog.Lines.Line import Line
from Catalog.Catalogue import Catalogue
from selenium import webdriver

class Gate(Hole):
    def __init__(self, parent: Line, name: str, offset1: dict, offset2: dict, 
                 width: dict = {"length":80, "unit":"cm"}, height: dict = {"length":215, "unit":"cm"}, altitude: dict = {"length":0, "unit":"cm"}, thickness: dict = {"length":30, "unit":"cm"}) -> None:
        super().__init__(parent, name, offset1, offset2, width, height, altitude, thickness)
        self.link = f"{Catalogue.CATALOG_ALTER.value} > {Catalogue.GATE.value}"

    def set_properties(self, driver: webdriver.Firefox):
        super().set_properties(driver)

    def place_hole(self, driver):
        super().place_hole(driver)
        self.set_properties(driver)
        
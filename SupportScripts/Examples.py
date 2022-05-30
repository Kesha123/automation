from Palette.ToolBar import ToolBar
from Catalog.Items.Bench import Bench

from ProjectParser.Parser import Parser

from Catalog.Lines.Wall import Wall
from Catalog.Holes.Gate import Gate

class Example:
    @staticmethod
    def items(driver):    
        bench1 = Bench(altitude={'length': 10000, 'unit': 'cm'})
        bench1.place_item(driver)
        bench2 = Bench(0,100,90,"bench2")    
        bench2.place_item(driver)

    @staticmethod
    def lines(driver):
        wall1 = Wall("Wall 1",300,1700,1000,1700, height={"length":999,"unit":"cm"}, thickness={"length":50,"unit":"cm"}, textureA="Painted")
        wall1.place_line(driver)
        wall2 = Wall("Wall 2",100,1000,800,1000, height={"length":999,"unit":"cm"}, thickness={"length":50,"unit":"cm"}, textureA="Painted")
        wall2.place_line(driver)   

    @staticmethod
    def holes(driver):
        wall = Wall("Line 1",300,1700,1000,1700, height={"length":999,"unit":"cm"}, thickness={"length":50,"unit":"cm"}, textureA="Painted")
        wall.place_line(driver)
        gate1 = Gate(wall,"Gate_1",{'length': 10, 'unit': 'cm'},{'length': 0, 'unit': 'cm'})
        gate1.place_hole(driver)
        gate2 = Gate(wall, "Gate2", {"length":220, "unit":"cm"}, {"length":400, "unit":"cm"})
        gate2.place_hole(driver)

    @staticmethod
    def load(driver, project_name="Project1.json"):
        parser = Parser(project_name)
        parser.load_project()
        ToolBar.load_project(driver, parser)

    @staticmethod
    def run(driver):
        Example.items(driver)
        Example.holes(driver)
        Example.lines(driver)

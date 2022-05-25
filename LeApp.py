from Palette.ToolBar import ToolBar
from Catalog.Items.Bench import Bench
from selenium import webdriver

from ProjectParser.Parser import Parser

from Catalog.Lines.Wall import Wall
from Catalog.Holes.Gate import Gate


driver = webdriver.Firefox()
driver.get("https://ainak.gitlab.io/leapp-app/") 
 

def items():
    
    bench1 = Bench(altitude={'length': 10000, 'unit': 'cm'})
    bench1.place_item(driver)

    bench2 = Bench(0,100,90,"bench2")    
    bench2.place_item(driver)


def lines():
    wall1 = Wall("Wall 1",300,1700,1000,1700,{'length':700,'unit':'cm'}, height={"length":999,"unit":"cm"}, thickness={"length":50,"unit":"cm"}, textureA="Painted")
    wall1.place_line(driver)

    wall2 = Wall("Wall 2",100,1000,800,1000,{'length': 700, 'unit': 'cm'}, height={"length":999,"unit":"cm"}, thickness={"length":50,"unit":"cm"}, textureA="Painted")
    wall2.place_line(driver)   


def holes():
    wall = Wall("Line 1",300,1700,1000,1700,{'length': 700, 'unit': 'cm'}, height={"length":999,"unit":"cm"}, thickness={"length":50,"unit":"cm"}, textureA="Painted")
    wall.place_line(driver)

    gate1 = Gate(wall,"Gate_1",{'length': 10, 'unit': 'cm'},{'length': 0, 'unit': 'cm'})
    gate1.place_hole(driver)

    gate2 = Gate(wall, "Gate2", {"length":220, "unit":"cm"}, {"length":400, "unit":"cm"})
    gate2.place_hole(driver)


def load():
    parser = Parser("Project1.json").load_project()
    print(parser)
    ToolBar.load_project(driver, parser)


if __name__ == "__main__":
    holes()
    #lines()
    #items()
    #load()
    

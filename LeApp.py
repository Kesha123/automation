from Palette.ToolBar import ToolBar
from Catalog.Items.Bench import Bench
from selenium import webdriver

from ProjectParser.Parser import Parser

from Catalog.Lines.Wall import Wall


driver = webdriver.Firefox()
driver.get("https://ainak.gitlab.io/leapp-app/") 
 

def items():
    
    bench1 = Bench(Altitude={'length': 10000, 'unit': 'cm'})
    bench1.place_item(driver)

    bench2 = Bench(0,100,90,"bench2")    
    bench2.place_item(driver)    

    ToolBar().save_project(driver)


def lines():
    wall = Wall("Line 1",603.12,1694.03,1110.95,1694.03,{'length': 507.83, 'unit': 'cm'})
    wall.place_line(driver)
    ToolBar().save_project(driver)


def load():
    parser = Parser("Project1.json").load_project()
    print(parser)
    ToolBar.load_project(driver, parser)


if __name__ == "__main__":
    #lines()
    #items()
    load()
    

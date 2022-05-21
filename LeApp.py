from Palette.Palette import ToolBar
from Catalog.Items.Bench import Bench
from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://ainak.gitlab.io/leapp-app/")   
 

def main():
    bench1 = Bench(Altitude={'length': 10000, 'unit': 'cm'})
    bench1.place_item(driver)

    bench2 = Bench(0,100,90,"bench2")    
    bench2.place_item(driver)    

    ToolBar().save_project(driver)


if __name__ == "__main__":
    main()



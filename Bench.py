from Palette import ToolBar, SideBar
from Item import Item

class Bench:

    bench_count: int = 1

    def __init__(self, x: float = 500, y: float = 1500, theta: float = 45, name: str = "bench") -> None:
        Bench.bench_count += 1
        self.id = Bench.bench_count
        self.x = x
        self.y = y
        self.theta = theta
        self.name = name
        self.link =  "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(10)" if self.id == 2 else "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(10)"

    
    def choose(self, driver) -> None:
        SideBar.elements_on_layer(driver)
        link = f".sidebar > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child({SideBar.count_sidebar_rows(driver)}) > div:nth-child({self.id})"
        button = driver.find_element_by_css_selector(link)
        button.click()


    def set_properties(self, driver) -> None:
        name = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)")
        name.clear()
        name.send_keys(self.name)

        x = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        x.clear()
        x.send_keys(self.x)

        y = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        y.clear()
        y.send_keys(self.y)

        rotation = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        rotation.clear()
        rotation.send_keys(self.theta)

        button_x = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
        button_x.click()
        
        button_y = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
        button_y.click()
        
        button_rotation = driver.find_element_by_css_selector(".sidebar > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
        button_rotation.click()


    def place_bench(self, driver):

        ToolBar.open_catalog(driver)

        Item.add_object(driver, self.link)
        Item.insert_object_on_layer(driver)

        self.choose(driver)
        self.set_properties(driver)


    def __str__(self) -> str:
        return str(dict([("X", self.x), ("Y", self.y), ("Rotation", self.theta), ("Id", self.id)]))
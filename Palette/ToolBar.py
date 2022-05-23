import os
from enum import Enum
#from ProjectParser.Parser import Parser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class ToolBarList(Enum):
    NEW_PROJECT = ".toolbar > div:nth-child(1)"
    SAVE_PROJECT = ".toolbar > div:nth-child(2)"
    LOAD_PROJECT = ".toolbar > div:nth-child(3)"
    CATALOG = ".toolbar > div:nth-child(4)"
    V_VIEW = ".toolbar > div:nth-child(5)"
    L_VIEW = ".toolbar > div:nth-child(6)"
    WALK = ".toolbar > div:nth-child(7)"
    UNDO = ".toolbar > div:nth-child(8)"
    CONFIG_PROJECT = ".toolbar > div:nth-child(9)"
    SNAPSHOT = ".toolbar > div:nth-child(10)"


class ToolBar:
    @staticmethod
    def open_catalog(driver) -> None:
        catalog = driver.find_element_by_css_selector(ToolBarList.CATALOG.value)
        catalog.click()

    @staticmethod
    def save_project(driver, path: str =".", project_name: str = "Project") -> None:
        button = driver.find_element_by_css_selector(ToolBarList.SAVE_PROJECT.value)
        button.click()

        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            save_alert = driver.switch_to.alert
            save_alert.send_keys(f"{project_name}.json")
            save_alert.accept()
        except TimeoutException:
            pass

        PATH = os.path.expanduser("~")
        os.replace(f"{PATH}/Загрузки/{project_name}.json", f"{path}/{project_name}.json")

    """
    @staticmethod
    def load_project(driver, path: str = "Project.json") -> None:
        parser = Parser(path).load_project().items()
    
        for layer in parser:
            items = layer[1].get("items")
            for item in items:
               item.place_item(driver)
    """
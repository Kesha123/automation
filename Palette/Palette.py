import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from enum import Enum

class ToolBarList(Enum):
    NEW_PROJECT = ".toolbar > div:nth-child(1)"
    SAVE_PROJECT = ".toolbar > div:nth-child(2)"
    LOAD_PROJECT = ".toolbar > div:nth-child(3)"
    CATALOGUE = ".toolbar > div:nth-child(4)"
    V_VIEW = ".toolbar > div:nth-child(5)"
    L_VIEW = ".toolbar > div:nth-child(6)"
    WALK = ".toolbar > div:nth-child(7)"
    UNDO = ".toolbar > div:nth-child(8)"
    CONFIG_PROJECT = ".toolbar > div:nth-child(9)"
    SNAPSHOT = ".toolbar > div:nth-child(10)"


class SideBarList(Enum):
    GUIDES = ".sidebar > div:nth-child(1)"
    LAYERS = ".sidebar > div:nth-child(2)"
    LAYOUT_ELEMENTS = ".sidebar > div:nth-child(3)"
    GROUPS = ".sidebar > div:nth-child(4)"
    PROPERTIES = ".sidebar > div:nth-child(5)"

    PROPERTIES_BODY = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)"

class ToolBar:
    @staticmethod
    def open_catalog(driver) -> None:
        catalog = driver.find_element_by_css_selector(ToolBarList.CATALOGUE.value)
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


class SideBar:
    @staticmethod
    def open_elements_on_layer(driver) -> None:
        properties = driver.find_element_by_css_selector(SideBarList.LAYOUT_ELEMENTS.value)
        properties.click()    

    @staticmethod
    def count_sidebar_groups_rows(driver) -> int:
        elements_list = driver.find_element_by_css_selector(SideBarList.LAYOUT_ELEMENTS.value).find_elements_by_tag_name("div")

        for index, element in enumerate(elements_list):
            if not element.get_attribute("user-select"):
                elements_list.pop(index)

        return len(elements_list)

    @staticmethod
    def get_lines_row() -> int:
        return 2

    @staticmethod
    def get_holes_row(driver) -> int:
        if SideBar.count_sidebar_groups_rows(driver) < 4:
            return None
        else:
            return SideBar.count_sidebar_groups_rows(driver) - 1

    @staticmethod
    def get_items_row(driver) -> int:
        return SideBar.count_sidebar_groups_rows(driver)

    

    
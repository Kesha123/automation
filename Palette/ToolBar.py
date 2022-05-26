import os
import platform
from enum import Enum
from posixpath import split
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from Logger.Logger import Logger


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

        download = "Загрузки"

        match platform.system():
            case "Linux":
                PATH = os.path.expanduser("~")
                try:
                    os.replace(f"{PATH}/{download}/{project_name}.json", f"{path}/{project_name}.json")
                    Logger.debug(f"Project saved successfully in {path}/{project_name}.json")
                except FileNotFoundError as ex:
                    Logger.error(f"Error occured while saving the file:\n\t{ex}")
            case "Windows":
                Logger.warning(f"Saving on {platform.system()} pcs hasn't been implemented so far due to ...")
                pass 
            case "Darwin":
                Logger.warning(f"Saving on {platform.system()} pcs hasn't been implemented so far due to ...")
                pass
            case _:
                Logger.warning("can not decet your os!")

    @staticmethod
    def load_project(driver, parser) -> None:
        Logger.warning("Project uploading is not implemented")

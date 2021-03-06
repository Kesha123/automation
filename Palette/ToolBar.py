import os
import platform
from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import configparser

from Logger.Logger import Logger
from Palette.SideBar import SideBar


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

        config = configparser.ConfigParser()
        config.read("config.env")
        download = config.get("DOWNLOAD","DOWNLOAD_DIR")

        match platform.system():
            case "Linux":
                PATH = os.path.expanduser("~")
                try:
                    os.replace(f"{PATH}/{download}/{project_name}.json", f"{path}/{project_name}.json")
                    Logger.debug(f"Project saved successfully in {path}/{project_name}.json")
                except FileNotFoundError as ex:
                    Logger.error(f"Error occured while saving the file:\n\t{ex}. \n\n You can try to change the download directory in config.env.")
            case "Windows":
                Logger.warning(f"Saving on {platform.system()} pcs hasn't been implemented so far due to ...")
                pass 
            case "Darwin":
                Logger.warning(f"Saving on {platform.system()} pcs hasn't been implemented so far due to ...")
                pass
            case _:
                Logger.warning("Can not detect your os!")

    @staticmethod
    def load_project(driver, parser) -> None:        
        for layer in parser.layers.items():
            SideBar.add_layer(driver,**layer[1].get("properties"))

            for line in layer[1].get("lines").items():
                line[1].place_line(driver)

            for hole in layer[1].get("holes"):
                hole.place_hole(driver)

            for item in layer[1].get("items"):
                item.place_item(driver)

            Logger.debug(f"Layer {layer[0]} is ready with:\n\n\t\t{len(layer[1]['lines'].items())} - lines;\n\t\t{len(layer[1]['holes'])} - holes;\n\t\t{len(layer[1]['items'])} - items;")

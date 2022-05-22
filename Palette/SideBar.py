from enum import Enum


class SideBarList(Enum):
    GUIDES = ".sidebar > div:nth-child(1)"
    LAYERS = ".sidebar > div:nth-child(2)"
    LAYOUT_ELEMENTS = ".sidebar > div:nth-child(3)"
    GROUPS = ".sidebar > div:nth-child(4)"
    PROPERTIES = ".sidebar > div:nth-child(5)"

    PROPERTIES_BODY = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)"
    MAIN_PROPERTIES_BODY = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)"
    

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
import sys
import getopt

from Logger.Logger import Logger
from Palette.ToolBar import ToolBar
from selenium import webdriver
from ProjectParser.Parser import Parser


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:i:e:")
    except getopt.GetoptError as ex:
        Logger.error(f"You provided unsupportde option:\n\t{ex.msg}")
        return

    driver = webdriver.Firefox()
    driver.get("https://ainak.gitlab.io/leapp-app/") 

    for option, argument in opts:    
        if ('-f') in option:
            parser = Parser(argument)
            parser.load_project()
            ToolBar.load_project(driver, parser)
        if ("-i") in option:
            Logger.warning("Interactive mode is not implemented. Need more ideas for that.")
        if ("-e") in option:
            Logger.info("Go to SupportScripts and run Examples.py. I'll implement it a bit later, gonna go support Finland today's hockey match!")


if __name__ == "__main__":
    main()
    

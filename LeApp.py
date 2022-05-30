import sys
import getopt

from Logger.Logger import Logger
from Palette.ToolBar import ToolBar
from selenium import webdriver
from ProjectParser.Parser import Parser




def main():
    
    arguments = sys.argv.copy()
    for index, arg in enumerate(sys.argv):
        if arg == '-h' or arg == '-e' or arg == '-i':
            arguments.insert(index+1, ' ')

    try:
        opts, args = getopt.getopt(arguments[1:], "h:f:i:e:")
    except getopt.GetoptError as ex:
        Logger.error(f"You provided unsupportde option:\n\t{ex.msg}")
        return


    for option, argument in opts:
        if ('-h') in option:
            Logger.info("You are usnig LeApp.\n\n\t -f <filename>.json - to load project from the file. \n\t -i - interactive mode. \n\t -e - to run examples.\n")
        if ('-f') in option:
            driver = webdriver.Firefox()
            driver.get("https://ainak.gitlab.io/leapp-app/") 
            parser = Parser(argument)
            parser.load_project()
            ToolBar.load_project(driver, parser)
        if ("-i") in option:
            Logger.warning("Interactive mode is not implemented. Need more ideas for that.")
        if ("-e") in option:
            Logger.warning("Go to SupportScripts and run Examples.py. I'll implement it a bit later, gonna go support Finland today's hockey match!")


if __name__ == "__main__":
    main()
    
